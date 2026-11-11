#!/usr/bin/env python3
"""Quentia - série « dynamique » : 5 films très différents (couleur, musique, typo, transitions),
coupes calées sur les temps de la musique, photos, ressorts, flou de mouvement sur les impacts, -14 LUFS.
Usage: dyn.py OUT_DIR FILM [--frames t1,t2]    FILM in telegram|sansdepot|zero|fiable|formation"""
import math, sys, subprocess, json
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = Path(__file__).parent; STOCK = HERE.parent / "stock"
OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True); FILM = sys.argv[2]
import os
W, H = (1080, 1920) if os.environ.get("VERT") else (1920, 1080); FPS, SR = 30, 44100; V = W < H
FI, CX = "/usr/share/fonts/opentype/inter/", "/usr/share/fonts/truetype/crosextra/"
_fc = {}
def F(path, size):
    k = (path, size)
    if k not in _fc: _fc[k] = ImageFont.truetype(path, size)
    return _fc[k]
def hexc(h): h = h.lstrip("#"); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
def clamp(x): return min(max(x, 0.0), 1.0)
def spring(x, z=1.0, w=11.0):
    """Amorti critique : arrive en douceur, ne dépasse jamais (pas de rebond)."""
    if x <= 0: return 0.0
    return 1 - math.exp(-w * x) * (1 + w * x)
def oexpo(t): t = clamp(t); return 1.0 if t >= 1 else 1 - 2 ** (-10 * t)

# ================================================================ les 5 films
R, OK = "#FF4B4B", None
FILMS = {
 "telegram": dict(bg="#05070F", acc="#2F6BFF", acc2="#8FB0FF", font=FI + "InterDisplay-Black.otf", upper=True, music="m400", trans=["flash", "glitch"],
   shots=[("slam", 2, "Tu veux apprendre le trading ?"), ("phone", 6, None), ("stamp", 1, "STOP."),
          ("split", 8, [("Signaux d'achat", "Une vraie méthode"), ("Promesses de gains", "Aucune promesse"), ("Dépôt chez un courtier", "Aucun dépôt requis")]),
          ("photo", 2, ("p1", "Apprends. Vraiment.")), ("end", 4, None)]),
 "sansdepot": dict(bg="#03100B", acc="#19D38B", acc2="#9BF5CF", font=FI + "InterDisplay-Bold.otf", upper=False, music="m623", trans=["zoomblur", "whip"],
   shots=[("count", 2, ("0 €", "à déposer chez un courtier.")), ("photo", 1, ("p5", "Pas de compte à ouvrir.")), ("photo", 1, ("p9", "Pas de dépôt.")),
          ("photo", 1, ("p48", "Pas de pression.")), ("photo", 1, ("p2", "Juste apprendre.")), ("stamp", 2, "SANS DÉPÔT"),
          ("check", 8, ["Apprends à ton rythme", "Entraîne-toi sur des exemples fictifs", "Plan de trade, journal, IA coach", "Tu décides quand passer au réel"]),
          ("photo", 4, ("p202", "Ton chemin. Ton rythme.")), ("end", 6, None)]),
 "zero": dict(bg="#0B0414", acc="#B45CFF", acc2="#E2B8FF", font=FI + "InterDisplay-BlackItalic.otf", upper=True, music="m175", trans=["glitch", "cut"],
   shots=[("count", 3, ("0", "promesse de gains.")), ("strike", 2, "Pas de Lambo."), ("strike", 2, "Pas de « +1000 % »."), ("strike", 2, "Pas de captures de gains."),
          ("strike", 2, "Pas de « libre en 30 jours »."), ("slam", 2, "Juste une méthode."), ("photo", 4, ("p43", "Plan. Risque. Journal.")),
          ("grid", 6, ["Bases", "Risque", "IA coach", "Journal", "Psychologie", "Méthode", "Études de cas", "Prompts", "Quiz", "Exercices", "Glossaire", "Plan de trade"]),
          ("end", 7, None)]),
 "fiable": dict(bg="#0E0A02", acc="#FFB020", acc2="#FFE0A0", font=CX + "Caladea-Bold.ttf", upper=False, music="m729", trans=["iris", "flash"],
   shots=[("slam", 2, "Comment reconnaître"), ("slam", 2, "une formation fiable ?"),
          ("check", 8, ["Aucune promesse de gains", "Aucun dépôt exigé chez un courtier", "Avertissement de risque clair", "Formateur qui trade en argent réel"]),
          ("photo", 3, ("p60", "Quentia coche tout.")), ("seal", 4, "PÉDAGOGIQUE · TRANSPARENT · SANS DÉPÔT · "), ("end", 6, None)]),
 "formation": dict(bg="#120804", acc="#FF6A24", acc2="#FFB089", font=FI + "InterDisplay-ExtraBold.otf", upper=False, music="m126", trans=["whip", "scale"],
   shots=[("slam", 2, "Tout pour apprendre"), ("slam", 2, "à trader avec l'IA."),
          ("cards", 6, ["Les bases", "Le risque", "L'IA coach", "Le journal", "La psychologie", "La méthode"]),
          ("slam", 2, "+ prompts IA, quiz, journal Excel"), ("stamp", 2, "Et ça grandit."), ("photo", 2, ("p180", "Ta formation. Ton rythme.")), ("end", 5, None)]),
}
CF = json.loads(Path(FILM).read_text()) if FILM.endswith(".json") else FILMS[FILM]; FILM = Path(FILM).stem; BG, ACC, ACC2 = hexc(CF["bg"]), hexc(CF["acc"]), hexc(CF["acc2"]); WHITE = (246, 244, 240); MUT = (160, 160, 170)
FD = CF["font"]; UI, UIB = FI + "Inter-Medium.otf", FI + "Inter-Bold.otf"

