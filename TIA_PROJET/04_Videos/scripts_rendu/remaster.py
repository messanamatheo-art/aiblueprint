#!/usr/bin/env python3
"""Quentia - remaster des 5 films avec les règles de claude-motion-design + saas-motion-kit.
- ressorts amortis (zeta >= 0.72), jamais de rebond cartoon
- flou de mouvement par sous-images adaptatives (obturateur 180°), jamais d'image figée (caméra vivante)
- variété entre films : une entrée de texte, une caméra et une origine de surprise différentes par film
- surprise : inondation orange qui s'ouvre sur le logo (motif:flood-to-logo, origine différente par film)
- son : normalisation deux passes à -14 LUFS, true peak -1.3 dB
Usage: remaster.py OUT_DIR FILM [--frames t1,t2]   FILM in plan|coach|risque|journal|programme"""
import math, subprocess, sys, json
from pathlib import Path
HERE = Path(__file__).parent
OUT_DIR, FILM = sys.argv[1], sys.argv[2]
probe = sys.argv[sys.argv.index("--frames") + 1] if "--frames" in sys.argv else None

# ---------- charge les scènes existantes (DA validée), sans lancer leur rendu
if FILM == "plan":
    src = (HERE / "premium.py").read_text(); sys.argv = ["premium.py", OUT_DIR]
else:
    src = (HERE / "premium2.py").read_text(); sys.argv = ["premium2.py", OUT_DIR, FILM]
    src = src.replace('src = (Path(__file__).parent / "premium.py").read_text()', f'src = (Path({str(HERE)!r}) / "premium.py").read_text()')
src = src[:src.index('if "--frames" in sys.argv')]
ns = {"__file__": str(HERE / "x.py"), "__name__": "quentia"}
exec(compile(src, "scenes", "exec"), ns)
np, Image, ImageFilter, ImageDraw = ns["np"], ns["Image"], ns["ImageFilter"], ns["ImageDraw"]
W, H, FPS, DUR = ns["W"], ns["H"], ns["FPS"], ns["DUR"]
ORANGE = ns["ORANGE"]

# ---------- ressort amorti (forme fermée), zeta 0.78 : petit dépassement, pas de rebond
def spring(x, zeta=0.78, omega=9.0):
    x = max(0.0, x)
    if x <= 0: return 0.0
    wd = omega * math.sqrt(1 - zeta * zeta)
    return 1 - math.exp(-zeta * omega * x) * (math.cos(wd * x) + zeta * omega / wd * math.sin(wd * x))

# ---------- 5 entrées de texte différentes (une par film)
orig_reveal = ns["blur_reveal"]
def _fade(im, a): return ns["fade"](im, a) if "fade" in ns else _fade0(im, a)
def _fade0(im, a):
    if a >= 1: return im
    im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * max(a, 0)))); return im
def _pos(t, cx, cy, anchor):
    x = cx - t.width / 2 if anchor == "center" else cx
    return x, cy - t.height / 2

def enter_mask(base, tile, cx, cy, k, rise=30, anchor="center"):   # volet masqué qui monte (mask wipe)
    if k <= 0.01: return
    s = spring(k * 1.1)
    h = max(1, int(tile.height * min(1, s)))
    crop = tile.crop((0, tile.height - h, tile.width, tile.height)) if s < 1 else tile
    x, y = _pos(tile, cx, cy, anchor)
    base.alpha_composite(_fade0(crop, min(1, k * 2)), (int(x), int(y + tile.height - h + 18 * (1 - min(1, s)))))
