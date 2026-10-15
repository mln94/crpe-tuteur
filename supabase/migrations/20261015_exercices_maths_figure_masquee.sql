-- Masque les figures qui donnent la réponse (ou n'apportent rien) sans les supprimer : ajout seul.
-- Pour réafficher une figure : passer figure_masquee à false.
alter table public.exercices_maths add column if not exists figure_masquee boolean not null default false;

update public.exercices_maths set figure_masquee = true
where id in (1, 2, 3, 4, 5, 6, 12, 15, 23, 26, 27, 28, 32, 34, 36, 39, 46, 48, 50, 53, 59, 68, 87, 90, 93, 96, 100, 103, 114, 115, 122, 130, 141, 176);