# ================================================================ musique : tempo, temps, extrait
def load(p, sr=SR):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(p), "-ac", "2", "-ar", str(sr), "-f", "s16le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32).reshape(-1, 2) / 32768
song = load(STOCK / f"{CF['music']}.mp3"); mono = song.mean(1)
hop = 512; nfr = len(mono) // hop
env = np.sqrt((mono[:nfr * hop].reshape(nfr, hop) ** 2).mean(1)); efps = SR / hop
on = np.maximum(0, np.diff(env, prepend=env[0]))
ac = np.correlate(on - on.mean(), on - on.mean(), "full")[nfr - 1:]
lags = np.arange(len(ac)) / efps; m = (lags > 60 / 170) & (lags < 60 / 85)
BEAT = lags[m][np.argmax(ac[m])]
CF["shots"] = [list(x) for x in CF["shots"]]
_k = 0
MINDUR = float(os.environ.get("MINDUR", "10.5"))
_POOL = [["MODULE 01", "Les bases", ["Comment fonctionne un marché", "Le vocabulaire, sans jargon"], "p0"],
         ["MODULE 02", "Le risque", ["Ta perte max, fixée avant d'entrer", "La taille de ta position"], "p175"],
         ["MODULE 03", "L'IA comme coach", ["Des prompts pour apprendre", "Jamais pour prédire le marché"], "p3"],
         ["MODULE 04", "Le journal", ["Noter chaque position", "Repérer tes erreurs"], "p24"],
         ["MODULE 05", "La psychologie", ["La peur de rater (FOMO)", "Le trade de revanche"], "p259"],
         ["MODULE 06", "La méthode", ["Une routine en 4 étapes", "Qui se répète à chaque séance"], "p60"],
         ["BONUS", "Études de cas", ["Des situations analysées", "Pas à pas"], "p43"],
         ["MODULE 00", "Bienvenue", ["Comment suivre la formation", "Ce qu'elle ne promet pas"], "p1"]]
_seed = sum(map(ord, FILM)); _j = 0
while sum(x[1] for x in CF["shots"]) * BEAT < MINDUR and _j < 8:
    _have = {x[2][1] for x in CF["shots"] if x[0] == "module"}
    _cand = [m for m in _POOL if m[1] not in _have] or _POOL
    CF["shots"].insert(len(CF["shots"]) - 1, ["module", max(4, int(round(2.6 / BEAT))), _cand[(_seed + _j) % len(_cand)]]); _j += 1
while sum(x[1] for x in CF["shots"]) * BEAT < MINDUR:
    CF["shots"][_k % len(CF["shots"])][1] += 1; _k += 1
NB = sum(s[1] for s in CF["shots"]); DUR = NB * BEAT
sm = np.convolve(env, np.ones(int(efps)) / int(efps), "same"); wn = int((DUR + 1) * efps)
best = max(range(int(4 * efps), nfr - wn), key=lambda i: sm[i:i + wn].mean()) / efps
ph = np.arange(0, BEAT, 1 / efps)  # phase des temps : celle qui tombe le plus sur les attaques
phase = max(ph, key=lambda p: sum(on[int((best + p + k * BEAT) * efps)] for k in range(int(DUR / BEAT))))
START = best + phase

# ================================================================ timeline
T = []; t0 = 0.0
for kind, nb, data in CF["shots"]:
    T.append(dict(kind=kind, t0=t0, t1=t0 + nb * BEAT, nb=nb, data=data)); t0 += nb * BEAT
CUTS = [s["t0"] for s in T[1:]]
if CF.get("vo"):
    def _tc(x): return f"{int(x // 3600):02d}:{int(x % 3600 // 60):02d}:{int(x % 60):02d},{int(x * 1000 % 1000):03d}"
    srt, txt_ = [], []
    for i, (sh, vo) in enumerate(zip(T, CF["vo"])):
        if not vo: continue
        srt.append(f"{len(srt) + 1}\n{_tc(sh['t0'] + 0.15)} --> {_tc(sh['t1'] - 0.1)}\n{vo}\n")
        txt_.append(f"[{sh['t0']:05.1f}s – {sh['t1']:05.1f}s]  {vo}")
    (OUT / f"{Path(sys.argv[2]).stem}_voix.srt").write_text("\n".join(srt)); (OUT / f"{Path(sys.argv[2]).stem}_voix.txt").write_text("\n".join(txt_))
