-- quiz_comptes.parcours_signup : par où la personne est arrivée en premier (copie de profils_utilisateurs.parcours_signup).
-- Rempli à la création de la ligne du quiz, et recopié si le parcours du profil est renseigné ou modifié ensuite.

alter table public.quiz_comptes add column if not exists parcours_signup text;

create or replace function public.quiz_comptes_parcours()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  if new.parcours_signup is null then
    select p.parcours_signup into new.parcours_signup from public.profils_utilisateurs p where p.user_id = new.user_id;
  end if;
  return new;
end;
$$;

drop trigger if exists quiz_comptes_parcours on public.quiz_comptes;
create trigger quiz_comptes_parcours
  before insert on public.quiz_comptes
  for each row execute function public.quiz_comptes_parcours();

create or replace function public.profils_parcours_vers_quiz()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  update public.quiz_comptes set parcours_signup = new.parcours_signup
   where user_id = new.user_id and parcours_signup is distinct from new.parcours_signup;
  return new;
end;
$$;

drop trigger if exists profils_parcours_vers_quiz on public.profils_utilisateurs;
create trigger profils_parcours_vers_quiz
  after insert or update of parcours_signup on public.profils_utilisateurs
  for each row when (new.parcours_signup is not null)
  execute function public.profils_parcours_vers_quiz();

-- Comptes existants
update public.quiz_comptes q set parcours_signup = p.parcours_signup
  from public.profils_utilisateurs p
 where p.user_id = q.user_id and q.parcours_signup is distinct from p.parcours_signup;
