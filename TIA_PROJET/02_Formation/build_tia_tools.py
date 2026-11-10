import sys, csv, importlib.util
from pathlib import Path
SRC = Path(sys.argv[1]); OUT = Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
spec = importlib.util.spec_from_file_location("content", SRC / "content.py"); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)

# ---------------------------------------------------------------- numérotation des 100 prompts
prompts = []; n = 0
for cat, step, when, items, example in C.PROMPTS:
    for title, obj, text in items:
        n += 1; prompts.append(dict(id=f"P{n:02d}", cat=cat, step=step, when=when, title=title, obj=obj, text=text, example=example, verif=C.V_STD))
assert len(prompts) == 100, len(prompts)

# ---------------------------------------------------------------- DOCX
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
BLUE = RGBColor(0x2F, 0x5F, 0xFF)
d = Document()
for s in d.sections: s.left_margin = s.right_margin = Cm(2); s.top_margin = s.bottom_margin = Cm(1.8)
st = d.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(10.5)
def H(t, l=1):
    h = d.add_heading(t, level=l)
    for r in h.runs: r.font.color.rgb = BLUE
def P(t, b=False, i=False):
    p = d.add_paragraph(); r = p.add_run(t); r.bold = b; r.italic = i; return p
def B(t): d.add_paragraph(t, style="List Bullet")
def T(headers, rows, widths=None):
    tb = d.add_table(rows=1, cols=len(headers)); tb.style = "Light Grid Accent 1"
    for k, h in enumerate(headers):
        c = tb.rows[0].cells[k]; c.text = ""; r = c.paragraphs[0].add_run(h); r.bold = True
    for row in rows:
        cells = tb.add_row().cells
        for k, v in enumerate(row): cells[k].text = str(v)
    if widths:
        for row in tb.rows:
            for k, w in enumerate(widths): row.cells[k].width = Cm(w)
    d.add_paragraph()

t = d.add_heading("Trading IA Academy — Boîte à outils et plan d'amélioration", 0)
P("Version 1 · 8 novembre 2026 · Document de travail pour le formateur", i=True)
P("Rappel non négociable : formation pédagogique. Aucune promesse de gains, aucun signal d'achat ou de vente, aucun conseil personnalisé. Le trading comporte un risque de perte en capital. Tous les exemples chiffrés sont fictifs.", b=True)

H("Sommaire du livrable")
for x in ["1. Audit complet", "2. Liste des améliorations", "3. Nouveaux modules", "4. Nouveaux outils (outils IA)", "5. Nouveaux bonus", "6. Nouveaux prompts IA (100)", "7. Nouveaux templates", "8. Nouvelle méthode propriétaire", "9. Plan d'implémentation", "10. Ordre de priorité", "Annexes : 20 checklists, 3 workflows, FAQ intégrée par module"]: B(x)

H("1. Audit complet de la formation actuelle (v1)")
P("Base analysée : Formation_Quentia_complete_v1 (modules 0 à 6, bonus études de cas, 20 prompts, parcours de 30 jours avec XP, journal Excel, certification).")
T(["Module", "Points forts", "Ce qui manque / à améliorer", "Correction proposée"], C.AUDIT, [3, 4, 5, 5])
P("Diagnostic global : le cadre (sérieux, légal, pédagogique) est solide, mais l'élève repart surtout avec des connaissances. Il manque des outils exploitables dès le jour 1, une méthode nommée qui relie tout, et une boucle d'amélioration outillée (revues). La v2 corrige ces trois points.", b=True)

H("2. Liste des améliorations")
for x in ["Créer une méthode propriétaire nommée (Méthode DÉCISION) présente dans chaque module.", "Passer de 20 à 100 prompts, classés par étape, avec vérification humaine obligatoire.", "Créer 20 checklists couvrant toute la journée du trader.", "Fournir 6 templates Excel avec calculs automatiques + un espace Notion.", "Imposer un format de leçon en 7 blocs (aucune leçon uniquement théorique).", "Ajouter les workflows quotidien, hebdomadaire et mensuel.", "Intégrer une FAQ par module pour réduire les demandes au support.", "Transformer les études de cas en format fixe, dont des cas perdants.", "Ajouter fiches de révision, quiz notés et projet final évalué.", "Garder et renforcer la gamification (XP, niveaux) liée aux livrables, pas aux gains."]: B(x)

