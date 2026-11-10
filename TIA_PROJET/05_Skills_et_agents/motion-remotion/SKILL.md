---
name: motion-remotion
description: Anime une vidéo de motion design en code avec Remotion (React) à partir d'un storyboard, puis l'exporte en MP4. À utiliser quand l'utilisateur veut créer, animer ou exporter une vidéo animée avec Claude Code.
---

# Animation avec Remotion

## Projet
- S'il n'existe pas, crée-le avec `npx create-video@latest` (modèle vide) et vérifie que `npx remotion studio` démarre.
- Si les skills officiels Remotion sont installés, suis aussi leurs règles.
- Format selon la plateforme : 1080x1920 (9:16), 1920x1080 (16:9), 1080x1080 ou 1080x1350. 30 images par seconde par défaut.

## Organisation
- Un fichier `theme.ts` : couleurs, polices, tailles, durées de base. Toutes les scènes l'utilisent.
- Une scène = un composant dans `src/scenes/`, assemblées avec `<Series>` ou `<TransitionSeries>`.
- Les durées viennent du storyboard, converties en images (secondes x fps).

## Animer
- Tout mouvement passe par `useCurrentFrame()` avec `interpolate()` (en limitant les valeurs) ou `spring()`. Jamais d'animation CSS ni de `setTimeout` : le rendu serait faux.
- Entrées décalées (stagger) de 3 à 6 images entre les éléments.
- Toujours un mouvement en cours : léger zoom continu, dérive, parallaxe.
- Transitions variées : glissement, masque, zoom à travers un élément, flou de mouvement simulé.
- Polices chargées avec `@remotion/google-fonts` ; images et logo dans `public/` via `staticFile()`.

## Son
Si une musique ou une voix est fournie, utilise `<Audio>` et cale les moments forts sur le rythme. Ne génère jamais de musique protégée.

## Vérifier et exporter
- Ouvre le studio, vérifie chaque scène, en particulier la lisibilité des textes sur mobile.
- Rendu final : `npx remotion render` avec le codec h264, fichier dans `out/`.
- Pour une autre plateforme, duplique la composition avec un autre format au lieu de tout refaire.

## Licence
Rappelle que Remotion est gratuit pour les particuliers et les entreprises jusqu'à 3 salariés ; au-delà, une licence entreprise est nécessaire.
