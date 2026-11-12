// Fabrique une page autonome (sans serveur) avec les chiffres du moment, pour un lien claude.ai.
// Usage : node snapshot.js <fichier-de-sortie>   (le serveur doit tourner sur PORT)
import { readFile, writeFile } from "node:fs/promises";
const port = process.env.PORT || 3000, out = process.argv[2] || "snapshot.html";
const data = await (await fetch(`http://localhost:${port}/api/stats`)).json();
let html = await readFile(new URL("./public/index.html", import.meta.url), "utf8");
// la page publiée est enveloppée automatiquement : on retire doctype, html, head et body
html = html.replace(/<!doctype html>\s*<html[^>]*>\s*<head>\s*/i, "").replace(/<meta charset[^>]*>\s*<meta name="viewport"[^>]*>\s*/i, "")
  .replace(/<\/head>\s*<body>\s*/i, "").replace(/<\/body>\s*<\/html>\s*$/i, "");
html = html.replace("<script>\n/* ====", `<script>window.__SNAPSHOT__ = ${JSON.stringify(data).replace(/</g, "\\u003c")};</script>\n<script>\n/* ====`);
await writeFile(out, html);
console.log(`Instantané écrit : ${out}`);
