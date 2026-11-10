*Version 1 · 8 novembre 2026 · Document de travail pour le formateur*

**Rappel non négociable : formation pédagogique. Aucune promesse de
gains, aucun signal d'achat ou de vente, aucun conseil personnalisé. Le
trading comporte un risque de perte en capital. Tous les exemples
chiffrés sont fictifs.**

# Sommaire du livrable

- 1\. Audit complet

- 2\. Liste des améliorations

- 3\. Nouveaux modules

- 4\. Nouveaux outils (outils IA)

- 5\. Nouveaux bonus

- 6\. Nouveaux prompts IA (100)

- 7\. Nouveaux templates

- 8\. Nouvelle méthode propriétaire

- 9\. Plan d'implémentation

- 10\. Ordre de priorité

- Annexes : 20 checklists, 3 workflows, FAQ intégrée par module

# 1. Audit complet de la formation actuelle (v1)

Base analysée : Formation_Quentia_complete_v1 (modules 0 à 6, bonus
études de cas, 20 prompts, parcours de 30 jours avec XP, journal Excel,
certification).

| **Module**                    | **Points forts**                                                             | **Ce qui manque / à améliorer**                                                                                         | **Correction proposée**                                                                                                  |
|-------------------------------|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Module 0 · Bienvenue          | Bon cadrage (règles, boucle d'apprentissage, XP).                            | Pas d'installation guidée des outils ; l'élève ne sait pas quoi ouvrir le jour 1.                                       | Ajouter une leçon « Installer ton cockpit » : Notion, Excel, ChatGPT, compte démo, avec checklist d'installation.        |
| Module 1 · Les bases          | Bonne pédagogie du levier et de la vérification des courtiers (AMF, REGAFI). | Peu d'exercices de lecture de graphique ; pas de glossaire téléchargeable.                                              | Ajouter une fiche glossaire, 3 graphiques commentés, quiz noté, checklist « choisir un intermédiaire ».                  |
| Module 2 · Le risque          | Point fort : règle des 1 %, série de pertes, formule de taille de position.  | Le calcul reste théorique tant que l'élève ne le pratique pas sur ses propres chiffres.                                 | Brancher le Plan de risque Excel (calcul automatique) + 10 exercices chiffrés corrigés + limites journalières/hebdo.     |
| Module 3 · IA                 | Bonne posture : l'IA prépare et relit, elle ne décide pas.                   | 20 prompts seulement, sans « quand l'utiliser » ni étape de vérification ; pas de démonstration de mauvaise réponse IA. | Passer à 100 prompts classés par étape DÉCISION + checklist de vérification + démo « l'IA se trompe : comment le voir ». |
| Module 4 · Journal            | Le journal Excel existe déjà, c'est un vrai atout.                           | Le lien journal → amélioration n'est pas outillé (pas de revue hebdo/mensuelle).                                        | Ajouter les tableaux de suivi (taux de respect du plan, R moyen) + revues hebdo et mensuelle + version Notion.           |
| Module 5 · Psychologie        | Les 6 biais sont pertinents.                                                 | Contenu surtout théorique ; pas d'outil le jour où l'émotion arrive.                                                    | Checklists « après une perte » / « après un gain », échelle d'état émotionnel dans le journal, prompts de débrief.       |
| Module 6 · Méthode + 30 jours | Le plan de 30 jours donne un cap.                                            | La méthode n'a pas de nom ni de structure mémorisable ; le plan de trading n'a pas de template.                         | Introduire la Méthode DÉCISION dès le module 0 et la faire vivre dans chaque module ; template de plan de trading.       |
| Bonus · Études de cas         | Rend la méthode concrète.                                                    | Risque de glisser vers « regardez mes gains ».                                                                          | Format fixe : contexte → plan → exécution → erreur/respect → leçon, en R et sans montant. Inclure des cas perdants.      |
| Transversal                   | Cadre légal solide (démo, aucune promesse, avertissements).                  | Leçons majoritairement théoriques ; peu de livrables concrets ; questions récurrentes non anticipées.                   | Format de leçon imposé en 7 blocs, FAQ intégrée par module, boîte à outils téléchargeable.                               |

**Diagnostic global : le cadre (sérieux, légal, pédagogique) est solide,
mais l'élève repart surtout avec des connaissances. Il manque des outils
exploitables dès le jour 1, une méthode nommée qui relie tout, et une
boucle d'amélioration outillée (revues). La v2 corrige ces trois
points.**

# 2. Liste des améliorations

- Créer une méthode propriétaire nommée (Méthode DÉCISION) présente dans
  chaque module.

- Passer de 20 à 100 prompts, classés par étape, avec vérification
  humaine obligatoire.

- Créer 20 checklists couvrant toute la journée du trader.

- Fournir 6 templates Excel avec calculs automatiques + un espace
  Notion.

- Imposer un format de leçon en 7 blocs (aucune leçon uniquement
  théorique).

- Ajouter les workflows quotidien, hebdomadaire et mensuel.

- Intégrer une FAQ par module pour réduire les demandes au support.

- Transformer les études de cas en format fixe, dont des cas perdants.

- Ajouter fiches de révision, quiz notés et projet final évalué.

- Garder et renforcer la gamification (XP, niveaux) liée aux livrables,
  pas aux gains.

# 3. Nouveaux modules (v2)

| **\#** | **Module**                                       | **Contenu**                                                                                                                      | **Outils livrés**                                          | **Prompts**      | **Validation**                                           |
|--------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|------------------|----------------------------------------------------------|
| M0     | Démarrage : installer ton cockpit                | Installer Notion, le classeur Excel TIA, ChatGPT et un compte démo chez un intermédiaire vérifié. Découvrir la Méthode DÉCISION. | Checklist d'installation · Espace Notion TIA               | P01, P02         | Captures de ton espace prêt                              |
| M1     | Les bases du trading                             | Marchés, ordres, levier, spread, horaires, vérification AMF/REGAFI.                                                              | Glossaire · Checklist « choisir un intermédiaire »         | P03, P11         | Quiz 10 questions                                        |
| M2     | Comprendre le marché (étape É)                   | Tendance, structure, zones, volatilité, lecture multi-timeframe.                                                                 | Checklist multi-timeframe · Fiche de lecture               | P11–P30          | Décrire 3 graphiques, comparer à la correction           |
| M3     | Gestion du risque (étape S)                      | Règle du % fixe, R, taille de position, limites jour/semaine, série de pertes.                                                   | Plan de risque Excel (calcul auto)                         | P41–P50          | 10 calculs corrigés                                      |
| M4     | L'IA comme copilote (étapes C et I)              | Écrire un bon prompt, donner le contexte, limites et hallucinations, vérification humaine.                                       | Bibliothèque de 100 prompts · Checklist de vérification IA | P31–P40          | Faire critiquer une analyse et repérer 2 erreurs de l'IA |
| M5     | Ton plan de trading (étape I)                    | Règles d'entrée, invalidation, sortie, horaires, marchés, scénarios si/alors.                                                    | Template Plan de trading                                   | P51–P60          | Plan écrit, relu par l'IA puis validé par toi            |
| M6     | Psychologie et discipline                        | FOMO, revanche, excès de confiance, biais de confirmation ; règles d'arrêt.                                                      | Checklists après perte / après gain · Échelle d'émotion    | P86–P95          | Identifier ton biais n°1 dans ton journal                |
| M7     | Journal et amélioration continue (étapes O et N) | Tenir un journal utile, mesurer la discipline, corriger une règle à la fois.                                                     | Journal · Suivi des performances · Revues hebdo/mensuelle  | P61–P85          | 2 semaines de journal + 1 revue hebdo                    |
| M8     | Ta routine (workflows)                           | Workflow quotidien, hebdomadaire et mensuel de la Méthode DÉCISION.                                                              | Les 3 workflows · Préparation hebdo                        | P01–P10, P76–P85 | Suivre la routine 7 jours                                |
| M9     | Études de cas                                    | Cas commentés au format fixe, dont des cas perdants.                                                                             | Fiche d'étude de cas                                       | P96–P100         | Rédiger ta propre étude de cas                           |
| Final  | Projet final et attestation                      | Présenter ton plan, 30 jours de journal démo et ta revue mensuelle.                                                              | Grille d'évaluation                                        | —                | Attestation privée TIA                                   |

## Format imposé de chaque leçon

| **Bloc**              | **Contenu**                                                                         |
|-----------------------|-------------------------------------------------------------------------------------|
| Théorie               | 5 à 8 minutes maximum, une seule idée.                                              |
| Démonstration         | Écran + voix : le formateur applique l'idée sur un vrai graphique.                  |
| Cas réel              | Une situation concrète, gagnante ou perdante, exprimée en R, sans montant d'argent. |
| Exercice              | L'élève refait la démonstration sur son compte démo ou sur un graphique historique. |
| Template associé      | Le fichier à remplir (Excel ou Notion) correspondant à la leçon.                    |
| Prompt IA associé     | Le prompt de la bibliothèque à utiliser, avec l'étape de vérification.              |
| Validation des acquis | Quiz de 3 à 5 questions ou livrable à cocher dans Notion (+XP).                     |

# 4. Nouveaux outils : outils IA recommandés

*Prix indicatifs relevés en novembre 2026 : à vérifier sur le site
officiel avant de les communiquer aux élèves.*

| **Outil**             | **Utilité dans TIA**                                                                                          | **Prix**                                                | **Avantages**                                                           | **Inconvénients**                                                                  | **Niveau**               |
|-----------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|-------------------------------------------------------------------------|------------------------------------------------------------------------------------|--------------------------|
| ChatGPT (OpenAI)      | Assistant principal : structurer une analyse, expliquer, relire un plan, utiliser la bibliothèque de prompts. | Gratuit ; offres payantes à partir d'environ 20 \$/mois | Très polyvalent, facile, version gratuite suffisante pour la formation. | Peut inventer des chiffres ; n'a pas toujours les données de marché en temps réel. | Débutant                 |
| Claude (Anthropic)    | Relire et critiquer un plan long, analyser un journal complet, rédiger des études de cas.                     | Gratuit ; offres payantes à partir d'environ 20 \$/mois | Excellent sur les longs documents et le raisonnement structuré.         | Pas de graphiques de marché intégrés ; limites d'usage en gratuit.                 | Débutant à intermédiaire |
| Gemini (Google)       | Assistant intégré à Google Sheets/Docs : analyser un journal tenu dans Sheets.                                | Gratuit ; offre payante intégrée à Google One           | Intégration à Google Sheets et Docs.                                    | Qualité variable selon les tâches.                                                 | Débutant                 |
| Perplexity            | Recherche avec sources citées : comprendre une actualité ou une annonce économique.                           | Gratuit ; offre Pro payante                             | Cite ses sources, pratique pour vérifier.                               | Les sources restent à vérifier soi-même.                                           | Débutant                 |
| NotebookLM (Google)   | Réviser la formation : y charger ses fiches et son plan pour poser des questions dessus.                      | Gratuit                                                 | Répond à partir de TES documents, limite les inventions.                | Ne remplace pas l'analyse de graphique.                                            | Débutant                 |
| TradingView           | Graphiques, multi-unités de temps, tracés, alertes, mode « replay » pour s'entraîner sur l'historique.        | Gratuit ; offres payantes                               | Référence des graphiques, replay idéal pour le backtest manuel.         | Pas un outil d'IA ; les fonctions avancées sont payantes.                          | Débutant à avancé        |
| Notion (+ Notion AI)  | Espace TIA : journal, checklists, prompts, revues.                                                            | Gratuit pour un usage personnel ; IA en option payante  | Tout centraliser, bases de données filtrables.                          | Prise en main de quelques heures.                                                  | Débutant                 |
| Excel / Google Sheets | Plan de risque, journal et suivi des performances avec calculs automatiques.                                  | Google Sheets gratuit ; Excel inclus dans Microsoft 365 | Calculs fiables et transparents, aucune boîte noire.                    | Moins visuel que Notion.                                                           | Débutant                 |

# 5. Nouveaux bonus premium

| **Bonus**                         | **Description**                                                                                                               |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Pack de 100 prompts IA            | Classés par étape de la Méthode DÉCISION, chacun avec objectif, moment d'utilisation, exemple et vérification humaine.        |
| Bibliothèque de 20 checklists     | De la préparation de séance au passage en réel, imprimables et dans Notion.                                                   |
| Espace Notion TIA                 | Journal, checklists, prompts et revues en bases de données prêtes à importer.                                                 |
| Classeur Excel TIA                | Journal, plan de trading, plan de risque avec calcul automatique, suivi des performances, préparation hebdo, revue mensuelle. |
| Fiches de révision                | Une page par module : idées clés, erreurs à éviter, quiz.                                                                     |
| Bibliothèque d'erreurs fréquentes | Les erreurs classiques des débutants, comment les repérer et la règle qui les évite.                                          |
| Plans d'action                    | Plans de 14 jours pour corriger une faiblesse précise (sortie anticipée, revanche, surtrading…).                              |
| Workflows imprimables             | Routines quotidienne, hebdomadaire et mensuelle sur une page.                                                                 |

# 6. Bibliothèque de 100 prompts IA

**Mode d'emploi commun : copie le prompt, remplace les \[CROCHETS\] par
tes informations, colle-le dans ton IA. Avant d'utiliser la réponse,
applique toujours la vérification humaine (étape I de la Méthode
DÉCISION).**

## Préparation et collecte des données — étape D

*Quand l'utiliser : Avant la séance, pendant la phase Données.*

*Exemple de remplissage : \[MARCHÉ\] = EUR/USD · \[NOTES\] = « annonce
de l'inflation US à 14 h 30, marché en range depuis hier entre 1,0820 et
1,0870 » (exemple fictif)*

**P01 · Brief de séance**

Objectif : Organiser les infos du jour en un brief clair.

> Voici mes notes du jour sur \[MARCHÉ\] : \[NOTES\]. Organise-les en un
> brief de séance en 5 rubriques : contexte, niveaux clés, annonces,
> risques, questions à vérifier. N'ajoute aucune information que je n'ai
> pas donnée et ne fais aucune recommandation d'achat ou de vente.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P02 · Calendrier économique expliqué**

Objectif : Comprendre les annonces du jour.

> Voici les annonces économiques du jour : \[LISTE\]. Explique
> simplement ce que mesure chacune et pourquoi elle peut augmenter la
> volatilité sur \[MARCHÉ\]. Ne prédis pas le résultat de l'annonce.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P03 · Glossaire express**

Objectif : Comprendre un terme inconnu.

> Explique le terme « \[TERME\] » à un débutant en trading, en 5 lignes,
> avec un exemple chiffré fictif clairement indiqué comme fictif.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P04 · Questions à se poser**

Objectif : Préparer son esprit critique.

> Je prépare une séance sur \[MARCHÉ\] en unité de temps \[UT\].
> Donne-moi 10 questions à me poser avant d'analyser le graphique, pour
> éviter les biais de confirmation.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P05 · Résumé de la veille**

Objectif : Repartir de son propre historique.

> Voici mon journal d'hier : \[JOURNAL\]. Résume en 5 points : ce que
> j'ai bien fait, mes erreurs, la règle de mon plan la plus souvent
> oubliée et une action concrète pour aujourd'hui.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P06 · Organiser mes niveaux**

Objectif : Mettre ses niveaux au propre.

> Voici les niveaux que j'ai repérés sur \[MARCHÉ\] : \[NIVEAUX + UT\].
> Classe-les du plus haut au plus bas dans un tableau (niveau, unité de
> temps, raison) sans en inventer de nouveaux.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P07 · Check-list personnalisée**

Objectif : Adapter la checklist à son plan.

> Voici mon plan de trading : \[PLAN\]. Transforme-le en checklist de
> préparation de séance de 8 points maximum, à cocher avant chaque
> séance.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P08 · Contexte de volatilité**

Objectif : Comprendre la notion de volatilité.

> Explique comment mesurer la volatilité de \[MARCHÉ\] avec l'ATR sur
> \[UT\], et comment elle doit influencer la taille de ma position.
> Utilise un exemple fictif indiqué comme tel.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P09 · Sources fiables**

Objectif : Savoir où vérifier.

> Liste les types de sources officielles où vérifier : un calendrier
> économique, l'autorisation d'un courtier en France, une donnée
> macroéconomique. N'invente pas d'adresse web : décris le type de
> source.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P10 · Objectif de séance**

Objectif : Donner un but d'apprentissage.

> Mon niveau : \[NIVEAU\]. Mon erreur récente : \[ERREUR\]. Propose-moi
> un objectif d'APPRENTISSAGE (pas de gain) pour la séance
> d'aujourd'hui, mesurable dans mon journal.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

## Lecture de marché et tendance — étape É

*Quand l'utiliser : Pendant l'étude du graphique.*

*Exemple de remplissage : \[MARCHÉ\] = CAC 40 · \[UT\] = 1 heure ·
\[DESCRIPTION\] = « sommets de plus en plus hauts depuis 3 jours,
dernier creux à 7 450 » (exemple fictif)*

**P11 · Décrire sans prédire**

Objectif : Apprendre à décrire objectivement.

> Je te décris un graphique de \[MARCHÉ\] en \[UT\] : \[DESCRIPTION\].
> Reformule ma description de façon objective (tendance, structure,
> zones) et signale les endroits où je fais une prédiction au lieu d'une
> observation.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P12 · Identifier la tendance**

Objectif : Classer la tendance.

> Voici les 6 derniers sommets et creux de \[MARCHÉ\] en \[UT\] :
> \[VALEURS\]. Indique si la structure est haussière, baissière ou en
> range selon la définition sommets/creux, et explique ton raisonnement
> étape par étape.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P13 · Zones importantes**

Objectif : Comprendre pourquoi une zone compte.

> Voici une zone que j'ai repérée : \[ZONE\] sur \[MARCHÉ\] \[UT\],
> touchée \[N\] fois. Explique quels critères rendent une zone
> significative et lesquels manquent à la mienne.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P14 · Phase de marché**

Objectif : Reconnaître la phase.

> D'après ces observations : \[OBSERVATIONS\], la phase de marché
> ressemble-t-elle à une tendance, un range ou une transition ? Donne
> les indices pour et contre chaque hypothèse.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P15 · Lecture d'une bougie**

Objectif : Comprendre une configuration.

> Explique ce que peut indiquer une bougie \[TYPE\] à proximité de
> \[ZONE\], ses limites, et pourquoi elle ne suffit jamais seule à
> justifier un trade.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P16 · Indicateur expliqué**

Objectif : Comprendre un indicateur.

> Explique l'indicateur \[INDICATEUR\] : calcul, interprétation
> courante, pièges fréquents des débutants, et comment l'utiliser comme
> simple confirmation.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P17 · Biais de confirmation**

Objectif : Tester sa lecture.

> Voici ma lecture de \[MARCHÉ\] : \[LECTURE\]. Joue l'avocat du diable
> : donne les 5 meilleurs arguments contre ma lecture.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P18 · Comparer deux lectures**

Objectif : Arbitrer entre deux hypothèses.

> Hypothèse A : \[A\]. Hypothèse B : \[B\]. Quels éléments observables
> sur le graphique permettraient de départager A et B ? Ne choisis pas à
> ma place.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P19 · Résumé de lecture**

Objectif : Synthétiser en 3 lignes.

> Résume ma lecture suivante en 3 lignes maximum, sans ajouter
> d'information : \[LECTURE\].

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P20 · Erreurs de lecture courantes**

Objectif : Prévenir les erreurs.

> Quelles sont les 7 erreurs les plus fréquentes des débutants quand ils
> lisent une tendance sur \[UT\] ? Donne pour chacune un moyen simple de
> la repérer.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

## Analyse multi-timeframe — étape É

*Quand l'utiliser : Quand tu compares plusieurs unités de temps.*

*Exemple de remplissage : \[UT1\] = Jour : tendance haussière · \[UT2\]
= 4 h : range · \[UT3\] = 15 min : baisse de court terme (exemple
fictif)*

**P21 · Cohérence des unités de temps**

Objectif : Vérifier l'alignement.

> Lecture en \[UT1\] : \[L1\]. En \[UT2\] : \[L2\]. En \[UT3\] : \[L3\].
> Ces lectures sont-elles cohérentes ? Liste les points d'accord et de
> désaccord.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P22 · Choisir ses 3 unités de temps**

Objectif : Construire son trio d'UT.

> Je trade pendant \[DURÉE\] par séance sur \[MARCHÉ\]. Propose 3
> combinaisons d'unités de temps possibles avec avantages et
> inconvénients pour un débutant.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P23 · Du haut vers le bas**

Objectif : Appliquer l'analyse descendante.

> Guide-moi étape par étape pour analyser \[MARCHÉ\] de \[UT longue\] à
> \[UT courte\], en me posant une question à chaque étape. Attends ma
> réponse avant de passer à la suivante.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P24 · Conflit d'unités de temps**

Objectif : Gérer un désaccord.

> Mon UT longue est \[LECTURE\] et mon UT courte est \[LECTURE\].
> Quelles règles de prudence un plan de trading peut-il prévoir dans ce
> cas ?

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P25 · Zone multi-UT**

Objectif : Repérer une zone commune.

> Voici mes zones en \[UT1\] : \[Z1\] et en \[UT2\] : \[Z2\]. Lesquelles
> se chevauchent ? Présente le résultat en tableau, sans en inventer.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P26 · Piège du zoom**

Objectif : Éviter de chercher une entrée.

> Explique le piège qui consiste à changer d'unité de temps jusqu'à
> trouver une entrée qui confirme son envie, et donne une règle pour
> l'éviter.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P27 · Fiche multi-UT**

Objectif : Créer sa fiche.

> Crée une fiche de lecture multi-unités de temps en tableau (UT,
> tendance, zone clé, remarque) que je remplirai à chaque séance.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P28 · Contexte de fond**

Objectif : Comprendre la tendance de fond.

> À partir de cette description en \[UT longue\] : \[DESCRIPTION\],
> explique ce que signifie « trader dans le sens de la tendance de fond
> » et ses limites.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P29 · Timing d'entrée**

Objectif : Comprendre le rôle de l'UT courte.

> Explique le rôle de l'unité de temps courte dans la préparation d'une
> entrée, et pourquoi elle ne doit jamais contredire le plan.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P30 · Auto-évaluation multi-UT**

Objectif : Se corriger.

> Voici ma fiche multi-UT remplie : \[FICHE\]. Note sa clarté de 1 à 10
> et indique ce qui manque pour qu'elle soit exploitable.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

## Analyse IA structurée (copilote) — étape C

*Quand l'utiliser : Quand tu fais travailler l'IA sur ta lecture.*

*Exemple de remplissage : \[ANALYSE\] = « Or en tendance haussière en
journalier, retour sur la zone 2 310–2 320 en 4 h, annonce de la Fed
demain » (exemple fictif)*

**P31 · Structurer mon analyse**

Objectif : Mettre en forme.

> Voici mon analyse brute de \[MARCHÉ\] : \[ANALYSE\]. Structure-la en :
> contexte, observations, hypothèses, éléments à vérifier. Ne fais
> aucune recommandation d'achat ou de vente.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P32 · Lister les incertitudes**

Objectif : Rendre l'incertitude visible.

> D'après cette analyse : \[ANALYSE\], liste tout ce qui est incertain
> ou non vérifié, du plus important au moins important.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P33 · Scénario contraire**

Objectif : Préparer l'inverse.

> Mon scénario principal est : \[SCÉNARIO\]. Décris le scénario
> contraire et les signes observables qui indiqueraient qu'il se
> produit.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P34 · Questions de l'IA**

Objectif : Se faire interroger.

> Pose-moi une à une 5 questions exigeantes sur mon analyse :
> \[ANALYSE\]. Attends ma réponse après chaque question.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P35 · Critique notée**

Objectif : Évaluer la qualité.

> Note mon analyse de 1 à 10 sur : objectivité, clarté, cohérence
> multi-UT, gestion du risque. Justifie chaque note. Analyse :
> \[ANALYSE\].

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P36 · Simplifier**

Objectif : Clarifier un raisonnement confus.

> Mon raisonnement est confus : \[TEXTE\]. Reformule-le en étapes
> numérotées et signale les sauts logiques.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P37 · Vérifier la cohérence avec le plan**

Objectif : Respect du plan.

> Mon plan de trading : \[PLAN\]. Mon idée de trade : \[IDÉE\]. Liste
> chaque règle du plan et indique si l'idée la respecte, ne la respecte
> pas, ou si l'information manque.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P38 · Détecter une hallucination**

Objectif : Former son œil critique.

> Relis ta réponse précédente et liste toutes les affirmations que tu ne
> peux pas garantir (prix, dates, chiffres). Indique comment je peux les
> vérifier moi-même.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P39 · Expliquer comme à un débutant**

Objectif : Comprendre une analyse complexe.

> Explique cette analyse à un débutant complet, en 8 lignes, sans jargon
> : \[ANALYSE\].

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P40 · Synthèse décisionnelle**

Objectif : Préparer MA décision.

> Résume en tableau les éléments pour, contre et incertains de mon idée
> : \[IDÉE\]. Termine par : « La décision t'appartient », sans
> recommander d'action.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

## Gestion du risque — étape S

*Quand l'utiliser : Avant toute entrée, et pour régler ses limites.*

*Exemple de remplissage : \[CAPITAL\] = 10 000 € (démo) · \[RISQUE\] = 1
% · \[ENTRÉE\] = 100 · \[STOP\] = 95 → taille attendue 20 unités
(exemple fictif)*

**P41 · Taille de position**

Objectif : Calculer sans erreur.

> Capital : \[CAPITAL\] €. Risque par trade : \[RISQUE\] %. Entrée :
> \[ENTRÉE\]. Stop : \[STOP\]. Calcule la taille de position avec la
> formule (Capital × Risque %) ÷ \|Entrée − Stop\| et montre chaque
> étape. Je vérifierai avec mon Plan de risque Excel.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P42 · Série de pertes**

Objectif : Mesurer l'impact.

> Avec un risque de \[RISQUE\] % par trade, calcule l'effet de \[N\]
> pertes consécutives sur un capital de \[CAPITAL\] €, étape par étape
> (calcul composé).

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P43 · Limites journalières**

Objectif : Fixer ses garde-fous.

> Je risque \[RISQUE\] % par trade et je fais au maximum \[N\] trades
> par jour. Propose des limites de perte journalière et hebdomadaire
> cohérentes pour un débutant, avec la logique de chaque limite.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P44 · Ratio gain/risque**

Objectif : Comprendre le ratio.

> Entrée \[ENTRÉE\], stop \[STOP\], objectif \[OBJECTIF\]. Calcule le
> ratio gain/risque et explique le taux de réussite minimum nécessaire
> pour être à l'équilibre avec ce ratio.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P45 · Levier expliqué**

Objectif : Comprendre son levier.

> Explique ce que signifie un levier de \[LEVIER\] sur un mouvement de
> \[MOUVEMENT\] % avec une mise de \[MISE\] € (exemple fictif), et le
> risque de perte supérieure à la mise prévue.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P46 · Audit de mes limites**

Objectif : Contrôler ses règles.

> Voici mes règles de risque : \[RÈGLES\]. Repère les incohérences ou
> les trous (ce qui n'est pas prévu).

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P47 · Stop logique**

Objectif : Placer un stop cohérent.

> Explique la différence entre un stop placé sur un montant arbitraire
> et un stop placé au niveau d'invalidation du scénario. Donne un
> exemple fictif.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P48 · Ajustement à la volatilité**

Objectif : Adapter la taille.

> Si l'ATR de \[MARCHÉ\] passe de \[ATR1\] à \[ATR2\], comment la taille
> de position doit-elle évoluer à risque constant ? Montre le calcul.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P49 · Règles anti-revanche**

Objectif : Se protéger de soi-même.

> Propose 5 règles de risque qui empêchent le trading de revanche après
> une perte, formulées de façon vérifiable dans un journal.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P50 · Check risque express**

Objectif : Contrôle final.

> Voici mon trade prévu : \[TRADE\]. Vérifie point par point : risque ≤
> \[RISQUE\] %, stop défini, taille calculée, limite du jour non
> atteinte. Réponds par OK / À CORRIGER pour chaque point.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

## Plan de trading et scénarios — étape I

*Quand l'utiliser : Quand tu écris ou ajustes ton plan.*

*Exemple de remplissage : \[IDÉE\] = « si le prix revient sur 1,0820 et
forme un creux plus haut en 15 min, alors j'étudie une entrée ;
invalidation sous 1,0805 » (exemple fictif)*

**P51 · Rédiger mon plan**

Objectif : Créer un premier plan.

> Aide-moi à écrire mon plan de trading en me posant les questions une
> par une sur : marchés, horaires, unités de temps, entrée,
> invalidation, sortie, risque, annonces, règles d'arrêt. Attends mes
> réponses.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P52 · Scénario si/alors**

Objectif : Formaliser un scénario.

> Transforme mon idée en scénarios « si… alors… » (principal,
> alternatif, invalidation) : \[IDÉE\]. Chaque scénario doit être
> observable sur le graphique.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P53 · Relire mon plan**

Objectif : Trouver les failles.

> Voici mon plan : \[PLAN\]. Repère les règles floues, non mesurables ou
> contradictoires, et propose une reformulation mesurable pour chacune.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P54 · Plan en une page**

Objectif : Condenser.

> Résume mon plan de trading en une page imprimable, sous forme de
> règles numérotées : \[PLAN\].

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P55 · Version 2 du plan**

Objectif : Faire évoluer.

> Voici mon plan v1 : \[PLAN\] et ma revue du mois : \[REVUE\]. Propose
> UNE seule modification prioritaire, justifiée par la revue.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P56 · Règles d'entrée**

Objectif : Clarifier l'entrée.

> Mes conditions d'entrée sont : \[CONDITIONS\]. Reformule-les en
> critères vérifiables (oui/non) à cocher avant chaque trade.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P57 · Règles de sortie**

Objectif : Clarifier la sortie.

> Aide-moi à définir des règles de sortie claires (stop, objectif,
> sortie anticipée) pour ce type de trade : \[TYPE\]. Chaque règle doit
> être vérifiable.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P58 · Plan face aux annonces**

Objectif : Prévoir les annonces.

> Propose 3 politiques possibles face aux annonces économiques majeures
> (ne pas trader, réduire la taille, attendre X minutes) avec avantages
> et inconvénients.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P59 · Test du plan sur l'historique**

Objectif : Préparer un test.

> Explique comment tester mon plan à la main sur des graphiques
> historiques (backtest manuel) : étapes, nombre d'exemples conseillé,
> ce qu'il faut noter, biais à éviter.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P60 · Plan d'apprentissage 30 jours**

Objectif : Organiser son mois.

> Construis-moi un plan d'apprentissage de 30 jours en compte démo
> autour de mon plan : \[PLAN\], avec un objectif de compétence par
> semaine (pas d'objectif de gain).

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

## Journal de trading — étape O

*Quand l'utiliser : Après chaque trade et en fin de séance.*

*Exemple de remplissage : \[NOTES\] = « EUR/USD vendu à 1,0860, stop
1,0880, objectif 1,0820, sorti à 1,0840 par peur, tension 4/5 » (exemple
fictif)*

**P61 · Remplir mon journal**

Objectif : Ne rien oublier.

> Voici mes notes brutes sur un trade : \[NOTES\]. Range-les dans les
> colonnes de mon journal : date, marché, sens, raison, stop, objectif,
> taille, résultat en R, plan respecté, émotion, leçon. Laisse vide ce
> que je n'ai pas donné.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P62 · Débrief de perte**

Objectif : Apprendre d'une perte.

> Voici un trade perdant : \[TRADE\]. Aide-moi à distinguer : perte
> normale (plan respecté) ou erreur (plan non respecté). Pose-moi les
> questions nécessaires.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P63 · Débrief de gain**

Objectif : Ne pas tirer de mauvaise leçon.

> Voici un trade gagnant : \[TRADE\]. Vérifie si le plan a été respecté
> et si le gain peut venir d'une erreur chanceuse.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P64 · Leçon en une phrase**

Objectif : Synthétiser.

> Résume la leçon de ce trade en une phrase actionnable pour mon
> prochain trade : \[TRADE\].

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P65 · Tags du journal**

Objectif : Classer ses erreurs.

> Propose une liste de 10 étiquettes (tags) pour classer mes trades et
> mes erreurs dans mon journal, avec une définition courte pour chacune.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P66 · Trades non pris**

Objectif : Valoriser la patience.

> Voici un trade que je n'ai pas pris : \[SITUATION\]. Aide-moi à noter
> pourquoi, et si c'était conforme à mon plan.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P67 · Analyse des émotions**

Objectif : Relier émotion et décision.

> Voici les notes d'émotion de mes 10 derniers trades : \[NOTES\]. Y
> a-t-il un lien entre mon niveau de tension et le respect du plan ?
> Présente-le en tableau.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P68 · Captures commentées**

Objectif : Exploiter une capture.

> Je te décris ma capture d'écran : \[DESCRIPTION\]. Rédige un
> commentaire de 4 lignes pour mon journal : contexte, entrée, gestion,
> sortie.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P69 · Journal de la journée**

Objectif : Clôturer la séance.

> Voici mes trades du jour : \[TRADES\]. Rédige un résumé de fin de
> journée : respect du plan, R total, erreur principale, action pour
> demain.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P70 · Format de journal**

Objectif : Améliorer son journal.

> Voici les colonnes de mon journal : \[COLONNES\]. Que manque-t-il pour
> mesurer ma discipline et mes erreurs ? Propose au maximum 3 ajouts.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P71 · Calcul du R**

Objectif : Exprimer en R.

> Risque prévu \[RISQUE €\], résultat \[RÉSULTAT €\]. Exprime le
> résultat en R et explique pourquoi raisonner en R est plus utile qu'en
> euros.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P72 · Taux de respect du plan**

Objectif : Mesurer la discipline.

> Sur \[N\] trades, \[M\] respectaient le plan. Calcule mon taux de
> respect et propose un objectif réaliste pour la semaine prochaine.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P73 · Revue de série**

Objectif : Analyser 10 trades.

> Voici mes 10 derniers trades (tableau) : \[TABLEAU\]. Trouve les 3
> schémas récurrents (positifs et négatifs).

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P74 · Erreur récurrente**

Objectif : Isoler le problème n°1.

> D'après ces erreurs notées : \[ERREURS\], quelle est l'erreur la plus
> coûteuse en R et la plus fréquente ? Propose une règle pour l'éviter.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P75 · Journal vers plan**

Objectif : Boucler la boucle.

> Voici la leçon principale de ma semaine : \[LEÇON\]. Faut-il modifier
> mon plan, ma checklist ou ma routine ? Propose une seule modification.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

## Revue et amélioration continue — étape N

*Quand l'utiliser : Chaque semaine et chaque mois.*

*Exemple de remplissage : \[TABLEAU\] = 12 trades, 9 conformes au plan,
R total +1,5, erreur fréquente : sortie anticipée (exemple fictif)*

**P76 · Revue hebdomadaire**

Objectif : Faire le bilan de la semaine.

> Voici mon tableau de la semaine : \[TABLEAU\]. Calcule : nombre de
> trades, taux de respect du plan, R total, R moyen, erreur la plus
> fréquente. Propose UNE amélioration pour la semaine prochaine.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P77 · Revue mensuelle**

Objectif : Faire le bilan du mois.

> Voici mes 4 revues hebdomadaires : \[REVUES\]. Décris l'évolution de
> ma discipline, mon biais principal et propose l'objectif
> d'apprentissage du mois prochain.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P78 · Préparer la semaine**

Objectif : Anticiper.

> Voici les annonces de la semaine : \[ANNONCES\] et mes niveaux clés :
> \[NIVEAUX\]. Organise un tableau de préparation hebdomadaire jour par
> jour.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P79 · Progression de compétence**

Objectif : Mesurer l'apprentissage.

> Propose 5 indicateurs de PROGRESSION d'un trader débutant qui ne
> dépendent pas du gain (ex. respect du plan), et comment les mesurer
> dans un journal.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P80 · Démo ou réel ?**

Objectif : Décision réfléchie.

> Voici mes statistiques de démo : \[STATS\]. Liste objectivement les
> critères remplis et non remplis de la checklist « Avant de passer en
> réel ». Ne prends pas la décision à ma place.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P81 · Comparer deux mois**

Objectif : Voir l'évolution.

> Mois 1 : \[STATS1\]. Mois 2 : \[STATS2\]. Compare en tableau et
> explique ce qui a progressé et ce qui a régressé.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P82 · Plan d'action correctif**

Objectif : Corriger une faiblesse.

> Ma faiblesse principale est : \[FAIBLESSE\]. Propose un plan d'action
> sur 2 semaines avec un exercice par jour de 10 minutes.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P83 · Fiche de révision**

Objectif : Réviser un module.

> Crée une fiche de révision d'une page sur \[THÈME\] avec : 5 idées
> clés, 3 erreurs à éviter, 3 questions de quiz avec réponses.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P84 · Quiz d'auto-évaluation**

Objectif : Valider ses acquis.

> Pose-moi 5 questions à choix multiples sur \[THÈME\], une par une, et
> corrige chaque réponse avec une explication.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P85 · Mise à jour de la checklist**

Objectif : Faire évoluer ses outils.

> Voici ma checklist actuelle : \[CHECKLIST\] et mes erreurs du mois :
> \[ERREURS\]. Propose au maximum 2 points à ajouter ou reformuler.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

## Psychologie et discipline — étape N

*Quand l'utiliser : Quand une émotion prend le dessus, ou en revue.*

*Exemple de remplissage : \[SITUATIONS\] = « entré sans plan après une
forte bougie ; déplacé mon stop deux fois ; repris un trade juste après
une perte » (exemple fictif)*

**P86 · Identifier mon biais**

Objectif : Se connaître.

> Voici 5 situations où j'ai dévié de mon plan : \[SITUATIONS\]. Quels
> biais cognitifs peuvent l'expliquer (FOMO, revanche, excès de
> confiance, aversion à la perte, confirmation) ? Explique simplement.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P87 · Routine anti-FOMO**

Objectif : Résister à l'envie d'entrer.

> Propose une routine de 2 minutes à appliquer quand je ressens la peur
> de rater un mouvement, avec des questions à me poser.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P88 · Après une série de pertes**

Objectif : Garder la tête froide.

> J'ai enchaîné \[N\] pertes. Aide-moi à vérifier si mon plan a été
> respecté et propose des règles de pause, sans m'encourager à me «
> refaire ».

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P89 · Excès de confiance**

Objectif : Rester humble après des gains.

> J'ai enchaîné \[N\] gains et j'ai envie d'augmenter mon risque. Liste
> les risques de cette réaction et rappelle-moi les règles de mon plan :
> \[PLAN\].

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P90 · Journal émotionnel**

Objectif : Mettre des mots.

> Aide-moi à décrire mon état émotionnel actuel en 3 phrases et à noter
> mon niveau de tension de 1 à 5. Ensuite, pose-moi la question : «
> Est-ce le bon moment pour trader ? »

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P91 · Règles d'arrêt**

Objectif : Savoir s'arrêter.

> Propose 5 règles d'arrêt de séance (émotionnelles et chiffrées) qu'un
> débutant peut appliquer sans ambiguïté.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P92 · Recadrage d'une perte**

Objectif : Accepter la perte.

> Explique pourquoi une perte qui respecte le plan est une bonne
> exécution, avec une analogie simple.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P93 · Ennui et surtrading**

Objectif : Éviter de trader pour trader.

> Je trade souvent par ennui. Propose 3 alternatives productives pendant
> une séance sans opportunité conforme au plan.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P94 · Visualisation de séance**

Objectif : Se préparer mentalement.

> Guide-moi dans une préparation mentale de 3 minutes avant ma séance :
> rappel du plan, des limites et du scénario d'invalidation.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P95 · Bilan psychologique du mois**

Objectif : Mesurer l'évolution mentale.

> Voici mes notes d'émotion du mois : \[NOTES\]. Résume l'évolution, le
> moment le plus difficile et une habitude à garder.

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

## Études de cas — étape N

*Quand l'utiliser : Pour analyser un cas, le sien ou celui de la
formation.*

*Exemple de remplissage : \[NOTES\] = « Or, plan : achat sur retour à 2
310, invalidation 2 298 ; entré trop tôt à 2 318, stoppé, −1 R »
(exemple fictif)*

**P96 · Structurer une étude de cas**

Objectif : Format fixe.

> Transforme ces notes en étude de cas au format : contexte, plan
> initial, exécution, résultat en R, ce qui a marché, ce qui doit
> changer, leçon : \[NOTES\].

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P97 · Cas perdant pédagogique**

Objectif : Apprendre de l'échec.

> Analyse ce cas perdant sous l'angle « plan respecté ou non » et tire 3
> leçons concrètes : \[CAS\].

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P98 · Comparer deux cas**

Objectif : Repérer les différences.

> Compare ces deux trades : \[CAS A\] et \[CAS B\]. Qu'est-ce qui
> explique la différence d'exécution ?

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P99 · Questions sur un cas**

Objectif : Approfondir.

> Pose-moi 5 questions sur cette étude de cas pour vérifier que j'ai
> compris la leçon : \[CAS\].

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

**P100 · Rédiger mon étude de cas**

Objectif : Livrable final.

> Aide-moi à rédiger mon étude de cas pour le projet final à partir de
> mon journal : \[JOURNAL\], au format de la formation, sans montant en
> euros (uniquement en R).

*Vérification humaine obligatoire : Vérifie chaque prix, niveau et date
cités sur ton graphique ou une source officielle. Rejette toute
recommandation d'achat/vente : la décision est la tienne.*

# 7. Nouveaux templates

**Journal de trading**

Une ligne par trade : date, marché, sens, raison liée au plan, stop,
objectif, taille, risque €, résultat €, résultat en R (calculé), plan
respecté, émotion avant/après, tags, leçon.

**Plan de trading**

Règles numérotées et versionnées : marchés, horaires, UT, entrée,
invalidation, sortie, risque, annonces, arrêt.

**Plan de gestion du risque**

Capital, % de risque, limites jour/semaine, calculateur de taille de
position automatique.

**Suivi des performances**

Calcul automatique : nombre de trades, % de respect du plan, R total, R
moyen, taux de réussite.

**Préparation hebdomadaire**

Tableau jour par jour : annonces, niveaux, objectif d'apprentissage.

**Revue mensuelle**

Indicateurs du mois, biais principal, modification du plan, décision
démo/réel.

*Fichiers fournis : TIA_Templates.xlsx (6 onglets + checklists) et le
pack Notion (bases de données CSV à importer).*

# 8. Nouvelle méthode propriétaire

## Noms proposés

| **Nom**                       | **Pourquoi**                                                                                                                         |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Méthode DÉCISION (recommandé) | Un acronyme en 8 lettres qui colle exactement aux 8 étapes et qui dit ce qu'on apprend : prendre une décision, pas suivre un signal. |
| Protocole TIA-8               | Sobre, technique, lié à la marque. Moins mémorable pour le grand public.                                                             |
| Méthode Copilote              | Image forte de l'IA qui assiste sans piloter. Pas d'acronyme pour structurer les étapes.                                             |
| Cycle CLARTÉ                  | Évoque la fin du flou, mais seulement 6 lettres : il faut regrouper des étapes.                                                      |

## La Méthode DÉCISION — 8 étapes

| **Lettre** | **Étape**          | **Fonction**          | **Ce qu'on fait**                                                                                                                               | **Outil**                                               | **Prompts** |
|------------|--------------------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|-------------|
| D          | Données            | Collecte des données  | Rassembler le contexte avant toute analyse : calendrier économique, graphique sur 3 unités de temps, niveaux de la veille, état de ton journal. | Checklist de préparation de séance                      | P01–P10     |
| É          | Étude              | Lecture du marché     | Décrire objectivement ce que fait le marché (tendance, zones, volatilité) sans chercher à prédire.                                              | Checklist multi-timeframe                               | P11–P30     |
| C          | Copilote IA        | Analyse IA            | Faire structurer, questionner et critiquer ta lecture par l'IA avec des prompts fermés. L'IA ne donne jamais d'ordre d'achat ou de vente.       | Checklist d'analyse avec IA                             | P31–P40     |
| I          | Inspection         | Vérification humaine  | Vérifier chaque affirmation de l'IA sur le graphique et les sources. Ce qui n'est pas vérifiable est écarté.                                    | Checklist de vérification d'une réponse IA              | —           |
| S          | Sécurité           | Gestion du risque     | Fixer le risque en % du capital, le stop, la taille de position et les limites journalières AVANT d'entrer.                                     | Checklist de gestion du risque + Plan de risque (Excel) | P41–P50     |
| I          | Intention          | Planification         | Écrire le plan du trade : raison, scénario si/alors, invalidation, sortie. Pas de plan écrit, pas de trade.                                     | Plan de trading + Checklist avant d'ouvrir un trade     | P51–P60     |
| O          | Observation        | Journalisation        | Noter chaque trade (y compris ceux qu'on n'a pas pris) : raison, respect du plan, émotion, résultat en R.                                       | Journal de trading (Excel / Notion)                     | P61–P75     |
| N          | Nouvelle itération | Amélioration continue | Chaque semaine et chaque mois : relire, mesurer la discipline, corriger UNE règle à la fois.                                                    | Revue hebdo + Revue mensuelle                           | P76–P100    |

**Message clé pour l'élève : « Avec DÉCISION, tu ne suis le signal de
personne. Tu prends ta décision, avec l'IA comme copilote. »**

# 9. Plan d'implémentation complet

| **Quand** | **Priorité** | **Action**                                                                                                                                               |
|-----------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Semaine 1 | P1           | Intégrer la Méthode DÉCISION (nom, schéma, 8 étapes) dans le module 0 et la page de vente ; publier la bibliothèque de 100 prompts et les 20 checklists. |
| Semaine 1 | P1           | Distribuer le classeur Excel TIA (6 templates) ; remplacer l'ancien fichier Quentia.                                                                     |
| Semaine 2 | P1           | Importer l'espace Notion TIA (bases Journal, Checklists, Prompts) et enregistrer la vidéo « Installer ton cockpit ».                                     |
| Semaine 2 | P2           | Ajouter à chaque leçon les 7 blocs (théorie, démo, cas, exercice, template, prompt, validation).                                                         |
| Semaine 3 | P2           | Ajouter la FAQ intégrée par module (réponses aux questions prévisibles).                                                                                 |
| Semaine 3 | P2           | Créer les fiches de révision et les quiz notés par module.                                                                                               |
| Semaine 4 | P2           | Enregistrer les démonstrations écran (workflows quotidien, hebdo, mensuel).                                                                              |
| Mois 2    | P3           | Produire les études de cas au format fixe (dont 50 % de cas perdants) et la bibliothèque d'erreurs.                                                      |
| Mois 2    | P3           | Créer les plans d'action de 14 jours et la grille d'évaluation du projet final.                                                                          |
| Mois 2    | P3           | Mettre à jour la page de vente : 10 modules, boîte à outils, Méthode DÉCISION ; collecter les premiers retours d'élèves (vrais avis seulement).          |

# 10. Ordre de priorité des améliorations

- P1 — Ce qui augmente le plus la valeur perçue, tout de suite : 100
  prompts, 20 checklists, classeur Excel, Méthode DÉCISION.

- P1 — Espace Notion + vidéo « Installer ton cockpit » (l'élève repart
  avec un système le jour 1).

- P2 — Format de leçon en 7 blocs, FAQ par module, fiches de révision et
  quiz (complétion + moins de support).

- P2 — Démonstrations écran des workflows.

- P3 — Études de cas au format fixe, bibliothèque d'erreurs, plans
  d'action, projet final évalué.

- P3 — Mise à jour de la page de vente et collecte de vrais avis
  d'élèves (jamais de faux témoignages).

# Annexe A — Les 20 checklists

**☐ Avant d'ouvrir un trade**

- [ ] Le marché et l'horaire font partie de mon plan

- [ ] Aucune annonce économique majeure dans les 30 prochaines minutes
  (ou c'est prévu dans mon plan)

- [ ] Ma lecture multi-timeframe est écrite

- [ ] Le scénario « si… alors… » est écrit

- [ ] Le niveau d'invalidation (stop) est défini

- [ ] Le risque est ≤ à mon % maximum par trade

- [ ] La taille de position est calculée dans le Plan de risque

- [ ] L'objectif de sortie est défini (et le ratio gain/risque est
  conforme)

- [ ] Je n'ai pas atteint ma limite de perte du jour

- [ ] Mon état émotionnel est ≤ 3/5 de tension

- [ ] J'accepte de perdre ce montant sans le regretter

- [ ] Je note le trade dans le journal AVANT d'entrer

**☐ Gestion du risque**

- [ ] Mon % de risque par trade est fixé (ex. 1 %, exemple)

- [ ] Ma limite de perte par jour est fixée

- [ ] Ma limite de perte par semaine est fixée

- [ ] Je connais mon nombre maximum de trades par jour

- [ ] Le levier utilisé est connu et compris

- [ ] Je ne déplace jamais mon stop pour élargir ma perte

- [ ] Je ne double jamais une position perdante

- [ ] Je sais combien représente 1 R en euros aujourd'hui

- [ ] Je vérifie la taille de position avec la formule

**☐ Analyse avec l'IA**

- [ ] J'ai donné à l'IA le contexte complet (marché, unité de temps,
  niveaux, horaires)

- [ ] J'ai demandé une structure, pas une recommandation d'achat ou de
  vente

- [ ] J'ai demandé à l'IA de lister ses incertitudes

- [ ] J'ai demandé le scénario contraire

- [ ] J'ai vérifié chaque chiffre cité sur mon graphique

- [ ] J'ai écarté tout ce qui n'est pas vérifiable

- [ ] La décision finale est la mienne et elle est écrite

**☐ Vérification d'une réponse IA**

- [ ] Les prix et niveaux cités existent sur mon graphique

- [ ] Les dates et événements cités sont vérifiés sur une source
  officielle

- [ ] La réponse ne contient aucune promesse ni certitude

- [ ] La réponse ne contredit pas mon plan de trading

- [ ] Je peux expliquer la réponse avec mes propres mots

- [ ] Si l'IA a inventé quelque chose, je l'ai noté dans le journal

**☐ Préparation de séance**

- [ ] Calendrier économique consulté

- [ ] Niveaux clés de la veille reportés

- [ ] Lecture sur 3 unités de temps faite

- [ ] Journal de la veille relu (erreur à éviter aujourd'hui)

- [ ] Limites du jour rappelées

- [ ] Plateforme et compte démo/réel vérifiés

**☐ Multi-timeframe**

- [ ] Unité de temps longue : tendance de fond décrite

- [ ] Unité intermédiaire : structure et zones repérées

- [ ] Unité courte : contexte d'entrée décrit

- [ ] Les 3 lectures sont cohérentes ou l'incohérence est notée

- [ ] Je n'ai pas changé d'unité de temps pour « trouver » une entrée

**☐ Annonces économiques**

- [ ] Annonces du jour listées avec leur heure

- [ ] Impact attendu noté (faible/moyen/fort)

- [ ] Règle de mon plan face aux annonces rappelée

- [ ] Positions ouvertes vérifiées avant l'annonce

**☐ État émotionnel**

- [ ] Tension notée de 1 à 5

- [ ] Je ne trade pas pour me « refaire »

- [ ] Je ne trade pas par ennui

- [ ] Je suis reposé et disponible

- [ ] Je peux arrêter la séance maintenant sans frustration

**☐ Sortie de trade**

- [ ] La sortie suit le plan (stop, objectif ou règle écrite)

- [ ] Je n'ai pas coupé par peur sans raison écrite

- [ ] Je n'ai pas laissé courir une perte au-delà du stop

- [ ] Résultat noté en R dans le journal

- [ ] Respect du plan noté (oui/non)

**☐ Après une perte**

- [ ] Je fais une pause de 15 minutes minimum

- [ ] Je note si le plan a été respecté

- [ ] Je ne reprends pas de trade pour compenser

- [ ] Je vérifie ma limite de perte du jour

- [ ] J'utilise le prompt de débrief (P71)

- [ ] Une perte qui respecte le plan est une bonne exécution

**☐ Après un gain**

- [ ] Je note si le plan a été respecté

- [ ] Je n'augmente pas mon risque sur le trade suivant

- [ ] Je vérifie que le gain ne vient pas d'une erreur chanceuse

- [ ] Je garde le même processus

**☐ Fin de journée**

- [ ] Tous les trades sont dans le journal

- [ ] Les trades non pris mais étudiés sont notés

- [ ] Respect du plan calculé pour la journée

- [ ] Erreur principale du jour identifiée

- [ ] Une action pour demain écrite

- [ ] Plateforme fermée, pas de surveillance le soir

**☐ Hebdomadaire**

- [ ] Toutes les séances de la semaine sont journalisées

- [ ] Taux de respect du plan calculé

- [ ] R total et R moyen calculés

- [ ] Erreur la plus fréquente identifiée

- [ ] UNE règle à ajuster choisie (pas plus)

- [ ] Préparation de la semaine suivante faite (annonces, niveaux)

- [ ] Prompt de revue hebdo utilisé (P76)

**☐ Mensuelle**

- [ ] Revue mensuelle remplie dans l'Excel

- [ ] Évolution du respect du plan sur 4 semaines

- [ ] Évolution du drawdown max

- [ ] Biais principal du mois identifié

- [ ] Plan de trading mis à jour (version + date)

- [ ] Objectif d'apprentissage du mois suivant fixé

- [ ] Décision écrite : rester en démo / passer au réel (checklist
  dédiée)

**☐ Choisir un intermédiaire**

- [ ] Nom absent des listes noires de l'AMF

- [ ] Autorisation vérifiée (REGAFI ou régulateur européen)

- [ ] Compte démo disponible

- [ ] Conditions de levier et de frais lues

- [ ] Aucun démarchage téléphonique ni promesse de rendement

**☐ Installation des outils**

- [ ] Classeur Excel TIA téléchargé et ouvert

- [ ] Espace Notion TIA importé

- [ ] Compte ChatGPT (ou autre IA) créé

- [ ] Compte démo ouvert

- [ ] Graphiques configurés sur 3 unités de temps

- [ ] Calendrier économique en favori

**☐ Plan de trading complet**

- [ ] Marchés et horaires définis

- [ ] Unités de temps définies

- [ ] Conditions d'entrée écrites

- [ ] Invalidation écrite

- [ ] Règles de sortie écrites

- [ ] Risque par trade et limites écrits

- [ ] Règles face aux annonces écrites

- [ ] Version et date du plan notées

**☐ Journal bien rempli**

- [ ] Date, heure, marché, sens

- [ ] Raison d'entrée liée au plan

- [ ] Stop, objectif, taille, risque en €

- [ ] Résultat en R

- [ ] Plan respecté : oui/non

- [ ] Émotion avant/après (1 à 5)

- [ ] Leçon en une phrase

- [ ] Capture d'écran jointe

**☐ Avant de passer en réel**

- [ ] Au moins 30 jours de démo journalisés

- [ ] Respect du plan ≥ 80 % sur les 4 dernières semaines

- [ ] Aucune limite de perte dépassée depuis 2 semaines

- [ ] Je n'investis que de l'argent dont je n'ai pas besoin

- [ ] J'accepte de pouvoir perdre la totalité de ce montant

- [ ] Intermédiaire vérifié (checklist dédiée)

- [ ] Taille de risque réduite pour le premier mois réel

**☐ Revue d'étude de cas**

- [ ] Contexte décrit

- [ ] Plan initial retrouvé

- [ ] Exécution comparée au plan

- [ ] Résultat exprimé en R

- [ ] Ce qui a été bien fait

- [ ] Ce qui doit changer

- [ ] Leçon ajoutée au plan ou au journal

# Annexe B — Workflows

## Quotidien (séance)

1\. Allumer le PC, fermer les réseaux sociais (2 min)

2\. D · Ouvrir le calendrier économique et noter les annonces (3 min)

3\. D · Relire la leçon d'hier dans le journal (2 min)

4\. É · Lecture multi-UT : UT longue → intermédiaire → courte (10 min)

5\. C · Faire structurer et critiquer la lecture par l'IA (P31, P37) (5
min)

6\. I · Vérifier chaque élément cité par l'IA (checklist vérification
IA) (3 min)

7\. S · Rappeler les limites du jour, calculer la taille si une idée se
présente (2 min)

8\. I · Écrire le scénario si/alors avant toute entrée (3 min)

9\. Exécution en compte démo, uniquement si la checklist « Avant
d'ouvrir un trade » est entièrement cochée

10\. O · Noter chaque trade et chaque trade non pris dans le journal

11\. Checklist fin de journée, puis fermeture de la plateforme

## Hebdomadaire (dimanche, 45 min)

1\. Exporter les trades de la semaine (journal)

2\. Calculer : trades, respect du plan, R total, R moyen

3\. Identifier l'erreur la plus fréquente (tags)

4\. Prompt P76 : revue hebdomadaire

5\. Choisir UNE règle à ajuster (plan, checklist ou routine)

6\. Préparer la semaine : annonces, niveaux clés (P78, tableau de
préparation hebdo)

7\. Fixer l'objectif d'apprentissage de la semaine

## Mensuel (fin de mois, 1 h 30)

1\. Remplir la revue mensuelle dans l'Excel

2\. Comparer avec le mois précédent (P81)

3\. Identifier le biais principal du mois (P86)

4\. Mettre à jour le plan de trading (nouvelle version datée)

5\. Mettre à jour les checklists (P85)

6\. Décider : rester en démo ou critères remplis pour le réel (checklist
dédiée, P80)

7\. Fixer l'objectif d'apprentissage du mois suivant

# Annexe C — FAQ intégrée par module (réduction du support)

| **Module** | **Questions probables**                                                         | **Incompréhensions**                      | **Erreurs fréquentes**                           | **Réponse intégrée**                                                                                                                                                                     |
|------------|---------------------------------------------------------------------------------|-------------------------------------------|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| M0         | Quel compte démo ouvrir ? · Faut-il payer ChatGPT ?                             | Penser que la formation donne des signaux | Ouvrir un compte réel trop tôt                   | Tout courtier autorisé (vérifié via la checklist) proposant une démo convient. La version gratuite de ChatGPT suffit. La formation ne donne jamais de signal : elle apprend une méthode. |
| M1         | C'est quoi le spread ? · Pourquoi le levier est-il dangereux ?                  | Confondre levier et capital               | Utiliser le levier maximum par défaut            | Glossaire + schéma du levier ; règle : le levier se règle au minimum en démo, et le risque se calcule toujours en % du capital.                                                          |
| M2         | Comment savoir si c'est une tendance ? · Quelle unité de temps choisir ?        | Voir des tendances partout                | Changer d'unité de temps pour trouver une entrée | Définition sommets/creux + checklist multi-UT ; règle : 3 UT fixées dans le plan, on n'en change pas pendant la séance.                                                                  |
| M3         | Mon calcul de taille ne tombe pas juste · Pourquoi 1 % ?                        | Penser que 1 % est une obligation         | Oublier les frais et la taille minimale de lot   | Le Plan de risque Excel fait le calcul ; le 1 % est un exemple pédagogique, chacun fixe son % dans son plan. Vérifier la taille minimale chez le courtier.                               |
| M4         | L'IA m'a donné un mauvais prix · Peut-on demander à l'IA quoi acheter ?         | Faire confiance aveuglément à l'IA        | Copier la réponse de l'IA sans vérifier          | Les IA inventent parfois des chiffres : checklist de vérification obligatoire. On ne demande jamais quoi acheter, on demande de structurer et de critiquer.                              |
| M5         | Mon plan est trop long · Combien de règles mettre ?                             | Croire qu'un plan doit être parfait       | Écrire des règles non mesurables                 | Un plan tient sur une page ; chaque règle doit être vérifiable par oui/non (prompt P53 pour reformuler).                                                                                 |
| M6         | Je n'arrive pas à respecter mon stop · Comment arrêter le trading de revanche ? | Penser que la discipline est innée        | Reprendre un trade juste après une perte         | Checklists après perte / après gain + règles d'arrêt chiffrées ; la discipline se mesure et progresse avec le journal.                                                                   |
| M7         | Mon journal me prend trop de temps · Que faut-il noter ?                        | Noter seulement les trades gagnants       | Remplir le journal le lendemain de mémoire       | Colonnes minimales imposées (checklist « journal bien rempli ») ; remplir avant d'entrer et à la sortie : 2 minutes par trade.                                                           |
| M8         | Je n'ai pas le temps de faire toute la routine                                  | Croire qu'il faut trader tous les jours   | Sauter la préparation                            | Version courte de 15 minutes de la routine ; ne pas trader un jour sans préparation est une décision conforme.                                                                           |
| M9         | Pourquoi montrer des trades perdants ?                                          | Attendre des cas « parfaits »             | Juger un cas sur son résultat seulement          | Un cas se juge sur le respect du plan, pas sur le résultat ; les cas perdants enseignent le plus.                                                                                        |