def shot_at(t): return next((s for s in T if s["t0"] <= t < s["t1"]), T[-1])

# ================================================================ outils de dessin
def txt(text): return text.upper() if CF["upper"] else text
def fit(text, path, maxw, size, maxlines=3):
    while size > 30:
        f = F(path, size); words = text.split(); lines, cur = [], []
        for w_ in words:
            if cur and f.getlength(" ".join(cur + [w_])) > maxw: lines.append(" ".join(cur)); cur = [w_]
            else: cur.append(w_)
        lines.append(" ".join(cur))
        if len(lines) <= maxlines and max(f.getlength(l) for l in lines) <= maxw: return f, lines
        size -= 6
    return F(path, 30), [text]
_tc = {}
def block(text, path, size, col, maxw=None, align="center", lh=1.04):
    maxw = maxw or (W - 140)
    k = (text, path, size, col, maxw, align)
    if k in _tc: return _tc[k]
    f, lines = fit(text, path, maxw, size)
    lhp = int(f.size * lh); w = int(max(f.getlength(l) for l in lines)) + 30
    im = Image.new("RGBA", (w, lhp * len(lines) + int(f.size * 0.3)), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    for i, l in enumerate(lines):
        x = (w - f.getlength(l)) / 2 if align == "center" else 0
        d.text((x, i * lhp), l, font=f, fill=col)
    _tc[k] = im; return im
def paste(base, im, cx, cy, s=1.0, a=1.0, rot=0.0):
    if s <= 0.01 or a <= 0.01: return
    if abs(s - 1) > 0.005: im = im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.BICUBIC)
    if abs(rot) > 0.1: im = im.rotate(rot, Image.BICUBIC, expand=True)
    if a < 1: im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * a)))
    base.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))
def rrect(w, h, r, fill, outline=None, width=2):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); ImageDraw.Draw(im).rounded_rectangle([0, 0, w - 1, h - 1], r, fill=fill, outline=outline, width=width); return im
def check_icon(d, cx, cy, r, k, col):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
    p = [(cx - r * .45, cy), (cx - r * .1, cy + r * .38), (cx + r * .5, cy - r * .38)]
    if k > 0: d.line(p[:2] if k < .5 else p, fill=BG + (255,) if False else (10, 10, 10), width=max(3, int(r * .22)))
def cross_icon(d, cx, cy, r, col=hexc(R)):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col); q = r * .4
    d.line([(cx - q, cy - q), (cx + q, cy + q)], fill=WHITE, width=max(3, int(r * .2))); d.line([(cx - q, cy + q), (cx + q, cy - q)], fill=WHITE, width=max(3, int(r * .2)))

# fond : dégradé de la couleur du film + lueur animée
yy, xx = np.mgrid[0:H // 4, 0:W // 4].astype(np.float32)
def background(t, boost=0.0):
    cx = 0.5 + 0.25 * math.sin(t * 0.9); cy = 0.6 + 0.2 * math.cos(t * 0.7)
    d2 = ((xx / (W / 4) - cx) * 1.78) ** 2 + (yy / (H / 4) - cy) ** 2
    g = np.exp(-d2 / 0.18)[..., None] * (0.35 + boost)
    arr = np.array(BG, np.float32) * (1 - g) + np.array(ACC, np.float32) * g * 0.55 + np.array(BG, np.float32) * g * 0.45
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).resize((W, H), Image.BILINEAR).convert("RGBA")

# photos : noir & blanc puis teinte de la couleur du film (duotone)
_ph = {}
def photo(pid):
    if pid not in _ph:
        im = Image.open(STOCK / "hd" / f"{pid}.jpg").convert("L").resize((2304, 1296), Image.BICUBIC)
        a = np.asarray(im, np.float32)[..., None] / 255
        lo, hi = np.array(BG, np.float32) * 0.6, np.array(ACC2, np.float32)
        mid = np.array(ACC, np.float32)
        col = np.where(a < 0.5, lo + (mid - lo) * (a / 0.5), mid + (hi - mid) * ((a - 0.5) / 0.5))
        _ph[pid] = Image.fromarray(np.clip(col * 0.85, 0, 255).astype(np.uint8))
    return _ph[pid]

# ================================================================ plans
def s_slam(im, s, lt):
    k = spring(lt / 0.5); b = block(txt(s["data"]), FD, 150, WHITE)
    paste(im, b, W / 2, H / 2 + 40 * (1 - k), 1.06 - 0.06 * k, clamp(lt / 0.25))
def s_stamp(im, s, lt):
    k = spring(lt / 0.6); b = block(txt(s["data"]), FD, 150 if V else 200, ACC, (W - 300) if V else None)
    pad = 50; box = rrect(b.width + 2 * pad, b.height + 2 * pad, 26, (0, 0, 0, 0), ACC + (255,), 14); box.alpha_composite(b, (pad, pad))
    paste(im, box, W / 2, H / 2, 1.08 - 0.08 * k, clamp(lt / 0.25), -5)
