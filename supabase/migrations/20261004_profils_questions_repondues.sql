-- Nombre de questions répondues par matière, thématique et classe, stocké dans
-- profils_utilisateurs.questions_repondues :
--   { "maths":    { "Nombres et calculs": { "5e": 5, "3e": 1 } },
--     "francais": { "Lecture": { "5e": 3 } } }
-- Seule la 1re tentative d'une question est comptée. Le compteur est tenu à
-- jour par un trigger sur les tables de réponses (le client n'a qu'un accès en
-- lecture à son profil).

ALTER TABLE profils_utilisateurs
  ADD COLUMN IF NOT EXISTS questions_repondues jsonb NOT NULL DEFAULT '{}'::jsonb;

CREATE OR REPLACE FUNCTION increment_questions_repondues()
RETURNS trigger
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
  matiere text := TG_ARGV[0];
  them    text := COALESCE(NULLIF(NEW.thematique, ''), 'Autre');
  cls     text := COALESCE(NULLIF(NEW.classe, ''), 'Autre');
BEGIN
  IF COALESCE(NEW.tentative, 1) <> 1 OR NEW.user_id IS NULL THEN
    RETURN NEW;
  END IF;

  UPDATE profils_utilisateurs p
  SET questions_repondues = jsonb_set(
        jsonb_set(
          jsonb_set(
            p.questions_repondues,
            ARRAY[matiere],
            COALESCE(p.questions_repondues -> matiere, '{}'::jsonb)
          ),
          ARRAY[matiere, them],
          COALESCE(p.questions_repondues -> matiere -> them, '{}'::jsonb)
        ),
        ARRAY[matiere, them, cls],
        to_jsonb(COALESCE((p.questions_repondues -> matiere -> them ->> cls)::int, 0) + 1)
      )
  WHERE p.user_id::text = NEW.user_id;

  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_questions_repondues_math ON reponses_utilisateurs_math;
CREATE TRIGGER trg_questions_repondues_math
  AFTER INSERT ON reponses_utilisateurs_math
  FOR EACH ROW EXECUTE FUNCTION increment_questions_repondues('maths');

DROP TRIGGER IF EXISTS trg_questions_repondues_francais ON reponses_utilisateurs_francais;
CREATE TRIGGER trg_questions_repondues_francais
  AFTER INSERT ON reponses_utilisateurs_francais
  FOR EACH ROW EXECUTE FUNCTION increment_questions_repondues('francais');

-- Remplissage à partir des réponses déjà enregistrées
WITH counts AS (
  SELECT user_id, 'maths' AS matiere,
         COALESCE(NULLIF(thematique, ''), 'Autre') AS them,
         COALESCE(NULLIF(classe, ''), 'Autre') AS cls, count(*) AS n
  FROM reponses_utilisateurs_math WHERE COALESCE(tentative, 1) = 1
  GROUP BY 1, 2, 3, 4
  UNION ALL
  SELECT user_id, 'francais',
         COALESCE(NULLIF(thematique, ''), 'Autre'),
         COALESCE(NULLIF(classe, ''), 'Autre'), count(*)
  FROM reponses_utilisateurs_francais WHERE COALESCE(tentative, 1) = 1
  GROUP BY 1, 2, 3, 4
),
by_them AS (
  SELECT user_id, matiere, them, jsonb_object_agg(cls, n) AS j
  FROM counts GROUP BY 1, 2, 3
),
by_matiere AS (
  SELECT user_id, matiere, jsonb_object_agg(them, j) AS j
  FROM by_them GROUP BY 1, 2
),
by_user AS (
  SELECT user_id, jsonb_object_agg(matiere, j) AS j
  FROM by_matiere GROUP BY 1
)
UPDATE profils_utilisateurs p
SET questions_repondues = b.j
FROM by_user b
WHERE p.user_id::text = b.user_id;