H("3. Nouveaux modules (v2)")
T(["#", "Module", "Contenu", "Outils livrés", "Prompts", "Validation"], C.MODULES, [1.2, 3.2, 5, 3.5, 2, 3])
H("Format imposé de chaque leçon", 2)
T(["Bloc", "Contenu"], C.LESSON_FORMAT, [4, 13])

H("4. Nouveaux outils : outils IA recommandés")
P("Prix indicatifs relevés en novembre 2026 : à vérifier sur le site officiel avant de les communiquer aux élèves.", i=True)
T(["Outil", "Utilité dans TIA", "Prix", "Avantages", "Inconvénients", "Niveau"], C.TOOLS, [2.6, 4, 2.8, 3, 3, 2])

H("5. Nouveaux bonus premium")
T(["Bonus", "Description"], C.BONUS, [5, 12])

H("6. Bibliothèque de 100 prompts IA")
P("Mode d'emploi commun : copie le prompt, remplace les [CROCHETS] par tes informations, colle-le dans ton IA. Avant d'utiliser la réponse, applique toujours la vérification humaine (étape I de la Méthode DÉCISION).", b=True)
cur = None
for p in prompts:
    if p["cat"] != cur:
        cur = p["cat"]; H(f"{cur} — étape {p['step']}", 2); P(f"Quand l'utiliser : {p['when']}", i=True); P(f"Exemple de remplissage : {p['example']}", i=True)
    P(f"{p['id']} · {p['title']}", b=True)
    P(f"Objectif : {p['obj']}")
    q = d.add_paragraph(); r = q.add_run(p["text"]); r.font.name = "Consolas"; r.font.size = Pt(9.5); q.paragraph_format.left_indent = Cm(0.6)
    P(f"Vérification humaine obligatoire : {p['verif']}", i=True)

H("7. Nouveaux templates")
for name, desc in [("Journal de trading", "Une ligne par trade : date, marché, sens, raison liée au plan, stop, objectif, taille, risque €, résultat €, résultat en R (calculé), plan respecté, émotion avant/après, tags, leçon."), ("Plan de trading", "Règles numérotées et versionnées : marchés, horaires, UT, entrée, invalidation, sortie, risque, annonces, arrêt."), ("Plan de gestion du risque", "Capital, % de risque, limites jour/semaine, calculateur de taille de position automatique."), ("Suivi des performances", "Calcul automatique : nombre de trades, % de respect du plan, R total, R moyen, taux de réussite."), ("Préparation hebdomadaire", "Tableau jour par jour : annonces, niveaux, objectif d'apprentissage."), ("Revue mensuelle", "Indicateurs du mois, biais principal, modification du plan, décision démo/réel.")]:
    P(name, b=True); P(desc)
P("Fichiers fournis : TIA_Templates.xlsx (6 onglets + checklists) et le pack Notion (bases de données CSV à importer).", i=True)

H("8. Nouvelle méthode propriétaire")
H("Noms proposés", 2)
T(["Nom", "Pourquoi"], C.METHOD_NAMES, [5, 12])
H("La Méthode DÉCISION — 8 étapes", 2)
T(["Lettre", "Étape", "Fonction", "Ce qu'on fait", "Outil", "Prompts"], C.METHOD, [1.2, 2.6, 3, 6, 3.5, 1.7])
P("Message clé pour l'élève : « Avec DÉCISION, tu ne suis le signal de personne. Tu prends ta décision, avec l'IA comme copilote. »", b=True)

H("9. Plan d'implémentation complet")
T(["Quand", "Priorité", "Action"], C.PLAN, [2.5, 1.8, 13])

