-- Entraîneur CRPE (outil gratuit) : contacts, questions servies et tentatives corrigées par l'IA.
-- Aucune table existante n'est modifiée. RLS activée sans aucune règle : seul le serveur (service role) lit et écrit,
-- le navigateur passe toujours par l'API /api/entraineur/*.

-- 1. Contacts inscrits via le formulaire de l'outil (pas de compte Supabase Auth)
create table if not exists public.entraineur_leads (
  id                    uuid primary key default gen_random_uuid(),
  prenom                text not null check (length(prenom) between 1 and 80),
  nom                   text not null check (length(nom) between 1 and 80),
  email                 text not null unique check (email = lower(email) and length(email) <= 254),
  telephone             text check (length(telephone) <= 30),
  consent_conseils      boolean not null default false,
  consent_partenaires   boolean not null default false,
  consent_version       text not null,
  klaviyo_synced_at     timestamptz,
  created_at            timestamptz not null default now(),
  updated_at            timestamptz not null default now()
);

-- 2. Questions servies (quota hebdomadaire, questions déjà vues, révélation du corrigé)
create table if not exists public.entraineur_questions_servies (
  id            uuid primary key default gen_random_uuid(),
  lead_id       uuid references public.entraineur_leads(id) on delete cascade,
  anon_id_hash  text,
  matiere       text not null check (matiere in ('maths', 'francais')),
  question_id   bigint not null,
  categorie     text not null,
  served_at     timestamptz not null default now(),
  revealed_at   timestamptz,
  check (lead_id is not null or anon_id_hash is not null)
);
create index if not exists entraineur_servies_lead_idx on public.entraineur_questions_servies (lead_id, served_at);
create index if not exists entraineur_servies_anon_idx on public.entraineur_questions_servies (anon_id_hash, served_at);

-- 3. Tentatives (3 maximum par question servie) et rapports de correction
create table if not exists public.entraineur_tentatives (
  id             uuid primary key default gen_random_uuid(),
  servie_id      uuid not null references public.entraineur_questions_servies(id) on delete cascade,
  tentative      smallint not null check (tentative between 1 and 3),
  reponse        text not null check (length(reponse) between 1 and 3000),
  rapport        jsonb not null,
  note           numeric(4,1) check (note between 0 and 20),
  model          text,
  input_tokens   integer,
  output_tokens  integer,
  created_at     timestamptz not null default now(),
  unique (servie_id, tentative)
);
create index if not exists entraineur_tentatives_created_idx on public.entraineur_tentatives (created_at);

alter table public.entraineur_leads              enable row level security;
alter table public.entraineur_questions_servies  enable row level security;
alter table public.entraineur_tentatives         enable row level security;

revoke all on public.entraineur_leads, public.entraineur_questions_servies, public.entraineur_tentatives from anon, authenticated;
