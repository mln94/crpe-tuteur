-- Entraîneur CRPE : copie ANONYME du contenu des rapports, conservée pour créer des contenus pédagogiques.
-- Aucune donnée d'identité : ni contact, ni lien de rapport, ni date précise (seulement le mois).
-- Une ligne par réponse ; serie_id (aléatoire, sans lien avec le rapport) regroupe les 5 réponses d'une même série.
create table if not exists public.entraineur_corpus (
  id                uuid primary key default gen_random_uuid(),
  serie_id          uuid not null,
  position          smallint not null check (position between 1 and 10),
  mois              date not null,                       -- premier jour du mois de la série
  matiere           text not null check (matiere in ('maths', 'francais')),
  categorie         text,
  classe            text,
  enonce            text,
  texte_support     text,
  question          text not null,
  reponse_attendue  text,
  reponse_candidat  text not null,
  note              numeric(4,1),
  niveau            text,
  evaluation        jsonb not null,
  synthese_serie    jsonb,                               -- analyse de la manière de répondre (identique pour les 5 lignes d'une série)
  model             text,
  created_at        timestamptz not null default date_trunc('month', now())
);
create index if not exists entraineur_corpus_categorie_idx on public.entraineur_corpus (matiere, categorie);
create index if not exists entraineur_corpus_serie_idx on public.entraineur_corpus (serie_id);

alter table public.entraineur_corpus enable row level security;
revoke all on public.entraineur_corpus from anon, authenticated;

-- Retire d'un texte les e-mails, numéros de téléphone, prénom et nom de la personne
create or replace function public.entraineur_anonymise(t text, prenom text, nom text)
returns text language sql immutable set search_path = public as $$
  select regexp_replace(regexp_replace(regexp_replace(regexp_replace(coalesce(t, ''),
    '[[:alnum:]._%+-]+@[[:alnum:].-]+\.[[:alpha:]]{2,}', '[e-mail]', 'g'),
    '(\+33 ?|0033 ?|\m0)[1-9]([ .-]?[0-9]{2}){4}\M', '[téléphone]', 'g'),
    case when length(coalesce(prenom, '')) >= 2 then '\m' || regexp_replace(prenom, '([.*+?^${}()|\[\]\\])', '\\\1', 'g') || '\M' else '(?!)' end, '[prénom]', 'gi'),
    case when length(coalesce(nom, '')) >= 2 then '\m' || regexp_replace(nom, '([.*+?^${}()|\[\]\\])', '\\\1', 'g') || '\M' else '(?!)' end, '[nom]', 'gi')
$$;
revoke all on function public.entraineur_anonymise(text, text, text) from public, anon, authenticated;

-- Reprise anonymisée des rapports déjà générés (e-mails, téléphones, prénom et nom retirés des textes)
with r as (
  select r.*, gen_random_uuid() as serie_id, l.prenom, l.nom
  from public.entraineur_rapports r join public.entraineur_leads l on l.id = r.lead_id
),
items as (
  select r.serie_id, r.matiere, r.model, r.synthese, r.created_at, r.prenom, r.nom, q.value as q, q.ordinality as pos
  from r cross join lateral jsonb_array_elements(r.questions) with ordinality q
)
insert into public.entraineur_corpus (serie_id, position, mois, matiere, categorie, classe, enonce, texte_support, question,
  reponse_attendue, reponse_candidat, note, niveau, evaluation, synthese_serie, model, created_at)
select serie_id, pos, date_trunc('month', created_at)::date, matiere,
  q->>'categorie', q->>'classe', q->>'enonce', q->>'texte_support', q->>'question', q->>'reponse_attendue',
  public.entraineur_anonymise(q->>'reponse', prenom, nom),
  (q->'evaluation'->>'note')::numeric, q->'evaluation'->>'niveau',
  public.entraineur_anonymise((q->'evaluation')::text, prenom, nom)::jsonb,
  public.entraineur_anonymise(synthese::text, prenom, nom)::jsonb, model,
  date_trunc('month', created_at)
from items;
