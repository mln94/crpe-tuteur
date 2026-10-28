-- Essai du Quiz CRPE : 10 questions gratuites par jour au lieu de 5 (ESSAI_PAR_JOUR, app.js).
-- Colonnes renommées sans le nombre de questions : essai_complet_premiere_fois_at (première fois où l'essai du jour a été fait en entier)
-- et essai_nb_jours_complets (nombre de jours). Les jours comptés avec 5 questions ne correspondent plus à un essai complet : remis à zéro.

alter table public.quiz_comptes rename column essai_5_questions_premiere_fois_at to essai_complet_premiere_fois_at;
alter table public.quiz_comptes rename column essai_nb_jours_5_questions to essai_nb_jours_complets;

update public.quiz_comptes set essai_complet_premiere_fois_at = null, essai_nb_jours_complets = 0
 where essai_complet_premiere_fois_at is not null or essai_nb_jours_complets <> 0;
