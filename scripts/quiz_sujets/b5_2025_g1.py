# Bac+5, session 2025, groupement 1
from slib import S, Q, N, C, epreuve

YOURCENAR = ("Texte : Marguerite Yourcenar, Nouvelles orientales, « Comment Wang-Fô fut sauvé » (1963). L'Empereur reproche au vieux peintre Wang-Fô "
             "de lui avoir fait croire, par ses tableaux, à un monde plus beau que le réel.")
VOYAGE = "Exercice 1 : voyage scolaire. Organisme A : 1 500 € + 100 € par élève. Organisme B : 2 000 € + 85 € par élève."
JETONS = "Exercice 2 : trois jetons équilibrés portent 1 sur une face et 0 sur l'autre. On les lance et on additionne les nombres obtenus."
PISCINE = "Exercice 3 : une piscine. On creuse une fosse de 30 m × 15 m × 3 m ; la terre extraite foisonne (son volume augmente) de 25 %."
POD = "Sujet de sciences et technologie : le Polar POD, une plateforme océanographique dérivante dans l'océan Austral."
FERRY = "Sujet d'histoire et EMC : en CM2, l'école primaire au temps de Jules Ferry, puis la laïcité."

QUESTIONS = [
    epreuve('Épreuve écrite disciplinaire de français', 16561, [
        S('francais', 'Étude de la langue · temps et modes', Q(
            "« Tu me demandes ce que tu m'as fait, vieux Wang-Fô ? reprit l'Empereur en penchant son cou grêle. » Quelle est la forme de « en penchant » ?",
            ["Un gérondif", "Un participe passé", "Un infinitif présent", "Un imparfait"], "Un gérondif",
            "« En » + participe présent = gérondif (« participe présent en emploi adverbial » est aussi accepté). Erreur fréquente : le relever sans « en » (Lyon, Bordeaux)."), YOURCENAR),
        S('francais', 'Étude de la langue · temps et modes', Q(
            "Dans « ce que tu m'as fait », quel est l'infinitif de la forme verbale « as fait » ?",
            ["Faire", "Avoir", "Avoir fait", "Se faire"], "Faire",
            "« As fait » est le passé composé de « faire » : l'auxiliaire avoir ne donne pas l'infinitif. Ne relevez pas non plus le pronom « m' » avec le verbe (Toulouse, Nantes)."), YOURCENAR),
        S('francais', 'Étude de la langue · réécriture', Q(
            "Avec « elles » au lieu de « je » : « Le jour, assis sur un tapis dont je savais par cœur le dessin, reposant mes paumes vides sur mes genoux de soie jaune, je rêvais aux joies que me procurerait l'avenir. »",
            ["Le jour, assises sur un tapis dont elles savaient par cœur le dessin, reposant leurs paumes vides sur leurs genoux de soie jaune, elles rêvaient aux joies que leur procurerait l'avenir.",
             "Le jour, assisent sur un tapis dont elles savaient par cœur le dessin, reposant leurs paumes vides sur leurs genoux de soie jaune, elles rêvaient aux joies que leurs procurerait l'avenir.",
             "Le jour, assises sur un tapis dont elles savaient par cœur le dessin, reposant leurs paumes vides sur leurs genoux de soie jaune, elles rêvaient aux joies que leur procureraient l'avenir.",
             "Le jour, assis sur des tapis dont elles savaient par cœur les dessins, reposant leurs paumes vides sur leurs genoux de soie jaune, elles rêvaient aux joies que leur procurerait l'avenir."],
            "Le jour, assises sur un tapis dont elles savaient par cœur le dessin, reposant leurs paumes vides sur leurs genoux de soie jaune, elles rêvaient aux joies que leur procurerait l'avenir.",
            "« Assises » est un participe employé comme adjectif (pas « assisent »). « Leur » pronom est invariable. « Procurerait » reste au singulier : son sujet est « l'avenir », placé après le verbe."), YOURCENAR),
        S('francais', 'Étude de la langue · propositions', Q(
            "« À seize ans, j'ai vu se rouvrir les portes qui me séparaient du monde. » Nature de « se rouvrir les portes » ?",
            ["Subordonnée infinitive", "Subordonnée relative", "Groupe nominal COD", "Subordonnée complétive conjonctive"], "Subordonnée infinitive",
            "L'infinitif « se rouvrir » a son propre sujet (« les portes ») et dépend d'un verbe de perception (« j'ai vu »). Elle n'est « presque jamais repérée » (Aix-Marseille, Lyon)."), YOURCENAR),
        S('francais', 'Étude de la langue · nature et fonction', Q(
            "« Tu m'as menti, Wang-Fô, vieil imposteur. » Fonction de « m' » ?",
            ["COI du verbe « mentir »", "COD du verbe « mentir »", "Pronom réfléchi", "Sujet"], "COI du verbe « mentir »",
            "On ment à quelqu'un : « m' » = « à moi ». C'est un pronom personnel, complément d'objet indirect."), YOURCENAR),
        S('francais', 'Étude de la langue · nature et fonction', Q(
            "Dans la même phrase, fonction de « vieil imposteur » ?",
            ["Apposition au nom « Wang-Fô »", "Sujet du verbe « mentir »", "Attribut du sujet", "COD"], "Apposition au nom « Wang-Fô »",
            "Le groupe nominal qualifie Wang-Fô, lui-même mis en apostrophe. L'apposition est « rarement identifiée » (Reims, Corse, Montpellier)."), YOURCENAR),
        S('francais', 'Lexique · synonymes', Q(
            "« L'Empereur, en penchant son cou grêle… » Quel synonyme convient à « grêle » ?",
            ["Frêle", "Enrhumé", "Tacheté", "Musclé"], "Frêle",
            "L'adjectif « grêle » (du latin gracilis) signifie mince, fluet, fragile. Il n'a rien à voir avec la grêle, le phénomène météorologique."), YOURCENAR),
        S('francais', 'Lexique · synonymes', Q(
            "Quel synonyme convient au nom « candeur » ?",
            ["Innocence", "Grandeur", "Frivolité", "Personne"], "Innocence",
            "Candeur : naïveté, pureté, ingénuité. Un synonyme doit avoir la même nature que le mot (un nom pour un nom). Proposer plusieurs synonymes a valu zéro (Lyon, Rennes, Toulouse)."), YOURCENAR),
        S('francais', 'Lexique · formation des mots', Q(
            "Comment est formé le verbe « dégoûter » ?",
            ["Par dérivation : préfixe dé- (privation) + base goûter", "Par composition de « dé » et « goût »", "Par dérivation : base dégoût + préfixe -er", "C'est un mot simple"],
            "Par dérivation : préfixe dé- (privation) + base goûter",
            "Le préfixe dé- exprime la cessation ou la privation : dégoûter, c'est ôter le goût. « Contraire » ou « inverse » ne conviennent pas (Lyon, Bordeaux)."), YOURCENAR),
    ]),
    epreuve('Épreuve écrite disciplinaire de mathématiques', 16564, [
        S('mathematiques', 'Exercice 1 · fonctions affines', Q(
            "Pour 24 élèves, quel organisme est le plus avantageux ?",
            ["L'organisme A : 3 900 € contre 4 040 €", "L'organisme B : 4 040 € contre 3 900 €", "Ils coûtent le même prix", "L'organisme A : 2 400 €"], "L'organisme A : 3 900 € contre 4 040 €",
            "A : 1 500 + 100 × 24 = 3 900 €. B : 2 000 + 85 × 24 = 4 040 €."), VOYAGE),
        S('mathematiques', 'Exercice 1 · inéquation', N(
            "À partir de combien d'élèves l'organisme B devient-il plus avantageux ?", 34,
            "1 500 + 100x > 2 000 + 85x donne 15x > 500, x > 33,3. B est plus avantageux à partir de 34 élèves. Cette inéquation n'est réussie que par 54,7 % des candidats (Nantes)."), VOYAGE),
        S('mathematiques', 'Exercice 1 · fractions', Q(
            "La mairie paie les 2/5 du coût, la coopérative 50 % du reste, les familles le reste. Quelle part du coût total paient les familles ?",
            ["3/10", "1/2", "3/5", "1/10"], "3/10",
            "Après la mairie, il reste 3/5. La coopérative en paie la moitié : 3/10. Les familles paient 1 − 2/5 − 3/10 = 3/10."), VOYAGE),
        S('mathematiques', 'Exercice 2 · probabilités', Q(
            "Quelle est la probabilité d'obtenir une somme égale à 3 ?",
            ["1/8", "1/4", "1/3", "3/8"], "1/8",
            "8 issues équiprobables, de (0;0;0) à (1;1;1). Une seule donne 3 : 1/8."), JETONS),
        S('mathematiques', 'Exercice 2 · probabilités', Q(
            "Olivier affirme : « On a une chance sur deux d'obtenir trois faces identiques. » A-t-il raison ?",
            ["Non : la probabilité est 2/8 = 1/4", "Oui", "Non : la probabilité est 1/8", "Non : c'est impossible"], "Non : la probabilité est 2/8 = 1/4",
            "Seules (0;0;0) et (1;1;1) donnent trois faces identiques : 2 issues sur 8."), JETONS),
        S('mathematiques', 'Exercice 3 · volumes', N(
            "Avec un foisonnement de 25 %, quel volume de terre faut-il évacuer, en m³ ?", 1687.5,
            "Fosse : 30 × 15 × 3 = 1 350 m³. +25 % : 1 350 × 1,25 = 1 687,5 m³. Avec des bennes de 30 m³ : 56,25, donc 57 bennes."), PISCINE),
        S('mathematiques', 'Exercice 3 · vitesse', N(
            "Un élève nage 16 longueurs de 25 m en 10 min. Quelle est sa vitesse en km/h ?", 2.4,
            "400 m en 10 min = 40 m/min = 2 400 m/h = 2,4 km/h."), None),
        S('mathematiques', 'Exercice 3 · statistiques', N(
            "Longueurs nagées par neuf élèves : 15, 14, 10, 11, 12, 14, 11, 13, 16. Quelle est la médiane ?", 13,
            "Rangée : 10 – 11 – 11 – 12 – 13 – 14 – 14 – 15 – 16. La 5e valeur sur 9 est 13. Seuls 30,8 % des candidats ont entièrement réussi cette question (Orléans-Tours)."), None),
        S('mathematiques', 'Exercice 4 · nature des nombres', Q(
            "Pour quelles valeurs de b le quotient 45/b est-il un entier naturel ?",
            ["1, 3, 5, 9, 15 et 45", "Les multiples de 45", "3, 5 et 9 seulement", "Tous les nombres impairs"], "1, 3, 5, 9, 15 et 45",
            "Ce sont les diviseurs de 45 = 3² × 5. Question réussie par seulement 35 % des candidats (Orléans-Tours)."), None),
        S('mathematiques', 'Exercice 4 · nature des nombres', Q(
            "Pour quelle valeur de c le quotient c/45 est-il un nombre décimal non entier ?",
            ["c = 9", "c = 45", "c = 3", "c = 5"], "c = 9",
            "45 = 3² × 5. Pour que c/45 soit décimal, il faut éliminer 3² du dénominateur : c multiple de 9. Pour qu'il ne soit pas entier, c ne doit pas être multiple de 5. 9/45 = 0,2."), None),
        S('mathematiques', 'Exercice 4 · nature des nombres', Q(
            "Lequel de ces nombres est un rationnel non décimal ?",
            ["1/45", "9/45", "45/2", "45/10"], "1/45",
            "1/45 = 0,0222… : son écriture décimale ne s'arrête pas, car il reste le facteur 3 au dénominateur. 9/45 = 0,2 ; 45/2 = 22,5 ; 45/10 = 4,5 sont décimaux."), None),
        S('mathematiques', 'Exercice 6 · pyramide', Q(
            "SABCD est une pyramide à base carrée de côté 4 cm, aux faces latérales équilatérales. Pourquoi le triangle ASC est-il rectangle en S ?",
            ["AC² = 32 et SA² + SC² = 16 + 16 = 32 : réciproque de Pythagore", "Parce que la base est un carré", "Parce que les faces sont équilatérales, tous les angles valent 90°", "Par le théorème de Thalès"],
            "AC² = 32 et SA² + SC² = 16 + 16 = 32 : réciproque de Pythagore",
            "AC est la diagonale du carré : AC² = 4² + 4² = 32. Comme SA² + SC² = AC², le triangle est rectangle en S, et isocèle car SA = SC. Question pleinement réussie par 11,5 % des candidats (Orléans-Tours)."), None),
    ]),
    epreuve("Épreuve écrite d'application (sciences, histoire-géographie-EMC ou arts)", 16558, [
        # ── Sciences ──
        S('technologie', 'Sciences · le Polar POD', Q(
            "Pourquoi le Polar POD a-t-il une structure en treillis ?",
            ["Pour être rigide tout en restant léger, et offrir peu de prise au vent et aux vagues", "Pour être plus lourd et couler plus vite", "Pour décorer la plateforme", "Pour stocker de l'eau"],
            "Pour être rigide tout en restant léger, et offrir peu de prise au vent et aux vagues",
            "Le treillis (assemblage de barres en triangles) est une solution technique classique : ponts, grues, pylônes."), POD),
        S('technologie', "Sciences · l'énergie du Polar POD", Q(
            "Quelles sources d'énergie renouvelables le Polar POD utilise-t-il ?",
            ["Le vent, le soleil et le courant marin", "Le pétrole et le charbon", "Le nucléaire", "Uniquement des batteries rechargées à terre"], "Le vent, le soleil et le courant marin",
            "Les éoliennes et les panneaux solaires produisent l'électricité stockée dans des batteries ; le courant circumpolaire fait dériver la plateforme sans moteur."), POD),
        S('technologie', 'Sciences · la programmation', Q(
            "Un programme doit détecter en permanence la présence d'un animal. Sans quelle instruction ne teste-t-il la présence qu'une seule fois ?",
            ["La boucle « répéter indéfiniment »", "Le bloc « attendre 1 seconde »", "Le bloc « afficher »", "La condition « si… alors »"], "La boucle « répéter indéfiniment »",
            "Sans boucle, le programme s'exécute une seule fois. Remédiation proposée : faire relire le programme à voix haute en langage naturel (Bordeaux, Paris)."), POD),
        S('physique_chimie', 'Sciences · le poids', N(
            "Le Polar POD a une masse de 1 000 tonnes ; g = 9,81 N/kg. Quel est son poids, en newtons ?", 9810000,
            "P = m × g = 1 000 000 kg × 9,81 N/kg = 9 810 000 N. La masse (en kg) et le poids (une force, en N) ne sont pas la même grandeur."), POD),
        S('physique_chimie', 'Sciences · la flottaison', Q(
            "Le Polar POD flotte à l'équilibre, soumis à son poids et à la poussée d'Archimède. Que peut-on dire de ces deux forces ?",
            ["Même direction verticale, même valeur, sens opposés : elles se compensent", "Le poids est plus grand que la poussée", "Elles ont le même sens", "La poussée d'Archimède est horizontale"],
            "Même direction verticale, même valeur, sens opposés : elles se compensent",
            "Le poids est dirigé vers le bas, la poussée d'Archimède vers le haut. Si elles se compensent, l'objet flotte à l'équilibre."), POD),
        S('physique_chimie', "Sciences · l'atome", Q(
            "L'atome d'oxygène (¹⁶₈O) a 8 protons. Combien a-t-il de neutrons et d'électrons ?",
            ["8 neutrons et 8 électrons", "16 neutrons et 8 électrons", "8 neutrons et 16 électrons", "16 neutrons et 16 électrons"], "8 neutrons et 8 électrons",
            "Neutrons : 16 − 8 = 8. L'atome est neutre : autant d'électrons que de protons. L'ion O²⁻ a 2 électrons de plus, soit 10."), POD),
        S('svt', 'Sciences · météorologie et climat', Q(
            "Quelle différence y a-t-il entre la météorologie et le climat ?",
            ["La météo décrit le temps en un lieu sur une courte durée ; le climat, les conditions moyennes d'une région sur au moins 30 ans", "Ce sont deux synonymes", "Le climat décrit le temps de demain", "La météo s'étudie sur 30 ans"],
            "La météo décrit le temps en un lieu sur une courte durée ; le climat, les conditions moyennes d'une région sur au moins 30 ans",
            "La différence tient à la durée et à l'échelle spatiale (Bordeaux, Corse)."), POD),
        S('svt', "Sciences · l'effet de serre", Q(
            "Lequel de ces gaz n'est pas un gaz à effet de serre ?",
            ["Le dioxygène", "Le dioxyde de carbone", "Le méthane", "La vapeur d'eau"], "Le dioxygène",
            "L'effet de serre est un phénomène naturel : certains gaz (CO₂, méthane, vapeur d'eau, protoxyde d'azote) retiennent une partie du rayonnement infrarouge émis par le sol."), POD),
        S('svt', 'Sciences · le carbone dans l\'océan', Q(
            "Comment le carbone capté par les diatomées peut-il se retrouver au fond de l'océan ?",
            ["Les diatomées captent le CO₂ par photosynthèse, le krill les mange, les baleines mangent le krill, et leur corps coule après leur mort", "Les diatomées rejettent du carbone dans l'air", "Le krill produit du pétrole", "Les baleines respirent sous l'eau"],
            "Les diatomées captent le CO₂ par photosynthèse, le krill les mange, les baleines mangent le krill, et leur corps coule après leur mort",
            "C'est une chaîne alimentaire : le carbone passe d'un maillon à l'autre, puis est stocké au fond de l'océan."), POD),
        # ── Histoire et EMC ──
        S('histoire_geographie', "Histoire · l'école de Jules Ferry", Q(
            "Que prévoit la loi du 28 mars 1882 ?",
            ["L'instruction obligatoire et la laïcité de l'enseignement primaire public", "La gratuité de l'école", "La séparation des Églises et de l'État", "La laïcisation du personnel enseignant"],
            "L'instruction obligatoire et la laïcité de l'enseignement primaire public",
            "Gratuité : 1881. Obligation et laïcité des programmes : 1882. Laïcisation du personnel : loi Goblet de 1886. Séparation des Églises et de l'État : 1905."), FERRY),
        S('histoire_geographie', "Histoire · l'école de Jules Ferry", Q(
            "Sous quel régime politique Jules Ferry fait-il voter les lois scolaires ?",
            ["La IIIe République", "La Ve République", "Le Second Empire", "La IIe République"], "La IIIe République",
            "Proclamée en 1870, la IIIe République s'enracine dans les années 1880. Les jurys relèvent des contresens comme « les lois Ferry répondent à la Constitution de 1958 » (Clermont-Ferrand)."), FERRY),
        S('histoire_geographie', "Histoire · l'école de Jules Ferry", Q(
            "Quelle matière remplace l'instruction morale et religieuse dans les programmes de 1882 ?",
            ["L'instruction morale et civique", "Le catéchisme", "Le latin", "La gymnastique"], "L'instruction morale et civique",
            "L'école doit former des citoyens attachés à la République : morale laïque, instruction civique, symboles (Marianne, drapeau, devise)."), FERRY),
        S('histoire_geographie', "Histoire · l'école de Jules Ferry", Q(
            "Dans les villages, quel bâtiment montre que « l'école est au cœur de la République » ?",
            ["La mairie-école", "L'église", "Le château", "La caserne"], "La mairie-école",
            "Le dossier contenait une carte postale de la mairie-école d'Arcy-sur-Cure (1909). La devise est inscrite sur les frontons des édifices publics à partir de 1880."), FERRY),
        S('emc', 'EMC · la laïcité', Q(
            "Sur quels deux fondements repose la laïcité ?",
            ["La séparation des Églises et de l'État et la neutralité de la puissance publique", "L'interdiction des religions et l'obligation de l'athéisme", "La religion d'État et la liberté de culte", "L'égalité filles-garçons et la gratuité"],
            "La séparation des Églises et de l'État et la neutralité de la puissance publique",
            "Elle garantit la liberté de conscience et l'égalité de tous. Elle ne se réduit pas à « la liberté de croire ou de ne pas croire » (Lille, Aix-Marseille)."), FERRY),
        S('emc', 'EMC · la laïcité', Q(
            "À quelle date a lieu la journée nationale de la laïcité ?",
            ["Le 9 décembre", "Le 14 juillet", "Le 8 mai", "Le 11 novembre"], "Le 9 décembre",
            "Elle commémore la loi du 9 décembre 1905 de séparation des Églises et de l'État."), FERRY),
        S('emc', 'EMC · la laïcité', Q(
            "Comment utiliser la Charte de la laïcité avec des CM2 ?",
            ["Choisir quelques articles et les confronter aux représentations des élèves et à des situations concrètes", "La faire apprendre par cœur en entier", "La lire une fois à voix haute sans commentaire", "L'afficher sans en parler"],
            "Choisir quelques articles et les confronter aux représentations des élèves et à des situations concrètes",
            "Le jury attendait « la dimension expérientielle de la pédagogie de la laïcité » : saynètes, débat réglé, dilemmes, à partir des affiches d'élèves (Lyon, Aix-Marseille)."), FERRY),
        S('emc', 'EMC · valeurs et principes', Q(
            "Selon le programme d'EMC, quelles sont les quatre valeurs et principes majeurs de la République ?",
            ["La liberté, l'égalité, la fraternité et la laïcité", "La paix, la justice, l'ordre et le travail", "La liberté, la sécurité, la propriété et la fraternité", "L'égalité, la solidarité, le respect et la politesse"],
            "La liberté, l'égalité, la fraternité et la laïcité",
            "Valeur, principe et règle de vie ne sont pas synonymes : la confusion est fréquente dans les copies (Bordeaux, Orléans-Tours)."), FERRY),
        # ── Arts ──
        S('arts', "Arts plastiques · l'écrit dans l'art", Q(
            "Jacques Villeglé a réalisé « Rue Michel Le Comte, septembre » (1980). Quel matériau utilise-t-il ?",
            ["Des affiches de rue lacérées, marouflées sur toile", "Des lettres découpées dans le bois", "De la peinture à l'huile", "Des photographies retouchées"],
            "Des affiches de rue lacérées, marouflées sur toile",
            "Villeglé, figure du Nouveau Réalisme, récupère des affiches déchirées dans la rue : les lettres et mots fragmentés deviennent des éléments plastiques."),
          "Dossier d'arts plastiques (cycle 2) : « une exploration plastique de l'écrit », avec Alechinsky, Joël Ducorroy et Jacques Villeglé."),
        S('arts', "Arts plastiques · l'écrit dans l'art", Q(
            "Dans une séance sur « l'écrit dans l'art », que peut devenir une lettre ?",
            ["Un élément plastique, par sa forme, sa taille, sa couleur et sa place, en plus de son sens", "Uniquement un signe à lire", "Un objet interdit en arts plastiques", "Une simple légende sous l'œuvre"],
            "Un élément plastique, par sa forme, sa taille, sa couleur et sa place, en plus de son sens",
            "Claude Reyt (document 3) : l'écriture peut s'intégrer à la surface peinte, servir de décor, ou prendre une fonction plastique à côté de son rôle signifiant."),
          "Document 3 : Claude Reyt, Les arts plastiques à l'école, « La lettre comme élément plastique »."),
        S('arts', 'Univers sonores · cycle 1', Q(
            "Une séance sur la comptine « Un canard a dit à sa cane » en petite section, période 1 : peu d'élèves chantent, beaucoup s'agitent. Que conseillent les ressources pour les 2-3 ans ?",
            ["Des morceaux courts, des jeux chantés avec des gestes, et l'imitation de l'adulte", "Une longue écoute assise en silence", "L'apprentissage de la partition", "Un chant à plusieurs voix"],
            "Des morceaux courts, des jeux chantés avec des gestes, et l'imitation de l'adulte",
            "À cet âge, l'attention est brève et l'enfant apprend en bougeant et en imitant. Le programme de maternelle demande d'abord d'explorer sa voix et de chanter avec les autres."),
          "Dossier « univers sonores » (cycle 1) : une fiche de préparation à analyser et le document « La danse chez les petits et tout-petits »."),
    ]),
    # ── Ajout : questions complémentaires tirées du même sujet ──
    epreuve('Épreuve écrite disciplinaire de français', 16561, [
        S('francais', 'Étude de la langue · temps et modes', Q(
            "« … reprit l'Empereur en penchant son cou grêle vers le vieil homme qui l'écoutait. » Temps et mode de « reprit » ?",
            ["Passé simple de l'indicatif", "Présent de l'indicatif", "Imparfait de l'indicatif", "Passé composé"], "Passé simple de l'indicatif",
            "Infinitif : reprendre. « Reprit » a parfois été pris pour un présent (Lyon, Besançon)."), YOURCENAR),
        S('francais', 'Étude de la langue · temps et modes', Q(
            "Dans la même phrase, temps et mode de « écoutait » ?",
            ["Imparfait de l'indicatif", "Passé simple", "Conditionnel présent", "Présent du subjonctif"], "Imparfait de l'indicatif",
            "Terminaison -ait : imparfait, temps de l'arrière-plan du récit."), YOURCENAR),
        S('francais', 'Étude de la langue · nature et fonction', Q(
            "« … secoué sur des routes dont je ne prévoyais ni la boue ni les pierres… » Fonction de « dont » ?",
            ["Complément des noms « la boue » et « les pierres »", "COD de « prévoyais »", "Sujet", "Complément circonstanciel de lieu"], "Complément des noms « la boue » et « les pierres »",
            "Test : « je ne prévoyais ni la boue ni les pierres de la route ». « De la route » complète les noms (Bordeaux)."), YOURCENAR),
        S('francais', 'Étude de la langue · nature et fonction', Q(
            "« J'ai parcouru les provinces de l'Empire. » Fonction de « de l'Empire » ?",
            ["Complément du nom « provinces »", "Complément circonstanciel de lieu", "COI", "Attribut du COD"], "Complément du nom « provinces »",
            "Le groupe prépositionnel précise de quelles provinces il s'agit : il complète le nom."), YOURCENAR),
        S('francais', 'Étude de la langue · propositions', Q(
            "« … je suis monté sur la terrasse du palais pour regarder les nuages, mais ils étaient moins beaux que ceux de tes crépuscules. » Nature de « que ceux de tes crépuscules » ?",
            ["Subordonnée circonstancielle de comparaison (elliptique du verbe)", "Subordonnée relative", "Subordonnée complétive", "Groupe nominal COD"], "Subordonnée circonstancielle de comparaison (elliptique du verbe)",
            "Il faut comprendre « que ceux de tes crépuscules [ne l'étaient] » : le verbe est sous-entendu."), YOURCENAR),
        S('francais', 'Étude de la langue · propositions', Q(
            "« Pour regarder les nuages » est-il une proposition subordonnée infinitive ?",
            ["Non : l'infinitif n'a pas de sujet propre, c'est un groupe infinitif complément circonstanciel de but", "Oui", "Oui, une subordonnée relative", "Non, c'est une proposition principale"],
            "Non : l'infinitif n'a pas de sujet propre, c'est un groupe infinitif complément circonstanciel de but",
            "C'est le sujet du verbe principal qui regarde. Toulouse, Nantes et Besançon relèvent cette confusion."), YOURCENAR),
        S('francais', 'Lexique · étymologie', Q(
            "L'adjectif « grêle » (« son cou grêle ») vient du latin gracilis. Quel mot français a la même origine ?",
            ["Gracieux", "Grêlon", "Grenier", "Graisse"], "Gracieux",
            "Le nom « la grêle » (phénomène météorologique) a une autre origine. Confondre les deux a produit des contresens (Toulouse, Nantes)."), YOURCENAR),
        S('francais', 'Culture littéraire · Yourcenar', Q(
            "Marguerite Yourcenar a été la première femme élue :",
            ["À l'Académie française, en 1980", "Présidente de la République", "Au Collège de France", "Prix Nobel de physique"], "À l'Académie française, en 1980",
            "Les Nouvelles orientales (1938, revues en 1963) s'inspirent de légendes d'Asie ; « Comment Wang-Fô fut sauvé » raconte le pouvoir de l'art sur le réel."), None),
    ]),
    epreuve('Épreuve écrite disciplinaire de mathématiques', 16564, [
        S('mathematiques', 'Exercice 1 · équation', N(
            "Avec l'organisme A (1 500 € + 100 € par élève), combien d'élèves pour un voyage de 4 300 € ?", 28,
            "1 500 + 100x = 4 300 donne 100x = 2 800, x = 28."), VOYAGE),
        S('mathematiques', 'Exercice 1 · fractions', N(
            "Avec l'organisme B, 44 élèves coûtent 5 740 €. La coopérative en paie 3/10. Combien cela fait-il par élève, en euros, à l'unité près ?", 39,
            "3/10 × 5 740 = 1 722 € ; 1 722 ÷ 44 ≈ 39 € par élève."), VOYAGE),
        S('mathematiques', 'Exercice 3 · volumes', N(
            "Avec des bennes de 30 m³, combien en faut-il au minimum pour 1 687,5 m³ de terre ?", 57,
            "1 687,5 ÷ 30 = 56,25 : 56 bennes ne suffisent pas, il en faut 57."), PISCINE),
        S('mathematiques', 'Exercice 3 · pourcentages', N(
            "562 100 L d'eau à 12 °C deviennent 564 000 L à 25 °C. De quel pourcentage le volume augmente-t-il, arrondi au centième ?", 0.34,
            "564 000 ÷ 562 100 ≈ 1,00338, soit une augmentation d'environ 0,34 %.", tol=0.005), None),
        S('mathematiques', 'Exercice 3 · vitesse', N(
            "Un élève nage 10 min à 0,6 m/s dans un bassin de 25 m. Combien de longueurs complètes fait-il ?", 14,
            "0,6 m/s = 36 m/min ; 360 m en 10 min, soit 14,4 longueurs : 14 longueurs complètes."), None),
        S('mathematiques', 'Exercice 3 · moyenne', N(
            "Neuf élèves totalisent 116 longueurs. Combien de longueurs doit faire un dixième élève pour que la moyenne soit de 13 ?", 14,
            "(116 + n) ÷ 10 = 13 donne n = 14."), None),
        S('mathematiques', 'Exercice 4 · nature des nombres', Q(
            "Pour quelle valeur de d le quotient 45/d est-il un décimal non entier ?",
            ["d = 2", "d = 3", "d = 5", "d = 9"], "d = 2",
            "45/2 = 22,5 (ou 45/10 = 4,5). 45/3, 45/5 et 45/9 sont entiers."), None),
        S('mathematiques', 'Exercice 6 · Scratch', N(
            "Dans le script, 1 cm vaut 20 pas. Combien de pas représentent les 4 cm d'un côté de la base ?", 80,
            "4 × 20 = 80 pas."), None),
        S('mathematiques', 'Exercice 6 · patrons', Q(
            "Une figure formée d'un carré et de quatre triangles est-elle toujours un patron de la pyramide SABCD ?",
            ["Non : il faut que les triangles soient équilatéraux et ne se superposent pas au pliage", "Oui, toujours", "Non, un patron n'a jamais de carré", "Oui, si les triangles sont isocèles"],
            "Non : il faut que les triangles soient équilatéraux et ne se superposent pas au pliage",
            "Dans le sujet, une figure avait deux triangles qui se superposaient, une autre des triangles isocèles et non équilatéraux."), None),
    ]),
    epreuve("Épreuve écrite d'application (sciences, histoire-géographie-EMC ou arts)", 16558, [
        S('technologie', 'Sciences · le Polar POD', Q(
            "Quel est le rôle des ballasts pendant la mise en place du Polar POD ?",
            ["En se remplissant d'eau, ils font basculer la plateforme de l'horizontale à la verticale", "Ils produisent l'électricité", "Ils servent de logement", "Ils mesurent la température de l'eau"],
            "En se remplissant d'eau, ils font basculer la plateforme de l'horizontale à la verticale",
            "Le flotteur, lui, assure la flottaison de l'ensemble (Bordeaux)."), POD),
        S('technologie', "Sciences · l'énergie du Polar POD", Q(
            "Dans la chaîne d'énergie du Polar POD, à quoi servent les batteries ?",
            ["À stocker l'énergie électrique produite par les éoliennes pour les équipements informatiques", "À produire du vent", "À propulser la plateforme", "À chauffer l'eau de mer"],
            "À stocker l'énergie électrique produite par les éoliennes pour les équipements informatiques",
            "Ordre du schéma : le vent, les éoliennes, les batteries, les équipements informatiques (Bordeaux, Paris)."), POD),
        S('physique_chimie', "Sciences · le dessalement solaire", Q(
            "Dans un distillateur solaire, pourquoi l'eau recueillie est-elle douce ?",
            ["L'eau s'évapore sous l'effet du soleil et le sel reste ; la vapeur se condense sur le film plastique", "Le soleil détruit le sel", "Le plastique filtre le sel", "La glace fond et donne de l'eau douce"],
            "L'eau s'évapore sous l'effet du soleil et le sel reste ; la vapeur se condense sur le film plastique",
            "Le bloc de froid peut faire croire que l'eau douce vient de la glace fondue : c'est un obstacle à anticiper (Bordeaux)."), POD),
        S('physique_chimie', "Sciences · l'atome", Q(
            "Combien d'électrons a l'ion oxyde O²⁻, sachant que l'atome d'oxygène en a 8 ?",
            ["10", "6", "8", "16"], "10",
            "La charge 2− signifie 2 électrons de plus que l'atome neutre. Protons et neutrons ne changent pas."), POD),
        S('svt', 'Sciences · croire et savoir', Q(
            "En sciences, quelle différence y a-t-il entre croire et savoir ?",
            ["Croire, c'est tenir pour vrai sans preuve ; savoir, c'est s'appuyer sur des faits établis par une méthode rigoureuse", "Ce sont des synonymes", "Savoir, c'est avoir une opinion", "Croire, c'est avoir fait une expérience"],
            "Croire, c'est tenir pour vrai sans preuve ; savoir, c'est s'appuyer sur des faits établis par une méthode rigoureuse",
            "En classe : confronter l'affirmation d'un élève à des relevés météorologiques et à des données sur le climat (Bordeaux)."), POD),
        S('svt', 'Sciences · lire un graphique', Q(
            "Un élève relie les points des températures de décembre sans suivre l'ordre des jours. Quelle remédiation proposer ?",
            ["Passer par un tableau des relevés, puis placer les points dans l'ordre des jours (ou tracer un diagramme en bâtons)", "Lui faire recopier le graphique", "Supprimer le graphique", "Lui donner la réponse"],
            "Passer par un tableau des relevés, puis placer les points dans l'ordre des jours (ou tracer un diagramme en bâtons)",
            "Tracer une ligne horizontale à 5 °C l'aide aussi à compter les jours sous ce seuil (Bordeaux)."), POD),
        S('svt', "Sciences · l'élevage en classe", Q(
            "Quelle précaution faut-il prévoir pour un élevage d'animaux en classe ?",
            ["Hygiène et sécurité (allergies, lavage des mains), soin des animaux pendant les vacances, respect de la réglementation", "Aucune", "Laisser les élèves les emporter chez eux sans organisation", "Les nourrir avec le goûter des élèves"],
            "Hygiène et sécurité (allergies, lavage des mains), soin des animaux pendant les vacances, respect de la réglementation",
            "C'était la réponse attendue à la question 24 (Bordeaux)."), POD),
        S('histoire_geographie', "Histoire · l'école de Jules Ferry", Q(
            "Quelle loi de 1881 rend l'école primaire publique gratuite ?",
            ["La loi du 16 juin 1881 (loi Ferry)", "La loi Falloux", "La loi Guizot", "La loi de 1905"], "La loi du 16 juin 1881 (loi Ferry)",
            "Gratuité (1881), puis obligation et laïcité de l'enseignement (1882), puis laïcisation du personnel (loi Goblet, 1886)."), FERRY),
        S('histoire_geographie', "Histoire · l'école de Jules Ferry", Q(
            "Pourquoi les républicains des années 1880 veulent-ils une école laïque ?",
            ["Pour former des citoyens attachés à la République et limiter l'influence de l'Église sur l'enseignement", "Pour supprimer la religion en France", "Pour former des soldats", "Pour enseigner le latin à tous"],
            "Pour former des citoyens attachés à la République et limiter l'influence de l'Église sur l'enseignement",
            "La IIIe République, fragile face aux monarchistes, s'enracine par l'école, où l'on apprend aussi les symboles républicains."), FERRY),
        S('histoire_geographie', "Histoire · l'école de Jules Ferry", Q(
            "En quelle année le 14 juillet devient-il la fête nationale ?",
            ["1880", "1789", "1905", "1945"], "1880",
            "C'est aussi à partir de 1880 que la devise « Liberté, Égalité, Fraternité » s'inscrit sur les frontons des édifices publics."), None),
        S('histoire_geographie', "Histoire · l'école de Jules Ferry", Q(
            "Que montre une photographie de classe de 1909 comparée à une classe d'aujourd'hui ?",
            ["Des rites scolaires différents : classes non mixtes, pupitres en rangées, discipline stricte", "Rien de différent", "Des tablettes numériques", "Des élèves sans enseignant"],
            "Des rites scolaires différents : classes non mixtes, pupitres en rangées, discipline stricte",
            "Comparer hier et aujourd'hui est une démarche suggérée par les ressources d'accompagnement (Aix-Marseille, Toulouse)."), FERRY),
        S('emc', 'EMC · la laïcité', Q(
            "Laquelle de ces définitions de la laïcité, pour des CM2, est complète ?",
            ["La laïcité sépare les religions et l'État ; l'école est neutre ; chacun est libre de croire ou de ne pas croire et tous sont égaux", "La laïcité, c'est ne pas croire en Dieu", "La laïcité interdit les religions", "La laïcité, c'est la liberté de croire, et c'est tout"],
            "La laïcité sépare les religions et l'État ; l'école est neutre ; chacun est libre de croire ou de ne pas croire et tous sont égaux",
            "Une définition pour des élèves reste exacte : courte, mais complète (Orléans-Tours, Toulouse)."), FERRY),
        S('emc', 'EMC · valeurs et principes', Q(
            "La laïcité est-elle une valeur ou un principe ?",
            ["Un principe d'organisation de la République", "Une règle de vie de la classe", "Une émotion", "Une opinion personnelle"], "Un principe d'organisation de la République",
            "Le programme parle des « valeurs et principes » : liberté, égalité, fraternité (valeurs) et laïcité (principe). La confusion est fréquente (Bordeaux, Orléans-Tours)."), None),
        S('arts', "Arts plastiques · l'écrit dans l'art", Q(
            "Pierre Alechinsky, présent dans le dossier, a peint « Sorti de la poche » (1992) sur :",
            ["Un papier ancien couvert d'écritures (vergé du XVIIe siècle)", "Une toile vierge", "Un mur de rue", "Une plaque de métal"], "Un papier ancien couvert d'écritures (vergé du XVIIe siècle)",
            "Encre de Chine et aquarelle sur un document ancien avec écritures et essais de plume : l'écrit devient support et matière."), None),
        S('arts', "Arts plastiques · l'écrit dans l'art", Q(
            "Quels matériaux du dossier permettent une « exploration plastique de l'écrit » en cycle 2 ?",
            ["Journaux, lettres découpées de tailles et polices différentes, tampons encreurs, papier calque", "Uniquement des crayons de couleur", "De la pâte à modeler", "Des instruments de musique"],
            "Journaux, lettres découpées de tailles et polices différentes, tampons encreurs, papier calque",
            "Les élèves jouent sur la forme, la taille, la couleur et la place des lettres, comme Villeglé avec ses affiches lacérées."), None),
    ]),
]
