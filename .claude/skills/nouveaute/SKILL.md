---
name: nouveaute
description: Annonce d'une modification du site PassCRPE (article de blog, ressource, nouvelle fonctionnalité PassCRPE ou Quiz CRPE, nouveau design). À lancer après chaque modification du site déployée, ou quand l'utilisateur demande de traiter les demandes de changement du dashboard /suivi-nouveautes. Prépare publication Instagram, campagne groupes Facebook, et email Klaviyo (applications seulement), puis enregistre tout dans le dashboard.
---

# Nouveauté du site → publications + dashboard /suivi-nouveautes

Dashboard : https://www.passcrpe.fr/suivi-nouveautes (tables Supabase `site_nouveautes`, `site_nouveautes_demandes`).
Script : `node scripts/nouveaute.mjs <dossier>` (images → bucket `nouveautes`, campagne groupes, brouillon Klaviyo, ligne du dashboard).

## Quand
- Après chaque modification du site **visible par les utilisateurs** et déployée : article de blog, ressource, fonctionnalité, design.
  Pas pour les pages internes (dashboards, admin), les corrections invisibles, le SEO technique.
- Plusieurs petits changements le même jour sur le même sujet = une seule nouveauté.

## Ce qu'on prépare selon le type
| type | Instagram | Groupes Facebook | Email Klaviyo |
|---|---|---|---|
| `article`, `ressource` | oui | oui | **non** |
| `feature_passcrpe`, `feature_quizcrpe`, `design` | oui | oui | oui (brouillon, liste Signup `SgJQyM`) |

Pas de publication sur la page Facebook (retirée du dashboard le 10/11/2026 à la demande de l'utilisateur).

## Étapes
1. Dossier `Ressources/nouveautes/AAAA-MM-JJ-sujet/` (git-ignoré).
2. `nouveaute.json` :
   ```json
   { "modifie_le": "AAAA-MM-JJ", "type": "feature_quizcrpe", "titre": "…", "resume": "Ce qui a été fait, concret, 2-5 lignes",
     "lien": "https://www.passcrpe.fr/…",
     "insta_legende": "…",
     "groupes": { "campagne": "passcrpe_sujet_court", "message": "… {LIEN} …" },
     "email": { "nom": "PassCRPE - Campagne - Nouveauté - …", "objet": "…", "preheader": "…" } }
   ```
   - `groupes.campagne` : minuscules, chiffres, `_` (nom UTM). Le message contient `{LIEN}`.
   - `email.nom` commence TOUJOURS par « PassCRPE » (Quiz CRPE : « PassCRPE - QuizCRPE - … »).
   - Ton : authentique, sincère, utile pour les candidats, qui donne envie de cliquer. Pas trop long.
   - Nom du quiz : « Le Quiz CRPE by PassCRPE ». Ne jamais mettre l'email personnel de l'utilisateur.
3. Images (rendu HTML → headless Chrome, couleurs PassCRPE indigo `#4f46e5` ou Quiz CRPE orange `#ea580c`) :
   - `instagram.png` 1080 × 1350 (modèle : `Ressources/réseaux sociaux/instagram/2026-11-05-presentation-quizcrpe/publication.html`)
   - Garder le HTML source (`instagram.html`) dans le dossier pour pouvoir le modifier.
4. Applications seulement : `email.html` (modèle : `emails/quizcrpe/campagnes/newsletter-1-suivi-notions/`),
   images locales référencées en `src="fichier.png"` (le script les héberge). Liens avec UTM `utm_source=klaviyo&utm_medium=email`.
   Copie aussi dans `emails/<passcrpe|quizcrpe>/campagnes/<sujet>/`.
5. `node scripts/nouveaute.mjs Ressources/nouveautes/AAAA-MM-JJ-sujet` → l'id est réécrit dans `nouveaute.json`.
   La campagne Klaviyo est créée **en brouillon** : l'utilisateur la vérifie et l'envoie lui-même.
6. Donner à l'utilisateur le lien `https://www.passcrpe.fr/suivi-nouveautes?nouveaute=<id>` et le lien Klaviyo.

## Demandes de changement (bouton « Demander un changement » du dashboard)
1. `node scripts/nouveaute.mjs --demandes` → liste des demandes en attente (id, élément, nouveauté, texte).
2. Pour chaque demande : modifier le fichier concerné dans le dossier de la nouveauté
   (`insta_legende` / `groupes.message` / `email.*` dans le JSON, `instagram.html` puis re-rendu PNG, `email.html`).
3. Relancer `node scripts/nouveaute.mjs <dossier>` (met à jour la ligne, les images, le message des groupes et le brouillon Klaviyo ;
   refuse de toucher une campagne Klaviyo déjà envoyée).
4. `node scripts/nouveaute.mjs --faite <id_demande> "ce qui a été changé"`.
