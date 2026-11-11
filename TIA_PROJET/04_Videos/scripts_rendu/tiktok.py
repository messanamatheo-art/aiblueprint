#!/usr/bin/env python3
"""Quentia - vidéos TikTok 12 s, coupes rapides, effets visuels + sonores. Rendu local, coût 0.
Usage: tiktok.py SPEC.json OUT_DIR [--strip]"""
import json, math, subprocess, sys, wave
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

W, H, FPS, SR = 1080, 1920, 30, 44100
FD = "/usr/share/fonts/opentype/inter/"
def font(w, s): return ImageFont.truetype(FD + f"Inter-{w}.otf", s)
COL = {"dark": (11, 11, 15), "blue": (47, 95, 224), "red": (200, 38, 38), "green": (18, 140, 70), "black": (0, 0, 0)}
TXT = {"white": (255, 255, 255), "blue": (91, 140, 255), "red": (255, 90, 90), "green": (74, 222, 128), "dark": (11, 11, 15)}

def oexpo(t): t = min(max(t, 0), 1); return 1.0 if t >= 1 else 1 - 2 ** (-10 * t)

spec = json.loads(Path(sys.argv[1]).read_text())
out_dir = Path(sys.argv[2]); out_dir.mkdir(parents=True, exist_ok=True)
beats = spec["beats"]
t0 = 0.0
for b in beats:
    b["t0"] = t0; t0 += b["d"]; b["t1"] = t0
DUR = t0

# ---------- texte : taille auto (max 3 lignes, 920 px)
def wrap(text, f, maxw):
    lines, cur = [], []
    for w in text.split():
        if cur and f.getlength(" ".join(cur + [w])) > maxw: lines.append(" ".join(cur)); cur = [w]
        else: cur.append(w)
    if cur: lines.append(" ".join(cur))
    return lines

