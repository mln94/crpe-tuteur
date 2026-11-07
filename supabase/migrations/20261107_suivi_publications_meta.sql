-- Suivi des publications Meta (/suivi-publications) : une campagne = un jeu de liens UTM (un par groupe Facebook).
-- meta_campagnes.liens_generes_at : quand les liens de la campagne ont été générés.
-- meta_publications : pour chaque groupe, le lien, quand il a été copié pour la première fois et la date de publication.
-- Lecture et écriture réservées au compte administrateur (même règle que /admin-support).
create table if not exists public.meta_campagnes (
  id uuid primary key default gen_random_uuid(),
  nom text not null unique,
  base_url text not null,
  liens_generes_at timestamptz not null default now(),
  created_at timestamptz not null default now()
);
create table if not exists public.meta_publications (
  campagne_id uuid not null references public.meta_campagnes (id) on delete cascade,
  groupe_slug text not null,
  groupe_nom text not null,
  lien text not null,
  lien_copie_at timestamptz,
  publie_le date,
  updated_at timestamptz not null default now(),
  primary key (campagne_id, groupe_slug)
);
alter table public.meta_campagnes enable row level security;
alter table public.meta_publications enable row level security;
drop policy if exists "Admin gère les campagnes" on public.meta_campagnes;
create policy "Admin gère les campagnes" on public.meta_campagnes for all
  using ((auth.jwt() ->> 'email') = 'mohamed.necib94310@gmail.com')
  with check ((auth.jwt() ->> 'email') = 'mohamed.necib94310@gmail.com');
drop policy if exists "Admin gère les publications" on public.meta_publications;
create policy "Admin gère les publications" on public.meta_publications for all
  using ((auth.jwt() ->> 'email') = 'mohamed.necib94310@gmail.com')
  with check ((auth.jwt() ->> 'email') = 'mohamed.necib94310@gmail.com');
