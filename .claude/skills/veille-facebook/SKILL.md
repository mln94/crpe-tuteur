---
name: veille-facebook
description: Veille quotidienne des groupes Facebook CRPE. Récupère les posts d'un jour (par défaut la veille) qui demandent de l'aide, des outils, des conseils ou un avis (livre, prépa, programme, méthode) et auxquels PassCRPE peut répondre, puis les ajoute au Google Sheet « PassCRPE - Veille groupes Facebook » avec une proposition de réponse. Lancée chaque jour à 9h30 par launchd, ou pour un jour passé depuis le dashboard /suivi-agents.
---

# Veille groupes Facebook → dashboard /suivi-agents + Google Sheet

Arguments : `jour=AAAA-MM-JJ` (jour des posts à analyser ; absent = hier, heure de Paris) et `run=<uuid>` (passage créé par
`scripts/agents-poller.sh`, absent = lancement à la main). Le « jour J » ci-dessous est ce jour-là.
Dashboard : https://www.passcrpe.fr/suivi-agents (tables Supabase `agents_runs`, `agents_veille_messages`).

Sheet : « PassCRPE - Veille groupes Facebook », Drive mohamed.necibfreelance@gmail.com
- ID : `10NdYKLI6Z-NmahCtfra7PWcIXPxy4s6FqooE9gPM5t0`, onglet `Messages`
- https://docs.google.com/spreadsheets/d/10NdYKLI6Z-NmahCtfra7PWcIXPxy4s6FqooE9gPM5t0/edit
- Colonnes : A Date de collecte | B Date du post | C Groupe Facebook | D Lien du groupe | E Pseudo du postant | F Message | G Type de demande | H Lien du post | I Proposition de réponse PassCRPE | J Statut

## 1. Liste des groupes
La lire à chaque fois dans `landing/suivi-publications.html`, tableau `const GROUPS=[ [nom, id, slug], … ]`.
URL d'un groupe : `https://www.facebook.com/groups/<id>/`.

## 2. Collecte (Claude in Chrome, session Facebook de l'utilisateur)
- Jour J = l'argument `jour`, sinon la veille de la date du jour, heure de Paris (00:00 → 23:59).
- Pour chaque groupe : nouvel onglet sur `https://www.facebook.com/groups/<id>/?sorting_setting=CHRONOLOGICAL`
  (tri « Nouvelles publications »), lire le texte de la page (get_page_text / read_page), faire défiler
  jusqu'à atteindre des posts plus anciens que J (au plus ~8 défilements par groupe si J = hier, ~25 si J est plus ancien).
- Ouvrir « Voir plus » si un post est tronqué. Pour chaque post du jour J : pseudo, texte complet, date/heure, lien du post
  (permalien `/groups/<id>/posts/<postId>/` ou `/permalink/`). Si l'heure est relative (« 14 h », « Hier à 18:02 »), la convertir.
- Groupe inaccessible (plus membre, en attente, erreur) : le noter dans le récap et passer au suivant. Ne pas réessayer en boucle.
- Ne rien publier, liker, commenter ni rejoindre sur Facebook. Lecture seule.
- Fermer les onglets ouverts à la fin.

## 3. Sélection
Garder un post s'il sollicite de l'aide à laquelle PassCRPE peut répondre :
- demande d'outils, de ressources, de méthode pour préparer le CRPE (écrits, oraux, maths, français, didactique…) ;
- demande d'avis sur un livre, une prépa, une plateforme, un programme de révision, une formation ;
- détresse / perte de repères (« je ne sais pas par où commencer », « je bloque en maths ») ;
- recherche d'entraînement : sujets, annales, corrections, QCM, quiz, copies corrigées.
Ignorer : annonces de résultats sans demande, administratif pur (inscriptions, dates, mutations), ventes, publicités, posts de PassCRPE lui-même.
Champ « Type de demande » : un parmi `Outils / ressources`, `Avis livre / prépa`, `Méthode / organisation`, `Entraînement / sujets`, `Maths`, `Français`, `Oral`, `Motivation / perdu`.

## 4. Proposition de réponse
Commentaire prêt à copier, en français, ton de candidat·e/formateur bienveillant, pas commercial :
- d'abord répondre vraiment à la question (1-2 conseils concrets) ;
- puis proposer PassCRPE comme piste, simplement : Le Quiz CRPE by PassCRPE (quiz d'entraînement maths et français),
  le tuteur IA PassCRPE (correction et explications), les articles du blog, le challenge gratuit « La Copie Parfaite avant Noël »
  (10-22 décembre 2026, inscriptions jusqu'au 8 décembre) tant qu'il est ouvert. Choisir ce qui colle à la demande, pas tout.
- Lien avec UTM : `https://www.passcrpe.fr/<page>?utm_source=facebook&utm_medium=groupe_reponse&utm_campaign=passcrpe_veille&utm_content=<slug du groupe>`
  (`/quizcrpe` pour le quiz, `/blog` ou l'article pertinent, `/copie-parfaite-noel` pour le challenge).
- 3 à 6 lignes. Pas de majuscules criardes, 0-1 emoji. Ne jamais mettre d'email personnel.
- Si le groupe interdit la pub (règle vue sur la page), écrire la réponse sans lien et ajouter « (groupe sans pub : proposer le lien en MP) ».

## 5a. Envoi au dashboard (obligatoire, même sans message retenu)
Écrire `logs/veille-facebook/<J>.json` :
```json
{ "jour": "AAAA-MM-JJ", "groupes_lus": 38, "groupes_echec": [{ "groupe": "…", "raison": "…" }],
  "resume": "2-4 phrases : ce qui a été vu, ce qui a été écarté et pourquoi",
  "messages": [{ "post_le": "AAAA-MM-JJ HH:MM", "groupe": "…", "groupe_slug": "…", "lien_groupe": "https://www.facebook.com/groups/…/",
                 "pseudo": "…", "message": "texte complet", "type_demande": "…", "lien_post": "https://…", "reponse": "…" }] }
```
puis lancer `node scripts/agents_suivi.mjs --enregistrer-veille logs/veille-facebook/<J>.json <run>` (sans `<run>` si absent).
Le script ignore les posts déjà enregistrés (même lien) et marque le passage « ok ».

## 5b. Écriture dans le Sheet
- Lire d'abord la colonne H (`Messages!H:H`) et ne pas ajouter un post dont le lien y est déjà.
- Ajouter les lignes avec `append_values` sur `Messages!A:J`. Dates au format `AAAA-MM-JJ` (B : `AAAA-MM-JJ HH:MM`). J = `À répondre`.
- Aucun post retenu : ajouter quand même une ligne `<date> | <J> | (aucun message pertinent)` pour tracer le passage.

## 6. Récap
Finir par un résumé court : groupes lus, groupes en échec, nombre de posts retenus, lien du Sheet.
Écrire ce récap dans `logs/veille-facebook/<J>.md`.
