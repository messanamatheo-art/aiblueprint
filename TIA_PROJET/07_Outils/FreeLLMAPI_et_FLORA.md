# Outils
## FreeLLMAPI (Mac de mth)
- App de bureau (DMG arm64). Tableau de bord : http://localhost:31415 (onglet Keys > API key pour la clé unifiée `freellmapi-…`).
- Fournisseurs ajoutés : Google AI Studio (Gemini), Groq, OpenRouter. Les clés montrées dans le chat doivent être révoquées et recréées.
- Configurer Claude Code : `npx freellmapi setup-claude --url http://localhost:31415` (colle la clé quand elle est demandée ; elle est masquée).
- Basculer quand la limite Claude est atteinte : `npx freellmapi launch --url http://localhost:31415`.
- Node v26 donne un avertissement EBADENGINE (installer Node 22 LTS si ça plante). Désactiver « bypass permissions » (Maj + Tab).
## FLORA
- Workspace « Nuvéa's workspace ». Génération d'images, vidéos et audio payante : toujours annoncer le prix en dollars avant.
