-- ============================================================
-- Vue organisée des compétences français cycle 4
-- Ordre : sous_catégorie ASC → 5e → 4e → 3e → ordre ASC
-- Inclut l'ID ET le nom de la sous-catégorie
-- ============================================================

CREATE OR REPLACE VIEW vue_competences_francais_cycle4 AS
SELECT
  c.id,
  sc.id                       AS sous_categorie_id,
  sc.nom                      AS sous_categorie_nom,
  sc.groupe                   AS sous_categorie_groupe,
  sc.thematique_id,
  c.classe,
  CASE c.classe
    WHEN '5e' THEN 1
    WHEN '4e' THEN 2
    WHEN '3e' THEN 3
  END                         AS classe_ordre,
  c.ordre,
  c.objectif
FROM "competences_français_cycle4" c
JOIN sous_categories_francais_cycle4 sc ON c.sous_categorie_id = sc.id
ORDER BY
  sc.thematique_id  ASC,
  sc.ordre          ASC,
  CASE c.classe
    WHEN '5e' THEN 1
    WHEN '4e' THEN 2
    WHEN '3e' THEN 3
  END               ASC,
  c.ordre           ASC;


-- ============================================================
-- (Optionnel) Requête de vérification par thématique complète
-- Exemple : afficher toutes les compétences de la thématique 1
-- (Lecture) organisées 5e → 4e → 3e
-- ============================================================

/*
SELECT
  sous_categorie_id,
  sous_categorie_nom,
  classe,
  ordre,
  objectif
FROM vue_competences_francais_cycle4
WHERE thematique_id = 1
ORDER BY
  sous_categorie_id,
  classe_ordre,
  ordre;
*/
