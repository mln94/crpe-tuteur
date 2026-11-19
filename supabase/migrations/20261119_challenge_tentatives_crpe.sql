-- Challenge : « Combien de fois avez-vous déjà passé le CRPE ? » (0 = première fois, 3 = 3 fois ou plus)
alter table public.challenge_inscriptions
  add column if not exists tentatives_crpe smallint check (tentatives_crpe between 0 and 3);
