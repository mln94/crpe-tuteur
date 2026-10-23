-- Fenêtre d'inscription : année où la personne passera le CRPE et nombre de fois où elle l'a déjà passé
-- (métadonnées annee_examen et tentatives_crpe du compte), recopiés dans profils_utilisateurs.
--   annee_examen    : '2027', '2028', '2029' ou 'Je ne sais pas encore'
--   tentatives_crpe : 0 = première fois, 1, 2, 3 = 3 fois ou plus
alter table public.profils_utilisateurs
  add column if not exists annee_examen text,
  add column if not exists tentatives_crpe smallint check (tentatives_crpe between 0 and 3);

-- Valeurs lues dans les métadonnées : vides ou invalides → null
create or replace function public.meta_annee_examen(meta jsonb) returns text language sql immutable set search_path = '' as $$
  select nullif(left(meta->>'annee_examen', 40), '')
$$;
create or replace function public.meta_tentatives_crpe(meta jsonb) returns smallint language sql immutable set search_path = '' as $$
  select case when meta->>'tentatives_crpe' ~ '^[0-3]$' then (meta->>'tentatives_crpe')::smallint end
$$;

create or replace function public.handle_new_user()
 returns trigger
 language plpgsql
 security definer
 set search_path to 'public'
as $function$
begin
  insert into public.profils_utilisateurs (user_id, parcours_signup, email, prenom, nom, consent_newsletter, consent_partenaires, consent_at,
                                           annee_examen, tentatives_crpe)
  values (new.id,
          case when new.raw_user_meta_data->>'parcours' = 'quizcrpe' then 'quizcrpe' else 'passcrpe' end,
          new.email, nullif(new.raw_user_meta_data->>'prenom', ''), nullif(new.raw_user_meta_data->>'nom', ''),
          coalesce((new.raw_user_meta_data->>'consent_conseils')::boolean, false),
          coalesce((new.raw_user_meta_data->>'consent_partenaires')::boolean, false),
          (new.raw_user_meta_data->>'consent_at')::timestamptz,
          public.meta_annee_examen(new.raw_user_meta_data), public.meta_tentatives_crpe(new.raw_user_meta_data))
  on conflict (user_id) do update set
    email  = excluded.email,
    prenom = coalesce(excluded.prenom, profils_utilisateurs.prenom),
    nom    = coalesce(excluded.nom, profils_utilisateurs.nom),
    parcours_signup = coalesce(profils_utilisateurs.parcours_signup, excluded.parcours_signup),
    consent_newsletter  = excluded.consent_newsletter,
    consent_partenaires = excluded.consent_partenaires,
    consent_at          = excluded.consent_at,
    annee_examen    = coalesce(excluded.annee_examen, profils_utilisateurs.annee_examen),
    tentatives_crpe = coalesce(excluded.tentatives_crpe, profils_utilisateurs.tentatives_crpe);
  return new;
end;
$function$;

create or replace function public.sync_profil_identite()
 returns trigger
 language plpgsql
 security definer
 set search_path to 'public'
as $function$
begin
  update public.profils_utilisateurs set
    email  = new.email,
    prenom = coalesce(nullif(new.raw_user_meta_data->>'prenom', ''), prenom),
    nom    = coalesce(nullif(new.raw_user_meta_data->>'nom', ''), nom),
    consent_newsletter  = coalesce((new.raw_user_meta_data->>'consent_conseils')::boolean, consent_newsletter),
    consent_partenaires = coalesce((new.raw_user_meta_data->>'consent_partenaires')::boolean, consent_partenaires),
    consent_at          = coalesce((new.raw_user_meta_data->>'consent_at')::timestamptz, consent_at),
    annee_examen        = coalesce(public.meta_annee_examen(new.raw_user_meta_data), annee_examen),
    tentatives_crpe     = coalesce(public.meta_tentatives_crpe(new.raw_user_meta_data), tentatives_crpe)
  where user_id = new.id;
  return new;
end;
$function$;
