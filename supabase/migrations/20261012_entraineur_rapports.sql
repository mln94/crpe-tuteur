-- Entraîneur CRPE, nouveau parcours : 5 questions, puis formulaire, puis rapport détaillé envoyé par e-mail (flow Klaviyo).
-- Chaque rapport a un lien personnel impossible à deviner (token). Ajout seul : les tables existantes ne sont pas modifiées.
create table if not exists public.entraineur_rapports (
  id               uuid primary key default gen_random_uuid(),
  token            text not null unique check (length(token) >= 32),
  lead_id          uuid not null references public.entraineur_leads(id) on delete cascade,
  matiere          text not null check (matiere in ('maths', 'francais')),
  questions        jsonb not null,
  synthese         jsonb not null,
  note             numeric(4,1) check (note between 0 and 20),
  model            text,
  input_tokens     integer,
  output_tokens    integer,
  klaviyo_event_at timestamptz,
  created_at       timestamptz not null default now()
);
create index if not exists entraineur_rapports_lead_idx on public.entraineur_rapports (lead_id, created_at);

alter table public.entraineur_rapports enable row level security;
revoke all on public.entraineur_rapports from anon, authenticated;
