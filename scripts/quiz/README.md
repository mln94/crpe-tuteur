# Questions du Quiz CRPE (sources)

Chaque fichier décrit des **notions** du programme du cycle 4, posées sous au moins 3 formulations (`variantes`).
Une notion est maîtrisée quand l'élève répond juste à 3 formulations différentes.

- `qlib.py` : constructeurs `Q` (QCM), `N` (réponse numérique), `C` (mot à cliquer : la réponse est entre crochets dans la phrase) et `notion(ref, objectif, niveau, clé, variantes)`.
- Un fichier par matière et par niveau (`_facile`, `_inter`, `_difficile`) : `m_` mathématiques, `f_` français, `hg_` histoire-géographie, `emc_`, `svt_`, `pc_` physique-chimie, `techno_` technologie, `arts_` (arts plastiques et éducation musicale), `anglais_`. Chaque matière compte 300 questions : 150 faciles, 100 intermédiaires, 50 difficiles.
- `referentiel.py` : objectifs officiels du cycle 4 pour les matières autres que le français et les maths (codes `H5-1`, `E4-2`, `S-1`, `P-3`, `T-2`, `A-4`, `L-1`…, avec la source BO). Ils sont aussi dans la table `programme_cycle4_disciplines`.
- Pour le français et les maths, `ref` renvoie à la ligne du programme en base (`M12` = `programme_mathématique_cycle4_grouped` id 12, `F52` = `programme_francais_cycle4_objectifs_grouped` id 52) et `objectif` à l'index de l'objectif dans cette ligne.

Les questions sont stockées dans la table Supabase `quiz_questions` (colonnes `niveau`, `type`, `notion`, `programme_ref`, `classe`, `theme`, `sous_theme`, `objectif`).

## Ajouter ou remplacer une matière

```
python3 scripts/quiz/construire.py svt > lignes.json   # plusieurs matières possibles
node scripts/quiz/inserer.mjs lignes.json
```

`construire.py` vérifie les comptes et rattache chaque question à son objectif. Pour le français et les maths, il faut définir `PROGRAMME_JSON` (export des tables de programme). `inserer.mjs` lit `VITE_SUPABASE_URL` et `SUPABASE_SERVICE_ROLE_KEY` dans `.env`. Il ignore une matière qui a déjà des questions avec notion et désactive (`actif = false`) les anciennes questions sans notion.
