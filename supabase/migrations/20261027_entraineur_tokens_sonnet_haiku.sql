-- Colonnes de tokens nommées par modèle : Sonnet (synthèse) et Haiku (correction des réponses)
alter table public.entraineur_rapports rename column synthese_input_tokens to sonnet_input_tokens;
alter table public.entraineur_rapports rename column synthese_output_tokens to sonnet_output_tokens;
alter table public.entraineur_rapports rename column correction_input_tokens to haiku_input_tokens;
alter table public.entraineur_rapports rename column correction_output_tokens to haiku_output_tokens;
alter table public.entraineur_rapports rename column model_synthese to model_sonnet;
alter table public.entraineur_rapports rename column model_correction to model_haiku;

create or replace function public.entraineur_rapports_couts()
returns trigger language plpgsql set search_path = public as $$
declare ts tarifs_modeles; th tarifs_modeles;
begin
  if new.model_sonnet is not null and new.model_haiku is not null then
    select * into ts from tarifs_modeles where model = new.model_sonnet;
    select * into th from tarifs_modeles where model = new.model_haiku;
    if ts.model is not null and th.model is not null then
      new.cout_input_usd  := (coalesce(new.sonnet_input_tokens, 0) * ts.prix_input_par_mtok + coalesce(new.haiku_input_tokens, 0) * th.prix_input_par_mtok) / 1000000;
      new.cout_output_usd := (coalesce(new.sonnet_output_tokens, 0) * ts.prix_output_par_mtok + coalesce(new.haiku_output_tokens, 0) * th.prix_output_par_mtok) / 1000000;
      new.cout_total_usd  := new.cout_input_usd + new.cout_output_usd;
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

drop trigger if exists entraineur_rapports_couts on public.entraineur_rapports;
create trigger entraineur_rapports_couts
  before insert or update of model, input_tokens, output_tokens, model_sonnet, model_haiku,
    sonnet_input_tokens, sonnet_output_tokens, haiku_input_tokens, haiku_output_tokens
  on public.entraineur_rapports
  for each row execute function public.entraineur_rapports_couts();
