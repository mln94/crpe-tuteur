-- Prix des modèles utilisés par l'Entraîneur CRPE (dollars par million de tokens, tarifs Anthropic)
insert into public.tarifs_modeles (model, prix_input_par_mtok, prix_output_par_mtok, prix_cache_lecture_par_mtok, prix_cache_ecriture_par_mtok) values
  ('claude-sonnet-5-5', 2.00, 10.00, 0.20, 2.50),
  ('claude-haiku-5-5', 0.10, 0.50, 0.01, 0.125)
on conflict (model) do update set prix_input_par_mtok = excluded.prix_input_par_mtok, prix_output_par_mtok = excluded.prix_output_par_mtok,
  prix_cache_lecture_par_mtok = excluded.prix_cache_lecture_par_mtok, prix_cache_ecriture_par_mtok = excluded.prix_cache_ecriture_par_mtok;

-- Tokens séparés par modèle : synthèse (modèle principal) et correction des réponses (modèle de correction)
alter table public.entraineur_rapports
  add column if not exists model_synthese text,
  add column if not exists synthese_input_tokens integer,
  add column if not exists synthese_output_tokens integer,
  add column if not exists model_correction text,
  add column if not exists correction_input_tokens integer,
  add column if not exists correction_output_tokens integer;

-- Coût calculé avec le prix de chaque modèle ; anciens rapports (tokens non séparés) : même calcul qu'avant
create or replace function public.entraineur_rapports_couts()
returns trigger language plpgsql set search_path = public as $$
declare ts tarifs_modeles; tc tarifs_modeles;
begin
  if new.model_synthese is not null and new.model_correction is not null then
    select * into ts from tarifs_modeles where model = new.model_synthese;
    select * into tc from tarifs_modeles where model = new.model_correction;
    if ts.model is not null and tc.model is not null then
      new.cout_input_usd  := (coalesce(new.synthese_input_tokens, 0) * ts.prix_input_par_mtok + coalesce(new.correction_input_tokens, 0) * tc.prix_input_par_mtok) / 1000000;
      new.cout_output_usd := (coalesce(new.synthese_output_tokens, 0) * ts.prix_output_par_mtok + coalesce(new.correction_output_tokens, 0) * tc.prix_output_par_mtok) / 1000000;
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
  before insert or update of model, input_tokens, output_tokens, model_synthese, model_correction,
    synthese_input_tokens, synthese_output_tokens, correction_input_tokens, correction_output_tokens
  on public.entraineur_rapports
  for each row execute function public.entraineur_rapports_couts();
