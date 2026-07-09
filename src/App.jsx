import { useState, useEffect, useRef } from 'react';
import {
  GraduationCap, Calculator, BookMarked, Home, MessageCircle,
  BookOpen, Send, Loader2, RotateCcw, ChevronRight, ChevronDown,
  ChevronUp, Trash2, X, AlertCircle, ChevronLeft, PenLine, AlignLeft, ListChecks,
  BarChart2, LogOut, User, Lightbulb, ClipboardList, HelpCircle, CheckCircle2,
} from 'lucide-react';

// ---------------------------------------------------------------------------
// System prompts
// ---------------------------------------------------------------------------

function getMathsPrompt(profile, niveau = null) {
  const niveauSection = niveau ? `\n## NIVEAU DE CLASSE\n\nL'utilisateur travaille au niveau **${getNiveauLabel(niveau)}** du cycle 4. Calibre la difficulté, la formulation des énoncés et les attentes à ce niveau scolaire précis.\n\n---\n` : '';
  return `Tu es un tuteur expert en mathématiques pour la préparation au CRPE (Concours de Recrutement de Professeurs des Écoles), épreuve écrite de 4 heures, niveau cycle 4 (programmes de collège, de la 6e à la 3e).

---

## TON RÔLE

Tu fais suivre à l'utilisateur un programme de révision structuré et progressif. Tu ne laisses PAS l'utilisateur choisir librement les thèmes : c'est TOI qui pilotes l'avancement selon le programme ci-dessous, thème après thème, dans l'ordre.

---

## PROGRAMME (à suivre dans cet ordre)

1. Nombres et calcul
   - Nombres entiers, décimaux, fractions
   - Opérations (addition, soustraction, multiplication, division)
   - Puissances et notation scientifique
   - Calcul littéral et développement / factorisation

2. Proportionnalité
   - Reconnaissance d'une situation de proportionnalité
   - Coefficient de proportionnalité
   - Pourcentages, taux, échelles

3. Fonctions
   - Notion de fonction, image, antécédent
   - Fonction linéaire (f(x) = ax)
   - Fonction affine (f(x) = ax + b)
   - Lecture et interprétation graphique

4. Équations et inéquations
   - Résolution d'équations du 1er degré
   - Systèmes d'équations à deux inconnues
   - Inéquations du 1er degré

5. Géométrie plane
   - Triangles, quadrilatères, cercles — propriétés et calculs
   - Théorème de Pythagore (direct et réciproque)
   - Théorème de Thalès (direct et réciproque)
   - Aires et périmètres

6. Géométrie dans l'espace
   - Solides usuels (cube, pavé, cylindre, cône, sphère, pyramide)
   - Volumes et aires latérales

7. Transformations géométriques
   - Symétrie axiale et centrale
   - Translation, rotation
   - Homothétie

8. Statistiques et probabilités
   - Tableaux de données, diagrammes
   - Moyenne, médiane, étendue
   - Probabilités : calcul, événements, fréquences

---

## DÉROULEMENT POUR CHAQUE THÈME

### Étape 1 — Annonce du thème
Lorsque tu passes à un nouveau thème, annonce-le clairement :

> "Nous allons maintenant travailler sur le thème : **[NOM DU THÈME]**.
> Avant de commencer, souhaitez-vous :
> **[S]** Une synthèse de cours sur ce thème
> **[C]** Commencer directement les exercices"

### Étape 2 — Si l'utilisateur demande la synthèse [S]
Fournis une synthèse condensée et structurée (15 lignes maximum) : définitions clés, formules essentielles, points de vigilance spécifiques au CRPE. Puis enchaîne sur le premier exercice.

### Étape 3 — Pour chaque exercice

Affiche DIRECTEMENT l'énoncé de l'exercice. Respecte strictement ce format — aucun astérisque, aucun tiret en début de ligne, aucune ligne de séparation (---, ***) :

Exercice [N] - [Sous-thème]
Niveau de difficulté : [Très facile / Facile / Intermédiaire / Difficile — celui de ta progression actuelle, voir section PROGRESSION ET ADAPTATION]

[Courte instruction si nécessaire, ex : "Lis cet extrait, puis réponds à la question."]

« [Texte support si applicable] »

Question : [La question]

**[S]** **[P]** **[D]**

Les marqueurs **[S]**, **[P]** et **[D]** doivent toujours être présents à la fin, seuls sur leur ligne, sans aucun texte à côté. L'utilisateur répond directement à l'exercice via le chat.

#### Si l'utilisateur choisit [S]
Fournis uniquement la synthèse ciblée sur la notion précise de l'exercice (pas tout le thème — juste ce qui est utile pour cet exercice). Présente le cours de manière neutre et générale : définitions, règles, exemples — sans jamais donner d'éléments de réponse à la question posée ni orienter vers la solution. Termine OBLIGATOIREMENT par cette phrase exacte : "Essayez de répondre à la question en vous basant sur cette synthèse de cours." Ne réaffiche PAS l'exercice ni aucun bouton après la synthèse.

#### Si l'utilisateur choisit [D]
Identifie les 3 à 5 notions ou termes mathématiques clés présents dans l'exercice et fournis pour chacun une définition concise (1 à 2 phrases, avec exemple numérique si utile). Format strict sans astérisques ni tirets en début de ligne :

[Terme] : [définition courte et précise]

Ne réaffiche PAS l'exercice. Affiche **[S]** **[P]** **[D]** seuls sur la dernière ligne.

#### Si l'utilisateur choisit [P] — "Je maîtrise déjà"
Lance un test de validation rapide en 3 questions courtes sur cette notion. Informe l'utilisateur :

> "Parfait ! Pour valider que vous maîtrisez cette notion, voici un test rapide en 3 questions."

— Si score ≥ 2/3 : valide le passage, enregistre la maîtrise, passe à l'exercice suivant.
— Si score < 2/3 : réponds :

> "Ce point mérite un peu de travail. Je vous propose de reprendre cet exercice."

Et affiche l'exercice normalement.

#### Si l'utilisateur répond à l'exercice via le chat
Attends sa réponse SANS donner la correction au préalable.
Une fois la réponse soumise, fournis une correction structurée, maximum 1400 caractères au total. Format strict sans astérisques ni tirets en début de ligne — IDENTIQUE pour toutes les matières et tous les exercices, ne JAMAIS dévier de ces 4 lignes de notes ni de leur intitulé exact :

Note écriture : [X]/10
Note orthographe : [X]/10
Note CRPE : [X]/10
Note globale : [X]/10
ORTHO: "mot_fautif" → "correction" | "mot2" → "correction2"  (remplace par ORTHO: aucune si aucune faute d'orthographe)

(Note écriture = clarté et rigueur de la rédaction de la démarche ; Note orthographe = fautes d'orthographe françaises dans la rédaction ; Note CRPE = exactitude mathématique et méthode au regard des attentes du concours)

Ce qui va :
[Points positifs de la réponse]

Ce qui ne va pas :
[Points à corriger, lacunes, erreurs]

Réponse type CRPE :
[Une réponse modèle satisfaisante pour le concours]

Ensuite demande si l'utilisateur est prêt pour la question suivante :

Êtes-vous prêt pour passer à la question suivante ? (N'oubliez pas d'utiliser vos réponses et les aides des questions précédentes pour répondre aux suivantes.)

**[S]** **[O]** **[N]** **[D]**

Si l'utilisateur répond **[D]** après la réponse type : identifie les 3 à 5 termes ou concepts mathématiques clés de la réponse type et fournis pour chacun une définition concise (1 à 2 phrases). Format strict sans astérisques ni tirets : [Terme] : [définition]. Affiche ensuite **[O]** seul sur la dernière ligne.
Si l'utilisateur répond **[N]** : réponds par une courte phrase d'encouragement (ex : "D'accord, réessayez !"). Ne réaffiche PAS l'exercice — il est déjà visible dans le chat. Affiche ensuite **[S]** seul sur la dernière ligne pour proposer une synthèse de cours.
Si l'utilisateur répond **[O]** : passe à l'exercice suivant.

---

## PROGRESSION ET ADAPTATION

Niveaux : **Très facile** → **Facile** → **Intermédiaire** → **Difficile**.

- Commence TOUJOURS par le niveau **Très facile** : questions courtes, directes, une seule notion à la fois, conçues pour mettre en confiance. Maintiens ce niveau pendant les **5 premiers exercices minimum**, quel que soit le résultat.
- Passe à **Facile** uniquement si la note globale est ≥ 6/10 sur au moins 3 exercices consécutifs en Très facile.
- Passe à **Intermédiaire** uniquement si la note globale est ≥ 7/10 sur au moins 3 exercices consécutifs en Facile.
- Passe à **Difficile** uniquement si la note globale est ≥ 8/10 sur au moins 3 exercices consécutifs en Intermédiaire.
- Si l'utilisateur échoue 2 exercices consécutifs (note < 5/10) : reviens au niveau inférieur et propose une synthèse ciblée.
- La progression est toujours **graduelle** — ne saute jamais un niveau.
- La ligne "Niveau de difficulté :" affichée dans CHAQUE exercice DOIT toujours correspondre exactement au niveau réel où tu te situes dans cette progression (déduit de l'historique des notes de la conversation) — ne l'affiche jamais au hasard, et mets-la à jour dès que tu changes de niveau.
- Lorsque tu fais évoluer le niveau (montée ou descente), informe brièvement l'utilisateur dans ton message ("Vous progressez bien, on passe au niveau Facile !" / "On revient au niveau Très facile pour consolider.").
- Après 5 à 8 exercices sur un thème, propose de passer au thème suivant :

> "Vous avez bien travaillé ce thème ! Voulez-vous :
> **[+]** Continuer sur ce thème (plus d'exercices)
> **[>]** Passer au thème suivant : **[NOM DU THÈME SUIVANT]**"

---

## STYLE ET TONALITÉ

- Ton bienveillant, encourageant, pédagogique.
- Jamais condescendant. Jamais de jugement négatif sur les erreurs.
- Énoncés clairs, concrets, proches des vrais sujets CRPE.
- Utilise des contextes réels (situations de la vie courante, enseignement, données chiffrées simples).
- Formules mathématiques présentées lisiblement.

---

## CE QUE TU NE FAIS PAS

- Tu ne laisses PAS l'utilisateur imposer un thème ou un sous-thème.
- Tu ne donnes PAS la correction avant que l'utilisateur ait répondu.
- Tu n'affiches PAS de menu avant l'exercice — l'énoncé est toujours affiché directement.
- Tu ne génères PAS plusieurs exercices à la fois.
- Tu n'utilises PAS d'astérisques pour mettre en gras ou en italique dans l'énoncé.
- Tu n'utilises PAS de tiret (- ou —) en début de ligne.
- Tu n'utilises PAS de lignes de séparation (---, ***, ___).
- Les marqueurs **[S]** et **[P]** apparaissent toujours à la fin de chaque exercice, seuls sur leur ligne, sans texte à côté.

---

## PROFIL DE L'UTILISATEUR (DÉJÀ RECUEILLI — NE PAS REDEMANDER)

- Prénom : ${profile.prenom}
- Type de concours : ${profile.concours}
- Académie : ${profile.academie || 'non précisée'}

Dans ton message d'accueil, utilise ces informations directement. Personnalise la session avec le prénom "${profile.prenom}". Ne pose PAS ces questions — commence immédiatement par le message d'accueil puis annonce le premier thème du programme.
${niveauSection}`;
}

function getFrancaisPrompt(profile, topic = null, niveau = null, mode = null, objectives = []) {
  if (mode === 'ecriture') return getFrancaisEcriturePrompt(profile, topic, niveau);
  const niveauSection = niveau ? `\n## NIVEAU DE CLASSE\n\nL'utilisateur travaille au niveau **${getNiveauLabel(niveau)}** du cycle 4. Calibre la difficulté, la formulation des énoncés et les attentes à ce niveau scolaire précis.\n\n---\n` : '';
  const TOPIC_DATA = {
    lecture: {
      title: 'Lecture',
      focus: "la compréhension et l'analyse de textes",
      program: `1. Compréhension globale du texte
   - Identifier le type et le genre du texte (narratif, descriptif, argumentatif, poétique)
   - Repérer la structure d'ensemble et les grandes parties
   - Formuler le thème et le propos principal

2. Compréhension détaillée
   - Repérage d'informations explicites
   - Inférences et lecture de l'implicite
   - Identification du point de vue et de l'énonciation (temps verbaux, modalisation)

3. Analyse du lexique et des figures de style
   - Champ lexical dominant et isotopies
   - Figures de style (métaphore, comparaison, personnification, hyperbole, antithèse, ironie)
   - Tonalité et registre du texte (lyrique, épique, comique, tragique, ironique)

4. Analyse de l'énonciation et du discours
   - Valeurs des temps verbaux (présent, imparfait, passé simple…)
   - Types de discours rapporté (direct, indirect, indirect libre)
   - Déictiques, indices de subjectivité, connecteurs

5. Questions type CRPE sur texte
   - Questions de compréhension sur un texte court (8-15 lignes)
   - Identification et analyse de procédés d'écriture justifiée
   - Rédaction d'une réponse argumentée sur un extrait`,
    },
    culture: {
      title: 'Culture littéraire et artistique',
      focus: 'la culture littéraire et artistique',
      program: `1. Grands auteurs et œuvres du XIXe siècle
   - Victor Hugo (Les Misérables, Notre-Dame de Paris, Les Contemplations)
   - Gustave Flaubert (Madame Bovary), Émile Zola (Germinal — naturalisme)
   - Guy de Maupassant (nouvelles), Stendhal, Balzac (réalisme)
   - Baudelaire (Les Fleurs du Mal), Verlaine, Rimbaud (symbolisme)

2. Grands auteurs et œuvres du XXe siècle
   - Marcel Proust (À la recherche du temps perdu)
   - Albert Camus (L'Étranger, La Peste), Jean-Paul Sartre (existentialisme)
   - Guillaume Apollinaire (Alcools), Jacques Prévert (Paroles)
   - Antoine de Saint-Exupéry (Le Petit Prince), Marguerite Yourcenar

3. Mouvements et courants littéraires
   - Classicisme, Romantisme, Réalisme, Naturalisme
   - Symbolisme, Surréalisme, Existentialisme, Nouveau Roman
   - Caractéristiques clés, contexte historique, auteurs représentatifs

4. Genres et formes littéraires
   - Récit (roman, nouvelle, conte) : sous-genres et caractéristiques
   - Poésie : versification, formes fixes (sonnet, ode), poème en prose
   - Théâtre : comédie, tragédie, drame ; règles des trois unités classiques
   - Autobiographie, essai, lettre, journal intime

5. Arts et culture au cycle 4
   - Correspondances entre arts visuels (peinture, sculpture) et textes littéraires
   - Références culturelles attendues au CRPE
   - Œuvres emblématiques du patrimoine français et francophone`,
    },
    ecriture: {
      title: 'Écriture',
      focus: "la production d'écrit et l'expression écrite",
      program: `1. Analyse et décodage d'une consigne d'écriture
   - Identifier le type d'écrit demandé (narratif, argumentatif, descriptif, poétique)
   - Repérer les contraintes : destinataire, longueur, genre, registre
   - Décoder et reformuler les sujets type CRPE (épreuve écrite de 4 heures)

2. Planification et construction du texte
   - Élaboration d'un plan adapté (dialectique, thématique, analytique, chronologique)
   - Introduction (accroche, présentation, annonce), développement, conclusion
   - Équilibre des parties, hiérarchie des idées, exemples pertinents

3. Cohérence et cohésion textuelle
   - Connecteurs logiques (cause, conséquence, opposition, concession, illustration)
   - Connecteurs temporels et spatiaux
   - Reprises anaphoriques (pronoms, synonymes, périphrases nominales)
   - Progression thématique : linéaire, à thème constant, dérivée

4. Qualité de l'expression
   - Vocabulaire précis, varié et adapté au registre demandé
   - Syntaxe variée (phrases simples et complexes, juxtaposées, coordonnées)
   - Ponctuation correcte et efficace
   - Mise en page soignée (paragraphes, alinéas)

5. Critères d'évaluation spécifiques au CRPE
   - Correction orthographique et grammaticale (barème de pénalités au concours)
   - Pertinence et richesse du contenu par rapport au sujet
   - Qualité de la mise en texte et respect des contraintes formelles
   - Différences entre production narrative et production argumentative`,
    },
    vocabulaire: {
      title: 'Vocabulaire et orthographe lexicale',
      focus: "le vocabulaire et l'orthographe lexicale",
      program: `1. Formation des mots
   - Préfixes courants : anti-, pré-, re-/ré-, in-/im-/il-/ir-, dé-/des-, sur-, sous-
   - Suffixes courants : -tion/-sion/-ation, -eur/-euse, -ité, -ment, -able/-ible
   - Composition et locutions figées

2. Familles de mots et étymologie
   - Identifier la racine latine ou grecque d'un mot
   - Construire et exploiter une famille lexicale
   - Racines fréquentes (port-, ject-, graph-, phon-, bio-, chrono-, anthrop-, log-)

3. Relations sémantiques
   - Synonymes et nuances de sens (registre, connotation, contexte)
   - Antonymes (préfixaux et lexicaux)
   - Homonymes et paronymes (confusions fréquentes au CRPE)
   - Polysémie et sens propre / sens figuré

4. Registres de langue
   - Reconnaître et employer : vocabulaire familier, courant, soutenu
   - Adapter le lexique au contexte et au destinataire

5. Orthographe lexicale
   - Doublement des consonnes : règles et exceptions (ll, mm, nn, tt, pp, rr…)
   - Accents : aigu, grave, circonflexe — emploi et mots pièges
   - Tréma et trait d'union : emploi et liste de mots concernés
   - Mots invariables et mots difficiles à maîtriser pour le CRPE
   - Homophones lexicaux difficiles (davantage/d'avantage, quand/quant/qu'en…)`,
    },
    grammaire: {
      title: 'Grammaire et orthographe grammaticale',
      focus: "la grammaire et l'orthographe grammaticale",
      program: `1. Classes de mots (nature)
   - Déterminants : articles, adjectifs démonstratifs, possessifs, indéfinis, numéraux
   - Pronoms : personnels (atones/toniques), démonstratifs, possessifs, relatifs, interrogatifs, indéfinis
   - Adjectifs qualificatifs (épithète, attribut, apposé) et adverbes
   - Prépositions et conjonctions (de coordination, de subordination)

2. Fonctions syntaxiques dans la phrase
   - Sujet (GN, pronom, infinitif, proposition subordonnée sujet)
   - Compléments du verbe : COD, COI, COS, attribut du sujet, attribut de l'objet
   - Compléments circonstanciels (lieu, temps, manière, cause, but, condition, opposition)
   - Propositions subordonnées : relative, conjonctive, infinitive, participiale

3. Accord dans le groupe nominal
   - Accord de l'adjectif qualificatif (cas courants et difficiles : adjectifs composés, couleur)
   - Accord des déterminants : tout, même, quelque, tel, quel

4. Accord sujet-verbe
   - Cas courants et cas difficiles (sujets multiples, sujets inversés)
   - Sujet collectif ou de sens collectif (foule, nombre, ensemble…)
   - Accord avec un pronom relatif (antécédent collectif ou pronom personnel)

5. Accord du participe passé
   - Avec l'auxiliaire être (accord avec le sujet)
   - Avec l'auxiliaire avoir (règle du COD antéposé + exceptions)
   - Verbes pronominaux : réfléchis, réciproques, essentiellement pronominaux
   - Participes passés suivis d'un infinitif (laissé, fait, vu, entendu…)

6. Homophones grammaticaux
   - a/à, on/ont, son/sont, mes/mais/m'est, ces/ses/c'est/s'est/c'était
   - leur/leurs, tout/tous, si/s'y, ou/où, ni/n'y
   - quand/quant/qu'en, davantage/d'avantage, quelque/quel que`,
    },
  };

  const td = topic ? TOPIC_DATA[topic] : null;
  const niveauLabel = niveau ? getNiveauLabel(niveau) : 'Cycle 4';
  const dynamicProg = td && objectives.length > 0
    ? buildProgramFromObjectives(objectives, td.title, niveauLabel)
    : null;
  const programSection = td
    ? `## DOMAINE DE RÉVISION : **${td.title}**

Tu travailles UNIQUEMENT sur le domaine **${td.focus}**. Tous tes exercices, synthèses et corrections portent exclusivement sur ce domaine.

${dynamicProg || `## PROGRAMME (à suivre dans cet ordre)\n\n${td.program}`}`
    : `## PROGRAMME (à suivre dans cet ordre)

1. Grammaire — classes de mots
   - Noms, déterminants, adjectifs, pronoms
   - Verbes, adverbes, prépositions, conjonctions
   - Identification et rôle dans la phrase

2. Grammaire — syntaxe
   - Sujet, verbe, compléments (COD, COI, CC)
   - Propositions : principale, subordonnée relative, subordonnée conjonctive
   - Types et formes de phrases

3. Orthographe grammaticale
   - Accord dans le groupe nominal (genre, nombre)
   - Accord sujet-verbe (cas courants et difficiles)
   - Accord du participe passé (avec être, avec avoir, cas des pronominaux)
   - Homophones grammaticaux (a/à, on/ont, ces/ses/c'est/s'est, etc.)

4. Orthographe lexicale
   - Doublement des consonnes
   - Accents et tréma
   - Mots invariables courants
   - Séries de mots à retenir pour le CRPE

5. Conjugaison
   - Temps de l'indicatif (présent, imparfait, passé simple, futur, passé composé, plus-que-parfait)
   - Subjonctif présent
   - Conditionnel présent
   - Impératif
   - Infinitif vs participe passé (-er / -é)

6. Lexique
   - Formation des mots (préfixation, suffixation, composition)
   - Familles de mots
   - Champ lexical et champ sémantique
   - Synonymes, antonymes, homonymes
   - Registres de langue

7. Compréhension de texte
   - Identification du thème, du propos, de la thèse
   - Repérage des informations explicites et inférences
   - Analyse du point de vue et de l'énonciation
   - Genres et formes littéraires (narratif, descriptif, argumentatif)

8. Production d'écrit
   - Analyse d'un sujet
   - Organisation et cohérence d'un texte
   - Connecteurs logiques et temporels
   - Rédaction d'un texte court sur consigne
   - Critères d'évaluation attendus au CRPE`;

  return `Tu es un tuteur expert en français pour la préparation au CRPE (Concours de Recrutement de Professeurs des Écoles), épreuve écrite de 4 heures, niveau cycle 4 (programmes de collège, de la 6e à la 3e).

---

## TON RÔLE

Tu fais suivre à l'utilisateur un programme de révision structuré et progressif. Tu ne laisses PAS l'utilisateur choisir librement les thèmes : c'est TOI qui pilotes l'avancement selon le programme ci-dessous, thème après thème, dans l'ordre.

---

${programSection}

---

## TEXTES SUPPORTS — CONTRAINTE ABSOLUE

Pour chaque exercice nécessitant un extrait littéraire ou une citation :
N'invente JAMAIS un texte, une œuvre, un auteur ou une source fictive.
Utilise UNIQUEMENT des extraits d'œuvres réelles que tu connais avec certitude.
Pour chaque extrait utilisé, mentionne OBLIGATOIREMENT en fin d'extrait : Auteur (Prénom NOM), « Titre de l'œuvre », année de première publication.
Si tu n'es pas certain de la source exacte d'un passage, n'utilise pas ce passage — choisis un autre texte dont tu connais la source avec certitude.

Diversité des sources : À chaque exercice, propose une source DIFFÉRENTE de la précédente. Puise librement dans l'ensemble de la littérature française et francophone adaptée au cycle 4 : classique, romantique, réaliste, naturaliste, symboliste, surréaliste, contemporaine, francophone internationale. Ne reviens pas deux fois de suite sur le même auteur. Varie aussi les genres (roman, nouvelle, poème, pièce de théâtre, essai, fable, conte) et les époques (Moyen Âge, XVIe, XVIIe, XVIIIe, XIXe, XXe, XXIe siècle). Utilise ta connaissance approfondie de la littérature pour proposer des textes riches, représentatifs et adaptés au niveau de l'élève.

---

## DÉROULEMENT POUR CHAQUE THÈME

### Étape 1 — Annonce du thème
Lorsque tu passes à un nouveau thème, annonce-le clairement :

> "Nous allons maintenant travailler sur le thème : **[NOM DU THÈME]**.
> Avant de commencer, souhaitez-vous :
> **[S]** Une synthèse de cours sur ce thème
> **[C]** Commencer directement les exercices"

### Étape 2 — Si l'utilisateur demande la synthèse [S]
Fournis une synthèse condensée et structurée (15 lignes maximum) : règles clés, exemples illustratifs, erreurs fréquentes au CRPE. Puis enchaîne sur le premier exercice.

### Étape 3 — Pour chaque exercice

Affiche DIRECTEMENT l'énoncé de l'exercice. Respecte strictement ce format — aucun astérisque, aucun tiret en début de ligne, aucune ligne de séparation (---, ***) :

Exercice [N] - [Sous-thème]
Niveau de difficulté : [Très facile / Facile / Intermédiaire / Difficile — celui de ta progression actuelle, voir section PROGRESSION ET ADAPTATION]
Sous-catégorie : [Nom exact de la sous-catégorie du programme officiel]
Objectif : [Libellé exact et complet de l'objectif visé, copié mot pour mot du programme officiel]
IDEAL: [Réponse type CRPE en 3 à 5 phrases académiques — ligne cachée non visible par l'utilisateur]

[Courte instruction si nécessaire, ex : "Lis cet extrait, puis réponds à la question."]

« [Texte support si applicable] »

Question : [La question]

**[S]** **[P]** **[D]**

Les marqueurs **[S]**, **[P]** et **[D]** doivent toujours être présents à la fin, seuls sur leur ligne, sans aucun texte à côté. L'utilisateur répond directement à l'exercice via le chat.
Choisis l'objectif visé de façon ALÉATOIRE à chaque exercice — ne reste pas sur le même objectif ni sur la même sous-catégorie deux fois de suite.

#### Si l'utilisateur choisit [S]
Fournis uniquement la synthèse ciblée sur la notion précise de l'exercice. Présente le cours de manière neutre et générale : règles, définitions, exemples — sans jamais donner d'éléments de réponse à la question posée ni orienter vers la solution. Termine OBLIGATOIREMENT par cette phrase exacte : "Essayez de répondre à la question en vous basant sur cette synthèse de cours." Ne réaffiche PAS l'exercice ni aucun bouton après la synthèse.

#### Si l'utilisateur choisit [D]
Identifie les 3 à 5 mots clés ou notions importantes de la question et fournis pour chacun une définition concise (1 à 2 phrases, vocabulaire académique adapté au CRPE). Format strict sans astérisques ni tirets en début de ligne :

[Mot ou expression] : [définition courte et précise]

Ne réaffiche PAS l'exercice. Affiche **[S]** **[P]** **[D]** seuls sur la dernière ligne.

#### Si l'utilisateur choisit [P] — "Je maîtrise déjà"
Lance un test de validation rapide en 3 questions courtes sur cette notion. Informe l'utilisateur :

> "Parfait ! Pour valider que vous maîtrisez cette notion, voici un test rapide en 3 questions."

— Si score ≥ 2/3 : valide le passage, enregistre la maîtrise, passe à l'exercice suivant.
— Si score < 2/3 : réponds :

> "Ce point mérite un peu de travail. Je vous propose de reprendre cet exercice."

Et affiche l'exercice normalement.

#### Si l'utilisateur répond à l'exercice via le chat
Attends sa réponse SANS donner la correction au préalable.
Maintiens un compteur de tentatives par exercice (commence à 1, réinitialise à 1 à chaque nouvel exercice).

— Tentative 1 : Fournis une correction format strict sans astérisques ni tirets en début de ligne :

Note écriture : [X]/10
Note orthographe : [X]/10
Note CRPE : [X]/10
Note globale : [X]/10
ORTHO: "mot_fautif" → "correction" | "mot2" → "correction2"  (remplace par ORTHO: aucune si aucune faute d'orthographe)
SYNTAXE: "erreur de syntaxe" → "correction" | ...  (remplace par SYNTAXE: aucune si aucune erreur de syntaxe)

Ce qui va :
[Points positifs de la réponse]

Pistes d'amélioration :
[2 à 3 pistes concrètes et actionnables pour améliorer la réponse — sans révéler la réponse modèle]

Souhaitez-vous améliorer votre réponse ?

**[R]** **[S]** **[N]** **[O]**

Si l'utilisateur répond **[R]** : affiche la réponse type CRPE complète sous ce format exact, puis affiche **[S]** **[O]** **[D]** seuls sur la dernière ligne :

Réponse type CRPE :
[Une réponse modèle complète et satisfaisante pour le concours]

Si l'utilisateur répond **[N]** (Réessayer) : réponds par une courte phrase d'encouragement (ex : "D'accord, réessayez !"). Ne réaffiche PAS l'exercice — il est déjà visible dans le chat. Affiche ensuite **[S]** seul sur la dernière ligne pour proposer une synthèse de cours. Incrémente le compteur à 2.
Si l'utilisateur répond **[O]** (Question suivante) : passe directement à l'exercice suivant sans afficher la réponse type.

— Tentative 2 : Fournis une correction complète format strict :

Note écriture : [X]/10
Note orthographe : [X]/10
Note CRPE : [X]/10
Note globale : [X]/10
ORTHO: "mot_fautif" → "correction" | ...  (ou ORTHO: aucune)
SYNTAXE: "erreur de syntaxe" → "correction" | ...  (ou SYNTAXE: aucune)

Ce qui va :
[Points positifs de la réponse]

Ce qui ne va pas :
[Points restant à corriger]

**[R]** **[S]** **[O]** **[D]**

Si l'utilisateur répond **[R]** : affiche la réponse type CRPE complète sous ce format exact, puis affiche **[S]** **[O]** **[D]** seuls sur la dernière ligne :

Réponse type CRPE :
[Une réponse modèle complète et satisfaisante pour le concours]

Si l'utilisateur répond **[D]** après la réponse type : identifie les 3 à 5 termes ou notions clés de la réponse type et fournis pour chacun une définition concise (1 à 2 phrases, vocabulaire académique). Format strict sans astérisques ni tirets : [Terme] : [définition]. Affiche ensuite **[O]** seul sur la dernière ligne.

Passe à l'exercice suivant.

---

## PROGRESSION ET ADAPTATION

Niveaux : **Très facile** → **Facile** → **Intermédiaire** → **Difficile**.

- Commence TOUJOURS par le niveau **Très facile** : questions courtes, directes, une seule notion à la fois, conçues pour mettre en confiance. Maintiens ce niveau pendant les **5 premiers exercices minimum**, quel que soit le résultat.
- Passe à **Facile** uniquement si la note globale est ≥ 6/10 sur au moins 3 exercices consécutifs en Très facile.
- Passe à **Intermédiaire** uniquement si la note globale est ≥ 7/10 sur au moins 3 exercices consécutifs en Facile.
- Passe à **Difficile** uniquement si la note globale est ≥ 8/10 sur au moins 3 exercices consécutifs en Intermédiaire.
- Si l'utilisateur échoue 2 exercices consécutifs (note < 5/10) : reviens au niveau inférieur et propose une synthèse ciblée.
- La progression est toujours **graduelle** — ne saute jamais un niveau.
- La ligne "Niveau de difficulté :" affichée dans CHAQUE exercice DOIT toujours correspondre exactement au niveau réel où tu te situes dans cette progression (déduit de l'historique des notes de la conversation) — ne l'affiche jamais au hasard, et mets-la à jour dès que tu changes de niveau.
- Lorsque tu fais évoluer le niveau (montée ou descente), informe brièvement l'utilisateur dans ton message ("Vous progressez bien, on passe au niveau Facile !" / "On revient au niveau Très facile pour consolider.").
- Après 5 à 8 exercices sur un thème, propose de passer au thème suivant :

> "Vous avez bien travaillé ce thème ! Voulez-vous :
> **[+]** Continuer sur ce thème (plus d'exercices)
> **[>]** Passer au thème suivant : **[NOM DU THÈME SUIVANT]**"

---

## STYLE ET TONALITÉ

- Ton bienveillant, encourageant, rigoureux.
- Jamais condescendant. Les erreurs sont des occasions d'apprendre.
- Énoncés clairs, phrases de support variées et représentatives du niveau cycle 4.
- Pour la compréhension de texte : utilise des extraits courts (8-12 lignes) de textes littéraires ou documentaires adaptés au niveau cycle 4.

---

## CE QUE TU NE FAIS PAS

- Tu ne laisses PAS l'utilisateur imposer un thème ou un sous-thème.
- Tu ne donnes PAS la correction avant que l'utilisateur ait répondu.
- Tu n'affiches PAS de menu avant l'exercice — l'énoncé est toujours affiché directement.
- Tu ne génères PAS plusieurs exercices à la fois.
- Tu n'utilises PAS d'astérisques pour mettre en gras ou en italique dans l'énoncé.
- Tu n'utilises PAS de tiret (- ou —) en début de ligne.
- Tu n'utilises PAS de lignes de séparation (---, ***, ___).
- Les marqueurs **[S]** et **[P]** apparaissent toujours à la fin de chaque exercice, seuls sur leur ligne, sans texte à côté.

---

## PROFIL DE L'UTILISATEUR (DÉJÀ RECUEILLI — NE PAS REDEMANDER)

- Prénom : ${profile.prenom}
- Type de concours : ${profile.concours}
- Académie : ${profile.academie || 'non précisée'}

Dans ton message d'accueil, utilise ces informations directement. Personnalise la session avec le prénom "${profile.prenom}". Ne pose PAS ces questions — commence immédiatement par le message d'accueil puis annonce le premier thème du programme.
${niveauSection}`;
}

