-- Inscriptions aux challenges PassCRPE (premier challenge : « La Copie Parfaite de Noël 2026 », page /copie-parfaite-noel).
-- Une ligne par candidat et par challenge ; écrite par le serveur (clé service) à chaque inscription,
-- en plus de la liste Klaviyo du challenge. Les colonnes « suivi » sont remplies pendant et après le challenge.
create table if not exists public.challenge_inscriptions (
  id uuid primary key default gen_random_uuid(),
  challenge text not null default 'copie-parfaite-noel-2026',   -- identifiant du challenge
  -- Formulaire d'inscription
  prenom text not null,
  nom text not null,
  email text not null check (email = lower(email)),
  telephone text,                                               -- format E.164 (+33…)
  deja_passe_crpe boolean not null,                             -- « Avez-vous déjà passé le CRPE ? »
  sujet_optionnel text not null default 'aucun'
    check (sujet_optionnel in ('aucun', 'histoire-geographie', 'emc', 'anglais', 'sciences-technologie', 'arts')),
  consent_conseils boolean not null default false,              -- newsletter PassCRPE
  consent_partenaires boolean not null default false,           -- offres des partenaires
  -- Suivi du challenge
  equipe text,                                                  -- binôme / trinôme attribué après la clôture
  note_maths numeric(5,2) check (note_maths between 0 and 100),           -- en %
  note_francais numeric(5,2) check (note_francais between 0 and 100),     -- en %
  note_optionnel numeric(5,2) check (note_optionnel between 0 and 100),   -- en %
  reussi boolean,                                               -- seuil atteint sur maths et français
  certificat_envoye_le timestamptz,
  user_id uuid references auth.users (id) on delete set null,   -- compte PassCRPE, s'il existe
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (challenge, email)
);
create index if not exists challenge_inscriptions_challenge on public.challenge_inscriptions (challenge, created_at);
create index if not exists challenge_inscriptions_equipe on public.challenge_inscriptions (challenge, equipe);

comment on table public.challenge_inscriptions is 'Inscriptions aux challenges PassCRPE (ex. copie-parfaite-noel-2026, page /copie-parfaite-noel)';

-- updated_at mis à jour automatiquement
create or replace function public.challenge_inscriptions_touch() returns trigger
language plpgsql set search_path = '' as $$
begin new.updated_at := now(); return new; end $$;
drop trigger if exists challenge_inscriptions_touch on public.challenge_inscriptions;
create trigger challenge_inscriptions_touch before update on public.challenge_inscriptions
  for each row execute function public.challenge_inscriptions_touch();

-- Données personnelles : aucun accès public ; le serveur écrit avec la clé service, l'admin lit et gère
alter table public.challenge_inscriptions enable row level security;
drop policy if exists "Admin gère les inscriptions aux challenges" on public.challenge_inscriptions;
create policy "Admin gère les inscriptions aux challenges" on public.challenge_inscriptions for all
  using ((auth.jwt() ->> 'email') = 'mohamed.necib94310@gmail.com')
  with check ((auth.jwt() ->> 'email') = 'mohamed.necib94310@gmail.com');