H("10. Ordre de priorité des améliorations")
for x in ["P1 — Ce qui augmente le plus la valeur perçue, tout de suite : 100 prompts, 20 checklists, classeur Excel, Méthode DÉCISION.", "P1 — Espace Notion + vidéo « Installer ton cockpit » (l'élève repart avec un système le jour 1).", "P2 — Format de leçon en 7 blocs, FAQ par module, fiches de révision et quiz (complétion + moins de support).", "P2 — Démonstrations écran des workflows.", "P3 — Études de cas au format fixe, bibliothèque d'erreurs, plans d'action, projet final évalué.", "P3 — Mise à jour de la page de vente et collecte de vrais avis d'élèves (jamais de faux témoignages)."]: B(x)

H("Annexe A — Les 20 checklists")
for title, items in C.CHECKLISTS:
    P(f"☐ {title}", b=True)
    for it in items: B("☐ " + it)
H("Annexe B — Workflows")
for k, steps in C.WORKFLOWS.items():
    H(k, 2)
    for i, s_ in enumerate(steps, 1): d.add_paragraph(f"{i}. {s_}")
H("Annexe C — FAQ intégrée par module (réduction du support)")
T(["Module", "Questions probables", "Incompréhensions", "Erreurs fréquentes", "Réponse intégrée"], [(m, " · ".join(q), " · ".join(i), " · ".join(e), r) for m, q, i, e, r in C.SUPPORT], [1.2, 4, 3.3, 3.3, 5.2])
d.save(OUT / "TIA_Boite_a_outils_et_plan_amelioration.docx")

# ---------------------------------------------------------------- XLSX
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule
wb = Workbook(); HDR = PatternFill("solid", fgColor="0B1020"); HF = Font(bold=True, color="FFFFFF"); BLUEF = PatternFill("solid", fgColor="2F5FFF"); INP = PatternFill("solid", fgColor="EAF1FF")
thin = Side(style="thin", color="C9D3EE")
def header(ws, row, cols, widths=None):
    for k, c in enumerate(cols, 1):
        x = ws.cell(row=row, column=k, value=c); x.fill = HDR; x.font = HF; x.alignment = Alignment(wrap_text=True, vertical="center")
    if widths:
        for k, w in enumerate(widths, 1): ws.column_dimensions[ws.cell(row=row, column=k).column_letter].width = w
def title(ws, t, sub):
    ws["A1"] = t; ws["A1"].font = Font(bold=True, size=16, color="2F5FFF"); ws["A2"] = sub; ws["A2"].font = Font(italic=True, color="666666")

ws = wb.active; ws.title = "Mode d'emploi"
title(ws, "Trading IA Academy — Classeur de l'élève", "Cellules bleu clair = à remplir. Les autres colonnes se calculent seules. Tous les exemples sont fictifs.")
for i, l in enumerate(["1. Onglet Plan de risque : saisis ton capital et ton % de risque, le calculateur donne ta taille de position.", "2. Onglet Journal : une ligne par trade, AVANT d'entrer puis à la sortie.", "3. Onglet Suivi : tout se calcule depuis le Journal.", "4. Onglet Préparation hebdo : à remplir le dimanche.", "5. Onglet Revue mensuelle : à remplir le dernier jour du mois.", "6. Onglet Plan de trading : tes règles, versionnées.", "7. Onglet Checklists : à imprimer ou cocher.", "", "Formation pédagogique : aucune promesse de gains. Le trading comporte un risque de perte en capital."], 4):
    ws.cell(row=i, column=1, value=l)
ws.column_dimensions["A"].width = 110

ws = wb.create_sheet("Plan de risque"); title(ws, "Plan de gestion du risque", "Remplis les cellules bleues.")
rows = [("Capital (démo ou réel) €", 10000), ("Risque par trade (%)", 0.01), ("Limite de perte par jour (%)", 0.02), ("Limite de perte par semaine (%)", 0.05), ("Nombre max de trades par jour", 3)]
for i, (k, v) in enumerate(rows, 4):
    ws.cell(row=i, column=1, value=k); c = ws.cell(row=i, column=2, value=v); c.fill = INP
    if "%" in k: c.number_format = "0.0%"
