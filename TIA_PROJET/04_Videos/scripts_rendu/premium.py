#!/usr/bin/env python3
"""Quentia - pub motion design « premium » (style des exemples TikTok de mth).
Sortie : screen_16x9.mp4 (à passer en plein écran et filmer) + tiktok_9x16.mp4 (prêt à publier).
Usage: premium.py OUT_DIR [--frames t1,t2,...]"""
import math, subprocess, sys, wave
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

W, H, FPS, SR = 1920, 1080, 30, 44100
DUR = 16.0
OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
FI = "/usr/share/fonts/opentype/inter/"
def F(name, size): return ImageFont.truetype(FI + name + ".otf", size)
ORANGE, ORANGE2, WHITE, MUTED = (255, 106, 36), (255, 150, 70), (245, 240, 236), (170, 160, 156)

def clamp(x): return min(max(x, 0.0), 1.0)
def oexpo(t): t = clamp(t); return 1.0 if t >= 1 else 1 - 2 ** (-10 * t)
def oquint(t): t = clamp(t); return 1 - (1 - t) ** 5
def iosine(t): t = clamp(t); return -(math.cos(math.pi * t) - 1) / 2
def win(t, a, b, fin=0.5, fout=0.4):
    """0->1 à l'entrée, 1->0 à la sortie (pour les fondus flous)."""
    if t < a or t > b: return 0.0
    return min(oquint((t - a) / fin), 1 - iosine((t - (b - fout)) / fout) if t > b - fout else 1.0)

# ---------------------------------------------------------------- fond : lueurs liquides orange/rouge
LW, LH = 192, 108
gy, gx = np.mgrid[0:LH, 0:LW].astype(np.float32)
def background(t, energy=1.0, cx_shift=0.0):
    acc = np.zeros((LH, LW, 3), np.float32)
    blobs = [
        (0.30 + 0.10 * math.sin(t * 0.7), 0.85 + 0.08 * math.cos(t * 0.5), 0.42, (230, 60, 15), 1.0),
        (0.72 + 0.12 * math.cos(t * 0.6 + 1), 0.95 + 0.05 * math.sin(t * 0.9), 0.38, (255, 110, 30), 0.9),
        (0.50 + 0.25 * math.sin(t * 0.35 + 2), 0.15 + 0.06 * math.sin(t * 0.8), 0.25, (160, 25, 10), 0.55),
    ]
    for bx, by, r, col, g in blobs:
        d2 = ((gx / LW - bx - cx_shift) * 1.78) ** 2 + (gy / LH - by) ** 2
        acc += np.exp(-d2 / (r * r))[..., None] * np.array(col, np.float32) * g * energy
    # ruban lumineux (traînée de lumière)
    yy = 0.55 + 0.18 * np.sin(gx / LW * 6.0 + t * 1.3) * math.sin(t * 0.4 + 0.5)
    rib = np.exp(-((gy / LH - yy) ** 2) / 0.0012) * (0.35 + 0.25 * math.sin(t * 0.9))
    acc += rib[..., None] * np.array((255, 140, 60), np.float32) * energy
    acc = acc / (1 + acc / 255.0)  # tonemap doux
    acc += np.array((7, 5, 5), np.float32)
    im = Image.fromarray(np.clip(acc, 0, 255).astype(np.uint8)).resize((W, H), Image.BICUBIC)
    return im.convert("RGBA")