def s_count(im, s, lt):
    num, lbl = s["data"]; k = spring(lt / 0.6)
    paste(im, block(txt(num), FD, 420, ACC), W / 2, H / 2 - 90, 0.9 + 0.1 * k, clamp(lt / 0.3))
    k2 = spring((lt - BEAT) / 0.5)
    if k2 > 0: paste(im, block(txt(lbl), FD, 84, WHITE), W / 2, H / 2 + 200 + 40 * (1 - k2), 1, clamp(k2 * 2))
def s_strike(im, s, lt):
    k = spring(lt / 0.4); b = block(txt(s["data"]), FD, 130, WHITE)
    paste(im, b, W / 2 + 60 * (1 - k), H / 2, 1, clamp(lt / 0.25))
    ks = oexpo((lt - BEAT * 0.6) / 0.18)
    if ks > 0:
        d = ImageDraw.Draw(im); x0 = W / 2 - b.width / 2 - 20
        d.line([(x0, H / 2 + 10), (x0 + (b.width + 40) * ks, H / 2 - 10)], fill=hexc(R), width=22)
def s_photo(im, s, lt):
    pid, cap = s["data"]; p = photo(pid); dur = s["t1"] - s["t0"]
    z = 1.0 + 0.12 * (lt / dur) + 0.06 * (1 - spring(lt / 0.4)); ch = 1296 / z / 1.05; cw = ch * W / H
    l = (2304 - cw) / 2 + 60 * math.sin(lt) * (0.3 if V else 1); tp = (1296 - ch) / 2
    im.alpha_composite(p.crop((int(l), int(tp), int(l + cw), int(tp + ch))).resize((W, H), Image.BILINEAR).convert("RGBA"))
    shade = Image.new("RGBA", (W, H), BG + (110,)); im.alpha_composite(shade)
    k = spring(lt / 0.5); b = block(txt(cap), FD, 130, WHITE)
    paste(im, b, W / 2, H / 2 + 30 * (1 - k), 1.04 - 0.04 * k, clamp(lt / 0.3))
def s_phone(im, s, lt):
    ph = rrect(560, 860, 60, (18, 20, 28, 255), (70, 74, 90, 255), 4); d = ImageDraw.Draw(ph)
    d.rounded_rectangle([20, 20, 540, 110], 28, fill=(28, 32, 44)); d.text((50, 42), "VIP SIGNALS TRADING", font=F(UIB, 30), fill=WHITE)
    d.text((50, 80), "Exemple fictif", font=F(UI, 20), fill=MUT)
    msgs = ["SIGNAL : achète maintenant", "+500 % garanti", "Dépose 250 € pour commencer", "Plus que 3 places !"]
    for i, m_ in enumerate(msgs):
        kk = spring((lt - i * BEAT) / 0.35)
        if kk <= 0: continue
        b = rrect(420, 92, 26, (44, 52, 74, 255)); ImageDraw.Draw(b).text((22, 28), m_, font=F(UI, 25), fill=WHITE)
        b2 = b.resize((int(420 * (0.92 + 0.08 * kk)), int(92 * (0.92 + 0.08 * kk))))
        ph.alpha_composite(b2, (30, 150 + i * 120))
        if lt > 4 * BEAT + i * 0.12: cross_icon(ImageDraw.Draw(ph), 500, 150 + i * 120 + 46, 28)
    k = spring(lt / 0.5); paste(im, ph, W / 2 + (0 if V else 300), H / 2 + (180 if V else 0) + 120 * (1 - k), 1, clamp(lt / 0.1), -4 * (1 - k))
    paste(im, block(txt("Ce qu'on te vend ailleurs"), FD, 80, ACC2, 900 if V else 700), W / 2 + (0 if V else -480), H / 2 - (420 if V else 0), 1, clamp(lt / 0.2))
