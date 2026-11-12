// Nuvéa Monde : petit serveur sans dépendance.
// Lit Stripe en lecture seule et sert le dashboard 3D. La clé vient uniquement de .env.
import http from "node:http";
import { readFile } from "node:fs/promises";
import { readFileSync, existsSync } from "node:fs";
import { extname, join, normalize } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = fileURLToPath(new URL(".", import.meta.url));

// --- .env minimal (pas de dépendance) ---
const envPath = join(ROOT, ".env");
if (existsSync(envPath)) {
  for (const line of readFileSync(envPath, "utf8").split("\n")) {
    const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*)\s*$/);
    if (m && !(m[1] in process.env)) process.env[m[1]] = m[2].replace(/^["']|["']$/g, "");
  }
}
const KEY = process.env.STRIPE_API_KEY;
const PORT = Number(process.env.PORT || 3000);
const REFRESH = Number(process.env.REFRESH_SECONDS || 60);
const TZ = process.env.TIMEZONE || "Europe/Paris";
const SIO_KEY = process.env.SYSTEMEIO_API_KEY;
if (!KEY) { console.error("STRIPE_API_KEY manquante dans .env"); process.exit(1); }

// --- Stripe ---
const ZERO_DECIMAL = new Set(["bif","clp","djf","gnf","jpy","kmf","krw","mga","pyg","rwf","ugx","vnd","vuv","xaf","xof","xpf"]);
const major = (amount, cur) => ZERO_DECIMAL.has(cur) ? amount : amount / 100;

async function stripeGet(path, params = {}) {
  const qs = new URLSearchParams();
  for (const [k, v] of Object.entries(params)) [].concat(v).forEach(x => qs.append(k, String(x)));
  const res = await fetch(`https://api.stripe.com${path}?${qs}`, {
    headers: { Authorization: `Bearer ${KEY}`, "Stripe-Version": "2024-06-20" }
  });
  const body = await res.json().catch(() => ({}));
  if (!res.ok) {
    const err = new Error(body?.error?.message || `HTTP ${res.status}`);
    err.status = res.status; throw err;
  }
  return body;
}
async function listAll(path, params = {}, max = 1000) {
  const out = []; let starting_after;
  while (out.length < max) {
    const page = await stripeGet(path, { limit: 100, ...params, ...(starting_after ? { starting_after } : {}) });
    out.push(...page.data);
    if (!page.has_more || !page.data.length) break;
    starting_after = page.data[page.data.length - 1].id;
  }
  return out;
}
// Exécute une section ; une permission manquante ne casse pas le reste.
async function section(fn) {
  try { return { ok: true, ...(await fn()) }; }
  catch (e) { return { ok: false, error: e.status === 401 || e.status === 403 ? "Accès refusé par la clé" : e.message }; }
}

