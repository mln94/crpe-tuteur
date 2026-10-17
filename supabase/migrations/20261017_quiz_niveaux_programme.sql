-- Quiz CRPE : niveau de difficulté, types de questions (QCM, réponse numérique, mot à cliquer),
-- notion (plusieurs formulations d'une même compétence) et rattachement au programme officiel.
alter table public.quiz_questions
  add column if not exists niveau text check (niveau in ('facile', 'intermediaire', 'difficile')),
  add column if not exists type text not null default 'qcm' check (type in ('qcm', 'numerique', 'cliquer_mot')),
  add column if not exists notion text,
  add column if not exists programme_ref text,
  add column if not exists classe text,
  add column if not exists theme text,
  add column if not exists sous_theme text,
  add column if not exists objectif text,
  add column if not exists tolerance numeric not null default 0;

comment on column public.quiz_questions.notion is 'Compétence évaluée : chaque notion est posée sous plusieurs formulations ; 3 bonnes réponses = notion maîtrisée.';
comment on column public.quiz_questions.programme_ref is 'Référence de la ligne du programme du cycle 4 (M = programme_mathématique_cycle4_grouped, F = programme_francais_cycle4_objectifs_grouped).';
comment on column public.quiz_questions.reponse is 'QCM : texte du bon choix ; numérique : nombre ; cliquer_mot : indices des mots attendus dans choix, séparés par des virgules.';

-- Les contrôles sur les choix ne concernent plus que les QCM
alter table public.quiz_questions drop constraint quiz_questions_reponse_dans_choix;
alter table public.quiz_questions add constraint quiz_questions_reponse_dans_choix check (type <> 'qcm' or choix ? reponse);
alter table public.quiz_questions drop constraint quiz_questions_choix_check;
alter table public.quiz_questions add constraint quiz_questions_choix_check check (jsonb_typeof(choix) = 'array' and (type <> 'qcm' or jsonb_array_length(choix) between 2 and 6));

create index if not exists quiz_questions_matiere_notion_idx on public.quiz_questions (matiere, notion) where actif;
