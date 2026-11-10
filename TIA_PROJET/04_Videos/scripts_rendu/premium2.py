#!/usr/bin/env python3
"""Quentia - série « premium » 16:9 (même DA que la vidéo écran validée, approches différentes).
Usage: premium2.py OUT_DIR VIDEO [--frames t1,t2]   VIDEO in coach|risque|journal|programme"""
import sys
from pathlib import Path
src = (Path(__file__).parent / "premium.py").read_text()
exec(src[:src.index("# ---------------------------------------------------------------- scènes")])  # fond, texte, verre, 3D (même DA)

VIDEO = sys.argv[2]
f_hero, f_hero_b = F("InterDisplay-Light", 110), F("InterDisplay-SemiBold", 110)
f_ui, f_ui_b, f_small = F("Inter-Regular", 36), F("Inter-SemiBold", 36), F("Inter-Regular", 26)
f_big, f_lbl = F("InterDisplay-SemiBold", 230), F("InterDisplay-Medium", 60)
f_brand, f_tag = F("InterDisplay-SemiBold", 150), F("Inter-Regular", 44)
DISC = "Contenu pédagogique, pas un conseil en investissement. Le trading comporte un risque de perte en capital."
disc_tile = text_tile(DISC, f_small, (150, 140, 136))
RED = (255, 92, 72)
yy, xx = np.mgrid[0:H, 0:W]
VIG = np.clip(1 - 0.5 * np.clip(np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) - 0.45, 0, None) ** 1.5, 0, 1)[..., None].astype(np.float32)
del yy, xx
_c = {}
def tile(key, fn):
    if key not in _c: _c[key] = fn()
    return _c[key]
def T(key, text, font, col=WHITE, track=0): return tile(key, lambda: text_tile(text, font, col, track))
def fade(im, k):
    if k >= 1: return im
    im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * max(k, 0)))); return im
def place(base, im, cx, cy, k, blur_in=True, shadow=True):
    if k <= 0.01: return
    if blur_in and k < 0.98:
        r = (1 - k) * 14; pad = int(r * 3)
        big = Image.new("RGBA", (im.width + 2 * pad, im.height + 2 * pad), (0, 0, 0, 0)); big.alpha_composite(im, (pad, pad))
        im = big.filter(ImageFilter.GaussianBlur(r))
    im = fade(im, k)
    x, y = cx - im.width / 2, cy - im.height / 2 + 40 * (1 - k)
    if shadow: shadowed(base, im, x, y, 50, 0.55, 40)
    else: base.alpha_composite(im, (int(x), int(y)))
def check(d, cx, cy, col=ORANGE, r=20):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col); d.line([(cx - 9, cy), (cx - 2, cy + 8), (cx + 10, cy - 8)], fill=WHITE, width=5)
def cross(d, cx, cy, r=20):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RED); d.line([(cx - 8, cy - 8), (cx + 8, cy + 8)], fill=WHITE, width=5); d.line([(cx - 8, cy + 8), (cx + 8, cy - 8)], fill=WHITE, width=5)

def title(im, t, a, b, l1, l2=None, col2=ORANGE2):
    k = win(t, a, b)
    if not k: return
    if l2:
        blur_reveal(im, T("t1" + l1, l1, f_hero, WHITE, -2), W / 2, H / 2 - 70, k)
        blur_reveal(im, T("t2" + l2, l2, f_hero_b, col2, -2), W / 2, H / 2 + 70, win(t, a + 0.35, b))
    else:
        blur_reveal(im, T("t1" + l1, l1, f_hero, WHITE, -2), W / 2, H / 2, k)

def endcard(im, t):
    k = oquint((t - 13.6) / 0.6) if t > 13.6 else 0
    if k:
        blur_reveal(im, tile("m2", lambda: mark(40)), W / 2 - 330, H / 2 - 90, k)
        blur_reveal(im, T("brand", "Quentia", f_brand, WHITE, -4), W / 2 + 40, H / 2 - 90, k)
        blur_reveal(im, T("tag", "Apprends à trader avec l'IA. Lien en bio.", f_tag, (210, 200, 196)), W / 2, H / 2 + 70, oquint((t - 14.1) / 0.6))