_cache = {}
def text_img(text, color, maxsize=190, weight="ExtraBold"):
    key = (text, color, maxsize, weight)
    if key in _cache: return _cache[key]
    size = maxsize
    while True:
        f = font(weight, size); lines = wrap(text, f, 920)
        if (len(lines) <= 3 and max(f.getlength(l) for l in lines) <= 920) or size <= 60: break
        size -= 6
    lh = int(size * 1.08)
    wmax = int(max(f.getlength(l) for l in lines)) + 40
    im = Image.new("RGBA", (wmax, lh * len(lines) + int(size * 0.35)), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for i, l in enumerate(lines):
        x = (wmax - f.getlength(l)) / 2
        d.text((x + 6, i * lh + 8), l, font=f, fill=(0, 0, 0, 150))  # ombre portée
        d.text((x, i * lh), l, font=f, fill=TXT[color])
    _cache[key] = im
    return im

# ---------- fond animé : bandes diagonales qui défilent
def background(b, t, lt):
    c = COL[b.get("bg", "dark")]
    im = Image.new("RGB", (W, H), c)
    d = ImageDraw.Draw(im)
    lighter = tuple(min(255, int(v * 1.25 + 10)) for v in c)
    off = (t * 900) % 240
    for k in range(-10, 18):
        x = k * 240 + off
        d.polygon([(x, 0), (x + 90, 0), (x + 90 - 900, H), (x - 900, H)], fill=lighter)
    return im

DISC = "Contenu pédagogique, pas un conseil en investissement. Le trading comporte un risque de perte en capital. Aucun résultat garanti."
fdisc = font("SemiBold", 28)
disc_lines = wrap(DISC, fdisc, 960)

def frame(t, i):
    b = next((x for x in beats if x["t0"] <= t < x["t1"]), beats[-1])
    lt = t - b["t0"]
    fx = b.get("fx", "slam")
    im = background(b, t, lt).convert("RGBA")
    # ----- texte principal
    ti = text_img(b["text"], b.get("color", "white"), b.get("size", 190))
    if fx in ("slam", "x", "check", "glitch", "logo"):
        s = 1 + 1.4 * (1 - oexpo(lt / 0.22))
    elif fx == "cta":
        s = 1 + 0.06 * math.sin(lt * 14)
    else:
        s = 1.0
    s *= 1 + 0.02 * lt  # léger zoom continu
    tw, th = max(1, int(ti.width * s)), max(1, int(ti.height * s))
    tim = ti.resize((tw, th), Image.BILINEAR)
    a = min(1.0, lt / 0.06)
    if a < 1: tim.putalpha(tim.getchannel("A").point(lambda v: int(v * a)))
    # tremblement à l'impact
    rng = np.random.default_rng(i)
    amp = 28 * max(0.0, 1 - lt / 0.3) if fx != "cta" else 0
    dx, dy = rng.integers(-1, 2) * amp, rng.integers(-1, 2) * amp
    cx, cy = W / 2 + dx, H * 0.46 + dy
    if fx == "logo":  # halo lumineux
        glow = tim.filter(ImageFilter.GaussianBlur(28))
        im.alpha_composite(glow, (int(cx - tw / 2), int(cy - th / 2)))
        im.alpha_composite(glow, (int(cx - tw / 2), int(cy - th / 2)))
    im.alpha_composite(tim, (int(cx - tw / 2), int(cy - th / 2)))
    d = ImageDraw.Draw(im)
    # ----- barré rouge (X) / coche verte
    if fx == "x" and lt > 0.25:
        k = oexpo((lt - 0.25) / 0.2)
        x0, y0 = cx - tw / 2 - 20, cy + th * 0.1
        d.line([(x0, y0 + 40), (x0 + (tw + 40) * k, y0 - 40 * k + 40 - 80 * k)], fill=(255, 40, 40), width=26)
    if fx == "check" and lt > 0.2:
        k = oexpo((lt - 0.2) / 0.25)
        bx, by = W / 2, cy - th / 2 - 150
        pts = [(bx - 70, by), (bx - 20, by + 50), (bx + 80, by - 70)]
        if k < 0.4: d.line([pts[0], (pts[0][0] + (pts[1][0] - pts[0][0]) * k / 0.4, pts[0][1] + (pts[1][1] - pts[0][1]) * k / 0.4)], fill=(74, 222, 128), width=30)
        else:
            kk = (k - 0.4) / 0.6
            d.line([pts[0], pts[1], (pts[1][0] + (pts[2][0] - pts[1][0]) * kk, pts[1][1] + (pts[2][1] - pts[1][1]) * kk)], fill=(74, 222, 128), width=30, joint="curve")
    if fx == "cta":  # flèche qui rebondit
        ay = cy + th / 2 + 80 + 30 * abs(math.sin(lt * 8))
        d.polygon([(W / 2 - 70, ay), (W / 2 + 70, ay), (W / 2, ay + 90)], fill=TXT["white"])
    # ----- bandeau d'avertissement permanent
    d.rectangle([0, H - 210, W, H], fill=(0, 0, 0, 170))
    for k, l in enumerate(disc_lines):
        d.text((60, H - 185 + k * 38), l, font=fdisc, fill=(220, 220, 228))
    d.text((60, 90), "QUENTIA", font=font("Bold", 42), fill=(255, 255, 255))
    arr = np.asarray(im.convert("RGB")).astype(np.int16)
    # ----- glitch RGB
    if fx == "glitch" and (lt < 0.35 or (i % 7 in (0, 1))):
        sh = int(18 + 10 * rng.random())
        arr[..., 0] = np.roll(arr[..., 0], sh, axis=1)
        arr[..., 2] = np.roll(arr[..., 2], -sh, axis=1)
        for _ in range(5):
            y = int(rng.integers(0, H - 80)); hgt = int(rng.integers(20, 80))
            arr[y:y + hgt] = np.roll(arr[y:y + hgt], int(rng.integers(-60, 60)), axis=1)
    # ----- flash blanc à chaque coupe
    if lt < 2 / FPS:
        f = 0.75 if lt < 1 / FPS else 0.35
        arr = (arr * (1 - f) + 255 * f)
    # ----- pulsation sur le tempo (128 bpm)
    beat = (t % (60 / 128)) / (60 / 128)
    z = 1 + 0.025 * (1 - beat) ** 3
    img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
    if z > 1.001:
        cw, ch = W / z, H / z
        img = img.crop((int((W - cw) / 2), int((H - ch) / 2), int((W + cw) / 2), int((H + ch) / 2))).resize((W, H), Image.BILINEAR)
    return img

# ---------- audio
def audio():
    n = int(DUR * SR); out = np.zeros(n); rng = np.random.default_rng(7)
    def add(sig, at, g=1.0):
        i0 = int(at * SR)
        if i0 >= n: return
        m = min(len(sig), n - i0); out[i0:i0 + m] += sig[:m] * g
    def tt(d): return np.arange(int(d * SR)) / SR
    spb = 60 / 128
    # kick + charley + basse
    t = tt(0.3); kick = np.sin(2 * np.pi * (45 * t + (150 - 45) / 18 * (1 - np.exp(-18 * t)))) * np.exp(-9 * t)
    hat = np.diff(rng.normal(0, 1, int(0.05 * SR) + 1)) * np.exp(-np.linspace(0, 9, int(0.05 * SR)))
    bassn = [45, 45, 43, 48]
    for k in range(int(DUR / spb) + 1):
        add(kick, k * spb, 0.9)
        add(hat, k * spb + spb / 2, 0.25)
        f = 440 * 2 ** ((bassn[(k // 4) % 4] - 69) / 12); tb = tt(spb)
        add(np.sign(np.sin(2 * np.pi * f * tb)) * np.exp(-3 * tb) * 0.5 + np.sin(2 * np.pi * f * tb) * 0.5, k * spb, 0.22)
    # sons par coupe
    for b in beats:
        fx, at = b.get("fx", "slam"), b["t0"]
        wl = 0.22; w = rng.normal(0, 1, int(wl * SR)); w = np.convolve(w, np.ones(8) / 8, "same") * np.linspace(0, 1, len(w)) ** 2
        add(w, max(0, at - wl), 0.35)  # whoosh
        t = tt(0.6); boom = np.sin(2 * np.pi * (35 * t + 80 / 6 * (1 - np.exp(-6 * t)))) * np.exp(-5 * t)
        add(boom, at, 0.8)
        add(rng.normal(0, 1, int(0.03 * SR)) * np.exp(-np.linspace(0, 6, int(0.03 * SR))), at, 0.4)  # clac
        if fx == "x":
            t = tt(0.3); add(np.sign(np.sin(2 * np.pi * 110 * t)) * 0.6 * np.exp(-4 * t), at + 0.25, 0.5)
        if fx == "check":
            t = tt(0.5); add((np.sin(2 * np.pi * 1320 * t) + 0.6 * np.sin(2 * np.pi * 1980 * t)) * np.exp(-7 * t), at + 0.2, 0.35)
        if fx == "glitch":
            for k in range(6):
                t = tt(0.03); add(np.sign(np.sin(2 * np.pi * (300 + 400 * rng.random()) * t)), at + k * 0.05, 0.25)
        if fx == "logo":
            t = tt(1.0); add(np.sin(2 * np.pi * (200 * t + 500 * t * t)) * np.linspace(0, 1, len(t)) ** 2 * 0.5, max(0, at - 1.0), 0.4)
            t = tt(1.2); add(np.sin(2 * np.pi * 40 * t) * np.exp(-2.5 * t), at, 1.0)
    out *= np.clip(np.arange(n) / (0.02 * SR), 0, 1) * np.clip((n - np.arange(n)) / (0.3 * SR), 0, 1)
    out = np.tanh(out * 1.3); out = out / np.abs(out).max() * 0.92
    p = out_dir / f"{spec['id']}.wav"
    with wave.open(str(p), "wb") as wv:
        wv.setnchannels(1); wv.setsampwidth(2); wv.setframerate(SR); wv.writeframes((out * 32767).astype(np.int16).tobytes())
    return p

if "--strip" in sys.argv:
    ts = [(b["t0"] + b["t1"]) / 2 for b in beats]
    sheet = Image.new("RGB", (216 * len(ts), 384))
    for k, t in enumerate(ts): sheet.paste(frame(t, int(t * FPS)).resize((216, 384)), (216 * k, 0))
    sheet.save(out_dir / f"{spec['id']}-strip.png"); sys.exit()

wav = audio()
o = out_dir / f"Quentia_TikTok_{spec['id']}.mp4"
p = subprocess.Popen(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", str(wav),
                      "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(o)], stdin=subprocess.PIPE)
for i in range(int(round(DUR * FPS))):
    p.stdin.write(frame(i / FPS, i).tobytes())
p.stdin.close(); p.wait(); print(o)