ws["A10"] = "Risque par trade (€) = 1 R"; ws["B10"] = "=B4*B5"; ws["A11"] = "Perte max du jour (€)"; ws["B11"] = "=B4*B6"; ws["A12"] = "Perte max de la semaine (€)"; ws["B12"] = "=B4*B7"
ws["A14"] = "CALCULATEUR DE TAILLE DE POSITION"; ws["A14"].font = Font(bold=True, color="2F5FFF")
for i, (k, v) in enumerate([("Prix d'entrée", 100), ("Prix du stop", 95), ("Objectif", 110)], 15):
    ws.cell(row=i, column=1, value=k); ws.cell(row=i, column=2, value=v).fill = INP
ws["A18"] = "Distance au stop"; ws["B18"] = "=ABS(B15-B16)"; ws["A19"] = "Taille de position (unités)"; ws["B19"] = "=IF(B18=0,\"\",B10/B18)"; ws["B19"].font = Font(bold=True, size=13)
ws["A20"] = "Ratio gain / risque"; ws["B20"] = "=IF(B18=0,\"\",ABS(B17-B15)/B18)"; ws["A21"] = "Taux de réussite minimum pour l'équilibre"; ws["B21"] = "=IF(B20=\"\",\"\",1/(1+B20))"; ws["B21"].number_format = "0.0%"
ws["A23"] = "Attention : pour le forex (lots), les futures (contrats) ou les CFD, convertis selon la valeur du point chez ton intermédiaire."
ws["A25"] = "IMPACT D'UNE SÉRIE DE PERTES"; ws["A25"].font = Font(bold=True, color="2F5FFF")
header(ws, 26, ["Pertes consécutives", "Capital restant", "Baisse"])
for k in range(1, 11):
    ws.cell(row=26 + k, column=1, value=k); ws.cell(row=26 + k, column=2, value=f"=$B$4*(1-$B$5)^A{26+k}").number_format = "#,##0 €"; ws.cell(row=26 + k, column=3, value=f"=1-B{26+k}/$B$4").number_format = "0.0%"
ws.column_dimensions["A"].width = 44; ws.column_dimensions["B"].width = 18; ws.column_dimensions["C"].width = 12

ws = wb.create_sheet("Journal"); title(ws, "Journal de trading", "Une ligne par trade. Résultat en R calculé automatiquement.")
cols = ["Date", "Heure", "Marché", "Sens", "UT", "Raison (liée au plan)", "Entrée", "Stop", "Objectif", "Taille", "Risque €", "Résultat €", "Résultat en R", "Plan respecté", "Émotion avant (1-5)", "Émotion après (1-5)", "Tags", "Leçon en une phrase"]
header(ws, 4, cols, [11, 7, 11, 8, 6, 34, 9, 9, 9, 8, 10, 11, 12, 12, 10, 10, 16, 36])
dv = DataValidation(type="list", formula1='"Oui,Non"', allow_blank=True); ws.add_data_validation(dv)
dv2 = DataValidation(type="list", formula1='"Achat,Vente"', allow_blank=True); ws.add_data_validation(dv2)
ex = ["2026-11-03", "14:40", "EUR/USD", "Vente", "15 min", "Retour sous la zone 1,0860, structure baissière en 1 h (EXEMPLE FICTIF)", 1.0860, 1.0880, 1.0820, "", 100, 50, "", "Non", 4, 3, "sortie anticipée", "J'ai coupé par peur avant l'objectif : laisser travailler le plan."]
for r in range(5, 205):
    for k in range(1, 19):
        c = ws.cell(row=r, column=k); c.border = Border(bottom=thin)
        if k not in (13,): c.fill = INP if r > 5 else PatternFill()
    ws.cell(row=r, column=13, value=f'=IF(OR(K{r}="",L{r}=""),"",L{r}/K{r})').number_format = '0.00" R"'
    dv.add(f"N{r}"); dv2.add(f"D{r}")
for k, v in enumerate(ex, 1):
    if k != 13: ws.cell(row=5, column=k, value=v)
ws.freeze_panes = "A5"
ws.conditional_formatting.add("N5:N204", CellIsRule(operator="equal", formula=['"Non"'], fill=PatternFill("solid", fgColor="FDE2E2")))

