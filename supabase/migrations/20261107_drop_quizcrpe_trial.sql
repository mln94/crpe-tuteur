-- profils_utilisateurs.quizcrpe_trial : colonne inutilisée (jamais lue par le code, ni par une fonction ou une vue).
-- L'état de l'essai du quiz est donné par quiz_comptes.essai_fait (Klaviyo : essai_fait_quizcrpe)
-- et le test par test_positionnement_realise. La propriété Klaviyo quizcrpe_trial n'est plus envoyée (app.js).
alter table public.profils_utilisateurs drop column if exists quizcrpe_trial;