# ======================================================== 1. IA COACH : conversation
USER_Q = "Dis-moi quoi acheter demain."
AI_1, AI_2 = "Je ne donne pas de signaux.", "Montre-moi ton plan : je te dis ce qui manque."
def bubble(text, font, fg, bg, edge, maxw=760):
    w = int(min(font.getlength(text), maxw)) + 64
    im = Image.new("RGBA", (w, 84), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, 83], 30, fill=bg, outline=edge, width=2); d.text((32, 20), text, font=font, fill=fg); return im
def scene_coach(im, t):
    title(im, t, 0.3, 2.4, "Tu demandes à l'IA", "quoi acheter ?")
    k = win(t, 2.3, 7.6)
    if k:
        win_ = glass(1200, 640, 34).copy(); d = ImageDraw.Draw(win_)
        d.text((44, 34), "Quentia · IA coach", font=f_ui_b, fill=WHITE)
        d.ellipse([1200 - 70, 44, 1200 - 50, 64], fill=ORANGE)
        n = int(len(USER_Q) * clamp((t - 2.8) / 0.9))
        if n:
            b = bubble(USER_Q[:n], f_ui, WHITE, (255, 106, 36, 230), (255, 160, 100, 255)); win_.alpha_composite(b, (1200 - 44 - b.width, 130))
        if 3.9 < t < 4.6:  # l'IA écrit…
            dots = Image.new("RGBA", (130, 70), (0, 0, 0, 0)); dd = ImageDraw.Draw(dots)
            dd.rounded_rectangle([0, 0, 129, 69], 30, fill=(40, 32, 30, 230))
            for j in range(3):
                a = 0.4 + 0.6 * (0.5 + 0.5 * math.sin(t * 12 - j))
                dd.ellipse([28 + j * 28, 28, 42 + j * 28, 42], fill=(255, 255, 255, int(255 * a)))
            win_.alpha_composite(dots, (44, 250))
        for j, (txt, at, y) in enumerate(((AI_1, 4.6, 250), (AI_2, 5.4, 360))):
            kk = oquint((t - at) / 0.45)
            if kk > 0:
                b = fade(bubble(txt, f_ui, WHITE, (40, 32, 30, 235), (255, 255, 255, 40), 1000), kk)
                win_.alpha_composite(b, (int(44 - 30 * (1 - kk)), y))
        ry = -10 + 8 * iosine((t - 2.3) / 5.3)
        place(im, tilt(win_, rx=4, ry=ry, persp=2400), W / 2, H / 2 + 10, k)
    k = win(t, 7.5, 10.6)
    if k:
        card = glass(1000, 530, 34).copy(); d = ImageDraw.Draw(card)
        d.text((50, 40), "Ton plan, relu par l'IA", font=f_ui_b, fill=WHITE)
        d.text((1000 - 50 - f_small.getlength("Exemple fictif"), 48), "Exemple fictif", font=f_small, fill=ORANGE2)
        rows = [("Raison", "Écrite", True), ("Risque max", "Fixé", True), ("Invalidation", "Manquante", False)]
        for i, (a, b, ok) in enumerate(rows):
            y = 130 + i * 102; kr = oexpo((t - (7.9 + i * 0.5)) / 0.4)
            d.line([(50, y - 14), (950, y - 14)], fill=(255, 255, 255, 30), width=1); d.text((50, y + 10), a, font=f_ui, fill=MUTED)
            if kr > 0.3:
                d.text((380, y + 10), b, font=f_ui_b if not ok else f_ui, fill=WHITE if ok else RED)
                (check if ok else cross)(d, 910, y + 32)
        if t > 9.4:
            pulse = 0.5 + 0.5 * math.sin((t - 9.4) * 9)
            d.rounded_rectangle([30, 130 + 2 * 102 - 22, 970, 130 + 2 * 102 + 82], 18, outline=(255, 92, 72, int(120 + 135 * pulse)), width=3)
            d.text((50, 130 + 3 * 102 - 4), "À définir avant d'entrer.", font=f_ui, fill=ORANGE2)
        place(im, tilt(card, rx=6, ry=14 - 10 * iosine((t - 7.5) / 3.1), persp=2000), W / 2, H / 2, k)
    k = win(t, 10.5, 13.7)
    if k:
        blur_reveal(im, T("c1", "L'IA comme coach.", f_hero_b, WHITE, -2), W / 2, H / 2 - 70, k)
        blur_reveal(im, T("c2", "Pas comme boule de cristal.", f_hero, ORANGE2, -2), W / 2, H / 2 + 70, win(t, 11.0, 13.7))
