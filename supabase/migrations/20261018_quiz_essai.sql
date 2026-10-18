-- Essai gratuit après le test de positionnement : questions déjà posées dans les 2 matières offertes
-- ({ "physique_chimie": [ids…], "arts": [ids…] }) ; les matières offertes se déduisent du résultat du test.
alter table public.quiz_comptes add column if not exists essai_reponses jsonb not null default '{}'::jsonb;