// ---------------------------------------------------------------------------
// Français topic list (used in SubjectPickerView and HistoryItem)
// ---------------------------------------------------------------------------
const FRANCAIS_TOPICS = [
  { id: 'lecture',     label: 'Lecture',                               description: 'Compréhension et analyse de textes' },
  { id: 'culture',     label: 'Culture littéraire et artistique',      description: 'Œuvres, auteurs, mouvements littéraires' },
  { id: 'ecriture',    label: 'Écriture',                              description: "Production d'écrit et organisation textuelle" },
  { id: 'vocabulaire', label: 'Vocabulaire et orthographe lexicale',   description: 'Formation des mots, synonymes, orthographe' },
  { id: 'grammaire',   label: 'Grammaire et orthographe grammaticale', description: 'Classes de mots, syntaxe, accords' },
];

const NIVEAUX = [
  { id: '5eme', label: '5ème', description: 'Début de cycle 4 — notions fondamentales' },
  { id: '4eme', label: '4ème', description: 'Milieu de cycle 4 — approfondissement' },
  { id: '3eme', label: '3ème', description: 'Fin de cycle 4 — niveau CRPE standard' },
];

function getNiveauLabel(id) {
  return NIVEAUX.find(n => n.id === id)?.label || id;
}

// ---------------------------------------------------------------------------
// Supabase — client + fetch official objectives from DB
// ---------------------------------------------------------------------------
import { createClient } from '@supabase/supabase-js';

const SUPABASE_URL = import.meta.env.VITE_SUPABASE_URL;
const SUPABASE_KEY = import.meta.env.VITE_SUPABASE_ANON_KEY;

export const sbClient = createClient(SUPABASE_URL, SUPABASE_KEY);

const TOPIC_TO_THEMATIQUE = {
  lecture:     'Lecture',
  culture:     'Culture littéraire et artistique',
  ecriture:    'Écriture',
  vocabulaire: 'Vocabulaire et orthographe lexicale',
  grammaire:   'Grammaire et orthographe grammaticale',
};
const NIVEAU_TO_CLASSE = { '5eme': '5e', '4eme': '4e', '3eme': '3e' };

const MATH_THEMATIQUES = [
  {
    id: 'nombres',
    label: 'Nombres et calculs',
    description: 'Opérations, fractions, puissances, calcul littéral',
    icon: Calculator,
    colors: { bg: 'bg-emerald-100', icon: 'text-emerald-600' },
  },
  {
    id: 'geometrie',
    label: 'Espace et géométrie',
    description: 'Figures planes, transformations, Pythagore, Thalès',
    icon: Lightbulb,
    colors: { bg: 'bg-sky-100', icon: 'text-sky-600' },
  },
  {
    id: 'proportionnalite',
    label: 'Proportionnalité, fonctions',
    description: 'Proportionnalité, fonctions affines, graphiques',
    icon: BarChart2,
    colors: { bg: 'bg-violet-100', icon: 'text-violet-600' },
  },
  {
    id: 'donnees',
    label: 'Organisation et gestion de données et probabilités',
    description: 'Statistiques, probabilités, diagrammes',
    icon: ListChecks,
    colors: { bg: 'bg-amber-100', icon: 'text-amber-600' },
  },
  {
    id: 'informatique',
    label: 'La pensée informatique',
    description: 'Algorithmes, programmation, logique',
    icon: AlignLeft,
    colors: { bg: 'bg-rose-100', icon: 'text-rose-600' },
  },
];

async function fetchExercicesMaths(thematique, classe) {
  if (!thematique || !classe || !SUPABASE_URL || !SUPABASE_KEY) return [];
  try {
    const params = new URLSearchParams({
      thematique: `eq.${thematique}`,
      classe:     `eq.${classe}`,
      select:     'id,objectif_id,objectif_apprentissage,thematique,sous_categorie,classe,enonce,question,reponse_ideale,figure_svg,synthese_cours,definition_mots_cles',
      order:      'id.asc',
    });
    const res = await fetch(`${SUPABASE_URL}/rest/v1/exercices_maths?${params}`, {
      headers: { apikey: SUPABASE_KEY, Authorization: `Bearer ${SUPABASE_KEY}` },
    });
    if (!res.ok) return [];
    return await res.json();
  } catch {
    return [];
  }
}

async function fetchObjectives(topic, niveau) {
  const thematique = TOPIC_TO_THEMATIQUE[topic];
  const classe = NIVEAU_TO_CLASSE[niveau];
  if (!thematique || !classe || !SUPABASE_URL || !SUPABASE_KEY) return [];
  try {
    const params = new URLSearchParams({
      thematique: `eq.${thematique}`,
      classe: `eq.${classe}`,
      select: 'groupe,sous_categorie,objectif,ordre_sous_categorie,ordre_objectif',
      order: 'ordre_sous_categorie.asc,ordre_objectif.asc',
    });
    const res = await fetch(`${SUPABASE_URL}/rest/v1/vue_competences_cycle4?${params}`, {
      headers: { apikey: SUPABASE_KEY, Authorization: `Bearer ${SUPABASE_KEY}` },
    });
    if (!res.ok) return [];
    return await res.json();
  } catch {
    return [];
  }
}

function shuffleArray(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

async function fetchQuestionsFromBanque(topic, niveau) {
  const thematique = TOPIC_TO_THEMATIQUE[topic];
  const classe = NIVEAU_TO_CLASSE[niveau];
  if (!thematique || !classe || !SUPABASE_URL || !SUPABASE_KEY) return [];
  try {
    const params = new URLSearchParams({
      thematique: `eq.${thematique}`,
      niveau:     `eq.${classe}`,
      select:     'id,thematique,sous_categorie,objectif,texte_support,question,reponse_ideale,niveau_difficulte,synthese_cours,definition_mots_cles',
    });
    const res = await fetch(`${SUPABASE_URL}/rest/v1/exercices_francais_v?${params}`, {
      headers: { apikey: SUPABASE_KEY, Authorization: `Bearer ${SUPABASE_KEY}` },
    });
    if (!res.ok) return [];
    const data = await res.json();
    return shuffleArray(data.filter(q => q.question && q.reponse_ideale));
  } catch {
    return [];
  }
}

async function fetchCompletedQuestionIds(userId) {
  if (!SUPABASE_URL || !SUPABASE_KEY || !userId) return new Set();
  try {
    const params = new URLSearchParams({
      user_id:               `eq.${userId}`,
      select:                'id_question_completee',
      id_question_completee: 'not.is.null',
    });
    const res = await fetch(`${SUPABASE_URL}/rest/v1/reponses_utilisateurs?${params}`, {
      headers: { apikey: SUPABASE_KEY, Authorization: `Bearer ${SUPABASE_KEY}` },
    });
    if (!res.ok) return new Set();
    const rows = await res.json();
    return new Set(rows.map(r => r.id_question_completee).filter(Boolean));
  } catch (_) { return new Set(); }
}

async function fetchProgressionStats(userId) {
  if (!SUPABASE_URL || !SUPABASE_KEY || !userId) {
    return { completedFacile: 0, avgGlobal: null, avgCrpe: null, avgEcriture: null, avgOrthographe: null, unlocked: false };
  }
  try {
    const params = new URLSearchParams({
      user_id: `eq.${userId}`,
      select:  'id_question_completee,note_ecriture,note_orthographe,note_crpe,thematique',
    });
    const res = await fetch(`${SUPABASE_URL}/rest/v1/reponses_utilisateurs?${params}`, {
      headers: { apikey: SUPABASE_KEY, Authorization: `Bearer ${SUPABASE_KEY}` },
    });
    if (!res.ok) throw new Error();
    const rows = await res.json();
    if (!Array.isArray(rows)) throw new Error();

    // Accept both short IDs (ChatView) and full names (BanqueQuestionsView)
    const francaisThematiques = new Set([
      ...Object.keys(TOPIC_TO_THEMATIQUE),
      ...Object.values(TOPIC_TO_THEMATIQUE),
    ]);
    const francaisRows = rows.filter(r => francaisThematiques.has(r.thematique));

    const completedFacile = new Set(
      francaisRows.filter(r => r.id_question_completee).map(r => r.id_question_completee)
    ).size;

    const mean = (arr) => {
      const valid = arr.filter(v => v != null);
      return valid.length ? Math.round(valid.reduce((a, b) => a + b, 0) / valid.length * 10) / 10 : null;
    };

    const avgGlobal = mean(francaisRows.map(r => {
      const ns = [r.note_ecriture, r.note_orthographe, r.note_crpe].filter(v => v != null);
      return ns.length ? ns.reduce((a, b) => a + b, 0) / ns.length : null;
    }));
    const avgCrpe        = mean(francaisRows.map(r => r.note_crpe));
    const avgEcriture    = mean(francaisRows.map(r => r.note_ecriture));
    const avgOrthographe = mean(francaisRows.map(r => r.note_orthographe));

    const unlocked = completedFacile > 100 && (avgGlobal ?? 0) >= 7 && (avgCrpe ?? 0) >= 8;

    return { completedFacile, avgGlobal, avgCrpe, avgEcriture, avgOrthographe, unlocked };
  } catch {
    return { completedFacile: 0, avgGlobal: null, avgCrpe: null, avgEcriture: null, avgOrthographe: null, unlocked: false };
  }
}

async function supabaseInsert(table, data) {
  if (!SUPABASE_URL || !SUPABASE_KEY) return;
  try {
    await fetch(`${SUPABASE_URL}/rest/v1/${table}`, {
      method: 'POST',
      headers: {
        apikey: SUPABASE_KEY,
        Authorization: `Bearer ${SUPABASE_KEY}`,
        'Content-Type': 'application/json',
        Prefer: 'return=minimal',
      },
      body: JSON.stringify(data),
    });
  } catch (e) {
    console.warn(`[Supabase] Insert ${table}:`, e.message);
  }
}

async function supabaseInsertReturningId(table, data) {
  if (!SUPABASE_URL || !SUPABASE_KEY) return null;
  try {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/${table}`, {
      method: 'POST',
      headers: {
        apikey: SUPABASE_KEY,
        Authorization: `Bearer ${SUPABASE_KEY}`,
        'Content-Type': 'application/json',
        Prefer: 'return=representation',
      },
      body: JSON.stringify(data),
    });
    const rows = await res.json();
    return rows?.[0]?.id ?? null;
  } catch (e) {
    console.warn(`[Supabase] Insert ${table}:`, e.message);
    return null;
  }
}

async function supabasePatch(table, filters, data) {
  if (!SUPABASE_URL || !SUPABASE_KEY) return;
  try {
    const params = new URLSearchParams(
      Object.entries(filters).map(([k, v]) => [k, `eq.${v}`])
    );
    await fetch(`${SUPABASE_URL}/rest/v1/${table}?${params}`, {
      method: 'PATCH',
      headers: {
        apikey: SUPABASE_KEY,
        Authorization: `Bearer ${SUPABASE_KEY}`,
        'Content-Type': 'application/json',
        Prefer: 'return=minimal',
      },
      body: JSON.stringify(data),
    });
  } catch (e) {
    console.warn(`[Supabase] Patch ${table}:`, e.message);
  }
}

// ---------------------------------------------------------------------------
// DB session helpers — sessions table
// ---------------------------------------------------------------------------
async function fetchActiveSession(userId, topic, niveau) {
  if (!SUPABASE_URL || !SUPABASE_KEY || !userId) return null;
  try {
    const params = new URLSearchParams({
      user_id:      `eq.${userId}`,
      topic:        `eq.${topic}`,
      niveau:       `eq.${niveau}`,
      is_completed: 'eq.false',
      order:        'updated_at.desc',
      limit:        '1',
      select:       'id,messages,current_index,exercice_num,displayed_diff,tentative,phase',
    });
    const res = await fetch(`${SUPABASE_URL}/rest/v1/sessions?${params}`, {
      headers: { apikey: SUPABASE_KEY, Authorization: `Bearer ${SUPABASE_KEY}` },
    });
    if (!res.ok) return null;
    const rows = await res.json();
    return rows[0] ?? null;
  } catch (_) { return null; }
}

async function fetchFreeQuestionsUsed(userId) {
  if (!userId) return null;
  try {
    const { data, error } = await sbClient
      .from('reponses_utilisateurs')
      .select('tentative')
      .eq('user_id', userId)
      .eq('tentative', 1);
    if (error) throw error;
    return Array.isArray(data) ? data.length : null;
  } catch (e) {
    console.warn('[fetchFreeQuestionsUsed]', e?.message);
    return null;
  }
}

async function fetchPaidStatus() {
  try {
    const { data, error } = await sbClient
      .from('profils_utilisateurs')
      .select('crpe_paid')
      .limit(1)
      .single();
    if (error) throw error;
    return data?.crpe_paid === true;
  } catch {
    return null; // null = non disponible (fallback localStorage)
  }
}

async function fetchLastActiveSession(userId) {
  if (!SUPABASE_URL || !SUPABASE_KEY || !userId) return null;
  try {
    const params = new URLSearchParams({
      user_id: `eq.${userId}`,
      order:   'created_at.desc',
      limit:   '1',
      select:  'id,topic,niveau,messages,current_index,exercice_num,displayed_diff,tentative,phase',
    });
    const res = await fetch(`${SUPABASE_URL}/rest/v1/sessions?${params}`, {
      headers: { apikey: SUPABASE_KEY, Authorization: `Bearer ${SUPABASE_KEY}` },
    });
    if (!res.ok) return null;
    const rows = await res.json();
    const row = rows[0];
    if (!row || !Array.isArray(row.messages) || row.messages.length <= 1) return null;
    return row;
  } catch (_) { return null; }
}

async function createDbSession(userId, topic, niveau) {
  if (!SUPABASE_URL || !SUPABASE_KEY || !userId) return null;
  try {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/sessions`, {
      method: 'POST',
      headers: {
        apikey: SUPABASE_KEY,
        Authorization: `Bearer ${SUPABASE_KEY}`,
        'Content-Type': 'application/json',
        Prefer: 'return=representation',
      },
      body: JSON.stringify({ user_id: userId, topic, niveau }),
    });
    if (!res.ok) return null;
    const rows = await res.json();
    return rows[0]?.id ?? null;
  } catch (_) { return null; }
}

async function updateDbSession(sessionId, payload) {
  if (!SUPABASE_URL || !SUPABASE_KEY || !sessionId) return;
  try {
    await fetch(`${SUPABASE_URL}/rest/v1/sessions?id=eq.${sessionId}`, {
      method: 'PATCH',
      headers: {
        apikey: SUPABASE_KEY,
        Authorization: `Bearer ${SUPABASE_KEY}`,
        'Content-Type': 'application/json',
        Prefer: 'return=minimal',
      },
      body: JSON.stringify({ ...payload, updated_at: new Date().toISOString() }),
    });
  } catch (_) {}
}

function extractExerciseData(text) {
  const subcatMatch   = text.match(/^Sous-catégorie\s*:\s*(.+)$/m);
  const objectifMatch = text.match(/^Objectif\s*:\s*(.+)$/m);
  const questionMatch = text.match(/^Question\s*:\s*(.+)$/m);
  const idealMatch    = text.match(/^IDEAL:\s*(.+)$/m);
  const texteMatch    = text.match(/«([\s\S]+?)»/);
  return {
    sous_categorie: subcatMatch?.[1]?.trim()   || null,
    objectif:       objectifMatch?.[1]?.trim() || null,
    question:       questionMatch?.[1]?.trim() || null,
    ideal:          idealMatch?.[1]?.trim()    || null,
    texte:          texteMatch?.[1]?.trim()    || null,
  };
}

function extractReponseTypeCRPE(text) {
  // Pas de flag m : $ = fin de chaîne uniquement (évite le bug "fin de ligne" du flag m)
  const m = text.match(/Réponse type CRPE\s*:\s*\n([\s\S]+?)(?=\n\s*\*\*\[|$)/);
  return m?.[1]?.trim() || null;
}

function extractOrthoFautes(text) {
  const match = text.match(/^ORTHO:\s*(.+)$/m);
  if (!match || /^aucune$/i.test(match[1].trim())) return [];
  return match[1].split('|').map(item => {
    const parts = item.split('→').map(s =>
      s.trim().replace(/^["«»"“”]+|["«»"“”]+$/g, '').trim()
    );
    return { faute: parts[0] || '', correction: parts[1] || '' };
  }).filter(f => f.faute);
}

function extractSyntaxeErreurs(text) {
  const match = text.match(/^SYNTAXE:\s*(.+)$/m);
  if (!match || /^aucune$/i.test(match[1].trim())) return [];
  return match[1].split('|').map(item => {
    const parts = item.split('→').map(s =>
      s.trim().replace(/^["«»"“”]+|["«»"“”]+$/g, '').trim()
    );
    return { erreur: parts[0] || '', correction: parts[1] || '' };
  }).filter(e => e.erreur);
}

function extractConseils(text) {
  // Format ChatView : notes (+ ORTHO/SYNTAXE) puis conseils ("Ce qui va", "Pistes d'amélioration"…)
  const m1 = text.match(/Note\s+globale\s*:\s*\d+\s*\/\s*10[^\n]*\n(?:ORTHO:.*\n)?(?:SYNTAXE:.*\n)?([\s\S]*?)(?=\s*Réponse type CRPE\s*:|\s*Souhaitez-vous|\s*Êtes-vous prêt|\s*\*\*\[|$)/);
  if (m1?.[1]?.trim()) return m1[1].trim();
  // Format banque de questions : conseils ("Sur le fond/forme/orthographe") puis notes
  const m2 = text.match(/^([\s\S]+?)\n+Note\s+écriture\s*:/m);
  return m2?.[1]?.trim() || null;
}

function extractNotesFromText(text) {
  const notes = {};
  const re = /^Note\s+(.+?)\s*:\s*(\d+)\s*\/\s*10/gm;
  let m;
  while ((m = re.exec(text)) !== null) {
    const lbl = m[1].toLowerCase();
    const val = parseInt(m[2]);
    if (lbl.includes('écriture'))    notes.ecriture    = val;
    else if (lbl.includes('ortho'))  notes.orthographe = val;
    else if (lbl.includes('crpe'))   notes.crpe        = val;
    else if (lbl.includes('global')) notes.globale     = val;
  }
  return notes;
}

function buildProgramFromObjectives(objectives, topicLabel, niveauLabel) {
  if (!objectives?.length) return null;
  const sections = [];
  const seen = new Map();
  objectives.forEach(obj => {
    const key = `${obj.ordre_sous_categorie}_${obj.sous_categorie}`;
    if (!seen.has(key)) {
      const sec = { groupe: obj.groupe, nom: obj.sous_categorie, items: [] };
      seen.set(key, sec);
      sections.push(sec);
    }
    seen.get(key).items.push(obj.objectif);
  });
  const lines = [
    `## OBJECTIFS OFFICIELS — ${topicLabel.toUpperCase()} — CLASSE DE ${niveauLabel.toUpperCase()}`,
    `(Programme officiel de français pour le cycle 4 — Ministère de l'Éducation nationale)`,
    '',
  ];
  let num = 1;
  let lastGroupe = null;
  sections.forEach(sec => {
    if (sec.groupe && sec.groupe !== lastGroupe) {
      lines.push(`#### ${sec.groupe}`);
      lastGroupe = sec.groupe;
    }
    lines.push(`### ${num}. ${sec.nom}`);
    sec.items.forEach(item => lines.push(`- ${item}`));
    lines.push('');
    num++;
  });
  lines.push(`**Ordre de travail :** Distribue les exercices de façon ALÉATOIRE entre ces objectifs — ne suis PAS l'ordre numérique. Varie les sous-catégories. Veille à couvrir l'ensemble des objectifs au fil de la session.`);
  return lines.join('\n');
}

function getFrancaisEcriturePrompt(profile, topic, niveau) {
  const topicLabel = topic ? FRANCAIS_TOPICS.find(t => t.id === topic)?.label || 'Français' : 'Français';
  const niveauLabel = niveau ? getNiveauLabel(niveau) : null;
  const niveauSection = niveauLabel ? `\n## NIVEAU DE CLASSE\n\nL'utilisateur travaille au niveau **${niveauLabel}**. Adapte la difficulté des exemples et des exercices à ce niveau.\n\n---\n` : '';

  return `Tu es un coach en rédaction pour la préparation au CRPE. L'utilisateur travaille sur le domaine **${topicLabel}**. Ton objectif : lui apprendre à construire des réponses bien rédigées, conformes aux attentes du concours.

---

## TON RÔLE

Pour chaque exercice :
1. Génère MENTALEMENT une réponse type CRPE parfaite (3-5 phrases, vocabulaire académique, mots clés, tournures). Garde-la en mémoire sans la montrer.
2. Pose une question type CRPE liée au domaine.
3. Fournis une réponse incorrecte sur la FORME uniquement (fond correct, registre familier, structure faible).
4. Propose les trois options disponibles via les boutons.

---

## FORMAT STRICT DE CHAQUE EXERCICE

Aucun astérisque dans le texte, aucun tiret en début de ligne, aucune ligne de séparation.

Exercice [N] - [Sous-thème]

Question : [Une question type CRPE sur le domaine]

Consigne : La réponse ci-dessous est incorrecte sur la forme, mais le fond est juste. Reformulez-la en 3 à 5 phrases conformes aux attentes du CRPE. Vous pouvez rédiger directement, demander une aide ou reconstituer la réponse en mode puzzle. Vous avez 2 tentatives.

Réponse incorrecte :
[Une réponse au fond correct mais mal formulée : registre familier, structure faible, vocabulaire peu académique — 2 à 4 lignes]

**[A]** **[M]** **[S]**

---

## GESTION DES OPTIONS AVANT RÉDACTION

Si l'utilisateur répond **[A]** — Aide à la rédaction :
Réponds avec EXACTEMENT ce format, dans cet ordre, sans texte avant ni après ces lignes techniques :

Mots clés : mot1 (définition en 4 mots), mot2 (définition en 4 mots), mot3 (définition en 4 mots), mot4 (définition en 4 mots), mot5 (définition en 4 mots)

Tournures de phrases : "Amorce 1" [début] / "Amorce 2" [début] / "Amorce 3" [milieu] / "Amorce 4" [milieu] / "Amorce 5" [fin] / "Amorce 6" [fin]

AIDE_PISTE: [Une phrase de piste de rédaction : comment structurer la réponse, quelle idée développer en premier, comment articuler les parties — 2 à 3 phrases maximum, directement actionnable]

**[A]** **[M]** **[S]**

Si l'utilisateur répond **[M]** — Mode puzzle (reconstitution guidée) :
1. Découpe ta réponse idéale en 6 à 8 segments courts (6-10 mots, coupures aux virgules ou conjonctions).
2. Mélange aléatoirement ces segments.
3. Affiche UNIQUEMENT :
   - Un court message : "Voici les segments dans le désordre. Quel est le premier selon vous ? Expliquez votre choix."
   - La ligne technique : PUZZLE_GAME: seg1|seg2|seg3|seg4|seg5|seg6
4. L'utilisateur répond en choisissant un segment et en expliquant son choix.
5. Valide son choix :
   - Correct → "Bon choix ! [brève raison]" puis "Choisissez maintenant le segment N+1 :" + PUZZLE_GAME: [segments restants]
   - Incorrect → "Ce n'est pas le bon segment. Réessayez." + PUZZLE_GAME: [mêmes segments dans un ordre légèrement différent]
6. Continue segment par segment jusqu'à ce que tous soient placés dans l'ordre.
7. Quand la reconstitution est complète : "Parfait ! Vous avez reconstitué la réponse. Vous pouvez maintenant l'envoyer pour obtenir votre note." — Sans ligne PUZZLE_GAME dans ce message final.

Si l'utilisateur répond **[S]** — Synthèse du cours :
Fournis une synthèse ciblée sur la notion. Présente le cours de manière neutre et générale — sans jamais donner d'éléments de réponse à la question posée ni orienter vers la solution. Termine OBLIGATOIREMENT par cette phrase exacte : "Essayez de répondre à la question en vous basant sur cette synthèse de cours." Puis réaffiche l'exercice complet en terminant par **[A]** **[M]** **[S]**.

---

## ÉVALUATION APRÈS CHAQUE RÉPONSE

Attends la réponse libre de l'utilisateur SANS donner la correction au préalable.
Suis un compteur de tentatives (1, 2…). Réinitialise à 1 à chaque nouvel exercice.

Une fois la réponse soumise, évalue-la. Format strict — NE DONNE AUCUNE indication de correction, aucun conseil, aucun point à corriger :

Note : [X]/10

Ce qui va :
[Points positifs uniquement : vocabulaire académique, structure, développement des idées]

Si note ≥ 8 :

Excellente réponse ! Vous maîtrisez bien cet exercice.

**[S]** **[N]** **[R]** **[O]**

Si note < 8 ET tentatives < 2 :

**[S]** **[N]** **[R]** **[O]**

Si note < 8 ET tentatives = 2 :

Vous avez utilisé vos 2 tentatives.

**[R]** **[S]** **[O]** **[D]**

---

## GESTION DES BOUTONS APRÈS ÉVALUATION

Si l'utilisateur répond **[N]** — Réessayer :
Réponds uniquement par une courte phrase d'encouragement (ex : "D'accord, réessayez !"). Ne réaffiche PAS l'exercice — il est déjà visible dans le chat. Incrémente le compteur. Affiche ensuite **[A]** **[M]** **[S]** seuls sur la dernière ligne.

Si l'utilisateur répond **[R]** — Voir la réponse type :
Affiche UNIQUEMENT la réponse type CRPE. Aucune explication. Puis : **[O]** **[D]**

Si l'utilisateur répond **[D]** après la réponse type : identifie les 3 à 5 termes ou expressions académiques clés de la réponse type et fournis pour chacun une définition concise. Format strict sans astérisques ni tirets : [Terme] : [définition]. Affiche ensuite **[O]** seul.

Si l'utilisateur répond **[O]** — Question suivante :
Passe à l'exercice suivant. Réinitialise le compteur à 1.

---

## STYLE ET TONALITÉ

- Bienveillant, pédagogique, exigeant sur la forme.
- La réponse incorrecte : fond correct, forme défaillante (registre familier, phrases mal construites).
- Dans l'évaluation, compare toujours avec la réponse incorrecte fournie.

---

## PROFIL DE L'UTILISATEUR

- Prénom : ${profile.prenom}
- Type de concours : ${profile.concours}
- Académie : ${profile.academie || 'non précisée'}
${niveauSection}`;
}

// ---------------------------------------------------------------------------
// Prompt — Révision mots clés & tournures
// ---------------------------------------------------------------------------
function getFrancaisRevisionPrompt(profile, keywordsData) {
  const allWords = [...new Set((keywordsData || []).flatMap(k => k.words || []))];
  const allTournures = [...new Set((keywordsData || []).flatMap(k => k.tournures || []))];

  const wordsSection = allWords.length
    ? `Mots clés à réviser : ${allWords.join(', ')}`
    : 'Aucun mot clé enregistré — invente une liste de 10 mots clés académiques CRPE courants pour la production écrite.';

  const tournuresSection = allTournures.length
    ? `Tournures de phrases à réviser : ${allTournures.map(t => `"${t}"`).join(' / ')}`
    : 'Aucune tournure enregistrée — invente une liste de 6 tournures académiques CRPE courantes.';

  return `Tu es un coach en mémorisation pour la préparation au CRPE. L'utilisateur a travaillé des mots clés et des tournures de phrases dans ses sessions "Apprendre à rédiger". Ton objectif : lui proposer des exercices variés pour les mémoriser et les réutiliser avec aisance.

---

## DONNÉES À RÉVISER

${wordsSection}

${tournuresSection}

---

## TYPES D'EXERCICES (un seul exercice à la fois, varier les types)

Type A — Compléter la phrase :
Propose une phrase à trous avec un mot clé manquant. Donne 3 choix dont la bonne réponse.

Type B — Reformuler avec une tournure :
Donne une phrase simple et demande à l'utilisateur de la reformuler en utilisant une tournure précise fournie.

Type C — Employer en contexte :
Donne un mot clé et demande à l'utilisateur de construire une phrase cohérente de style CRPE l'intégrant.

Type D — Identifier la bonne tournure :
Propose deux formulations de la même idée et demande laquelle est la tournure académique correcte.

---

## FORMAT STRICT DE CHAQUE EXERCICE

Aucun astérisque dans le texte, aucun tiret en début de ligne, aucune ligne de séparation.

Exercice [N] — Type [A / B / C / D]

[Énoncé clair de l'exercice]

**[S]** **[P]**

---

## APRÈS CHAQUE RÉPONSE

Attends la réponse SANS corriger au préalable. Puis :

Note : [X]/10

Ce qui va :
[Points positifs uniquement]

Si note ≥ 8 :
Bonne réponse !

**[N]** **[O]**

Si note < 8 :

**[S]** **[N]** **[R]** **[O]**

Si l'utilisateur répond **[S]** : fournis une synthèse ciblée sur la notion de l'exercice. Présente le cours de manière neutre et générale — sans jamais donner d'éléments de réponse à la question posée ni orienter vers la solution. Termine OBLIGATOIREMENT par cette phrase exacte : "Essayez de répondre à la question en vous basant sur cette synthèse de cours." Ne réaffiche PAS l'exercice ni aucun bouton après la synthèse.
Si l'utilisateur répond **[N]** : réponds par une courte phrase d'encouragement. Ne réaffiche PAS l'exercice — il est déjà visible dans le chat. Affiche ensuite **[S]** seul sur la dernière ligne pour proposer une synthèse de cours.
Si l'utilisateur répond **[R]** : donne la bonne réponse sans commentaire. Puis **[O]** **[D]** sur la dernière ligne.

Si l'utilisateur répond **[D]** après la réponse : identifie les 2 à 3 termes clés de la réponse et fournis pour chacun une définition concise. Format : [Terme] : [définition]. Affiche ensuite **[O]** seul.
Si l'utilisateur répond **[O]** : passe à l'exercice suivant, en changeant de type.

---

## STYLE ET TONALITÉ

- Bienveillant, dynamique, encourageant.
- Varie obligatoirement les types d'exercices pour éviter la monotonie.
- Reviens régulièrement sur les mots clés et tournures les moins bien maîtrisés.

---

## PROFIL DE L'UTILISATEUR

- Prénom : ${profile.prenom}
- Type de concours : ${profile.concours}
- Académie : ${profile.academie || 'non précisée'}`;
}

// ---------------------------------------------------------------------------
// Storage
// ---------------------------------------------------------------------------
const storage = {
  get: (key) => {
    try {
      const raw = window.storage?.getItem
        ? window.storage.getItem(key)
        : localStorage.getItem(key);
      return raw ? JSON.parse(raw) : null;
    } catch { return null; }
  },
  set: (key, val) => {
    try {
      const s = JSON.stringify(val);
      if (window.storage?.setItem) window.storage.setItem(key, s);
      else localStorage.setItem(key, s);
    } catch {}
  },
};

function uid() {
  return Date.now().toString(36) + Math.random().toString(36).slice(2);
}

// ---------------------------------------------------------------------------
// Streaming helper
// ---------------------------------------------------------------------------
async function streamClaude(messages, system, onChunk, onDone, meta) {
  const res = await fetch('/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ messages, system, meta }),
  });

  if (!res.ok) throw new Error(`HTTP ${res.status}`);

  const reader = res.body.getReader();
  const decoder = new TextDecoder();
  let buffer = '';
  let fullText = '';

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    buffer += decoder.decode(value, { stream: true });
    const lines = buffer.split('\n');
    buffer = lines.pop() ?? '';

    for (const line of lines) {
      if (!line.startsWith('data: ')) continue;
      const payload = line.slice(6);
      if (payload === '[DONE]') { onDone(fullText); return; }
      try {
        const { text, error } = JSON.parse(payload);
        if (error) throw new Error(error);
        if (text) { fullText += text; onChunk(fullText); }
      } catch (e) { if (e.message !== 'Unexpected end of JSON') throw e; }
    }
  }
  onDone(fullText);
}

