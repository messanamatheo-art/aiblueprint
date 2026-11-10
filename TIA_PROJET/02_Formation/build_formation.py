import sys, importlib.util, html
from pathlib import Path
SRC = Path(sys.argv[1]); OUT = Path(sys.argv[2]); LOGO = Path(sys.argv[3]); OUT.mkdir(parents=True, exist_ok=True)
def load(n):
    s = importlib.util.spec_from_file_location(n, SRC / f"{n}.py"); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
C = load("content"); K = load("course")
E = html.escape
prompts = []; n = 0
for cat, step, when, items, example in C.PROMPTS:
    for title, obj, text in items:
        n += 1; prompts.append((f"P{n:02d}", cat, step, when, title, obj, text, example))

css = """
@page { size: A4; margin: 16mm 15mm 18mm; }
* { box-sizing: border-box; }
body { font-family: Inter, 'DejaVu Sans', sans-serif; color: #111827; font-size: 10.5pt; line-height: 1.5; margin: 0; }
h1, h2, h3 { font-family: 'Inter Display', Inter, sans-serif; letter-spacing: -0.01em; margin: 0 0 6px; }
h1 { font-size: 24pt; color: #0b1020; } h2 { font-size: 15pt; color: #2f5fff; margin-top: 14px; } h3 { font-size: 11.5pt; margin-top: 10px; }
.page { page-break-before: always; }
.cover { height: 260mm; background: radial-gradient(circle at 50% 38%, #10204a 0, #04060d 62%); color: #fff; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 20mm; margin: -16mm -15mm 0; }
.cover img { width: 62mm; border-radius: 50%; } .cover h1 { color: #fff; font-size: 30pt; margin-top: 10mm; } .cover p { color: #b8c4e6; max-width: 140mm; }
.tag { display: inline-block; font: 600 8pt Inter; letter-spacing: .12em; text-transform: uppercase; color: #2f5fff; }
.box { border: 1px solid #d6def5; border-left: 4px solid #2f5fff; border-radius: 6px; padding: 8px 12px; margin: 8px 0; background: #f6f8ff; page-break-inside: avoid; }
.warn { border-left-color: #f59e0b; background: #fffaf0; }
table { width: 100%; border-collapse: collapse; margin: 6px 0 10px; font-size: 9.5pt; page-break-inside: auto; }
th { background: #0b1020; color: #fff; text-align: left; padding: 5px 7px; } td { border-bottom: 1px solid #e3e8f5; padding: 5px 7px; vertical-align: top; }
tr { page-break-inside: avoid; }
.meta { color: #4b5563; font-size: 9.5pt; } .step { display: inline-block; background: #2f5fff; color: #fff; border-radius: 4px; padding: 1px 7px; font-weight: 700; font-size: 9pt; }
.blk { page-break-inside: avoid; margin: 6px 0; } .blk b.t { color: #2f5fff; display: block; font-size: 9pt; text-transform: uppercase; letter-spacing: .08em; }
.prompt { font-family: 'JetBrains Mono', 'DejaVu Sans Mono', monospace; font-size: 8.6pt; background: #0b1020; color: #e6ecff; padding: 7px 9px; border-radius: 6px; white-space: pre-wrap; }
.p { page-break-inside: avoid; margin: 0 0 9px; } .small { font-size: 8.8pt; color: #4b5563; }
ul.check { list-style: none; padding-left: 0; } ul.check li::before { content: "☐  "; color: #2f5fff; }
.method { display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; } .m { border: 1px solid #d6def5; border-radius: 8px; padding: 7px; page-break-inside: avoid; }
.m .l { font: 800 20pt 'Inter Display', Inter; color: #2f5fff; }
"""
H = [f"<!doctype html><html lang='fr'><head><meta charset='utf-8'><title>Formation Trading IA Academy</title><style>{css}</style></head><body>"]
a = H.append
a(f"<div class='cover'><img src='{LOGO.as_uri()}'><h1>Trading IA Academy</h1><p style='font-size:14pt;color:#fff'>La formation complète · Version 2</p><p>Apprends à analyser les marchés avec méthode, et l'IA comme copilote.<br>10 modules · Méthode DÉCISION · 100 prompts IA · 20 checklists · 6 templates · Espace Notion</p><p style='margin-top:18mm;font-size:8.5pt'>Formation pédagogique. Ce n'est pas un conseil en investissement. Le trading comporte un risque de perte de tout ou partie du capital. Aucun résultat n'est promis. Tous les exemples chiffrés sont fictifs.</p></div>")
a("<div class='page'><span class='tag'>Sommaire</span><h1>Ton parcours</h1><table><tr><th>#</th><th>Module</th><th>Durée</th><th>Étape DÉCISION</th></tr>")
for m in K.MODS: a(f"<tr><td>{m['code']}</td><td>{E(m['title'])}</td><td>{m['dur']}</td><td>{m['step']}</td></tr>")
a("<tr><td>Final</td><td>Projet final et attestation privée TIA</td><td>—</td><td>Toutes</td></tr></table>")
a("<h3>Annexes</h3><p>A · 100 prompts IA · B · 20 checklists · C · Workflows · D · Outils IA · E · Glossaire · F · Exercices de risque corrigés · G · Bonus et fichiers fournis</p>")
a("<div class='box'><b>Comment suivre la formation.</b> Chaque leçon suit 7 blocs : <b>théorie</b>, <b>démonstration</b> (vidéo écran), <b>cas réel</b>, <b>exercice</b>, <b>template</b>, <b>prompt IA</b>, <b>validation des acquis</b>. Aucune leçon n'est seulement théorique : tu repars à chaque fois avec un livrable.</div>")
a("<div class='box warn'><b>À lire avant de commencer.</b> Cette formation enseigne une méthode. Elle ne donne aucun signal d'achat ou de vente et ne promet aucun gain. Commence en compte démo. Ne trade jamais avec de l'argent dont tu as besoin.</div></div>")
a("<div class='page'><span class='tag'>Le cœur de la formation</span><h1>La Méthode DÉCISION</h1><p>Tu ne suis le signal de personne. <b>Tu prends ta décision, avec l'IA comme copilote.</b> Chaque séance suit ces 8 étapes, dans cet ordre.</p><div class='method'>")
for l, nm, fn, what, tool, pr in C.METHOD: a(f"<div class='m'><div class='l'>{l}</div><b>{E(nm)}</b><div class='small'>{E(fn)}</div><p class='small'>{E(what)}</p><div class='small'><b>Outil :</b> {E(tool)}<br><b>Prompts :</b> {pr}</div></div>")
a("</div><div class='box'>La boucle : <b>D</b>onnées → <b>É</b>tude → <b>C</b>opilote IA → <b>I</b>nspection → <b>S</b>écurité → <b>I</b>ntention → <b>O</b>bservation → <b>N</b>ouvelle itération → et on recommence. On ne progresse pas en tradant plus, mais en relisant mieux.</div></div>")
for m in K.MODS:
    a(f"<div class='page'><span class='tag'>Module {m['code'][1:]} · {m['dur']} · étape <span class='step'>{m['step']}</span></span><h1>{E(m['title'])}</h1><p class='meta'><b>Objectif :</b> {E(m['goal'])}</p>")
    a("<div class='blk'><b class='t'>1 · Théorie</b>" + "".join(f"<p>{t}</p>" for t in m["theory"]) + "</div>")
    a(f"<div class='blk'><b class='t'>2 · Démonstration (vidéo)</b><p>{E(m['demo'])}</p></div>")
    a(f"<div class='blk box'><b class='t'>3 · Cas réel (exemple fictif)</b><p>{E(m['case'])}</p></div>")
    a(f"<div class='blk'><b class='t'>4 · Exercice</b><p>{E(m['exercise'])}</p></div>")
    a(f"<div class='blk'><b class='t'>5 · Template associé</b><p>{E(m['template'])}</p></div>")
    a(f"<div class='blk'><b class='t'>6 · Prompts IA associés</b><p>{E(m['prompts'])} — voir annexe A. Vérification humaine obligatoire.</p></div>")
    a("<div class='blk'><b class='t'>7 · Validation des acquis</b><table><tr><th>Question</th><th>Réponse</th></tr>" + "".join(f"<tr><td>{E(q)}</td><td>{E(r)}</td></tr>" for q, r in m["quiz"]) + "</table></div>")
    a("<div class='blk'><b class='t'>Questions fréquentes</b>" + "".join(f"<p><b>{E(q)}</b><br>{E(r)}</p>" for q, r in m["faq"]) + "</div></div>")