async function collect() {
  const now = Math.floor(Date.now() / 1000), since = now - 30 * 86400;
  const range = { "created[gte]": since };

  const [account, charges, intents, sessions, products, balance] = await Promise.all([
    section(async () => {
      const a = await stripeGet("/v1/account");
      return { name: a.business_profile?.name || a.settings?.dashboard?.display_name || a.email || a.id,
        charges_enabled: !!a.charges_enabled, payouts_enabled: !!a.payouts_enabled, currency: a.default_currency };
    }),
    section(async () => {
      const all = await listAll("/v1/charges", range);
      const ok = all.filter(c => c.status === "succeeded" && c.paid);
      const cur = mostCommon(ok.map(c => c.currency)) || mostCommon(all.map(c => c.currency));
      const inCur = ok.filter(c => c.currency === cur);
      const who = new Set(inCur.map(c => c.customer || c.billing_details?.email || c.receipt_email || c.payment_method_details?.card?.fingerprint).filter(Boolean));
      const gross = inCur.reduce((s, c) => s + c.amount, 0);
      const refunded = inCur.reduce((s, c) => s + c.amount_refunded, 0);
      // CA jour par jour (heure de Paris) et clients par moment de la journée.
      const dayKey = ts => new Intl.DateTimeFormat("fr-CA", { timeZone: TZ, year: "numeric", month: "2-digit", day: "2-digit" }).format(new Date(ts * 1000));
      const hourOf = ts => Number(new Intl.DateTimeFormat("fr-FR", { timeZone: TZ, hour: "2-digit", hourCycle: "h23" }).format(new Date(ts * 1000)));
      const days = [];
      for (let i = 29; i >= 0; i--) days.push({ date: dayKey(now - i * 86400), amount: 0, count: 0 });
      const idx = new Map(days.map((d, i) => [d.date, i]));
      const moments = { matin: 0, midi: 0, soir: 0 };
      for (const c of inCur) {
        const i = idx.get(dayKey(c.created));
        if (i !== undefined) { days[i].amount += major(c.amount, cur); days[i].count++; }
        const h = hourOf(c.created);
        moments[h < 12 ? "matin" : h < 14 ? "midi" : "soir"]++;
      }
      const active = days.filter(d => d.count);
      const best = active.length ? active.reduce((a, b) => (b.amount > a.amount ? b : a)) : null;
      const calm = active.length ? active.reduce((a, b) => (b.amount < a.amount ? b : a)) : null;
      return { currency: cur || null, count: inCur.length, customers: who.size, days, best, calm, moments,
        gross: major(gross, cur), refunded: major(refunded, cur), net: major(gross - refunded, cur),
        avg: inCur.length ? major(gross / inCur.length, cur) : null,
        pending: all.filter(c => c.status === "pending").length,
        failed: all.filter(c => c.status === "failed").length,
        otherCurrencies: [...new Set(ok.map(c => c.currency))].filter(c => c !== cur) };
    }),
    section(async () => {
      const all = await listAll("/v1/payment_intents", range);
      return { inProgress: all.filter(p => ["processing", "requires_capture", "requires_action"].includes(p.status)).length,
        abandoned: all.filter(p => p.status === "requires_payment_method" || p.status === "canceled").length };
    }),
    section(async () => {
      const all = await listAll("/v1/checkout/sessions", { ...range, "expand[]": "data.line_items" }, 500);
      const done = all.filter(s => s.status === "complete");
      const byProduct = new Map();
      for (const s of done) for (const li of s.line_items?.data || []) {
        const k = li.description || li.price?.product || "Produit";
        const p = byProduct.get(k) || { name: k, qty: 0, revenue: 0, currency: li.currency };
        p.qty += li.quantity || 0; p.revenue += major(li.amount_total || 0, li.currency);
        byProduct.set(k, p);
      }
      return { created: all.length, completed: done.length, open: all.filter(s => s.status === "open").length,
        expired: all.filter(s => s.status === "expired").length,
        top: [...byProduct.values()].sort((a, b) => b.revenue - a.revenue || b.qty - a.qty).slice(0, 5) };
    }),
    section(async () => {
      const all = await listAll("/v1/products", { active: true }, 300);
      // Stripe ne gère pas de stock : on lit metadata.stock si tu l'as rempli.
      const withStock = all.filter(p => p.metadata?.stock !== undefined);
      return { active: all.length,
        stock: withStock.length ? withStock.reduce((s, p) => s + (Number(p.metadata.stock) || 0), 0) : null,
        tracked: withStock.length };
    }),
    section(async () => {
      const b = await stripeGet("/v1/balance");
      const sum = arr => arr.reduce((s, x) => s + major(x.amount, x.currency), 0);
      return { available: sum(b.available || []), pending: sum(b.pending || []), currency: b.available?.[0]?.currency || null };
    })
  ]);

  const [systeme, budget] = await Promise.all([section(() => readSystemeIo(since)), section(readBudget)]);

  return { fetchedAt: new Date().toISOString(), periodStart: new Date(since * 1000).toISOString(),
    refreshSeconds: REFRESH, account, charges, intents, sessions, products, balance, systeme, budget };
}

// --- systeme.io (lecture seule) ---
async function sioGet(path, params = {}) {
  if (!SIO_KEY) { const e = new Error("Clé systeme.io absente du .env"); e.status = 0; throw e; }
  const res = await fetch(`https://api.systeme.io/api${path}?${new URLSearchParams(params)}`, {
    headers: { "X-API-Key": SIO_KEY, Accept: "application/json" }
  });
  const body = await res.json().catch(() => ({}));
  if (!res.ok) { const e = new Error(body.detail || `HTTP ${res.status}`); e.status = res.status; throw e; }
  return body;
}
async function sioAll(path, max = 2000) {
  const out = []; let startingAfter;
  while (out.length < max) {
    const page = await sioGet(path, { limit: 100, ...(startingAfter ? { startingAfter } : {}) });
    const items = page.items || [];
    out.push(...items);
    if (!page.hasMore || !items.length) break;
    startingAfter = items[items.length - 1].id;
  }
  return out;
}
async function readSystemeIo(since) {
  const contacts = await sioAll("/contacts");
  const tagNames = c => (c.tags || []).map(t => (t.name || "").toUpperCase());
  const recent = contacts.filter(c => c.registeredAt && Date.parse(c.registeredAt) / 1000 >= since);
  const clients = contacts.filter(c => tagNames(c).includes("CLIENT"));
  const optional = async (p) => { try { const r = await sioGet(p, { limit: 100 }); return (r.items || []).length; } catch { return null; } };
  const [courses, funnels] = await Promise.all([optional("/school/courses"), optional("/funnels")]);
  return { contacts: contacts.length, newContacts: recent.length, clients: clients.length,
    newClients: clients.filter(c => recent.includes(c)).length, courses, funnels };
}

