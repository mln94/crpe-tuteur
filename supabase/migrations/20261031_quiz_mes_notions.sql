-- « Mes notions » (QuizCRPE) : une ligne par notion, la progression de chaque compte par notion, et les totaux calculés en base.
-- Rien n'est modifié dans les tables existantes.

-- ── Notions : déduites de quiz_questions (questions actives de même clé « notion ») ──
-- intitule : formulation « Je sais… » de la notion, remplie plus tard ; exemple : texte de sa première question, affiché tant que
-- l'intitulé est vide (le sous-thème est commun à plusieurs notions).
create table if not exists public.quiz_notions (
  matiere text not null,
  notion text not null,
  theme text not null default 'Notions',
  sous_theme text,
  classe text,
  niveau text,
  nb_questions integer not null default 0,
  ordre integer not null default 0,
  intitule text,
  exemple text,
  primary key (matiere, notion)
);
create index if not exists quiz_notions_theme_idx on public.quiz_notions (matiere, theme);
alter table public.quiz_notions enable row level security;

-- À relancer après chaque ajout ou remplacement de questions (scripts/quiz/inserer.mjs) : garde les intitulés déjà écrits.
create or replace function public.quiz_notions_sync()
returns integer
language plpgsql
security definer
set search_path = public
as $$
declare n integer;
begin
  insert into quiz_notions (matiere, notion, theme, sous_theme, classe, niveau, nb_questions, ordre, exemple)
  select matiere, notion, coalesce(min(theme), 'Notions'), min(sous_theme), min(classe), min(niveau), count(*),
         row_number() over (partition by matiere order by min(ordre), min(id)),
         (array_agg(question order by ordre, id))[1]
    from quiz_questions where actif and notion is not null
   group by matiere, notion
  on conflict (matiere, notion) do update
    set theme = excluded.theme, sous_theme = excluded.sous_theme, classe = excluded.classe, niveau = excluded.niveau,
        nb_questions = excluded.nb_questions, ordre = excluded.ordre, exemple = excluded.exemple;
  delete from quiz_notions n2
   where not exists (select 1 from quiz_questions q where q.actif and q.matiere = n2.matiere and q.notion = n2.notion);
  select count(*) into n from quiz_notions;
  return n;
end;
$$;
revoke all on function public.quiz_notions_sync() from public, anon, authenticated;
select public.quiz_notions_sync();

-- ── Progression par compte et par notion : même contenu que la progression gardée par le navigateur ──
-- ok / vus : questions réussies / vues ; due : prochaine révision (ms) ; derniere_ok : résultat de la dernière réponse.
create table if not exists public.quiz_progres_notions (
  user_id uuid not null references auth.users (id) on delete cascade,
  matiere text not null,
  notion text not null,
  ok bigint[] not null default '{}',
  vus bigint[] not null default '{}',
  erreurs integer not null default 0,
  fois integer not null default 0,
  due bigint not null default 0,
  maitrise boolean not null default false,
  derniere_ok boolean,
  derniere_at timestamptz,
  updated_at timestamptz not null default now(),
  primary key (user_id, matiere, notion)
);
create index if not exists quiz_progres_revoir_idx on public.quiz_progres_notions (user_id, derniere_at desc) where derniere_ok = false;
alter table public.quiz_progres_notions enable row level security;
drop policy if exists "Users view own notion progress" on public.quiz_progres_notions;
create policy "Users view own notion progress" on public.quiz_progres_notions for select using (auth.uid() = user_id);

-- Fusion de la progression envoyée par le navigateur (après chaque réponse, ou toute la progression locale une fois) :
-- questions réussies et vues réunies, compteurs au plus haut, dernière réponse = la plus récente.
-- p_lignes : [{ matiere, notion, ok, vus, erreurs, fois, due, maitrise, derniere_ok, derniere_at }]
create or replace function public.quiz_progres_fusion(p_lignes jsonb)
returns integer
language plpgsql
security definer
set search_path = public
as $$
declare uid uuid := auth.uid(); n integer;
begin
  if uid is null then raise exception 'Connexion requise'; end if;
  if jsonb_typeof(p_lignes) <> 'array' or jsonb_array_length(p_lignes) > 5000 then raise exception 'Données invalides'; end if;
  insert into quiz_progres_notions as p (user_id, matiere, notion, ok, vus, erreurs, fois, due, maitrise, derniere_ok, derniere_at, updated_at)
  select uid, l.matiere, l.notion,
         coalesce((select array_agg(distinct x::bigint) from jsonb_array_elements_text(l.ok) x), '{}'),
         coalesce((select array_agg(distinct x::bigint) from jsonb_array_elements_text(l.vus) x), '{}'),
         greatest(coalesce(l.erreurs, 0), 0), greatest(coalesce(l.fois, 0), 0), greatest(coalesce(l.due, 0), 0),
         coalesce(l.maitrise, false), l.derniere_ok, l.derniere_at, now()
    from jsonb_to_recordset(p_lignes) as l(matiere text, notion text, ok jsonb, vus jsonb, erreurs integer, fois integer, due bigint,
                                           maitrise boolean, derniere_ok boolean, derniere_at timestamptz)
   where exists (select 1 from quiz_notions qn where qn.matiere = l.matiere and qn.notion = l.notion)
  on conflict (user_id, matiere, notion) do update set
    ok = (select coalesce(array_agg(distinct x), '{}') from unnest(p.ok || excluded.ok) x),
    vus = (select coalesce(array_agg(distinct x), '{}') from unnest(p.vus || excluded.vus) x),
    erreurs = greatest(p.erreurs, excluded.erreurs),
    fois = greatest(p.fois, excluded.fois),
    due = case when excluded.derniere_at is not null and (p.derniere_at is null or excluded.derniere_at >= p.derniere_at) then excluded.due else p.due end,
    maitrise = p.maitrise or excluded.maitrise,
    derniere_ok = case when excluded.derniere_at is not null and (p.derniere_at is null or excluded.derniere_at >= p.derniere_at) then excluded.derniere_ok else p.derniere_ok end,
    derniere_at = greatest(p.derniere_at, excluded.derniere_at),
    updated_at = now();
  get diagnostics n = row_count;
  return n;
