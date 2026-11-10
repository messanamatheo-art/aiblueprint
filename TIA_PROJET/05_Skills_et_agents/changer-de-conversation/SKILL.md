---
name: changer-de-conversation
description: Surveille la taille de la conversation et propose de passer à une nouvelle conversation avant qu'elle consomme trop de jetons. À utiliser quand la conversation devient longue (beaucoup d'échanges, gros fichiers lus, nombreux rendus ou résultats d'outils volumineux), quand l'utilisateur parle de jetons, de lenteur, de limite ou de « changer de conv », ou à la fin d'une grosse étape de travail.
---

# Changer de conversation au bon moment

## 1. Repérer le moment
Propose de changer de conversation dès qu'un de ces signaux apparaît :
- plus d'environ 40 échanges, ou des dizaines de résultats d'outils volumineux (images, logs, gros fichiers) ;
- la conversation a été résumée automatiquement (« compactée ») au moins une fois ;
- une grosse étape vient de se terminer (livrable envoyé, validation obtenue) : c'est le meilleur moment ;
- l'utilisateur évoque les jetons, la lenteur, une limite, ou demande à changer.
Ne coupe jamais au milieu d'une tâche : termine l'étape en cours ou mets-la proprement en pause.

## 2. Préparer le passage (avant de proposer)
1. Mets à jour le fichier de contexte du projet (pour Trading IA Academy : `00_LIRE_EN_PREMIER.md` du dossier `TIA_PROJET`, identique à `CLAUDE.md`) :
   - section « Ce qui reste à faire » à jour ;
   - toute nouvelle décision ou consigne de l'utilisateur ;
   - ce qui attend une validation de sa part.
2. Ajoute une ligne datée au journal des décisions et à la mémoire.
3. Arrête les tâches de fond (rendus, scripts) ou note où elles en sont.
4. Envoie à l'utilisateur le fichier de contexte mis à jour (et seulement les fichiers nouveaux ou modifiés, en petits envois).

## 3. Message de passage (court)
Écris en français, sans jargon :
- **Pourquoi changer** : en une phrase, la conversation est longue et chaque nouveau message coûte plus de jetons.
- **Ce qui est sauvegardé** : le nom du fichier de contexte.
- **Le message à coller** dans la nouvelle conversation, dans un bloc à copier :
  > Lis 00_LIRE_EN_PREMIER.md, puis reprends là où on s'est arrêtés : [prochaine étape précise].
- **Ce que tu dois faire maintenant** : 1) télécharger le fichier, 2) ouvrir une nouvelle conversation (dans le Projet claude.ai si il existe, avec le fichier dans ses connaissances), 3) coller le message.

## 4. Économiser en attendant
Tant que l'utilisateur n'a pas changé de conversation : réponses courtes, pas de relecture de gros fichiers, pas de longues listes, pas d'images inutiles.
