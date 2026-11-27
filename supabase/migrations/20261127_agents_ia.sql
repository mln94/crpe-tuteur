-- Suivi des agents IA (/suivi-agents) : veille des groupes Facebook et rédaction automatique du blog.
-- Lecture et écriture réservées au compte administrateur (même règle que /suivi-nouveautes).
-- Les scripts du Mac (scripts/agents_suivi.mjs) écrivent avec la clé service.

-- Passages des agents. Pour la veille : un passage = un jour de posts Facebook analysé.
-- Une relance depuis le dashboard crée un passage « en_attente », exécuté par le Mac (scripts/agents-poller.sh).
create table if not exists public.agents_runs (
  id uuid primary key default gen_random_uuid(),
  agent text not null check (agent in ('veille_facebook', 'blog')),
  jour date not null,                                     -- veille : jour des posts analysés ; blog : jour de publication
  statut text not null default 'en_attente' check (statut in ('en_attente', 'en_cours', 'ok', 'erreur')),
  origine text not null default 'planifie' check (origine in ('planifie', 'dashboard')),
  groupes_lus int,
  groupes_echec jsonb,                                    -- [{ "groupe": "…", "raison": "…" }]
  messages_retenus int,
  resume text,
  debut timestamptz,
  fin timestamptz,
  created_at timestamptz not null default now()
);
create index if not exists agents_runs_agent_jour on public.agents_runs (agent, jour desc, created_at desc);

-- Messages Facebook retenus par la veille
create table if not exists public.agents_veille_messages (
  id uuid primary key default gen_random_uuid(),
  jour date not null,                                     -- jour du post
  post_le text,                                           -- date et heure du post (AAAA-MM-JJ HH:MM)
  groupe text not null,
  groupe_slug text,
  lien_groupe text,
  pseudo text,
  message text not null,
  type_demande text,
  lien_post text unique,
  reponse text,
  statut text not null default 'À répondre' check (statut in ('À répondre', 'Répondu', 'Ignoré')),
  run_id uuid references public.agents_runs (id) on delete set null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index if not exists agents_veille_messages_jour on public.agents_veille_messages (jour desc);

-- Articles du blog préparés par la routine cloud et publiés par le Publieur du Mac (Ressources/articles-auto/*)
create table if not exists public.agents_blog_articles (
  dossier text primary key,
  jour date not null,
  slug text,
  titre text,
  url text,
  statut text,                                            -- OK / ERREUR / en attente de publication
  commit text,
  erreur text,
  publie_le timestamptz,
  updated_at timestamptz not null default now()
);

-- État des programmes du Mac (dernier passage du Publieur, du poller…)
create table if not exists public.agents_etat (
  cle text primary key,
  valeur text,
  updated_at timestamptz not null default now()
);

alter table public.agents_runs enable row level security;
alter table public.agents_veille_messages enable row level security;
alter table public.agents_blog_articles enable row level security;
alter table public.agents_etat enable row level security;
do $$ declare t text; begin
  foreach t in array array['agents_runs', 'agents_veille_messages', 'agents_blog_articles', 'agents_etat'] loop
    execute format('drop policy if exists "Admin gère %1$s" on public.%1$I', t);
    execute format('create policy "Admin gère %1$s" on public.%1$I for all
      using ((auth.jwt() ->> ''email'') = ''mohamed.necib94310@gmail.com'')
      with check ((auth.jwt() ->> ''email'') = ''mohamed.necib94310@gmail.com'')', t);
  end loop;
end $$;
