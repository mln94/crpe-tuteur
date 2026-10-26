-- Prénom, nom et e-mail de l'utilisateur dans la table de consommation (remplis automatiquement à l'insertion depuis auth.users)
alter table public.consommation_utilisateurs
  add column if not exists prenom text,
  add column if not exists nom text,
  add column if not exists email text;

create or replace function public.consommation_utilisateurs_identite()
returns trigger language plpgsql security definer set search_path = public, auth as $$
begin
  select nullif(u.raw_user_meta_data->>'prenom', ''), nullif(u.raw_user_meta_data->>'nom', ''), u.email
    into new.prenom, new.nom, new.email
  from auth.users u where u.id::text = new.user_id;
  return new;
end $$;
revoke all on function public.consommation_utilisateurs_identite() from public, anon, authenticated;

create or replace trigger consommation_utilisateurs_identite
  before insert on public.consommation_utilisateurs
  for each row execute function public.consommation_utilisateurs_identite();

-- Reprise des lignes déjà présentes
update public.consommation_utilisateurs c
set prenom = nullif(u.raw_user_meta_data->>'prenom', ''), nom = nullif(u.raw_user_meta_data->>'nom', ''), email = u.email
from auth.users u where u.id::text = c.user_id;

-- Vue renommée : consommation_par_utilisateur → consommation_totale_par_utilisateur, avec prénom, nom et e-mail
drop view if exists public.consommation_par_utilisateur;
create view public.consommation_totale_par_utilisateur with (security_invoker = true) as
 SELECT c.user_id,
    (array_agg(c.prenom ORDER BY c.created_at DESC))[1] AS prenom,
    (array_agg(c.nom ORDER BY c.created_at DESC))[1] AS nom,
    (array_agg(c.email ORDER BY c.created_at DESC))[1] AS email,
    count(*) AS nombre_requetes_total,
    sum(c.input_tokens) AS total_input_tokens,
    sum(c.output_tokens) AS total_output_tokens,
    sum(c.cache_read_input_tokens) AS total_cache_read_tokens,
    sum(c.cache_creation_input_tokens) AS total_cache_creation_tokens,
    round(sum(c.input_tokens::numeric / 1000000 * COALESCE(t.prix_input_par_mtok, 0) + c.output_tokens::numeric / 1000000 * COALESCE(t.prix_output_par_mtok, 0) + c.cache_read_input_tokens::numeric / 1000000 * COALESCE(t.prix_cache_lecture_par_mtok, 0) + c.cache_creation_input_tokens::numeric / 1000000 * COALESCE(t.prix_cache_ecriture_par_mtok, 0)), 4) AS cout_estime_usd,
    min(c.created_at) AS premiere_requete_le,
    max(c.created_at) AS derniere_requete_le,
    string_agg(DISTINCT c.model, ', ' ORDER BY c.model) AS modeles_utilises,
    round(sum(c.cout_input_usd), 6) AS cout_input_usd,
    round(sum(c.cout_output_usd), 6) AS cout_output_usd,
    round(sum(c.cout_cache_lecture_usd), 6) AS cout_cache_lecture_usd,
    round(sum(c.cout_cache_ecriture_usd), 6) AS cout_cache_ecriture_usd,
    round(sum(c.cout_total_usd), 6) AS cout_total_usd
   FROM consommation_utilisateurs c
     LEFT JOIN tarifs_modeles t ON t.model = c.model
  GROUP BY c.user_id;
revoke all on public.consommation_totale_par_utilisateur from anon, authenticated;
