-- consommation_utilisateurs.erreur : message renvoyé par l'API Anthropic quand un appel échoue (success = false)
alter table public.consommation_utilisateurs add column if not exists erreur text;
