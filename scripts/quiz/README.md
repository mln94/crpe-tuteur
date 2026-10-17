# Questions du Quiz CRPE (sources)

Chaque fichier décrit des **notions** du programme du cycle 4, posées sous au moins 3 formulations (`variantes`).
Une notion est maîtrisée quand l'élève répond juste à 3 formulations différentes.

- `qlib.py` : constructeurs `Q` (QCM), `N` (réponse numérique), `C` (mot à cliquer : la réponse est entre crochets dans la phrase) et `notion(ref, objectif, niveau, clé, variantes)`.
- `m_*.py` / `f_*.py` : mathématiques et français, par niveau (facile, intermédiaire, difficile).
- `ref` renvoie à la ligne du programme en base (`M12` = `programme_mathématique_cycle4_grouped` id 12, `F52` = `programme_francais_cycle4_objectifs_grouped` id 52) et `objectif` à l'index de l'objectif dans cette ligne.

Les questions sont stockées dans la table Supabase `quiz_questions` (colonnes `niveau`, `type`, `notion`, `programme_ref`, `classe`, `theme`, `sous_theme`, `objectif`).
