-- Inscriptions → Klaviyo depuis la base, quelle que soit la page d'inscription du site.
-- L'ancien trigger appelait la fonction Edge « klaviyo-signup », qui n'existe pas (réponse 404) : les inscrits des pages
-- autres que l'accueil et le quiz n'arrivaient dans Klaviyo qu'à la confirmation de l'e-mail, et seulement avec la newsletter.
-- Les deux triggers appellent maintenant le serveur (POST /api/webhook/supabase-auth, app.js) avec l'id du compte :
--   création du compte          → profil Klaviyo, signup_confirmed = false
--   confirmation de l'e-mail     → signup_confirmed = true

create or replace function public.handle_new_user_klaviyo()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  perform net.http_post(
    url := 'https://www.passcrpe.fr/api/webhook/supabase-auth',
    headers := jsonb_build_object('Content-Type', 'application/json'),
    body := jsonb_build_object('type', 'INSERT', 'record', jsonb_build_object('id', new.id))
  );
  return new;
end;
$$;

create or replace function public.handle_user_confirmed_klaviyo()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  perform net.http_post(
    url := 'https://www.passcrpe.fr/api/webhook/supabase-auth',
    headers := jsonb_build_object('Content-Type', 'application/json'),
    body := jsonb_build_object('type', 'UPDATE', 'record', jsonb_build_object('id', new.id))
  );
  return new;
end;
$$;

drop trigger if exists on_auth_user_confirmed_klaviyo on auth.users;
create trigger on_auth_user_confirmed_klaviyo
  after update of email_confirmed_at on auth.users
  for each row
  when (old.email_confirmed_at is null and new.email_confirmed_at is not null)
  execute function public.handle_user_confirmed_klaviyo();