a("<div class='page'><span class='tag'>Fin de parcours</span><h1>Projet final et attestation</h1><p>Pour obtenir l'attestation privée Trading IA Academy, envoie :</p><ul class='check'>" + "".join(f"<li>{E(x)}</li>" for x in K.FINAL) + "</ul><div class='box'>L'attestation valide le suivi d'une méthode pendant 30 jours. C'est une attestation privée, pas un diplôme reconnu par l'État, et elle ne certifie aucune performance financière.</div></div>")
a("<div class='page'><span class='tag'>Annexe A</span><h1>Les 100 prompts IA</h1><p>Copie le prompt, remplace les [CROCHETS] par tes informations, colle-le dans ton IA. Puis applique toujours l'étape <b>I — Inspection</b> : " + E(C.V_STD) + "</p>")
cur = None
for pid, cat, step, when, title, obj, text, example in prompts:
    if cat != cur:
        cur = cat; a(f"<h2>{E(cat)} <span class='step'>{step}</span></h2><p class='small'><b>Quand :</b> {E(when)}<br><b>Exemple de remplissage :</b> {E(example)}</p>")
    a(f"<div class='p'><b>{pid} · {E(title)}</b> <span class='small'>— {E(obj)}</span><div class='prompt'>{E(text)}</div></div>")
