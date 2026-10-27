-- Coût par modèle détaillé : entrée, sortie, puis total (Sonnet = synthèse, Haiku = correction), en dollars
alter table public.entraineur_rapports
  add column if not exists cout_sonnet_input_usd  numeric(12,6),
  add column if not exists cout_sonnet_output_usd numeric(12,6),
  add column if not exists cout_haiku_input_usd   numeric(12,6),
  add column if not exists cout_haiku_output_usd  numeric(12,6);

create or replace function public.entraineur_rapports_couts()
returns trigger language plpgsql set search_path = public as $$
declare ts tarifs_modeles; th tarifs_modeles;
begin
  new.cout_sonnet_input_usd := null; new.cout_sonnet_output_usd := null; new.cout_sonnet_usd := null;
  new.cout_haiku_input_usd := null; new.cout_haiku_output_usd := null; new.cout_haiku_usd := null;
  if new.model_sonnet is not null and new.model_haiku is not null then
    select * into ts from tarifs_modeles where model = new.model_sonnet;
    select * into th from tarifs_modeles where model = new.model_haiku;
    if ts.model is not null and th.model is not null then
      new.cout_sonnet_input_usd  := coalesce(new.sonnet_input_tokens, 0)  * ts.prix_input_par_mtok  / 1000000;
      new.cout_sonnet_output_usd := coalesce(new.sonnet_output_tokens, 0) * ts.prix_output_par_mtok / 1000000;
      new.cout_sonnet_usd        := new.cout_sonnet_input_usd + new.cout_sonnet_output_usd;
      new.cout_haiku_input_usd   := coalesce(new.haiku_input_tokens, 0)  * th.prix_input_par_mtok  / 1000000;
      new.cout_haiku_output_usd  := coalesce(new.haiku_output_tokens, 0) * th.prix_output_par_mtok / 1000000;
      new.cout_haiku_usd         := new.cout_haiku_input_usd + new.cout_haiku_output_usd;
      new.cout_input_usd  := new.cout_sonnet_input_usd + new.cout_haiku_input_usd;
      new.cout_output_usd := new.cout_sonnet_output_usd + new.cout_haiku_output_usd;
      new.cout_total_usd  := new.cout_sonnet_usd + new.cout_haiku_usd;
      return new;
    end if;
  else
    select * into ts from tarifs_modeles where model = new.model;
    if ts.model is not null then
      new.cout_input_usd  := coalesce(new.input_tokens, 0)  * ts.prix_input_par_mtok  / 1000000;
      new.cout_output_usd := coalesce(new.output_tokens, 0) * ts.prix_output_par_mtok / 1000000;
      new.cout_total_usd  := new.cout_input_usd + new.cout_output_usd;
      return new;
    end if;
  end if;
  -- modèle absent de tarifs_modeles : coûts laissés vides plutôt que faux
  new.cout_input_usd := null; new.cout_output_usd := null; new.cout_total_usd := null;
  return new;
end $$;

-- Recalcul des rapports existants
update public.entraineur_rapports set model_sonnet = model_sonnet where model_sonnet is not null;
