-- quiz_comptes.essai_derniere_question_at : date et heure de la dernière question gratuite répondue (essai, compte non payé).
-- Contrairement à essai_jour (remis à jour seulement à la première réponse du jour suivant), elle donne l'heure exacte de la dernière activité d'essai.

alter table public.quiz_comptes
  add column if not exists essai_derniere_question_at timestamptz;

-- Uniquement l'essai à 5 questions par jour : pas de reprise des séries de l'ancien essai (2 séries offertes)
