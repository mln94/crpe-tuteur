-- Test de positionnement réalisé : indicateur explicite, calculé automatiquement à partir du résultat enregistré
alter table public.quiz_comptes
  add column if not exists test_positionnement_realise boolean generated always as (positionnement is not null) stored;