end;
$$;
revoke all on function public.quiz_progres_fusion(jsonb) from public, anon;
grant execute on function public.quiz_progres_fusion(jsonb) to authenticated;

-- Statut d'une notion pour un compte (même règle que l'appli : 3 bonnes réponses à des questions différentes = maîtrisée,
-- une notion maîtrisée le reste) : pas_vue, a_revoir (dernière réponse fausse), en_cours, maitrisee.
create or replace function public.quiz_statut_notion(p public.quiz_progres_notions)
returns text
language sql
immutable
as $$
  select case
    when p.user_id is null or (p.fois = 0 and cardinality(p.ok) = 0 and p.erreurs = 0 and cardinality(p.vus) = 0) then 'pas_vue'
    when p.maitrise then 'maitrisee'
    when p.derniere_ok = false then 'a_revoir'
    when p.derniere_ok is null and cardinality(p.ok) = 0 then 'a_revoir'
    else 'en_cours'
  end
$$;

-- Totaux par matière et 5 notions à revoir les plus récentes (écran « Mes notions »)
create or replace function public.quiz_notions_resume()
returns jsonb
language sql
stable
security definer
set search_path = public
as $$
  with s as (
    select n.matiere, quiz_statut_notion(p) as statut
      from quiz_notions n
      left join quiz_progres_notions p on p.user_id = auth.uid() and p.matiere = n.matiere and p.notion = n.notion
  ), r as (
    select n.matiere, n.notion, n.intitule, n.exemple, n.theme, p.derniere_at
      from quiz_progres_notions p join quiz_notions n on n.matiere = p.matiere and n.notion = p.notion
     where p.user_id = auth.uid() and not p.maitrise and quiz_statut_notion(p) = 'a_revoir'
     order by p.derniere_at desc nulls last limit 5
  )
  select jsonb_build_object(
    'matieres', (select jsonb_agg(jsonb_build_object('matiere', matiere, 'total', total, 'maitrisees', m, 'en_cours', c, 'a_revoir', r2))
                   from (select matiere, count(*) total, count(*) filter (where statut = 'maitrisee') m,
                                count(*) filter (where statut = 'en_cours') c, count(*) filter (where statut = 'a_revoir') r2
                           from s group by matiere) t),
    'revoir', coalesce((select jsonb_agg(to_jsonb(r) order by r.derniere_at desc nulls last) from r), '[]'::jsonb))
  where auth.uid() is not null
$$;

-- Thèmes d'une matière avec leurs totaux par statut (les notions d'un thème sont chargées à son ouverture)
create or replace function public.quiz_notions_themes(p_matiere text)
returns table (theme text, ordre integer, total integer, maitrisees integer, en_cours integer, a_revoir integer, pas_vues integer)
language sql
stable
security definer
set search_path = public
as $$
  select n.theme, min(n.ordre)::integer, count(*)::integer,
         count(*) filter (where quiz_statut_notion(p) = 'maitrisee')::integer,
         count(*) filter (where quiz_statut_notion(p) = 'en_cours')::integer,
         count(*) filter (where quiz_statut_notion(p) = 'a_revoir')::integer,
         count(*) filter (where quiz_statut_notion(p) = 'pas_vue')::integer
    from quiz_notions n
    left join quiz_progres_notions p on p.user_id = auth.uid() and p.matiere = n.matiere and p.notion = n.notion
   where n.matiere = p_matiere and auth.uid() is not null
   group by n.theme
   order by min(n.ordre)
$$;

-- Notions d'un thème avec leur statut pour le compte connecté
create or replace function public.quiz_notions_liste(p_matiere text, p_theme text)
returns table (notion text, intitule text, exemple text, classe text, niveau text, nb_questions integer, ordre integer,
               bonnes integer, fois integer, statut text, derniere_ok boolean, derniere_at timestamptz)
language sql
stable
security definer
set search_path = public
as $$
  select n.notion, n.intitule, n.exemple, n.classe, n.niveau, n.nb_questions, n.ordre,
         coalesce(cardinality(p.ok), 0), coalesce(p.fois, 0), quiz_statut_notion(p), p.derniere_ok, p.derniere_at
    from quiz_notions n
    left join quiz_progres_notions p on p.user_id = auth.uid() and p.matiere = n.matiere and p.notion = n.notion
   where n.matiere = p_matiere and n.theme = p_theme and auth.uid() is not null
   order by n.ordre
$$;

revoke all on function public.quiz_notions_resume() from public, anon;
revoke all on function public.quiz_notions_themes(text) from public, anon;
revoke all on function public.quiz_notions_liste(text, text) from public, anon;
grant execute on function public.quiz_notions_resume() to authenticated;
grant execute on function public.quiz_notions_themes(text) to authenticated;
grant execute on function public.quiz_notions_liste(text, text) to authenticated;
