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
    # ── Ajout : questions complémentaires tirées du même sujet (regroupement 3, Polynésie française) ──
    epreuve('Épreuve écrite disciplinaire de français', 16582, [
        S('francais', 'Étude de la langue · temps et modes', Q(
            "« … tout ce que j'allais trouver serait une réponse dont je m'accommoderais. » Temps et mode de « serait » ?",
            ["Conditionnel présent", "Futur simple", "Imparfait de l'indicatif", "Présent du subjonctif"], "Conditionnel présent",
            "Il exprime ici un futur dans le passé, après « j'allais trouver ». « M'accommoderais » est aussi au conditionnel présent."), JARRY),
        S('francais', 'Étude de la langue · nature et fonction', Q(
            "« … je ne disposais d'aucun indice. » Fonction de « d'aucun indice » ?",
            ["COI du verbe « disposer »", "COD", "Complément du nom", "Complément circonstanciel de manière"], "COI du verbe « disposer »",
            "On dispose de quelque chose : le complément est introduit par la préposition « de », c'est un COI."), JARRY),
        S('francais', 'Étude de la langue · nature et fonction', Q(
            "« … la magie du lieu qui se livrerait à moi docilement. » Nature de « docilement » ?",
            ["Adverbe de manière", "Adjectif", "Nom", "Préposition"], "Adverbe de manière",
            "Formé de l'adjectif « docile » + -ment, il modifie le verbe « se livrer »."), JARRY),
        S('francais', 'Étude de la langue · voix active et passive', Q(
            "« Le secret avait été instauré […] par mon grand-père. » Comment appelle-t-on « par mon grand-père » ?",
            ["Le complément d'agent", "Le COD", "Le sujet", "Le complément du nom"], "Le complément d'agent",
            "À la voix passive, celui qui fait l'action est le complément d'agent ; à la voix active, il devient sujet."), JARRY),
        S('francais', 'Lexique · sens en contexte', Q(
            "Que veut dire la narratrice par « m'enfoncer dans les eaux vertes et troubles » ?",
            ["Se lancer dans une recherche incertaine, obscure, sur un passé familial mystérieux", "Se baigner dans un lac", "Tomber malade", "Peindre un paysage"],
            "Se lancer dans une recherche incertaine, obscure, sur un passé familial mystérieux",
            "C'est une métaphore : l'eau trouble dit l'incertitude de son enquête au Japon, sans indice ni réponse."), JARRY),
    ]),
    epreuve('Épreuve écrite disciplinaire de mathématiques', 16567, [
        S('mathematiques', 'Exercice 4 · probabilités', Q(
            "Dés à 6 et à 10 faces : pourquoi la probabilité d'obtenir le produit 35 vaut-elle 1/60 ?",
            ["Seul le couple (5 ; 7) donne 35, sur 60 issues équiprobables", "Il y a 35 issues", "35 est divisible par 5", "Le produit maximal est 60"], "Seul le couple (5 ; 7) donne 35, sur 60 issues équiprobables",
            "35 = 5 × 7 = 7 × 5, mais le dé à six faces ne peut pas donner 7. Il reste (5 ; 7)."), DES),
        S('mathematiques', 'Exercice 4 · probabilités', Q(
            "Numérateur au dé à dix faces, dénominateur au dé à six faces. Quelle est la probabilité que la fraction soit un entier ?",
            ["23/60", "1/6", "1/4", "1/2"], "23/60",
            "Le dénominateur doit diviser le numérateur : 10 cas pour 1, 5 pour 2, 3 pour 3, 2 pour 4, 2 pour 5, 1 pour 6, soit 23 sur 60."), DES),
        S('mathematiques', 'Exercice 3 · pourcentages', N(
            "Un lotissement produit 5 280 kg de déchets verts ; le compost représente 55 % de cette masse. Combien de kg de compost ?", 2904,
            "5 280 × 0,55 = 2 904 kg."), None),
        S('histoire_geographie', 'Géographie · Bora-Bora, un espace touristique', Q(
            "Pourquoi Bora-Bora est-elle la « vitrine touristique » de la Polynésie française ?",
            ["Elle concentre de nombreux hôtels de luxe de chaînes internationales, beaucoup de vols et la majorité des touristes internationaux", "Elle est la capitale de la Polynésie", "Elle n'a aucun hôtel", "C'est l'île la plus grande"],
            "Elle concentre de nombreux hôtels de luxe de chaînes internationales, beaucoup de vols et la majorité des touristes internationaux",
            "Elle reçoit les trois cinquièmes des touristes internationaux et la majorité des hôtels 5 étoiles du territoire (document 3)."), "Sujet de géographie (Polynésie française, CM1) : le tourisme à Bora-Bora, avec un texte de la géographe Caroline Blondy, des photographies et des images satellites."),
        S('histoire_geographie', 'Géographie · Bora-Bora, un espace touristique', Q(
            "Quel type d'hébergement caractérise le paysage touristique de Bora-Bora ?",
            ["Les bungalows sur pilotis au-dessus du lagon", "Les gratte-ciel", "Les campings de montagne", "Les chalets de ski"], "Les bungalows sur pilotis au-dessus du lagon",
            "En 2012, l'île comptait 12 hôtels et 833 unités, dont près de la moitié de bungalows sur pilotis (document 3)."), "Document 3 : C. Blondy, « Le tourisme, un facteur de développement durable des territoires insulaires tropicaux ? »."),
        S('histoire_geographie', 'Géographie · Bora-Bora, un espace touristique', Q(
            "Que désigne le mot « motu », utilisé à Bora-Bora ?",
            ["Un petit îlot de sable et de corail autour du lagon", "Un hôtel de luxe", "Une montagne volcanique", "Un bateau de pêche"], "Un petit îlot de sable et de corail autour du lagon",
            "Les hôtels se sont implantés au sud de l'île et sur les motu périphériques, ce qui a transformé ces paysages."), None),
        S('histoire_geographie', 'Géographie · Bora-Bora, un espace touristique', Q(
            "Selon le document 3, le tourisme a-t-il seulement des effets négatifs à Bora-Bora ?",
            ["Non : il transforme les paysages et pèse sur les ressources, mais crée des emplois, freine l'émigration et a amélioré la gestion des déchets et de l'eau", "Oui, uniquement négatifs", "Il n'a aucun effet", "Il a seulement fait baisser la population"],
            "Non : il transforme les paysages et pèse sur les ressources, mais crée des emplois, freine l'émigration et a amélioré la gestion des déchets et de l'eau",
            "« L'opposition entre tourisme et environnement est loin d'être aussi simple qu'elle n'y paraît » : une approche nuancée, attendue en géographie."), "Document 3 : C. Blondy, 2016."),
        S('histoire_geographie', 'Géographie · le paysage', Q(
            "Selon le glossaire Géoconfluences (document 2), le paysage est :",
            ["L'ensemble des éléments observables depuis un lieu, à la fois objectif et perçu par chacun selon sa sensibilité", "Uniquement un espace naturel", "Une carte vue du dessus", "Un tableau de peintre"],
            "L'ensemble des éléments observables depuis un lieu, à la fois objectif et perçu par chacun selon sa sensibilité",
            "Le paysage n'est pas réservé aux espaces « naturels » : les espaces urbains et industriels ont aussi des paysages à analyser."), "Document 2 : glossaire Géoconfluences, « paysage » et « organisation de l'espace »."),
        S('histoire_geographie', 'Géographie · lire une image', Q(
            "Quelle différence y a-t-il entre une vue aérienne oblique et une image satellite verticale ?",
            ["La vue oblique montre le paysage en perspective, proche de ce que l'on voit ; la vue verticale (zénithale) se rapproche d'une carte", "Il n'y en a aucune", "La vue verticale est toujours en noir et blanc", "La vue oblique est un dessin"],
            "La vue oblique montre le paysage en perspective, proche de ce que l'on voit ; la vue verticale (zénithale) se rapproche d'une carte",
            "Le dossier proposait les deux (photographie aérienne d'un hôtel, image du satellite Pléiades) : les croiser aide les élèves à passer du paysage à la carte."), None),
        S('emc', 'EMC · une action de développement durable', Q(
            "Qu'est-ce qu'une « clean walk », comme celle organisée sur le littoral de Bora-Bora ?",
            ["Une marche collective pour ramasser les déchets", "Une course à pied", "Une visite guidée d'hôtel", "Un nettoyage des bateaux"], "Une marche collective pour ramasser les déchets",
            "Le document 8 la présente comme un succès inspirant : une action concrète que peut mener une classe pendant la semaine du développement durable."), "Document 8 : « Bora-Bora nettoie son littoral : le succès d'un clean walk », 2024."),
        S('emc', 'EMC · une action de développement durable', Q(
            "Pourquoi une action collective comme le ramassage de déchets relève-t-elle de l'EMC ?",
            ["Elle développe la responsabilité envers les autres et l'environnement, et l'engagement dans un projet commun", "Elle remplace les cours de sciences", "Elle sert seulement à nettoyer", "Elle n'a aucun lien avec l'EMC"],
            "Elle développe la responsabilité envers les autres et l'environnement, et l'engagement dans un projet commun",
            "L'EMC vise une culture de l'engagement ; l'éducation au développement durable (document 10) s'appuie sur des actions concrètes dans l'école et autour d'elle."), None),
        S('svt', "Sciences · de la poule à l'œuf", Q(
            "À quelle espèce appartiennent toutes les races de poules domestiques ?",
            ["Une seule et même espèce, Gallus gallus (sous-espèce domesticus)", "Une espèce différente par race", "Aux canards", "Aux faisans"], "Une seule et même espèce, Gallus gallus (sous-espèce domesticus)",
            "Les races sont interfécondes et leurs descendants sont fertiles : c'est le critère de l'espèce."), OEUF),
        S('svt', "Sciences · l'œuf", Q(
            "Un œuf de poule acheté au supermarché peut-il donner un poussin ?",
            ["Non, en général : il n'a pas été fécondé, faute de coq", "Oui, toujours", "Oui, si on le met au réfrigérateur", "Oui, si on le fait cuire"], "Non, en général : il n'a pas été fécondé, faute de coq",
            "Une poule pond même sans coq ; seul un œuf fécondé et couvé (environ 21 jours) peut se développer en poussin."), OEUF),
        S('physique_chimie', "Sciences · l'œuf", Q(
            "Un œuf coule dans l'eau douce et flotte dans l'eau très salée. Pourquoi ?",
            ["L'eau salée est plus dense : la poussée d'Archimède augmente et compense le poids", "Le sel rend l'œuf plus léger", "L'œuf absorbe le sel", "L'eau salée est plus chaude"],
            "L'eau salée est plus dense : la poussée d'Archimède augmente et compense le poids",
            "La poussée d'Archimède dépend de la masse volumique du liquide déplacé."), OEUF),
        S('technologie', 'Sciences · le poulailler automatisé', Q(
            "Que sont les capteurs de fin de course d'une porte automatique ?",
            ["Des capteurs qui détectent que la porte est complètement ouverte ou fermée, pour arrêter le moteur", "Des capteurs de température", "Des capteurs de lumière", "Des capteurs de poids des poules"],
            "Des capteurs qui détectent que la porte est complètement ouverte ou fermée, pour arrêter le moteur",
            "Sans eux, le moteur continuerait de tourner et pourrait abîmer le système."), OEUF),
        S('arts', 'Arts plastiques · la ressemblance', Q(
            "Au programme du cycle 3, que signifie « la valeur expressive de l'écart dans la représentation » ?",
            ["S'éloigner volontairement de la ressemblance (déformation, couleurs, matière) peut renforcer l'expression", "Toujours copier le réel le plus fidèlement possible", "Mesurer l'écart entre deux objets", "Représenter seulement des paysages"],
            "S'éloigner volontairement de la ressemblance (déformation, couleurs, matière) peut renforcer l'expression",
            "Le sujet demandait d'analyser une fiche de préparation sur ce point, avec Camille Claudel et Auguste Chabaud."), None),
        S('arts', 'Éducation musicale · cycle 2', Q(
            "Que signifie « interpréter un chant avec expressivité » ?",
            ["Chanter en jouant sur les nuances, le tempo et l'intention pour transmettre une émotion", "Chanter le plus vite possible", "Chanter seul sans écouter les autres", "Réciter les paroles"],
            "Chanter en jouant sur les nuances, le tempo et l'intention pour transmettre une émotion",
            "C'est l'un des points du programme de cycle 2 sur lesquels le sujet demandait une fiche de préparation."), None),
    ]),
]
