-- Suivi des publications Meta : groupe bloqué (publication refusée, exclusion, liens interdits…).
-- bloque_le : date à laquelle le groupe a été marqué bloqué (null = non bloqué). Reprise pour les nouvelles campagnes.
alter table public.meta_publications add column if not exists bloque_le date;
