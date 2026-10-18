-- Historique des séries du Quiz CRPE (« Mes séries ») : une ligne par série terminée
create table if not exists public.quiz_series (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  matiere text not null,
  niveau text not null check (niveau in ('facile', 'intermediaire', 'difficile')),
  score integer not null check (score >= 0),
  total integer not null check (total > 0 and score <= total),
  essai boolean not null default false,
  -- [{ id, question, theme, ok, attendu }] : détail des questions de la série
  details jsonb not null default '[]'::jsonb,
  created_at timestamptz not null default now()
);
create index if not exists quiz_series_user_date on public.quiz_series (user_id, created_at desc);
alter table public.quiz_series enable row level security;
create policy "Users view own series" on public.quiz_series for select using (auth.uid() = user_id);
create policy "Users insert own series" on public.quiz_series for insert with check (auth.uid() = user_id);
