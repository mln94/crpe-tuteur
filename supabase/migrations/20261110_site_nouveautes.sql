-- Suivi des nouveautés du site (/suivi-nouveautes) : chaque modification du site (article, ressource, fonctionnalité,
-- design) et les publications préparées pour l'annoncer (Instagram, page Facebook, groupes Facebook, email Klaviyo).
-- Lecture et écriture réservées au compte administrateur (même règle que /suivi-publications).
create table if not exists public.site_nouveautes (
  id uuid primary key default gen_random_uuid(),
  modifie_le date not null default current_date,           -- date de la modification sur le site
  type text not null check (type in ('article', 'ressource', 'feature_passcrpe', 'feature_quizcrpe', 'design')),
  titre text not null,
  resume text not null,                                    -- ce qui a été fait
  lien text not null,                                      -- adresse de la nouveauté
  -- Instagram (image 1080 × 1350)
  insta_image_url text,
  insta_legende text,
  insta_publie_le date,
  -- Page Facebook (image 1200 × 630, aperçu du lien)
  facebook_image_url text,
  facebook_post text,
  facebook_publie_le date,
  -- Groupes Facebook : campagne de /suivi-publications (liens UTM par groupe)
  meta_campagne_id uuid references public.meta_campagnes (id) on delete set null,
  -- Email Klaviyo (fonctionnalités et design des applications seulement)
  klaviyo_campaign_id text,
  klaviyo_url text,
  email_objet text,
  email_html text,                                         -- HTML de l'email (aperçu dans le dashboard)
  email_envoye_le date,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- Demandes de changement faites depuis le dashboard, traitées ensuite par Claude
create table if not exists public.site_nouveautes_demandes (
  id uuid primary key default gen_random_uuid(),
  nouveaute_id uuid not null references public.site_nouveautes (id) on delete cascade,
  element text not null check (element in ('insta_texte', 'insta_image', 'facebook_texte', 'facebook_image', 'groupes_message', 'email')),
  demande text not null,
  statut text not null default 'en_attente' check (statut in ('en_attente', 'faite')),
  reponse text,                                            -- ce qui a été changé
  created_at timestamptz not null default now(),
  traitee_at timestamptz
);
create index if not exists site_nouveautes_demandes_attente on public.site_nouveautes_demandes (statut, created_at);

alter table public.site_nouveautes enable row level security;
alter table public.site_nouveautes_demandes enable row level security;
drop policy if exists "Admin gère les nouveautés" on public.site_nouveautes;
create policy "Admin gère les nouveautés" on public.site_nouveautes for all
  using ((auth.jwt() ->> 'email') = 'mohamed.necib94310@gmail.com')
  with check ((auth.jwt() ->> 'email') = 'mohamed.necib94310@gmail.com');
drop policy if exists "Admin gère les demandes" on public.site_nouveautes_demandes;
create policy "Admin gère les demandes" on public.site_nouveautes_demandes for all
  using ((auth.jwt() ->> 'email') = 'mohamed.necib94310@gmail.com')
  with check ((auth.jwt() ->> 'email') = 'mohamed.necib94310@gmail.com');

-- Images et aperçus d'email : bucket public (lecture par lien), écriture par le serveur (clé service) uniquement
insert into storage.buckets (id, name, public) values ('nouveautes', 'nouveautes', true)
on conflict (id) do update set public = true;

-- Instagram : deux propositions par nouveauté, la publication classique (insta_image_url) et une publication
-- construite à partir d'une capture d'écran de l'application (insta_capture_url)
alter table public.site_nouveautes add column if not exists insta_capture_url text;
alter table public.site_nouveautes_demandes drop constraint if exists site_nouveautes_demandes_element_check;
alter table public.site_nouveautes_demandes add constraint site_nouveautes_demandes_element_check
  check (element in ('insta_texte', 'insta_image', 'insta_capture', 'facebook_texte', 'facebook_image', 'groupes_message', 'email'));
