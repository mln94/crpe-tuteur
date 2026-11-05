# Bac+5, session 2026, groupement 1
from slib import S, Q, N, C, epreuve

MAALOUF = ("Texte : Amin Maalouf, Le Périple de Baldassare (2000). Le narrateur, un marchand de Gibelet, commence un carnet où il consigne son voyage ; "
           "il évoque son premier cahier perdu et sa fuite de Londres en flammes.")
MUSEE = "Exercice 1 : tarifs d'un musée pour les groupes scolaires : adulte 16 €, enfant 8,50 €, réduction de 15 % du montant global pour les groupes de 50 personnes et plus."
TOMBOLA = "Exercice 2 : une tombola de 500 tickets à 2 €. Lots : 1 de 100 €, 2 de 50 €, 5 de 10 €, 20 de 5 €, 50 de 2 €. Les autres tickets portent la mention « Perdu »."
CROSS = "Exercice 3 : parcours de cross. A, B, E alignés ; A, C, D alignés ; ABC rectangle en B. AE = 15 m, AC = 65 m, AB = 25 m, AD = 39 m."
EAU = "Sujet de sciences et technologie : un projet d'aménagement hydraulique à La Réunion (qualité, traitement et distribution de l'eau)."
MONTAGNE = "Sujet d'histoire-géographie et EMC : une séquence de géographie de CE2 sur les paysages de montagne, puis l'EMC et le bien commun."