ws = wb.create_sheet("Suivi des performances"); title(ws, "Tableau de suivi", "Calculé automatiquement depuis l'onglet Journal. On suit la DISCIPLINE avant le résultat.")
stats = [("Nombre de trades", "=COUNTA(Journal!A5:A204)"), ("Trades conformes au plan", '=COUNTIF(Journal!N5:N204,"Oui")'), ("Taux de respect du plan", "=IF(B4=0,\"\",B5/B4)"), ("R total", "=SUM(Journal!M5:M204)"), ("R moyen par trade", "=IF(B4=0,\"\",B7/B4)"), ("Trades gagnants", '=COUNTIF(Journal!L5:L204,">0")'), ("Taux de réussite", "=IF(B4=0,\"\",B9/B4)"), ("Émotion moyenne avant trade", "=IFERROR(AVERAGE(Journal!O5:O204),\"\")"), ("Pire trade (R)", "=IFERROR(MIN(Journal!M5:M204),\"\")")]
for i, (k, f) in enumerate(stats, 4):
    ws.cell(row=i, column=1, value=k); c = ws.cell(row=i, column=2, value=f)
    if "Taux" in k: c.number_format = "0.0%"
    if "R " in k or "(R)" in k: c.number_format = '0.00" R"'
ws["A14"] = "Objectif d'apprentissage : taux de respect du plan ≥ 80 % sur 4 semaines avant d'envisager le réel."; ws["A14"].font = Font(bold=True, color="2F5FFF")
ws.column_dimensions["A"].width = 40; ws.column_dimensions["B"].width = 16

ws = wb.create_sheet("Préparation hebdo"); title(ws, "Préparation de la semaine", "À remplir le dimanche.")
header(ws, 4, ["Jour", "Annonces économiques (heure, impact)", "Niveaux clés", "Marchés / UT", "Objectif d'apprentissage du jour", "Séance prévue ?"], [12, 40, 30, 18, 40, 14])
for i, j in enumerate(["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"], 5):
    ws.cell(row=i, column=1, value=j)
    for k in range(2, 7): ws.cell(row=i, column=k).fill = INP
ws["A11"] = "Objectif de la semaine (compétence, pas de gain) :"; ws["A12"].fill = INP; ws["A13"] = "Règle à travailler cette semaine :"; ws["A14"].fill = INP

ws = wb.create_sheet("Revue mensuelle"); title(ws, "Revue mensuelle", "À remplir le dernier jour du mois.")
header(ws, 4, ["Indicateur", "Semaine 1", "Semaine 2", "Semaine 3", "Semaine 4", "Commentaire"], [30, 12, 12, 12, 12, 40])
for i, k in enumerate(["Nombre de trades", "Respect du plan (%)", "R total", "Limite du jour dépassée (nb)", "Émotion moyenne (1-5)", "Erreur principale"], 5):
    ws.cell(row=i, column=1, value=k)
    for c in range(2, 7): ws.cell(row=i, column=c).fill = INP
for i, k in enumerate(["Biais principal du mois", "Ce qui a progressé", "Ce qui a régressé", "Modification du plan (une seule)", "Objectif d'apprentissage du mois prochain", "Décision : rester en démo / critères réels remplis (voir checklist)"], 13):
    ws.cell(row=i, column=1, value=k).font = Font(bold=True); ws.merge_cells(start_row=i, start_column=2, end_row=i, end_column=6); ws.cell(row=i, column=2).fill = INP

ws = wb.create_sheet("Plan de trading"); title(ws, "Mon plan de trading", "Version : ___ · Date : ___ · Une règle = une phrase vérifiable par oui/non.")
header(ws, 4, ["Rubrique", "Ma règle", "Vérifiable (oui/non) ?"], [26, 80, 20])
for i, k in enumerate(["Marchés tradés", "Horaires de séance", "Unités de temps (3)", "Conditions d'entrée", "Invalidation (stop)", "Règles de sortie", "Risque par trade (%)", "Limites jour / semaine", "Annonces économiques", "Nombre max de trades / jour", "Règles d'arrêt de séance", "Règle après une perte", "Règle après un gain"], 5):
    ws.cell(row=i, column=1, value=k).font = Font(bold=True); ws.cell(row=i, column=2).fill = INP; ws.cell(row=i, column=3).fill = INP

