-- profils_utilisateurs.email_verified : l'e-mail du compte est confirmé (copie de auth.users.email_confirmed_at)
-- Tenu à jour par deux triggers : à la création du profil, et à la confirmation de l'e-mail (lien ou confirmation manuelle).

alter table public.profils_utilisateurs
  add column if not exists email_verified boolean not null default false,
  add column if not exists email_verified_at timestamptz;

create or replace function public.profils_utilisateurs_email_verified()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  select u.email_confirmed_at is not null, u.email_confirmed_at
    into new.email_verified, new.email_verified_at
    from auth.users u where u.id = new.user_id;
  new.email_verified := coalesce(new.email_verified, false);
  return new;
end;
$$;

drop trigger if exists profils_utilisateurs_email_verified on public.profils_utilisateurs;
create trigger profils_utilisateurs_email_verified
  before insert on public.profils_utilisateurs
  for each row execute function public.profils_utilisateurs_email_verified();

create or replace function public.auth_user_email_verified_profil()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  update public.profils_utilisateurs
     set email_verified = new.email_confirmed_at is not null,
         email_verified_at = new.email_confirmed_at
   where user_id = new.id;
  return new;
end;
$$;

drop trigger if exists on_auth_user_email_verified_profil on auth.users;
create trigger on_auth_user_email_verified_profil
  after update of email_confirmed_at on auth.users
  for each row
  when (old.email_confirmed_at is distinct from new.email_confirmed_at)
  execute function public.auth_user_email_verified_profil();

-- Comptes existants
update public.profils_utilisateurs p
   set email_verified = u.email_confirmed_at is not null,
       email_verified_at = u.email_confirmed_at
  from auth.users u
 where u.id = p.user_id;
