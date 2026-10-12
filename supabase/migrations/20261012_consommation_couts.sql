-- Coût de chaque appel à l'IA de l'application, en dollars, selon le modèle (table tarifs_modeles, prix par million de tokens).
-- Ajout seul : colonnes calculées automatiquement à l'insertion, puis reprises dans la vue consommation_par_utilisateur.
alter table public.consommation_utilisateurs
  add column if not exists cout_input_usd          numeric(12,6),
  add column if not exists cout_output_usd         numeric(12,6),
  add column if not exists cout_cache_lecture_usd  numeric(12,6),
  add column if not exists cout_cache_ecriture_usd numeric(12,6),
  add column if not exists cout_total_usd          numeric(12,6);

create or replace function public.consommation_utilisateurs_couts()
returns trigger language plpgsql set search_path = public as $$
declare t tarifs_modeles;
begin
  select * into t from tarifs_modeles where model = new.model;
  if found then
    new.cout_input_usd          := coalesce(new.input_tokens, 0)                * t.prix_input_par_mtok          / 1000000;
    new.cout_output_usd         := coalesce(new.output_tokens, 0)               * t.prix_output_par_mtok         / 1000000;
    new.cout_cache_lecture_usd  := coalesce(new.cache_read_input_tokens, 0)     * t.prix_cache_lecture_par_mtok  / 1000000;
    new.cout_cache_ecriture_usd := coalesce(new.cache_creation_input_tokens, 0) * t.prix_cache_ecriture_par_mtok / 1000000;
    new.cout_total_usd := new.cout_input_usd + new.cout_output_usd + new.cout_cache_lecture_usd + new.cout_cache_ecriture_usd;
  else
    -- modèle absent de tarifs_modeles : coûts laissés vides plutôt que faux
    new.cout_input_usd := null; new.cout_output_usd := null; new.cout_cache_lecture_usd := null;
    new.cout_cache_ecriture_usd := null; new.cout_total_usd := null;
  end if;
  return new;
end $$;

create or replace trigger consommation_utilisateurs_couts
  before insert or update of model, input_tokens, output_tokens, cache_read_input_tokens, cache_creation_input_tokens
  on public.consommation_utilisateurs
  for each row execute function public.consommation_utilisateurs_couts();

-- Calcul pour les lignes déjà présentes
update public.consommation_utilisateurs set model = model where cout_total_usd is null;

-- Vue par utilisateur : totaux de coûts détaillés ajoutés à la fin
create or replace view public.consommation_par_utilisateur with (security_invoker = true) as
 SELECT c.user_id,
    count(*) AS nombre_requetes_total,
    sum(c.input_tokens) AS total_input_tokens,
    sum(c.output_tokens) AS total_output_tokens,
    sum(c.cache_read_input_tokens) AS total_cache_read_tokens,
    sum(c.cache_creation_input_tokens) AS total_cache_creation_tokens,
    round(sum(c.input_tokens::numeric / 1000000::numeric * COALESCE(t.prix_input_par_mtok, 0::numeric) + c.output_tokens::numeric / 1000000::numeric * COALESCE(t.prix_output_par_mtok, 0::numeric) + c.cache_read_input_tokens::numeric / 1000000::numeric * COALESCE(t.prix_cache_lecture_par_mtok, 0::numeric) + c.cache_creation_input_tokens::numeric / 1000000::numeric * COALESCE(t.prix_cache_ecriture_par_mtok, 0::numeric)), 4) AS cout_estime_usd,
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
