-- Essai gratuit du Quiz CRPE : 5 questions par jour (heure de Paris) au lieu de 2 séries offertes.
-- essai_jour : jour (Europe/Paris) des questions comptées dans essai_jour_ids ; un autre jour, le compteur repart de 0.
-- essai_jour_ids : identifiants des questions répondues ce jour-là (une question déjà répondue le même jour ne compte pas deux fois).
-- essai_reponses (ancien essai par séries) est gardé pour l'historique et n'est plus écrit.

alter table public.quiz_comptes
  add column if not exists essai_jour date,
  add column if not exists essai_jour_ids jsonb not null default '[]'::jsonb;
