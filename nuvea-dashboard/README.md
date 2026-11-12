# Nuvéa Monde

Dashboard 3D (Three.js) de l'activité Nuvéa : une ville isométrique où chaque élément est cliquable et ouvre ses statistiques. Les chiffres viennent de Stripe, en lecture seule, et la page se met à jour toutes les minutes.

## Lancer en local

1. Crée une clé restreinte Stripe en **lecture** : Charges, PaymentIntents, Checkout Sessions, Produits, Solde, Compte.
2. Copie `.env.example` en `.env` et colles-y la clé (`STRIPE_API_KEY=rk_live_...`). Le `.env` est ignoré par git.
3. Lance le serveur (Node 18 ou plus, aucune dépendance) :

```bash
npm start
```

4. Ouvre http://localhost:3000

## Dans une session Claude Code cloud

La clé est enregistrée dans les secrets réseau de l'environnement, et le proxy l'ajoute aux requêtes vers `api.stripe.com`. Le `.env` garde la valeur factice `STRIPE_API_KEY=proxy-injected`. Lance :

```bash
npm run start:cloud
```

## Ce qui est lu

- `GET /api/stats` : paiements des 30 derniers jours (CA, clients, panier moyen, CA par jour, clients par moment de la journée), paiements en cours, sessions Checkout et produits les plus vendus, produits actifs (stock via `metadata.stock`), solde et état du compte.
- Le serveur garde le résultat en cache pendant la période de rafraîchissement (`REFRESH_SECONDS`, 60 par défaut).
- TikTok, mail, studio et tunnel systeme.io ne viennent pas de Stripe : leurs cartes affichent un relevé fixe du 12 nov. 2026.
