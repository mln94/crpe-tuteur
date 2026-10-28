-- quiz_comptes.essai_derniere_question_at : date et heure de la dernière question gratuite répondue (essai, compte non payé).
-- Contrairement à essai_jour (remis à jour seulement à la première réponse du jour suivant), elle donne l'heure exacte de la dernière activité d'essai.

alter table public.quiz_comptes
  add column if not exists essai_derniere_question_at timestamptz;

-- Comptes existants : fin de leur dernière série d'essai enregistrée
update public.quiz_comptes c
   set essai_derniere_question_at = s.derniere
  from (select user_id, max(created_at) as derniere from public.quiz_series where essai group by user_id) s
 where s.user_id = c.user_id and c.essai_derniere_question_at is null;
