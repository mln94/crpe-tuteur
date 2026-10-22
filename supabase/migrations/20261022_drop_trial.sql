-- L'ancienne colonne « trial » est remplacée par passcrpe_trial : suppression du déclencheur de copie puis de la colonne.
drop trigger if exists copie_trial on public.profils_utilisateurs;
drop function if exists public.copie_trial_vers_passcrpe_trial();
alter table public.profils_utilisateurs drop column if exists trial;
