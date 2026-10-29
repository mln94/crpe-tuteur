-- quiz_comptes.essai_fait : true dès la première question gratuite de l'essai (10 questions par jour), false sinon.
-- Mis à true par le serveur (POST /api/quiz/reponse). Klaviyo : propriété essai_fait_quizcrpe.

alter table public.quiz_comptes add column if not exists essai_fait boolean not null default false;

-- Comptes existants : ceux qui ont déjà répondu à une question de l'essai
update public.quiz_comptes set essai_fait = true where essai_jour is not null and not essai_fait;