// --- Budget perso : data/budget.json (jamais envoyé sur GitHub) ---
async function readBudget() {
  const b = JSON.parse(await readFile(join(ROOT, "data", "budget.json"), "utf8"));
  const known = Object.entries(b.charges || {}).filter(([, v]) => typeof v === "number");
  const missing = Object.entries(b.charges || {}).filter(([, v]) => typeof v !== "number").map(([k]) => k);
  const chargesTotal = missing.length ? null : known.reduce((s, [, v]) => s + v, 0);
  // Prochaine paie (heure de Paris)
  const today = new Date(new Intl.DateTimeFormat("en-CA", { timeZone: TZ }).format(new Date()) + "T12:00:00");
  let pay = new Date(today.getFullYear(), today.getMonth(), b.jourDePaie, 12);
  if (pay < today) pay = new Date(today.getFullYear(), today.getMonth() + 1, b.jourDePaie, 12);
  const daysToPay = Math.round((pay - today) / 86400000);
  // Projection mois par mois jusqu'à finProjection, si toutes les charges sont connues
  let projection = null;
  if (chargesTotal !== null) {
    projection = []; let compte = b.compteCourant, epargne = b.epargne;
    const [ey, em] = b.finProjection.split("-").map(Number);
    for (let d = new Date(pay); d.getFullYear() * 12 + d.getMonth() <= ey * 12 + em - 1; d = new Date(d.getFullYear(), d.getMonth() + 1, b.jourDePaie, 12)) {
      compte += b.salaire - chargesTotal;
      let used = 0;
      if (compte < 0) { used = Math.min(epargne, -compte); epargne -= used; compte += used; }
      projection.push({ mois: d.toLocaleDateString("fr-FR", { month: "long", year: "numeric" }), salaire: b.salaire, charges: chargesTotal,
        reste: b.salaire - chargesTotal, epargneUtilisee: used, compte, epargne });
    }
  }
  return { source: b.source, compteCourant: b.compteCourant, epargne: b.epargne, salaire: b.salaire,
    jourDePaie: b.jourDePaie, nextPay: pay.toISOString().slice(0, 10), daysToPay,
    charges: Object.fromEntries(known), missing, chargesTotal,
    resteAVivre: chargesTotal === null ? null : b.salaire - chargesTotal, projection };
}
function mostCommon(arr) {
  const m = new Map(); arr.forEach(x => m.set(x, (m.get(x) || 0) + 1));
  return [...m.entries()].sort((a, b) => b[1] - a[1])[0]?.[0];
}

// Cache : Stripe est interrogé au plus une fois par période de rafraîchissement.
let cache = null, cacheAt = 0, inflight = null;
async function stats() {
  if (cache && Date.now() - cacheAt < (REFRESH - 5) * 1000) return cache;
  if (!inflight) inflight = collect().then(d => { cache = d; cacheAt = Date.now(); return d; }).finally(() => { inflight = null; });
  return inflight;
}

// --- HTTP ---
const TYPES = { ".html": "text/html; charset=utf-8", ".js": "text/javascript", ".css": "text/css", ".svg": "image/svg+xml", ".png": "image/png" };
const PUBLIC = join(ROOT, "public");
http.createServer(async (req, res) => {
  const url = new URL(req.url, "http://x");
  try {
    if (url.pathname === "/api/stats") {
      const data = await stats();
      res.writeHead(200, { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" });
      return res.end(JSON.stringify(data));
    }
    const file = normalize(join(PUBLIC, url.pathname === "/" ? "index.html" : url.pathname));
    if (!file.startsWith(PUBLIC)) { res.writeHead(403); return res.end(); }
    const body = await readFile(file);
    res.writeHead(200, { "Content-Type": TYPES[extname(file)] || "application/octet-stream" });
    res.end(body);
  } catch (e) {
    res.writeHead(e.code === "ENOENT" ? 404 : 500, { "Content-Type": "text/plain; charset=utf-8" });
    res.end(e.code === "ENOENT" ? "Introuvable" : "Erreur serveur");
  }
}).listen(PORT, "0.0.0.0", () => console.log(`Nuvéa Monde : http://localhost:${PORT}  (Stripe relu toutes les ${REFRESH} s)`));
