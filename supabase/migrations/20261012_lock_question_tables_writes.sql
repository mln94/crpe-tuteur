-- Sécurité : les visiteurs (clé publique) pouvaient modifier ou supprimer les questions.
-- On retire uniquement les droits d'écriture ; la lecture reste ouverte (l'application charge les questions avec la clé publique).
-- Aucune donnée ni colonne n'est supprimée. Le serveur (service role) garde tous ses droits.

revoke insert, update, delete, truncate on public.exercices_maths       from anon, authenticated;
revoke insert, update, delete, truncate on public."exercices_français"  from anon, authenticated;
revoke insert, update, delete, truncate on public.exercices_francais_v  from anon, authenticated;
