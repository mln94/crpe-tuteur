-- Suivi des publications Meta : groupes où une publication doit être validée par un admin du groupe.
-- validation_requise : le groupe demande une validation (reprise pour les nouvelles campagnes, d'après la dernière campagne).
-- valide_le : date à laquelle la publication a été validée (null = en attente).
alter table public.meta_publications
  add column if not exists validation_requise boolean not null default false,
  add column if not exists valide_le date;
