-- Référentiel des programmes officiels du cycle 4 pour les matières du quiz autres que le français et les
-- mathématiques (histoire-géographie, EMC, SVT, physique-chimie, technologie, arts, anglais).
-- Les données viennent de scripts/quiz/referentiel.py (upsert sur matiere + code).
-- Lecture réservée au serveur : RLS activée, aucune politique.
create table if not exists public.programme_cycle4_disciplines (
  id bigint generated always as identity primary key,
  matiere text not null,
  code text not null,
  classe text,
  theme text not null,
  sous_theme text not null,
  objectifs jsonb not null check (jsonb_typeof(objectifs) = 'array'),
  source text not null,
  created_at timestamptz not null default now(),
  unique (matiere, code)
);

alter table public.programme_cycle4_disciplines enable row level security;
