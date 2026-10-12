-- Entraîneur CRPE : coût de chaque rapport, en dollars (prix Anthropic), calculé selon le modèle utilisé
-- à partir de la table tarifs_modeles (prix par million de tokens). Ajout seul, rien n'est supprimé.
alter table public.entraineur_rapports
  add column if not exists cout_input_usd  numeric(12,6),
  add column if not exists cout_output_usd numeric(12,6),
  add column if not exists cout_total_usd  numeric(12,6);

create or replace function public.entraineur_rapports_couts()
returns trigger language plpgsql set search_path = public as $$
declare t tarifs_modeles;
begin
  select * into t from tarifs_modeles where model = new.model;
  if found then
    new.cout_input_usd  := coalesce(new.input_tokens, 0)  * t.prix_input_par_mtok  / 1000000;
    new.cout_output_usd := coalesce(new.output_tokens, 0) * t.prix_output_par_mtok / 1000000;
    new.cout_total_usd  := new.cout_input_usd + new.cout_output_usd;
  else
    -- modèle absent de tarifs_modeles : coûts laissés vides plutôt que faux
    new.cout_input_usd := null; new.cout_output_usd := null; new.cout_total_usd := null;
  end if;
  return new;
end $$;

create or replace trigger entraineur_rapports_couts
  before insert or update of model, input_tokens, output_tokens on public.entraineur_rapports
  for each row execute function public.entraineur_rapports_couts();
