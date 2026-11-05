# Bac+5, session 2026, groupement 2
from slib import S, Q, N, C, epreuve

BONNEFOY = ("Texte : Miguel Bonnefoy, Le rêve du jaguar (2024). Le jeune Cristóbal suit sa mère diplomate de pays en pays ; "
            "pour lui, les livres, qui ne changent pas, sont un refuge.")
FRAISES = "Exercice 1 : une école aménage un potager et plante des fraisiers dans un rectangle LMNP avec LM = 185 cm et LP = 444 cm, en suivant un maillage carré."
DES = "Exercice 3 : on lance un dé cubique (1 à 6) et un dé tétraédrique (1 à 4)."
NUIT = "Sujet de sciences et technologie : la pollution lumineuse et la préservation de la nuit (séjour d'une classe dans le Parc naturel régional du Vercors)."
GUERRES = "Sujet d'histoire et EMC : en CM2, les deux guerres mondiales à partir de leurs traces, puis la participation des élèves à la commémoration du 8 mai 1945."

QUESTIONS = [
    epreuve('Épreuve écrite disciplinaire de français', 20145, [
        S('francais', 'Étude de la langue · temps et voix', Q(
            "« Venezuela fut nommée chargée des affaires culturelles de l'ambassade. » Temps, voix et infinitif de « fut nommée » ?",
            ["Passé simple, voix passive, nommer", "Passé composé, voix active, nommer", "Plus-que-parfait, voix passive, être", "Passé simple, voix active, être"], "Passé simple, voix passive, nommer",
            "Auxiliaire être au passé simple + participe passé : voix passive. Le sujet subit l'action ; l'infinitif est celui du verbe principal, nommer."), BONNEFOY),
        S('francais', 'Étude de la langue · accords', Q(
            "« … effectuant la même tâche qu'avaient accomplie les chroniqueurs des Indes orientales. » Pourquoi « accomplie » est-il au féminin singulier ?",
            ["Il s'accorde avec le COD « qu' » (la tâche), placé avant l'auxiliaire avoir", "Il s'accorde avec le sujet « les chroniqueurs »", "Le participe passé avec avoir s'accorde toujours au féminin", "C'est une faute de l'auteur"],
            "Il s'accorde avec le COD « qu' » (la tâche), placé avant l'auxiliaire avoir",
            "Le sujet « les chroniqueurs » est inversé. Le pronom relatif « que » reprend « la même tâche » et est COD : placé avant avoir, il impose l'accord."), BONNEFOY),
        S('francais', 'Étude de la langue · nature des mots', Q(
            "« Tandis que Cristóbal grandissait dans un univers de cosmogonies, Venezuela fut nommée… » Nature de « Tandis que » ?",
            ["Locution conjonctive de subordination", "Adverbe", "Préposition", "Conjonction de coordination"], "Locution conjonctive de subordination",
            "Elle introduit une subordonnée circonstancielle (ici de temps, avec une nuance d'opposition)."), BONNEFOY),
        S('francais', 'Étude de la langue · liens logiques', Q(
            "« Les villes changeaient, les langues se multipliaient, […] or les livres, eux, ne changeaient pas. » Nature de « or » et lien logique ?",
            ["Conjonction de coordination exprimant l'opposition", "Adverbe exprimant le temps", "Conjonction de subordination exprimant la cause", "Nom commun (le métal)"],
            "Conjonction de coordination exprimant l'opposition",
            "« Or » fait partie des conjonctions de coordination (mais, ou, et, donc, or, ni, car). On peut le remplacer par une conjonction de subordination : « alors que » ou « tandis que »."), BONNEFOY),
        S('francais', 'Étude de la langue · propositions', Q(
            "« … des cardinaux qui se demandaient si les conquistadors de la Patagonie avaient réellement vu la nation des géants. » Nature et fonction de « si les conquistadors… géants » ?",
            ["Subordonnée interrogative indirecte, COD de « se demandaient »", "Subordonnée circonstancielle de condition", "Subordonnée relative, complément du nom", "Proposition indépendante"],
            "Subordonnée interrogative indirecte, COD de « se demandaient »",
            "Introduite par « si » après un verbe de questionnement, elle rapporte une question (« Les conquistadors ont-ils vu… ? ») : ce n'est pas une condition."), BONNEFOY),
        S('francais', 'Lexique · familles de mots', Q(
            "Quel mot n'appartient pas à la même famille que « émerveillement » ?",
            ["Merle", "Merveille", "Émerveiller", "Merveilleux"], "Merle",
            "Merveille, merveilleux, émerveiller, émerveillement partagent le radical merveill-. « Merle » n'a que le son en commun."), BONNEFOY),
        S('francais', 'Lexique · formation et sens', Q(
            "« C'est là que réside la fondation invariable des hommes. » Quel synonyme convient à « invariable » en contexte ?",
            ["Immuable", "Changeant", "Fragile", "Variable"], "Immuable",
            "In- (négation) + variable (vari(er) + -able) : qui ne peut pas varier, qui ne change pas. Synonymes : immuable, constant, permanent."), BONNEFOY),
        S('francais', 'Lexique · sens d\'une image', Q(
            "Que signifie l'image « Les romans sont une île entourée de terre » ?",
            ["Pour un enfant toujours en voyage, les romans sont un refuge stable, un point fixe au milieu du mouvement", "Les romans parlent toujours d'îles", "Lire empêche de voyager", "Les romans sont ennuyeux comme une île déserte"],
            "Pour un enfant toujours en voyage, les romans sont un refuge stable, un point fixe au milieu du mouvement",
            "L'image renverse l'île habituelle (entourée d'eau) : pour Cristóbal, « lire c'était rester ». Les livres sont « un havre sans départ ni exil »."), BONNEFOY),
    ]),
    epreuve('Épreuve écrite disciplinaire de mathématiques', 20157, [
        S('mathematiques', 'Exercice 1 · PGCD', N(
            "On veut une règle de longueur entière (plus de 10 cm) qui permette d'espacer régulièrement les fraisiers sur 185 cm et sur 444 cm. Quelle est sa longueur, en cm ?", 37,
            "La longueur doit diviser 185 et 444 : 185 = 5 × 37 et 444 = 12 × 37. Le seul diviseur commun supérieur à 10 est 37 (le PGCD)."), FRAISES),
        S('mathematiques', 'Exercice 1 · dénombrement', N(
            "Avec un écart de 37 cm, combien de fraisiers les élèves pourront-ils planter, sommets compris ?", 78,
            "185 ÷ 37 = 5 intervalles, donc 6 plants ; 444 ÷ 37 = 12 intervalles, donc 13 plants. 6 × 13 = 78 fraisiers. Attention : il y a un plant de plus que d'intervalles."), FRAISES),
        S('mathematiques', 'Exercice 1 · pourcentages', N(
            "Un prix augmente de 2 %, puis de 3 %. Quel est le pourcentage d'augmentation globale ?", 5.06,
            "1,02 × 1,03 = 1,0506, soit +5,06 % (et non 5 %). Un plant à 1,20 € coûte alors 1,26 €."), None),
        S('mathematiques', 'Exercice 1 · fractions', Q(
            "Un neuvième des fraises ne peut pas être consommé ; un quart des fraises restantes sert à la confiture. Quelle proportion de la récolte sert à la confiture ?",
            ["2/9", "1/4", "1/36", "5/36"], "2/9",
            "Il reste 8/9 de la récolte ; un quart de 8/9 : 1/4 × 8/9 = 8/36 = 2/9. Si 3 kg vont à la confiture, la récolte pèse 3 ÷ 2/9 = 13,5 kg."), None),
        S('mathematiques', 'Exercice 1 · volumes', Q(
            "Une bassine est un grand cône (rayon 42 cm, hauteur 40 cm) dont on retire un petit cône. Quelle est la valeur exacte du volume du grand cône ?",
            ["23 520π cm³", "70 560π cm³", "1 680π cm³", "23 520 cm³"], "23 520π cm³",
            "V = π × r² × h ÷ 3 = π × 42² × 40 ÷ 3 = π × 1 764 × 40 ÷ 3 = 23 520π cm³. Le diamètre (84 cm) n'est pas le rayon."), None),
        S('mathematiques', 'Exercice 2 · statistiques', N(
            "Vitesses (m/s) et effectifs : 2,35 (2) ; 2,4 (5) ; 2,43 (8) ; 2,5 (12) ; 2,54 (13) ; 2,67 (10) ; 2,78 (7) ; 2,9 (3). Quelle est la vitesse médiane ?", 2.54,
            "60 élèves : la médiane est entre la 30e et la 31e valeur. Effectifs cumulés : 2, 7, 15, 27, 40. Les 30e et 31e valent 2,54 m/s. La moyenne vaut environ 2,57 m/s."), None),
        S('mathematiques', 'Exercice 3 · probabilités', N(
            "Le dé cubique donne le chiffre des dizaines, le dé tétraédrique celui des unités. Combien y a-t-il d'issues ?", 24,
            "6 × 4 = 24 nombres possibles, de 11 à 64."), DES),
        S('mathematiques', 'Exercice 3 · probabilités', Q(
            "Même jeu (dizaines au dé cubique, unités au dé tétraédrique). Quelle est la probabilité d'obtenir un nombre supérieur ou égal à 30 ?",
            ["2/3", "1/2", "4/6", "1/3"], "2/3",
            "Chiffre des dizaines de 3 à 6 : 4 × 4 = 16 issues sur 24, soit 2/3 (4/6 est égal mais non simplifié)."), DES),
        S('mathematiques', 'Exercice 3 · probabilités', Q(
            "Même jeu. Quelle est la probabilité d'obtenir un multiple de 3 ?",
            ["1/3", "1/4", "1/6", "1/2"], "1/3",
            "Multiples de 3 possibles : 12, 21, 24, 33, 42, 51, 54, 63, soit 8 issues sur 24 : 1/3."), DES),
        S('mathematiques', 'Exercice 3 · probabilités', Q(
            "On multiplie maintenant les deux résultats. Quelle est la probabilité d'obtenir un nombre pair multiple de 3 ?",
            ["1/3", "1/6", "1/4", "1/2"], "1/3",
            "Pair et multiple de 3 = multiple de 6. Produits concernés : 2×3, 3×2, 3×4, 4×3, 6×1, 6×2, 6×3, 6×4, soit 8 issues sur 24 : 1/3."), DES),
        S('mathematiques', 'Exercice 5 · vrai ou faux', Q(
            "NE = 2,04 m, EF = 9,6 dm et NF = 180 cm. Affirmation : « le triangle NEF est rectangle en F. » Vrai ou faux ?",
            ["Vrai : 96² + 180² = 204²", "Faux : les longueurs ne sont pas dans la même unité", "Faux : 96 + 180 ≠ 204", "Vrai : NE est le plus petit côté"], "Vrai : 96² + 180² = 204²",
            "En cm : NE = 204, EF = 96, NF = 180. 96² + 180² = 9 216 + 32 400 = 41 616 = 204². Par la réciproque de Pythagore, le triangle est rectangle au sommet opposé à [NE], c'est-à-dire en F."), None),
        S('mathematiques', 'Exercice 5 · vrai ou faux', Q(
            "Affirmation : « 6x² − 15x = 0 admet comme unique solution 2,5. » Vrai ou faux ?",
            ["Faux : 0 est aussi solution", "Vrai", "Faux : la solution est −2,5", "Faux : il n'y a aucune solution"], "Faux : 0 est aussi solution",
            "On factorise : x(6x − 15) = 0, donc x = 0 ou x = 2,5. Diviser par x fait perdre la solution 0."), None),
    ]),
    epreuve("Épreuve écrite d'application (sciences, histoire-géographie-EMC ou arts)", 20169, [
        # ── Sciences ──
        S('physique_chimie', 'Sciences · sources de lumière', Q(
            "Parmi les astres observés la nuit, lequel est une source primaire de lumière ?",
            ["Une étoile", "La Lune", "Une planète comme Vénus", "Un satellite artificiel"], "Une étoile",
            "Une source primaire produit sa propre lumière (une étoile, le Soleil). Un objet diffusant renvoie la lumière qu'il reçoit (la Lune, les planètes)."), NUIT),
        S('physique_chimie', 'Sciences · la photosynthèse', Q(
            "Pourquoi la photosynthèse est-elle une transformation chimique ?",
            ["Des espèces chimiques disparaissent (CO₂, eau) et de nouvelles apparaissent (glucose, dioxygène)", "Parce qu'elle a besoin de lumière", "Parce que l'eau change d'état", "Parce que la plante grandit"],
            "Des espèces chimiques disparaissent (CO₂, eau) et de nouvelles apparaissent (glucose, dioxygène)",
            "Équation : 6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂. Elle est ajustée : 6 carbones, 12 hydrogènes et 18 oxygènes de chaque côté."), NUIT),
        S('physique_chimie', 'Sciences · la molécule de glucose', Q(
            "Quelle est la composition de la molécule de glucose C₆H₁₂O₆ ?",
            ["6 atomes de carbone, 12 d'hydrogène et 6 d'oxygène", "6 atomes de calcium, 12 d'hélium et 6 d'oxygène", "6 atomes de carbone, 12 d'hydrogène et 6 d'azote", "24 atomes de carbone"], "6 atomes de carbone, 12 d'hydrogène et 6 d'oxygène",
            "Dans une formule chimique, l'indice suit le symbole de l'atome : C pour carbone, H pour hydrogène, O pour oxygène. Soit 24 atomes au total."), NUIT),
        S('physique_chimie', "Sciences · l'énergie d'un lampadaire", Q(
            "Un lampadaire convertit de l'énergie. Laquelle reçoit-il et laquelle fournit-il principalement ?",
            ["Il reçoit de l'énergie électrique et fournit de l'énergie lumineuse (avec une perte thermique)", "Il reçoit de l'énergie lumineuse et fournit de l'énergie électrique", "Il reçoit de l'énergie chimique et fournit de l'énergie cinétique", "Il ne convertit aucune énergie"],
            "Il reçoit de l'énergie électrique et fournit de l'énergie lumineuse (avec une perte thermique)",
            "Dans un diagramme de conversion, le convertisseur est au centre : énergie électrique en entrée, énergie lumineuse (utile) et énergie thermique (perdue) en sortie."), NUIT),
        S('svt', 'Sciences · la biodiversité nocturne', Q(
            "Réseau alimentaire nocturne : herbacée, chenille, escargot, fourmi, salamandre, hérisson, renard, hibou. Quel est le régime alimentaire de l'escargot ?",
            ["Végétarien (il mange des végétaux)", "Carnivore", "Omnivore", "Il ne se nourrit pas"], "Végétarien (il mange des végétaux)",
            "L'escargot consomme des plantes herbacées. Le hibou et le renard, qui mangent d'autres animaux, sont carnivores (le renard est plutôt omnivore dans la réalité)."), NUIT),
        S('svt', 'Sciences · les trames noires', Q(
            "Qu'est-ce qu'une trame noire ?",
            ["Un réseau de zones et de corridors assez sombres pour que les espèces nocturnes circulent, se nourrissent et se reproduisent", "Une route sans éclairage public", "Un filet qui protège les arbres la nuit", "Une carte des étoiles visibles"],
            "Un réseau de zones et de corridors assez sombres pour que les espèces nocturnes circulent, se nourrissent et se reproduisent",
            "Comme la trame verte et bleue pour les continuités écologiques, la trame noire relie des réservoirs de biodiversité, ici protégés de la pollution lumineuse."), NUIT),
        S('svt', 'Sciences · la classification', Q(
            "Lequel de ces verbes correspond à la construction d'une clé de détermination ?",
            ["Trier", "Ranger", "Classer"], "Trier",
            "Une clé de détermination procède par tris successifs selon un critère (« a un tragus / n'en a pas ») pour identifier un être vivant. Ranger, c'est ordonner ; classer, c'est regrouper selon des caractères partagés."), NUIT),
        S('svt', 'Sciences · les chauves-souris', Q(
            "Pourquoi les chauves-souris sont-elles de bonnes espèces indicatrices pour mettre en place une trame noire ?",
            ["Elles sont présentes partout et leurs ultrasons enregistrables révèlent leurs trajets nocturnes et les obstacles lumineux", "Elles sont très faciles à voir la nuit", "Elles ne craignent pas la lumière", "Elles vivent seulement en forêt"],
            "Elles sont présentes partout et leurs ultrasons enregistrables révèlent leurs trajets nocturnes et les obstacles lumineux",
            "Le programme de sciences participatives Vigie-Chiro (Vigie-Nature École) prête aux classes des enregistreurs d'ultrasons."), NUIT),
        S('technologie', 'Sciences · réduire la pollution lumineuse', Q(
            "Depuis 2025, une norme interdit les lampes d'extérieur dont le faisceau dépasse l'horizontale. Pourquoi ?",
            ["Pour éviter d'éclairer le ciel : la lumière n'est dirigée que vers le sol", "Pour éclairer plus loin", "Pour consommer plus d'électricité", "Pour éclairer les façades des immeubles"],
            "Pour éviter d'éclairer le ciel : la lumière n'est dirigée que vers le sol",
            "Une lumière envoyée vers le haut est perdue (gaspillage d'énergie) et crée un halo qui masque les étoiles et perturbe la faune."), NUIT),
        S('technologie', 'Sciences · un lampadaire intelligent', Q(
            "Un lampadaire micro:bit a un capteur de luminosité et un capteur de présence. Quel est l'intérêt de ce lampadaire ?",
            ["Il n'éclaire que la nuit et seulement quand quelqu'un passe : économie d'énergie et moins de pollution lumineuse", "Il éclaire en permanence plus fort", "Il change de couleur toute la nuit", "Il fonctionne sans électricité"],
            "Il n'éclaire que la nuit et seulement quand quelqu'un passe : économie d'énergie et moins de pollution lumineuse",
            "Le programme combine deux conditions : il fait nuit (luminosité < 100) ET une présence est détectée. Les DEL sont les actionneurs."), NUIT),
        # ── Histoire et EMC ──
        S('histoire_geographie', "Histoire · les traces des guerres mondiales", Q(
            "Selon l'historien Marc Bloch (document 3), qu'est-ce qu'une « trace » ?",
            ["La marque, perceptible aux sens, qu'a laissée un phénomène passé impossible à saisir directement", "Un souvenir personnel inventé", "Un manuel d'histoire", "Uniquement un document écrit"],
            "La marque, perceptible aux sens, qu'a laissée un phénomène passé impossible à saisir directement",
            "« Aucun égyptologue n'a vu Ramsès » : l'historien connaît le passé « par traces ». Monuments aux morts, plaques, lettres de soldats en sont des exemples proches des élèves."), GUERRES),
        S('histoire_geographie', 'Histoire · les traces des guerres mondiales', Q(
            "Selon la loi du 8 novembre 1920, où sont inhumés les restes du Soldat inconnu ?",
            ["Sous l'Arc de triomphe, à Paris", "Au Panthéon", "À Verdun, à l'ossuaire de Douaumont", "Aux Invalides"], "Sous l'Arc de triomphe, à Paris",
            "Les honneurs du Panthéon lui sont rendus le 11 novembre 1920, puis il est inhumé sous l'Arc de triomphe (article 2 de la loi)."), GUERRES),
        S('histoire_geographie', 'Histoire · les traces des guerres mondiales', Q(
            "Pourquoi six villages de la Meuse sont-ils dits « morts pour la France » ?",
            ["Ils ont été entièrement détruits pendant la bataille de Verdun (1916) et n'ont jamais été reconstruits", "Leurs habitants ont tous émigré en 1945", "Ils ont été inondés par un barrage", "Ils ont été détruits par un tremblement de terre"],
            "Ils ont été entièrement détruits pendant la bataille de Verdun (1916) et n'ont jamais été reconstruits",
            "Comme Louvemont-Côte-du-Poivre, ils n'ont plus d'habitants mais gardent un maire : ce sont des traces de la Grande Guerre dans le paysage."), GUERRES),
        S('emc', 'EMC · la commémoration du 8 mai 1945', Q(
            "Que commémore-t-on le 8 mai ?",
            ["La victoire des Alliés et la fin de la Seconde Guerre mondiale en Europe, en 1945", "L'armistice de la Première Guerre mondiale", "La prise de la Bastille", "La libération de Paris"],
            "La victoire des Alliés et la fin de la Seconde Guerre mondiale en Europe, en 1945",
            "Le 11 novembre commémore l'armistice de 1918. En fin de CM2, les élèves « comprennent la signification du 11 novembre et du 8 mai, notamment dans le cadre de la participation aux cérémonies »."), GUERRES),
        S('emc', 'EMC · la commémoration du 8 mai 1945', Q(
            "Pourquoi la participation à une commémoration aide-t-elle à construire une culture civique ?",
            ["Elle relie l'histoire nationale à des lieux proches (le monument aux morts), transmet la mémoire et fait vivre un engagement collectif", "Elle remplace les cours d'histoire", "Elle permet de manquer l'école", "Elle sert à apprendre le solfège"],
            "Elle relie l'histoire nationale à des lieux proches (le monument aux morts), transmet la mémoire et fait vivre un engagement collectif",
            "Les élèves « identifient les monuments comme la mémoire de la Nation » (repères de CM2). La cérémonie se prépare en classe : sens de l'événement, lecture de noms, chant, attitude attendue."), GUERRES),
        S('emc', 'EMC · les symboles de la République et de l\'Europe', Q(
            "D'où vient la musique de l'hymne européen, étudiée en CM2 ?",
            ["De la 9e symphonie de Beethoven", "De La Marseillaise", "Des Quatre Saisons de Vivaldi", "D'un chant de la Résistance"], "De la 9e symphonie de Beethoven",
            "Les repères de CM2 citent les symboles de l'Union européenne : le drapeau, le nombre d'étoiles (12) et l'hymne, l'« Ode à la joie » de la 9e symphonie."),
          "Document 2 : repères annuels de progression de CM2 (2024), EMC."),
        # ── Arts ──
        S('arts', 'Arts plastiques · le collage', Q(
            "Selon le document cité dans le sujet, qu'est-ce qu'un collage en arts plastiques ?",
            ["L'insertion d'un corps étranger dans un contexte donné", "Une peinture à l'huile sur toile", "Un dessin au crayon", "Une sculpture en bronze"], "L'insertion d'un corps étranger dans un contexte donné",
            "La citation poursuit : pas seulement « d'un morceau de papier ». Le collage crée du sens par la rencontre d'éléments hétérogènes."),
          "Dossier d'arts plastiques (cycle 3) : Nicole Morin et Ghislaine Bellocq, Des techniques au service du projet."),
        S('arts', 'Éducation musicale · les univers sonores', Q(
            "À quelle période musicale appartiennent « Les Quatre Saisons » d'Antonio Vivaldi (1725) ?",
            ["Baroque", "Romantique", "Classique", "Contemporaine"], "Baroque",
            "La période baroque va environ de 1600 à 1750 (Vivaldi, Bach, Haendel). Le 3e mouvement de « L'été » évoque un orage d'été, par des traits rapides des cordes."),
          "Dossier « univers sonores » (cycle 1, grande section) : une fiche de séance d'écoute de « L'été » de Vivaldi, à analyser."),
        S('arts', 'Éducation musicale · les univers sonores', Q(
            "« Les Quatre Saisons » est un ensemble de quatre :",
            ["Concertos pour violon", "Symphonies", "Opéras", "Lieder"], "Concertos pour violon",
            "Chaque saison est un concerto en trois mouvements (vif, lent, vif) pour violon soliste et orchestre à cordes, accompagné d'un sonnet qui décrit la scène."), None),
    ]),
    # ── Ajout : questions complémentaires tirées du même sujet ──
    epreuve('Épreuve écrite disciplinaire de français', 20145, [
        S('francais', 'Étude de la langue · temps et voix', Q(
            "« Devenue diplomate, elle commença à voyager. » Temps, voix et infinitif de « commença » ?",
            ["Passé simple, voix active, commencer", "Imparfait, voix active, commencer", "Passé simple, voix passive, commencer", "Passé composé, voix active, commencer"], "Passé simple, voix active, commencer",
            "Le c prend une cédille devant a pour garder le son [s] : commença."), BONNEFOY),
        S('francais', 'Étude de la langue · temps et voix', Q(
            "« … la même tâche qu'avaient accomplie les chroniqueurs. » Temps et voix de « avaient accomplie » ?",
            ["Plus-que-parfait, voix active", "Plus-que-parfait, voix passive", "Passé antérieur, voix active", "Imparfait, voix passive"], "Plus-que-parfait, voix active",
            "Auxiliaire avoir à l'imparfait + participe passé : plus-que-parfait. L'auxiliaire avoir indique ici un temps composé de la voix active, pas une voix passive."), BONNEFOY),
        S('francais', 'Étude de la langue · nature des mots', Q(
            "« … représentant sa patrie à l'étranger, effectuant la même tâche… » Nature de « représentant » ?",
            ["Participe présent", "Nom commun", "Adjectif verbal", "Gérondif"], "Participe présent",
            "Il exprime une action et a un complément (« sa patrie ») : participe présent, invariable. Sans « en », ce n'est pas un gérondif ; le nom « représentant » existe aussi, mais pas ici."), BONNEFOY),
        S('francais', 'Étude de la langue · liens logiques', Q(
            "Remplacez « or » par une conjonction de subordination : « Les villes changeaient, […] or les livres, eux, ne changeaient pas. »",
            ["Les villes changeaient, alors que les livres, eux, ne changeaient pas.", "Les villes changeaient, donc les livres ne changeaient pas.", "Les villes changeaient, car les livres ne changeaient pas.", "Les villes changeaient, et les livres ne changeaient pas."],
            "Les villes changeaient, alors que les livres, eux, ne changeaient pas.",
            "« Alors que » ou « tandis que » expriment l'opposition. « Donc » et « car » sont des conjonctions de coordination (conséquence, cause)."), BONNEFOY),
        S('francais', 'Lexique · sens en contexte', Q(
            "« Cristóbal s'attelait à ces royaumes pétrifiés. » Que désignent ces « royaumes pétrifiés » ?",
            ["Les livres, immobiles et immuables comme la pierre", "Des pays visités", "Des villes en ruines", "Des statues de musée"], "Les livres, immobiles et immuables comme la pierre",
            "« Les pages ont l'immobilité du métal et de l'agate » : pour l'enfant toujours en voyage, les livres sont ce qui ne change pas."), BONNEFOY),
        S('francais', 'Lexique · sens en contexte', Q(
            "Pourquoi Cristóbal pense-t-il que « lire, ce n'est pas voyager », contrairement à sa mère ?",
            ["Parce que, pour un enfant qui déménage sans cesse, lire c'est au contraire rester, retrouver quelque chose de stable", "Parce qu'il n'aime pas lire", "Parce que les livres parlent de voyages imaginaires", "Parce qu'il a peur de l'avion"],
            "Parce que, pour un enfant qui déménage sans cesse, lire c'est au contraire rester, retrouver quelque chose de stable",
            "Le texte renverse la formule de Venezuela : « pour Cristóbal, dont l'enfance n'avait été que voyages, lire c'était rester »."), BONNEFOY),
        S('francais', 'Culture · notes du texte', Q(
            "Qui était Fernand de Magellan, cité dans le texte ?",
            ["Un navigateur portugais qui découvrit le détroit entre l'Atlantique et le Pacifique", "Un conquistador qui soumit l'Empire inca", "Un roi d'Espagne", "Un écrivain vénézuélien"], "Un navigateur portugais qui découvrit le détroit entre l'Atlantique et le Pacifique",
            "Pizarro est le conquistador qui soumit l'Empire inca. Les deux noms nourrissent l'imaginaire de l'enfant lecteur."), BONNEFOY),
    ]),
    epreuve('Épreuve écrite disciplinaire de mathématiques', 20157, [
        S('mathematiques', 'Exercice 1 · pourcentages', N(
            "Un plant à 1,20 € augmente de 2 %, puis de 3 %. Quel est son nouveau prix, arrondi au centime, en euros ?", 1.26,
            "1,20 × 1,02 × 1,03 = 1,26072 ≈ 1,26 €."), None),
        S('mathematiques', 'Exercice 1 · fractions', N(
            "3 kg de fraises, soit 2/9 de la récolte, servent à la confiture. Quelle est la masse de la récolte, en kg ?", 13.5,
            "Récolte = 3 ÷ 2/9 = 3 × 9/2 = 13,5 kg."), None),
        S('mathematiques', 'Exercice 1 · Thalès', N(
            "Bassine : grand cône de rayon 42 cm ; OC = 22 cm ; CA = 18,9 cm ; (AC) // (OB). Combien mesure OS, en cm ?", 40,
            "Thalès : SC/SO = CA/OB = 18,9/42 = 0,45. SC = SO − 22, donc SO − 22 = 0,45 SO, soit 0,55 SO = 22 et SO = 40 cm."), None),
        S('mathematiques', 'Exercice 1 · volumes', N(
            "Le volume de la bassine (grand cône moins petit cône) vaut environ 67 157 cm³. Combien cela fait-il de litres, arrondi au centilitre ?", 67.16,
            "1 L = 1 000 cm³ : 67 157 cm³ ≈ 67,16 L."), None),
        S('mathematiques', 'Exercice 1 · dénombrement', N(
            "Sur la longueur de 444 cm, avec un écart de 37 cm entre deux fraisiers, combien de plants (extrémités comprises) ?", 13,
            "444 ÷ 37 = 12 intervalles, donc 13 plants."), FRAISES),
        S('mathematiques', 'Exercice 2 · statistiques', N(
            "Vitesses (m/s) et effectifs : 2,35 (2) ; 2,4 (5) ; 2,43 (8) ; 2,5 (12) ; 2,54 (13) ; 2,67 (10) ; 2,78 (7) ; 2,9 (3). Vitesse moyenne, arrondie au centième ?", 2.57,
            "Somme des produits : 154,02 ; effectif total : 60. 154,02 ÷ 60 ≈ 2,57 m/s.", tol=0.005), None),
        S('mathematiques', 'Exercice 3 · probabilités', Q(
            "On multiplie les résultats d'un dé à 6 faces et d'un dé à 4 faces. Lequel de ces événements est impossible ?",
            ["Obtenir 25", "Obtenir 24", "Obtenir 1", "Obtenir 12"], "Obtenir 25",
            "Le produit maximal est 6 × 4 = 24. 25 = 5 × 5 est impossible, puisque le dé à 4 faces ne donne jamais 5."), DES),
    ]),
    epreuve("Épreuve écrite d'application (sciences, histoire-géographie-EMC ou arts)", 20169, [
        S('physique_chimie', 'Sciences · la distance Terre-Lune', N(
            "Une impulsion laser fait l'aller-retour Terre-Lune (384 000 km) à 3,00 × 10⁸ m/s. Combien de temps dure l'aller-retour, en secondes ?", 2.56,
            "Distance aller-retour : 2 × 3,84 × 10⁸ m = 7,68 × 10⁸ m. t = d ÷ v = 7,68 × 10⁸ ÷ 3 × 10⁸ = 2,56 s."), NUIT),
        S('physique_chimie', 'Sciences · les phases de la Lune', Q(
            "Pourquoi n'observe-t-on pas toujours le même aspect de la Lune ?",
            ["La Lune tourne autour de la Terre : on voit plus ou moins sa face éclairée par le Soleil", "L'ombre de la Terre cache chaque soir une partie de la Lune", "La Lune change de forme", "Les nuages la cachent"],
            "La Lune tourne autour de la Terre : on voit plus ou moins sa face éclairée par le Soleil",
            "L'ombre de la Terre n'explique que les éclipses, pas les phases : c'est une conception erronée fréquente. La modélisation Soleil-Terre-Lune permet de la dépasser."), NUIT),
        S('physique_chimie', 'Sciences · les phases de la Lune', Q(
            "Comment expliquer à un élève de CM1 ce que signifie « modéliser » ?",
            ["Représenter, avec des objets ou un schéma, un phénomène trop grand ou trop lointain pour être observé directement", "Copier un modèle de dessin", "Fabriquer un objet décoratif", "Apprendre une leçon par cœur"],
            "Représenter, avec des objets ou un schéma, un phénomène trop grand ou trop lointain pour être observé directement",
            "Par exemple, une lampe (le Soleil), un ballon (la Terre) et une balle (la Lune) pour comprendre les phases."), NUIT),
        S('svt', 'Sciences · les pelotes de réjection', Q(
            "Pourquoi étudier en classe des pelotes de réjection ramassées dans la nature peut-il poser problème ?",
            ["Pour des raisons d'hygiène : il faut des pelotes stérilisées, achetées chez un fournisseur, et des gants", "Parce qu'elles sont trop chères", "Parce que les élèves ne savent pas ce qu'est un hibou", "Parce qu'elles sentent bon"],
            "Pour des raisons d'hygiène : il faut des pelotes stérilisées, achetées chez un fournisseur, et des gants",
            "Une pelote ramassée peut contenir des germes ; on peut aussi utiliser des photographies ou des vidéos de dissection."), NUIT),
        S('svt', 'Sciences · les pelotes de réjection', Q(
            "Que contient une pelote de réjection de hibou ?",
            ["Les restes non digérés de ses proies : os, poils, plumes", "Des œufs", "Des graines", "Des excréments liquides"], "Les restes non digérés de ses proies : os, poils, plumes",
            "Le rapace la régurgite : l'analyse des os permet d'identifier ses proies et donc son régime alimentaire."), NUIT),
        S('svt', 'Sciences · la biodiversité nocturne', Q(
            "Comment modéliser l'interdépendance des espèces avec des pelotes de laine et des cartes d'espèces ?",
            ["Chaque élève tient une carte d'espèce ; on relie par la laine celui qui mange à celui qui est mangé ; si les chenilles disparaissent, on lâche leurs fils et on observe qui est touché", "On fait un dessin libre", "On classe les cartes par couleur", "On lit les cartes à voix haute"],
            "Chaque élève tient une carte d'espèce ; on relie par la laine celui qui mange à celui qui est mangé ; si les chenilles disparaissent, on lâche leurs fils et on observe qui est touché",
            "Le jeu de rôle rend visible le réseau alimentaire et l'effet en cascade de la disparition d'une espèce."), NUIT),
        S('svt', 'Sciences · les sciences participatives', Q(
            "En quoi un programme de sciences participatives comme Vigie-Nature École aide-t-il à « pratiquer des démarches scientifiques » ?",
            ["Les élèves suivent un protocole rigoureux, collectent de vraies données utilisées par des chercheurs et les interprètent", "Ils regardent un film documentaire", "Ils apprennent une liste d'espèces", "Ils dessinent librement"],
            "Les élèves suivent un protocole rigoureux, collectent de vraies données utilisées par des chercheurs et les interprètent",
            "Lancé en 2010, Vigie-Nature École permet aux classes de participer à de vrais programmes de recherche sur la biodiversité ordinaire."), NUIT),
        S('technologie', 'Sciences · un lampadaire intelligent', Q(
            "Dans le lampadaire micro:bit, il fait nuit quand la valeur du capteur de luminosité est inférieure à 100. Quelle condition allume les DEL ?",
            ["Luminosité < 100 ET présence détectée", "Luminosité > 100 OU présence détectée", "Luminosité < 100 seulement", "Présence détectée seulement"], "Luminosité < 100 ET présence détectée",
            "Les deux conditions doivent être vraies : la nuit, et quelqu'un passe. C'est ce qui permet d'économiser l'énergie."), NUIT),
        S('histoire_geographie', 'Histoire · les traces des guerres mondiales', Q(
            "Une carte postale envoyée par un soldat en 1917, « en franchise », est :",
            ["Une source historique écrite, trace directe de la Grande Guerre", "Un manuel d'histoire", "Un témoignage inventé", "Un document du XXIe siècle"], "Une source historique écrite, trace directe de la Grande Guerre",
            "La franchise permettait aux soldats d'écrire gratuitement. Ces correspondances sont des traces proches des élèves (archives familiales)."), GUERRES),
        S('histoire_geographie', 'Histoire · les traces des guerres mondiales', Q(
            "Dans « Un sac de billes » (Joseph Joffo), pourquoi les deux frères doivent-ils fuir en 1943 ?",
            ["Parce qu'ils sont juifs et persécutés sous l'Occupation", "Parce qu'ils ont volé des billes", "Parce qu'ils partent en vacances", "Parce qu'ils sont recherchés par la police pour un crime"],
            "Parce qu'ils sont juifs et persécutés sous l'Occupation",
            "Ce récit autobiographique permet d'aborder avec des CM2 la persécution des Juifs pendant la Seconde Guerre mondiale."), GUERRES),
        S('histoire_geographie', 'Histoire · les traces des guerres mondiales', Q(
            "Pourquoi s'appuyer sur le monument aux morts de la commune avec des CM2 ?",
            ["C'est une trace proche, que l'on peut observer, et qui montre l'ampleur des pertes dans chaque village", "Parce que c'est le seul document disponible", "Pour apprendre l'architecture", "Pour connaître les noms de rues"],
            "C'est une trace proche, que l'on peut observer, et qui montre l'ampleur des pertes dans chaque village",
            "Le programme invite à partir « des traces de ces conflits dans l'environnement des élèves ». Le dossier en montrait un à Saint-Louis, en Guadeloupe."), GUERRES),
        S('emc', 'EMC · les commémorations', Q(
            "Que commémore-t-on le 11 novembre ?",
            ["L'armistice de 1918, qui met fin aux combats de la Première Guerre mondiale", "La fin de la Seconde Guerre mondiale", "La prise de la Bastille", "L'appel du 18 juin"], "L'armistice de 1918, qui met fin aux combats de la Première Guerre mondiale",
            "Depuis 2012, le 11 novembre rend aussi hommage à tous les morts pour la France."), GUERRES),
        S('emc', 'EMC · les commémorations', Q(
            "Comment préparer des élèves à participer à une cérémonie du 8 mai ?",
            ["Expliquer le sens de l'événement, préparer la lecture de noms ou un chant, et l'attitude attendue pendant la cérémonie", "Les emmener sans préparation", "Leur faire apprendre la date par cœur seulement", "Organiser une fête"],
            "Expliquer le sens de l'événement, préparer la lecture de noms ou un chant, et l'attitude attendue pendant la cérémonie",
            "La cérémonie devient une expérience civique : les élèves comprennent la signification du 8 mai et le rôle du monument aux morts."), GUERRES),
        S('arts', 'Éducation musicale · les univers sonores', Q(
            "En grande section, comment faire écouter « L'été » de Vivaldi à de jeunes élèves ?",
            ["Par des écoutes courtes et répétées, avec le corps et le geste, en lien avec ce que la musique évoque (l'orage)", "Par une écoute de 30 minutes en silence", "En lisant la partition", "En leur faisant écrire leurs impressions"],
            "Par des écoutes courtes et répétées, avec le corps et le geste, en lien avec ce que la musique évoque (l'orage)",
            "Au cycle 1, l'attention est brève et l'écoute passe par le mouvement et l'expression orale."), None),
        S('arts', 'Arts plastiques · le collage', Q(
            "Quelle compétence de cycle 3 un travail de collage permet-il de développer ?",
            ["Expérimenter, produire, créer en associant des matériaux et des images hétérogènes", "Recopier une œuvre au crayon", "Apprendre une date", "Mesurer des longueurs"],
            "Expérimenter, produire, créer en associant des matériaux et des images hétérogènes",
            "Le collage fait naître du sens par la rencontre d'éléments différents ; le document du dossier parle d'une « pensée divergente »."), None),
    ]),
]
