-- quiz_comptes contient tous les comptes QuizCRPE (profils_utilisateurs.parcours_signup = 'quizcrpe'), test de positionnement fait ou non.
-- Avant : la ligne n'était créée qu'à l'enregistrement du test (POST /api/quiz/positionnement, upsert sur user_id).
-- Une ligne sans test (positionnement null) ne change rien côté application : même comportement qu'une ligne absente.
-- Prénom, nom et parcours sont remplis par les déclencheurs existants (quiz_compte_identite, quiz_comptes_parcours).

create or replace function public.profils_parcours_vers_quiz()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  -- Compte QuizCRPE : ligne du quiz créée dès l'inscription
  if new.parcours_signup = 'quizcrpe' then
    insert into public.quiz_comptes (user_id, email)
    select new.user_id, coalesce(new.email, u.email) from auth.users u where u.id = new.user_id
    on conflict (user_id) do nothing;
  end if;
  update public.quiz_comptes set parcours_signup = new.parcours_signup
   where user_id = new.user_id and parcours_signup is distinct from new.parcours_signup;
  return new;
end;
$$;

-- Comptes QuizCRPE existants sans ligne dans quiz_comptes
insert into public.quiz_comptes (user_id, email)
select p.user_id, coalesce(p.email, u.email)
  from public.profils_utilisateurs p
  join auth.users u on u.id = p.user_id
 where p.parcours_signup = 'quizcrpe'
on conflict (user_id) do nothing;

-- Date de création des lignes ajoutées : date d'inscription du compte (appliqué à la main le 2026-11-04)
-- update public.quiz_comptes q set created_at = u.created_at from auth.users u
--  where u.id = q.user_id and q.positionnement is null;
