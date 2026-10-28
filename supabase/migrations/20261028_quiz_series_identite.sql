-- quiz_series : prénom, nom et e-mail de la personne qui a fait la série (lus dans auth.users à l'enregistrement de la série).
-- La série est enregistrée par le navigateur : le trigger remplace toujours ces champs par ceux du compte (user_id).

alter table public.quiz_series
  add column if not exists prenom text,
  add column if not exists nom text,
  add column if not exists email text;

create or replace function public.quiz_series_identite()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  select u.raw_user_meta_data->>'prenom', u.raw_user_meta_data->>'nom', u.email
    into new.prenom, new.nom, new.email
    from auth.users u where u.id = new.user_id;
  return new;
end;
$$;

drop trigger if exists quiz_series_identite on public.quiz_series;
create trigger quiz_series_identite
  before insert on public.quiz_series
  for each row execute function public.quiz_series_identite();

-- Séries déjà enregistrées
update public.quiz_series s
   set prenom = u.raw_user_meta_data->>'prenom', nom = u.raw_user_meta_data->>'nom', email = u.email
  from auth.users u
 where u.id = s.user_id;