QUESTIONS = [
    epreuve('Épreuve écrite disciplinaire de français', 20142, [
        S('francais', 'Étude de la langue · nature et fonction', Q(
            "« … un cahier de feuilles cousues, dont je noircis en cet instant la toute première page. » Quelle est la fonction du pronom relatif « dont » ?",
            ["Complément du nom « page »", "COD du verbe « noircir »", "Sujet du verbe « noircir »", "Complément circonstanciel de lieu"], "Complément du nom « page »",
            "Je noircis la première page du cahier : « dont » remplace « du cahier » et complète le nom « page ». Erreur la plus fréquente : le prendre pour le COD de « noircir » (Reims, Limoges, Nantes)."), MAALOUF),
        S('francais', 'Étude de la langue · nature et fonction', Q(
            "« Mais je ne suis pas sûr que je continuerai. » Nature et fonction de « sûr » ?",
            ["Adjectif qualificatif, attribut du sujet « je »", "Adverbe, complément circonstanciel", "Adjectif, épithète", "Préposition"], "Adjectif qualificatif, attribut du sujet « je »",
            "« Sûr » est relié au sujet par le verbe d'état « être ». Limoges relève des copies qui en font un adverbe ou une préposition."), MAALOUF),
        S('francais', 'Étude de la langue · nature et fonction', Q(
            "« Je me suis finalement procuré ce matin un cahier de feuilles cousues. » Fonction de « un cahier de feuilles cousues » ?",
            ["COD du verbe « se procurer »", "Sujet inversé", "Attribut du sujet", "Complément du nom « matin »"], "COD du verbe « se procurer »",
            "On se procure quoi ? un cahier. Il faut écrire le verbe pronominal en entier : « procurer » seul a été pénalisé (Limoges)."), MAALOUF),
        S('francais', 'Étude de la langue · temps, mode et voix', Q(
            "« Que ce cahier survive ou qu'il brûle, j'écrirai. » Temps et mode de « brûle » ?",
            ["Présent du subjonctif", "Présent de l'indicatif", "Futur de l'indicatif", "Impératif présent"], "Présent du subjonctif",
            "« Que… ou que… » introduit une concession qui appelle le subjonctif. Ce subjonctif n'a souvent pas été repéré (Créteil, Reims, Nantes, Limoges)."), MAALOUF),
        S('francais', 'Étude de la langue · temps, mode et voix', Q(
            "« Lorsque l'incendie s'était déclaré, j'avais été contraint de me cacher. » Quelle est la voix de « s'était déclaré » ?",
            ["Voix pronominale", "Voix passive", "Voix active", "Voix réfléchie impersonnelle"], "Voix pronominale",
            "Le verbe est conjugué avec un pronom réfléchi (s') : voix pronominale, au plus-que-parfait de l'indicatif. Beaucoup ne connaissent que l'actif et le passif (Dijon, Limoges)."), MAALOUF),
        S('francais', 'Étude de la langue · propositions', Q(
            "« Le premier cahier, qui racontait le commencement de mon périple, s'est perdu lorsque je dus quitter Constantinople à la hâte. » Nature de « lorsque je dus quitter Constantinople à la hâte » ?",
            ["Subordonnée conjonctive circonstancielle de temps", "Subordonnée relative", "Subordonnée complétive", "Proposition principale"], "Subordonnée conjonctive circonstancielle de temps",
            "Introduite par « lorsque », elle situe l'action dans le temps. La relative « qui racontait… » est insérée dans la principale, qu'il fallait délimiter (Créteil)."), MAALOUF),
        S('francais', 'Étude de la langue · accords', Q(
            "Mise au pluriel : « … lorsque je devais parfois jeter au feu un vieux livre pourrissant et décomposé, je ne pouvais m'empêcher de songer au malheureux qui l'avait écrit. » Quelle fin de phrase est correcte ?",
            ["… de vieux livres pourrissants et décomposés, nous ne pouvions nous empêcher de songer aux malheureux qui les avaient écrits.",
             "… de vieux livres pourrissant et décomposés, nous ne pouvions nous empêcher de songer aux malheureux qui les avaient écrit.",
             "… de vieux livres pourrissants et décomposés, nous ne pouvions nous empêcher de songer aux malheureux qui les avaient écrit.",
             "… de vieux livres pourrissant et décomposé, nous ne pouvions nous empêcher de songer aux malheureux qui les avait écrits."],
            "… de vieux livres pourrissants et décomposés, nous ne pouvions nous empêcher de songer aux malheureux qui les avaient écrits.",
            "« Pourrissants » est ici un adjectif verbal, qui s'accorde (le participe présent, lui, est invariable). « Écrits » s'accorde avec le COD « les » placé avant l'auxiliaire avoir."), MAALOUF),
        S('francais', 'Lexique · sens en contexte', Q(
            "« Je noircis, non sans volupté, la toute première page. » Que signifie « non sans volupté » ?",
            ["Avec plaisir", "Sans aucun plaisir", "Avec difficulté", "Avec tristesse"], "Avec plaisir",
            "La double négation (non + sans) renverse le sens : c'est une litote. La majorité des candidats a compris l'inverse (Reims, Nantes)."), MAALOUF),
        S('francais', 'Lexique · sens en contexte', Q(
            "Dans « populace écervelée », quelle est la valeur du suffixe -ace ?",
            ["Péjorative", "Diminutive", "Mélioratrice", "Neutre"], "Péjorative",
            "Comme dans paperasse, vinasse ou fadasse. « Écervelée » signifie « sans cervelle » : le narrateur juge sévèrement la foule de Londres déchaînée."), MAALOUF),
        S('francais', 'Lexique · familles de mots', Q(
            "Lequel de ces mots appartient à la même famille que « culpabilité » ?",
            ["Disculper", "Cupide", "Coupure", "Culte"], "Disculper",
            "Même radical latin culpa (la faute) : coupable, culpabiliser, inculper, disculper. Cupide et coupure ne se rapprochent que par le son, une erreur relevée par Bordeaux."), MAALOUF),
        S('francais', 'Lexique · familles de mots', Q(
            "Lequel de ces mots appartient à la même famille que « furie » ?",
            ["Furibond", "Fureter", "Colère", "Folie"], "Furibond",
            "Furieux, fureur, furibond, furieusement. « Colère » est un synonyme (même champ lexical), pas un mot de la même famille ; « fureter » n'a que le son en commun."), MAALOUF),
    ]),
    epreuve('Épreuve écrite disciplinaire de mathématiques', 20154, [
        S('mathematiques', 'Exercice 1 · tableur', Q(
            "Colonne B : nombre de personnes ; colonne C : tarif. Quelle formule saisir en D2, à étirer vers le bas, pour le montant de chaque ligne ?",
            ["=B2*C2", "B2*C2", "=SOMME(B2:C2)", "=B2+C2"], "=B2*C2",
            "Montant = effectif × tarif. Une formule commence toujours par « = »."), MUSEE),
        S('mathematiques', 'Exercice 1 · tableur', Q(
            "Le montant total avant réduction est en D8. Quelle formule saisir en D9 pour appliquer la réduction de 15 % ?",
            ["=D8*0,85", "=D8*0,15", "=D8-15", "=D8*1,15"], "=D8*0,85",
            "Baisser de 15 %, c'est multiplier par 1 − 0,15 = 0,85. Avec un total de 724 €, on obtient 615,40 €."), MUSEE),
        S('mathematiques', 'Exercice 1 · calcul littéral', Q(
            "n élèves sont accompagnés de 4 adultes, et le groupe compte moins de 50 personnes. Quel est le coût total de la visite, en euros ?",
            ["8,5n + 64", "8,5n + 16", "(8,5n + 64) × 0,85", "16n + 34"], "8,5n + 64",
            "Le groupe compte au plus 45 personnes : pas de réduction. n élèves à 8,50 € et 4 adultes à 16 € (64 €). Limoges regrette que la condition « moins de 50 » soit rarement justifiée."), MUSEE),
        S('mathematiques', 'Exercice 1 · équation', N(
            "L'école a payé 378,50 € pour n élèves et 4 adultes (coût 8,5n + 64). Combien d'élèves ont participé ?", 37,
            "8,5n + 64 = 378,5 donne 8,5n = 314,5, soit n = 37."), MUSEE),
        S('mathematiques', 'Exercice 1 · vitesse', N(
            "L'autocar parcourt 85 km en 1 h 10 min. Quelle est sa vitesse moyenne, en km/h, arrondie à l'unité ?", 73,
            "1 h 10 min = 7/6 h (et non 1,10 h). 85 ÷ 7/6 ≈ 72,9, soit environ 73 km/h."), None),
        S('mathematiques', 'Exercice 2 · probabilités', Q(
            "Quelle est la probabilité de tirer un ticket qui fait gagner un lot de 50 € ?",
            ["1/250", "1/500", "2/50", "1/50"], "1/250",
            "Il y a 2 lots de 50 € sur 500 tickets : 2/500 = 1/250 (fraction irréductible)."), TOMBOLA),
        S('mathematiques', 'Exercice 2 · probabilités', Q(
            "Quelle est la probabilité de tirer un ticket qui fait gagner un lot strictement supérieur à la mise de 2 € ?",
            ["7/125", "78/500", "39/250", "1/25"], "7/125",
            "Lots de plus de 2 € : 1 + 2 + 5 + 20 = 28. 28/500 = 7/125. Les lots de 2 € remboursent la mise, ils ne lui sont pas strictement supérieurs."), TOMBOLA),
        S('mathematiques', 'Exercice 2 · probabilités', Q(
            "Quelle est la probabilité de tirer un ticket « Perdu » ?",
            ["211/250", "422/500", "39/250", "1/2"], "211/250",
            "78 tickets gagnants (1 + 2 + 5 + 20 + 50), donc 422 perdants : 422/500 = 211/250. 422/500 est juste mais non irréductible."), TOMBOLA),
        S('mathematiques', 'Exercice 2 · médiane', N(
            "Tickets vendus par élève : 4 (10 élèves), 6 (4), 7 (8), 10 (14), 15 (12), 20 (3). Quelle est la médiane ?", 10,
            "51 élèves : la médiane est la 26e valeur. Effectifs cumulés : 10, 14, 22, 36. La 26e valeur est 10. Au moins la moitié des élèves ont vendu 10 tickets ou moins."), None),
        S('mathematiques', 'Exercice 3 · Pythagore', N(
            "ABC est rectangle en B, AC = 65 m et AB = 25 m. Combien vaut BC, en m ?", 60,
            "BC² = 65² − 25² = 4 225 − 625 = 3 600, donc BC = 60 m."), CROSS),
        S('mathematiques', 'Exercice 3 · Thalès', Q(
            "Pour montrer que (BC) et (DE) sont parallèles, quelle propriété utilise-t-on ?",
            ["La réciproque du théorème de Thalès, car AE/AB = AD/AC = 0,6 avec les points dans le même ordre", "Le théorème de Thalès", "Le théorème de Pythagore", "La réciproque du théorème de Pythagore"],
            "La réciproque du théorème de Thalès, car AE/AB = AD/AC = 0,6 avec les points dans le même ordre",
            "Pour démontrer un parallélisme, c'est la réciproque. 15/25 = 0,6 et 39/65 = 0,6, et E, A, B d'une part, D, A, C d'autre part sont alignés dans le même ordre. C'est cette question qui a classé les copies."), CROSS),
        S('mathematiques', 'Exercice 3 · longueurs', N(
            "Quelle est la longueur du parcours EBCDE, en m ? (BC = 60 m, DE = 36 m)", 240,
            "EB = 15 + 25 = 40 m, CD = 65 + 39 = 104 m. Total : 40 + 60 + 104 + 36 = 240 m."), CROSS),
        S('mathematiques', 'Exercice 3 · masse volumique', N(
            "Un plot a un volume de 6,45 dm³ et est rempli de sable de masse volumique 1,6 t/m³. Quelle est sa masse, en kg, arrondie au dixième ?", 10.3,
            "1,6 t/m³ = 1,6 kg/dm³. 6,45 × 1,6 = 10,32 ≈ 10,3 kg.", tol=0.05), None),
        S('mathematiques', 'Exercice 4 · vrai ou faux', Q(
            "Affirmation : « Si a est un multiple de b et b un multiple de c (c non nul), alors a/c est un entier. » Vrai ou faux ?",
            ["Vrai", "Faux"], "Vrai",
            "a = kb et b = mc (k et m entiers), donc a = (km)c et a/c = km est entier. Seules 25 % des copies réussissent cette question (Nantes) : un exemple ne suffit pas."), None),
        S('mathematiques', 'Exercice 4 · vrai ou faux', Q(
            "Affirmation : « Après trois augmentations successives de 20 %, un prix a augmenté de 72,8 %. » Vrai ou faux ?",
            ["Vrai : 1,2³ = 1,728", "Faux : il a augmenté de 60 %", "Faux : il a augmenté de 80 %", "Faux : il a augmenté de 20 %"], "Vrai : 1,2³ = 1,728",
            "Les coefficients multiplicateurs se multiplient : 1,2 × 1,2 × 1,2 = 1,728, soit +72,8 %. On n'additionne pas les pourcentages."), None),
        S('mathematiques', 'Exercice 4 · vrai ou faux', Q(
            "Affirmation : « Tout nombre divisible par 4 est divisible par 12. » Vrai ou faux ?",
            ["Faux : 8 est un contre-exemple", "Vrai : 12 est un multiple de 4", "Vrai : on le vérifie avec 12 et 24", "Faux : aucun multiple de 4 n'est multiple de 12"], "Faux : 8 est un contre-exemple",
            "C'est l'inverse qui est vrai : tout multiple de 12 est multiple de 4. Un seul contre-exemple suffit."), None),
        S('mathematiques', 'Exercice 5 · parallélogramme et Scratch', N(
            "Un parallélogramme a un angle de 30°. Combien mesure l'angle consécutif α, en degrés ?", 150,
            "Deux angles consécutifs d'un parallélogramme sont supplémentaires : α = 180° − 30° = 150°. Pour tracer un angle α avec Scratch, le lutin tourne de 180° − α."), None),
    ]),
    epreuve("Épreuve écrite d'application (sciences, histoire-géographie-EMC ou arts)", 20166, [
        # ── Sciences ──
        S('physique_chimie', "Sciences · les changements d'état de l'eau", Q(
            "Comment s'appelle le passage de l'état solide directement à l'état gazeux ?",
            ["La sublimation", "La fusion", "La vaporisation", "La solidification"], "La sublimation",
            "Les six changements d'état : fusion (solide → liquide), solidification (liquide → solide), vaporisation (liquide → gaz), liquéfaction (gaz → liquide), sublimation (solide → gaz), condensation solide (gaz → solide). Les candidats se sont souvent limités à ceux du schéma (Bordeaux)."), EAU),
        S('physique_chimie', "Sciences · le traitement de l'eau", Q(
            "Matières : caoutchouc 950 kg/m³, plomb 11 350, liège 240, sable 1 600, cuivre 8 920, essence 750. Lesquelles restent en surface du bac de décantation ?",
            ["Le caoutchouc, le liège et l'essence", "Le plomb, le sable et le cuivre", "Le liège seulement", "Toutes les matières"], "Le caoutchouc, le liège et l'essence",
            "Flottent les matières moins denses que l'eau (1 000 kg/m³) et non miscibles avec elle. Bordeaux relève que la miscibilité est rarement mobilisée."), EAU),
        S('physique_chimie', "Sciences · le traitement de l'eau", Q(
            "Quelle relation donne la masse volumique ρ d'un échantillon ?",
            ["ρ = m ÷ V (kg/m³)", "ρ = V ÷ m", "ρ = m × V", "ρ = m ÷ g"], "ρ = m ÷ V (kg/m³)",
            "Masse volumique = masse ÷ volume, avec m en kg et V en m³ (ou m en g et V en cm³). Dijon relève que la formule est souvent inconnue."), EAU),
        S('physique_chimie', "Sciences · le traitement de l'eau", Q(
            "Qu'est-ce qu'un mélange hétérogène ?",
            ["Un mélange dont on distingue à l'œil nu au moins deux constituants", "Un mélange d'une seule substance", "Un mélange transparent", "Un mélange de deux gaz"], "Un mélange dont on distingue à l'œil nu au moins deux constituants",
            "On peut en séparer les constituants par décantation, filtration, tamisage ou dégrillage. La distillation n'est pas une méthode réaliste en classe (Reims)."), EAU),
        S('svt', "Sciences · la qualité de l'eau", Q(
            "Des eaux usées riches en matière organique arrivent dans une rivière. Pourquoi le dioxygène dissous diminue-t-il ?",
            ["Les bactéries qui décomposent la matière organique se multiplient et respirent : elles consomment le dioxygène", "La matière organique produit du dioxygène", "L'eau se réchauffe à cause des bactéries", "Les poissons rejettent du dioxygène"],
            "Les bactéries qui décomposent la matière organique se multiplient et respirent : elles consomment le dioxygène",
            "La respiration consomme du dioxygène et rejette du dioxyde de carbone : C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O."), EAU),
        S('svt', 'Sciences · la classification du vivant', Q(
            "Sur quoi repose la classification scientifique des êtres vivants ?",
            ["Sur les attributs qu'ils possèdent en commun, en groupes emboîtés", "Sur ce qu'ils ne possèdent pas", "Sur leur milieu de vie", "Sur leur régime alimentaire"],
            "Sur les attributs qu'ils possèdent en commun, en groupes emboîtés",
            "On classe d'après des caractères observables que les êtres vivants possèdent, pas d'après ceux qui leur manquent. Cette question a été « très rarement réussie » (Dijon)."), EAU),
        S('svt', "Sciences · la démarche d'investigation", Q(
            "Des élèves pensent que le type de sol influe sur la transparence de l'eau qui ruisselle. Quel protocole permet de le tester ?",
            ["Des bacs identiques avec des sols différents, arrosés de la même façon, en ne changeant que le type de sol", "Un seul bac de terre arrosé plusieurs fois", "Des bacs de sols différents arrosés avec des quantités différentes", "Observer une rivière par temps de pluie"],
            "Des bacs identiques avec des sols différents, arrosés de la même façon, en ne changeant que le type de sol",
            "On ne fait varier qu'un paramètre à la fois. Sans témoin ni paramètre isolé, le protocole n'est pas recevable (Reims, Bordeaux)."), EAU),
        S('technologie', "Sciences · la distribution de l'eau", Q(
            "Quelles sont les deux fonctions principales d'un château d'eau ?",
            ["Stocker l'eau potable et la mettre sous pression pour alimenter le réseau", "Produire et chauffer l'eau", "Filtrer et dessaler l'eau", "Mesurer et facturer l'eau"],
            "Stocker l'eau potable et la mettre sous pression pour alimenter le réseau",
            "La mise sous pression, due à la hauteur du réservoir, a souvent été oubliée (Bordeaux)."), EAU),
        S('technologie', "Sciences · la distribution de l'eau", Q(
            "Récupérateur d'eau de pluie : un flotteur est relié par un fil, via une poulie, à un contrepoids. Quand le niveau d'eau monte, que fait le contrepoids ?",
            ["Il descend", "Il monte aussi", "Il reste immobile", "Il tourne sur lui-même"], "Il descend",
            "Le système est inversé : le flotteur monte, le contrepoids descend. C'est donc en bas de sa course qu'il faut placer le capteur pour détecter le niveau maximal (question « source de nombreuses difficultés », Dijon, Reims)."), EAU),
        S('technologie', "Sciences · la distribution de l'eau", Q(
            "Dans la maquette, quel élément est un capteur ?",
            ["Le capteur infrarouge qui détecte le contrepoids", "La LED", "La carte micro:bit", "Le contrepoids"], "Le capteur infrarouge qui détecte le contrepoids",
            "Le capteur acquiert l'information, la carte micro:bit la traite, la LED (actionneur) signale le niveau maximal."), EAU),
        # ── Histoire-géographie et EMC ──
        S('histoire_geographie', 'Géographie · les paysages de montagne', Q(
            "Quelle définition de la montagne convient à des élèves de CE2 ?",
            ["Un relief très élevé, aux pentes raides séparées par des vallées, où il fait plus froid en altitude et que les hommes aménagent", "Une grande colline en forme de triangle", "Un endroit où il y a toujours de la neige", "Un pic qui touche le ciel"],
            "Un relief très élevé, aux pentes raides séparées par des vallées, où il fait plus froid en altitude et que les hommes aménagent",
            "Au moins trois éléments de vocabulaire étaient attendus : relief, altitude, pente, climat, étagement (Dijon), sans oublier la montagne habitée et aménagée."), MONTAGNE),
        S('histoire_geographie', 'Géographie · les paysages de montagne', Q(
            "Comment appelle-t-on la succession des types de végétation selon l'altitude en montagne ?",
            ["L'étagement de la végétation", "L'érosion", "La transhumance", "Le versant"], "L'étagement de la végétation",
            "Feuillus, conifères, alpages, puis rochers et neiges : la végétation change avec l'altitude et le froid. Le sujet fournissait un schéma du massif du Mont-Blanc."), MONTAGNE),
        S('histoire_geographie', 'Géographie · les paysages de montagne', Q(
            "Comparer une carte postale de La Clusaz au début du XXe siècle et une photographie de 2025 permet de montrer :",
            ["Qu'un paysage se transforme : la neige, d'abord une contrainte, est devenue un atout touristique", "Que la montagne n'a pas changé en un siècle", "Que les stations de ski existaient déjà au Moyen Âge", "Que la montagne est un espace inhabité"],
            "Qu'un paysage se transforme : la neige, d'abord une contrainte, est devenue un atout touristique",
            "Le programme de cycle 2 demande de « comparer les paysages d'aujourd'hui et du passé pour mettre en évidence quelques transformations » (Dijon)."), MONTAGNE),
        S('emc', "EMC · le bien commun", Q(
            "Qu'est-ce que le bien commun ?",
            ["Ce qui appartient à tous et dont chacun profite, et dont chacun est responsable", "Un objet que l'on partage avec un ami", "L'argent de l'État", "Ce que chacun possède personnellement"],
            "Ce qui appartient à tous et dont chacun profite, et dont chacun est responsable",
            "L'air, l'eau, la montagne, mais aussi la cour de récréation ou la bibliothèque de l'école. Erreur relevée : le confondre avec l'intérêt général ou le développement durable (Reims, Limoges, Dijon)."), MONTAGNE),
        S('emc', 'EMC · le bien commun', Q(
            "Quelle limite le jury attendait-il dans l'analyse de l'affiche du Parc national des Écrins sur les gestes éco-responsables ?",
            ["Elle réduit la protection de l'environnement à de « petits gestes » individuels et reste éloignée du vécu de certains élèves", "Elle est trop simple pour des CE2", "Elle ne parle pas de la montagne", "Elle est en anglais"],
            "Elle réduit la protection de l'environnement à de « petits gestes » individuels et reste éloignée du vécu de certains élèves",
            "Une approche critique du document était attendue (Dijon) : utilisable, mais à accompagner d'une grille de lecture ou de situations proches des élèves."), MONTAGNE),
        # ── Arts ──
        S('arts', 'Arts plastiques · le dessin', Q(
            "Avec quel outil Giacometti a-t-il dessiné « D'après une sculpture égyptienne : statue de Rahotep » (1949) ?",
            ["Le stylo bille", "Le fusain", "L'aquarelle", "La sanguine"], "Le stylo bille",
            "Le sujet demandait une séance sur « l'incidence des outils et des supports » dans le dessin : Giacometti au stylo bille, Van Gogh à l'encre et au crayon, Alechinsky à l'encre de Chine et à l'aquarelle."),
          "Dossier d'arts plastiques (cycle 2) : trois dessins de Giacometti, Van Gogh et Alechinsky pour explorer « la représentation du monde »."),
        S('arts', 'Arts plastiques · le dessin', Q(
            "Lequel de ces éléments fait partie du « langage plastique » selon le programme d'arts plastiques ?",
            ["Le geste, le support et l'outil", "La mélodie et le rythme", "Le vocabulaire et la syntaxe", "La date et l'auteur"], "Le geste, le support et l'outil",
            "Le programme cite : forme, espace, lumière, couleur, matière, geste, support, outil, temps."),
          "Document 4 : programme d'arts plastiques du cycle 2 (2020), extraits."),
        S('arts', 'Éducation musicale · écouter, comparer', Q(
            "La séance d'écoute de « Beautiful Tango » d'Hindi Zahra vise à repérer un ostinato. Qu'est-ce qu'un ostinato ?",
            ["Un motif musical court répété avec obstination tout au long d'un passage", "Un changement brusque de tempo", "Un silence prolongé", "Un chant sans accompagnement"],
            "Un motif musical court répété avec obstination tout au long d'un passage",
            "De l'italien ostinato, « obstiné ». Repérer un ostinato développe l'écoute attentive, l'une des compétences « Écouter, comparer » du cycle 3."),
          "Dossier d'éducation musicale (cycle 3) : la fiche de préparation d'une séance d'écoute de « Beautiful Tango » d'Hindi Zahra, à analyser."),
        S('arts', 'Éducation musicale · écouter, comparer', Q(
            "La fiche de préparation fait écrire les élèves pendant la toute première écoute. Que peut-on lui reprocher ?",
            ["Les élèves écrivent pendant qu'ils découvrent l'œuvre, au lieu d'abord l'écouter attentivement", "La chanson est trop courte", "Il n'y a pas de fiche d'écoute", "La séance ne prévoit aucune écoute"],
            "Les élèves écrivent pendant qu'ils découvrent l'œuvre, au lieu d'abord l'écouter attentivement",
            "Les ressources Éduscol sur l'écoute recommandent une première écoute globale, sans consigne écrite, puis des écoutes ciblées. Le sujet demandait une analyse critique de la fiche."),
          "Document 2 : fiche de préparation d'une séance d'éducation musicale en CM1-CM2."),
    ]),
    # ── Ajout : questions complémentaires tirées du même sujet ──
    epreuve('Épreuve écrite disciplinaire de français', 20142, [
        S('francais', 'Étude de la langue · temps et modes', Q(
            "« Que ce cahier survive ou qu'il brûle, j'écrirai. » Temps et mode de « écrirai » ?",
            ["Futur simple de l'indicatif", "Conditionnel présent", "Passé simple", "Présent du subjonctif"], "Futur simple de l'indicatif",
            "Terminaison -ai sur le radical écrir- : futur. Le conditionnel serait « écrirais ». Reims relève des confusions entre futur et conditionnel."), MAALOUF),
        S('francais', 'Étude de la langue · nature et fonction', Q(
            "« … dont je noircis en cet instant, non sans volupté, la toute première page. » Fonction de « en cet instant » ?",
            ["Complément circonstanciel de temps", "COD du verbe noircir", "Complément du nom « page »", "Attribut du sujet"], "Complément circonstanciel de temps",
            "Groupe prépositionnel déplaçable et supprimable, qui situe l'action dans le temps. Il faut préciser « de temps » (Nantes)."), MAALOUF),
        S('francais', 'Étude de la langue · propositions', Q(
            "« Le premier cahier, qui racontait le commencement de mon périple, s'est perdu… » Nature de « qui racontait le commencement de mon périple » ?",
            ["Subordonnée relative", "Subordonnée complétive", "Subordonnée circonstancielle de cause", "Proposition indépendante"], "Subordonnée relative",
            "Introduite par le pronom relatif « qui », elle complète l'antécédent « le premier cahier ». « Proposition relative » sans « subordonnée » a été relevé comme imprécis (Nantes)."), MAALOUF),
        S('francais', 'Étude de la langue · accords', Q(
            "« … de vieux livres pourrissants. » Pourquoi « pourrissants » s'accorde-t-il ?",
            ["C'est un adjectif verbal, qui s'accorde comme un adjectif", "C'est un participe présent, toujours variable", "C'est un gérondif", "Il s'accorde avec le sujet du verbe"], "C'est un adjectif verbal, qui s'accorde comme un adjectif",
            "Le participe présent (action, invariable) se distingue de l'adjectif verbal (qualité, variable). Ici, « pourrissants » décrit l'état des livres."), MAALOUF),
        S('francais', 'Lexique · sens en contexte', Q(
            "Que désigne « mortel oublieux de la mort » ?",
            ["L'homme qui se sait mortel mais agit et crée comme s'il était immortel", "Un livre oublié", "Un soldat mort", "Un médecin"], "L'homme qui se sait mortel mais agit et crée comme s'il était immortel",
            "C'est une alliance de mots, un paradoxe. L'expression a souvent été rattachée à tort au carnet ou aux livres (Dijon, Nantes, Limoges)."), MAALOUF),
        S('francais', 'Lexique · figures de style', Q(
            "Comment s'appelle la figure de « non sans volupté », qui dit moins pour suggérer plus ?",
            ["Une litote", "Une hyperbole", "Une métaphore", "Une antithèse"], "Une litote",
            "La double négation atténue l'expression pour mieux suggérer un vif plaisir. Nommer la litote a été valorisé, à condition de l'expliquer (Dijon)."), MAALOUF),
        S('francais', 'Lexique · familles de mots', Q(
            "Quelle est la différence entre une famille de mots et un champ lexical ?",
            ["Une famille partage un même radical ; un champ lexical réunit des mots d'un même thème", "Ce sont deux synonymes", "Un champ lexical partage un même radical", "Une famille réunit des mots de même nature"],
            "Une famille partage un même radical ; un champ lexical réunit des mots d'un même thème",
            "Erreur relevée : donner des synonymes (« colère » pour « furie ») au lieu de mots de la famille (Bordeaux, Créteil, Limoges). C'est une notion enseignée dès le cycle 2."), None),
        S('francais', 'Réflexion · écrire sa vie', Q(
            "Le sujet de réflexion portait sur l'intérêt de mettre par écrit ses expériences vécues. Laquelle de ces œuvres relève de l'écriture de soi ?",
            ["Les Confessions de Rousseau", "Les Misérables de Hugo", "L'Odyssée d'Homère", "Les Fables de La Fontaine"], "Les Confessions de Rousseau",
            "Autres références proposées : Sarraute (Enfance), Sartre (Les Mots), le Journal d'Anne Frank, Primo Levi. Reims a jugé L'Odyssée et Les Misérables non pertinents."), None),
    ]),
    epreuve('Épreuve écrite disciplinaire de mathématiques', 20154, [
        S('mathematiques', 'Exercice 1 · tableur', Q(
            "Quelle formule saisir en D8 pour additionner les montants de D2 à D7 ?",
            ["=SOMME(D2:D7)", "=D2+D7", "SOMME(D2;D7)", "=SOMME(D2-D7)"], "=SOMME(D2:D7)",
            "Le deux-points désigne une plage de cellules ; le point-virgule séparerait deux cellules seulement (D2 et D7)."), MUSEE),
        S('mathematiques', 'Exercice 1 · coût du transport', N(
            "Aller-retour de 170 km, consommation 30 L/100 km, gazole à 1,60 €/L, péage 13,90 € par trajet, forfait de 150 €. Coût total, en euros ?", 259.4,
            "Carburant : 51 L × 1,60 = 81,60 €. Péages : 2 × 13,90 = 27,80 €. Total : 81,60 + 27,80 + 150 = 259,40 €."), None),
        S('mathematiques', 'Exercice 1 · conversions', Q(
            "Combien vaut 1 h 10 min en heures ?",
            ["7/6 h (environ 1,17 h)", "1,10 h", "1,1 h", "1,6 h"], "7/6 h (environ 1,17 h)",
            "10 min = 10/60 h = 1/6 h. Écrire 1,10 h est une erreur classique : les durées ne sont pas décimales."), None),
        S('mathematiques', 'Exercice 2 · moyenne', N(
            "51 élèves ont vendu 500 tickets. Combien de tickets un élève a-t-il vendus en moyenne, arrondi à l'unité ?", 10,
            "500 ÷ 51 ≈ 9,8, soit environ 10 tickets."), None),
        S('mathematiques', 'Exercice 2 · médiane', Q(
            "La médiane du nombre de tickets vendus est 10. Comment l'interpréter ?",
            ["Au moins la moitié des élèves ont vendu 10 tickets ou moins, et au moins la moitié 10 ou plus", "Tous les élèves ont vendu 10 tickets", "La moyenne est 10", "10 élèves ont vendu des tickets"],
            "Au moins la moitié des élèves ont vendu 10 tickets ou moins, et au moins la moitié 10 ou plus",
            "L'interprétation de la médiane n'est réussie que par 25 % des candidats à Nantes : il faut employer « au moins la moitié »."), None),
        S('mathematiques', 'Exercice 3 · Thalès', N(
            "Avec (BC) // (DE), BC = 60 m et AD/AC = 0,6, combien mesure DE, en m ?", 36,
            "DE = 0,6 × 60 = 36 m. Créteil relève que les triangles sont dans le rapport 5/12/13, un triplet pythagoricien."), CROSS),
        S('mathematiques', 'Exercice 3 · volumes', N(
            "Le socle d'un plot est un pavé de 24,5 cm × 24,5 cm × 3,5 cm. Quel est son volume, en cm³, arrondi à l'unité ?", 2101,
            "24,5 × 24,5 × 3,5 ≈ 2 100,9 cm³, soit environ 2 101 cm³.", tol=1), None),
        S('mathematiques', 'Exercice 4 · vrai ou faux', Q(
            "Affirmation : « Pour tout réel x, 24x² − 9 = (3x + 1)(8x − 5) − (−7x + 4). » Vrai ou faux ?",
            ["Vrai", "Faux"], "Vrai",
            "(3x + 1)(8x − 5) = 24x² − 15x + 8x − 5 = 24x² − 7x − 5. On retire (−7x + 4) : 24x² − 7x − 5 + 7x − 4 = 24x² − 9."), None),
        S('mathematiques', 'Exercice 5 · Scratch', N(
            "Pour dessiner avec Scratch un angle de 30° dans un parallélogramme, de combien de degrés le lutin doit-il tourner ?", 150,
            "Le lutin tourne de 180° − α. Pour un angle de 30°, il tourne de 150° ; pour un angle de 150°, de 30° (Créteil)."), None),
    ]),
    epreuve("Épreuve écrite d'application (sciences, histoire-géographie-EMC ou arts)", 20166, [
        S('svt', "Sciences · la démarche d'investigation", Q(
            "Quelles étapes manquent souvent dans une séquence pour travailler la démarche d'investigation ?",
            ["La formulation d'un problème, l'émission d'hypothèses et la confrontation des résultats aux hypothèses", "La copie de la leçon", "La dictée de vocabulaire", "La lecture d'un manuel"],
            "La formulation d'un problème, l'émission d'hypothèses et la confrontation des résultats aux hypothèses",
            "C'était la réponse attendue à la question 2 (Bordeaux), sur la séquence de CM1 « l'eau dans tous ses états »."), EAU),
        S('physique_chimie', "Sciences · obstacle didactique", Q(
            "Pourquoi le passage de l'eau liquide à l'état gazeux est-il un obstacle pour les élèves de cycle 2 ?",
            ["La vapeur d'eau est invisible : l'élève voit l'eau « disparaître » et la confond avec la buée ou le brouillard", "Les élèves ne savent pas ce qu'est l'eau", "L'expérience est trop dangereuse", "L'eau ne s'évapore pas en classe"],
            "La vapeur d'eau est invisible : l'élève voit l'eau « disparaître » et la confond avec la buée ou le brouillard",
            "Buée, brouillard et nuages sont des gouttelettes d'eau liquide. Le passage à l'état gazeux demande une abstraction difficile au cycle 2 (Bordeaux)."), EAU),
        S('svt', "Sciences · le développement des êtres vivants", Q(
            "Quelle question permet de lancer l'élevage de larves prélevées dans une rivière ?",
            ["« Les petits vers rouges trouvés dans la rivière deviennent-ils des adultes qui leur ressemblent ? »", "« Combien pèse une rivière ? »", "« Pourquoi l'eau est-elle mouillée ? »", "« Quelle est la couleur préférée des larves ? »"],
            "« Les petits vers rouges trouvés dans la rivière deviennent-ils des adultes qui leur ressemblent ? »",
            "Un élevage permet d'observer le développement et la métamorphose : c'est une question qui se vérifie par l'observation (Bordeaux)."), EAU),
        S('physique_chimie', "Sciences · séparer les constituants", Q(
            "Pour rendre limpide une eau trouble, quelles propositions d'élèves sont des techniques de séparation ?",
            ["Le filtre à café (filtration), l'éponge (rétention) et laisser reposer (décantation)", "Ajouter du savon", "Mélanger plus fort", "Ajouter du sucre"],
            "Le filtre à café (filtration), l'éponge (rétention) et laisser reposer (décantation)",
            "Ajouter du savon ne sépare rien. Le faire tester par l'élève lui-même fait émerger l'erreur sans le disqualifier (Bordeaux)."), EAU),
        S('physique_chimie', "Sciences · séparer les constituants", Q(
            "Pourquoi la distillation n'est-elle pas une méthode adaptée ici ?",
            ["Ce n'est réaliste ni en classe ni pour l'épuration de l'eau d'une ville", "Elle ne sépare rien", "Elle est interdite par la loi", "Elle ne fonctionne qu'avec du sel"],
            "Ce n'est réaliste ni en classe ni pour l'épuration de l'eau d'une ville",
            "Reims relève aussi des confusions entre distillation, vaporisation et évaporation."), EAU),
        S('technologie', "Sciences · la distribution de l'eau", Q(
            "Un algorigramme doit gérer un château d'eau quand le niveau est très bas. Que doit-il faire ?",
            ["Allumer le voyant rouge et mettre en marche la motopompe auxiliaire, puis tout arrêter quand le niveau redevient suffisant", "Éteindre toutes les pompes", "Vider le réservoir", "Allumer seulement le voyant"],
            "Allumer le voyant rouge et mettre en marche la motopompe auxiliaire, puis tout arrêter quand le niveau redevient suffisant",
            "La justification doit aussi dire pourquoi l'autre algorigramme est faux (Bordeaux)."), EAU),
        S('technologie', "Sciences · réaliser un objet technique", Q(
            "Quelle compétence du cycle 3 travaillent des élèves qui fabriquent et testent un récupérateur d'eau de pluie ?",
            ["Réaliser une maquette ou un prototype pour matérialiser une solution, puis la tester pour la valider", "Lire une carte de géographie", "Calculer une moyenne", "Apprendre une poésie"],
            "Réaliser une maquette ou un prototype pour matérialiser une solution, puis la tester pour la valider",
            "C'était la réponse attendue à la question 22 (Bordeaux). Les notions de fonction et de solution technique « ne sont pas maîtrisées » par beaucoup de candidats (Reims)."), EAU),
        S('technologie', "Sciences · réaliser un objet technique", Q(
            "Lequel de ces savoirs est un prérequis pour comprendre le récupérateur à flotteur et contrepoids ?",
            ["Savoir pourquoi un objet flotte", "Connaître les capitales européennes", "Savoir conjuguer au passé simple", "Connaître les tables de 9"], "Savoir pourquoi un objet flotte",
            "Autres prérequis : le principe du contrepoids, le rôle d'un capteur et d'un actionneur, la programmation de la micro:bit. Reims relève que les candidats confondent prérequis et consignes de sécurité."), EAU),
        S('histoire_geographie', 'Géographie · les paysages de montagne', Q(
            "Que montrent les dessins d'élèves de la montagne (document 10) ?",
            ["Des représentations stéréotypées : sommets pointus et enneigés, sapins, montagne inhabitée", "Des représentations scientifiques exactes", "Des cartes topographiques", "Des stations de ski détaillées"],
            "Des représentations stéréotypées : sommets pointus et enneigés, sapins, montagne inhabitée",
            "Ils servent d'évaluation diagnostique : on part de cet archétype pour aller vers une montagne habitée et aménagée (Dijon). La consigne était de dessiner « un beau paysage » (Limoges)."), MONTAGNE),
        S('histoire_geographie', 'Géographie · les paysages de montagne', Q(
            "Comment appelle-t-on les pentes d'une montagne, de part et d'autre d'une vallée ?",
            ["Les versants", "Les plaines", "Les plateaux", "Les deltas"], "Les versants",
            "Sommet, versant, vallée, altitude : le vocabulaire attendu pour décrire un paysage de montagne au CE2."), MONTAGNE),
        S('histoire_geographie', 'Géographie · les paysages de montagne', Q(
            "Quelle est la différence entre la météo et le climat, confondus par certains candidats ?",
            ["La météo est le temps qu'il fait à un moment ; le climat, les conditions moyennes sur une longue période", "Ce sont des synonymes", "Le climat change chaque jour", "La météo décrit 30 ans de données"],
            "La météo est le temps qu'il fait à un moment ; le climat, les conditions moyennes sur une longue période",
            "Dijon, Limoges et Nantes relèvent la confusion entre météo et climat, et entre montagne et relief."), None),
        S('histoire_geographie', 'Géographie · les paysages de montagne', Q(
            "Quelle démarche convient pour une séquence sur les paysages de montagne au CE2 ?",
            ["Recueillir les représentations, décrire une photographie, localiser les massifs sur une carte, comparer des paysages d'hier et d'aujourd'hui", "Faire recopier une définition", "Lire un texte scientifique d'adulte", "Dessiner une montagne sans document"],
            "Recueillir les représentations, décrire une photographie, localiser les massifs sur une carte, comparer des paysages d'hier et d'aujourd'hui",
            "La carte en relief (document 3) a presque jamais été utilisée et la localisation des massifs rarement travaillée (Nantes, Dijon)."), MONTAGNE),
        S('emc', 'EMC · le bien commun', Q(
            "Lequel de ces exemples est un bien commun à l'échelle de l'école ?",
            ["La cour de récréation et les livres de la bibliothèque", "Le cartable d'un élève", "Le goûter d'un camarade", "La trousse de l'enseignant"], "La cour de récréation et les livres de la bibliothèque",
            "Ce qui appartient à tous et dont chacun profite : chacun en est responsable, pour soi et pour les autres."), MONTAGNE),
        S('emc', 'EMC · le bien commun', Q(
            "Le programme d'EMC de 2024 parle de construire une « culture de l'engagement ». Qu'est-ce que cela signifie au CE2 ?",
            ["Agir concrètement pour la classe et l'école : prendre des responsabilités, participer à un projet collectif", "Apprendre la liste des ministres", "S'inscrire à un parti politique", "Voter aux élections"],
            "Agir concrètement pour la classe et l'école : prendre des responsabilités, participer à un projet collectif",
            "Le jury valorisait les situations où l'intérêt particulier entre en tension avec l'intérêt général (Dijon)."), None),
        S('emc', 'EMC · le bien commun', Q(
            "Qu'est-ce qui distingue un vrai débat réglé d'un simple échange d'opinions ?",
            ["Un cadre (règles de parole, rôles), une question précise et un objectif d'apprentissage", "Le fait que tout le monde parle en même temps", "L'absence de l'enseignant", "Le vote final obligatoire"],
            "Un cadre (règles de parole, rôles), une question précise et un objectif d'apprentissage",
            "Reims relève des « débats » sans cadre ni objectif, qui ne sont que des échanges d'opinions."), None),
        S('arts', 'Arts plastiques · le dessin', Q(
            "Vincent Van Gogh a dessiné « Bateaux de pêche aux Saintes-Maries-de-la-Mer » (1888) avec :",
            ["De l'encre et du crayon sur papier", "Du stylo bille", "De la peinture acrylique", "Des pastels gras"], "De l'encre et du crayon sur papier",
            "Chaque outil (stylo bille, plume, encre, crayon) produit des traits différents : c'est l'« incidence des outils » à faire expérimenter."), None),
        S('arts', 'Arts plastiques · le dessin', Q(
            "Selon le programme de cycle 2, quelle compétence travaille une séance sur les outils du dessin ?",
            ["Observer les effets produits par ses gestes et par les outils utilisés", "Reproduire exactement une œuvre", "Apprendre une technique unique imposée", "Colorier sans dépasser"],
            "Observer les effets produits par ses gestes et par les outils utilisés",
            "C'est une compétence de « Expérimenter, produire, créer » citée dans le document 4 du dossier."), None),
        S('arts', 'Éducation musicale · écouter, comparer', Q(
            "Que demande la compétence « Échanger, partager et argumenter » en éducation musicale au cycle 3 ?",
            ["Exprimer ses goûts et ses émotions en les justifiant, et écouter ceux des autres", "Chanter seul devant la classe", "Recopier les paroles", "Jouer d'un instrument"],
            "Exprimer ses goûts et ses émotions en les justifiant, et écouter ceux des autres",
            "La fiche analysée visait à « exprimer son ressenti tout en respectant celui des autres » avec un vocabulaire adapté."), None),
    ]),
]