// ---------------------------------------------------------------------------
// Quick-reply option extraction  — matches **[X]** in assistant text
// ---------------------------------------------------------------------------
const OPTION_RE = /\*\*\[([SPRCQON+>1-9MAD])\]\*\*/g;

function extractOptions(text) {
  const seen = new Set();
  let m;
  while ((m = OPTION_RE.exec(text)) !== null) seen.add(m[1]);
  return [...seen];
}

function extractScores(messages) {
  const re = /Note(?:\s+globale)?\s*:\s*(\d+)\s*\/\s*10/gi;
  const scores = [];
  (messages || []).forEach(msg => {
    if (msg.role === 'assistant') {
      re.lastIndex = 0;
      let m;
      while ((m = re.exec(msg.content)) !== null) {
        const n = parseInt(m[1]);
        if (n >= 0 && n <= 10) scores.push(n);
      }
    }
  });
  return scores;
}

function avgScore(scores) {
  if (!scores.length) return null;
  return Math.round(scores.reduce((a, b) => a + b, 0) / scores.length * 10) / 10;
}

function extractAllScores(messages) {
  const result = { ecriture: [], orthographe: [], crpe: [] };
  (messages || []).forEach(msg => {
    if (msg.role !== 'assistant') return;
    msg.content.split('\n').forEach(line => {
      const m = line.match(/^Note\s+(.+?)\s*:\s*(\d+)\s*\/\s*10/i);
      if (!m) return;
      const lbl = m[1].toLowerCase();
      const val = parseInt(m[2]);
      if (val < 0 || val > 10) return;
      if (lbl.includes('criture'))      result.ecriture.push(val);
      else if (lbl.includes('orth'))    result.orthographe.push(val);
      else if (lbl.includes('crpe'))    result.crpe.push(val);
    });
  });
  return result;
}

function extractKeywords(text) {
  const match = text.match(/^Mots\s+cl[eé]s\s*:\s*(.+)$/im);
  if (!match) return [];
  return match[1].split(',').map(item => {
    const m = item.trim().match(/^(.+?)\s*\(([^)]+)\)\s*$/);
    if (m) return { word: m[1].trim(), def: m[2].trim() };
    return { word: item.trim(), def: null };
  }).filter(k => k.word);
}

function extractTournures(text) {
  const match = text.match(/^Tournures\s+de\s+phrases\s*:\s*(.+)$/im);
  if (!match) return [];
  return match[1].split('/').map(item => {
    const posMath = item.match(/\[(début|milieu|fin)\]/i);
    const position = posMath ? posMath[1].toLowerCase() : null;
    const cleaned = item.replace(/\[(début|milieu|fin)\]/i, '').replace(/^["«""\s]+|["»""\s]+$/g, '').trim();
    return { text: cleaned, position };
  }).filter(t => t.text);
}

function stripEcritureLines(text) {
  return text.split('\n')
    .filter(line => !/^Mots\s+cl[eé]s\s*:/i.test(line.trim()))
    .filter(line => !/^Tournures\s+de\s+phrases\s*:/i.test(line.trim()))
    .filter(line => !/^AIDE_PISTE:/i.test(line.trim()))
    .filter(line => !/^PUZZLE_GAME:/i.test(line.trim()))
    .filter(line => !/^PUZZLE:/i.test(line.trim()))
    .filter(line => !/^ORTHO:/i.test(line.trim()))
    .filter(line => !/^SYNTAXE:/i.test(line.trim()))
    .filter(line => !/^IDEAL:/i.test(line.trim()))
    .join('\n');
}

// ---------------------------------------------------------------------------
// Simple markdown renderer (bold + blockquote + newlines)
// ---------------------------------------------------------------------------
function renderLine(line, key) {
  const noteMatch = line.match(/^(Note(?:\s+\S+)*)\s*:\s*(\d+)\s*\/\s*(\d+)$/);
  if (noteMatch) {
    const [, label, score, total] = noteMatch;
    const n = parseInt(score);
    const pct = Math.round((n / parseInt(total)) * 100);
    const isEcriture  = label.includes('écriture');
    const isOrtho     = label.includes('orthographe');
    const isCRPE      = label.includes('CRPE');
    const isGlobale   = label.includes('globale');
    const cfg = isEcriture
      ? { bg: 'bg-blue-50',    border: 'border-blue-200',    text: 'text-blue-700',    bar: 'bg-blue-400',    icon: <PenLine       className="w-3 h-3 flex-shrink-0" /> }
      : isOrtho
      ? { bg: 'bg-rose-50',    border: 'border-rose-200',    text: 'text-rose-700',    bar: 'bg-rose-400',    icon: <AlignLeft     className="w-3 h-3 flex-shrink-0" /> }
      : isCRPE
      ? { bg: 'bg-amber-50',   border: 'border-amber-200',   text: 'text-amber-700',   bar: 'bg-amber-400',   icon: <GraduationCap className="w-3 h-3 flex-shrink-0" /> }
      : isGlobale
      ? { bg: 'bg-emerald-50', border: 'border-emerald-200', text: 'text-emerald-700', bar: 'bg-emerald-500', icon: <BookMarked    className="w-3 h-3 flex-shrink-0" /> }
      : { bg: 'bg-gray-50',    border: 'border-gray-200',    text: 'text-gray-700',    bar: 'bg-gray-400',    icon: null };
    return (
      <div key={key} className={`flex items-center gap-2 my-1 px-2.5 py-1.5 border rounded-lg ${cfg.bg} ${cfg.border} ${cfg.text}`}>
        {cfg.icon}
        <span className="text-xs font-medium flex-1">{label}</span>
        <div className="w-16 h-1.5 bg-white rounded-full overflow-hidden">
          <div className={`h-full rounded-full ${cfg.bar}`} style={{ width: `${pct}%` }} />
        </div>
        <span className="text-sm font-bold tabular-nums">{score}<span className="text-xs font-normal opacity-60">/{total}</span></span>
      </div>
    );
  }

  if (line.startsWith('Niveau de difficulté :')) {
    const label = line.slice('Niveau de difficulté :'.length).trim();
    const lower = label.toLowerCase();
    const cfg = lower.includes('très facile')
      ? { bg: 'bg-emerald-50', border: 'border-emerald-200', text: 'text-emerald-700', dot: 'bg-emerald-400' }
      : lower.includes('facile')
      ? { bg: 'bg-green-50',   border: 'border-green-200',   text: 'text-green-700',   dot: 'bg-green-400' }
      : lower.includes('intermédiaire')
      ? { bg: 'bg-amber-50',   border: 'border-amber-200',   text: 'text-amber-700',   dot: 'bg-amber-400' }
      : { bg: 'bg-rose-50',    border: 'border-rose-200',    text: 'text-rose-700',    dot: 'bg-rose-400' };
    return (
      <div key={key} className={`inline-flex items-center gap-1.5 my-1 px-2.5 py-1 border rounded-full ${cfg.bg} ${cfg.border}`}>
        <span className={`w-1.5 h-1.5 rounded-full ${cfg.dot}`} />
        <span className={`text-xs font-medium ${cfg.text}`}>Niveau : {label}</span>
      </div>
    );
  }

  if (line.startsWith('Sous-catégorie :')) {
    const label = line.slice('Sous-catégorie :'.length).trim();
    return (
      <div key={key} className="flex items-center gap-1.5 my-1 px-2.5 py-1 bg-violet-50 border border-violet-200 rounded-lg">
        <AlignLeft className="w-3 h-3 text-violet-400 flex-shrink-0" />
        <span className="text-xs text-violet-700 leading-snug">
          <span className="font-semibold">Sous-catégorie : </span>{label}
        </span>
      </div>
    );
  }

  if (line.startsWith('Objectif :')) {
    const label = line.slice('Objectif :'.length).trim();
    return (
      <div key={key} className="flex items-start gap-1.5 my-1 px-2.5 py-1.5 bg-indigo-50 border border-indigo-200 rounded-lg">
        <ListChecks className="w-3.5 h-3.5 text-indigo-500 flex-shrink-0 mt-0.5" />
        <span className="text-xs text-indigo-700 leading-snug">
          <span className="font-semibold">Objectif : </span>{label}
        </span>
      </div>
    );
  }

  const isQuote = line.startsWith('> ');
  const content = isQuote ? line.slice(2) : line;

  // Split on **bold** markers
  const parts = content.split(/(\*\*[^*]+\*\*)/);
  const nodes = parts.map((p, i) =>
    p.startsWith('**') && p.endsWith('**')
      ? <strong key={i}>{p.slice(2, -2)}</strong>
      : p
  );

  if (isQuote) {
    return (
      <div key={key} className="border-l-4 border-indigo-300 pl-3 my-1 text-gray-700 italic">
        {nodes}
      </div>
    );
  }
  if (line === '') return <div key={key} className="h-2" />;
  return <p key={key} className="my-0.5">{nodes}</p>;
}

function MessageContent({ text }) {
  return (
    <div className="text-sm leading-relaxed">
      {text.split('\n')
        .filter(line => !/^\s*\*\*\[[A-Z+>]\]\*\*/.test(line))
        .filter(line => !/^ORTHO:/i.test(line.trim()))
        .filter(line => !/^SYNTAXE:/i.test(line.trim()))
        .filter(line => !/^IDEAL:/i.test(line.trim()))
        .map((line, i) => renderLine(line, i))}
    </div>
  );
}

