#!/usr/bin/env python3
"""Quentia - style « plan-séquence » (comme les références TikTok de mth) : aucune coupe.
Chaque plan devient une station posée dans un grand espace ; une seule caméra voyage de station
en station (glissés, plongées, reculs), avec des particules en profondeur. Musique douce.
Usage: VERT=1 flow.py OUT_DIR SPEC.json [--frames t1,t2]"""
import math, os, sys
from pathlib import Path
HERE = Path(__file__).parent
src = (HERE / "dyn.py").read_text()
head = src[:src.index("# ================================================================ image finale")]
exec(compile(head, "dyn_head", "exec"))  # moteur de plans, musique, timeline T, BEAT, DUR, SHOTS...

SOFT = os.environ.get("SOFTMUSIC")
MOVE = min(0.42, BEAT * 0.85)
# ---------------------------------------------------------------- disposition des stations dans l'espace
PATTERNS = ["right", "zoomin", "down", "left", "zoomout", "down", "right", "zoomin", "left", "down"]
seed = sum(map(ord, FILM))
st = []
x, y, sc = 0.0, 0.0, 1.0
for i, s in enumerate(T):
    if i > 0:
        p = PATTERNS[(seed + i) % len(PATTERNS)]
        if s["kind"] == "end": p = "zoomout"
        if p == "right": x += W * 1.25 * sc
        elif p == "left": x -= W * 1.25 * sc
        elif p == "down": y += H * 1.15 * sc
        elif p == "zoomin": x += W * 0.22 * sc; y += H * 0.18 * sc; sc *= 0.16
        elif p == "zoomout": sc *= 5.0; x -= W * 0.30 * sc; y -= H * 0.12 * sc
    st.append((x, y, sc))
def ease(u):  # quintique entrée-sortie : fluide, aucun dépassement
    u = min(max(u, 0.0), 1.0); return u * u * u * (u * (u * 6 - 15) + 10)
def camera(t):
    i = T.index(shot_at(t))
    cx, cy, cs = st[i]; drift = (t - T[i]["t0"]) / max(0.1, T[i]["t1"] - T[i]["t0"])
    z = 1 / cs * (1 + 0.06 * drift) * (1 + 0.07 * (1 - ease(min(1.0, (t - T[i]['t0']) / 0.35))))  # petit zoom qui se pose à l'arrivée, puis avance lente
    if i + 1 < len(T) and t > T[i + 1]["t0"] - MOVE:  # trajet vers la station suivante
        u = ease((t - (T[i + 1]["t0"] - MOVE)) / MOVE); nx, ny, ns = st[i + 1]
        lz = math.log(z) + (math.log(1 / ns) - math.log(z)) * u  # zoom en espace log
        pull = 1 - 0.36 * math.sin(math.pi * u)  # recule pendant le trajet puis replonge
        return cx + (nx - cx) * u, cy + (ny - cy) * u, math.exp(lz) * pull, u
    return cx, cy, z, 0.0

# ---------------------------------------------------------------- particules en profondeur (parallaxe)
rng = np.random.default_rng(3)
DOTS = []
for k in range(22):
    r = int(rng.integers(4, 16)); b = float(rng.choice([3, 8, 14]))
    spr = Image.new("RGBA", (r * 2 + 60, r * 2 + 60), (0, 0, 0, 0))
    ImageDraw.Draw(spr).ellipse([30, 30, 30 + 2 * r, 30 + 2 * r], fill=(ACC if k % 3 else ACC2) + (int(rng.integers(25, 70)),))
    DOTS.append((spr.filter(ImageFilter.GaussianBlur(b)), rng.uniform(-1, 1), rng.uniform(-1, 1), rng.uniform(0.15, 0.6)))
def particles(im, cx, cy, z, t):
    for spr, px, py, depth in DOTS:
        sx = (px * W * 2.5 - cx * depth * 0.0006 * W - t * 25 * depth) % (W + 200) - 100
        sy = (py * H * 2.5 - cy * depth * 0.0006 * H + math.sin(t * 0.5 + px * 9) * 30) % (H + 200) - 100
        im.alpha_composite(spr, (int(sx), int(sy)))

# ---------------------------------------------------------------- image
_card = {}
def station_canvas(i, lt):
    s = T[i]; c = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    SHOTS[s["kind"]](c, s, max(0.0, lt))
    return c
def frame(t):
    cx, cy, z, moving = camera(t)
    im = background(t, 0.05 * math.sin(t)).convert("RGBA")
    particles(im, cx, cy, z, t)
    cur = T.index(shot_at(t))
    for i in range(max(0, cur - 1), min(len(T), cur + 2)):
        sx, sy, ss = st[i]; k = ss * z
        if k < 0.04 or k > 8: continue
        w, h = W * k, H * k; ox = W / 2 + (sx - cx) * z - w / 2; oy = H / 2 + (sy - cy) * z - h / 2
        if ox > W or oy > H or ox + w < 0 or oy + h < 0: continue
        d = abs(i - cur) - (moving if i > cur else 0) + (moving if i == cur else 0)  # distance au centre d'intérêt
        a = max(0.0, 1 - 0.75 * min(1, d))
        if a < 0.03: continue
        lt = t - T[i]["t0"] + MOVE
        c = station_canvas(i, lt)
        if abs(k - 1) > 0.01: c = c.resize((max(1, int(w)), max(1, int(h))), Image.BILINEAR)
        if a < 1: c.putalpha(c.getchannel("A").point(lambda v: int(v * a)))
        im.alpha_composite(c, (int(ox), int(oy)))
    if VIG is None: _vig()
    return Image.fromarray(np.clip(np.asarray(im.convert("RGB"), np.float32) * VIG, 0, 255).astype(np.uint8))