EV_COACH = dict(whoosh=[0.3, 2.3, 7.5, 10.5, 13.6], hit=[0.35, 2.35, 7.55, 10.55], typing=[(2.8, 0.9, len(USER_Q))],
                ding=[(3.75, 1320), (4.65, 1760), (5.45, 1975), (7.95, 1760), (8.45, 1975)], buzz=[8.95], riser=12.0)

# ======================================================== 2. RISQUE : calculateur animé
def bar(w, frac, col, h=26):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], h // 2, fill=(255, 255, 255, 30))
    if frac > 0.01: d.rounded_rectangle([0, 0, max(h, int((w - 1) * frac)), h - 1], h // 2, fill=col)
    return im
def scene_risque(im, t):
    title(im, t, 0.3, 2.4, "Combien es-tu prêt", "à perdre ?")
    k = win(t, 2.3, 7.3)
    if k:
        p = glass(1150, 600, 34).copy(); d = ImageDraw.Draw(p)
        d.text((50, 40), "Calculateur de risque", font=f_ui_b, fill=WHITE)
        d.text((1150 - 50 - f_small.getlength("Exemple fictif"), 48), "Exemple fictif", font=f_small, fill=ORANGE2)
        d.text((50, 140), "Capital", font=f_ui, fill=MUTED); d.text((1100 - f_ui_b.getlength("1 000 €"), 140), "1 000 €", font=f_ui_b, fill=WHITE)
        p.alpha_composite(bar(1050, oexpo((t - 2.6) / 0.8), (255, 255, 255, 200)), (50, 200))
        rk = oquint((t - 3.4) / 1.4); pct = 1.0 * rk
        d.text((50, 280), "Risque par trade", font=f_ui, fill=MUTED)
        d.text((1100 - f_ui_b.getlength(f"{pct:.1f} %".replace(".", ",")), 280), f"{pct:.1f} %".replace(".", ","), font=f_ui_b, fill=ORANGE2)
        sl = Image.new("RGBA", (1050, 50), (0, 0, 0, 0)); ds = ImageDraw.Draw(sl)
        ds.rounded_rectangle([0, 18, 1049, 32], 7, fill=(255, 255, 255, 30)); xk = 20 + 1000 * rk * 0.25
        ds.rounded_rectangle([0, 18, xk, 32], 7, fill=ORANGE); ds.ellipse([xk - 22, 3, xk + 22, 47], fill=WHITE)
        p.alpha_composite(sl, (50, 330))
        if t > 4.9:
            kk = oquint((t - 4.9) / 0.5)
            big = fade(text_tile("= 10 € max par trade", F("InterDisplay-SemiBold", 70), WHITE, -1), kk)
            p.alpha_composite(big, (40, int(440 + 20 * (1 - kk))))
        place(im, tilt(p, rx=6, ry=-16 + 12 * iosine((t - 2.3) / 5), persp=2100), W / 2, H / 2, k)
    k = win(t, 7.2, 10.6)
    if k:
        n = int(10 * clamp((t - 7.6) / 1.8)); cap = 1000 * 0.99 ** n
        p = glass(1150, 560, 34).copy(); d = ImageDraw.Draw(p)
        d.text((50, 40), "10 pertes d'affilée, à 1 % chacune", font=f_ui_b, fill=WHITE)
        d.text((1150 - 50 - f_small.getlength("Exemple fictif"), 48), "Exemple fictif", font=f_small, fill=ORANGE2)
        for j in range(10):
            x = 50 + j * 105; on = j < n
            d.rounded_rectangle([x, 130, x + 88, 218], 16, fill=(255, 92, 72, 200) if on else (255, 255, 255, 25))
            if on: d.line([(x + 30, 160), (x + 58, 188)], fill=WHITE, width=5); d.line([(x + 30, 188), (x + 58, 160)], fill=WHITE, width=5)
        d.text((50, 270), "Il te reste", font=f_ui, fill=MUTED)
        num = text_tile(f"{cap:,.0f} €".replace(",", " "), F("InterDisplay-SemiBold", 150), WHITE, -4); p.alpha_composite(num, (36, 320))
        place(im, tilt(p, rx=6, ry=14 - 10 * iosine((t - 7.2) / 3.4), persp=2100), W / 2, H / 2, k)
    k = win(t, 10.5, 13.7)
    if k:
        blur_reveal(im, T("r1", "Le risque se décide", f_hero, WHITE, -2), W / 2, H / 2 - 70, k)
        blur_reveal(im, T("r2", "avant d'entrer.", f_hero_b, ORANGE2, -2), W / 2, H / 2 + 70, win(t, 11.0, 13.7))
EV_RISQUE = dict(whoosh=[0.3, 2.3, 7.2, 10.5, 13.6], hit=[0.35, 2.35, 7.25, 10.55], typing=[], ding=[(2.7, 1320), (5.0, 1760)],
                 ticks=[7.6 + 1.8 * j / 10 + 0.18 for j in range(10)], riser=12.0)

# ======================================================== 3. JOURNAL : mur de fiches en 3D
MARKETS = ["Indice", "Forex", "Actions", "Crypto", "Matières"]
EMO = ["Calme", "Calme", "Patient", "FOMO", "Calme", "Revanche", "Patient", "Calme"]
def journal_wall():
    rng = np.random.default_rng(5); cols, rows = 6, 4; cw, ch = 360, 210
    im = Image.new("RGBA", (cols * (cw + 30), rows * (ch + 30)), (0, 0, 0, 0))
    for r in range(rows):
        for c in range(cols):
            g = glass(cw, ch, 22).copy(); d = ImageDraw.Draw(g); i = r * cols + c
            d.text((24, 20), f"Trade #{i + 1:02d}", font=f_ui_b, fill=WHITE)
            d.text((24, 74), MARKETS[i % 5], font=f_small, fill=MUTED)
            e = EMO[i % 8]; hot = (r, c) == (1, 2)
            d.rounded_rectangle([24, 128, 24 + f_small.getlength(e) + 36, 176], 22, fill=(255, 106, 36, 220) if hot else (255, 255, 255, 30))
            d.text((42, 136), e, font=f_small, fill=WHITE)
            (check(d, cw - 50, 44, ORANGE, 18) if e != "FOMO" else cross(d, cw - 50, 44, 18))
            im.alpha_composite(g, (c * (cw + 30), r * (ch + 30)))
    return im
def scene_journal(im, t):
    title(im, t, 0.3, 2.4, "Ce que ton journal", "sait sur toi.")
    k = win(t, 2.3, 8.2)
    if k:
        wall = tile("wall", journal_wall)
        p = (t - 2.3) / 5.9
        wt = tilt(wall, rx=10, ry=-38 + 22 * iosine(p), persp=1800)
        s = 0.62 + 0.18 * iosine(p); wt = wt.resize((int(wt.width * s), int(wt.height * s)), Image.BICUBIC)
        place(im, wt, W / 2 + 120 * (1 - iosine(p)), H / 2, k, shadow=False)
    k = win(t, 8.1, 10.6, 0.35, 0.3)
    if k:
        n = "1 trade"; blur_reveal(im, T("j1", "1 trade", f_big, WHITE, -6), W / 2, H / 2 - 80, k)
        blur_reveal(im, T("j2", "= 1 ligne.", f_lbl, ORANGE2), W / 2, H / 2 + 110, win(t, 8.5, 10.6))
    k = win(t, 10.5, 13.7)
    if k:
        card = tile("hot", lambda: _hot())
        place(im, tilt(card, rx=6, ry=-12 + 8 * iosine((t - 10.5) / 3), persp=1800), W / 2, H / 2 - 110, k)
        blur_reveal(im, T("j3", "Tes erreurs deviennent visibles.", F("InterDisplay-SemiBold", 84), WHITE, -2), W / 2, H / 2 + 200, win(t, 11.0, 13.7))
def _hot():
    g = glass(620, 230, 26).copy(); d = ImageDraw.Draw(g)
    d.text((32, 26), "Trade #09", font=f_ui_b, fill=WHITE); d.text((32, 82), "Entrée hors plan", font=f_ui, fill=MUTED)
    d.rounded_rectangle([32, 146, 200, 198], 24, fill=(255, 106, 36, 230)); d.text((58, 154), "FOMO", font=f_ui_b, fill=WHITE)
    cross(d, 620 - 60, 50, 22); return g
EV_JOURNAL = dict(whoosh=[0.3, 2.3, 8.1, 10.5, 13.6], hit=[0.35, 2.35, 8.15, 10.55], typing=[], ding=[(8.6, 1760)], buzz=[10.9], riser=12.0,
                  ticks=[2.6 + j * 0.22 for j in range(24)])

# ======================================================== 4. PROGRAMME : carrousel 3D
MODS = [("00", "Bienvenue", "Comment suivre la formation"), ("01", "Les bases", "Le fonctionnement d'un marché"), ("02", "Le risque", "Fixer sa perte maximum"),
        ("03", "Préparer l'IA", "L'IA comme assistant d'étude"), ("04", "Le journal", "Noter chaque position"), ("05", "Psychologie", "Les décisions sous émotion"),
        ("06", "La méthode", "Une routine qui se répète"), ("+", "Bonus", "Études de cas")]
def mod_card(i):
    n, a, b = MODS[i]; g = glass(520, 620, 34).copy(); d = ImageDraw.Draw(g)
    d.text((44, 40), "Module" if n != "+" else "Bonus", font=f_small, fill=MUTED)
    d.text((40, 80), n, font=F("InterDisplay-SemiBold", 200), fill=ORANGE)
    d.text((44, 400), a, font=F("InterDisplay-SemiBold", 54), fill=WHITE); d.text((44, 480), b, font=f_small, fill=MUTED)
    return g
def scene_programme(im, t):
    title(im, t, 0.3, 2.4, "7 modules.", "1 méthode.")
    k = win(t, 2.3, 11.1)
    if k:
        pos = clamp((t - 2.6) / 7.8) * 7  # index centré (continu)
        pos = math.floor(pos) + iosine(pos - math.floor(pos)) if pos < 7 else 7
        order = sorted(range(8), key=lambda i: -abs(i - pos))
        for i in order:
            dx = i - pos
            if abs(dx) > 2.6: continue
            c = tile(f"mod{i}", lambda i=i: mod_card(i))
            s = 1.0 - 0.18 * min(abs(dx), 2); ry = max(-45, min(45, -dx * 32))
            ct = tilt(c, rx=0, ry=ry, persp=1600); ct = ct.resize((int(ct.width * s), int(ct.height * s)), Image.BICUBIC)
            bl = min(abs(dx), 2) * 4
            if bl > 0.5: ct = ct.filter(ImageFilter.GaussianBlur(bl))
            ct = fade(ct, k * (1 - 0.35 * min(abs(dx), 2)))
            x = W / 2 + dx * 470 - ct.width / 2; y = H / 2 - ct.height / 2
            shadowed(im, ct, x, y, 40, 0.5, 40)
    k = win(t, 11.0, 13.7)
    if k:
        blur_reveal(im, T("p1", "Tout est inclus.", f_hero_b, WHITE, -2), W / 2, H / 2 - 90, k)
        items = "Journal Excel   ·   20 prompts IA   ·   Certification privée"
        blur_reveal(im, T("p2", items, F("Inter-Regular", 46), ORANGE2), W / 2, H / 2 + 60, win(t, 11.4, 13.7))
EV_PROG = dict(whoosh=[0.3, 2.3, 11.0, 13.6] + [2.6 + 7.8 * (j + 0.5) / 7 for j in range(7)], hit=[0.35, 2.35, 11.05], typing=[],
               ding=[(2.6 + 7.8 * (j + 0.8) / 7, 1320 + 110 * j) for j in range(7)], riser=12.0)

SCENES = {"coach": (scene_coach, EV_COACH), "risque": (scene_risque, EV_RISQUE), "journal": (scene_journal, EV_JOURNAL), "programme": (scene_programme, EV_PROG)}
scene, EV = SCENES[VIDEO]

def frame(t):
    energy = 0.55 + 0.45 * oquint(t / 1.5)
    if 10.5 <= t < 13.6: energy *= 0.75
    im = background(t + sum(map(ord, VIDEO)) % 7, energy)
    scene(im, t); endcard(im, t)
    im.alpha_composite(disc_tile, (int(W / 2 - disc_tile.width / 2), H - 70))
    arr = np.asarray(im.convert("RGB"), np.float32) * VIG
    arr += np.random.default_rng(int(t * FPS)).normal(0, 2.2, (H, W, 1))
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

def audio():
    n = int(DUR * SR); out = np.zeros(n); rng = np.random.default_rng(3)
    def add(sig, at, g=1.0):
        i0 = int(at * SR)
        if 0 <= i0 < n: m = min(len(sig), n - i0); out[i0:i0 + m] += sig[:m] * g
    def ts(d): return np.arange(int(d * SR)) / SR
    note = lambda m: 440 * 2 ** ((m - 69) / 12)
    base = {"coach": 0, "risque": -2, "journal": 3, "programme": 5}[VIDEO]
    chords = [(0, [45, 52, 57, 60, 64]), (4.4, [41, 48, 57, 60, 65]), (8.0, [43, 50, 55, 59, 62]), (10.5, [40, 47, 55, 59, 64]), (13.6, [45, 52, 57, 61, 64])]
    for idx, (a, ch) in enumerate(chords):
        b = chords[idx + 1][0] if idx + 1 < len(chords) else DUR
        t = ts(b - a + 1.0); env = np.clip(t / 0.8, 0, 1) * np.clip((b - a + 1.0 - t) / 1.0, 0, 1)
        s = sum(np.sin(2 * np.pi * note(m + base) * t + k) + 0.4 * np.sin(2 * np.pi * note(m + base) * 1.004 * t) for k, m in enumerate(ch))
        add(s / len(ch) * env * 0.33, a)
    for at in EV["whoosh"]:
        d = 0.45; w = rng.normal(0, 1, int(d * SR)); w = np.convolve(w, np.ones(12) / 12, "same") * np.sin(np.linspace(0, np.pi, len(w))) ** 2; add(w, at - d / 2, 0.35)
    def hit(at, g):
        t = ts(1.6); add(np.sin(2 * np.pi * (32 * t + 60 / 5 * (1 - np.exp(-5 * t)))) * np.exp(-2.2 * t), at, g)
    for at in EV["hit"]: hit(at, 0.7)
    for a, d, cnt in EV["typing"]:
        for i in range(cnt):
            c = rng.normal(0, 1, int(0.012 * SR)) * np.exp(-np.linspace(0, 7, int(0.012 * SR))); add(c, a + d * i / cnt, 0.18)
    for at, f in EV["ding"]:
        t = ts(0.8); add((np.sin(2 * np.pi * f * t) + 0.5 * np.sin(2 * np.pi * f * 1.5 * t)) * np.exp(-6 * t), at, 0.18)
    for at in EV.get("buzz", []):
        t = ts(0.35); add(np.sign(np.sin(2 * np.pi * 98 * t)) * np.exp(-6 * t), at, 0.18)
    for at in EV.get("ticks", []):
        t = ts(0.06); add(np.sin(2 * np.pi * 2400 * t) * np.exp(-60 * t), at, 0.2)
    r = EV["riser"]; t = ts(1.6); add(np.sin(2 * np.pi * (180 * t + 380 * t * t)) * np.linspace(0, 1, len(t)) ** 2 * 0.22, r)
    hit(13.62, 1.1); t = ts(0.8); add(np.sin(2 * np.pi * 880 * t) * np.exp(-6 * t), 13.7, 0.25)
    out *= np.clip((n - np.arange(n)) / (0.8 * SR), 0, 1)
    out = np.tanh(out * 1.2); out = out / np.abs(out).max() * 0.9
    p = OUT / f"{VIDEO}.wav"
    with wave.open(str(p), "wb") as wv:
        wv.setnchannels(1); wv.setsampwidth(2); wv.setframerate(SR); wv.writeframes((out * 32767).astype(np.int16).tobytes())
    return p

if "--frames" in sys.argv:
    for tv in sys.argv[sys.argv.index("--frames") + 1].split(","):
        frame(float(tv)).resize((640, 360)).save(OUT / f"{VIDEO}_{tv}.png")
    sys.exit()
wav = audio()
o = OUT / f"Quentia_{VIDEO}_16x9.mp4"
p = subprocess.Popen(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", str(wav),
                      "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(o)], stdin=subprocess.PIPE)
for i in range(int(DUR * FPS)):
    p.stdin.write(frame(i / FPS).tobytes())
p.stdin.close(); p.wait(); print(o)