ws = wb.create_sheet("Checklists"); title(ws, "Les 20 checklists TIA", "Imprime-les ou coche la colonne B.")
r = 4
for t_, items in C.CHECKLISTS:
    ws.cell(row=r, column=1, value=t_).font = Font(bold=True, color="FFFFFF"); ws.cell(row=r, column=1).fill = BLUEF; ws.cell(row=r, column=2).fill = BLUEF; r += 1
    for it in items: ws.cell(row=r, column=1, value=it); ws.cell(row=r, column=2, value="☐"); r += 1
    r += 1
ws.column_dimensions["A"].width = 90; ws.column_dimensions["B"].width = 6
wb.save(OUT / "TIA_Templates.xlsx")

# ---------------------------------------------------------------- Pack Notion (CSV importables + pages markdown)
NP = OUT / "Notion_TIA"; NP.mkdir(exist_ok=True)
with open(NP / "Prompts_IA.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(["Nom", "ID", "Catégorie", "Étape DÉCISION", "Objectif", "Quand l'utiliser", "Prompt", "Exemple de remplissage", "Vérification humaine"])
    for p in prompts: w.writerow([p["title"], p["id"], p["cat"], p["step"], p["obj"], p["when"], p["text"], p["example"], p["verif"]])
with open(NP / "Checklists.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(["Point", "Checklist", "Fait"])
    for t_, items in C.CHECKLISTS:
        for it in items: w.writerow([it, t_, "No"])
with open(NP / "Journal_de_trading.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(["Trade", "Date", "Marché", "Sens", "UT", "Raison", "Entrée", "Stop", "Objectif", "Risque €", "Résultat €", "Résultat R", "Plan respecté", "Émotion avant", "Émotion après", "Tags", "Leçon"])
    w.writerow(["EXEMPLE FICTIF", "2026-11-03", "EUR/USD", "Vente", "15 min", "Retour sous 1,0860", 1.0860, 1.0880, 1.0820, 100, 50, 0.5, "No", 4, 3, "sortie anticipée", "Laisser travailler le plan."])
with open(NP / "Modules.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(["Module", "Code", "Contenu", "Outils", "Prompts", "Validation", "Terminé"])
    for m in C.MODULES: w.writerow([m[1], m[0], m[2], m[3], m[4], m[5], "No"])
md = ["# Méthode DÉCISION — Trading IA Academy", "", "> Tu ne suis le signal de personne. Tu prends ta décision, avec l'IA comme copilote.", ""]
for l, nm, fn, what, tool, pr in C.METHOD: md += [f"## {l} — {nm} ({fn})", what, f"- Outil : {tool}", f"- Prompts : {pr}", ""]
(NP / "Methode_DECISION.md").write_text("\n".join(md), encoding="utf-8")
wf = ["# Workflows TIA", ""]
for k, steps in C.WORKFLOWS.items(): wf += [f"## {k}"] + [f"- [ ] {s_}" for s_ in steps] + [""]
(NP / "Workflows.md").write_text("\n".join(wf), encoding="utf-8")
(NP / "LISEZMOI_import_Notion.md").write_text("""# Importer l'espace TIA dans Notion
1. Dans Notion, crée une page « Trading IA Academy ».
2. Menu ⋯ → Importer → CSV : importe `Prompts_IA.csv`, `Checklists.csv`, `Journal_de_trading.csv` et `Modules.csv`. Chacun devient une base de données.
3. Importe `Methode_DECISION.md` et `Workflows.md` (Importer → Texte et Markdown).
4. Dans la base Prompts, crée une vue groupée par « Étape DÉCISION ». Dans Checklists, une vue groupée par « Checklist ». Dans Journal, change « Plan respecté » en propriété Case à cocher.
5. Supprime la ligne EXEMPLE FICTIF du journal quand tu commences.
""", encoding="utf-8")

# Markdown complet (pour Google Docs / autres agents)
import subprocess
subprocess.run(["pandoc", str(OUT / "TIA_Boite_a_outils_et_plan_amelioration.docx"), "-t", "gfm", "-o", str(OUT / "TIA_Boite_a_outils_et_plan_amelioration.md")], check=False)
print("ok", len(prompts), "prompts,", len(C.CHECKLISTS), "checklists")
