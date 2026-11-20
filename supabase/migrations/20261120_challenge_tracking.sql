-- Challenge Copie Parfaite : source de l'inscription (UTM + référent) et première connexion au tableau de bord
alter table public.challenge_inscriptions
  add column if not exists utm_source text,
  add column if not exists utm_medium text,
  add column if not exists utm_campaign text,
  add column if not exists utm_content text,
  add column if not exists utm_term text,
  add column if not exists referrer text,
  add column if not exists premiere_connexion_dashboard_at timestamptz;