def s_split(im, s, lt):
    rows = s["data"]; d = ImageDraw.Draw(im)
    if V: return s_split_v(im, s, lt)
    d.rectangle([0, 0, W // 2, H], fill=(20, 8, 10)); d.rectangle([W // 2, 0, W, H], fill=tuple(int(c * 0.35) for c in ACC))
    d.text((W / 4 - F(UIB, 52).getlength("AILLEURS") / 2, 140), "AILLEURS", font=F(UIB, 52), fill=hexc(R))
    d.text((3 * W / 4 - F(UIB, 52).getlength("QUENTIA") / 2, 140), "QUENTIA", font=F(UIB, 52), fill=WHITE)
    for i, (a, b) in enumerate(rows):
        kk = spring((lt - (i * 2 + 0.3) * BEAT) / 0.4)
        if kk <= 0: continue
        y = 330 + i * 200
        fa, fb = F(UIB, 50), F(UIB, 50)
        ia = Image.new("RGBA", (900, 80), (0, 0, 0, 0)); ImageDraw.Draw(ia).text((110, 8), a, font=fa, fill=(220, 200, 200)); cross_icon(ImageDraw.Draw(ia), 50, 40, 32)
        ib = Image.new("RGBA", (900, 80), (0, 0, 0, 0)); db = ImageDraw.Draw(ib); db.text((110, 8), b, font=fb, fill=WHITE)
        db.ellipse([18, 8, 82, 72], fill=ACC); db.line([(34, 40), (46, 54), (68, 26)], fill=(10, 10, 10), width=8)
        im.alpha_composite(ia, (int(80 - 200 * (1 - kk)), y)); im.alpha_composite(ib, (int(W // 2 + 80 + 200 * (1 - kk)), y))
def s_split_v(im, s, lt):
    rows = s["data"]; d = ImageDraw.Draw(im); f = F(UIB, 46); fh = F(UIB, 60)
    d.rectangle([0, 0, W, H // 2], fill=(20, 8, 10)); d.rectangle([0, H // 2, W, H], fill=tuple(int(c * 0.35) for c in ACC))
    d.text((W / 2 - fh.getlength("AILLEURS") / 2, 300), "AILLEURS", font=fh, fill=hexc(R)); d.text((W / 2 - fh.getlength("QUENTIA") / 2, H // 2 + 110), "QUENTIA", font=fh, fill=WHITE)
    for i, (a, b) in enumerate(rows):
        kk = spring((lt - (i * 2 + 0.3) * BEAT) / 0.4)
        if kk <= 0: continue
        ia = Image.new("RGBA", (980, 80), (0, 0, 0, 0)); ImageDraw.Draw(ia).text((100, 10), a, font=f, fill=(220, 200, 200)); cross_icon(ImageDraw.Draw(ia), 45, 40, 30)
        ib = Image.new("RGBA", (980, 80), (0, 0, 0, 0)); db = ImageDraw.Draw(ib); db.text((100, 10), b, font=f, fill=WHITE)
        db.ellipse([15, 10, 75, 70], fill=ACC); db.line([(30, 40), (42, 53), (62, 26)], fill=(10, 10, 10), width=8)
        im.alpha_composite(ia, (int(60 - 200 * (1 - kk)), 440 + i * 130)); im.alpha_composite(ib, (int(60 + 200 * (1 - kk)), H // 2 + 250 + i * 130))
def s_check(im, s, lt):
    items = s["data"]; d = ImageDraw.Draw(im); per = (s["t1"] - s["t0"]) / len(items)
    for i, it in enumerate(items):
        kk = spring((lt - i * per) / 0.4)
        if kk <= 0: continue
        y = (560 + i * 200) if V else (200 + i * 175); RW = W - 100; fs = 66
        while fs > 34 and max(F(FD, fs).getlength(x) for x in items) > RW - 190: fs -= 4
        f = F(FD, fs)
        row = Image.new("RGBA", (RW, 130), (0, 0, 0, 0)); dr = ImageDraw.Draw(row)
        dr.rounded_rectangle([0, 0, RW - 1, 129], 30, fill=(255, 255, 255, 18), outline=ACC + (90,), width=2)
        dr.ellipse([30, 25, 110, 105], fill=ACC); kc = clamp((lt - i * per - 0.12) / 0.2)
        if kc > 0: dr.line([(50, 66), (64, 82), (92, 46)] if kc > .5 else [(50, 66), (64, 82)], fill=(10, 10, 10), width=10)
        dr.text((150, 26), it, font=f, fill=WHITE)
        cur = i == min(len(items) - 1, int(lt // per))
        paste(im, row, W / 2 + 160 * (1 - kk), y + 65, 1.0, clamp(kk * 1.5) * (1 if cur else 0.6))
def s_grid(im, s, lt):
    words = s["data"]; d = ImageDraw.Draw(im); n = len(words); cols = 2 if V else 4
    hi = int(lt / (BEAT / 2)) % n
    for i, w_ in enumerate(words):
        r, c = divmod(i, cols); x = (75 + c * 470) if V else (160 + c * 420); y = (330 + r * 180) if V else (200 + r * 230)
        kk = spring((lt - i * 0.04) / 0.4)
        if kk <= 0: continue
        on_ = i == hi
        t_ = rrect(390, 170 if V else 190, 28, ACC + (255,) if on_ else (255, 255, 255, 20), ACC + (120,), 2)
        f = F(UIB, 40); ImageDraw.Draw(t_).text(((390 - f.getlength(w_)) / 2, 62 if V else 72), w_, font=f, fill=(10, 10, 10) if on_ else WHITE)
        paste(im, t_, x + 195, y + 95, 0.95 + 0.05 * kk, clamp(kk * 1.5))
def s_cards(im, s, lt):
    names = s["data"]; i = min(len(names) - 1, int(lt / BEAT)); u = (lt - i * BEAT)
    k = spring(u / 0.4)
    for j, x, sc, al, rot in ((i - 1, W / 2 - 760 * k, 1 - 0.22 * k, 1 - 0.65 * k, 8 * k), (i, W / 2 + 760 * (1 - k), 0.78 + 0.22 * k, 0.35 + 0.65 * k, -8 * (1 - k))):
        if not 0 <= j < len(names): continue
        c = rrect(620, 760, 40, (30, 22, 18, 240), ACC + (160,), 3); d = ImageDraw.Draw(c)
        d.text((50, 50), "MODULE", font=F(UIB, 30), fill=ACC2); d.text((50, 470), names[j], font=F(FD, 64), fill=WHITE)
        d.ellipse([50, 130, 330, 410], outline=ACC, width=10); d.text((105, 205), str(j + 1).zfill(2), font=F(FD, 110), fill=ACC)
        paste(im, c, x, H / 2, sc, al, rot)
def s_seal(im, s, lt):
    r = 340; seal = Image.new("RGBA", (2 * r + 40, 2 * r + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(seal); c = r + 20
    d.ellipse([20, 20, 20 + 2 * r, 20 + 2 * r], outline=ACC, width=10); d.ellipse([90, 90, 2 * r - 50, 2 * r - 50], outline=ACC2, width=3)
    txt_ = s["data"] * 2; f = F(UIB, 34); ang = lt * 25
    for k_, ch in enumerate(txt_):
        a = math.radians(ang + k_ * 360 / len(txt_)); x, y = c + (r - 45) * math.cos(a), c + (r - 45) * math.sin(a)
        g = Image.new("RGBA", (50, 50), (0, 0, 0, 0)); ImageDraw.Draw(g).text((10, 6), ch, font=f, fill=ACC)
        g = g.rotate(-math.degrees(a) - 90, Image.BICUBIC); seal.alpha_composite(g, (int(x - 25), int(y - 25)))
    q = F(FD, 130); d.text((c - q.getlength("Q") / 2, c - 85), "Q", font=q, fill=WHITE)
    k = spring(lt / 0.8); paste(im, seal, W / 2, H / 2, 0.92 + 0.08 * k, clamp(lt / 0.3), (1 - k) * 10)
def s_end(im, s, lt):
    k = spring(lt / 0.6); d = ImageDraw.Draw(im)
    b = block("Quentia", FD, 150 if V else 200, WHITE); dot = Image.new("RGBA", (90, 90), (0, 0, 0, 0)); ImageDraw.Draw(dot).ellipse([10, 10, 80, 80], fill=ACC)
    paste(im, dot, W / 2 - b.width / 2 - 40, H / 2 - 110, k, 1); paste(im, b, W / 2 + 30, H / 2 - 110, 0.9 + 0.1 * k, clamp(lt / 0.1))
    k2 = spring((lt - BEAT) / 0.5)
    if k2 > 0: paste(im, block("Apprends à trader avec l'IA.", UI, 52, (215, 210, 205)), W / 2, H / 2 + 60 + 20 * (1 - k2), 1, clamp(k2 * 2))
    k3 = spring((lt - 2 * BEAT) / 0.5)
    if k3 > 0:
        pill = rrect(420, 96, 48, ACC + (255,)); f = F(UIB, 44); ImageDraw.Draw(pill).text(((420 - f.getlength("Lien en bio")) / 2, 20), "Lien en bio", font=f, fill=(10, 10, 10))
        paste(im, pill, W / 2, H / 2 + 200, 0.95 + 0.05 * k3, clamp(k3 * 1.5))
def s_module(im, s, lt):
    num, title, bullets, pid = s["data"]; dur = s["t1"] - s["t0"]
    p = photo(pid); ph_h = int(H * 0.36) if V else H; z = 1.04 + 0.06 * (lt / dur)
    ch = 1296 / z; cw = ch * W / ph_h
    if cw > 2304: cw = 2304; ch = cw * ph_h / W
    l = (2304 - cw) / 2; tp = (1296 - ch) / 2
    crop = p.crop((int(l), int(tp), int(l + cw), int(tp + ch))).resize((W, ph_h), Image.BILINEAR).convert("RGBA")
    g = Image.new("L", (1, ph_h)); g.putdata([int(255 * min(1, (ph_h - y) / (ph_h * 0.45))) for y in range(ph_h)]); crop.putalpha(g.resize((W, ph_h)))
    im.alpha_composite(crop, (0, 0))
    k = spring(lt / 0.7); d = ImageDraw.Draw(im)
    tag = rrect(300, 70, 35, ACC + (255,)); f = F(UIB, 34); ImageDraw.Draw(tag).text(((300 - f.getlength(num)) / 2, 14), num, font=f, fill=(10, 10, 10))
    y0 = int(H * 0.36) - 40 if V else 160
    paste(im, tag, 80 + 150, y0 + 35 + 20 * (1 - k), 1, clamp(lt / 0.3))
    tb = block(title, FD, 104, WHITE, W - 160, "left")
    im.alpha_composite(fade_im(tb, clamp(lt / 0.35)), (80, int(y0 + 110 + 30 * (1 - k))))
    yb = y0 + 140 + tb.height
    for i, b_ in enumerate(bullets):
        kk = spring((lt - 0.6 - i * (dur - 1.4) / len(bullets)) / 0.6)
        if kk <= 0: continue
        row = Image.new("RGBA", (W - 160, 150), (0, 0, 0, 0)); dr = ImageDraw.Draw(row)
        dr.ellipse([0, 22, 36, 58], fill=ACC); fb = F(UI, 46)
        words = b_.split(); lines, cur = [], []
        for w_ in words:
            if cur and fb.getlength(" ".join(cur + [w_])) > W - 260: lines.append(" ".join(cur)); cur = [w_]
            else: cur.append(w_)
        lines.append(" ".join(cur))
        for j, L in enumerate(lines[:2]): dr.text((60, 10 + j * 58), L, font=fb, fill=(235, 232, 228))
        im.alpha_composite(fade_im(row, clamp(kk * 1.4)), (int(80 + 60 * (1 - kk)), int(yb + i * 165)))
def fade_im(im, a):
    if a >= 1: return im
    im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * a))); return im
SHOTS = dict(module=s_module, slam=s_slam, stamp=s_stamp, count=s_count, strike=s_strike, photo=s_photo, phone=s_phone, split=s_split, check=s_check,
             grid=s_grid, cards=s_cards, seal=s_seal, end=s_end)
DISC = "Contenu pédagogique, pas un conseil en investissement. Le trading comporte un risque de perte en capital."
DISC_L = ["Contenu pédagogique, pas un conseil en investissement.", "Le trading comporte un risque de perte en capital."] if V else [DISC]

# ================================================================ image finale : plan + transition + caméra sur le temps
VIG = None
def frame(t):
    global VIG
    s = shot_at(t); lt = t - s["t0"]; idx = T.index(s)
    beatph = ((t % BEAT) / BEAT); boost = 0.06 * math.sin(t * 1.3)
    im = background(t, boost); SHOTS[s["kind"]](im, s, lt)
    d = ImageDraw.Draw(im); f = F(UI, 26 if V else 24)
    for j, L in enumerate([] if os.environ.get('NODISC') else DISC_L): d.text((W / 2 - f.getlength(L) / 2, (H - 300 + j * 36) if V else H - 52), L, font=f, fill=(165, 165, 175))
    z = 1 + 0.03 * (t / DUR)  # poussée lente et continue, sans à-coups
    img = im.convert("RGB")
    tr = {"glitch": "blurfade", "cut": "blurfade", "flash": "softflash", "whip": "slide", "scale": "zoomsoft", "zoomblur": "zoomsoft"}.get(CF["trans"][idx % len(CF["trans"])], CF["trans"][idx % len(CF["trans"])]); u = float(lt) / 0.25; ue = float(1 - (1 - min(u, 1)) ** 3)  # entrée de plan selon le style du film
    arr = None
    if idx > 0 and u < 1:
        if tr == "softflash": arr = np.asarray(img, np.float32) * (1 - 0.3 * (1 - ue)) + 255 * 0.3 * (1 - ue)
        elif tr == "blurfade":
            pv = background(t).convert("RGB"); img = Image.blend(pv, img.filter(ImageFilter.GaussianBlur(12 * (1 - ue))), ue)
        elif tr == "slide":
            off = int(W * 0.12 * (1 - ue)); img = Image.blend(background(t).convert("RGB"), Image.fromarray(np.roll(np.asarray(img), off, 1)), ue)
        elif tr == "wipe":
            pv = background(t).convert("RGB"); m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).rectangle([0, 0, int(W * ue), H], fill=255)
            img = Image.composite(img, pv, m.filter(ImageFilter.GaussianBlur(30)))
        elif tr == "pushup":
            off = int(H * 0.10 * (1 - ue)); img = Image.blend(background(t).convert("RGB"), Image.fromarray(np.roll(np.asarray(img), off, 0)), ue)
        elif tr == "zoomsoft": z *= 1 + 0.05 * (1 - ue); img = Image.blend(background(t).convert("RGB"), img, ue)
        elif tr == "glitch":
            a = np.asarray(img).copy(); sh = int(40 * (1 - u)); a[..., 0] = np.roll(a[..., 0], sh, 1); a[..., 2] = np.roll(a[..., 2], -sh, 1)
            rng = np.random.default_rng(int(t * FPS))
            for _ in range(6):
                y = int(rng.integers(0, H - 90)); a[y:y + 60] = np.roll(a[y:y + 60], int(rng.integers(-120, 120)), 1)
            img = Image.fromarray(a)
        elif tr == "zoomblur": z *= 1 + 0.25 * (1 - spring(u * 0.6))
        elif tr == "whip":
            off = int(W * 0.5 * (1 - spring(u * 0.7))); a = np.roll(np.asarray(img), off, 1); img = Image.fromarray(a).filter(ImageFilter.BoxBlur(int(30 * (1 - u))))
        elif tr == "scale": z *= 1.0 + 0.4 * (1 - spring(u * 0.7))
        elif tr == "iris":
            prev = T[idx - 1]; pv = background(t).convert("RGB")
            m = Image.new("L", (W, H), 0); r = 1300 * ue; ImageDraw.Draw(m).ellipse([W / 2 - r, H / 2 - r, W / 2 + r, H / 2 + r], fill=255)
            img = Image.composite(img, pv, m.filter(ImageFilter.GaussianBlur(40)))
    if arr is not None: img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
    if z > 1.001:
        cw, ch = W / z, H / z; img = img.crop((int((W - cw) / 2), int((H - ch) / 2), int((W + cw) / 2), int((H + ch) / 2))).resize((W, H), Image.BILINEAR)
    if VIG is None:
        y_, x_ = np.mgrid[0:H, 0:W]; VIG = np.clip(1 - 0.45 * np.clip(np.sqrt(((x_ - W / 2) / (W / 2)) ** 2 + ((y_ - H / 2) / (H / 2)) ** 2) - 0.5, 0, None) ** 1.4, 0, 1)[..., None].astype(np.float32)
    return Image.fromarray(np.clip(np.asarray(img, np.float32) * VIG, 0, 255).astype(np.uint8))

def render(t):  # flou de mouvement sur les impacts, jamais à travers une coupe
    s = shot_at(t); lt = t - s["t0"]
    if lt > 0.2: return frame(t)
    acc = None; n = 3
    for j in range(n):
        ts = max(s["t0"], t + (j / n - 0.5) * 0.5 / FPS); a = np.asarray(frame(ts), np.float32); acc = a if acc is None else acc + a
    return Image.fromarray(np.clip(acc / n, 0, 255).astype(np.uint8))

if "--frames" in sys.argv:
    tl = sys.argv[sys.argv.index("--frames") + 1]
    ts = [(s["t0"] + s["t1"]) / 2 for s in T] if tl == "mid" else [float(x) for x in tl.split(",")]
    tw, th = W // 5, H // 5; sheet = Image.new("RGB", (tw * len(ts), th))
    for k, tv in enumerate(ts): sheet.paste(frame(tv).resize((tw, th)), (tw * k, 0))
    sheet.save(OUT / f"{FILM}_sheet.png"); print(f"BEAT={BEAT:.3f}s DUR={DUR:.2f}s START={START:.2f}s"); sys.exit()

# ================================================================ son : musique calée + effets sur les coupes, -14 LUFS
n = int(DUR * SR); mus = song[int(START * SR): int(START * SR) + n].copy()
if len(mus) < n: mus = np.pad(mus, ((0, n - len(mus)), (0, 0)))
fade = np.ones(n); fade[:200] = np.linspace(0, 1, 200); fade[-int(0.7 * SR):] = np.linspace(1, 0, int(0.7 * SR)); mus *= fade[:, None] * 0.8
sfx = np.zeros(n); rng = np.random.default_rng(5)
def add(sig, at, g):
    i0 = int(at * SR)
    if 0 <= i0 < n: m_ = min(len(sig), n - i0); sfx[i0:i0 + m_] += sig[:m_] * g
def ts_(d): return np.arange(int(d * SR)) / SR
for s in T[1:]:
    w_ = rng.normal(0, 1, int(0.25 * SR)); w_ = np.convolve(w_, np.ones(10) / 10, "same") * np.linspace(0, 1, len(w_)) ** 3; add(w_, s["t0"] - 0.25, 0.25)
for s in T:
    if s["kind"] in ("stamp", "slam", "count", "seal"):
        t = ts_(0.8); add(np.sin(2 * np.pi * (40 * t + 70 / 6 * (1 - np.exp(-6 * t)))) * np.exp(-4 * t), s["t0"], 0.5)
    if s["kind"] == "strike": t = ts_(0.25); add(np.sign(np.sin(2 * np.pi * 110 * t)) * np.exp(-8 * t), s["t0"] + BEAT * 0.6, 0.12)
    if s["kind"] == "check":
        per = (s["t1"] - s["t0"]) / len(s["data"])
        for i in range(len(s["data"])): t = ts_(0.5); add(np.sin(2 * np.pi * 1760 * t) * np.exp(-9 * t), s["t0"] + i * per + 0.12, 0.12)
    if s["kind"] == "phone":
        for i in range(4): t = ts_(0.15); add(np.sin(2 * np.pi * 1200 * t) * np.exp(-25 * t), s["t0"] + i * BEAT, 0.12)
mix = mus + sfx[:, None]
raw = OUT / f"{FILM}_raw.wav"
import wave
with wave.open(str(raw), "wb") as wv:
    wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR); wv.writeframes((np.clip(mix, -1, 1) * 32767).astype(np.int16).tobytes())
st = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(raw), "-af", "loudnorm=I=-14:TP=-1.3:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
LUFS = CF.get('lufs', -14); mm = json.loads(st[st.rindex("{"):st.rindex("}") + 1]); norm = OUT / f"{FILM}_norm.wav"
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(raw), "-af",
                f"loudnorm=I={LUFS}:TP=-1.3:LRA=11:measured_I={mm['input_i']}:measured_TP={mm['input_tp']}:measured_LRA={mm['input_lra']}:measured_thresh={mm['input_thresh']}:offset={mm['target_offset']}:linear=true",
                "-ar", "48000", str(norm)], check=True)
o = OUT / f"Quentia_{FILM}.mp4"
p = subprocess.Popen(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", str(norm),
                      "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-pix_fmt", "yuv420p", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv",
                      "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(o)], stdin=subprocess.PIPE)
for i in range(int(DUR * FPS)): p.stdin.write(render(i / FPS).tobytes())
p.stdin.close(); p.wait(); print(o, f"BEAT={BEAT:.3f} DUR={DUR:.2f}")
