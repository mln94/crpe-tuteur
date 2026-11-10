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
| `feature_passcrpe`, `feature_quizcrpe`, `design` | oui | oui | oui (brouillon, liste Newsletter `U97rGQ` : les abonnés ; la liste Signup contient des comptes non consentants, ignorés par Klaviyo) |

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
3. Captures d'écran de la nouveauté sur PassCRPE ou Le Quiz CRPE (vraies captures de l'app, connecté au compte admin) :
   écrire `captures.mjs` dans le dossier (modèle : `Ressources/nouveautes/2026-11-05-quiz-sujets/captures.mjs`), qui utilise
   `scripts/nouveaute_captures.mjs` (`ouvrir()` = téléphone 430 × 932 en 2x, `capturer()` remplace le nom du compte par « Mon compte »),
   puis `node Ressources/nouveautes/<dossier>/captures.mjs` → `captures/1-….png`, `2-….png`, `3-….png`.
   Répondre à une question compte dans les questions gratuites du jour du compte admin : limiter les réponses.
   Montages : `python3 scripts/nouveaute_montage.py eventail <sortie> c1 c2 c3` (3 écrans en éventail)
   et `python3 scripts/nouveaute_montage.py cadre <sortie> capture [--hauteur 1250]` (un écran encadré).
   Couleurs : Quiz CRPE `--fond '#fff7ed' --bord '#fed7aa'` (défaut), PassCRPE `--fond '#f5f6ff' --bord '#c7d2fe'`.
4. Instagram : DEUX propositions d'image (même légende), rendues en HTML puis headless Chrome à 1080 × 1350 :
   - `instagram.png` classique, visuel texte (modèle : `<dossier quiz sujets>/instagram.html`) ;
   - `instagram-capture.png` faite d'une capture de l'app encadrée + bulles d'avantages (modèle : `<dossier quiz sujets>/instagram-capture.html`).
   Garder les HTML sources dans le dossier pour pouvoir les modifier.
   **Jamais « Lien en bio »** : le lien complet (ex. passcrpe.fr/rapports-jury-crpe/disciplines) est écrit sur l'image, sur une seule ligne,
   aligné dans un encart, et en entier dans la légende (https://…). Vérifier le rendu : rien ne doit déborder ni passer sous le cercle.
   Email (applications seulement) : `email.html` (modèle : `<dossier quiz sujets>/email.html`), images = **captures de l'app uniquement**
   (éventail + écran encadré), référencées en `src="fichier.png"` (le script les héberge). Liens avec UTM `utm_source=klaviyo&utm_medium=email`.
   Copie aussi dans `emails/<passcrpe|quizcrpe>/campagnes/<sujet>/`.
   Balises Klaviyo : `{{ first_name|default:'' }}` et **`{% unsubscribe_link %}`** pour le désabonnement (jamais `{% unsubscribe_url %}`,
   qui n'existe pas : la campagne passe « Sent » sans aucun destinataire). Le script teste le rendu du modèle et s'arrête en cas d'erreur.
5. `node scripts/nouveaute.mjs Ressources/nouveautes/AAAA-MM-JJ-sujet` → l'id est réécrit dans `nouveaute.json`.
   La campagne Klaviyo est créée **en brouillon** : l'utilisateur la vérifie et l'envoie lui-même.
6. Donner à l'utilisateur le lien `https://www.passcrpe.fr/suivi-nouveautes?nouveaute=<id>` et le lien Klaviyo.

## Demandes de changement (bouton « Demander un changement » du dashboard)
1. `node scripts/nouveaute.mjs --demandes` → liste des demandes en attente (id, élément, nouveauté, texte).
2. Pour chaque demande : modifier le fichier concerné dans le dossier de la nouveauté
   (`insta_legende` / `groupes.message` / `email.*` dans le JSON, `instagram.html` ou `instagram-capture.html` puis re-rendu PNG, `email.html`, ou nouvelles captures).
3. Relancer `node scripts/nouveaute.mjs <dossier>` (met à jour la ligne, les images, le message des groupes et le brouillon Klaviyo ;
   ne touche pas à une campagne Klaviyo déjà envoyée : note seulement sa date d'envoi).
4. `node scripts/nouveaute.mjs --faite <id_demande> "ce qui a été changé"`.
