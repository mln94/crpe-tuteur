-- Essai du Quiz CRPE : jours où la personne a fait ses 5 questions gratuites, remplis par le serveur quand la 5e question du jour est validée.
-- essai_5_questions_premiere_fois_at : première fois (vide = jamais) ; essai_nb_jours_5_questions : nombre de jours.
-- La dernière activité d'essai est dans essai_derniere_question_at. Rien n'est reconstitué pour les jours passés.

alter table public.quiz_comptes
  add column if not exists essai_5_questions_premiere_fois_at timestamptz,
  add column if not exists essai_nb_jours_5_questions integer not null default 0;
