-- Klaviyo : date de la dernière connexion (date_dernier_signin), envoyée à chaque connexion.
-- auth.users.last_sign_in_at change à chaque connexion (mot de passe, lien de confirmation) : le serveur
-- (POST /api/webhook/supabase-auth, type SIGNIN, app.js) relit le compte et met à jour le profil Klaviyo.
-- date_creation_compte est envoyée à l'inscription (type INSERT) ; les profils existants sont remplis par
-- scripts/klaviyo_sync_dates_compte.mjs.

create or replace function public.handle_user_signin_klaviyo()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  perform net.http_post(
    url := 'https://www.passcrpe.fr/api/webhook/supabase-auth',
    headers := jsonb_build_object('Content-Type', 'application/json'),
    body := jsonb_build_object('type', 'SIGNIN', 'record', jsonb_build_object('id', new.id))
  );
  return new;
end;
$$;

drop trigger if exists on_auth_user_signin_klaviyo on auth.users;
create trigger on_auth_user_signin_klaviyo
  after update of last_sign_in_at on auth.users
  for each row
  when (new.last_sign_in_at is not null and old.last_sign_in_at is distinct from new.last_sign_in_at)
  execute function public.handle_user_signin_klaviyo();
