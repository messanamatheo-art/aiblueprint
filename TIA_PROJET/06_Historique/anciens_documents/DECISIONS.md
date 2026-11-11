# DECISIONS

## D-001 — 2026-11-01 — Point de départ
Le cahier des charges est la référence unique. Aucun ancien système repris. Révision : sur demande de l'utilisateur.

## D-002 — 2026-11-01 — Emplacement de la persistance
- Fichiers de référence : dossier partagé du projet `/mnt/project-files/entreprise/` (survit à tous les fils du projet).
- Mémoire projet : mémoire partagée du projet Claude (fichiers mémoire, relue au démarrage de chaque fil).
- Données des tableaux de bord : base de données de l'Artifact « Centre de pilotage » (stockage cloud claude.ai).
Raison : ce sont les trois espaces persistants réellement disponibles dans cet environnement.

## D-003 — 2026-11-01 — Choix du 2e agent opérationnel : Organisation & Administration
Raison : (1) l'objectif central est de faire de Claude le point d'entrée unique (communications, agenda, documents, tâches) ; (2) Gmail, Google Agenda et Google Drive sont déjà connectés et testés ; la boîte compte ~1 280 fils non lus, un besoin concret de tri ; (3) aucun chevauchement avec Budget (chiffres). Il alimente Budget (factures, échéances repérées dans les mails).
Alternatives écartées pour l'instant : Marketing (pas encore d'activité commerciale décrite), Technique (pas de besoin identifié), Recherche (couvert par le coordinateur).
Révision : si l'utilisateur précise une activité professionnelle prioritaire différente.

## D-004 — 2026-11-01 — Forme technique des agents
Chaque agent existe sous deux formes réelles et réutilisables :
1. Définition de sous-agent Claude Code (`.claude/agents/<nom>.md`, mémoire projet) pour le poste de travail.
2. Compétence (Skill) du compte Claude proposée à l'enregistrement, utilisable dans toute conversation.
Le coordinateur = Claude dans ce projet, régi par les instructions du projet.
Limite assumée : un agent ne tourne pas en continu de lui-même ; il agit quand il est invoqué ou quand une routine planifiée le déclenche.

## D-005 — 2026-11-01 — Changement de direction : E-COMMERCE remplace le trading
Décision de mth (message du 2026-11-01, nouveau document « Projet_entreprise_IA_ECOMMERCE_VERSION_MAJ.docx »).
- Le nouveau document devient la référence canonique ; l'ancien est déplacé dans `00_reference/obsolete/` (trace, ne s'applique plus). D-001 est révisée en ce sens.
- Trading abandonné : agent, fichiers, tâche, données et règles retirés de l'organisation active ; fichiers déplacés dans `_archive/trading_2026-11-01/` (réversible). Ne jamais réactiver.
- Socle : coordinateur + agent E-commerce (nouveau) + agent Budget (adapté au suivi pro de la boutique).
- Organisation & Administration (D-003) est conservé : utile au fonctionnement général (mails, agenda, documents, tâches) et sans chevauchement.
Révision : uniquement sur demande de mth.

## D-006 — 2026-11-01 — Boutique en dropshipping + agent Marketing & Contenu
Choix de mth (cartes) : modèle de vente = dropshipping ; création immédiate d'un agent Marketing & Contenu (SEO inclus au début). Service client & logistique, sourcing et technique restent proposés pour plus tard.

## D-007 — 2026-11-05 — Changement de direction : formations « trader avec l'IA » remplacent l'e-commerce
Décision de mth (message du 2026-11-05 08:10, « plus de ecomm… on va vendre des formations sur comment trader avec l'IA… part de 0 »).
- D-005 (trading abandonné) et D-006 (dropshipping) sont révisées.
- Fichiers e-commerce ARCHIVÉS (choix « Archiver » sur carte, 08:16) dans `_archive/ecommerce_2026-11-05/`, rien supprimé.
- Boutique Shopify, DSers et comptes non touchés : décision séparée de mth.
- Nouveaux agents : Formation & Offre (créé), Marketing (réorienté). Budget et Organisation conservés.
- Garde-fous légaux inscrits dans la charte (pas de promesse de gains, pas de conseil personnalisé, pas de pyramide).

## D-008 — 2026-11-05 — Quentia : mth est le formateur
Carte cliquée par mth (10:03) : « Moi, j'ai une vraie expérience ». La page « Qui enseigne » sera construite sur son parcours réel (durée, marchés, méthode), sans afficher de gains. Durée déclarée : 1 à 3 ans en argent réel ; plusieurs marchés (formation généraliste) ; preuves = journal tenu + relevés de courtier gardés privés. Brouillon de la page « Qui enseigne » dans le plan fondateur.