a("</div><div class='page'><span class='tag'>Annexe B</span><h1>Les 20 checklists</h1>")
for t, items in C.CHECKLISTS: a(f"<div class='blk'><h3>{E(t)}</h3><ul class='check'>" + "".join(f"<li>{E(i)}</li>" for i in items) + "</ul></div>")
a("</div><div class='page'><span class='tag'>Annexe C</span><h1>Les workflows</h1>")
for k, steps in C.WORKFLOWS.items(): a(f"<h2>{E(k)}</h2><ol>" + "".join(f"<li>{E(s)}</li>" for s in steps) + "</ol>")
a("<div class='box'><b>Version courte (15 min) :</b> calendrier + journal d'hier · lecture 3 UT · limites du jour · pas de trade sans scénario écrit · journal en fin de séance.</div></div>")
a("<div class='page'><span class='tag'>Annexe D</span><h1>Les outils IA</h1><p class='small'>Prix indicatifs (novembre 2026), à vérifier sur le site officiel.</p><table><tr><th>Outil</th><th>Utilité</th><th>Prix</th><th>Avantages</th><th>Inconvénients</th><th>Niveau</th></tr>" + "".join("<tr>" + "".join(f"<td>{E(x)}</td>" for x in t) + "</tr>" for t in C.TOOLS) + "</table>")
a("<span class='tag'>Annexe E</span><h1>Glossaire</h1><table><tr><th>Terme</th><th>Définition</th></tr>" + "".join(f"<tr><td><b>{E(k)}</b></td><td>{E(v)}</td></tr>" for k, v in K.GLOSSARY) + "</table></div>")
a("<div class='page'><span class='tag'>Annexe F</span><h1>Exercices de risque corrigés</h1><p>Formule : Taille = (Capital × Risque %) ÷ |Entrée − Stop|. Tous les chiffres sont fictifs. Fais le calcul, puis vérifie dans l'onglet Plan de risque.</p><table><tr><th>#</th><th>Capital</th><th>Risque</th><th>Entrée</th><th>Stop</th><th>1 R</th><th>Taille (corrigé)</th></tr>")
for i, (cap, r, en, sl) in enumerate(K.EXOS, 1):
    risk = cap * r / 100; size = risk / abs(en - sl)
    a(f"<tr><td>{i}</td><td>{cap:,} €".replace(",", " ") + f"</td><td>{str(r).replace('.', ',')} %</td><td>{str(en).replace('.', ',')}</td><td>{str(sl).replace('.', ',')}</td><td>{risk:,.0f} €".replace(",", " ") + f"</td><td><b>{size:,.1f}</b> unités".replace(",", " ").replace(".", ",") + "</td></tr>")
a("</table></div>")
a("<div class='page'><span class='tag'>Annexe G</span><h1>Bonus et fichiers fournis</h1><table><tr><th>Bonus</th><th>Description</th></tr>" + "".join(f"<tr><td><b>{E(k)}</b></td><td>{E(v)}</td></tr>" for k, v in C.BONUS) + "</table>")
a("<h3>Les fichiers de la formation</h3><ul><li><b>TIA_Templates.xlsx</b> : journal, plan de risque (calcul automatique), suivi des performances, préparation hebdo, revue mensuelle, plan de trading, checklists.</li><li><b>Notion_TIA</b> : bases Prompts, Checklists, Journal, Modules + pages Méthode DÉCISION et Workflows (mode d'emploi d'import inclus).</li></ul>")
a("<div class='box warn'><b>Avertissement.</b> Trading IA Academy est une formation à visée pédagogique. Elle ne constitue ni un conseil en investissement, ni une recommandation personnalisée, ni une incitation à acheter ou vendre un instrument financier. Le trading comporte un risque élevé de perte en capital, pouvant aller jusqu'à la totalité de la somme investie. Les performances passées ne préjugent pas des performances futures.</div></div></body></html>")
(OUT / "Formation_Trading_IA_Academy_v2.html").write_text("".join(H), encoding="utf-8")
print("html ok", len(prompts))
