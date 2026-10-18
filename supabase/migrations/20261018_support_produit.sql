-- Demandes de support : outil concerné (tuteur IA ou Quiz CRPE), affiché dans /admin-support
alter table public.support_tickets add column if not exists produit text check (produit in ('tuteur', 'quiz'));
