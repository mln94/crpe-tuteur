-- Vue consommation_par_utilisateur : ajout de la colonne modeles_utilises (modèles d'IA utilisés par chaque utilisateur).
-- Même définition qu'avant, la nouvelle colonne est ajoutée à la fin.
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
    string_agg(DISTINCT c.model, ', ' ORDER BY c.model) AS modeles_utilises
   FROM consommation_utilisateurs c
     LEFT JOIN tarifs_modeles t ON t.model = c.model
  GROUP BY c.user_id;
