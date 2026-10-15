-- Lien du rapport visible directement dans la table (colonne calculée à partir du token, rien à remplir à la main).
alter table public.entraineur_rapports
  add column if not exists report_url text
  generated always as ('https://www.passcrpe.fr/outils/entraineur-crpe/rapport/' || token) stored;