VIG = None
def _vig():
    global VIG
    y_, x_ = np.mgrid[0:H, 0:W]; VIG = np.clip(1 - 0.45 * np.clip(np.sqrt(((x_ - W / 2) / (W / 2)) ** 2 + ((y_ - H / 2) / (H / 2)) ** 2) - 0.5, 0, None) ** 1.4, 0, 1)[..., None].astype(np.float32)
def render(t):  # flou de mouvement pendant les trajets de caméra
    if camera(t)[3] <= 0.0 or camera(t)[3] >= 1.0: return frame(t)
    acc = None
    for j in range(3):
        a = np.asarray(frame(t + (j / 3 - 0.33) * 0.5 / FPS), np.float32); acc = a if acc is None else acc + a
    return Image.fromarray(np.clip(acc / 3, 0, 255).astype(np.uint8))

if "--frames" in sys.argv:
    ts = [float(v) for v in sys.argv[sys.argv.index("--frames") + 1].split(",")]
    tw, th = W // 5, H // 5; sheet = Image.new("RGB", (tw * len(ts), th))
    for k_, tv in enumerate(ts): sheet.paste(frame(tv).resize((tw, th)), (tw * k_, 0))
    sheet.save(OUT / f"{FILM}_flow.png"); print(f"DUR={DUR:.1f}"); sys.exit()

# ---------------------------------------------------------------- son : musique douce + whoosh léger sur chaque trajet
n = int(DUR * SR); mus = song[int(START * SR): int(START * SR) + n].copy()
if len(mus) < n: mus = np.pad(mus, ((0, n - len(mus)), (0, 0)))
fade = np.ones(n); fade[:int(0.4 * SR)] = np.linspace(0, 1, int(0.4 * SR)); fade[-int(1.0 * SR):] = np.linspace(1, 0, int(1.0 * SR)); mus *= fade[:, None]
sfx = np.zeros(n); rng2 = np.random.default_rng(5)
def add(sig, at, g):
    i0 = int(at * SR)
    if 0 <= i0 < n: m_ = min(len(sig), n - i0); sfx[i0:i0 + m_] += sig[:m_] * g
def ts_(d): return np.arange(int(d * SR)) / SR
for s in T[1:]:  # whoosh sur chaque trajet de caméra
    L = int(MOVE * SR); w_ = rng2.normal(0, 1, L); w_ = np.convolve(w_, np.ones(14) / 14, "same") * np.sin(np.linspace(0, np.pi, L)) ** 2; add(w_, s["t0"] - MOVE, 0.30)
for s in T:
    if s["kind"] in ("stamp", "slam", "count", "seal", "end"):
        t_ = ts_(0.8); add(np.sin(2 * np.pi * (40 * t_ + 70 / 6 * (1 - np.exp(-6 * t_)))) * np.exp(-4 * t_), s["t0"], 0.55)
    if s["kind"] == "strike": t_ = ts_(0.25); add(np.sign(np.sin(2 * np.pi * 110 * t_)) * np.exp(-8 * t_), s["t0"] + BEAT * 0.6, 0.12)
    if s["kind"] == "check":
        per = (s["t1"] - s["t0"]) / len(s["data"])
        for i in range(len(s["data"])): t_ = ts_(0.5); add(np.sin(2 * np.pi * 1760 * t_) * np.exp(-9 * t_), s["t0"] + i * per + 0.12, 0.14)
    if s["kind"] == "module":
        dur = s["t1"] - s["t0"]
        for i in range(len(s["data"][2])): t_ = ts_(0.12); add(np.sin(2 * np.pi * 1400 * t_) * np.exp(-30 * t_), s["t0"] + 0.6 + i * (dur - 1.4) / len(s["data"][2]), 0.12)
    if s["kind"] == "phone":
        for i in range(4): t_ = ts_(0.15); add(np.sin(2 * np.pi * 1200 * t_) * np.exp(-25 * t_), s["t0"] + i * BEAT, 0.14)
# musique à peine audible : normalisée seule à -34 LUFS (environ 14 dB sous les bruitages)
import wave
def _norm(sig, target, tag):
    p_ = OUT / f"{FILM}_{tag}.wav"
    with wave.open(str(p_), "wb") as wv: wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR); wv.writeframes((np.clip(sig, -1, 1) * 32767).astype(np.int16).tobytes())
    q = subprocess.run(["ffmpeg", "-v", "error", "-i", str(p_), "-af", f"loudnorm=I={target}:TP=-3:LRA=11", "-ar", str(SR), "-ac", "2", "-f", "s16le", "-"], capture_output=True).stdout
    return np.frombuffer(q, np.int16).astype(np.float32).reshape(-1, 2)[:n] / 32768
mus = _norm(mus, -34, "mus")
if len(mus) < n: mus = np.pad(mus, ((0, n - len(mus)), (0, 0)))
sfx_peak = np.abs(sfx).max() or 1; sfx = sfx / sfx_peak * 0.7
mix = mus + sfx[:, None]
import wave
norm = OUT / f"{FILM}_flow_mix.wav"
with wave.open(str(norm), "wb") as wv:
    wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR); wv.writeframes((np.clip(mix, -1, 1) * 32767).astype(np.int16).tobytes())
o = OUT / f"Quentia_{FILM}.mp4"
p = subprocess.Popen(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", str(norm),
                      "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(o)], stdin=subprocess.PIPE)
for i in range(int(DUR * FPS)): p.stdin.write(render(i / FPS).tobytes())
p.stdin.close(); p.wait(); print(o, f"DUR={DUR:.1f}")