# ---------------------------------------------------------------- outils texte / verre / 3D
def text_tile(text, font, color, track=0):
    w = int(font.getlength(text) + track * len(text)) + 40
    im = Image.new("RGBA", (w, int(font.size * 1.45)), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if track:
        x = 10
        for ch in text: d.text((x, 4), ch, font=font, fill=color); x += font.getlength(ch) + track
    else:
        d.text((10, 4), text, font=font, fill=color)
    return im

def blur_reveal(base, tile, cx, cy, k, rise=30, anchor="center"):
    """Apparition floue -> nette (le look « focus pull » des exemples)."""
    if k <= 0.01: return
    t = tile
    r = (1 - k) * 22
    if r > 0.5:
        pad = int(r * 3)
        big = Image.new("RGBA", (t.width + 2 * pad, t.height + 2 * pad), (0, 0, 0, 0)); big.alpha_composite(t, (pad, pad))
        t = big.filter(ImageFilter.GaussianBlur(r))
    else: pad = 0
    if k < 1: t = t.copy(); t.putalpha(t.getchannel("A").point(lambda v: int(v * k)))
    x = cx - t.width / 2 if anchor == "center" else cx - pad
    base.alpha_composite(t, (int(x), int(cy - t.height / 2 + rise * (1 - k))))

def glass(w, h, r=28, fill=(22, 16, 16, 205), edge=(255, 255, 255, 46)):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], r, fill=fill, outline=edge, width=2)
    d.rounded_rectangle([2, 2, w - 3, h // 2], r, outline=(255, 255, 255, 18), width=1)
    return im

def _coeffs(dst, src):
    A, B = [], []
    for (dx, dy), (sx, sy) in zip(dst, src):
        A.append([dx, dy, 1, 0, 0, 0, -sx * dx, -sx * dy]); B.append(sx)
        A.append([0, 0, 0, dx, dy, 1, -sy * dx, -sy * dy]); B.append(sy)
    return np.linalg.lstsq(np.array(A, float), np.array(B, float), rcond=None)[0]

def tilt(im, rx=0.0, ry=0.0, persp=1800.0):
    w, h = im.size; ax, ay = math.radians(rx), math.radians(ry); pts = []
    for x, y in ((-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)):
        z = 0.0
        y, z = y * math.cos(ax) - z * math.sin(ax), y * math.sin(ax) + z * math.cos(ax)
        x, z = x * math.cos(ay) + z * math.sin(ay), -x * math.sin(ay) + z * math.cos(ay)
        s = persp / max(persp - z, 1.0); pts.append((x * s, y * s))
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]; ox, oy = min(xs), min(ys)
    ow, oh = int(math.ceil(max(xs) - ox)), int(math.ceil(max(ys) - oy))
    return im.transform((ow, oh), Image.PERSPECTIVE, _coeffs([(x - ox, y - oy) for x, y in pts], [(0, 0), (w, 0), (w, h), (0, h)]), Image.BICUBIC)

def shadowed(base, im, x, y, blur=40, op=0.6, dy=40):
    a = im.getchannel("A").filter(ImageFilter.GaussianBlur(blur)).point(lambda v: int(v * op))
    s = Image.new("RGBA", im.size, (0, 0, 0, 0)); s.putalpha(a)
    base.alpha_composite(s, (int(x), int(y + dy))); base.alpha_composite(im, (int(x), int(y)))

def mark(size, col=ORANGE):
    """Le signe Quentia : un point orange lumineux."""
    im = Image.new("RGBA", (size * 3, size * 3), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse([size, size, size * 2, size * 2], fill=col)
    glow = im.filter(ImageFilter.GaussianBlur(size * 0.5)); glow.alpha_composite(im)
    return glow

# ---------------------------------------------------------------- scènes
PROMPT = "Crée-moi un plan de trade avant chaque position."
f_hero, f_hero_b = F("InterDisplay-Light", 120), F("InterDisplay-SemiBold", 120)
f_ui, f_ui_b, f_small = F("Inter-Regular", 36), F("Inter-SemiBold", 36), F("Inter-Regular", 26)
f_num, f_lbl = F("InterDisplay-SemiBold", 300), F("InterDisplay-Medium", 64)
f_brand, f_tag = F("InterDisplay-SemiBold", 150), F("Inter-Regular", 44)
DISC = "Contenu pédagogique, pas un conseil en investissement. Le trading comporte un risque de perte en capital."
disc_tile = text_tile(DISC, f_small, (150, 140, 136))

ROWS = [("Raison", "Pourquoi j'entre, en une phrase"), ("Risque max", "1 % du capital (exemple)"),
        ("Invalidation", "Le niveau où mon idée est fausse"), ("Sortie", "Fixée avant d'entrer")]
NUMS = [(8.7, 9.8, 7, "modules."), (9.8, 10.9, 8, "vidéos."), (10.9, 12.0, 20, "prompts IA.")]

_cache = {}
def tile(key, fn):
    if key not in _cache: _cache[key] = fn()
    return _cache[key]

def frame(t):
    energy = 0.55 + 0.45 * oquint(t / 1.5)
    if 12.0 <= t < 13.6: energy *= 0.6
    im = background(t, energy)
    # --- 0-2.2 : titre
    k = win(t, 0.3, 2.3)
    if k:
        blur_reveal(im, tile("m", lambda: mark(46)), W / 2, H / 2 - 150, k)
        blur_reveal(im, tile("h1", lambda: text_tile("Trader avec l'IA.", f_hero, WHITE, -2)), W / 2, H / 2 + 20, k)
    # --- 2.2-5.3 : barre de prompt + frappe
    k = win(t, 2.2, 5.4)
    if k:
        bar = glass(1240, 150, 40).copy(); d = ImageDraw.Draw(bar)
        n = int(len(PROMPT) * clamp((t - 2.7) / 1.7))
        txt = PROMPT[:n] if n else ""
        d.text((48, 52), txt or "Demande à Quentia…", font=f_ui, fill=WHITE if txt else MUTED)
        if txt and (int(t * 2.2) % 2 == 0 or n < len(PROMPT)):
            cx = 48 + f_ui.getlength(txt) + 4; d.rectangle([cx, 50, cx + 3, 98], fill=WHITE)
        press = clamp((t - 4.6) / 0.25)
        bc = tuple(int(a + (b - a) * press) for a, b in zip((120, 60, 30), ORANGE))
        d.rounded_rectangle([1240 - 118, 38, 1240 - 44, 112], 22, fill=bc)
        d.polygon([(1240 - 81, 56), (1240 - 99, 80), (1240 - 63, 80)], fill=WHITE); d.rectangle([1240 - 84, 78, 1240 - 78, 96], fill=WHITE)
        s = 0.94 + 0.06 * k
        b2 = bar.resize((int(bar.width * s), int(bar.height * s)), Image.BICUBIC)
        if k < 1: b2.putalpha(b2.getchannel("A").point(lambda v: int(v * k)))
        shadowed(im, b2, W / 2 - b2.width / 2, H / 2 - b2.height / 2 + 40 * (1 - k), 50, 0.5, 30)
        chips = ["Risque", "Journal", "Plan", "IA coach"]
        x = W / 2 - 330
        for c in chips:
            ct = tile("chip" + c, lambda c=c: _chip(c))
            kk = clamp(k * 1.2 - 0.1)
            if kk > 0:
                c2 = ct.copy(); c2.putalpha(c2.getchannel("A").point(lambda v: int(v * kk)))
                im.alpha_composite(c2, (int(x), int(H / 2 + 110)))
            x += ct.width + 18
    # --- 5.3-8.8 : carte « Plan de trade » inclinée en 3D, lignes qui se remplissent
    k = win(t, 5.3, 8.8)
    if k:
        card = glass(1100, 560, 34).copy(); d = ImageDraw.Draw(card)
        d.text((50, 40), "Plan de trade", font=f_ui_b, fill=WHITE)
        d.text((1100 - 50 - f_small.getlength("Exemple fictif"), 48), "Exemple fictif", font=f_small, fill=ORANGE2)
        for i, (a, b) in enumerate(ROWS):
            kr = oexpo((t - (5.8 + i * 0.45)) / 0.4)
            y = 130 + i * 102
            d.line([(50, y - 14), (1050, y - 14)], fill=(255, 255, 255, 30), width=1)
            d.text((50, y + 10), a, font=f_ui, fill=MUTED)
            if kr > 0:
                tl = text_tile(b, f_ui, WHITE); tl.putalpha(tl.getchannel("A").point(lambda v: int(v * kr)))
                card.alpha_composite(tl, (int(330 + 30 * (1 - kr)), y + 6))
                if kr > 0.6:
                    cx, cy = 1010, y + 32
                    d.ellipse([cx - 20, cy - 20, cx + 20, cy + 20], fill=ORANGE)
                    d.line([(cx - 9, cy), (cx - 2, cy + 8), (cx + 10, cy - 8)], fill=WHITE, width=5)
        ry = -26 + 16 * iosine((t - 5.3) / 3.5)
        c3 = tilt(card, rx=6, ry=ry, persp=2000)
        s = 0.92 + 0.08 * k; c3 = c3.resize((int(c3.width * s), int(c3.height * s)), Image.BICUBIC)
        if k < 1: c3.putalpha(c3.getchannel("A").point(lambda v: int(v * k)))
        shadowed(im, c3, W / 2 - c3.width / 2 + 60 * (1 - k), H / 2 - c3.height / 2, 60, 0.6, 50)
    # --- 8.7-12 : grands chiffres qui défilent
    for a, b, n, lbl in NUMS:
        k = win(t, a, b, 0.35, 0.3)
        if k:
            val = int(round(n * oexpo((t - a) / 0.6)))
            num = text_tile(str(val), f_num, WHITE, -8)
            gl = text_tile(str(val), f_num, ORANGE, -8).filter(ImageFilter.GaussianBlur(30))
            blur_reveal(im, gl, W / 2 - 170, H / 2 - 20, k * 0.8)
            blur_reveal(im, num, W / 2 - 170, H / 2 - 20, k)
            blur_reveal(im, tile("l" + lbl, lambda lbl=lbl: text_tile(lbl, f_lbl, ORANGE2)), W / 2 - 170 + num.width / 2 - 10, H / 2 + 50, k, 20, "left")
    # --- 12-13.7 : différenciation
    k = win(t, 12.0, 13.7, 0.35, 0.3)
    if k:
        blur_reveal(im, tile("z1", lambda: text_tile("0 promesse de gains.", f_hero_b, WHITE, -2)), W / 2, H / 2 - 70, k)
        k2 = win(t, 12.6, 13.7, 0.35, 0.3)
        blur_reveal(im, tile("z2", lambda: text_tile("1 vraie méthode.", f_hero, ORANGE2, -2)), W / 2, H / 2 + 80, k2)
    # --- 13.6-16 : carte de fin
    k = clamp((t - 13.6) / 0.6) and oquint((t - 13.6) / 0.6)
    if k:
        blur_reveal(im, tile("m2", lambda: mark(40)), W / 2 - 330, H / 2 - 90, k)
        blur_reveal(im, tile("brand", lambda: text_tile("Quentia", f_brand, WHITE, -4)), W / 2 + 40, H / 2 - 90, k)
        k2 = oquint((t - 14.1) / 0.6)
        blur_reveal(im, tile("tag", lambda: text_tile("Apprends à trader avec l'IA. Lien en bio.", f_tag, (210, 200, 196))), W / 2, H / 2 + 70, k2)
    # avertissement permanent
    im.alpha_composite(disc_tile, (int(W / 2 - disc_tile.width / 2), H - 70))
    # vignette + grain
    arr = np.asarray(im.convert("RGB"), np.float32)
    arr *= VIG
    arr += np.random.default_rng(int(t * FPS)).normal(0, 2.2, (H, W, 1))
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

def _chip(c):
    w = int(f_small.getlength(c)) + 48
    im = glass(w, 54, 27, (30, 22, 20, 190), (255, 255, 255, 40)); ImageDraw.Draw(im).text((24, 11), c, font=f_small, fill=(220, 210, 206)); return im

yy, xx = np.mgrid[0:H, 0:W]
VIG = np.clip(1 - 0.5 * np.clip(np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) - 0.45, 0, None) ** 1.5, 0, 1)[..., None].astype(np.float32)
del yy, xx

# ---------------------------------------------------------------- version 9:16 (écran incliné + accroche)
TW, TH = 1080, 1920
f_cap = F("Inter-SemiBold", 50)
EMOJI = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf", 109)
def caption_box():
    lines = ["J'ai demandé à l'IA de faire", "la pub de ma formation trading"]
    lw = max(f_cap.getlength(l) for l in lines) + 70
    im = Image.new("RGBA", (TW, 230), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    x0 = (TW - lw - 60) / 2
    d.rounded_rectangle([x0, 20, x0 + lw + 60, 20 + 2 * 66 + 40], 18, fill=(255, 255, 255))
    for i, l in enumerate(lines): d.text((x0 + 30, 38 + i * 66), l, font=f_cap, fill=(0, 0, 0))
    e = Image.new("RGBA", (140, 140), (0, 0, 0, 0)); ImageDraw.Draw(e).text((0, 0), "😳", font=EMOJI, embedded_color=True)
    e = e.crop(e.getbbox()).resize((54, 54), Image.LANCZOS)
    im.alpha_composite(e, (int(x0 + 30 + f_cap.getlength(lines[1]) + 14), 38 + 66 + 4))
    return im
CAP = caption_box()
room = np.zeros((TH, TW, 3), np.float32)
ry_, rx_ = np.mgrid[0:TH, 0:TW]
room += np.array((14, 11, 10), np.float32)
room += (np.exp(-(((rx_ - TW / 2) / 700) ** 2 + ((ry_ - 1250) / 380) ** 2))[..., None] * np.array((70, 30, 14), np.float32))  # lueur de l'écran sur le bureau
ROOM = Image.fromarray(np.clip(room, 0, 255).astype(np.uint8)).convert("RGBA")
del room, ry_, rx_
f_d9 = F("Inter-Regular", 28)
DISC9 = [text_tile("Contenu pédagogique, pas un conseil en investissement.", f_d9, (170, 160, 156)),
         text_tile("Le trading comporte un risque de perte en capital.", f_d9, (170, 160, 156))]

def vertical(fr, t):
    im = ROOM.copy()
    scr = fr.resize((1000, 562), Image.BICUBIC).convert("RGBA")
    bez = Image.new("RGBA", (1024, 586), (18, 18, 20, 255)); ImageDraw.Draw(bez).rounded_rectangle([0, 0, 1023, 585], 16, outline=(60, 60, 64, 255), width=3)
    bez.alpha_composite(scr, (12, 12))
    ry = -7 + 3 * math.sin(t * 0.4)
    sc = tilt(bez, rx=8, ry=ry, persp=2200)
    glow = sc.filter(ImageFilter.GaussianBlur(40)); glow.putalpha(glow.getchannel("A").point(lambda v: int(v * 0.45)))
    x, y = TW / 2 - sc.width / 2, 980 - sc.height / 2
    im.alpha_composite(glow, (int(x), int(y + 30)))
    im.alpha_composite(sc, (int(x), int(y)))
    # base du portable
    d = ImageDraw.Draw(im)
    d.polygon([(x + 30, y + sc.height - 4), (x + sc.width - 30, y + sc.height - 4), (x + sc.width - 5, y + sc.height + 26), (x + 5, y + sc.height + 26)], fill=(30, 28, 30))
    im.alpha_composite(CAP, (0, 300))
    for i, dt in enumerate(DISC9): im.alpha_composite(dt, (int(TW / 2 - dt.width / 2), 1560 + i * 44))
    return im.convert("RGB")

# ---------------------------------------------------------------- son : nappe + impacts + whoosh + frappe
def audio():
    n = int(DUR * SR); out = np.zeros(n); rng = np.random.default_rng(3); tt = np.arange(n) / SR
    def add(sig, at, g=1.0):
        i0 = int(at * SR)
        if 0 <= i0 < n: m = min(len(sig), n - i0); out[i0:i0 + m] += sig[:m] * g
    def ts(d): return np.arange(int(d * SR)) / SR
    note = lambda m: 440 * 2 ** ((m - 69) / 12)
    chords = [(0, [45, 52, 57, 60, 64]), (4.4, [41, 48, 57, 60, 65]), (8.7, [43, 50, 55, 59, 62]), (12.0, [40, 47, 55, 59, 64]), (13.6, [45, 52, 57, 61, 64])]
    for idx, (a, ch) in enumerate(chords):
        b = chords[idx + 1][0] if idx + 1 < len(chords) else DUR
        t = ts(b - a + 1.0); env = np.clip(t / 0.8, 0, 1) * np.clip((b - a + 1.0 - t) / 1.0, 0, 1)
        s = sum(np.sin(2 * np.pi * note(m) * t + k) + 0.4 * np.sin(2 * np.pi * note(m) * 1.004 * t) for k, m in enumerate(ch))
        add(s / len(ch) * env * 0.33, a)
    out *= 0.6 + 0.4 * np.clip(tt / 1.5, 0, 1)
    def whoosh(at, d=0.45, g=0.35):
        w = rng.normal(0, 1, int(d * SR)); k = 12
        w = np.convolve(w, np.ones(k) / k, "same") * np.sin(np.linspace(0, np.pi, len(w))) ** 2; add(w, at - d / 2, g)
    def hit(at, g=0.9):
        t = ts(1.6); add(np.sin(2 * np.pi * (32 * t + 60 / 5 * (1 - np.exp(-5 * t)))) * np.exp(-2.2 * t), at, g)
    def ding(at, f=1760, g=0.18):
        t = ts(0.8); add((np.sin(2 * np.pi * f * t) + 0.5 * np.sin(2 * np.pi * f * 1.5 * t)) * np.exp(-6 * t), at, g)
    for at in (0.3, 2.2, 5.3, 8.7, 12.0, 13.6): whoosh(at)
    for at in (0.35, 5.35, 8.75, 12.05): hit(at, 0.7)
    for i in range(len(PROMPT)):  # frappe clavier
        at = 2.7 + 1.7 * i / len(PROMPT)
        c = rng.normal(0, 1, int(0.012 * SR)) * np.exp(-np.linspace(0, 7, int(0.012 * SR))); add(c, at, 0.18)
    ding(4.65, 1320, 0.2)
    for i in range(4): ding(5.8 + i * 0.45 + 0.25, 1760 + i * 220)
    for a, b, nn, l in NUMS: hit(a + 0.05, 0.55); ding(a + 0.55, 2093, 0.12)
    t = ts(1.6); add(np.sin(2 * np.pi * (180 * t + 380 * t * t)) * np.linspace(0, 1, len(t)) ** 2 * 0.22, 12.0)  # montée
    hit(13.62, 1.1); ding(13.7, 880, 0.25)
    out *= np.clip((n - np.arange(n)) / (0.8 * SR), 0, 1)
    out = np.tanh(out * 1.2); out = out / np.abs(out).max() * 0.9
    p = OUT / "premium.wav"
    with wave.open(str(p), "wb") as wv:
        wv.setnchannels(1); wv.setsampwidth(2); wv.setframerate(SR); wv.writeframes((out * 32767).astype(np.int16).tobytes())
    return p

if "--frames" in sys.argv:
    for tv in sys.argv[sys.argv.index("--frames") + 1].split(","):
        fr = frame(float(tv)); fr.resize((960, 540)).save(OUT / f"p_{tv}.png")
        vertical(fr, float(tv)).resize((540, 960)).save(OUT / f"v_{tv}.png")
    sys.exit()

wav = audio()
def pipe(path, w, h):
    return subprocess.Popen(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}", "-r", str(FPS), "-i", "-", "-i", str(wav),
                             "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(path)], stdin=subprocess.PIPE)
p1 = pipe(OUT / "Quentia_premium_ecran_16x9.mp4", W, H)
p2 = pipe(OUT / "Quentia_premium_tiktok_9x16.mp4", TW, TH)
for i in range(int(DUR * FPS)):
    t = i / FPS; fr = frame(t)
    p1.stdin.write(fr.tobytes()); p2.stdin.write(vertical(fr, t).tobytes())
for p in (p1, p2): p.stdin.close(); p.wait()
print("ok")