def enter_slide(base, tile, cx, cy, k, rise=30, anchor="center"):  # glisse latérale, sens alterné
    if k <= 0.01: return
    s = spring(k * 1.1); d = 1 if (int(cx + cy) // 7) % 2 == 0 else -1
    x, y = _pos(tile, cx, cy, anchor)
    base.alpha_composite(_fade0(tile, min(1, k * 1.6)), (int(x - d * 120 * (1 - s)), int(y)))
def enter_track(base, tile, cx, cy, k, rise=30, anchor="center"):  # approche qui se resserre (tracking collapse)
    if k <= 0.01: return
    s = spring(k * 1.1); sx = 1 + 0.35 * (1 - s)
    t2 = tile.resize((max(1, int(tile.width * sx)), tile.height), Image.BICUBIC)
    if s < 0.9: t2 = t2.filter(ImageFilter.GaussianBlur(4 * (1 - s)))
    x, y = _pos(t2, cx, cy, anchor) if anchor == "center" else (cx, cy - t2.height / 2)
    base.alpha_composite(_fade0(t2, min(1, k * 1.5)), (int(x), int(y)))
def enter_scale(base, tile, cx, cy, k, rise=30, anchor="center"):  # pousse depuis le centre
    if k <= 0.01: return
    s = spring(k * 1.1); sc = 0.82 + 0.18 * s
    t2 = tile.resize((max(1, int(tile.width * sc)), max(1, int(tile.height * sc))), Image.BICUBIC)
    x, y = _pos(t2, cx if anchor == "center" else cx + tile.width / 2 - t2.width / 2, cy, "center" if anchor == "center" else "left")
    if anchor != "center": x = cx + (tile.width - t2.width) / 2
    base.alpha_composite(_fade0(t2, min(1, k * 1.4)), (int(x), int(y)))

# film -> (entrée, caméra, origine de l'inondation)
STYLE = {
    "plan":      (orig_reveal,  "push",  (0.5, 0.5)),   # flou -> net, poussée lente
    "coach":     (enter_mask,   "pan",   (0.85, 0.3)),  # volet masqué, panoramique latéral
    "risque":    (enter_slide,  "punch", (0.15, 0.8)),  # glisse, coups de caméra sur les temps forts
    "journal":   (enter_track,  "dolly", (0.5, 1.0)),   # resserrement, travelling arrière
    "programme": (enter_scale,  "whip",  (0.0, 0.5)),   # poussée centrale, whip pan aux coupes
}
entrance, CAM, FLOOD_O = STYLE[FILM]
ns["blur_reveal"] = entrance
CUTS = {"plan": [2.2, 5.3, 8.7, 9.8, 10.9, 12.0, 13.6], "coach": [2.3, 7.5, 10.5, 13.6], "risque": [2.3, 7.2, 10.5, 13.6],
        "journal": [2.3, 8.1, 10.5, 13.6], "programme": [2.3, 11.0, 13.6]}[FILM]

# ---------- caméra : toujours vivante (aucune image figée), zoom en espace log
def camera(img, t):
    z, dx = 1.0, 0.0
    if CAM == "push":  z = math.exp(math.log(1.0) + (math.log(1.06) - 0) * (t / DUR))
    if CAM == "pan":   z = 1.04; dx = -40 + 80 * (t / DUR)
    if CAM == "dolly": z = math.exp(math.log(1.08) * (1 - t / DUR))
    if CAM == "punch":
        z = 1.02
        for c in CUTS: z += 0.02 * math.exp(-max(0, t - c) * 6) * (t >= c)
    if CAM == "whip":
        z = 1.03
        for c in CUTS:
            u = (t - (c - 0.18)) / 0.36
            if 0 <= u <= 1: dx += -W * 0.35 * math.sin(math.pi * u) * (1 if c != 11.0 else -1)
    if abs(z - 1) < 1e-4 and abs(dx) < 0.5: return img
    cw, ch = W / z, H / z
    l = (W - cw) / 2 - dx / z; tp = (H - ch) / 2
    l = min(max(l, -W * 0.4), W * 1.4 - cw)
    if l < 0 or l + cw > W:  # whip : bord étendu en miroir
        pad = int(W * 0.5); big = Image.new("RGB", (W + 2 * pad, H)); big.paste(img, (pad, 0))
        big.paste(img.transpose(Image.FLIP_LEFT_RIGHT).crop((W - pad, 0, W, H)), (0, 0)); big.paste(img.transpose(Image.FLIP_LEFT_RIGHT).crop((0, 0, pad, H)), (W + pad, 0))
        return big.crop((int(l + pad), int(tp), int(l + pad + cw), int(tp + ch))).resize((W, H), Image.BICUBIC)
    return img.crop((int(l), int(tp), int(l + cw), int(tp + ch))).resize((W, H), Image.BICUBIC)

# ---------- surprise : l'orange inonde l'écran puis s'ouvre sur le logo
ox, oy = FLOOD_O[0] * W, FLOOD_O[1] * H
RMAX = max(math.hypot(ox - x, oy - y) for x in (0, W) for y in (0, H)) + 10
def flood(img, t):
    a0, a1, a2 = 13.15, 13.55, 14.05
    if not (a0 <= t <= a2): return img
    col = Image.new("RGB", (W, H), ORANGE)
    m = Image.new("L", (W, H), 0); d = ImageDraw.Draw(m)
    if t < a1:
        r = RMAX * spring((t - a0) / (a1 - a0) * 1.15, 0.9, 8)
        d.ellipse([ox - r, oy - r, ox + r, oy + r], fill=255)
    else:
        d.rectangle([0, 0, W, H], fill=255)
        r = RMAX * spring((t - a1) / (a2 - a1) * 1.15, 0.9, 8)
        d.ellipse([W / 2 - r, H / 2 - r, W / 2 + r, H / 2 + r], fill=0)
    return Image.composite(col, img, m.filter(ImageFilter.GaussianBlur(2)))

# ---------- sous-images adaptatives (flou de mouvement), jamais à travers une coupe nette
SHUTTER = 0.5
def n_sub(t):
    hot = any(0 <= t - c < 0.7 for c in CUTS) or 13.1 <= t <= 14.1 or t < 1.0
    if CAM == "whip" and any(abs(t - c) < 0.25 for c in CUTS): return 10
    return 4 if hot else 1
def render(t, i):
    n = n_sub(t)
    if n == 1: return flood(camera(ns["frame"](t), t), t)
    acc = None
    for j in range(n):
        ts = t + (j / n - 0.5) * SHUTTER / FPS
        fr = np.asarray(flood(camera(ns["frame"](max(0, ts)), ts), ts), np.float32)
        acc = fr if acc is None else acc + fr
    return Image.fromarray(np.clip(acc / n, 0, 255).astype(np.uint8))

out = Path(OUT_DIR); out.mkdir(parents=True, exist_ok=True)
if probe:
    for tv in probe.split(","):
        render(float(tv), int(float(tv) * FPS)).resize((640, 360)).save(out / f"{FILM}_{tv}.png")
    sys.exit()

# ---------- son : bande son existante + normalisation deux passes -14 LUFS
raw = ns["audio"]()
st = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(raw), "-af", "loudnorm=I=-14:TP=-1.3:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
m = json.loads(st[st.rindex("{"):st.rindex("}") + 1])
norm = out / f"{FILM}_norm.wav"
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(raw), "-af",
                f"loudnorm=I=-14:TP=-1.3:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true",
                "-ar", "48000", str(norm)], check=True)
o = out / f"Quentia_{FILM}_v2.mp4"
p = subprocess.Popen(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", str(norm),
                      "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv",
                      "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(o)], stdin=subprocess.PIPE)
for i in range(int(DUR * FPS)):
    p.stdin.write(render(i / FPS, i).tobytes())
p.stdin.close(); p.wait(); print(o)
