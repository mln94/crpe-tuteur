-- ================================================================
-- MIGRATION (PARTIE 2/2) : à exécuter APRÈS que les données aient
-- été copiées dans reponses_utilisateurs_francais / _math (copie
-- effectuée hors SQL, via l'API Supabase, en préservant les id
-- d'origine).
--
-- Fait :
-- 1) Repointe les FK de fautes_orthographe / erreurs_syntaxe vers
--    reponses_utilisateurs_francais (recherche dynamique du nom de
--    contrainte réel, pas d'hypothèse sur son nom).
-- 2) Recale les séquences d'auto-incrément des 2 nouvelles tables
--    pour continuer après les id copiés (évite les collisions).
-- 3) Archive l'ancienne table reponses_utilisateurs (renommée, PAS
--    supprimée) au lieu de la droper, par sécurité.
-- ================================================================

BEGIN;

DO $$
DECLARE
  cname text;
BEGIN
  SELECT tc.constraint_name INTO cname
  FROM information_schema.table_constraints tc
  JOIN information_schema.key_column_usage kcu
    ON tc.constraint_name = kcu.constraint_name
  WHERE tc.table_name = 'fautes_orthographe'
    AND tc.constraint_type = 'FOREIGN KEY'
    AND kcu.column_name = 'id_reponse_utilisateur';
  IF cname IS NOT NULL THEN
    EXECUTE format('ALTER TABLE fautes_orthographe DROP CONSTRAINT %I', cname);
  END IF;
  ALTER TABLE fautes_orthographe
    ADD CONSTRAINT fautes_orthographe_id_reponse_utilisateur_fkey
    FOREIGN KEY (id_reponse_utilisateur) REFERENCES reponses_utilisateurs_francais(id);
END $$;

DO $$
DECLARE
  cname text;
BEGIN
  SELECT tc.constraint_name INTO cname
  FROM information_schema.table_constraints tc
  JOIN information_schema.key_column_usage kcu
    ON tc.constraint_name = kcu.constraint_name
  WHERE tc.table_name = 'erreurs_syntaxe'
    AND tc.constraint_type = 'FOREIGN KEY'
    AND kcu.column_name = 'id_reponse_utilisateur';
  IF cname IS NOT NULL THEN
    EXECUTE format('ALTER TABLE erreurs_syntaxe DROP CONSTRAINT %I', cname);
  END IF;
  ALTER TABLE erreurs_syntaxe
    ADD CONSTRAINT erreurs_syntaxe_id_reponse_utilisateur_fkey
    FOREIGN KEY (id_reponse_utilisateur) REFERENCES reponses_utilisateurs_francais(id);
END $$;

-- Recaler les séquences après la copie de données (évite toute
-- collision d'id lors des prochains inserts faits par l'appli)
SELECT setval(
  pg_get_serial_sequence('reponses_utilisateurs_francais', 'id'),
  COALESCE((SELECT MAX(id) FROM reponses_utilisateurs_francais), 1),
  true
);
SELECT setval(
  pg_get_serial_sequence('reponses_utilisateurs_math', 'id'),
  COALESCE((SELECT MAX(id) FROM reponses_utilisateurs_math), 1),
  true
);

-- Archiver l'ancienne table (au lieu de la supprimer) par sécurité
ALTER TABLE reponses_utilisateurs RENAME TO reponses_utilisateurs_legacy;

COMMIT;