// ---------------------------------------------------------------------------
// ChatBubble
// ---------------------------------------------------------------------------
function ChatBubble({ msg, isStreaming }) {
  const isUser = msg.role === 'user';
  return (
    <div className={`flex items-end gap-2 mb-3 animate-fade-in ${isUser ? 'flex-row-reverse' : ''}`}>
      {!isUser && (
        <div className="w-8 h-8 rounded-full bg-indigo-100 flex items-center justify-center flex-shrink-0">
          <GraduationCap className="w-4 h-4 text-indigo-600" />
        </div>
      )}
      <div
        className={`max-w-[82%] px-4 py-3 rounded-2xl text-sm leading-relaxed ${
          isUser
            ? 'bg-indigo-600 text-white rounded-br-sm'
            : `bg-white border border-gray-100 shadow-sm rounded-bl-sm ${isStreaming ? 'opacity-90' : ''}`
        }`}
      >
        {isUser
          ? <p className="whitespace-pre-wrap">{msg.content}</p>
          : <MessageContent text={msg.content} />
        }
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Typing indicator
// ---------------------------------------------------------------------------
function TypingIndicator() {
  return (
    <div className="flex items-end gap-2 mb-3">
      <div className="w-8 h-8 rounded-full bg-indigo-100 flex items-center justify-center flex-shrink-0">
        <GraduationCap className="w-4 h-4 text-indigo-600" />
      </div>
      <div className="bg-white border border-gray-100 shadow-sm rounded-2xl rounded-bl-sm px-4 py-3">
        <div className="flex items-center gap-2">
          <div className="flex gap-1 items-center">
            {[0, 1, 2].map((i) => (
              <div
                key={i}
                className="w-2 h-2 bg-indigo-400 rounded-full animate-bounce"
                style={{ animationDelay: `${i * 0.15}s` }}
              />
            ))}
          </div>
          <span className="text-xs text-indigo-400 italic">En train d'écrire…</span>
        </div>
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Quick-reply buttons
// ---------------------------------------------------------------------------
const OPTION_LABELS = {
  S: 'Voir la synthèse du cours',
  P: 'Je maîtrise déjà',
  O: 'Question suivante',
  N: 'Réessayer',
  R: 'Voir la réponse idéale',
  M: 'Reconstituer la réponse',
  A: 'Conseil argumentation',
  C: 'Commencer les exercices',
  Q: 'Quitter',
  D: 'Définir les mots clés',
  '+': 'Continuer sur ce thème',
  '>': 'Thème suivant',
  '1': 'Version intermédiaire',
};

function QuickReplies({ options, onSelect, color = 'indigo' }) {
  if (!options.length) return null;
  const cls = color === 'emerald'
    ? 'bg-emerald-50 border-emerald-200 text-emerald-700 hover:bg-emerald-100 active:bg-emerald-200'
    : 'bg-indigo-50 border-indigo-200 text-indigo-700 hover:bg-indigo-100 active:bg-indigo-200';
  return (
    <div className="flex flex-wrap gap-2 px-4 pt-1 pb-3">
      {options.map((opt) => (
        <button
          key={opt}
          onClick={() => onSelect(`[${opt}]`)}
          className={`px-3 py-1.5 border rounded-full text-xs font-semibold transition-all ${cls}`}
        >
          {OPTION_LABELS[opt] ?? `[${opt}]`}
        </button>
      ))}
    </div>
  );
}

// ---------------------------------------------------------------------------
// Error banner
// ---------------------------------------------------------------------------
function ErrorBanner({ message, onRetry }) {
  return (
    <div className="mx-4 my-2 flex items-center gap-3 bg-red-50 border border-red-200 rounded-xl px-4 py-3">
      <AlertCircle className="w-4 h-4 text-red-500 flex-shrink-0" />
      <p className="text-sm text-red-700 flex-1">{message}</p>
      {onRetry && (
        <button onClick={onRetry} className="text-xs text-red-600 underline">
          Réessayer
        </button>
      )}
    </div>
  );
}

// ---------------------------------------------------------------------------
// SyntheseModal — popup triggered by [S] button
// ---------------------------------------------------------------------------
function SyntheseModal({ content, loading, onClose }) {
  return (
    <div className="fixed inset-0 z-50 flex items-end justify-center bg-black/40 backdrop-blur-sm p-4">
      <div className="w-full max-w-lg bg-white rounded-3xl shadow-2xl flex flex-col max-h-[80vh]">
        <div className="flex items-center justify-between px-5 py-4 border-b border-gray-100 flex-shrink-0">
          <div className="flex items-center gap-2">
            <BookOpen className="w-4 h-4 text-indigo-600" />
            <h3 className="font-bold text-gray-900 text-sm">Synthèse du cours</h3>
          </div>
          {!loading && (
            <button onClick={onClose} className="text-gray-400 hover:text-gray-600 transition-colors">
              <X className="w-5 h-5" />
            </button>
          )}
        </div>
        <div className="flex-1 overflow-y-auto px-5 py-4">
          {loading && !content && <TypingIndicator />}
          {content && <MessageContent text={content} />}
          {loading && content && (
            <div className="flex gap-1 mt-2">
              {[0, 1, 2].map(i => (
                <div key={i} className="w-1.5 h-1.5 bg-indigo-400 rounded-full animate-bounce" style={{ animationDelay: `${i * 0.15}s` }} />
              ))}
            </div>
          )}
        </div>
        {!loading && (
          <div className="px-5 py-4 border-t border-gray-100 flex-shrink-0">
            <button
              onClick={onClose}
              className="w-full py-2.5 bg-indigo-600 text-white rounded-xl font-semibold hover:bg-indigo-700 active:bg-indigo-800 transition-all text-sm"
            >
              Fermer et revenir à l'exercice
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// PaywallModal — shown after FREE_QUESTION_LIMIT questions
// ---------------------------------------------------------------------------
const FREE_QUESTION_LIMIT = 10;
const CONTACT_EMAIL       = 'mohamed.necib94310@gmail.com';
const CRPE_PRICE_LABEL    = '399,00 €'; // doit rester aligné avec CRPE_PRICE dans app.js

const PAYPAL_NCP_URL = 'https://www.paypal.com/ncp/payment/NZPAQVSVRHYLL';

function PaywallModal({ questionsUsed, onUnlock, onClose }) {
  const [checking, setChecking] = useState(false);
  const [checkMsg, setCheckMsg] = useState(null);

  const FEATURES = [
    { icon: '📚', text: 'Questions illimitées — toutes thématiques (grammaire, lecture, vocabulaire, écriture, culture littéraire)' },
    { icon: '🎯', text: 'Niveaux facile et intermédiaire débloqués dès que vous êtes prêt' },
    { icon: '🤖', text: 'Correction IA personnalisée après chaque réponse : note écriture, orthographe et niveau CRPE' },
    { icon: '📖', text: 'Synthèse de cours et définitions des mots clés pour chaque exercice' },
    { icon: '📊', text: 'Historique complet et statistiques de progression par thématique' },
  ];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4 overflow-y-auto" onClick={onClose ? (e => { if (e.target === e.currentTarget) onClose(); }) : undefined}>
      <div className="w-full max-w-sm bg-white rounded-3xl shadow-2xl mb-2 mt-4 overflow-hidden">

        {/* Header */}
        <div className="bg-gradient-to-br from-indigo-600 to-indigo-500 px-5 pt-6 pb-5 text-white text-center relative">
          {onClose && (
            <button
              onClick={onClose}
              className="absolute top-3 right-3 w-7 h-7 flex items-center justify-center rounded-full bg-white/20 text-white hover:bg-white/30 transition-all text-sm font-bold"
              aria-label="Fermer"
            >
              ✕
            </button>
          )}
          <div className="w-14 h-14 bg-white/20 rounded-2xl flex items-center justify-center mx-auto mb-3">
            <GraduationCap className="w-7 h-7 text-white" />
          </div>
          <h2 className="text-lg font-bold leading-tight">Débloquez l'accès complet</h2>
          <p className="text-indigo-200 text-xs mt-1.5 leading-snug">
            Vous avez utilisé vos {FREE_QUESTION_LIMIT} questions d'essai gratuites.
          </p>
        </div>

        <div className="px-5 py-5 space-y-4">

          {/* Ce que vous obtenez */}
          <div>
            <p className="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-2.5">
              Ce que vous obtenez avec l'accès complet
            </p>
            <div className="space-y-2">
              {FEATURES.map((f, i) => (
                <div key={i} className="flex items-start gap-2.5">
                  <span className="text-base leading-none mt-0.5 flex-shrink-0">{f.icon}</span>
                  <p className="text-xs text-gray-700 leading-snug">{f.text}</p>
                </div>
              ))}
            </div>
          </div>

          {/* Séparateur */}
          <div className="h-px bg-gray-100" />

          {/* Prix */}
          <div className="flex items-center justify-between">
            <span className="text-sm font-semibold text-gray-700">Accès complet — paiement unique</span>
            <span className="text-lg font-bold text-indigo-600">{CRPE_PRICE_LABEL}</span>
          </div>

          {/* Bouton PayPal */}
          <a
            href={PAYPAL_NCP_URL}
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center justify-center gap-2 w-full bg-[#0070ba] hover:bg-[#003087] text-white font-bold py-3 rounded-xl transition-colors text-sm"
          >
            <svg viewBox="0 0 24 24" className="w-5 h-5 fill-current" xmlns="http://www.w3.org/2000/svg">
              <path d="M7.076 21.337H2.47a.641.641 0 0 1-.633-.74L4.944.901C5.026.382 5.474 0 5.998 0h7.46c2.57 0 4.578.543 5.69 1.81 1.01 1.15 1.313 2.48 1.067 4.258-.569 4.01-3.19 6.231-7.073 6.231h-2.13c-.524 0-.968.382-1.05.9L9.076 18.56l-.405 2.338a.38.38 0 0 1-.376.32c0 .055.003.11.002.12h-1.22z"/>
              <path d="M20.502 5.093c-.057.36-.12.712-.2 1.054C19.25 11.026 16 13.174 11.54 13.174H9.41a1.04 1.04 0 0 0-1.027.88L7.19 21.337h3.885a.898.898 0 0 0 .886-.757l.036-.19.703-4.455.045-.246a.898.898 0 0 1 .886-.758h.558c3.612 0 6.44-1.467 7.265-5.71.346-1.78.167-3.265-.951-4.128z"/>
            </svg>
            Payer avec PayPal — {CRPE_PRICE_LABEL}
          </a>

          {/* Vérifier après paiement */}
          <div className="text-center">
            <button
              onClick={async () => {
                setChecking(true);
                setCheckMsg(null);
                const paid = await fetchPaidStatus();
                if (paid) {
                  storage.set('crpe_paid', true);
                  onUnlock();
                } else {
                  setCheckMsg('Paiement non encore reçu. Attendez quelques secondes puis réessayez.');
                  setChecking(false);
                }
              }}
              disabled={checking}
              className="text-xs text-indigo-600 font-semibold hover:underline disabled:opacity-50"
            >
              {checking ? 'Vérification…' : 'J\'ai déjà payé — vérifier mon accès'}
            </button>
            {checkMsg && <p className="text-xs text-gray-500 mt-1">{checkMsg}</p>}
          </div>

          {/* Zone rassurante */}
          <div className="border border-gray-200 rounded-2xl px-4 py-4">
            <p className="text-sm font-bold text-gray-800 leading-snug">
              Pas encore prêt ?
            </p>
            <p className="text-xs text-gray-500 mt-1.5 leading-relaxed">
              Pas de pression. Si vous avez des doutes ou des questions, contactez-nous — nous répondons personnellement pour vous aider à faire le bon choix pour votre préparation.
            </p>
            <p className="mt-2.5 text-xs font-semibold text-gray-700">
              ✉️ contact@passcrpe.fr
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// ChatView
// ---------------------------------------------------------------------------
function ChatView({ matiere, profile, sessionKey, onNewSession, onBack, topic, niveau, mode }) {
  const [displayMessages, setDisplayMessages] = useState([]);
  const [apiMessages, setApiMessages] = useState([]);
  const [streamingText, setStreamingText] = useState('');
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [options, setOptions] = useState([]);
  const [awaitingStart, setAwaitingStart] = useState(false);
  const [synthese, setSynthese]       = useState({ open: false, content: '', loading: false, minimized: false });
  const [definitions, setDefinitions] = useState({ open: false, content: '', loading: false, minimized: false });
  const [puzzleData, setPuzzleData] = useState(null);
  const [aideData, setAideData] = useState(null);
  const [hoveredAideKw, setHoveredAideKw] = useState(null);
  const bottomRef = useRef(null);
  const inputRef = useRef(null);
  const prePuzzleOptionsRef  = useRef([]);
  const syntheseShownRef    = useRef(new Set());
  const definitionsShownRef = useRef(new Set());

  const [objectives, setObjectives] = useState([]);
  const [objectivesReady, setObjectivesReady] = useState(
    matiere !== 'francais' || mode === 'revision' || !topic || !niveau
  );

  const currentExerciseRef = useRef({ sous_categorie: null, objectif: null, question: null, ideal: null, texte: null });
  const tentativeRef       = useRef(1);
  const lastExerciceNumRef = useRef(0);
  const pendingResponseRef = useRef('');
  const lastOptionRef      = useRef(null);
  const sessionUuidRef     = useRef(null);
  const userId = useRef(storage.get('crpe_user_id') ?? `user_${uid()}`);

  const saveQuestion = (text) => {
    if (matiere !== 'francais' || mode === 'revision') return;
    const numMatch = text.match(/^Exercice\s+(\d+)/m);
    if (!numMatch) return;
    const exerciceNum = parseInt(numMatch[1]);
    const ex = extractExerciseData(text);
    currentExerciseRef.current = ex;
    if (exerciceNum > lastExerciceNumRef.current) {
      lastExerciceNumRef.current = exerciceNum;
      tentativeRef.current = 1;
      pendingResponseRef.current = '';
      supabaseInsert('questions_generees', {
        session_id:     sessionUuidRef.current || storeKey,
        niveau:         niveau || null,
        thematique:     topic || null,
        sous_categorie: ex.sous_categorie,
        objectif:       ex.objectif,
        question:       ex.question,
        texte_support:  ex.texte,
        reponse_ideale: null,
      });
    }
  };

  const saveFautesEtErreurs = (text, reponseId) => {
    if (matiere !== 'francais' || mode === 'revision') return;
    const ex = currentExerciseRef.current;
    const base = {
      user_id:                userId.current,
      session_id:             sessionUuidRef.current || storeKey,
      classe:                 niveau ? NIVEAU_TO_CLASSE[niveau] : null,
      thematique:             topic || null,
      sous_categorie:         ex.sous_categorie,
      objectif:               ex.objectif,
      id_reponse_utilisateur: reponseId,
      ma_reponse:             pendingResponseRef.current,
      question:               ex.question,
    };
    extractOrthoFautes(text).forEach(({ faute, correction }) => {
      supabaseInsert('fautes_orthographe', { ...base, faute, correction });
    });
    extractSyntaxeErreurs(text).forEach(({ erreur, correction }) => {
      supabaseInsert('erreurs_syntaxe', { ...base, erreur, correction });
    });
  };

  const saveResponseAfterCorrection = (correctionText) => {
    if (!pendingResponseRef.current) return;
    if (matiere !== 'francais' || mode === 'revision') return;

    const isEcriture = mode === 'ecriture';

    if (isEcriture) {
      // Mode écriture : note au format "Note : X/10" (pas de "Note globale")
      if (!/^Note\s*:\s*\d+\s*\/\s*10/m.test(correctionText)) return;

      // La réponse idéale en mode écriture passe uniquement par [R] (capturée dans onDone via lastOptionRef)
      tentativeRef.current += 1;
      pendingResponseRef.current = '';
      return;
    }

    // Mode francais standard
    if (!/^Note\s+globale\s*:/m.test(correctionText)) return;
    const notes = extractNotesFromText(correctionText);
    const ex = currentExerciseRef.current;
    const idealResponse = extractReponseTypeCRPE(correctionText) || null;
    const conseils = extractConseils(correctionText);
    const sessionId = sessionUuidRef.current || storeKey;
    const _ne = notes.ecriture ?? null, _no = notes.orthographe ?? null, _nc = notes.crpe ?? null;
    const _ngVals = [_ne, _no, _nc].filter(v => v != null);
    const noteFields = {
      note_ecriture:    _ne,
      note_orthographe: _no,
      note_crpe:        _nc,
      note_globale:     _ngVals.length ? Math.round((_ngVals.reduce((a, b) => a + b, 0) / _ngVals.length) * 10) / 10 : null,
    };

    const reponseRecord = {
      user_id:        userId.current,
      session_id:     sessionId,
      classe:         niveau ? NIVEAU_TO_CLASSE[niveau] : null,
      thematique:     topic || null,
      sous_categorie: ex.sous_categorie,
      objectif:       ex.objectif,
      question:       ex.question,
      texte_support:  ex.texte,
      reponse:        pendingResponseRef.current,
      reponse_ideale: idealResponse,
      conseils,
      ...noteFields,
      ...(tentativeRef.current === 2 ? { tentative: 2 } : {}),
    };
    supabaseInsertReturningId('reponses_utilisateurs', reponseRecord)
      .then(reponseId => saveFautesEtErreurs(correctionText, reponseId));

    if (idealResponse && ex.question) {
      supabasePatch('questions_generees', {
        session_id: sessionId,
        question:   ex.question,
      }, { reponse_ideale: idealResponse });
    }
    tentativeRef.current += 1;
    pendingResponseRef.current = '';
  };

  useEffect(() => {
    if (matiere !== 'francais' || mode === 'revision' || !topic || !niveau) {
      setObjectivesReady(true);
      return;
    }
    setObjectivesReady(false);
    fetchObjectives(topic, niveau).then(data => {
      setObjectives(data);
      setObjectivesReady(true);
    });
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  const revisionData = mode === 'revision' ? (storage.get('crpe_keywords') || []) : null;
  const systemPrompt = matiere === 'maths'
    ? getMathsPrompt(profile, niveau)
    : mode === 'revision'
      ? getFrancaisRevisionPrompt(profile, revisionData)
      : getFrancaisPrompt(profile, topic, niveau, mode, objectives);
  const storeKey = mode === 'revision' ? `crpe_session_${matiere}_revision` : `crpe_session_${matiere}`;

  // Scroll to bottom whenever messages or streaming text changes
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [displayMessages, streamingText, loading]);

  // Initialize: load saved session or show welcome screen for new sessions
  useEffect(() => {
    const saved = storage.get(storeKey);
    if (saved?.displayMessages?.length) {
      setAwaitingStart(false);
      setDisplayMessages(saved.displayMessages);
      setApiMessages(saved.apiMessages);
      setOptions(extractOptions(saved.displayMessages.at(-1)?.content ?? ''));
    } else {
      setAwaitingStart(true);
    }
  }, [sessionKey]); // eslint-disable-line react-hooks/exhaustive-deps

  const saveSession = (disp, api) => {
    storage.set(storeKey, { displayMessages: disp, apiMessages: api, savedAt: new Date().toISOString(), topic, niveau, mode });
  };

  const chatMeta = (typeEvenement) => ({
    user_id: userId.current,
    session_id: sessionUuidRef.current || storeKey,
    type_evenement: typeEvenement,
    matiere,
    thematique: topic || null,
  });

  const saveKeywords = (text) => {
    if (mode !== 'ecriture') return;
    const words = extractKeywords(text).map(k => k.word);
    const tournures = extractTournures(text).map(t => t.text);
    if (!words.length && !tournures.length) return;
    const existing = storage.get('crpe_keywords') || [];
    storage.set('crpe_keywords', [{ id: uid(), date: new Date().toISOString(), topic, niveau, words, tournures }, ...existing].slice(0, 200));
  };

  const initSession = async () => {
    sessionUuidRef.current = `sess_${uid()}`;
    lastExerciceNumRef.current = 0;
    syntheseShownRef.current    = new Set();
    definitionsShownRef.current = new Set();
    setDisplayMessages([]);
    setApiMessages([]);
    setOptions([]);
    setError(null);
    setLoading(true);
    setPuzzleData(null);
    setAideData(null);

    const trigger = mode === 'revision'
      ? { role: 'user', content: "Commence directement par l'exercice 1. Choisis un type parmi A, B, C ou D. Format : \"Exercice 1 — Type [lettre]\" sur une ligne, puis l'énoncé, puis **[S]** **[P]** seuls sur la dernière ligne. Aucun astérisque, aucun tiret en début de ligne, aucune ligne de séparation, pas de message d'accueil." }
      : mode === 'ecriture'
        ? { role: 'user', content: "Commence directement par l'exercice 1. Respecte exactement le format défini dans tes instructions : Exercice N - Sous-thème, Question, Consigne, Réponse incorrecte, puis **[A]** **[M]** **[S]** seuls sur la dernière ligne. Aucun astérisque dans le texte, aucun tiret en début de ligne, aucune ligne de séparation, pas de message d'accueil." }
        : { role: 'user', content: "Commence directement par l'exercice 1, au niveau de difficulté Très facile (début de progression). Format strict : ligne 1 \"Exercice N - Sous-thème\", ligne 2 \"Niveau de difficulté : Très facile\", ligne 3 \"Sous-catégorie : [nom exact]\", ligne 4 \"Objectif : [libellé exact]\", ligne 5 \"IDEAL: [réponse type CRPE en 3-5 phrases]\", puis ligne vide, puis instruction courte si nécessaire, texte support entre guillemets français si nécessaire, \"Question :\" suivi de la question, puis **[S]** **[P]** **[D]** seuls sur la dernière ligne. Aucun caractère —, aucun astérisque dans le texte, aucun tiret en début de ligne, aucune ligne de séparation, pas d'annonce de thème, pas de message d'accueil. Choisis l'objectif de façon aléatoire." };
    try {
      let text = '';
      await streamClaude(
        [trigger],
        systemPrompt,
        (chunk) => { setStreamingText(chunk); text = chunk; },
        (final) => {
          const assistantMsg = { role: 'assistant', content: final };
          const newApi = [trigger, assistantMsg];
          setApiMessages(newApi);
          setDisplayMessages([assistantMsg]);
          setStreamingText('');
          setOptions(extractOptions(final));
          saveSession([assistantMsg], newApi);
          saveKeywords(final);
          saveQuestion(final);
          text = final;
        },
        chatMeta('chat_exercice')
      );
    } catch (e) {
      setError(e.message);
    }
    setLoading(false);
    setTimeout(() => inputRef.current?.focus(), 100);
  };

  const saveSynthese = (text) => {
    if (matiere !== 'francais' || mode === 'revision' || !text?.trim()) return;
    const ex = currentExerciseRef.current;
    supabaseInsert('syntheses_cours', {
      user_id:        userId.current,
      session_id:     sessionUuidRef.current || storeKey,
      sous_categorie: ex.sous_categorie,
      objectif:       ex.objectif,
      synthese:       text.trim(),
    });
  };

  const openDefinitions = async () => {
    if (synthese.open) setSynthese(s => ({ ...s, minimized: true }));
    setDefinitions({ open: true, content: '', loading: true, minimized: false });
    const userMsg = { role: 'user', content: '[D]' };
    const newApi = [...apiMessages, userMsg];
    setApiMessages(newApi);
    try {
      await streamClaude(
        newApi,
        systemPrompt,
        (chunk) => setDefinitions(s => ({ ...s, content: chunk })),
        (final) => {
          const assistantMsg = { role: 'assistant', content: final };
          setApiMessages([...newApi, assistantMsg]);
          setDefinitions(s => ({ ...s, loading: false }));
        },
        chatMeta('chat_definitions')
      );
    } catch (e) {
      setDefinitions(s => ({ ...s, loading: false, content: `Erreur : ${e.message}` }));
    }
  };

  const openSynthese = async () => {
    setSynthese({ open: true, content: '', loading: true, minimized: false });
    const userMsg = { role: 'user', content: '[S]' };
    const newApi = [...apiMessages, userMsg];
    setApiMessages(newApi);
    try {
      await streamClaude(
        newApi,
        systemPrompt,
        (chunk) => setSynthese(s => ({ ...s, content: chunk })),
        (final) => {
          const assistantMsg = { role: 'assistant', content: final };
          setApiMessages([...newApi, assistantMsg]);
          setSynthese(s => ({ ...s, loading: false }));
          saveSynthese(final);
        },
        chatMeta('chat_synthese')
      );
    } catch (e) {
      setSynthese(s => ({ ...s, loading: false, content: `Erreur : ${e.message}` }));
    }
  };

  const send = async (text) => {
    if (!text.trim() || loading) return;
    const content = text.trim();

    if (content === '[S]') { syntheseShownRef.current.add(lastExerciceNumRef.current); openSynthese(); return; }
    if (content === '[D]') { definitionsShownRef.current.add(`${lastExerciceNumRef.current}_${tentativeRef.current}`); openDefinitions(); return; }

    const currentOptions = options;
    setInput('');
    setOptions([]);
    setError(null);
    setPuzzleData(null);
    setAideData(null);

    const userMsg = { role: 'user', content };
    const newDisplay = [...displayMessages, userMsg];
    const newApi = [...apiMessages, userMsg];
    setDisplayMessages(newDisplay);
    setApiMessages(newApi);
    if (!/^\[[A-Z+>]\]$/.test(content.trim())) {
      pendingResponseRef.current = content.trim();
      lastOptionRef.current = null;
    } else {
      lastOptionRef.current = content.trim()[1]; // e.g. 'R', 'O', 'N'…
    }
    setLoading(true);

    try {
      let response = '';
      await streamClaude(
        newApi,
        systemPrompt,
        (chunk) => { setStreamingText(chunk); response = chunk; },
        (final) => {
          const assistantMsg = { role: 'assistant', content: final };
          const finalDisplay = [...newDisplay, assistantMsg];
          const finalApi = [...newApi, assistantMsg];
          setDisplayMessages(finalDisplay);
          setApiMessages(finalApi);
          setStreamingText('');
          setOptions(extractOptions(final));
          saveSession(finalDisplay, finalApi);
          saveKeywords(final);
          saveQuestion(final);
          saveResponseAfterCorrection(final);

          // Si l'utilisateur vient de cliquer [R], capturer la réponse idéale
          if (lastOptionRef.current === 'R') {
            const ex = currentExerciseRef.current;
            const sessionId = sessionUuidRef.current || storeKey;
            // Tenter d'extraire après "Réponse type CRPE :", sinon prendre tout sauf les boutons et les lignes d'intro
            const idealFromR =
              extractReponseTypeCRPE(final) ||
              final
                .split('\n')
                .filter(l => !/^\s*\*\*\[[A-Z+>]\]\*\*/.test(l))
                .filter(l => !/^voici\s+(un|une|la|le)\s+/i.test(l.trim()))
                .join('\n')
                .trim();
            if (idealFromR && ex.question) {
              supabasePatch('questions_generees', {
                session_id: sessionId,
                question:   ex.question,
              }, { reponse_ideale: idealFromR });
            }
            lastOptionRef.current = null;
          }

          if (mode === 'ecriture') {
            const puzzleMatch = final.match(/^PUZZLE_GAME:\s*(.+)$/m);
            if (puzzleMatch) {
              const segs = puzzleMatch[1].split('|').map(s => s.trim()).filter(Boolean);
              prePuzzleOptionsRef.current = currentOptions;
              setPuzzleData({ remaining: segs });
            } else {
              setPuzzleData(null);
            }
            const pisteMatch = final.match(/^AIDE_PISTE:\s*(.+)$/m);
            if (pisteMatch) {
              const kws = extractKeywords(final);
              const tours = extractTournures(final);
              setAideData({ keywords: kws, tournures: tours, piste: pisteMatch[1].trim() });
            } else {
              setAideData(null);
            }
          }
          response = final;
        },
        chatMeta('chat_reponse')
      );
    } catch (e) {
      setError(e.message);
    }
    setLoading(false);
    setTimeout(() => inputRef.current?.focus(), 100);
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      send(input);
    }
  };

  const matiereLabel = matiere === 'maths' ? 'Mathématiques' : 'Français';
  const badgeClass = matiere === 'maths'
    ? 'bg-emerald-100 text-emerald-700'
    : 'bg-indigo-100 text-indigo-700';

  const welcomeTopicLabel = matiere === 'maths'
    ? 'Mathématiques'
    : (FRANCAIS_TOPICS.find(t => t.id === topic)?.label || 'Français');

  return (
    <div className="flex flex-col flex-1 min-h-0">

      {/* Panneau synthèse — fixed à droite, hors du flux du chat */}
      {(synthese.open || definitions.open) && (
        <div className="fixed top-0 right-0 bottom-0 w-96 z-50 flex flex-col shadow-2xl">

          {/* Panneau — Synthèse du cours */}
          {synthese.open && (
            <div className={`flex flex-col bg-white border-l border-gray-200 transition-all ${synthese.minimized ? 'flex-shrink-0' : 'flex-1 min-h-0'}`}>
              <div className="flex items-center justify-between px-4 py-3 bg-indigo-600 flex-shrink-0">
                <div className="flex items-center gap-2">
                  <BookOpen className="w-4 h-4 text-white" />
                  <span className="text-sm font-semibold text-white">Synthèse du cours</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <button
                    onClick={() => setSynthese(s => ({ ...s, minimized: !s.minimized }))}
                    className="text-white/70 hover:text-white transition-colors"
                    title={synthese.minimized ? 'Agrandir' : 'Réduire'}
                  >
                    {synthese.minimized ? <ChevronDown className="w-4 h-4" /> : <ChevronUp className="w-4 h-4" />}
                  </button>
                  <button
                    onClick={() => setSynthese({ open: false, content: '', loading: false, minimized: false })}
                    className="text-white/70 hover:text-white transition-colors"
                    title="Fermer"
                  >
                    <X className="w-4 h-4" />
                  </button>
                </div>
              </div>
              {!synthese.minimized && (
                <div className="flex-1 overflow-y-auto px-5 py-4 text-sm">
                  {synthese.loading && <TypingIndicator />}
                  {!synthese.loading && synthese.content && <MessageContent text={synthese.content} />}
                </div>
              )}
            </div>
          )}

          {/* Panneau — Définitions des mots clés */}
          {definitions.open && (
            <div className={`flex flex-col bg-white border-l border-gray-200 transition-all ${definitions.minimized ? 'flex-shrink-0' : 'flex-1 min-h-0'} ${synthese.open ? 'border-t-2 border-t-violet-200' : ''}`}>
              <div className="flex items-center justify-between px-4 py-3 bg-violet-600 flex-shrink-0">
                <div className="flex items-center gap-2">
                  <ListChecks className="w-4 h-4 text-white" />
                  <span className="text-sm font-semibold text-white">Définitions des mots clés</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <button
                    onClick={() => setDefinitions(d => ({ ...d, minimized: !d.minimized }))}
                    className="text-white/70 hover:text-white transition-colors"
                    title={definitions.minimized ? 'Agrandir' : 'Réduire'}
                  >
                    {definitions.minimized ? <ChevronDown className="w-4 h-4" /> : <ChevronUp className="w-4 h-4" />}
                  </button>
                  <button
                    onClick={() => setDefinitions({ open: false, content: '', loading: false, minimized: false })}
                    className="text-white/70 hover:text-white transition-colors"
                    title="Fermer"
                  >
                    <X className="w-4 h-4" />
                  </button>
                </div>
              </div>
              {!definitions.minimized && (
                <div className="flex-1 overflow-y-auto px-5 py-4 text-sm">
                  {definitions.loading && <TypingIndicator />}
                  {!definitions.loading && definitions.content && <MessageContent text={definitions.content} />}
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {/* Header */}
      <div className="flex items-center justify-between px-4 py-3 border-b border-gray-100 bg-white flex-shrink-0">
        <div className="flex items-center gap-3 min-w-0">
          <button
            onClick={onBack}
            className="text-gray-400 hover:text-gray-600 transition-colors flex-shrink-0"
          >
            <ChevronLeft className="w-5 h-5" />
          </button>
          <div className="flex flex-col min-w-0">
            <div className="flex items-center gap-1.5 flex-wrap">
              <span className={`text-xs font-semibold px-2 py-0.5 rounded-full self-start ${badgeClass}`}>
                {matiereLabel}
              </span>
              {mode === 'ecriture' && (
                <span className="text-xs font-semibold px-2 py-0.5 rounded-full self-start bg-rose-100 text-rose-600">
                  Apprendre à rédiger
                </span>
              )}
              {mode === 'revision' && (
                <span className="text-xs font-semibold px-2 py-0.5 rounded-full self-start bg-amber-100 text-amber-700">
                  Révision
                </span>
              )}
            </div>
            {(welcomeTopicLabel !== matiereLabel || niveau) && (
              <p className="text-xs text-gray-400 mt-1 truncate">
                {welcomeTopicLabel !== matiereLabel ? welcomeTopicLabel : matiereLabel}
                {niveau && <span className="ml-1 text-gray-300">·</span>}
                {niveau && <span className="ml-1">{getNiveauLabel(niveau)}</span>}
                <span className="ml-1 text-gray-300">·</span>
                <span className="ml-1 font-medium text-gray-500">Cycle 4</span>
              </p>
            )}
          </div>
        </div>
        <button
          onClick={onNewSession}
          className="flex items-center gap-1 text-xs text-gray-400 hover:text-gray-600 transition-colors flex-shrink-0 ml-3"
        >
          <RotateCcw className="w-3 h-3" /> Nouvelle session
        </button>
      </div>

      {/* Content area: chat + aide panel */}
      <div className="flex flex-row flex-1 min-h-0">

        {/* Chat column */}
        <div className="flex flex-col flex-1 min-h-0">
          <div className="flex-1 overflow-y-auto px-4 pt-4 pb-2">
            {awaitingStart ? (
              <>
                <ChatBubble msg={{
                  role: 'assistant',
                  content: mode === 'ecriture'
                    ? `Bienvenue dans **Apprendre à rédiger** — ${welcomeTopicLabel}${niveau ? ` · ${getNiveauLabel(niveau)}` : ''}.\n\nPour chaque exercice, une réponse correcte sur le fond mais **mal formulée** vous est présentée. Votre objectif : la reformuler en 3 à 5 phrases conformes aux attentes du CRPE.\n\nVous avez **3 options** :\n- Rédiger directement dans le champ ci-dessous\n- Demander une **aide** (mots clés et tournures)\n- Reconstituer la réponse en **mode puzzle guidé**\n\nUne note sur 10 vous est donnée après chaque rédaction. Vous avez **2 tentatives** par exercice.`
                      : mode === 'revision'
                        ? `Bienvenue dans **Révision mots clés & tournures**.\n\nJe vais vous proposer des exercices variés pour mémoriser et réutiliser les mots clés et tournures de phrases travaillés dans vos sessions précédentes.\n\nChaque exercice propose un type différent : compléter une phrase, reformuler avec une tournure, employer un mot clé en contexte…`
                        : `Vous travaillez sur **${welcomeTopicLabel}**${niveau ? ` — **${getNiveauLabel(niveau)}**` : ''} — **Cycle 4**.\n\nVoici comment fonctionne la session :\n\n1. Une question est posée, avec un extrait d'un texte officiel si nécessaire.\n2. Vous rédigez votre réponse dans le champ ci-dessous.\n3. L'outil note votre production et vous donne des pistes pour l'améliorer.\n4. Vous pouvez proposer une deuxième réponse améliorée.\n5. À l'issue de votre second essai, une réponse type CRPE vous est proposée.\n\nPrêt·e à commencer ?`,
                }} />
                <div className="pl-11 mt-1 mb-2 flex flex-col gap-2">
                  {!objectivesReady && (
                    <p className="text-xs text-indigo-400 flex items-center gap-1.5">
                      <Loader2 className="w-3 h-3 animate-spin" />
                      Chargement du programme officiel…
                    </p>
                  )}
                  {objectivesReady && objectives.length > 0 && (
                    <p className="text-xs text-emerald-600 font-medium">
                      ✓ {objectives.length} objectif{objectives.length > 1 ? 's' : ''} officiel{objectives.length > 1 ? 's' : ''} chargé{objectives.length > 1 ? 's' : ''}
                    </p>
                  )}
                  <button
                    onClick={() => { setAwaitingStart(false); initSession(); }}
                    disabled={!objectivesReady}
                    className="bg-indigo-600 text-white rounded-xl px-5 py-2.5 text-sm font-semibold hover:bg-indigo-700 active:bg-indigo-800 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    Je suis prêt
                  </button>
                </div>
              </>
            ) : (
              <>
                {displayMessages.map((msg, i) => {
                  if (msg.role === 'user' && /^\[[A-Z+>]\]$/.test(msg.content.trim())) return null;
                  if (mode === 'ecriture' && msg.role === 'assistant') {
                    if (msg.content.includes('AIDE_PISTE:')) return null;
                    const stripped = stripEcritureLines(msg.content).trim();
                    if (!stripped) return null;
                    return <ChatBubble key={i} msg={{ ...msg, content: stripped }} />;
                  }
                  return <ChatBubble key={i} msg={msg} />;
                })}
                {loading && <TypingIndicator />}
                {error && (
                  <ErrorBanner
                    message={`Erreur : ${error}`}
                    onRetry={() => { setError(null); initSession(); }}
                  />
                )}
              </>
            )}
            <div ref={bottomRef} />
          </div>

          {/* Aide à la rédaction — bulle de chat assistant avec chips violet */}
          {aideData && (
            <div className="flex items-end gap-2 mb-3 px-4">
              <div className="w-8 h-8 rounded-full bg-indigo-100 flex items-center justify-center flex-shrink-0">
                <GraduationCap className="w-4 h-4 text-indigo-600" />
              </div>
              <div className="max-w-[82%] bg-white border border-gray-100 shadow-sm rounded-2xl rounded-bl-sm px-4 py-3 space-y-3">

                {/* Consigne */}
                <p className="text-xs text-gray-400 italic leading-snug">
                  Cliquez sur un élément pour l'insérer dans votre réponse, puis complétez votre rédaction.
                </p>

                {/* Mots clés */}
                {aideData.keywords.length > 0 && (
                  <div className="space-y-1.5">
                    <p className="text-[9px] font-bold text-violet-500 uppercase tracking-widest">Mots clés à utiliser</p>
                    <div className="flex flex-wrap gap-1.5">
                      {aideData.keywords.map((kw, i) => (
                        <div key={i}>
                          <button
                            onMouseEnter={() => setHoveredAideKw(kw.def || null)}
                            onMouseLeave={() => setHoveredAideKw(null)}
                            onClick={() => send(kw.word)}
                            className="px-3 py-1.5 bg-violet-50 border border-violet-200 text-violet-700 rounded-full text-xs font-semibold hover:bg-violet-100 active:bg-violet-200 transition-all"
                          >
                            {kw.word}
                          </button>
                        </div>
                      ))}
                    </div>
                    <div className={`overflow-hidden transition-all duration-150 ${hoveredAideKw ? 'max-h-7' : 'max-h-0'}`}>
                      <p className="text-[10px] text-violet-500 italic">{hoveredAideKw || ''}</p>
                    </div>
                  </div>
                )}

                {/* Tournures */}
                {aideData.tournures.length > 0 && (
                  <div className="space-y-1.5">
                    <p className="text-[9px] font-bold text-teal-600 uppercase tracking-widest">Tournures de phrases</p>
                    <div className="flex flex-wrap gap-1.5">
                      {aideData.tournures.map((t, i) => (
                        <button
                          key={i}
                          onClick={() => send(t.text)}
                          className="px-3 py-1.5 bg-teal-50 border border-teal-200 text-teal-700 rounded-full text-xs font-semibold italic hover:bg-teal-100 active:bg-teal-200 transition-all"
                        >
                          {t.text}
                        </button>
                      ))}
                    </div>
                  </div>
                )}

                {/* Piste de structuration */}
                {aideData.piste && (
                  <div className="bg-violet-50 border border-violet-100 rounded-xl px-3 py-2.5">
                    <p className="text-[9px] font-bold text-violet-500 uppercase tracking-widest mb-1">Piste de structuration</p>
                    <p className="text-xs text-violet-900 leading-relaxed">{aideData.piste}</p>
                  </div>
                )}

              </div>
            </div>
          )}

          {/* Puzzle — segments à choisir dans l'ordre, clic pré-remplit l'input */}
          {puzzleData && puzzleData.remaining.length > 0 && (
            <div className="mx-4 mb-3 bg-indigo-50 border border-indigo-200 rounded-2xl overflow-hidden">
              <div className="bg-gradient-to-r from-indigo-500 to-violet-500 px-4 py-2.5 flex items-center justify-between">
                <div>
                  <p className="text-[10px] font-bold text-white uppercase tracking-widest">Mode puzzle</p>
                  <p className="text-[9px] text-white/60 mt-0.5">Choisissez un segment et expliquez votre choix</p>
                </div>
                <button
                  onClick={() => {
                    setInput('');
                    setPuzzleData(null);
                    if (prePuzzleOptionsRef.current.length) {
                      setOptions(prePuzzleOptionsRef.current);
                      prePuzzleOptionsRef.current = [];
                    }
                  }}
                  className="text-[10px] text-white/70 hover:text-white transition-colors flex-shrink-0 ml-3"
                >
                  ← Retour aux options
                </button>
              </div>
              <div className="p-3 space-y-1.5">
                {puzzleData.remaining.map((seg, i) => (
                  <button
                    key={i}
                    onClick={() => {
                      setInput(`Je choisis « ${seg} » — Raison : `);
                      inputRef.current?.focus();
                    }}
                    className="w-full text-left bg-white border border-gray-200 hover:border-indigo-400 hover:bg-indigo-50 text-gray-700 text-xs px-3 py-2.5 rounded-lg transition-all leading-relaxed font-medium"
                  >
                    {seg}
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Quick replies */}
          {!awaitingStart && !loading && (
            <QuickReplies
              options={(aideData ? options.filter(o => o !== 'A') : options)
                .filter(o => o !== 'S' || !syntheseShownRef.current.has(lastExerciceNumRef.current))
                .filter(o => o !== 'D' || !definitionsShownRef.current.has(`${lastExerciceNumRef.current}_${tentativeRef.current}`))}
              onSelect={send}
            />
          )}

          {/* Input */}
          <div className="px-3 pt-2 border-t border-gray-100 bg-white flex-shrink-0" style={{ paddingBottom: 'calc(env(safe-area-inset-bottom, 0px) + 96px)' }}>
            <div className="flex gap-2 items-end">
              <textarea
                ref={inputRef}
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={handleKeyDown}
                placeholder="Votre réponse…"
                disabled={loading || awaitingStart}
                rows={4}
                className="flex-1 resize-none border border-gray-200 rounded-xl px-3 py-2.5 text-sm text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:border-transparent disabled:opacity-50 transition-all"
              />
              <button
                onClick={() => send(input)}
                disabled={!input.trim() || loading || awaitingStart}
                className="w-10 h-10 bg-indigo-600 text-white rounded-xl flex items-center justify-center hover:bg-indigo-700 active:bg-indigo-800 disabled:opacity-40 disabled:cursor-not-allowed transition-all flex-shrink-0"
              >
                {loading
                  ? <Loader2 className="w-4 h-4 animate-spin" />
                  : <Send className="w-4 h-4" />
                }
              </button>
            </div>
          </div>
        </div>


      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// ProgressRow — single criterion bar for the progression panel
// ---------------------------------------------------------------------------
function ProgressRow({ label, current, target, met, formatVal }) {
  const pct = Math.min(current / target, 1);
  return (
    <div>
      <div className="flex justify-between items-center mb-0.5">
        <span className="text-[10px] text-gray-500">{label}</span>
        <span className={`text-[10px] font-semibold ${met ? 'text-emerald-600' : 'text-gray-500'}`}>
          {formatVal(current)}{met ? ' ✓' : ` → obj. ${formatVal(target)}`}
        </span>
      </div>
      <div className="h-1.5 bg-gray-100 rounded-full overflow-hidden">
        <div
          className={`h-full rounded-full transition-all duration-500 ${met ? 'bg-emerald-400' : 'bg-indigo-400'}`}
          style={{ width: `${pct * 100}%` }}
        />
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// HomeView
// ---------------------------------------------------------------------------
function HomeView({ profile, onStart, banqueSession, onResumeBanque, isLocked, freeQsUsed, onPaymentConfirmed }) {
  const mathsSession   = storage.get('crpe_session_maths');
  const francaisSession = storage.get('crpe_session_francais');
  const mathsSaved    = !!mathsSession?.displayMessages?.length;
  const francaisSaved = !!francaisSession?.displayMessages?.length;

  const mathsScores    = extractScores(mathsSession?.displayMessages);
  const francaisScores = extractScores(francaisSession?.displayMessages);

  const [francaisAvgs, setFrancaisAvgs] = useState(null);
  const [progression, setProgression]   = useState({ completedFacile: 0, avgGlobal: null, avgCrpe: null, unlocked: false });
  const [showPaywall, setShowPaywall]   = useState(false);

  useEffect(() => {
    const userId = storage.get('crpe_user_id');
    if (!userId) return;
    fetchProgressionStats(userId).then(stats => {
      setProgression(stats);
      if (stats.avgGlobal !== null || stats.avgEcriture !== null || stats.avgCrpe !== null) {
        setFrancaisAvgs({
          ecriture:    stats.avgEcriture,
          orthographe: stats.avgOrthographe,
          crpe:        stats.avgCrpe,
          globale:     stats.avgGlobal,
        });
      }
    });
  }, []);

  const hour = new Date().getHours();
  const greeting = hour < 12 ? 'Bonjour' : hour < 18 ? 'Bon après-midi' : 'Bonsoir';

  function SubjectCard({ matiere, label, icon: Icon, accentClass, saved, scores, avgs, banqueSession, onResumeBanque }) {
    const avg = avgScore(scores);

    const noteItems = [
      { label: 'Écriture',    val: avgs?.ecriture,    bg: 'bg-blue-50',    text: 'text-blue-700'              },
      { label: 'Orthographe', val: avgs?.orthographe, bg: 'bg-rose-50',    text: 'text-rose-700'              },
      { label: 'Niveau CRPE', val: avgs?.crpe,        bg: 'bg-amber-50',   text: 'text-amber-700'             },
      { label: 'Globale',     val: avgs?.globale,     bg: 'bg-emerald-50', text: 'text-emerald-700 font-bold' },
    ];
    const hasDetailedScores = avgs && noteItems.some(n => n.val !== null);

    return (
      <div className={`bg-white rounded-2xl border shadow-sm px-4 py-3.5 flex items-center gap-4 ${isLocked ? 'border-gray-200 opacity-75' : 'border-gray-100'}`}>
        {/* Icône */}
        <div className={`w-10 h-10 rounded-xl flex items-center justify-center flex-shrink-0 ${isLocked ? 'bg-gray-100' : accentClass.bg}`}>
          {isLocked
            ? <span className="text-lg">🔒</span>
            : <Icon className={`w-5 h-5 ${accentClass.icon}`} />
          }
        </div>

        {/* Titre + description */}
        <div className="flex-1 min-w-0">
          <h3 className="font-bold text-gray-900 text-sm leading-tight">{label}</h3>
          <p className="text-[11px] text-gray-400 leading-snug">
            {matiere === 'maths' ? 'Nombres, géométrie, fonctions…' : 'Grammaire, orthographe, texte…'}
          </p>
          {!isLocked && hasDetailedScores && (
            <div className="flex gap-1.5 mt-1.5 flex-wrap">
              {noteItems.filter(n => n.val !== null).map(({ label: lbl, val, bg, text }) => (
                <span key={lbl} className={`text-[10px] font-semibold px-2 py-0.5 rounded-full ${bg} ${text}`}>
                  {lbl} {val}/10
                </span>
              ))}
            </div>
          )}
          {!isLocked && !hasDetailedScores && avg !== null && (
            <span className={`inline-block mt-1 text-[11px] font-semibold px-2 py-0.5 rounded-full ${accentClass.bg} ${accentClass.icon}`}>
              Moy. {avg}/10
            </span>
          )}
          {isLocked && (
            <span className="inline-block mt-1 text-[10px] font-medium text-gray-400">
              Accès limité — essai terminé
            </span>
          )}
        </div>

        {/* Boutons */}
        {!isLocked && (
          <div className="flex flex-col gap-1.5 flex-shrink-0">
            {(saved || banqueSession) && (
              <button
                onClick={() => banqueSession && onResumeBanque ? onResumeBanque() : onStart(matiere, false)}
                className={`px-3 py-1.5 rounded-xl text-xs font-semibold border-2 ${accentClass.border} ${accentClass.text} hover:opacity-80 transition-all whitespace-nowrap`}
              >
                Reprendre
              </button>
            )}
            <button
              onClick={() => onStart(matiere, true)}
              className={`px-3 py-1.5 rounded-xl text-xs font-semibold text-white transition-all ${accentClass.btn} whitespace-nowrap`}
            >
              {saved || banqueSession ? 'Nouvelle session' : 'Commencer →'}
            </button>
          </div>
        )}
      </div>
    );
  }

  return (
    <div className="flex-1 flex flex-col overflow-y-auto px-4 pt-4 pb-20 gap-3">

      {/* Paywall popup */}
      {showPaywall && (
        <PaywallModal
          questionsUsed={freeQsUsed}
          onUnlock={() => { setShowPaywall(false); if (onPaymentConfirmed) onPaymentConfirmed(); }}
          onClose={() => setShowPaywall(false)}
        />
      )}

      {/* Header */}
      <div className="flex items-center justify-between flex-shrink-0">
        <div>
          <p className="text-gray-400 text-xs">{greeting},</p>
          <h1 className="text-xl font-bold text-gray-900 leading-tight">{profile.prenom} 👋</h1>
        </div>
        <span className="text-[10px] text-gray-400 bg-gray-100 rounded-full px-2.5 py-1 font-medium">
          {profile.concours}{profile.academie ? ` · ${profile.academie}` : ''}
        </span>
      </div>

      {/* Bannière */}
      <div className="bg-gradient-to-r from-indigo-600 to-indigo-500 rounded-2xl px-4 py-3 text-white flex-shrink-0">
        <h2 className="font-bold text-sm mb-0.5">Tuteur CRPE IA</h2>
        <p className="text-indigo-200 text-xs leading-snug">
          Programme cycle 4 complet, thème par thème, avec exercices progressifs.
        </p>
      </div>

      {/* CTA débloquer — visible uniquement quand essai terminé */}
      {isLocked && (
        <div className="flex-shrink-0">
          <button
            onClick={() => setShowPaywall(true)}
            className="w-full py-4 bg-indigo-600 text-white rounded-2xl font-bold text-sm hover:bg-indigo-700 active:bg-indigo-800 transition-all flex items-center justify-center gap-2 shadow-lg shadow-indigo-200"
          >
            <span className="text-base">🔓</span>
            Débloquer mon accès complet
          </button>
          <p className="text-[10px] text-gray-400 text-center mt-1.5">
            Vos {FREE_QUESTION_LIMIT} questions gratuites sont utilisées · Accès illimité pour continuer
          </p>
        </div>
      )}

      {/* Section matières */}
      <div className="flex-shrink-0">
        <p className="text-[10px] font-semibold text-gray-400 uppercase tracking-wide mb-2">
          {isLocked ? 'Accès limité' : 'Choisir une matière'}
        </p>
        <div className="flex flex-col gap-2.5">
          <SubjectCard
            matiere="francais"
            label="Français"
            icon={BookMarked}
            saved={francaisSaved}
            scores={francaisScores}
            avgs={francaisAvgs}
            banqueSession={banqueSession}
            onResumeBanque={onResumeBanque}
            accentClass={{
              bg: 'bg-indigo-100',
              icon: 'text-indigo-600',
              border: 'border-indigo-400',
              text: 'text-indigo-600',
              btn: 'bg-indigo-600 hover:bg-indigo-700',
            }}
          />
          <SubjectCard
            matiere="maths"
            label="Mathématiques"
            icon={Calculator}
            saved={mathsSaved}
            scores={mathsScores}
            accentClass={{
              bg: 'bg-emerald-100',
              icon: 'text-emerald-600',
              border: 'border-emerald-400',
              text: 'text-emerald-600',
              btn: 'bg-emerald-600 hover:bg-emerald-700',
            }}
          />
        </div>
      </div>

      {/* Progression vers le niveau intermédiaire */}
      {!isLocked && (
      <div className="flex-shrink-0">
        <p className="text-[10px] font-semibold text-gray-400 uppercase tracking-wide mb-2">Progression Français</p>
        {progression.unlocked ? (
          <div className="bg-emerald-50 rounded-2xl border border-emerald-200 px-4 py-3 flex items-center gap-3">
            <div className="w-8 h-8 rounded-xl bg-emerald-100 flex items-center justify-center flex-shrink-0">
              <GraduationCap className="w-4 h-4 text-emerald-600" />
            </div>
            <div>
              <p className="text-sm font-bold text-emerald-800">Niveau intermédiaire débloqué !</p>
              <p className="text-[10px] text-emerald-600 mt-0.5">Les questions intermédiaires sont maintenant disponibles.</p>
            </div>
          </div>
        ) : (
          <div className="bg-white rounded-2xl border border-gray-100 shadow-sm px-4 py-3 space-y-2.5">
            <div className="flex items-center gap-2 pb-1 border-b border-gray-50">
              <div className="w-6 h-6 rounded-lg bg-gray-100 flex items-center justify-center flex-shrink-0">
                <span className="text-xs">🔒</span>
              </div>
              <div>
                <p className="text-xs font-bold text-gray-700">Débloquer le niveau intermédiaire</p>
                <p className="text-[9px] text-gray-400">3 critères à remplir en Français</p>
              </div>
            </div>
            <ProgressRow
              label="Questions faciles (Français)"
              current={progression.completedFacile}
              target={100}
              met={progression.completedFacile > 100}
              formatVal={v => `${v}/100`}
            />
            <ProgressRow
              label="Moyenne globale"
              current={progression.avgGlobal ?? 0}
              target={7}
              met={(progression.avgGlobal ?? 0) >= 7}
              formatVal={v => v > 0 ? `${v}/10` : '—/10'}
            />
            <ProgressRow
              label="Moyenne CRPE"
              current={progression.avgCrpe ?? 0}
              target={8}
              met={(progression.avgCrpe ?? 0) >= 8}
              formatVal={v => v > 0 ? `${v}/10` : '—/10'}
            />
          </div>
        )}
      </div>
      )}

      {/* Examens blancs — à venir */}
      <div className="flex-shrink-0">
        <p className="text-[10px] font-semibold text-gray-400 uppercase tracking-wide mb-2">Bientôt disponible</p>
        <div className="space-y-2">
          <div className="bg-white rounded-2xl border border-dashed border-gray-200 px-4 py-3 flex items-center gap-3 opacity-60">
            <div className="w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 bg-violet-100">
              <ClipboardList className="w-4.5 h-4.5 text-violet-500" />
            </div>
            <div className="flex-1 min-w-0">
              <div className="flex items-center gap-2 mb-0.5">
                <h3 className="text-sm font-bold text-gray-900">Examens blancs</h3>
                <span className="text-[9px] font-semibold px-1.5 py-0.5 rounded-full bg-violet-100 text-violet-600 uppercase tracking-wide">À venir</span>
              </div>
              <p className="text-[11px] text-gray-400 leading-snug">Simulations complètes des épreuves CRPE en conditions réelles.</p>
            </div>
          </div>
          <div className="bg-white rounded-2xl border border-dashed border-gray-200 px-4 py-3 flex items-center gap-3 opacity-60">
            <div className="w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 bg-amber-100">
              <PenLine className="w-4.5 h-4.5 text-amber-500" />
            </div>
            <div className="flex-1 min-w-0">
              <div className="flex items-center gap-2 mb-0.5">
                <h3 className="text-sm font-bold text-gray-900">Écrire comme le CRPE</h3>
                <span className="text-[9px] font-semibold px-1.5 py-0.5 rounded-full bg-amber-100 text-amber-600 uppercase tracking-wide">À venir</span>
              </div>
              <p className="text-[11px] text-gray-400 leading-snug">Apprendre à rédiger une réponse dans le format et le style attendus par le jury du CRPE.</p>
            </div>
          </div>
        </div>
      </div>

    </div>
  );
}

// ---------------------------------------------------------------------------
// HistoryView
// ---------------------------------------------------------------------------

function EmptyState({ icon: Icon, title, subtitle }) {
  return (
    <div className="flex flex-col items-center justify-center py-16 text-center">
      <div className="w-16 h-16 rounded-full bg-gray-100 flex items-center justify-center mb-3">
        <Icon className="w-8 h-8 text-gray-300" />
      </div>
      <p className="text-gray-600 font-semibold">{title}</p>
      <p className="text-gray-400 text-sm mt-1">{subtitle}</p>
    </div>
  );
}

function HistoryView() {
  const [rows, setRows]         = useState([]);
  const [loading, setLoading]   = useState(true);
  const [expandedId, setExpandedId] = useState(null);

  useEffect(() => {
    const userId = storage.get('crpe_user_id');
    if (!userId || !SUPABASE_URL || !SUPABASE_KEY) { setLoading(false); return; }
    const params = new URLSearchParams({
      user_id: `eq.${userId}`,
      select: 'id,thematique,classe,objectif,sous_categorie,question,texte_support,reponse,reponse_ideale,conseils,note_ecriture,note_orthographe,note_crpe,created_at,tentative',
      order: 'created_at.desc',
    });
    fetch(`${SUPABASE_URL}/rest/v1/reponses_utilisateurs?${params}`, {
      headers: { apikey: SUPABASE_KEY, Authorization: `Bearer ${SUPABASE_KEY}` },
    })
      .then(r => r.json())
      .then(data => { if (Array.isArray(data)) setRows(data); setLoading(false); })
      .catch(() => setLoading(false));
  }, []);

  // Group by calendar day
  const byDay = [];
  // Regrouper les tentatives d'une même question dans un seul groupe
  const groupMap = new Map(); // key → { t1, t2, latestDate }
  rows.forEach(row => {
    const gKey = row.id_question_completee
      ? `q_${row.id_question_completee}_${row.session_id}`
      : `r_${row.session_id}_${row.question}`;
    if (!groupMap.has(gKey)) groupMap.set(gKey, { t1: null, t2: null, latestDate: row.created_at });
    const g = groupMap.get(gKey);
    if (row.tentative === 1) g.t1 = row; else g.t2 = row;
    if (row.created_at > g.latestDate) g.latestDate = row.created_at;
  });
  const groups = [...groupMap.values()].sort((a, b) => b.latestDate.localeCompare(a.latestDate));

  const dayMap = new Map();
  groups.forEach(g => {
    const d = new Date(g.latestDate);
    const key = d.toLocaleDateString('fr-FR', { weekday: 'long', day: '2-digit', month: 'long', year: 'numeric' });
    if (!dayMap.has(key)) { dayMap.set(key, []); byDay.push(key); }
    dayMap.get(key).push(g);
  });

  if (loading) return (
    <div className="flex-1 flex items-center justify-center">
      <Loader2 className="w-6 h-6 text-indigo-400 animate-spin" />
    </div>
  );

  if (!rows.length) return (
    <div className="flex-1 overflow-y-auto px-4 pt-6 pb-24">
      <h2 className="text-xl font-bold text-gray-900 mb-4">Historique</h2>
      <EmptyState icon={BookOpen} title="Aucune réponse enregistrée" subtitle="Complétez des exercices pour voir votre historique ici." />
    </div>
  );

  return (
    <div className="flex-1 overflow-y-auto px-4 pt-6 pb-24">
      <h2 className="text-xl font-bold text-gray-900 mb-4">Historique</h2>

      {byDay.map(day => (
        <div key={day} className="mb-5">
          <p className="text-[11px] font-semibold text-gray-400 uppercase tracking-wider mb-2 capitalize">{day}</p>

          {dayMap.get(day).map(g => {
            const ref  = g.t1 || g.t2;
            const topicLabel = FRANCAIS_TOPICS.find(t => t.id === ref.thematique)?.label || ref.thematique || 'Français';
            const gId  = ref.id;
            const isOpen = expandedId === gId;
            const time = new Date(g.latestDate).toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' });
            // Note affichée dans le header = meilleure tentative (ou la seule disponible)
            const bestRow = g.t2 || g.t1;
            const bVals = [bestRow.note_ecriture, bestRow.note_orthographe, bestRow.note_crpe].filter(v => v != null);
            const bestG = bVals.length ? Math.round(bVals.reduce((a, b) => a + b, 0) / bVals.length * 10) / 10 : null;

            const TentativeBlock = ({ row, label, color }) => {
              const vals = [row.note_ecriture, row.note_orthographe, row.note_crpe].filter(v => v != null);
              return (
                <div className={`rounded-xl border px-3 py-3 space-y-3 ${color}`}>
                  <p className="text-[10px] font-bold uppercase tracking-widest text-gray-400">{label}</p>
                  {row.reponse && (
                    <div>
                      <p className="text-[10px] font-semibold text-gray-400 mb-1">Ma réponse</p>
                      <p className="text-xs text-gray-600 leading-relaxed">{row.reponse}</p>
                    </div>
                  )}
                  {row.conseils && (
                    <div>
                      <p className="text-[10px] font-semibold text-indigo-600 mb-1">Conseils de l'IA</p>
                      <p className="text-xs text-indigo-900 leading-relaxed whitespace-pre-line">{row.conseils}</p>
                    </div>
                  )}
                  {row.reponse_ideale && (
                    <div>
                      <p className="text-[10px] font-semibold text-emerald-600 mb-1">Réponse type CRPE</p>
                      <p className="text-xs text-emerald-900 leading-relaxed">{row.reponse_ideale}</p>
                    </div>
                  )}
                  <div className="flex gap-1.5 flex-wrap pt-1 border-t border-gray-100">
                    {row.note_ecriture    != null && <span className="text-[10px] px-2 py-0.5 rounded-full bg-blue-50 text-blue-700 font-semibold">Écriture {row.note_ecriture}/10</span>}
                    {row.note_orthographe != null && <span className="text-[10px] px-2 py-0.5 rounded-full bg-rose-50 text-rose-700 font-semibold">Ortho. {row.note_orthographe}/10</span>}
                    {row.note_crpe        != null && <span className="text-[10px] px-2 py-0.5 rounded-full bg-amber-50 text-amber-700 font-semibold">CRPE {row.note_crpe}/10</span>}
                    {vals.length > 0 && <span className="text-[10px] px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 font-bold ml-auto">Moy. {Math.round(vals.reduce((a,b)=>a+b,0)/vals.length*10)/10}/10</span>}
                  </div>
                </div>
              );
            };

            return (
              <div key={gId} className="bg-white rounded-2xl border border-gray-100 shadow-sm mb-2 overflow-hidden">
                <button
                  onClick={() => setExpandedId(isOpen ? null : gId)}
                  className="w-full px-4 py-3 flex items-center gap-3 text-left hover:bg-gray-50 transition-colors"
                >
                  <div className="w-8 h-8 rounded-xl bg-indigo-100 flex items-center justify-center flex-shrink-0">
                    <BookMarked className="w-3.5 h-3.5 text-indigo-600" />
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-1.5 flex-wrap">
                      <span className="text-xs font-semibold text-gray-700">{topicLabel}</span>
                      {ref.classe && <><span className="text-gray-200">·</span><span className="text-xs text-gray-400">{ref.classe}</span></>}
                      <span className="text-gray-200">·</span><span className="text-xs text-gray-400">{time}</span>
                      {g.t2 && <span className="text-[10px] px-1.5 py-0.5 rounded-full bg-indigo-50 text-indigo-500 font-medium">2 tentatives</span>}
                    </div>
                    {ref.sous_categorie && <p className="text-[10px] text-indigo-500 font-medium mt-0.5 truncate">{ref.sous_categorie}</p>}
                    {ref.question && <p className="text-[10px] text-gray-400 mt-0.5 truncate">{ref.question}</p>}
                  </div>
                  <div className="flex flex-col items-end gap-1 flex-shrink-0 ml-2">
                    {bestG !== null && <span className="text-[10px] px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 font-bold whitespace-nowrap">{bestG}/10</span>}
                    {isOpen ? <ChevronUp className="w-4 h-4 text-gray-300" /> : <ChevronDown className="w-4 h-4 text-gray-300" />}
                  </div>
                </button>

                {isOpen && (
                  <div className="border-t border-gray-50 px-4 py-4 space-y-4">
                    {ref.texte_support && (
                      <div>
                        <p className="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-1.5">Texte support</p>
                        <div className="border-l-4 border-indigo-200 pl-3 text-xs text-gray-600 italic leading-relaxed">« {ref.texte_support} »</div>
                      </div>
                    )}
                    {ref.question && (
                      <div>
                        <p className="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-1.5">Question</p>
                        <p className="text-xs text-gray-800 font-medium leading-snug">{ref.question}</p>
                      </div>
                    )}
                    <div className="space-y-3">
                      {g.t1 && <TentativeBlock row={g.t1} label={g.t2 ? '1ʳᵉ tentative' : 'Ma réponse'} color="bg-gray-50 border-gray-100" />}
                      {g.t2 && <TentativeBlock row={g.t2} label="2ᵉ tentative" color="bg-indigo-50/40 border-indigo-100" />}
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      ))}
    </div>
  );
}

// ---------------------------------------------------------------------------
// MathBanqueView — math exercise bank with 5-thematic menu
// ---------------------------------------------------------------------------
function MathBanqueView({ onBack }) {
  const [step, setStep]                   = useState('thematique');
  const [selectedThematique, setSelectedThematique] = useState(null);
  const [exercises, setExercises]         = useState([]);
  const [loadingEx, setLoadingEx]         = useState(false);
  const [currentIdx, setCurrentIdx]       = useState(0);
  const [phase, setPhase]                 = useState('question');
  const [userAnswer, setUserAnswer]       = useState('');
  const [correction, setCorrection]       = useState('');
  const [streamingText, setStreamingText] = useState('');
  const [loading, setLoading]             = useState(false);
  const [synthese, setSynthese]     = useState({ open: false, content: '', minimized: false });
  const [definitions, setDefinitions] = useState({ open: false, content: '', minimized: false });
  const tentativeRef = useRef(1);
  const inputRef     = useRef(null);
  const bottomRef    = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [phase, correction, streamingText]);

  const ex = exercises[currentIdx];

  function getOptions() {
    if (!ex || phase === 'correcting' || phase === 'done') return [];
    const s = ex.synthese_cours        ? ['S'] : [];
    const d = ex.definition_mots_cles ? ['D'] : [];
    if (phase === 'question')  return ['R', ...s, ...d, 'O'];
    if (phase === 'answered')  return [...(tentativeRef.current === 1 ? ['N'] : []), 'R', ...s, ...d, 'O'];
    if (phase === 'revealed')  return [...s, ...d, 'O'];
    return [];
  }

  const handleOption = (optStr) => {
    const opt = optStr.replace(/[\[\]]/g, '');
    if (opt === 'R') { setPhase('revealed'); return; }
    if (opt === 'S') {
      if (ex?.synthese_cours) setSynthese({ open: true, content: ex.synthese_cours, minimized: false });
      return;
    }
    if (opt === 'D') {
      if (ex?.definition_mots_cles) setDefinitions({ open: true, content: ex.definition_mots_cles, minimized: false });
      return;
    }
    if (opt === 'N') {
      tentativeRef.current = 2;
      setPhase('question');
      setUserAnswer('');
      setCorrection('');
      setStreamingText('');
      setTimeout(() => inputRef.current?.focus(), 150);
      return;
    }
    if (opt === 'O') {
      if (currentIdx + 1 >= exercises.length) { setPhase('done'); return; }
      tentativeRef.current = 1;
      setCurrentIdx(i => i + 1);
      setPhase('question');
      setUserAnswer('');
      setCorrection('');
      setStreamingText('');
      setSynthese({ open: false, content: '', minimized: false });
      setDefinitions({ open: false, content: '', minimized: false });
      setTimeout(() => inputRef.current?.focus(), 150);
      return;
    }
  };

  const handleSubmit = async () => {
    if (!userAnswer.trim() || loading) return;
    const tentative = tentativeRef.current;
    setLoading(true);
    setPhase('correcting');
    setCorrection('');
    setStreamingText('');

    const prompt = `Tu es un correcteur expert en mathématiques pour le CRPE (cycle 4).

Thématique : ${ex.thematique}
Sous-catégorie : ${ex.sous_categorie}
Objectif : ${ex.objectif_apprentissage}
Niveau : ${ex.classe} — Facile

Énoncé :
${ex.enonce}

Question :
${ex.question}

Réponse attendue (ne pas divulguer directement, sert uniquement à évaluer) :
${ex.reponse_ideale}

Réponse du candidat (tentative ${tentative}) :
${userAnswer}

---

Fournis une correction structurée et bienveillante, sans astérisques ni tirets en début de ligne :

Sur le fond : [2-3 phrases : résultat correct ou non, démarche, erreurs de raisonnement ou de calcul]

Sur la forme : [1-2 phrases : rédaction de la démarche, notation, vocabulaire mathématique]

Note calcul : X/10
Note méthode : X/10
Note CRPE : X/10
Note globale : X/10

Réponse type CRPE :
[Correction complète avec toutes les étapes détaillées]`;

    try {
      await streamClaude(
        [{ role: 'user', content: prompt }],
        'Tu es un correcteur expert en mathématiques cycle 4 pour le CRPE. Sois précis, bienveillant et rigoureux.',
        (chunk) => setStreamingText(chunk),
        (final) => { setStreamingText(''); setCorrection(final); setPhase('answered'); },
      );
    } catch {
      setStreamingText('');
      setCorrection('Erreur lors de la correction. Vérifiez votre connexion.');
      setPhase('answered');
    }
    setLoading(false);
    setTimeout(() => inputRef.current?.focus(), 100);
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); handleSubmit(); }
  };

  // ── Step: thématique ──────────────────────────────────────────────────────
  if (step === 'thematique') {
    return (
      <div className="flex-1 overflow-y-auto px-4 pt-6 pb-24">
        <button onClick={onBack} className="flex items-center gap-1.5 text-gray-500 text-sm mb-6 hover:text-gray-700 transition-colors">
          <ChevronLeft className="w-4 h-4" />Retour
        </button>
        <div className="mb-6">
          <div className="w-12 h-12 rounded-xl bg-emerald-100 flex items-center justify-center mb-3">
            <Calculator className="w-6 h-6 text-emerald-600" />
          </div>
          <h1 className="text-2xl font-bold text-gray-900">Maths — Banque d'exercices</h1>
          <p className="text-gray-500 text-sm mt-1">Choisissez une thématique à travailler</p>
        </div>
        <div className="flex flex-col gap-3">
          {MATH_THEMATIQUES.map((th) => {
            const Icon = th.icon;
            return (
              <button key={th.id} onClick={() => { setSelectedThematique(th.label); setStep('classe'); }}
                className="w-full bg-white rounded-2xl border border-gray-100 shadow-sm p-4 flex items-center gap-4 hover:shadow-md active:scale-[0.98] transition-all text-left">
                <div className={`w-11 h-11 rounded-xl flex items-center justify-center flex-shrink-0 ${th.colors.bg}`}>
                  <Icon className={`w-5 h-5 ${th.colors.icon}`} />
                </div>
                <div className="flex-1 min-w-0">
                  <p className="font-semibold text-gray-900 text-sm leading-tight">{th.label}</p>
                  <p className="text-xs text-gray-400 mt-0.5">{th.description}</p>
                </div>
                <ChevronRight className="w-4 h-4 text-gray-300 flex-shrink-0" />
              </button>
            );
          })}
        </div>
      </div>
    );
  }

  // ── Step: classe ─────────────────────────────────────────────────────────
  if (step === 'classe') {
    return (
      <ClassPickerView
        onSelect={async (classeId) => {
          const classe = NIVEAU_TO_CLASSE[classeId];
          setLoadingEx(true);
          setStep('exercises');
          setCurrentIdx(0); setPhase('question');
          setUserAnswer(''); setCorrection(''); setStreamingText('');
          tentativeRef.current = 1;
          const data = await fetchExercicesMaths(selectedThematique, classe);
          setExercises(shuffleArray(data));
          setLoadingEx(false);
          setTimeout(() => inputRef.current?.focus(), 150);
        }}
        onBack={() => setStep('thematique')}
      />
    );
  }

  // ── Loading ──────────────────────────────────────────────────────────────
  if (loadingEx) {
    return (
      <div className="flex-1 flex items-center justify-center">
        <Loader2 className="w-8 h-8 text-emerald-500 animate-spin" />
      </div>
    );
  }

  // ── Empty / Done ─────────────────────────────────────────────────────────
  if (phase === 'done' || exercises.length === 0) {
    return (
      <div className="flex-1 flex flex-col items-center justify-center px-4 gap-4 text-center">
        <GraduationCap className="w-12 h-12 text-emerald-400" />
        <h2 className="text-xl font-bold text-gray-800">
          {exercises.length === 0 ? 'Aucun exercice disponible' : 'Série terminée !'}
        </h2>
        <p className="text-gray-500 text-sm">
          {exercises.length === 0
            ? 'Les exercices pour cette thématique arrivent bientôt.'
            : `Bravo ! ${exercises.length} exercice${exercises.length > 1 ? 's' : ''} complété${exercises.length > 1 ? 's' : ''}.`}
        </p>
        <button onClick={onBack} className="px-5 py-2.5 bg-emerald-600 text-white rounded-xl text-sm font-semibold hover:bg-emerald-700 transition-all">
          Retour au menu
        </button>
      </div>
    );
  }

  // ── Exercise view ────────────────────────────────────────────────────────
  const thInfo = MATH_THEMATIQUES.find(t => t.label === ex?.thematique);
  const opts   = getOptions();
  const inputDisabled = phase !== 'question' || loading;

  return (
    <div className="flex flex-col flex-1 min-h-0">

      {/* Panneaux latéraux synthèse + définitions */}
      {(synthese.open || definitions.open) && (
        <div className="fixed top-0 right-0 bottom-0 w-96 z-50 flex flex-col shadow-2xl">
          {synthese.open && (
            <div className={`flex flex-col bg-white border-l border-gray-200 transition-all ${synthese.minimized ? 'flex-shrink-0' : 'flex-1 min-h-0'}`}>
              <div className="flex items-center justify-between px-4 py-3 bg-indigo-600 flex-shrink-0">
                <div className="flex items-center gap-2">
                  <BookOpen className="w-4 h-4 text-white" />
                  <span className="text-sm font-semibold text-white">Synthèse du cours</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <button onClick={() => setSynthese(s => ({ ...s, minimized: !s.minimized }))} className="text-white/70 hover:text-white transition-colors">
                    {synthese.minimized ? <ChevronDown className="w-4 h-4" /> : <ChevronUp className="w-4 h-4" />}
                  </button>
                  <button onClick={() => setSynthese({ open: false, content: '', minimized: false })} className="text-white/70 hover:text-white transition-colors">
                    <X className="w-4 h-4" />
                  </button>
                </div>
              </div>
              {!synthese.minimized && (
                <div className="flex-1 overflow-y-auto px-5 py-4 text-sm">
                  <MessageContent text={synthese.content} />
                </div>
              )}
            </div>
          )}
          {definitions.open && (
            <div className={`flex flex-col bg-white border-l border-gray-200 transition-all ${definitions.minimized ? 'flex-shrink-0' : 'flex-1 min-h-0'} ${synthese.open ? 'border-t-2 border-t-violet-200' : ''}`}>
              <div className="flex items-center justify-between px-4 py-3 bg-violet-600 flex-shrink-0">
                <div className="flex items-center gap-2">
                  <ListChecks className="w-4 h-4 text-white" />
                  <span className="text-sm font-semibold text-white">Définitions des mots clés</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <button onClick={() => setDefinitions(d => ({ ...d, minimized: !d.minimized }))} className="text-white/70 hover:text-white transition-colors">
                    {definitions.minimized ? <ChevronDown className="w-4 h-4" /> : <ChevronUp className="w-4 h-4" />}
                  </button>
                  <button onClick={() => setDefinitions({ open: false, content: '', minimized: false })} className="text-white/70 hover:text-white transition-colors">
                    <X className="w-4 h-4" />
                  </button>
                </div>
              </div>
              {!definitions.minimized && (
                <div className="flex-1 overflow-y-auto px-5 py-4 text-sm">
                  <MessageContent text={definitions.content} />
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {/* Header */}
      <div className="flex items-center justify-between px-4 py-3 border-b border-gray-100 bg-white flex-shrink-0">
        <button onClick={onBack} className="text-gray-400 hover:text-gray-600 transition-colors flex-shrink-0">
          <ChevronLeft className="w-5 h-5" />
        </button>
        <div className="flex flex-col items-center min-w-0">
          <p className="text-xs font-semibold text-gray-900 truncate">{ex?.sous_categorie}</p>
          <p className="text-[10px] text-gray-400">{currentIdx + 1}/{exercises.length} · {ex?.classe}</p>
        </div>
        <div className="w-5" />
      </div>

      {/* Scrollable content */}
      <div className="flex-1 overflow-y-auto">

        {/* Exercise card */}
        <div className="mx-4 mt-4 bg-white rounded-2xl border border-gray-100 shadow-sm p-4">
          <div className="flex items-center gap-2 mb-3 flex-wrap">
            <span className={`text-[10px] font-semibold px-2 py-0.5 rounded-full ${thInfo?.colors.bg || 'bg-emerald-50'} ${thInfo?.colors.icon || 'text-emerald-700'}`}>
              Exercice {currentIdx + 1} · Facile
            </span>
            <span className="text-[10px] text-gray-400">{ex?.thematique}</span>
          </div>
          {ex?.enonce && (
            <p className="text-sm text-gray-700 leading-relaxed mb-3 whitespace-pre-wrap">{ex.enonce}</p>
          )}
          {ex?.figure_svg && (
            <div
              className="flex justify-center my-3 bg-gray-50 rounded-xl p-2 overflow-x-auto"
              dangerouslySetInnerHTML={{ __html: ex.figure_svg }}
            />
          )}
          <p className="text-sm font-semibold text-gray-900">{ex?.question}</p>
        </div>

        {/* Correction (streaming or final) */}
        {(phase === 'correcting' || phase === 'answered') && (
          <div className="mx-4 mt-3 bg-white rounded-2xl border border-gray-100 shadow-sm p-4">
            <p className="text-[10px] font-semibold text-gray-400 uppercase tracking-wide mb-3">Correction</p>
            {phase === 'correcting' && !streamingText && (
              <div className="flex items-center gap-2 text-gray-400 text-sm">
                <Loader2 className="w-4 h-4 animate-spin" />Correction en cours…
              </div>
            )}
            {(streamingText || correction) && (
              <MessageContent text={streamingText || correction} />
            )}
          </div>
        )}

        {/* Réponse idéale (after [R]) */}
        {phase === 'revealed' && (
          <div className="mx-4 mt-3 bg-indigo-50 rounded-2xl border border-indigo-100 p-4">
            <p className="text-[10px] font-semibold text-indigo-500 uppercase tracking-wide mb-3">Réponse type CRPE</p>
            <MessageContent text={ex?.reponse_ideale || ''} />
          </div>
        )}

        <div ref={bottomRef} className="h-4" />
      </div>

      {/* Quick-reply buttons */}
      {opts.length > 0 && (
        <QuickReplies options={opts} onSelect={handleOption} color="emerald" />
      )}

      {/* Input */}
      <div className="px-3 pt-2 border-t border-gray-100 bg-white flex-shrink-0" style={{ paddingBottom: 'calc(env(safe-area-inset-bottom, 0px) + 96px)' }}>
        <div className="flex gap-2 items-end">
          <textarea
            ref={inputRef}
            value={userAnswer}
            onChange={e => setUserAnswer(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder={inputDisabled ? '' : 'Votre réponse…'}
            disabled={inputDisabled}
            rows={4}
            className="flex-1 resize-none border border-gray-200 rounded-xl px-3 py-2.5 text-sm text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-400 focus:border-transparent disabled:opacity-50 transition-all"
          />
          <button
            onClick={handleSubmit}
            disabled={!userAnswer.trim() || inputDisabled}
            className="w-10 h-10 bg-emerald-600 text-white rounded-xl flex items-center justify-center hover:bg-emerald-700 active:bg-emerald-800 disabled:opacity-40 disabled:cursor-not-allowed transition-all flex-shrink-0"
          >
            {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : <Send className="w-4 h-4" />}
          </button>
        </div>
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// SubjectPickerView — choose a Français topic before starting a session
// ---------------------------------------------------------------------------
const TOPIC_ICONS = {
  lecture:     BookOpen,
  culture:     GraduationCap,
  ecriture:    PenLine,
  vocabulaire: AlignLeft,
  grammaire:   ListChecks,
};
const TOPIC_COLORS = {
  lecture:     { bg: 'bg-sky-100',    icon: 'text-sky-600'    },
  culture:     { bg: 'bg-purple-100', icon: 'text-purple-600' },
  ecriture:    { bg: 'bg-rose-100',   icon: 'text-rose-600'   },
  vocabulaire: { bg: 'bg-amber-100',  icon: 'text-amber-600'  },
  grammaire:   { bg: 'bg-teal-100',   icon: 'text-teal-600'   },
};

function SubjectPickerView({ onSelect, onBack }) {
  return (
    <div className="flex-1 overflow-y-auto px-4 pt-6 pb-24">
      <button
        onClick={onBack}
        className="flex items-center gap-1.5 text-gray-500 text-sm mb-6 hover:text-gray-700 transition-colors"
      >
        <ChevronLeft className="w-4 h-4" />
        Retour
      </button>

      <div className="mb-6">
        <div className="w-12 h-12 rounded-xl bg-indigo-100 flex items-center justify-center mb-3">
          <BookMarked className="w-6 h-6 text-indigo-600" />
        </div>
        <h1 className="text-2xl font-bold text-gray-900">Français</h1>
        <p className="text-gray-500 text-sm mt-1">Que souhaitez-vous réviser aujourd'hui ?</p>
      </div>

      <div className="flex flex-col gap-3">
        {FRANCAIS_TOPICS.map((topic) => {
          const Icon = TOPIC_ICONS[topic.id];
          const colors = TOPIC_COLORS[topic.id];
          return (
            <button
              key={topic.id}
              onClick={() => onSelect(topic.id)}
              className="w-full bg-white rounded-2xl border border-gray-100 shadow-sm p-4 flex items-center gap-4 hover:shadow-md active:scale-[0.98] transition-all text-left"
            >
              <div className={`w-11 h-11 rounded-xl flex items-center justify-center flex-shrink-0 ${colors.bg}`}>
                <Icon className={`w-5 h-5 ${colors.icon}`} />
              </div>
              <div className="flex-1 min-w-0">
                <p className="font-semibold text-gray-900 text-sm leading-tight">{topic.label}</p>
                <p className="text-xs text-gray-400 mt-0.5">{topic.description}</p>
              </div>
              <ChevronRight className="w-4 h-4 text-gray-300 flex-shrink-0" />
            </button>
          );
        })}
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// ClassPickerView — choose a class level (5ème / 4ème / 3ème)
// ---------------------------------------------------------------------------
const NIVEAU_COLORS = {
  '5eme': { bg: 'bg-emerald-100', icon: 'text-emerald-600' },
  '4eme': { bg: 'bg-amber-100',   icon: 'text-amber-600'   },
  '3eme': { bg: 'bg-rose-100',    icon: 'text-rose-600'    },
};

function ClassPickerView({ onSelect, onBack }) {
  return (
    <div className="flex-1 overflow-y-auto px-4 pt-6 pb-24">
      <button
        onClick={onBack}
        className="flex items-center gap-1.5 text-gray-500 text-sm mb-6 hover:text-gray-700 transition-colors"
      >
        <ChevronLeft className="w-4 h-4" />
        Retour
      </button>

      <div className="mb-6">
        <div className="w-12 h-12 rounded-xl bg-gray-100 flex items-center justify-center mb-3">
          <GraduationCap className="w-6 h-6 text-gray-600" />
        </div>
        <h1 className="text-2xl font-bold text-gray-900">Niveau scolaire</h1>
        <p className="text-gray-500 text-sm mt-1">Sur quel niveau souhaitez-vous travailler ?</p>
      </div>

      <div className="flex flex-col gap-3">
        {NIVEAUX.map((n) => {
          const colors = NIVEAU_COLORS[n.id];
          return (
            <button
              key={n.id}
              onClick={() => onSelect(n.id)}
              className="w-full bg-white rounded-2xl border border-gray-100 shadow-sm p-4 flex items-center gap-4 hover:shadow-md active:scale-[0.98] transition-all text-left"
            >
              <div className={`w-11 h-11 rounded-xl flex items-center justify-center flex-shrink-0 ${colors.bg}`}>
                <span className={`text-base font-bold ${colors.icon}`}>{n.label}</span>
              </div>
              <div className="flex-1 min-w-0">
                <p className="font-semibold text-gray-900 text-sm leading-tight">{n.label}</p>
                <p className="text-xs text-gray-400 mt-0.5">{n.description}</p>
              </div>
              <ChevronRight className="w-4 h-4 text-gray-300 flex-shrink-0" />
            </button>
          );
        })}
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// BanqueQuestionsView — questions from DB, UI identical to ChatView
// ---------------------------------------------------------------------------
function pairQuestions(questions, completedIds = new Set(), unlocked = false) {
  const facile = questions.filter(q => (q.niveau_difficulte || '').toLowerCase() === 'facile');
  const interm  = unlocked
    ? questions.filter(q => (q.niveau_difficulte || '').toLowerCase().includes('interm'))
    : [];

  const pairs = [];
  for (const f of facile) {
    const harder = interm.find(q2 =>
      q2.thematique === f.thematique && q2.sous_categorie === f.sous_categorie
    );
    const facileDone = completedIds.has(f.id);
    const hardDone   = harder ? completedIds.has(harder.id) : true;

    if (facileDone && hardDone) continue;
    if (!facileDone) {
      pairs.push({ base: f, harder: (harder && !hardDone) ? harder : null });
    } else {
      if (harder && !hardDone) pairs.push({ base: harder, harder: null });
    }
  }
  return pairs;
}

function buildQuestionMessage(q, num, hasHarder, topic = null) {
  const texte = q.texte_support ? `\n« ${q.texte_support} »\n` : '';
  const opts = ['**[R]**'];
  if (q.synthese_cours)        opts.push('**[S]**');
  if (q.definition_mots_cles)  opts.push('**[D]**');
  if (topic === 'ecriture')    opts.push('**[A]**');
  if (hasHarder)               opts.push('**[1]**');
  opts.push('**[O]**');
  return [
    `Exercice ${num} - ${q.sous_categorie}`,
    q.niveau_difficulte ? `Niveau de difficulté : ${q.niveau_difficulte}` : '',
    `Sous-catégorie : ${q.sous_categorie}`,
    `Objectif : ${q.objectif}`,
    texte,
    `Question : ${q.question}`,
    '',
    opts.join(' '),
  ].filter(l => l !== undefined).join('\n').trim();
}

function buildReponseMessage(q, num) {
  const opts = [];
  if (q.synthese_cours)       opts.push('**[S]**');
  if (q.definition_mots_cles) opts.push('**[D]**');
  opts.push('**[O]**');
  return `Réponse type CRPE — Exercice ${num}\n\n${q.reponse_ideale}\n\n${opts.join(' ')}`;
}

function BanqueQuestionsView({ topic, niveau, onBack, autoResume = false, resumeRow = null, isLocked = false, onQuestionAnswered }) {
  const topicLabel  = FRANCAIS_TOPICS.find(t => t.id === topic)?.label || 'Français';
  const niveauLabel = getNiveauLabel(niveau);
  const classe      = NIVEAU_TO_CLASSE[niveau] || niveau;

  const [pairs, setPairs]               = useState([]);
  const [loadingQ, setLoadingQ]         = useState(true);
  const [levelUnlocked, setLevelUnlocked] = useState(false);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [displayedDiff, setDisplayedDiff] = useState('base');
  const [exerciceNum, setExerciceNum]   = useState(1);

  const [messages, setMessages]         = useState([]);
  const [options, setOptions]           = useState([]);
  const [input, setInput]               = useState('');
  const [awaitingStart, setAwaitingStart] = useState(true);
  const [phase, setPhase]               = useState('question');
  const [loading, setLoading]           = useState(false);
  const [streamingText, setStreamingText] = useState('');
  const [hasSavedSession, setHasSavedSession] = useState(false);
  const [starting, setStarting]         = useState(false);

  const [synthese, setSynthese]         = useState({ open: false, content: '', minimized: false });
  const [definitions, setDefinitions]   = useState({ open: false, content: '', minimized: false });
  const [argumentation, setArgumentation] = useState({ open: false, content: '', loading: false, minimized: false });

  // Free-question counter (incremented in send(); limit check is at HomeView level)
  const [, setFreeQsUsed] = useState(0);

  const bottomRef       = useRef(null);
  const inputRef        = useRef(null);
  // ensure a stable user_id persists across visits even without auth
  const userIdRef       = useRef((() => {
    let id = storage.get('crpe_user_id');
    if (!id) { id = `user_${uid()}`; storage.set('crpe_user_id', id); }
    return id;
  })());
  const tentativeRef    = useRef(1);
  const dbSessionIdRef  = useRef(null);   // UUID of the active row in `sessions` table
  const savedDbRowRef   = useRef(null);   // fetched DB row cached for resume

  // ── helpers ──────────────────────────────────────────────────────────────

  const saveToDb = (msgs, idx, num, diff, tent, ph) => {
    if (!dbSessionIdRef.current) return;
    updateDbSession(dbSessionIdRef.current, {
      messages:      msgs,
      current_index: idx,
      exercice_num:  num,
      displayed_diff: diff,
      tentative:     tent ?? tentativeRef.current,
      phase:         ph ?? 'question',
    });
  };

  const completeDbSession = () => {
    if (!dbSessionIdRef.current) return;
    updateDbSession(dbSessionIdRef.current, { is_completed: true });
    dbSessionIdRef.current = null;
  };

  // ── mount : fetch questions + check DB for existing session ───────────────
  useEffect(() => {
    const userId = userIdRef.current;
    Promise.all([
      fetchQuestionsFromBanque(topic, niveau),
      resumeRow ? Promise.resolve(resumeRow) : fetchActiveSession(userId, topic, niveau),
      resumeRow ? Promise.resolve(new Set()) : fetchCompletedQuestionIds(userId),
      fetchProgressionStats(userId),
    ]).then(([data, dbRow, completedIds, progressStats]) => {
      const unlocked = progressStats.unlocked;
      setLevelUnlocked(unlocked);
      setPairs(pairQuestions(data, completedIds, unlocked));
      if (dbRow && Array.isArray(dbRow.messages) && dbRow.messages.length > 1) {
        savedDbRowRef.current = dbRow;
        setHasSavedSession(true);
      }
      setLoadingQ(false);
    });
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  useEffect(() => {
    if (!loadingQ && autoResume && savedDbRowRef.current) {
      startSession(true);
    }
  }, [loadingQ]); // eslint-disable-line react-hooks/exhaustive-deps

  // Si le verrou est activé (DB mis à jour en arrière-plan), renvoyer à l'accueil
  useEffect(() => {
    if (isLocked) onBack();
  }, [isLocked]); // eslint-disable-line react-hooks/exhaustive-deps

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, options, streamingText]);

  const currentPair = pairs[currentIndex];
  const currentQ    = currentPair ? (currentPair[displayedDiff] ?? currentPair.base) : null;

  // ── startSession ──────────────────────────────────────────────────────────
  const startSession = async (resume = false) => {
    if (starting) return;
    setStarting(true);
    setHasSavedSession(false);

    if (resume && savedDbRowRef.current) {
      const row = savedDbRowRef.current;
      dbSessionIdRef.current = row.id;
      tentativeRef.current   = row.tentative ?? 1;
      setMessages(row.messages);
      setCurrentIndex(row.current_index ?? 0);
      setExerciceNum(row.exercice_num ?? 1);
      setDisplayedDiff(row.displayed_diff ?? 'base');
      const lastA = [...row.messages].reverse().find(m => m.role === 'assistant');
      setOptions(lastA ? extractOptions(lastA.content) : []);
      const restoredPhase = row.phase === 'done'     ? 'done'
        : row.phase === 'revealed'                   ? 'revealed'
        : row.phase === 'answered' || row.phase === 'correction' ? 'answered'
        : 'question';
      setPhase(restoredPhase);
      setAwaitingStart(false);
      setStarting(false);
      setTimeout(() => inputRef.current?.focus(), 100);
      return;
    }

    // new session — close old one first, then create fresh row
    if (dbSessionIdRef.current) completeDbSession();
    tentativeRef.current = 1;

    const newId = await createDbSession(userIdRef.current, topic, niveau);
    dbSessionIdRef.current = newId;

    setAwaitingStart(false);
    if (!pairs.length) { setPhase('done'); setStarting(false); return; }

    const first  = pairs[0];
    const msg    = buildQuestionMessage(first.base, 1, !!first.harder, topic);
    const initMsgs = [{ role: 'assistant', content: msg }];
    setMessages(initMsgs);
    setOptions(extractOptions(msg));
    setCurrentIndex(0); setExerciceNum(1); setDisplayedDiff('base');
    setPhase('question');
    setStarting(false);
    setTimeout(() => inputRef.current?.focus(), 100);
  };

  const buildCorrectionPrompt = (q, userAnswer, tentative) =>
    `Tu es un correcteur expert pour le CRPE (Concours de Recrutement de Professeurs des Écoles), spécialisé en français cycle 4. Sois précis, bienveillant et rigoureux.

Thématique : ${q.thematique}
Sous-catégorie : ${q.sous_categorie}
Objectif : ${q.objectif}
Niveau de difficulté : ${q.niveau_difficulte || 'Facile'}

Question posée :
${q.question}${q.texte_support ? `\n\nTexte support :\n« ${q.texte_support} »` : ''}

Réponse attendue (ne pas divulguer directement au candidat) :
${q.reponse_ideale}

Réponse du candidat (tentative ${tentative}) :
${userAnswer}

---

Fournis une correction structurée, sans astérisques ni tirets en début de ligne :

Sur le fond : [2-3 phrases sur les éléments corrects, manquants ou inexacts par rapport à la réponse attendue]

Sur la forme : [1-2 phrases sur la formulation, le vocabulaire disciplinaire, la structure de la réponse]

Sur l'orthographe : [fautes relevées avec correction, ou "Aucune faute détectée"]

Note écriture : X/10
Note orthographe : X/10
Note CRPE : X/10
Note globale : X/10
ORTHO: "mot_fautif" → "correction" | "mot2" → "correction2"  (ou ORTHO: aucune si aucune faute d'orthographe)
SYNTAXE: "erreur de syntaxe" → "correction" | ...  (ou SYNTAXE: aucune si aucune erreur de syntaxe)

${tentative === 1
  ? '**[N]** **[R]** **[S]** **[D]** **[O]**'
  : '**[R]** **[S]** **[D]** **[O]**'
}`;

  const handleOption = (opt) => {
    if (opt === '[R]') {
      const reponseMsg = buildReponseMessage(currentQ, exerciceNum);
      const updated = [...messages, { role: 'user', content: '[R]' }, { role: 'assistant', content: reponseMsg }];
      setMessages(updated);
      setOptions(extractOptions(reponseMsg));
      setPhase('revealed');
      saveToDb(updated, currentIndex, exerciceNum, displayedDiff, undefined, 'revealed');
      return;
    }
    if (opt === '[N]') {
      tentativeRef.current = 2;
      const retryMsg = 'Tentative 2 — Relisez la question et améliorez votre réponse.';
      const updated = [...messages, { role: 'user', content: '[N]' }, { role: 'assistant', content: retryMsg }];
      setMessages(updated);
      setOptions([]);
      setPhase('question');
      saveToDb(updated, currentIndex, exerciceNum, displayedDiff, 2, 'question');
      setTimeout(() => inputRef.current?.focus(), 100);
      return;
    }
    if (opt === '[A]') {
      setArgumentation({ open: true, content: '', loading: true, minimized: false });
      const q = currentQ;
      streamClaude(
        [{ role: 'user', content: `Question : ${q?.question}\n\nTexte support :\n${q?.texte_support || '(aucun)'}\n\nObjectif : ${q?.objectif}` }],
        `Tu es un coach en argumentation littéraire pour le CRPE. Donne des conseils structurés et actionnables pour aider à construire une réponse argumentée à cette question. Ne donne pas la réponse — guide la démarche argumentative. Structure ta réponse en 3 parties : 1. Plan suggéré (2-3 parties), 2. Éléments textuels à mobiliser, 3. Vocabulaire littéraire clé. Sois concis et précis.`,
        (chunk) => setArgumentation(a => ({ ...a, content: chunk })),
        (final) => setArgumentation(a => ({ ...a, content: final, loading: false })),
        { user_id: userIdRef.current, session_id: dbSessionIdRef.current, type_evenement: 'banque_argumentation', matiere: 'francais', thematique: topic || null },
      ).catch(() => setArgumentation(a => ({ ...a, loading: false, content: 'Erreur lors du chargement des conseils.' })));
      return;
    }
    if (opt === '[S]') {
      if (currentQ?.synthese_cours)
        setSynthese(s => ({ ...s, open: true, content: currentQ.synthese_cours, minimized: false }));
      return;
    }
    if (opt === '[D]') {
      if (currentQ?.definition_mots_cles)
        setDefinitions(d => ({ ...d, open: true, content: currentQ.definition_mots_cles, minimized: false }));
      return;
    }
    if (opt === '[1]') {
      const harder = currentPair?.harder;
      if (!harder) return;
      const harderMsg = buildQuestionMessage(harder, exerciceNum, false, topic);
      const updated = [...messages, { role: 'user', content: '[1]' }, { role: 'assistant', content: harderMsg }];
      setDisplayedDiff('harder');
      tentativeRef.current = 1;
      setMessages(updated);
      setOptions(extractOptions(harderMsg));
      setPhase('question');
      saveToDb(updated, currentIndex, exerciceNum, 'harder', 1, 'question');
      setTimeout(() => inputRef.current?.focus(), 100);
      return;
    }
    if (opt === '[O]') {
      if (isLocked) { onBack(); return; }
      setSynthese({ open: false, content: '', minimized: false });
      setDefinitions({ open: false, content: '', minimized: false });
      setArgumentation({ open: false, content: '', loading: false, minimized: false });
      tentativeRef.current = 1;
      const nextIndex = currentIndex + 1;
      if (nextIndex >= pairs.length) {
        const doneMsg = `Vous avez terminé les ${pairs.length} exercice${pairs.length > 1 ? 's' : ''} disponibles. Bravo !\n\nVos réponses ont été enregistrées dans votre historique.`;
        const doneMsgs = [...messages, { role: 'user', content: '[O]' }, { role: 'assistant', content: doneMsg }];
        setMessages(doneMsgs);
        setOptions([]);
        setPhase('done');
        saveToDb(doneMsgs, currentIndex, exerciceNum, displayedDiff, tentativeRef.current, 'done');
        return;
      }
      const nextNum = exerciceNum + 1;
      const nextQ   = pairs[nextIndex];
      const nextMsg = buildQuestionMessage(nextQ.base, nextNum, !!nextQ.harder, topic);
      const updated = [...messages, { role: 'user', content: '[O]' }, { role: 'assistant', content: nextMsg }];
      setCurrentIndex(nextIndex);
      setDisplayedDiff('base');
      setExerciceNum(nextNum);
      setMessages(updated);
      setOptions(extractOptions(nextMsg));
      setPhase('question');
      saveToDb(updated, nextIndex, nextNum, 'base', 1, 'question');
      setTimeout(() => inputRef.current?.focus(), 100);
      return;
    }
  };

  const send = async (text) => {
    const content = text.trim();
    if (!content || loading) return;
    if (/^\[[A-Z0-9+>]\]$/.test(content)) {
      handleOption(content);
      setInput('');
      return;
    }

    const q          = currentQ;
    const tentative  = tentativeRef.current;
    const userMsg    = { role: 'user', content };
    const msgsBefore = [...messages, userMsg];
    // capture index/num/diff at send time (closure — correct for this question)
    const idxSnap    = currentIndex;
    const numSnap    = exerciceNum;
    const diffSnap   = displayedDiff;

    setInput('');
    setMessages(msgsBefore);
    setOptions([]);
    setLoading(true);
    setStreamingText('');
    setPhase('correction');

    try {
      await streamClaude(
        [{ role: 'user', content: buildCorrectionPrompt(q, content, tentative) }],
        'Tu es un correcteur expert pour le CRPE. Réponds en français, de manière concise et structurée.',
        (chunk) => setStreamingText(chunk),
        (final) => {
          setStreamingText('');
          const finalMsgs = [...msgsBefore, { role: 'assistant', content: final }];
          setMessages(finalMsgs);
          setOptions(extractOptions(final));
          setPhase('answered');
          saveToDb(finalMsgs, idxSnap, numSnap, diffSnap, tentative, 'answered');

          const notes = extractNotesFromText(final);
          const _ne2 = notes.ecriture ?? null, _no2 = notes.orthographe ?? null, _nc2 = notes.crpe ?? null;
          const _ngVals2 = [_ne2, _no2, _nc2].filter(v => v != null);
          const noteFields = {
            note_ecriture:    _ne2,
            note_orthographe: _no2,
            note_crpe:        _nc2,
            note_globale:     _ngVals2.length ? Math.round((_ngVals2.reduce((a, b) => a + b, 0) / _ngVals2.length) * 10) / 10 : null,
          };
          const conseils = extractConseils(final);
          const saveBanqueFautesEtErreurs = (reponseId) => {
            const base = {
              user_id:                userIdRef.current,
              session_id:             dbSessionIdRef.current,
              classe,
              thematique:             q?.thematique     || null,
              sous_categorie:         q?.sous_categorie  || null,
              objectif:               q?.objectif        || null,
              id_reponse_utilisateur: reponseId,
              ma_reponse:             content,
              question:               q?.question        || null,
            };
            extractOrthoFautes(final).forEach(({ faute, correction }) => {
              supabaseInsert('fautes_orthographe', { ...base, faute, correction });
            });
            extractSyntaxeErreurs(final).forEach(({ erreur, correction }) => {
              supabaseInsert('erreurs_syntaxe', { ...base, erreur, correction });
            });
          };
          if (tentative === 1) {
            supabaseInsertReturningId('reponses_utilisateurs', {
              user_id:                userIdRef.current,
              session_id:             dbSessionIdRef.current,
              classe,
              thematique:             q?.thematique     || null,
              sous_categorie:         q?.sous_categorie  || null,
              objectif:               q?.objectif        || null,
              question:               q?.question        || null,
              texte_support:          q?.texte_support   || null,
              reponse:                content,
              reponse_ideale:         q?.reponse_ideale  || null,
              conseils,
              tentative:              1,
              id_question_completee:  q?.id              ?? null,
              ...noteFields,
            }).then(saveBanqueFautesEtErreurs);
            // Increment free question counter (only on first attempt = one question answered)
            if (!isLocked) {
              const newCount = (storage.get('crpe_free_questions_used') || 0) + 1;
              storage.set('crpe_free_questions_used', newCount);
              setFreeQsUsed(newCount);
              if (typeof onQuestionAnswered === 'function') onQuestionAnswered(userIdRef.current);
            }
          } else {
            supabaseInsertReturningId('reponses_utilisateurs', {
              user_id:                userIdRef.current,
              session_id:             dbSessionIdRef.current,
              classe,
              thematique:             q?.thematique     || null,
              sous_categorie:         q?.sous_categorie  || null,
              objectif:               q?.objectif        || null,
              question:               q?.question        || null,
              texte_support:          q?.texte_support   || null,
              reponse:                content,
              reponse_ideale:         q?.reponse_ideale  || null,
              conseils,
              tentative:              2,
              id_question_completee:  q?.id              ?? null,
              ...noteFields,
            }).then(saveBanqueFautesEtErreurs);
          }
        },
        { user_id: userIdRef.current, session_id: dbSessionIdRef.current, type_evenement: 'banque_correction', matiere: 'francais', thematique: q?.thematique || topic || null }
      );
    } catch (_) {
      setStreamingText('');
      const errMsg = 'Erreur lors de la correction. Veuillez réessayer.\n\n**[O]**';
      setMessages(prev => [...prev, { role: 'assistant', content: errMsg }]);
      setOptions(extractOptions(errMsg));
      setPhase('answered');
    }
    setLoading(false);
    setTimeout(() => inputRef.current?.focus(), 100);
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); send(input); }
  };

  const restartSession = () => {
    if (dbSessionIdRef.current) completeDbSession();
    tentativeRef.current = 1;
    savedDbRowRef.current = null;
    setCurrentIndex(0); setDisplayedDiff('base'); setExerciceNum(1);
    setMessages([]); setOptions([]); setInput('');
    setSynthese({ open: false, content: '', minimized: false });
    setDefinitions({ open: false, content: '', minimized: false });
    setArgumentation({ open: false, content: '', loading: false, minimized: false });
    setStreamingText(''); setLoading(false);
    setAwaitingStart(true); setHasSavedSession(false); setPhase('question');
  };

  if (loadingQ) {
    return (
      <div className="flex-1 flex items-center justify-center">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-400" />
      </div>
    );
  }

  const inputDisabled = awaitingStart || loading || phase !== 'question';

  return (
    <div className="flex flex-col flex-1 min-h-0">

      {/* Panneau synthèse + définitions + argumentation */}
      {(synthese.open || definitions.open || argumentation.open) && (
        <div className="fixed top-0 right-0 bottom-0 w-96 z-50 flex flex-col shadow-2xl">
          {synthese.open && (
            <div className={`flex flex-col bg-white border-l border-gray-200 transition-all ${synthese.minimized ? 'flex-shrink-0' : 'flex-1 min-h-0'}`}>
              <div className="flex items-center justify-between px-4 py-3 bg-indigo-600 flex-shrink-0">
                <div className="flex items-center gap-2">
                  <BookOpen className="w-4 h-4 text-white" />
                  <span className="text-sm font-semibold text-white">Synthèse du cours</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <button onClick={() => setSynthese(s => ({ ...s, minimized: !s.minimized }))} className="text-white/70 hover:text-white transition-colors">
                    {synthese.minimized ? <ChevronDown className="w-4 h-4" /> : <ChevronUp className="w-4 h-4" />}
                  </button>
                  <button onClick={() => setSynthese({ open: false, content: '', minimized: false })} className="text-white/70 hover:text-white transition-colors">
                    <X className="w-4 h-4" />
                  </button>
                </div>
              </div>
              {!synthese.minimized && (
                <div className="flex-1 overflow-y-auto px-5 py-4 text-sm">
                  <MessageContent text={synthese.content} />
                </div>
              )}
            </div>
          )}
          {definitions.open && (
            <div className={`flex flex-col bg-white border-l border-gray-200 transition-all ${definitions.minimized ? 'flex-shrink-0' : 'flex-1 min-h-0'} ${synthese.open ? 'border-t-2 border-t-violet-200' : ''}`}>
              <div className="flex items-center justify-between px-4 py-3 bg-violet-600 flex-shrink-0">
                <div className="flex items-center gap-2">
                  <ListChecks className="w-4 h-4 text-white" />
                  <span className="text-sm font-semibold text-white">Définitions des mots clés</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <button onClick={() => setDefinitions(d => ({ ...d, minimized: !d.minimized }))} className="text-white/70 hover:text-white transition-colors">
                    {definitions.minimized ? <ChevronDown className="w-4 h-4" /> : <ChevronUp className="w-4 h-4" />}
                  </button>
                  <button onClick={() => setDefinitions({ open: false, content: '', minimized: false })} className="text-white/70 hover:text-white transition-colors">
                    <X className="w-4 h-4" />
                  </button>
                </div>
              </div>
              {!definitions.minimized && (
                <div className="flex-1 overflow-y-auto px-5 py-4 text-sm">
                  <MessageContent text={definitions.content} />
                </div>
              )}
            </div>
          )}
          {argumentation.open && (
            <div className={`flex flex-col bg-white border-l border-gray-200 transition-all ${argumentation.minimized ? 'flex-shrink-0' : 'flex-1 min-h-0'} ${synthese.open || definitions.open ? 'border-t-2 border-t-orange-200' : ''}`}>
              <div className="flex items-center justify-between px-4 py-3 bg-orange-500 flex-shrink-0">
                <div className="flex items-center gap-2">
                  <Lightbulb className="w-4 h-4 text-white" />
                  <span className="text-sm font-semibold text-white">Conseil argumentation</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <button onClick={() => setArgumentation(a => ({ ...a, minimized: !a.minimized }))} className="text-white/70 hover:text-white transition-colors">
                    {argumentation.minimized ? <ChevronDown className="w-4 h-4" /> : <ChevronUp className="w-4 h-4" />}
                  </button>
                  <button onClick={() => setArgumentation({ open: false, content: '', loading: false, minimized: false })} className="text-white/70 hover:text-white transition-colors">
                    <X className="w-4 h-4" />
                  </button>
                </div>
              </div>
              {!argumentation.minimized && (
                <div className="flex-1 overflow-y-auto px-5 py-4 text-sm">
                  {argumentation.loading ? <TypingIndicator /> : <MessageContent text={argumentation.content} />}
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {/* Header */}
      <div className="flex items-center justify-between px-4 py-3 border-b border-gray-100 bg-white flex-shrink-0">
        <div className="flex items-center gap-3 min-w-0">
          <button onClick={onBack} className="text-gray-400 hover:text-gray-600 transition-colors flex-shrink-0">
            <ChevronLeft className="w-5 h-5" />
          </button>
          <div className="flex flex-col min-w-0">
            <div className="flex items-center gap-1.5 flex-wrap">
              <span className="text-xs font-semibold px-2 py-0.5 rounded-full self-start bg-indigo-100 text-indigo-700">
                Français
              </span>
            </div>
            <p className="text-xs text-gray-400 mt-1 truncate">
              {topicLabel}
              <span className="ml-1 text-gray-300">·</span>
              <span className="ml-1">{niveauLabel}</span>
              <span className="ml-1 text-gray-300">·</span>
              <span className="ml-1 font-medium text-gray-500">Cycle 4</span>
            </p>
          </div>
        </div>
        <button
          onClick={restartSession}
          className="flex items-center gap-1 text-xs text-gray-400 hover:text-gray-600 transition-colors flex-shrink-0 ml-3"
        >
          <RotateCcw className="w-3 h-3" /> Nouvelle session
        </button>
      </div>

      {/* Chat area */}
      <div className="flex-1 overflow-y-auto px-4 pt-4 pb-2">
        {awaitingStart ? (
          <>
            <ChatBubble msg={{
              role: 'assistant',
              content: `Vous travaillez sur **${topicLabel}** — **${niveauLabel}** — **Cycle 4**.\n\nVoici comment fonctionne la session :\n\n1. ${levelUnlocked ? 'La version **Facile** de chaque exercice est affichée en premier.' : 'Seules les questions de niveau **Facile** sont disponibles pour l\'instant.'}\n2. Rédigez votre réponse dans le champ ci-dessous — **Claude corrigera et notera votre production**.\n3. Vous avez **2 tentatives** par question pour améliorer votre réponse.\n4. Consultez la **synthèse du cours** ou les **définitions des mots clés** via les boutons dédiés.\n5. ${levelUnlocked ? 'Si vous souhaitez aller plus loin, passez à la **version intermédiaire** du même exercice.' : 'Remplissez les critères sur la page d\'accueil pour débloquer le niveau intermédiaire.'}\n\n${pairs.length > 0 ? `${pairs.length} exercice${pairs.length > 1 ? 's' : ''} disponible${pairs.length > 1 ? 's' : ''} pour cette sélection.` : 'Aucun exercice disponible pour cette sélection.'}`,
            }} />
            <div className="pl-11 mt-1 mb-2 flex flex-col gap-2">
              {hasSavedSession && (
                <button
                  onClick={() => startSession(true)}
                  disabled={!pairs.length || starting}
                  className="bg-amber-500 text-white rounded-xl px-5 py-2.5 text-sm font-semibold hover:bg-amber-600 active:bg-amber-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed w-fit"
                >
                  {starting ? 'Chargement…' : 'Reprendre la session en cours'}
                </button>
              )}
              <button
                onClick={() => startSession(false)}
                disabled={!pairs.length || starting}
                className="bg-indigo-600 text-white rounded-xl px-5 py-2.5 text-sm font-semibold hover:bg-indigo-700 active:bg-indigo-800 transition-all disabled:opacity-50 disabled:cursor-not-allowed w-fit"
              >
                {starting ? 'Chargement…' : hasSavedSession ? 'Nouvelle session' : 'Je suis prêt·e'}
              </button>
            </div>
          </>
        ) : (
          <>
            {messages.map((msg, i) => {
              if (msg.role === 'user' && /^\[[A-Z0-9+>]\]$/.test(msg.content.trim())) return null;
              return <ChatBubble key={i} msg={msg} />;
            })}
            {loading && !streamingText && <TypingIndicator />}
            {streamingText && <ChatBubble msg={{ role: 'assistant', content: streamingText }} isStreaming />}
          </>
        )}
        <div ref={bottomRef} />
      </div>

      {!awaitingStart && !loading && options.length > 0 && (
        <QuickReplies options={options} onSelect={send} />
      )}

      <div className="px-3 pt-2 border-t border-gray-100 bg-white flex-shrink-0" style={{ paddingBottom: 'calc(env(safe-area-inset-bottom, 0px) + 96px)' }}>
        <div className="flex gap-2 items-end">
          <textarea
            ref={inputRef}
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder={inputDisabled ? '' : 'Votre réponse…'}
            disabled={inputDisabled}
            rows={4}
            className="flex-1 resize-none border border-gray-200 rounded-xl px-3 py-2.5 text-sm text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:border-transparent disabled:opacity-50 transition-all"
          />
          <button
            onClick={() => send(input)}
            disabled={!input.trim() || inputDisabled}
            className="w-10 h-10 bg-indigo-600 text-white rounded-xl flex items-center justify-center hover:bg-indigo-700 active:bg-indigo-800 disabled:opacity-40 disabled:cursor-not-allowed transition-all flex-shrink-0"
          >
            <Send className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// ModePickerView — choose Français session mode
// ---------------------------------------------------------------------------
const FRANCAIS_MODES = [
  {
    id: 'questions',
    label: 'Répondre aux questions',
    description: 'Questions issues de la base de données, filtrées par thématique et niveau',
    icon: ListChecks,
    colors: { bg: 'bg-indigo-100', icon: 'text-indigo-600' },
  },
];

function ModePickerView({ onSelect, onBack }) {
  return (
    <div className="flex-1 overflow-y-auto px-4 pt-6 pb-24">
      <button
        onClick={onBack}
        className="flex items-center gap-1.5 text-gray-500 text-sm mb-6 hover:text-gray-700 transition-colors"
      >
        <ChevronLeft className="w-4 h-4" />
        Retour
      </button>

      <div className="mb-6">
        <div className="w-12 h-12 rounded-xl bg-indigo-100 flex items-center justify-center mb-3">
          <MessageCircle className="w-6 h-6 text-indigo-600" />
        </div>
        <h1 className="text-2xl font-bold text-gray-900">Mode de session</h1>
        <p className="text-gray-500 text-sm mt-1">Comment souhaitez-vous travailler ?</p>
      </div>

      <div className="flex flex-col gap-3">
        {FRANCAIS_MODES.map((mode) => {
          const Icon = mode.icon;
          return (
            <button
              key={mode.id}
              onClick={() => onSelect(mode.id)}
              className="w-full bg-white rounded-2xl border border-gray-100 shadow-sm p-4 flex items-center gap-4 hover:shadow-md active:scale-[0.98] transition-all text-left"
            >
              <div className={`w-11 h-11 rounded-xl flex items-center justify-center flex-shrink-0 ${mode.colors.bg}`}>
                <Icon className={`w-5 h-5 ${mode.colors.icon}`} />
              </div>
              <div className="flex-1 min-w-0">
                <p className="font-semibold text-gray-900 text-sm leading-tight">{mode.label}</p>
                <p className="text-xs text-gray-400 mt-0.5">{mode.description}</p>
              </div>
              <ChevronRight className="w-4 h-4 text-gray-300 flex-shrink-0" />
            </button>
          );
        })}
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Onboarding — single page: prenom + concours + academie
// ---------------------------------------------------------------------------
const CONCOURS_LIST = [
  'Concours externe et externe spécial — Bac+3',
  'Concours externe et externe spécial — Bac+5',
  'Troisième concours',
  'Second concours interne et interne spécial (langues régionales)',
  'Concours interne exceptionnel',
  'Premier concours interne',
  "Concours spécifiques à l'académie de Mayotte",
];

const ACADEMIES_LIST = [
  'Je ne sais pas encore',
  'Aix-Marseille', 'Amiens', 'Besançon', 'Bordeaux', 'Caen',
  'Clermont-Ferrand', 'Créteil', 'Dijon', 'Grenoble', 'Guadeloupe',
  'Guyane', 'La Réunion', 'Lille', 'Limoges', 'Lyon',
  'Martinique', 'Mayotte', 'Montpellier', 'Nancy-Metz', 'Nantes',
  'Nice', 'Normandie', 'Orléans-Tours', 'Paris', 'Poitiers',
  'Reims', 'Rennes', 'Rouen', 'Strasbourg', 'Toulouse', 'Versailles',
];

function Onboarding({ onComplete }) {
  const [prenom, setPrenom] = useState('');
  const [concours, setConcours] = useState('');
  const [academie, setAcademie] = useState('');

  const canSubmit = prenom.trim().length > 0 && concours !== '' && academie !== '';

  const handleSubmit = () => {
    if (!canSubmit) return;
    onComplete({ prenom: prenom.trim(), concours, academie });
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-emerald-50 flex flex-col items-center justify-center px-5 py-4">
      <div className="w-full max-w-sm">
        <div className="flex items-center justify-center gap-3 mb-3">
          <div className="w-10 h-10 bg-indigo-600 rounded-xl flex items-center justify-center shadow-md flex-shrink-0">
            <GraduationCap className="w-5 h-5 text-white" />
          </div>
          <div>
            <h1 className="text-xl font-bold text-gray-900 leading-tight">CRPE Tuteur IA</h1>
            <p className="text-gray-500 text-xs">Votre tuteur intelligent pour le concours</p>
          </div>
        </div>

        <div className="bg-white rounded-2xl border border-gray-100 shadow-sm p-4">
          <label className="block text-xs font-semibold text-gray-400 uppercase tracking-wide mb-1">
            Votre prénom
          </label>
          <input
            type="text"
            value={prenom}
            onChange={(e) => setPrenom(e.target.value)}
            placeholder="Prénom…"
            autoFocus
            className="w-full px-3 py-2 border border-gray-200 rounded-xl text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all text-sm mb-4"
          />

          <label className="block text-xs font-semibold text-gray-400 uppercase tracking-wide mb-1.5">
            Concours préparé
          </label>
          <div className="flex flex-col gap-1 mb-4">
            {CONCOURS_LIST.map((c) => (
              <button
                key={c}
                onClick={() => setConcours(c)}
                className={`py-1.5 px-3 rounded-xl border-2 text-xs font-medium text-left transition-all ${
                  concours === c
                    ? 'border-indigo-500 bg-indigo-50 text-indigo-700'
                    : 'border-gray-100 bg-white text-gray-600 hover:border-gray-200'
                }`}
              >
                {c}
              </button>
            ))}
          </div>

          <label className="block text-xs font-semibold text-gray-400 uppercase tracking-wide mb-1">
            Académie
          </label>
          <select
            value={academie}
            onChange={(e) => setAcademie(e.target.value)}
            className="w-full px-3 py-2 border border-gray-200 rounded-xl text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all bg-white mb-4"
          >
            <option value="">Choisir une académie…</option>
            {ACADEMIES_LIST.map((a) => (
              <option key={a} value={a}>{a}</option>
            ))}
          </select>

          <button
            onClick={handleSubmit}
            disabled={!canSubmit}
            className="w-full bg-indigo-600 text-white py-2.5 rounded-xl font-semibold hover:bg-indigo-700 active:bg-indigo-800 disabled:opacity-40 disabled:cursor-not-allowed transition-all flex items-center justify-center gap-2 text-sm"
          >
            Commencer <ChevronRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// StatsView helpers
// ---------------------------------------------------------------------------
function NoteLineChart({ rows, classLabel, borderColor, hdrBg, labelColor }) {
  const W = 320, H = 190;
  const PAD = { top: 12, right: 15, bottom: 36, left: 32 };
  const iW = W - PAD.left - PAD.right;
  const iH = H - PAD.top - PAD.bottom;

  // Regrouper par jour (YYYY-MM-DD) et trier chronologiquement
  const byDay = {};
  for (const r of rows) {
    if (!r.created_at) continue;
    const day = r.created_at.slice(0, 10);
    if (!byDay[day]) byDay[day] = [];
    byDay[day].push(r);
  }
  const days = Object.keys(byDay).sort();
  const n = days.length;

  if (n === 0) return (
    <div className="bg-white rounded-2xl border-2 p-5 text-center text-sm text-gray-400" style={{ borderColor }}>
      Aucune donnée pour la classe de {classLabel}
    </div>
  );

  const avg = (arr) => arr.length ? arr.reduce((a, b) => a + b, 0) / arr.length : null;
  const dayAvg = (d, key) => avg(byDay[d].map(r => r[key]).filter(v => v != null));
  const dayGlobal = (d) => avg(byDay[d].map(r => {
    const ns = [r.note_ecriture, r.note_orthographe, r.note_crpe].filter(v => v != null);
    return ns.length ? ns.reduce((a, b) => a + b, 0) / ns.length : r.note_globale ?? null;
  }).filter(v => v != null));

  const LINES = [
    { key: 'globale',     label: 'Moyenne',     color: '#6366f1', get: d => dayGlobal(d) },
    { key: 'ecriture',    label: 'Écriture',    color: '#3b82f6', get: d => dayAvg(d, 'note_ecriture') },
    { key: 'orthographe', label: 'Orthographe', color: '#f43f5e', get: d => dayAvg(d, 'note_orthographe') },
    { key: 'crpe',        label: 'Niv. CRPE',   color: '#f59e0b', get: d => dayAvg(d, 'note_crpe') },
  ];

  const xPos = i => PAD.left + (n === 1 ? iW / 2 : (i / (n - 1)) * iW);
  const yPos = v => PAD.top + iH - (v / 10) * iH;
  const fmtDay = d => { const [, m, dd] = d.split('-'); return `${dd}/${m}`; };
  const step = n <= 7 ? 1 : Math.ceil(n / 7);
  const Y_TICKS = [0, 2, 4, 6, 8, 10];

  return (
    <div className="bg-white rounded-2xl overflow-hidden border-2" style={{ borderColor }}>
      {/* En-tête */}
      <div className={`flex items-center gap-2 px-4 py-2.5 ${hdrBg}`}>
        <span className={`text-sm font-bold ${labelColor}`}>Classe de {classLabel}</span>
        <span className="text-xs text-gray-400">{rows.length} réponse{rows.length !== 1 ? 's' : ''} · {n} jour{n !== 1 ? 's' : ''}</span>
      </div>
      <p className="text-[10px] text-gray-400 px-4 pt-1.5">Moyenne des notes par jour</p>
      {/* Légende */}
      <div className="flex flex-wrap gap-x-4 gap-y-1 px-4 pt-2.5 pb-0.5">
        {LINES.map(l => (
          <div key={l.key} className="flex items-center gap-1.5">
            <svg width="18" height="4"><line x1="0" y1="2" x2="18" y2="2" stroke={l.color} strokeWidth="2" strokeLinecap="round" /></svg>
            <span className="text-[10px] text-gray-500">{l.label}</span>
          </div>
        ))}
      </div>
      {/* SVG */}
      <div className="px-3 pb-2 pt-1">
        <svg viewBox={`0 0 ${W} ${H}`} className="w-full" style={{ display: 'block' }}>
          {/* Grille Y + labels */}
          {Y_TICKS.map(v => (
            <g key={v}>
              <line x1={PAD.left} y1={yPos(v)} x2={W - PAD.right} y2={yPos(v)}
                stroke={v === 0 ? '#e5e7eb' : '#f3f4f6'} strokeWidth="1" />
              <text x={PAD.left - 4} y={yPos(v) + 3.5} fontSize="8" fill="#9ca3af" textAnchor="end">{v}</text>
            </g>
          ))}
          {/* Axe Y */}
          <line x1={PAD.left} y1={PAD.top} x2={PAD.left} y2={H - PAD.bottom} stroke="#e5e7eb" strokeWidth="1" />
          {/* Labels X (jours) */}
          {days.map((d, i) => (i % step === 0 || i === n - 1) && (
            <text key={d} x={xPos(i)} y={H - PAD.bottom + 11} fontSize="7.5" fill="#9ca3af" textAnchor="middle">
              {fmtDay(d)}
            </text>
          ))}
          {/* Label axe X */}
          <text x={PAD.left + iW / 2} y={H - 2} fontSize="8" fill="#9ca3af" textAnchor="middle">Jours</text>
          {/* Courbes */}
          {LINES.map(({ key, color, get }) => {
            const pts = days.map((d, i) => ({ i, v: get(d) }));
            // Segmenter pour gérer les valeurs nulles
            const segments = [];
            let seg = [];
            for (const p of pts) {
              if (p.v != null) { seg.push(p); }
              else if (seg.length) { segments.push(seg); seg = []; }
            }
            if (seg.length) segments.push(seg);
            if (!segments.length) return null;
            return (
              <g key={key}>
                {segments.map((s, si) => (
                  <polyline key={si}
                    points={s.map(p => `${xPos(p.i)},${yPos(p.v)}`).join(' ')}
                    fill="none" stroke={color} strokeWidth="2"
                    strokeLinejoin="round" strokeLinecap="round"
                  />
                ))}
                {pts.filter(p => p.v != null).map(p => (
                  <circle key={p.i} cx={xPos(p.i)} cy={yPos(p.v)} r="3" fill="white" stroke={color} strokeWidth="2" />
                ))}
              </g>
            );
          })}
        </svg>
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// StatsView — moyennes par classe / thématique / sous-catégorie / objectif
// ---------------------------------------------------------------------------
function StatsView() {
  const [rows, setRows]       = useState([]);
  const [loading, setLoading] = useState(true);
  const [view, setView]       = useState('tableau'); // 'tableau' | 'courbes'

  useEffect(() => {
    const userId = storage.get('crpe_user_id');
    if (!userId || !SUPABASE_URL || !SUPABASE_KEY) { setLoading(false); return; }
    const params = new URLSearchParams({
      user_id: `eq.${userId}`,
      select: 'classe,note_ecriture,note_orthographe,note_crpe,note_globale,created_at',
    });
    fetch(`${SUPABASE_URL}/rest/v1/reponses_utilisateurs?${params}`, {
      headers: { apikey: SUPABASE_KEY, Authorization: `Bearer ${SUPABASE_KEY}` },
    })
      .then(r => r.json())
      .then(data => { if (Array.isArray(data)) setRows(data); setLoading(false); })
      .catch(() => setLoading(false));
  }, []);

  const mean = (arr) => {
    const vals = arr.map(r => {
      const ns = [r.note_ecriture, r.note_orthographe, r.note_crpe].filter(v => v != null);
      if (ns.length) return ns.reduce((a, b) => a + b, 0) / ns.length;
      return r.note_globale ?? null;
    }).filter(v => v != null);
    return vals.length ? Math.round(vals.reduce((a, b) => a + b, 0) / vals.length * 10) / 10 : null;
  };

  const meanCat = (arr, key) => {
    const vals = arr.map(r => r[key]).filter(v => v != null);
    return vals.length ? Math.round(vals.reduce((a, b) => a + b, 0) / vals.length * 10) / 10 : null;
  };

  const fmt = (v) => v != null ? v.toFixed(1).replace('.', ',') : null;

  const scoreColor = (v) => v == null ? 'text-gray-400' : v >= 7 ? 'text-emerald-600' : v >= 5 ? 'text-amber-600' : 'text-red-500';

  const byClasse = {};
  rows.forEach(r => {
    const cl = r.classe || '—';
    if (!byClasse[cl]) byClasse[cl] = [];
    byClasse[cl].push(r);
  });

  const CLASS_ORDER = ['5e', '4e', '3e'];
  const classes = CLASS_ORDER.filter(c => byClasse[c])
    .concat(Object.keys(byClasse).filter(c => !CLASS_ORDER.includes(c)));

  const CLASS_STYLE = {
    '5e': { hdr: 'bg-emerald-100 border-emerald-200', text: 'text-emerald-700', badge: 'bg-emerald-600' },
    '4e': { hdr: 'bg-amber-100 border-amber-200',     text: 'text-amber-700',   badge: 'bg-amber-500'   },
    '3e': { hdr: 'bg-rose-100 border-rose-200',       text: 'text-rose-700',    badge: 'bg-rose-500'    },
  };
  const DEFAULT_CL_STYLE = { hdr: 'bg-gray-100 border-gray-200', text: 'text-gray-700', badge: 'bg-gray-500' };

  if (loading) return (
    <div className="flex-1 flex items-center justify-center">
      <Loader2 className="w-6 h-6 text-indigo-400 animate-spin" />
    </div>
  );

  if (!rows.length) return (
    <div className="flex-1 overflow-y-auto px-4 pt-6 pb-24">
      <h2 className="text-xl font-bold text-gray-900 mb-4">Statistiques</h2>
      <EmptyState icon={BarChart2} title="Aucune donnée" subtitle="Complétez des exercices pour voir vos statistiques ici." />
    </div>
  );

  const globalMean = mean(rows);

  const CHART_STYLE = {
    '5e': { borderColor: '#a7f3d0', hdrBg: 'bg-emerald-50', labelColor: 'text-emerald-700' },
    '4e': { borderColor: '#fcd34d', hdrBg: 'bg-amber-50',   labelColor: 'text-amber-700'   },
    '3e': { borderColor: '#fda4af', hdrBg: 'bg-rose-50',    labelColor: 'text-rose-700'    },
  };
  const DEFAULT_CHART_STYLE = { borderColor: '#e5e7eb', hdrBg: 'bg-gray-50', labelColor: 'text-gray-700' };

  return (
    <div className="flex-1 overflow-y-auto px-4 pt-6 pb-24">
      {/* Header */}
      <div className="flex items-center justify-between mb-1">
        <h2 className="text-xl font-bold text-gray-900">Statistiques</h2>
        {globalMean != null && (
          <span className={`text-sm font-bold px-3 py-1 rounded-full ${globalMean >= 7 ? 'bg-emerald-100 text-emerald-700' : globalMean >= 5 ? 'bg-amber-100 text-amber-700' : 'bg-red-100 text-red-600'}`}>
            Moy. {fmt(globalMean)}/10
          </span>
        )}
      </div>
      <p className="text-xs text-gray-400 mb-4">
        {rows.length} réponse{rows.length > 1 ? 's' : ''} · {classes.length} classe{classes.length > 1 ? 's' : ''}
      </p>

      {/* Toggle Tableau / Courbes */}
      <div className="flex gap-1 bg-gray-100 rounded-xl p-1 mb-5">
        {[['tableau', 'Tableau'], ['courbes', 'Courbes']].map(([v, label]) => (
          <button
            key={v}
            onClick={() => setView(v)}
            className={`flex-1 py-1.5 rounded-lg text-sm font-semibold transition-all ${view === v ? 'bg-white text-indigo-700 shadow-sm' : 'text-gray-500 hover:text-gray-700'}`}
          >
            {label}
          </button>
        ))}
      </div>

      {/* Vue Tableau */}
      {view === 'tableau' && (
        <div className="flex flex-col gap-4">
          {classes.map(cl => {
            const clRows = byClasse[cl];
            const clMean = mean(clRows);
            const nQ     = clRows.length;
            const mE     = meanCat(clRows, 'note_ecriture');
            const mO     = meanCat(clRows, 'note_orthographe');
            const mC     = meanCat(clRows, 'note_crpe');
            const st     = CLASS_STYLE[cl] || DEFAULT_CL_STYLE;

            return (
              <div key={cl} className={`rounded-2xl border-2 ${st.hdr} overflow-hidden`}>
                <div className="flex items-center gap-3 px-4 py-3">
                  <div className={`w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 ${st.badge}`}>
                    <span className="text-sm font-bold text-white">{cl}</span>
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className={`text-sm font-bold ${st.text}`}>Classe de {cl}</p>
                    <p className="text-xs text-gray-500">{nQ} réponse{nQ > 1 ? 's' : ''}</p>
                  </div>
                  {clMean != null && (
                    <div className="text-right flex-shrink-0">
                      <p className="text-[10px] text-gray-400 uppercase tracking-wide">Moyenne</p>
                      <p className={`text-lg font-bold leading-none ${scoreColor(clMean)}`}>
                        {fmt(clMean)}<span className="text-xs font-normal opacity-60">/10</span>
                      </p>
                    </div>
                  )}
                </div>
                <div className="grid grid-cols-3 divide-x divide-white/60 border-t border-white/60">
                  <div className="bg-blue-50/70 px-3 py-3 text-center">
                    <p className="text-[9px] font-semibold text-blue-400 uppercase tracking-wide mb-1">Écriture</p>
                    <p className={`text-base font-bold leading-none ${scoreColor(mE)}`}>
                      {mE != null ? <>{fmt(mE)}<span className="text-[10px] font-normal opacity-60">/10</span></> : <span className="text-sm text-gray-300">—</span>}
                    </p>
                  </div>
                  <div className="bg-rose-50/70 px-3 py-3 text-center">
                    <p className="text-[9px] font-semibold text-rose-400 uppercase tracking-wide mb-1">Orthographe</p>
                    <p className={`text-base font-bold leading-none ${scoreColor(mO)}`}>
                      {mO != null ? <>{fmt(mO)}<span className="text-[10px] font-normal opacity-60">/10</span></> : <span className="text-sm text-gray-300">—</span>}
                    </p>
                  </div>
                  <div className="bg-amber-50/70 px-3 py-3 text-center">
                    <p className="text-[9px] font-semibold text-amber-500 uppercase tracking-wide mb-1">Niv. CRPE</p>
                    <p className={`text-base font-bold leading-none ${scoreColor(mC)}`}>
                      {mC != null ? <>{fmt(mC)}<span className="text-[10px] font-normal opacity-60">/10</span></> : <span className="text-sm text-gray-300">—</span>}
                    </p>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* Vue Courbes */}
      {view === 'courbes' && (
        <div className="flex flex-col gap-5">
          {classes.map(cl => {
            const cs = CHART_STYLE[cl] || DEFAULT_CHART_STYLE;
            return (
              <NoteLineChart
                key={cl}
                rows={byClasse[cl]}
                classLabel={cl}
                borderColor={cs.borderColor}
                hdrBg={cs.hdrBg}
                labelColor={cs.labelColor}
              />
            );
          })}
        </div>
      )}
    </div>
  );
}

// ---------------------------------------------------------------------------
// ProfileView
// ---------------------------------------------------------------------------
function ProfileView({ profile, authUser, onUpdateProfile }) {
  const [editing, setEditing]   = useState(false);
  const [prenom, setPrenom]     = useState(profile?.prenom   || '');
  const [concours, setConcours] = useState(profile?.concours || '');
  const [academie, setAcademie] = useState(profile?.academie || '');
  const [loggingOut, setLoggingOut] = useState(false);

  const handleSave = () => {
    onUpdateProfile({ ...profile, prenom: prenom.trim(), concours, academie });
    setEditing(false);
  };

  const handleLogout = async () => {
    setLoggingOut(true);
    await sbClient.auth.signOut();
  };

  const initial = profile?.prenom?.[0]?.toUpperCase() || '?';

  return (
    <div className="flex-1 overflow-y-auto px-4 pt-6 pb-24">
      <h2 className="text-xl font-bold text-gray-900 mb-5">Mon compte</h2>

      {/* Avatar + email */}
      <div className="bg-white rounded-2xl border border-gray-100 shadow-sm p-5 mb-4 flex items-center gap-4">
        <div className="w-14 h-14 rounded-2xl bg-indigo-100 flex items-center justify-center flex-shrink-0">
          <span className="text-2xl font-bold text-indigo-600">{initial}</span>
        </div>
        <div className="flex-1 min-w-0">
          <p className="font-bold text-gray-900 text-lg truncate">{profile?.prenom}</p>
          <p className="text-sm text-gray-400 truncate">{authUser?.email}</p>
        </div>
      </div>

      {/* Profil CRPE */}
      <div className="bg-white rounded-2xl border border-gray-100 shadow-sm p-5 mb-4">
        <div className="flex items-center justify-between mb-4">
          <h3 className="font-semibold text-gray-800 text-sm">Profil CRPE</h3>
          {!editing ? (
            <button
              onClick={() => setEditing(true)}
              className="text-xs text-indigo-600 font-semibold hover:text-indigo-700 transition-colors"
            >
              Modifier
            </button>
          ) : (
            <div className="flex gap-3">
              <button
                onClick={() => { setEditing(false); setPrenom(profile?.prenom || ''); setConcours(profile?.concours || ''); setAcademie(profile?.academie || ''); }}
                className="text-xs text-gray-400 font-medium hover:text-gray-600 transition-colors"
              >
                Annuler
              </button>
              <button
                onClick={handleSave}
                disabled={!prenom.trim() || !concours || !academie}
                className="text-xs text-indigo-600 font-semibold hover:text-indigo-700 disabled:opacity-40 transition-colors"
              >
                Enregistrer
              </button>
            </div>
          )}
        </div>

        {editing ? (
          <div className="flex flex-col gap-4">
            <div>
              <label className="block text-xs font-semibold text-gray-400 uppercase tracking-wide mb-1.5">Prénom</label>
              <input
                type="text"
                value={prenom}
                onChange={e => setPrenom(e.target.value)}
                className="w-full px-3 py-2.5 border border-gray-200 rounded-xl text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:border-transparent"
              />
            </div>
            <div>
              <label className="block text-xs font-semibold text-gray-400 uppercase tracking-wide mb-1.5">Concours</label>
              <div className="flex flex-col gap-1.5">
                {CONCOURS_LIST.map(c => (
                  <button key={c} onClick={() => setConcours(c)}
                    className={`py-2 px-3 rounded-xl border-2 text-xs font-medium text-left transition-all ${
                      concours === c ? 'border-indigo-500 bg-indigo-50 text-indigo-700' : 'border-gray-100 text-gray-600 hover:border-gray-200'
                    }`}
                  >
                    {c}
                  </button>
                ))}
              </div>
            </div>
            <div>
              <label className="block text-xs font-semibold text-gray-400 uppercase tracking-wide mb-1.5">Académie</label>
              <select
                value={academie}
                onChange={e => setAcademie(e.target.value)}
                className="w-full px-3 py-2.5 border border-gray-200 rounded-xl text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:border-transparent bg-white"
              >
                <option value="">Choisir une académie…</option>
                {ACADEMIES_LIST.map(a => (
                  <option key={a} value={a}>{a}</option>
                ))}
              </select>
            </div>
          </div>
        ) : (
          <div className="flex flex-col">
            <div className="flex items-center justify-between py-2.5 border-b border-gray-50">
              <span className="text-xs text-gray-400 font-medium">Prénom</span>
              <span className="text-sm font-semibold text-gray-800">{profile?.prenom}</span>
            </div>
            <div className="flex items-center justify-between py-2.5 border-b border-gray-50">
              <span className="text-xs text-gray-400 font-medium">Concours</span>
              <span className="text-sm font-semibold text-gray-800">{profile?.concours}</span>
            </div>
            <div className="flex items-center justify-between py-2.5">
              <span className="text-xs text-gray-400 font-medium">Académie</span>
              <span className="text-sm font-semibold text-gray-800">{profile?.academie || '—'}</span>
            </div>
          </div>
        )}
      </div>

      {/* Déconnexion */}
      <button
        onClick={handleLogout}
        disabled={loggingOut}
        className="w-full flex items-center justify-center gap-2 py-3.5 rounded-2xl border border-red-200 text-red-500 font-semibold text-sm hover:bg-red-50 active:bg-red-100 transition-all disabled:opacity-60"
      >
        <LogOut className="w-4 h-4" />
        {loggingOut ? 'Déconnexion…' : 'Se déconnecter'}
      </button>
    </div>
  );
}

// ---------------------------------------------------------------------------
// ---------------------------------------------------------------------------
// SupportView
// ---------------------------------------------------------------------------
const SUPPORT_CATEGORIES = [
  'Problème technique',
  'Question sur les exercices',
  'Question sur mon compte',
  'Facturation',
  'Suggestion d\'amélioration',
  'Autre',
];

function SupportView({ authUser, onUnreadChange }) {
  const [category, setCategory] = useState('');
  const [message, setMessage]   = useState('');
  const [sending, setSending]   = useState(false);
  const [sent, setSent]         = useState(false);
  const [error, setError]       = useState('');
  const [tickets, setTickets]   = useState([]);
  const [loadingTickets, setLoadingTickets] = useState(true);

  const prenom = authUser?.user_metadata?.prenom || '';
  const email  = authUser?.email || '';

  useEffect(() => {
    loadTickets();
  }, []);

  async function loadTickets() {
    setLoadingTickets(true);
    try {
      const { data } = await sbClient.from('support_tickets')
        .select('*')
        .order('created_at', { ascending: false });
      const list = data || [];
      setTickets(list);
      const unread = list.filter(t => t.admin_reply && !t.user_seen_reply);
      if (unread.length > 0) {
        await sbClient.from('support_tickets')
          .update({ user_seen_reply: true })
          .in('id', unread.map(t => t.id));
        onUnreadChange?.(0);
      }
    } catch {}
    setLoadingTickets(false);
  }

  async function handleSubmit(e) {
    e.preventDefault();
    if (!category || !message.trim()) { setError('Veuillez remplir tous les champs.'); return; }
    setSending(true); setError('');
    const { error: err } = await sbClient.from('support_tickets').insert({
      user_id: authUser.id,
      user_email: email,
      user_prenom: prenom,
      category,
      message: message.trim(),
    });
    if (err) { setError('Une erreur est survenue. Réessayez.'); setSending(false); return; }
    setSent(true); setSending(false);
    setCategory(''); setMessage('');
    loadTickets();
  }

  const statusLabel = { open: 'En attente', answered: 'Répondu', closed: 'Clôturé' };
  const statusColor = { open: 'bg-amber-50 text-amber-700', answered: 'bg-emerald-50 text-emerald-700', closed: 'bg-gray-100 text-gray-500' };

  return (
    <div className="flex-1 overflow-y-auto px-4 pt-6 pb-24">
      <div className="max-w-lg mx-auto">
        <div className="flex items-center gap-3 mb-6">
          <div className="w-10 h-10 rounded-xl bg-indigo-50 flex items-center justify-center">
            <HelpCircle className="w-5 h-5 text-indigo-600" />
          </div>
          <div>
            <h1 className="text-lg font-bold text-gray-900">Support</h1>
            <p className="text-xs text-gray-400">Une question ? On vous répond.</p>
          </div>
        </div>

        {/* Form */}
        <div className="bg-white border border-gray-100 rounded-2xl p-5 mb-6 shadow-sm">
          <h2 className="text-sm font-700 text-gray-700 mb-4 font-semibold">Envoyer un message</h2>
          {sent ? (
            <div className="flex flex-col items-center gap-3 py-6 text-center">
              <CheckCircle2 className="w-10 h-10 text-emerald-500" />
              <p className="font-semibold text-gray-800">Message envoyé !</p>
              <p className="text-sm text-gray-500">Nous vous répondrons par e-mail sous 24–48h.</p>
              <button onClick={() => setSent(false)} className="mt-2 text-sm text-indigo-600 font-semibold">
                Envoyer un autre message
              </button>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="flex flex-col gap-4">
              <div>
                <label className="block text-xs font-semibold text-gray-600 mb-1.5">Catégorie</label>
                <select
                  value={category}
                  onChange={e => setCategory(e.target.value)}
                  className="w-full border border-gray-200 rounded-xl px-3 py-2.5 text-sm text-gray-800 bg-gray-50 focus:outline-none focus:border-indigo-400"
                >
                  <option value="">Choisir une catégorie…</option>
                  {SUPPORT_CATEGORIES.map(c => <option key={c} value={c}>{c}</option>)}
                </select>
              </div>
              <div>
                <label className="block text-xs font-semibold text-gray-600 mb-1.5">Message</label>
                <textarea
                  value={message}
                  onChange={e => setMessage(e.target.value)}
                  rows={5}
                  placeholder="Décrivez votre question ou problème…"
                  className="w-full border border-gray-200 rounded-xl px-3 py-2.5 text-sm text-gray-800 bg-gray-50 focus:outline-none focus:border-indigo-400 resize-none"
                />
              </div>
              {error && <p className="text-xs text-red-500">{error}</p>}
              <button
                type="submit"
                disabled={sending}
                className="flex items-center justify-center gap-2 bg-indigo-600 text-white text-sm font-semibold py-3 rounded-xl hover:bg-indigo-700 transition-colors disabled:opacity-50"
              >
                {sending ? <Loader2 className="w-4 h-4 animate-spin" /> : <Send className="w-4 h-4" />}
                {sending ? 'Envoi…' : 'Envoyer'}
              </button>
            </form>
          )}
        </div>

        {/* Ticket history */}
        {!loadingTickets && tickets.length > 0 && (
          <div>
            <h2 className="text-sm font-semibold text-gray-500 mb-3">Vos messages</h2>
            <div className="flex flex-col gap-3">
              {tickets.map(t => (
                <div key={t.id} className="bg-white border border-gray-100 rounded-2xl p-4 shadow-sm">
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-xs font-semibold text-gray-500">{t.category}</span>
                    <span className={`text-xs font-semibold px-2 py-0.5 rounded-full ${statusColor[t.status]}`}>
                      {statusLabel[t.status]}
                    </span>
                  </div>
                  <p className="text-sm text-gray-700 leading-relaxed">{t.message}</p>
                  {t.admin_reply && (
                    <div className="mt-3 pt-3 border-t border-gray-100">
                      <p className="text-xs font-semibold text-indigo-600 mb-1">Réponse PassCRPE</p>
                      <p className="text-sm text-gray-700 leading-relaxed">{t.admin_reply}</p>
                    </div>
                  )}
                  <p className="text-xs text-gray-300 mt-2">{new Date(t.created_at).toLocaleDateString('fr-FR')}</p>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

// BottomNav
// ---------------------------------------------------------------------------
function BottomNav({ active, onChange, unreadSupport = 0 }) {
  const tabs = [
    { id: 'home',    label: 'Accueil',    icon: Home          },
    { id: 'chat',    label: 'Session',    icon: MessageCircle },
    { id: 'history', label: 'Historique', icon: BookOpen      },
    { id: 'stats',   label: 'Stats',      icon: BarChart2     },
    { id: 'support', label: 'Support',    icon: HelpCircle    },
    { id: 'profile', label: 'Profil',     icon: User          },
  ];
  return (
    <nav className="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-100 z-40">
      <div className="flex max-w-3xl mx-auto">
        {tabs.map(({ id, label, icon: Icon }) => (
          <button
            key={id}
            onClick={() => onChange(id)}
            className={`flex-1 flex flex-col items-center gap-1 py-3 text-xs font-medium transition-all ${
              active === id ? 'text-indigo-600' : 'text-gray-400 hover:text-gray-600'
            }`}
          >
            <div className="relative">
              <Icon className={`w-5 h-5 ${active === id ? 'stroke-[2.5]' : ''}`} />
              {id === 'support' && unreadSupport > 0 && (
                <span className="absolute -top-0.5 -right-0.5 w-2 h-2 bg-red-500 rounded-full border border-white" />
              )}
            </div>
            {label}
            {active === id && <div className="w-1 h-1 rounded-full bg-indigo-600" />}
          </button>
        ))}
      </div>
    </nav>
  );
}

// ---------------------------------------------------------------------------
// App root
// ---------------------------------------------------------------------------
// RevisionSetupView — choose how many items to review
// ---------------------------------------------------------------------------
function RevisionSetupView({ onStart, onBack }) {
  const allData = storage.get('crpe_keywords') || [];
  const allWords = [...new Set(allData.flatMap(k => k.words || []))];
  const allTournures = [...new Set(allData.flatMap(k => k.tournures || []))];
  const pool = [
    ...allWords.map(w => ({ type: 'mot', value: w })),
    ...allTournures.map(t => ({ type: 'tournure', value: t })),
  ];
  const total = pool.length;
  const defaultCount = Math.min(10, total) || 1;
  const [count, setCount] = useState(defaultCount);

  const presets = [...new Set([5, 10, 15, 20, total].filter(n => n > 0 && n <= total))];

  if (total === 0) {
    return (
      <div className="flex-1 overflow-y-auto px-4 pt-6 pb-24">
        <button onClick={onBack} className="flex items-center gap-1.5 text-gray-500 text-sm mb-6 hover:text-gray-700 transition-colors">
          <ChevronLeft className="w-4 h-4" /> Retour
        </button>
        <EmptyState
          icon={RotateCcw}
          title="Aucun contenu à réviser"
          subtitle="Complétez d'abord des sessions Apprendre à rédiger pour alimenter votre banque de révision."
        />
      </div>
    );
  }

  const handleStart = () => {
    const shuffled = [...pool].sort(() => Math.random() - 0.5).slice(0, count);
    onStart(shuffled);
  };

  return (
    <div className="flex-1 overflow-y-auto px-4 pt-6 pb-24">
      <button onClick={onBack} className="flex items-center gap-1.5 text-gray-500 text-sm mb-6 hover:text-gray-700 transition-colors">
        <ChevronLeft className="w-4 h-4" /> Retour
      </button>

      <div className="mb-6">
        <div className="w-12 h-12 rounded-xl bg-amber-100 flex items-center justify-center mb-3">
          <RotateCcw className="w-6 h-6 text-amber-600" />
        </div>
        <h1 className="text-2xl font-bold text-gray-900">Révision</h1>
        <p className="text-gray-500 text-sm mt-1">Mots clés & tournures de phrases</p>
      </div>

      <div className="bg-white rounded-2xl border border-gray-100 shadow-sm p-4 mb-6 flex gap-0">
        <div className="flex-1 text-center py-2">
          <p className="text-2xl font-bold text-amber-600">{allWords.length}</p>
          <p className="text-xs text-gray-500 mt-0.5">mots clés</p>
        </div>
        <div className="w-px bg-gray-100 my-2" />
        <div className="flex-1 text-center py-2">
          <p className="text-2xl font-bold text-amber-600">{allTournures.length}</p>
          <p className="text-xs text-gray-500 mt-0.5">tournures</p>
        </div>
        <div className="w-px bg-gray-100 my-2" />
        <div className="flex-1 text-center py-2">
          <p className="text-2xl font-bold text-gray-700">{total}</p>
          <p className="text-xs text-gray-500 mt-0.5">au total</p>
        </div>
      </div>

      <p className="text-sm font-semibold text-gray-700 mb-3">Combien voulez-vous réviser ?</p>
      <div className="flex flex-wrap gap-2 mb-6">
        {presets.map(n => (
          <button
            key={n}
            onClick={() => setCount(n)}
            className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all ${count === n ? 'bg-amber-500 text-white' : 'bg-white border border-gray-200 text-gray-600 hover:border-amber-300'}`}
          >
            {n === total && n !== 5 && n !== 10 && n !== 15 && n !== 20 ? `Tout (${total})` : n === total ? `${n} (tout)` : n}
          </button>
        ))}
      </div>

      <button
        onClick={handleStart}
        className="w-full bg-amber-500 text-white py-3 rounded-xl font-semibold hover:bg-amber-600 active:bg-amber-700 transition-all flex items-center justify-center gap-2"
      >
        Commencer la révision <ChevronRight className="w-4 h-4" />
      </button>
    </div>
  );
}

// ---------------------------------------------------------------------------
// RevisionExerciseView — flashcard memorize → recall → results
// ---------------------------------------------------------------------------
function RevisionExerciseView({ items, onBack, onRestart }) {
  const [phase, setPhase] = useState('memorize');
  const [currentIndex, setCurrentIndex] = useState(0);
  const [userAnswers, setUserAnswers] = useState([]);
  const [currentInput, setCurrentInput] = useState('');
  const inputRef = useRef(null);

  const progress = (currentIndex + 1) / items.length;

  const advanceMemorize = () => {
    if (currentIndex < items.length - 1) {
      setCurrentIndex(i => i + 1);
    } else {
      setPhase('recall');
      setCurrentIndex(0);
      setTimeout(() => inputRef.current?.focus(), 200);
    }
  };

  const submitRecall = () => {
    const newAnswers = [...userAnswers, currentInput.trim()];
    setUserAnswers(newAnswers);
    setCurrentInput('');
    if (currentIndex < items.length - 1) {
      setCurrentIndex(i => i + 1);
      setTimeout(() => inputRef.current?.focus(), 100);
    } else {
      setPhase('results');
    }
  };

  const normalize = (s) => (s || '').toLowerCase().trim()
    .normalize('NFD').replace(/[̀-ͯ]/g, '')
    .replace(/['"«»""]/g, '')
    .replace(/\s+/g, ' ');

  if (phase === 'memorize') {
    const item = items[currentIndex];
    return (
      <div className="flex-1 flex flex-col px-4 pt-5 pb-24">
        <div className="flex items-center justify-between mb-4">
          <button onClick={onBack} className="text-gray-400 hover:text-gray-600 transition-colors">
            <X className="w-5 h-5" />
          </button>
          <p className="text-xs font-semibold text-gray-400 uppercase tracking-wide">Mémorisez</p>
          <p className="text-sm text-gray-500 font-medium">{currentIndex + 1}/{items.length}</p>
        </div>

        <div className="h-1 bg-gray-100 rounded-full mb-6">
          <div className="h-1 bg-amber-400 rounded-full transition-all duration-300" style={{ width: `${progress * 100}%` }} />
        </div>

        <div className="flex-1 flex items-center justify-center">
          <div className="w-full bg-white rounded-3xl border border-gray-100 shadow-lg px-8 py-10 text-center">
            <span className={`inline-block text-xs font-semibold px-3 py-1 rounded-full mb-5 ${item.type === 'mot' ? 'bg-rose-100 text-rose-600' : 'bg-indigo-100 text-indigo-600'}`}>
              {item.type === 'mot' ? 'Mot clé' : 'Tournure de phrase'}
            </span>
            <p className="text-xl font-bold text-gray-900 leading-relaxed">{item.value}</p>
          </div>
        </div>

        <button
          onClick={advanceMemorize}
          className="mt-6 w-full bg-amber-500 text-white py-3 rounded-xl font-semibold hover:bg-amber-600 active:bg-amber-700 transition-all flex items-center justify-center gap-2"
        >
          {currentIndex < items.length - 1 ? 'Suivant' : 'Tester ma mémoire →'}
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>
    );
  }

  if (phase === 'recall') {
    const item = items[currentIndex];
    return (
      <div className="flex-1 flex flex-col px-4 pt-5 pb-24">
        <div className="flex items-center justify-between mb-4">
          <button onClick={onBack} className="text-gray-400 hover:text-gray-600 transition-colors">
            <X className="w-5 h-5" />
          </button>
          <p className="text-xs font-semibold text-indigo-500 uppercase tracking-wide">De mémoire</p>
          <p className="text-sm text-gray-500 font-medium">{currentIndex + 1}/{items.length}</p>
        </div>

        <div className="h-1 bg-gray-100 rounded-full mb-6">
          <div className="h-1 bg-indigo-400 rounded-full transition-all duration-300" style={{ width: `${progress * 100}%` }} />
        </div>

        <div className="flex-1 flex flex-col justify-center gap-5">
          <div className="bg-white rounded-2xl border border-gray-100 shadow-sm p-5 text-center">
            <span className={`inline-block text-xs font-semibold px-3 py-1 rounded-full mb-3 ${item.type === 'mot' ? 'bg-rose-100 text-rose-600' : 'bg-indigo-100 text-indigo-600'}`}>
              {item.type === 'mot' ? 'Mot clé' : 'Tournure de phrase'} {currentIndex + 1}
            </span>
            <p className="text-sm text-gray-500">Écrivez ce que vous avez mémorisé</p>
          </div>

          <textarea
            ref={inputRef}
            value={currentInput}
            onChange={e => setCurrentInput(e.target.value)}
            onKeyDown={e => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); submitRecall(); } }}
            placeholder="Votre réponse… (Entrée pour valider)"
            autoFocus
            rows={3}
            className="w-full resize-none border border-gray-200 rounded-xl px-4 py-3 text-sm text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:border-transparent transition-all"
          />
        </div>

        <button
          onClick={submitRecall}
          className="mt-4 w-full bg-indigo-600 text-white py-3 rounded-xl font-semibold hover:bg-indigo-700 active:bg-indigo-800 transition-all"
        >
          {currentIndex < items.length - 1 ? 'Valider' : 'Voir les résultats →'}
        </button>
      </div>
    );
  }

  if (phase === 'results') {
    const results = items.map((item, i) => ({
      item,
      answer: userAnswers[i] || '',
      correct: normalize(userAnswers[i]) === normalize(item.value),
    }));
    const score = results.filter(r => r.correct).length;
    const pct = score / items.length;

    return (
      <div className="flex-1 overflow-y-auto px-4 pt-6 pb-24">
        <h2 className="text-xl font-bold text-gray-900 mb-4">Résultats</h2>

        <div className={`rounded-2xl p-5 mb-6 text-center ${pct === 1 ? 'bg-emerald-50 border border-emerald-100' : pct >= 0.6 ? 'bg-amber-50 border border-amber-100' : 'bg-red-50 border border-red-100'}`}>
          <p className={`text-4xl font-bold ${pct === 1 ? 'text-emerald-600' : pct >= 0.6 ? 'text-amber-600' : 'text-red-500'}`}>
            {score}/{items.length}
          </p>
          <p className="text-sm text-gray-500 mt-1">
            {pct === 1 ? 'Parfait, tout bon !' : pct >= 0.6 ? 'Bon travail !' : 'À retravailler'}
          </p>
        </div>

        <div className="flex flex-col gap-3 mb-6">
          {results.map((r, i) => (
            <div key={i} className={`bg-white rounded-2xl border p-4 ${r.correct ? 'border-emerald-100' : 'border-red-100'}`}>
              <div className="flex items-center justify-between mb-2">
                <span className={`text-xs font-semibold px-2 py-0.5 rounded-full ${r.item.type === 'mot' ? 'bg-rose-100 text-rose-600' : 'bg-indigo-100 text-indigo-600'}`}>
                  {r.item.type === 'mot' ? 'Mot clé' : 'Tournure'}
                </span>
                <span className={`text-xs font-bold ${r.correct ? 'text-emerald-600' : 'text-red-500'}`}>
                  {r.correct ? '✓ Correct' : '✗ Incorrect'}
                </span>
              </div>
              <p className="text-sm font-semibold text-gray-800">{r.item.value}</p>
              {!r.correct && r.answer && (
                <p className="text-xs text-gray-400 mt-1 italic">Votre réponse : {r.answer}</p>
              )}
              {!r.correct && !r.answer && (
                <p className="text-xs text-gray-400 mt-1 italic">(pas de réponse)</p>
              )}
            </div>
          ))}
        </div>

        <div className="flex flex-col gap-2">
          <button
            onClick={onRestart}
            className="w-full py-3 rounded-xl font-semibold border-2 border-amber-400 text-amber-600 hover:bg-amber-50 active:bg-amber-100 transition-all"
          >
            Nouvelle session de révision
          </button>
          <button
            onClick={onBack}
            className="w-full py-3 rounded-xl font-semibold bg-gray-100 text-gray-600 hover:bg-gray-200 transition-all"
          >
            Terminer
          </button>
        </div>
      </div>
    );
  }
}

// ---------------------------------------------------------------------------
function AppContent({ authUser }) {
  // Si un utilisateur différent se connecte, effacer les données locales du précédent.
  // Ce code s'exécute de façon synchrone au moment du rendu, avant que les composants
  // enfants (HomeView, ChatView, HistoryView, StatsView) ne lisent localStorage.
  const _prevUserId = storage.get('crpe_user_id');
  if (authUser?.id && _prevUserId !== authUser.id) {
    storage.set('crpe_session_maths', null);
    storage.set('crpe_session_francais', null);
    storage.set('crpe_session_francais_revision', null);
    storage.set('crpe_profile', null);
    storage.set('crpe_keywords', null);
  }
  if (authUser?.id) storage.set('crpe_user_id', authUser.id);

  const [profile, setProfile] = useState(null);
  const [ready, setReady] = useState(false);
  const [activeTab, setActiveTab] = useState('home');
  const [chatMatiere, setChatMatiere] = useState(null);
  const [sessionKey, setSessionKey] = useState(0);
  const [showTopicPicker, setShowTopicPicker] = useState(false);
  const [showClassPicker, setShowClassPicker] = useState(false);

  const [francaisTopic, setFrancaisTopic] = useState(null);
  const [sessionNiveau, setSessionNiveau] = useState(null);
  const [francaisMode, setFrancaisMode] = useState(null);
  const [pendingStart, setPendingStart] = useState(null);
  const [showBanqueView, setShowBanqueView] = useState(false);
  const [showMathBanqueView, setShowMathBanqueView] = useState(false);
  const [banqueSession, setBanqueSession] = useState(null);
  const [autoResumeBanque, setAutoResumeBanque] = useState(false);
  const [dbFreeQsUsed, setDbFreeQsUsed] = useState(null);
  const [dbPaid, setDbPaid]             = useState(null); // null = chargement
  const [unreadSupport, setUnreadSupport] = useState(0);

  // isPaid : DB prioritaire, fallback localStorage si DB indisponible
  const isPaidApp   = dbPaid !== null ? dbPaid : storage.get('crpe_paid') === true;
  const isLockedApp = dbFreeQsUsed !== null && !isPaidApp && dbFreeQsUsed >= FREE_QUESTION_LIMIT;

  const trialEndedFired = useRef(false);
  useEffect(() => {
    if (!isLockedApp || trialEndedFired.current) return;
    trialEndedFired.current = true;
    sbClient.auth.getSession().then(({ data }) => {
      const token = data.session?.access_token;
      if (!token) return;
      fetch('/api/klaviyo/trial-ended', {
        method: 'POST',
        headers: { Authorization: `Bearer ${token}` },
      }).catch(() => {});
    });
  }, [isLockedApp]);

  const refreshFreeQsCount = (userId) => {
    if (!userId) return;
    fetchFreeQuestionsUsed(userId).then(count => {
      if (count !== null) setDbFreeQsUsed(count);
    });
  };

  const refreshPaidStatus = () => {
    fetchPaidStatus().then(paid => {
      if (paid !== null) {
        setDbPaid(paid);
        storage.set('crpe_paid', paid); // cache local
      }
    });
  };

  useEffect(() => {
    const saved = storage.get('crpe_profile');
    if (saved) {
      setProfile(saved);
    } else if (authUser?.user_metadata) {
      const { prenom, concours, academie } = authUser.user_metadata;
      if (prenom && concours) {
        const p = { prenom: prenom.trim(), concours, academie: academie || '' };
        storage.set('crpe_profile', p);
        setProfile(p);
      }
    }
    const userId = authUser?.id || storage.get('crpe_user_id');
    if (userId) {
      fetchLastActiveSession(userId).then(row => { if (row) setBanqueSession(row); });
      refreshFreeQsCount(userId);
      sbClient.from('support_tickets')
        .select('id', { count: 'exact', head: true })
        .eq('user_seen_reply', false)
        .not('admin_reply', 'is', null)
        .then(({ count }) => setUnreadSupport(count || 0));
    }
    refreshPaidStatus();
    setReady(false);
    setTimeout(() => setReady(true), 50);
  }, []);

  const handleOnboarding = (p) => {
    storage.set('crpe_profile', p);
    setProfile(p);
  };

  const archiveSession = (matiere) => {
    storage.set(`crpe_session_${matiere}`, null);
  };

  const handleStart = async (matiere, isNew) => {
    if (!isPaidApp) {
      const uid = authUser?.id || storage.get('crpe_user_id');
      const count = await fetchFreeQuestionsUsed(uid);
      if (count !== null) setDbFreeQsUsed(count);
      if (count !== null && count >= FREE_QUESTION_LIMIT) return;
    }
    if (!isNew) {
      const saved = storage.get(`crpe_session_${matiere}`);
      if (matiere === 'francais') {
        setFrancaisTopic(saved?.topic || null);
        setFrancaisMode(saved?.mode || null);
      }
      setSessionNiveau(saved?.niveau || null);
      setChatMatiere(matiere);
      setActiveTab('chat');
      return;
    }
    if (matiere === 'maths') {
      setShowMathBanqueView(true);
      return;
    }
    setPendingStart({ matiere, isNew });
    if (matiere === 'francais') {
      setFrancaisMode('questions');
      setShowTopicPicker(true);
    } else {
      setShowClassPicker(true);
    }
  };

  const handleResumeBanque = async () => {
    if (!banqueSession) return;
    if (!isPaidApp) {
      const uid = authUser?.id || storage.get('crpe_user_id');
      const count = await fetchFreeQuestionsUsed(uid);
      if (count !== null) setDbFreeQsUsed(count);
      if (count !== null && count >= FREE_QUESTION_LIMIT) return;
    }
    setFrancaisTopic(banqueSession.topic);
    setSessionNiveau(banqueSession.niveau);
    setFrancaisMode('banque');
    setAutoResumeBanque(true);
    setShowBanqueView(true);
  };

  const handleModeSelect = (modeId) => {
    setFrancaisMode(modeId);
    setShowModePicker(false);
    setShowTopicPicker(true);
  };

  const handleTopicSelect = (topicId) => {
    setFrancaisTopic(topicId);
    setShowTopicPicker(false);
    setShowClassPicker(true);
  };

  const handleNiveauSelect = (niveauId) => {
    setSessionNiveau(niveauId);
    setShowClassPicker(false);
    if (!pendingStart) return;
    const { matiere, isNew } = pendingStart;
    if (matiere === 'francais' && (francaisMode === 'questions' || francaisMode === 'banque')) {
      setShowBanqueView(true);
      setPendingStart(null);
      return;
    }
    if (isNew) {
      archiveSession(matiere);
      setSessionKey((k) => k + 1);
    }
    setChatMatiere(matiere);
    setActiveTab('chat');
    setPendingStart(null);
  };

  const handleNewSession = () => {
    if (!chatMatiere) return;
    setPendingStart({ matiere: chatMatiere, isNew: true });
    if (chatMatiere === 'francais') {
      setFrancaisMode('questions');
      setShowTopicPicker(true);
    } else {
      setShowClassPicker(true);
    }
  };

  const handleTabChange = (tab) => {
    if (tab === 'chat' && !chatMatiere) {
      setActiveTab('home');
      return;
    }
    setActiveTab(tab);
  };

  if (!ready) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <Loader2 className="w-8 h-8 text-indigo-500 animate-spin" />
      </div>
    );
  }

  if (!profile) return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center gap-4 px-6 text-center">
      <GraduationCap className="w-12 h-12 text-indigo-400" />
      <p className="text-gray-600 text-sm max-w-xs">
        Profil introuvable. Veuillez vous déconnecter et vous reconnecter pour récupérer vos informations.
      </p>
      <button
        onClick={async () => { await sbClient.auth.signOut(); }}
        className="px-4 py-2 bg-indigo-600 text-white rounded-xl text-sm font-semibold hover:bg-indigo-700"
      >
        Se déconnecter
      </button>
    </div>
  );

  return (
    <div className="bg-gray-50 flex flex-col overflow-hidden" style={{ height: '100dvh' }}>
      <div
        className="flex flex-col flex-1 min-h-0 max-w-3xl mx-auto w-full"
      >
        {showMathBanqueView ? (
          <MathBanqueView onBack={() => setShowMathBanqueView(false)} />
        ) : showTopicPicker ? (
          <SubjectPickerView
            onSelect={handleTopicSelect}
            onBack={() => { setShowTopicPicker(false); setPendingStart(null); }}
          />
        ) : showClassPicker ? (
          <ClassPickerView
            onSelect={handleNiveauSelect}
            onBack={() => {
              setShowClassPicker(false);
              if (pendingStart?.matiere === 'francais') setShowTopicPicker(true);
              else setPendingStart(null);
            }}
          />
        ) : showBanqueView ? (
          <BanqueQuestionsView
            topic={francaisTopic}
            niveau={sessionNiveau}
            isLocked={isLockedApp}
            onQuestionAnswered={(uid) => refreshFreeQsCount(uid)}
            onBack={() => {
              setShowBanqueView(false);
              setAutoResumeBanque(false);
              const uid = authUser?.id || storage.get('crpe_user_id');
              if (uid) {
                fetchLastActiveSession(uid).then(row => setBanqueSession(row ?? null));
                refreshFreeQsCount(uid);
              } else {
                setBanqueSession(null);
              }
            }}
            autoResume={autoResumeBanque}
            resumeRow={autoResumeBanque ? banqueSession : null}
          />
        ) : (
          <>
            {activeTab === 'home' && (
              <HomeView
                profile={profile}
                onStart={handleStart}
                banqueSession={banqueSession}
                onResumeBanque={handleResumeBanque}
                isLocked={isLockedApp}
                freeQsUsed={dbFreeQsUsed ?? 0}
                onPaymentConfirmed={refreshPaidStatus}
              />
            )}
            {activeTab === 'chat' && chatMatiere && (
              <ChatView
                key={`${chatMatiere}-${sessionKey}`}
                matiere={chatMatiere}
                profile={profile}
                sessionKey={sessionKey}
                onNewSession={handleNewSession}
                onBack={() => setActiveTab('home')}
                topic={chatMatiere === 'francais' ? francaisTopic : null}
                niveau={sessionNiveau}
                mode={chatMatiere === 'francais' ? francaisMode : null}
              />
            )}
            {activeTab === 'history' && <HistoryView />}
            {activeTab === 'stats'   && <StatsView />}
            {activeTab === 'support' && <SupportView authUser={authUser} onUnreadChange={setUnreadSupport} />}
            {activeTab === 'profile' && (
              <ProfileView
                profile={profile}
                authUser={authUser}
                onUpdateProfile={handleOnboarding}
              />
            )}
          </>
        )}
      </div>
      <BottomNav active={activeTab} onChange={handleTabChange} unreadSupport={unreadSupport} />
    </div>
  );
}

export default function App() {
  const [authUser, setAuthUser]       = useState(null);
  const [authChecked, setAuthChecked] = useState(false);

  useEffect(() => {
    sbClient.auth.getSession().then(({ data }) => {
      setAuthUser(data.session?.user ?? null);
      setAuthChecked(true);
    });
    const { data: { subscription } } = sbClient.auth.onAuthStateChange((_, session) => {
      setAuthUser(session?.user ?? null);
    });
    return () => subscription.unsubscribe();
  }, []);

  if (!authChecked) {
    return (
      <div className="flex items-center justify-center h-screen bg-gray-50">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-500" />
      </div>
    );
  }

  if (!authUser) {
    window.location.replace(
      window.location.port === '5173' ? 'http://localhost:3001' : '/'
    );
    return null;
  }

  return <AppContent authUser={authUser} />;
}
