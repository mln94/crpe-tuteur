# Bac+5, session 2025, groupement 3
from slib import S, Q, N, C, epreuve

JARRY = ("Texte : Isabelle Jarry, Le jardin Yamata (1999). La narratrice part au Japon sur les traces d'un secret familial, "
         "sans savoir si quelqu'un a reçu sa lettre.")
DES = "Exercice 4 : un élève lance un dé à six faces et un dé à dix faces, équilibrés."
OEUF = "Sujet de sciences et technologie : de la poule à l'œuf, l'œuf objet naturel, et un poulailler automatisé pour le bien-être animal."
TOURISME = "Sujet de géographie et EMC : en CM1, « se loger, travailler, se cultiver, avoir des loisirs dans un espace touristique » ; puis une action pour la semaine du développement durable."

QUESTIONS = [
    epreuve('Épreuve écrite disciplinaire de français', 16582, [
        S('francais', 'Étude de la langue · accords', Q(
            "« Il me semblait improbable que quelqu'un ait reçu ma lettre, mieux, l'ait lue et comprise. » Pourquoi « lue » et « comprise » sont-ils au féminin ?",
            ["Ils s'accordent avec le COD « l' » (ma lettre), placé avant l'auxiliaire avoir", "Ils s'accordent avec le sujet « quelqu'un »", "Le participe passé avec avoir s'accorde toujours au féminin", "Ils s'accordent avec « improbable »"],
            "Ils s'accordent avec le COD « l' » (ma lettre), placé avant l'auxiliaire avoir",
            "« Reçu » reste invariable : son COD « ma lettre » est placé après le verbe."), JARRY),
        S('francais', 'Étude de la langue · accords', Q(
            "« J'étais partie sans attendre de réponse. » Pourquoi « partie » est-il au féminin ?",
            ["Avec l'auxiliaire être, le participe s'accorde avec le sujet « je », qui désigne la narratrice", "Il s'accorde avec « réponse »", "C'est un adjectif", "Il s'accorde avec un COD placé avant"],
            "Avec l'auxiliaire être, le participe s'accorde avec le sujet « je », qui désigne la narratrice",
            "Le texte donne l'indice du genre : c'est une narratrice. Avec être, accord avec le sujet ; avec avoir, accord avec le COD placé avant."), JARRY),
        S('francais', 'Étude de la langue · temps et modes', Q(
            "« … une réponse dont je m'accommoderais quelle qu'elle soit. » Temps et mode de « soit » ?",
            ["Présent du subjonctif", "Présent de l'indicatif", "Conditionnel présent", "Imparfait du subjonctif"], "Présent du subjonctif",
            "« Quel que » (en deux mots, accordé : « quelle qu'elle ») exprime la concession et entraîne le subjonctif."), JARRY),
        S('francais', 'Étude de la langue · liens logiques', Q(
            "« Je pensais « c'est normal ». Et rien ne me paraissait normal… » Quel sens a ici « et » ?",
            ["L'opposition", "L'addition", "La cause", "Le temps"], "L'opposition",
            "La conjonction de coordination « et » prend ici une valeur d'opposition. On peut écrire : « Je pensais que c'était normal alors que rien ne me paraissait normal »."), JARRY),
        S('francais', 'Étude de la langue · voix active et passive', Q(
            "À la voix active : « Le secret avait été instauré et farouchement gardé par mon grand-père. »",
            ["Mon grand-père avait instauré et farouchement gardé le secret.", "Mon grand-père instaura et garda farouchement le secret.", "Le secret avait instauré et gardé mon grand-père.", "Mon grand-père a instauré et farouchement gardé le secret."],
            "Mon grand-père avait instauré et farouchement gardé le secret.",
            "Le complément d'agent devient sujet, le sujet devient COD, et le temps est conservé : plus-que-parfait (avait été instauré → avait instauré)."), JARRY),
        S('francais', 'Lexique · orthographe des préfixes', Q(
            "Pourquoi écrit-on « improbable » mais « inabordable » ?",
            ["Le préfixe in- devient im- devant b, m et p", "Ce sont deux préfixes différents", "On écrit im- devant une voyelle", "C'est une exception sans règle"],
            "Le préfixe in- devient im- devant b, m et p",
            "Même préfixe négatif : im-probable, in-abordable. Il devient aussi il- devant l (illisible) et ir- devant r (irréel)."), JARRY),
        S('francais', 'Lexique · familles de mots', Q(
            "Quel mot appartient à la même famille que « improbable » ?",
            ["Probabilité", "Problème", "Prouver", "Probe"], "Probabilité",
            "Probable, probablement, probabilité, improbabilité partagent le même radical. « Problème » n'a que le son en commun."), JARRY),
    ]),
    epreuve('Épreuve écrite disciplinaire de mathématiques', 16567, [
        S('mathematiques', 'Exercice 1 · vrai ou faux', N(
            "Série : 4 – 16 – 8 – 15 – 10 – 17 – 10 – 6 – 12 – 9 – 14. Quelle est sa médiane ?", 10,
            "Rangée : 4, 6, 8, 9, 10, 10, 12, 14, 15, 16, 17. La 6e valeur sur 11 est 10 : l'affirmation « la médiane est 11 » est fausse."), None),
        S('mathematiques', 'Exercice 1 · vrai ou faux', Q(
            "Noah Lyles a couru le 100 m en 9,79 s aux Jeux de 2024. Affirmation : « il a couru à plus de 37 km/h. » Vrai ou faux ?",
            ["Faux : environ 36,8 km/h", "Vrai : environ 37,4 km/h", "Vrai : environ 102 km/h", "Faux : environ 10,2 km/h"], "Faux : environ 36,8 km/h",
            "100 ÷ 9,79 ≈ 10,21 m/s, et 10,21 × 3,6 ≈ 36,8 km/h, moins que 37 km/h."), None),
        S('mathematiques', 'Exercice 1 · vrai ou faux', Q(
            "Affirmation : « L'aire d'un carré est proportionnelle à la longueur de son côté. » Vrai ou faux ?",
            ["Faux : si le côté double, l'aire est multipliée par 4", "Vrai", "Vrai, avec le coefficient 4", "Faux : l'aire ne dépend pas du côté"], "Faux : si le côté double, l'aire est multipliée par 4",
            "A = c² : côté 1 → aire 1 ; côté 2 → aire 4. Le rapport aire/côté n'est pas constant. C'est le périmètre (4c) qui est proportionnel au côté."), None),
        S('mathematiques', 'Exercice 2 · énigme', N(
            "Je suis un entier entre 1 000 et 4 000, multiple de 3, non divisible par 4. Mon chiffre des unités est 4, mon chiffre des centaines est le double de celui des unités, et mon nombre de centaines est un multiple de 9. Qui suis-je ?", 1854,
            "Unités 4, centaines 8 : le nombre s'écrit a8b4. Nombre de centaines 10a + 8 multiple de 9, avec a entre 1 et 3 : a = 1 (18). Multiple de 3 : 1 + 8 + b + 4 = 13 + b, donc b = 2, 5 ou 8. Non divisible par 4 : 24 et 84 le sont, 54 non. Réponse : 1 854."), None),
        S('mathematiques', 'Exercice 3 · proportionnalité', N(
            "Chaque habitant produit 88 kg de déchets verts par an ; 1 m³ de déchets verts pèse 0,2 t. Quel volume produisent 60 personnes, en m³ ?", 26.4,
            "60 × 88 = 5 280 kg = 5,28 t. 5,28 ÷ 0,2 = 26,4 m³. Avec 55 % de compost : 2 904 kg."), None),
        S('mathematiques', 'Exercice 4 · probabilités', Q(
            "On multiplie les résultats des deux dés. Quelle est la probabilité d'obtenir 16 ?",
            ["1/30", "1/60", "1/20", "1/16"], "1/30",
            "60 issues. Produit 16 : (2 ; 8) et (4 ; 4), soit 2/60 = 1/30. (Pour 35, seule (5 ; 7) convient : 1/60.)"), DES),
        S('mathematiques', 'Exercice 4 · probabilités', Q(
            "Quelle est la probabilité que le produit soit un multiple de 3 ?",
            ["8/15", "1/3", "1/2", "2/5"], "8/15",
            "Dé à six faces sur 3 ou 6 : 2 × 10 = 20 issues. Sinon (4 valeurs), le dé à dix faces doit donner 3, 6 ou 9 : 4 × 3 = 12 issues. Total 32/60 = 8/15."), DES),
        S('mathematiques', 'Exercice 4 · fractions', Q(
            "Le dé à dix faces donne 10 (numérateur), le dé à six faces donne 3 (dénominateur). Quelle est la décomposition de 10/3 ?",
            ["3 + 1/3", "3 + 3/10", "1 + 7/3", "10 + 1/3"], "3 + 1/3",
            "10 = 3 × 3 + 1, donc 10/3 = 3 + 1/3, avec 1/3 strictement inférieur à 1."), DES),
        S('mathematiques', 'Exercice 4 · probabilités', Q(
            "Quelle est la probabilité que la partie entière de la fraction (numérateur au dé à dix faces, dénominateur au dé à six faces) soit 0 ?",
            ["1/4", "1/6", "15/36", "1/10"], "1/4",
            "La partie entière vaut 0 quand le numérateur est plus petit que le dénominateur : 0 + 1 + 2 + 3 + 4 + 5 = 15 issues sur 60, soit 1/4."), DES),
    ]),
    epreuve("Épreuve écrite d'application (sciences, histoire-géographie-EMC ou arts)", 16579, [
        # ── Sciences ──
        S('svt', "Sciences · de la poule à l'œuf", Q(
            "Comment définit-on une espèce ?",
            ["Un ensemble d'individus qui peuvent se reproduire entre eux et avoir une descendance fertile", "Des animaux qui vivent au même endroit", "Des animaux de la même couleur", "Des animaux qui mangent la même nourriture"],
            "Un ensemble d'individus qui peuvent se reproduire entre eux et avoir une descendance fertile",
            "Les races de poules domestiques appartiennent toutes à la même espèce : elles sont interfécondes."), OEUF),
        S('svt', "Sciences · de la poule à l'œuf", Q(
            "Pourquoi un gène favorisant la ponte est-il devenu très fréquent chez la poule domestique ?",
            ["Les éleveurs ont sélectionné, génération après génération, les poules qui le portaient", "Il est apparu chez toutes les poules en même temps", "Le climat l'a imposé", "Les poules l'ont choisi"],
            "Les éleveurs ont sélectionné, génération après génération, les poules qui le portaient",
            "C'est la sélection artificielle : les êtres humains font se reproduire les individus qui ont le caractère recherché, et la fréquence de l'allèle augmente."), OEUF),
        S('svt', "Sciences · de la poule à l'œuf", Q(
            "Pour qu'un élève de cycle 3 utilise une clé de détermination des races de poules, quelle simplification est utile ?",
            ["Remplacer les termes techniques par des mots simples et ajouter des dessins", "Ajouter plus de critères", "Retirer toutes les images", "Utiliser des noms latins"],
            "Remplacer les termes techniques par des mots simples et ajouter des dessins",
            "On peut aussi réduire le nombre de critères, garder des critères observables et limiter la clé aux races du poulailler."), OEUF),
        S('physique_chimie', "Sciences · l'œuf", Q(
            "Comment s'appelle le passage de l'état solide à l'état liquide ?",
            ["La fusion", "La solidification", "La vaporisation", "La dissolution"], "La fusion",
            "Ne confondez pas avec la dissolution (un solide qui se mélange à un liquide, comme le sel dans l'eau)."), OEUF),
        S('physique_chimie', "Sciences · l'œuf", Q(
            "Un œuf flotte dans de l'eau très salée. Quelles forces s'exercent sur lui ?",
            ["Son poids, vers le bas, et la poussée d'Archimède, vers le haut, qui se compensent", "Seulement son poids", "Seulement la poussée d'Archimède", "Deux forces horizontales"],
            "Son poids, vers le bas, et la poussée d'Archimède, vers le haut, qui se compensent",
            "L'eau salée, plus dense, exerce une poussée plus grande : l'œuf qui coulait dans l'eau douce peut flotter."), OEUF),
        S('physique_chimie', "Sciences · l'œuf", Q(
            "Quelle est la composition atomique de la molécule de dioxyde de carbone, CO₂ ?",
            ["1 atome de carbone et 2 atomes d'oxygène", "2 atomes de carbone et 1 atome d'oxygène", "1 atome de calcium et 2 atomes d'oxygène", "1 atome de cobalt et 2 atomes d'oxygène"],
            "1 atome de carbone et 2 atomes d'oxygène",
            "Le préfixe di- de dioxyde indique 2 atomes d'oxygène. Dans une équation chimique ajustée, les atomes de chaque sorte sont aussi nombreux de chaque côté."), OEUF),
        S('technologie', 'Sciences · le poulailler automatisé', Q(
            "Une porte de poulailler est ouverte par un fil enroulé sur une poulie motorisée. Quels sont les mouvements de la poulie et de la porte ?",
            ["Poulie : rotation ; porte : translation (verticale)", "Poulie : translation ; porte : rotation", "Les deux tournent", "Les deux glissent"], "Poulie : rotation ; porte : translation (verticale)",
            "Le système transforme un mouvement de rotation en mouvement de translation."), OEUF),
        S('technologie', 'Sciences · le poulailler automatisé', Q(
            "La porte doit s'ouvrir automatiquement au lever du jour. Quel capteur faut-il ?",
            ["Un capteur de luminosité", "Un capteur de température", "Un capteur de présence", "Un micro"], "Un capteur de luminosité",
            "Le programme compare la luminosité mesurée à un seuil : au-dessus, il commande le moteur pour ouvrir la porte. Des fins de course arrêtent le moteur."), OEUF),
        # ── Géographie et EMC ──
        S('histoire_geographie', 'Géographie · un espace touristique', Q(
            "Au CM1, le thème « se loger, travailler, se cultiver, avoir des loisirs » amène à étudier un espace touristique. Que montre-t-on ?",
            ["Comment le tourisme transforme un lieu : aménagements, emplois, habitants permanents et saisonniers, et ses effets sur l'environnement", "La liste des monuments de France", "Uniquement les plages", "L'histoire des rois de France"],
            "Comment le tourisme transforme un lieu : aménagements, emplois, habitants permanents et saisonniers, et ses effets sur l'environnement",
            "On part d'un lieu (station littorale ou de montagne, ville touristique) et de ses habitants, avec cartes, photographies et documents."), TOURISME),
        S('histoire_geographie', 'Géographie · un espace touristique', Q(
            "Pourquoi certaines communes touristiques voient-elles leur population varier fortement dans l'année ?",
            ["Parce que les touristes et les travailleurs saisonniers s'ajoutent aux habitants permanents pendant la saison", "Parce que les habitants déménagent chaque hiver", "Parce que les recensements sont faux", "Parce que la commune change de superficie"],
            "Parce que les touristes et les travailleurs saisonniers s'ajoutent aux habitants permanents pendant la saison",
            "Cette variation impose des équipements dimensionnés pour la haute saison : logements, eau, transports, déchets."), TOURISME),
        S('emc', 'EMC · une action de développement durable', Q(
            "Quel est l'intérêt pédagogique d'une action concrète (par exemple réduire le gaspillage à la cantine) pendant la semaine du développement durable ?",
            ["Faire passer les élèves de la connaissance à l'engagement, dans un projet collectif qui a un effet mesurable", "Remplacer les cours de sciences", "Occuper les élèves pendant une semaine", "Récompenser les meilleurs élèves"],
            "Faire passer les élèves de la connaissance à l'engagement, dans un projet collectif qui a un effet mesurable",
            "L'EMC vise une « culture de l'engagement » : responsabilité individuelle et collective envers les autres et l'environnement."), TOURISME),
        S('emc', 'EMC · une action de développement durable', Q(
            "Que désignent les 17 objectifs de développement durable (ODD) ?",
            ["Des objectifs adoptés par l'ONU en 2015 pour 2030 (pauvreté, faim, éducation, climat…)", "Des règles de l'école française", "Des articles de la Constitution", "Des épreuves du concours"],
            "Des objectifs adoptés par l'ONU en 2015 pour 2030 (pauvreté, faim, éducation, climat…)",
            "Ils servent de cadre aux projets d'éducation au développement durable, comme la labellisation E3D des écoles."), None),
        # ── Arts ──
        S('arts', 'Arts plastiques · la ressemblance', Q(
            "Camille Claudel a sculpté « La Petite Châtelaine » (1895-1896). Dans quel matériau ?",
            ["Le marbre", "La terre cuite peinte", "Le plastique", "Le béton"], "Le marbre",
            "Le sujet portait sur « la ressemblance » et « la valeur expressive de l'écart » dans la représentation, avec une œuvre de Claudel et une d'Auguste Chabaud."),
          "Dossier d'arts plastiques (cycle 3) : une fiche de préparation à analyser sur la ressemblance."),
        S('arts', 'Éducation musicale · explorer et imaginer', Q(
            "« Inventer une organisation simple à partir d'éléments sonores » (cycle 2), qu'est-ce que c'est ?",
            ["Organiser des sons choisis (voix, objets, corps) selon un ordre, des durées et des nuances, pour créer une courte pièce", "Recopier une partition", "Écouter une œuvre sans réagir", "Apprendre le solfège"],
            "Organiser des sons choisis (voix, objets, corps) selon un ordre, des durées et des nuances, pour créer une courte pièce",
            "La démarche de création sonore (ressources Éduscol) : explorer, choisir, organiser, interpréter, puis écouter et améliorer."), None),
    ]),
]
