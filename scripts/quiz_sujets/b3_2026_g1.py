# Bac+3, session 2026, groupement 1
from slib import S, Q, N, C, epreuve

ZOLA = "Texte : Émile Zola, Au Bonheur des Dames (1883). Le grand magasin de Mouret s'agrandit ; la boutique de l'oncle Baudu, le Vieil Elbeuf, dépérit."
EX1 = "Exercice 1 : dans une école de 300 élèves, 40 % pratiquent un sport, 75 pratiquent un instrument de musique, et parmi ceux qui pratiquent un instrument, 60 % pratiquent aussi un sport."
EX2 = "Exercice 2 : un motif évolutif compte 1 carreau à l'étape 1, 4 à l'étape 2, 7 à l'étape 3 et 10 à l'étape 4."
EX3 = "Exercice 3 : ABCDE est un pentagone régulier de centre O, inscrit dans un cercle de centre O."
EX5 = "Exercice 5 : sur un axe gradué d'origine O, le point U a pour abscisse 1. L'unité est partagée en 8 graduations égales ; A est sur la 4e graduation et B sur la 11e."
ISS = "Sujet de sciences : les scientifiques à bord de la Station spatiale internationale (ISS)."
SCOOBY = ("Text: “How therapy dog Scooby has left pupils animated”, BBC News NI, 27 October 2025. Scooby the labradoodle is the newest member of staff "
          "at Mount St Catherine's, an Armagh primary school. It is one of only seven mainstream schools in Northern Ireland with a therapy dog. "
          "About 60 of the 160 pupils have Special Educational Needs (SEN) while 93 are newcomer pupils.")

QUESTIONS = [
    epreuve('Première épreuve écrite (français et mathématiques)', 20277, [
        # ── Français : étude de la langue et lexique ──
        S('francais', 'Étude de la langue · temps et modes', C(
            "Cliquez sur le verbe conjugué au plus-que-parfait de l'indicatif.",
            "Mouret, disait-on, [avait traité] avec le baron Hartmann, et il occuperait tout le pâté de maisons.",
            "« Avait traité » associe l'auxiliaire avoir à l'imparfait et le participe passé : c'est un plus-que-parfait. Erreur fréquente relevée par les jurys : le confondre avec un passé composé."), ZOLA),
        S('francais', 'Étude de la langue · temps et modes', Q(
            "« Il occuperait tout le pâté de maisons. » À quel temps est conjugué le verbe « occuperait » ?",
            ["Conditionnel présent", "Futur simple", "Imparfait", "Subjonctif présent"], "Conditionnel présent",
            "Terminaison -rait : conditionnel présent, que la terminologie actuelle range parmi les temps de l'indicatif (futur dans le passé). C'est l'erreur la plus fréquente de la question selon Bordeaux."), ZOLA),
        S('francais', 'Étude de la langue · temps et modes', Q(
            "« … où le baron voulait construire une concurrence au Grand-Hôtel. » Temps et mode de « voulait » ?",
            ["Imparfait de l'indicatif", "Passé simple de l'indicatif", "Conditionnel présent", "Plus-que-parfait de l'indicatif"], "Imparfait de l'indicatif",
            "Terminaison -ait sur le radical voul- : imparfait de l'indicatif. Pensez à toujours donner le mode avec le temps."), ZOLA),
        S('francais', 'Étude de la langue · réécriture', Q(
            "Réécriture avec le sujet au pluriel : « Seule, au milieu de ce bouleversement, l'étroite masure du vieux Bourras restait immobile et intacte, obstinément accrochée entre les autres murailles, couvertes de maçons. » Quelle version est correcte ?",
            ["Seules, au milieu de ce bouleversement, les étroites masures du vieux Bourras restaient immobiles et intactes, obstinément accrochées entre les autres murailles, couvertes de maçons.",
             "Seule, au milieu de ce bouleversement, les étroites masures du vieux Bourras restaient immobiles et intactes, obstinément accrochées entre les autres murailles, couvertes de maçons.",
             "Seules, au milieu de ce bouleversement, les étroites masures du vieux Bourras restaient immobile et intacte, obstinément accrochées entre les autres murailles, couvertes de maçons.",
             "Seules, au milieu de ces bouleversements, les étroites masures des vieux Bourras restaient immobiles et intactes, obstinément accrochées entre les autres murailles, couvertes de maçons."],
            "Seules, au milieu de ce bouleversement, les étroites masures du vieux Bourras restaient immobiles et intactes, obstinément accrochées entre les autres murailles, couvertes de maçons.",
            "Seul le sujet et ce qui s'accorde avec lui changent : Seules, étroites masures, restaient, immobiles, intactes, accrochées. « Seule » en tête de phrase est le piège le plus relevé (Reims, Limoges). « Ce bouleversement » et « le vieux Bourras » ne bougent pas."), ZOLA),
        S('francais', 'Étude de la langue · nature et fonction', Q(
            "« Elle la revoyait assombrie. » Nature et fonction de « la » ?",
            ["Pronom personnel, COD du verbe revoir", "Article défini, déterminant du nom", "Pronom personnel, COI du verbe revoir", "Pronom relatif, sujet"], "Pronom personnel, COD du verbe revoir",
            "« La » remplace « la boutique » : on revoit quelque chose, sans préposition, donc COD. C'est l'élément le plus échoué de la question (Reims, Versailles, Limoges)."), ZOLA),
        S('francais', 'Étude de la langue · nature et fonction', Q(
            "« Elle la revoyait assombrie, gagnée davantage par la somnolence de la ruine. » Quelle est la fonction de « par la somnolence » ?",
            ["Complément d'agent du participe passif « gagnée »", "Complément circonstanciel de manière", "COI du verbe revoir", "Complément du nom « ruine »"], "Complément d'agent du participe passif « gagnée »",
            "À la voix active : « la somnolence gagnait la boutique ». Le groupe introduit par « par » désigne celui qui fait l'action : complément d'agent. Il a été « très rarement » identifié (Versailles, Bordeaux, Reims)."), ZOLA),
        S('francais', 'Étude de la langue · nature et fonction', Q(
            "« Dans la boutique, Denise éprouva le même serrement de cœur. » Nature et fonction de « Dans la boutique » ?",
            ["Groupe nominal prépositionnel, complément circonstanciel de lieu", "Groupe nominal, COD du verbe éprouver", "Groupe nominal prépositionnel, complément du nom", "Adverbe, complément circonstanciel de lieu"],
            "Groupe nominal prépositionnel, complément circonstanciel de lieu",
            "Le groupe est introduit par une préposition, peut être déplacé ou supprimé : complément circonstanciel (ou complément de phrase), de lieu par son sens."), ZOLA),
        S('francais', 'Étude de la langue · propositions', N(
            "« Lorsque, le lendemain, Denise se rendit avec Pépé chez l'oncle Baudu, la rue était justement barrée par une file de tombereaux, qui déchargeaient des briques devant l'ancien hôtel Duvillard. » Combien de propositions compte cette phrase ?",
            3, "Une proposition par verbe conjugué : se rendit, était barrée, déchargeaient. Donc trois propositions : une subordonnée circonstancielle de temps, une principale, une subordonnée relative."), ZOLA),
        S('francais', 'Étude de la langue · propositions', Q(
            "Dans la même phrase, quelle est la nature de « Lorsque, le lendemain, Denise se rendit avec Pépé chez l'oncle Baudu » ?",
            ["Subordonnée conjonctive circonstancielle de temps", "Subordonnée relative", "Subordonnée complétive", "Proposition principale"], "Subordonnée conjonctive circonstancielle de temps",
            "Elle est introduite par la conjonction de subordination « lorsque » et indique le moment. Erreur relevée : la confondre avec une complétive (Reims, Limoges)."), ZOLA),
        S('francais', 'Étude de la langue · propositions', Q(
            "Quelle est la nature de « qui déchargeaient des briques devant l'ancien hôtel Duvillard » ?",
            ["Subordonnée relative", "Subordonnée conjonctive circonstancielle", "Proposition indépendante", "Subordonnée interrogative indirecte"], "Subordonnée relative",
            "Elle est introduite par le pronom relatif « qui », dont l'antécédent est « tombereaux »."), ZOLA),
        S('francais', 'Lexique · formation des mots', Q(
            "Comment est formé le mot « immobile » (ligne 15) ?",
            ["Par dérivation : préfixe privatif in- (im-) + base mobile", "Par composition de deux mots", "Par dérivation : base immo- + suffixe -bile", "C'est un mot simple, non construit"],
            "Par dérivation : préfixe privatif in- (im-) + base mobile",
            "Le préfixe in- s'écrit im- devant m, b, p. Valeur privative : « qui n'est pas mobile ». Nommer le procédé (« dérivation ») distingue les meilleures copies (Reims)."), ZOLA),
        S('francais', 'Lexique · formation des mots', Q(
            "Quel mot est formé avec le même préfixe que « immobile » ?",
            ["Impossible", "Immobilier", "Important", "Mobilité"], "Impossible",
            "Impossible = im- (privatif) + possible. Immobilier et mobilité sont de la famille de mobile, pas des mots formés avec le préfixe : c'est l'erreur relevée par Reims, Versailles et Limoges. « Important » ne contient pas de préfixe privatif."), ZOLA),
        S('francais', 'Lexique · figures de style', Q(
            "« Une détresse tombait de la façade entière. » Quelle figure de style est employée ?",
            ["Une métaphore (personnification) : la façade est vue comme un visage triste", "Une comparaison introduite par « comme »", "Une hyperbole", "Une antithèse"],
            "Une métaphore (personnification) : la façade est vue comme un visage triste",
            "La façade ne souffre pas réellement : son aspect sombre et délabré donne une impression de misère. Le corrigé de Bordeaux accepte métaphore, personnification ou métonymie."), ZOLA),
        # ── Mathématiques ──
        S('mathematiques', 'Exercice 1 · tableau et probabilités', N(
            "Combien d'élèves pratiquent à la fois un sport et un instrument de musique ?", 45,
            "60 % des 75 musiciens : 0,6 × 75 = 45 élèves."), EX1),
        S('mathematiques', 'Exercice 1 · tableau et probabilités', N(
            "On choisit un élève au hasard. Quelle est la probabilité qu'il pratique au moins l'une des deux activités ? (Réponse décimale ou fraction.)", 0.5,
            "Sportifs : 40 % de 300 = 120. Au moins une activité : 120 + 75 − 45 = 150 élèves, soit 150/300 = 1/2. L'erreur relevée : compter deux fois les 45 élèves qui font les deux (120 + 75)."), EX1),
        S('mathematiques', 'Exercice 1 · tableau et probabilités', Q(
            "On choisit au hasard un élève qui pratique un sport. Quelle est la probabilité qu'il pratique aussi un instrument ?",
            ["3/8", "3/20", "3/5", "45/300"], "3/8",
            "On se restreint aux 120 sportifs : 45/120 = 3/8 (fraction irréductible). 3/5 serait la proportion de sportifs parmi les musiciens, l'inverse de la question."), EX1),
        S('mathematiques', 'Exercice 2 · motif évolutif', N(
            "Combien de carreaux le motif compte-t-il à l'étape 20 ?", 58,
            "On ajoute 3 carreaux à chaque étape : 1 + 19 × 3 = 58. Vérification avec la formule 3n − 2 : 3 × 20 − 2 = 58."), EX2),
        S('mathematiques', 'Exercice 2 · motif évolutif', Q(
            "Quelle expression donne le nombre de carreaux à l'étape n ?",
            ["3n − 2", "3n + 1", "n + 3", "4n − 3"], "3n − 2",
            "Étape 1 : 3 − 2 = 1 ; étape 4 : 12 − 2 = 10. Testez toujours la formule sur les étapes connues (conseil de Versailles)."), EX2),
        S('mathematiques', 'Exercice 2 · motif évolutif', Q(
            "Dans un tableur, les étapes sont en colonne A et les nombres de carreaux en colonne B (B2 contient 1). Quelle formule entrer en B3, à étirer vers le bas ?",
            ["=B2+3", "B2+3", "=B3+3", "=A2+3"], "=B2+3",
            "Chaque nombre vaut le précédent plus 3 : =B2+3. « =3*A3-2 » convient aussi. Erreurs relevées : signe « = » oublié, mauvaise référence de cellule (Bordeaux, Versailles, Nantes, Reims)."), EX2),
        S('mathematiques', 'Exercice 2 · motif évolutif', N(
            "À quelle étape le motif compte-t-il exactement 100 carreaux ?", 34,
            "3n − 2 = 100 donne 3n = 102, n = 34. Pour 2 000 carreaux, n = 2 002/3 n'est pas entier : aucune étape ne convient."), EX2),
        S('mathematiques', 'Exercice 3 · pentagones', N(
            "Combien mesure l'angle au centre DOC, en degrés ?", 72,
            "Les cinq côtés sont égaux, donc les cinq angles au centre aussi : 360° ÷ 5 = 72°."), EX3),
        S('mathematiques', 'Exercice 3 · pentagones', Q(
            "Quelle est la nature du triangle OCD ?",
            ["Isocèle en O", "Équilatéral", "Rectangle en O", "Quelconque"], "Isocèle en O",
            "OC = OD, car ce sont deux rayons du cercle. Erreur relevée : le confondre avec un triangle équilatéral (Bordeaux, Reims, Versailles) ; l'angle en O vaut 72°, pas 60°."), EX3),
        S('mathematiques', 'Exercice 3 · pentagones', N(
            "Combien mesure l'angle DCB du pentagone régulier, en degrés ?", 108,
            "Angles à la base du triangle OCD : (180° − 72°) ÷ 2 = 54°. L'angle DCB vaut 54° + 54° = 108°. La somme des angles du pentagone est donc 5 × 108° = 540°."), EX3),
        S('mathematiques', 'Exercice 3 · pentagones', Q(
            "Dans le pentagone JKLMN, JK = KL = 10 cm et l'angle JKL est droit. Quelle est la nature du triangle JKL, et combien mesure JL ?",
            ["Rectangle isocèle en K ; JL = √200 cm", "Rectangle en K ; JL = 20 cm", "Équilatéral ; JL = 10 cm", "Isocèle en J ; JL = √100 cm"], "Rectangle isocèle en K ; JL = √200 cm",
            "Deux côtés égaux et un angle droit en K : rectangle isocèle en K. Pythagore : JL² = 10² + 10² = 200, donc JL = √200 cm. Les jurys attendaient la nature complète avec le sommet."), None),
        S('mathematiques', 'Exercice 4 · vrai ou faux', N(
            "X s'écrit avec quatre chiffres tous différents de 0 ; son nombre de dizaines est 12 et le chiffre de ses unités est le triple du chiffre de ses dixièmes. Combien de valeurs X peut-il prendre ?", 3,
            "X s'écrit 12u,d avec u = 3d et d non nul : 123,1 ; 126,2 ; 129,3. Trois valeurs : l'affirmation « exactement deux valeurs » est fausse."), None),
        S('mathematiques', 'Exercice 4 · vrai ou faux', Q(
            "Affirmation : « Si un entier est à la fois multiple de 4 et de 10, il est nécessairement multiple de 40. » Vrai ou faux ?",
            ["Faux : 20 est un contre-exemple", "Vrai : 4 × 10 = 40", "Vrai : on le vérifie avec 40 et 80", "Faux : aucun multiple de 4 n'est multiple de 10"], "Faux : 20 est un contre-exemple",
            "20 est multiple de 4 et de 10 mais pas de 40. Un seul contre-exemple suffit pour dire « faux » ; des exemples ne prouvent jamais qu'une affirmation est vraie."), None),
        S('mathematiques', 'Exercice 4 · vrai ou faux', Q(
            "Offre 1 : le deuxième produit à −50 %. Offre 2 : 50 % de produit en plus offert. Laquelle est la plus avantageuse ?",
            ["L'offre 2", "L'offre 1", "Elles sont équivalentes", "On ne peut pas comparer"], "L'offre 2",
            "Offre 1 : 2 produits pour 1,5 prix, soit 0,75 prix par produit. Offre 2 : 1,5 produit pour 1 prix, soit environ 0,67 prix par produit. Ramenez-vous toujours au prix d'un produit."), None),
        S('mathematiques', 'Exercice 4 · vrai ou faux', Q(
            "Affirmation : « Le quotient d'un nombre décimal par 4 est un nombre décimal. » Vrai ou faux ?",
            ["Vrai", "Faux"], "Vrai",
            "Un décimal s'écrit a/10ⁿ (a entier). Son quotient par 4 vaut a/(4 × 10ⁿ) = 25a/10ⁿ⁺², encore décimal. Créteil le rappelle : une collection d'exemples « n'a aucune valeur logique »."), None),
        S('mathematiques', 'Exercice 5 · axe gradué', N(
            "Quelle est l'abscisse b du point B ? (Réponse décimale ou fraction.)", 1.375,
            "Une graduation vaut 1/8 ; B est sur la 11e : b = 11/8 = 1,375. De même a = 4/8 = 1/2."), EX5),
        S('mathematiques', 'Exercice 5 · axe gradué', N(
            "Quelle est l'abscisse du milieu du segment [OB] ? (Réponse décimale ou fraction.)", 0.6875,
            "Milieu de [OB] : b/2 = 11/16 = 0,6875."), EX5),
        S('mathematiques', 'Exercice 5 · axe gradué', Q(
            "Le point D d'abscisse 4/3 appartient-il au segment [AB], avec a = 1/2 et b = 11/8 ?",
            ["Oui : 12/24 < 32/24 < 33/24", "Non : 4/3 est plus grand que 11/8", "Non : 4/3 n'est pas un nombre décimal", "Oui, car 4/3 > 1"], "Oui : 12/24 < 32/24 < 33/24",
            "Au même dénominateur 24 : 1/2 = 12/24, 4/3 = 32/24, 11/8 = 33/24. Comparer seulement à 1 ne permet pas de conclure (Versailles)."), EX5),
    ]),
    epreuve('Seconde épreuve écrite (domaines au choix)', 20268, [
        # ── Histoire-géographie ──
        S('histoire_geographie', 'Histoire · le régime de Vichy', Q(
            "À quelle date l'Assemblée nationale vote-t-elle les pleins pouvoirs au maréchal Pétain ?",
            ["10 juillet 1940", "22 juin 1940", "18 juin 1940", "11 novembre 1942"], "10 juillet 1940",
            "Après l'armistice du 22 juin 1940, les parlementaires réunis à Vichy votent les pleins pouvoirs le 10 juillet : l'« État français » remplace la IIIe République. Les jurys ont relevé de nombreuses erreurs de chronologie."),
          "Question du sujet : « Quelles sont les caractéristiques du régime de Vichy ? »"),
        S('histoire_geographie', 'Histoire · le régime de Vichy', Q(
            "Quelle devise remplace « Liberté, Égalité, Fraternité » sous le régime de Vichy ?",
            ["Travail, Famille, Patrie", "Honneur et Patrie", "Ordre et Progrès", "Un peuple, un empire, un chef"], "Travail, Famille, Patrie",
            "C'est la devise de la Révolution nationale, l'idéologie nationaliste et réactionnaire du régime. La Révolution nationale n'est « presque jamais citée » dans les copies (Limoges, Nantes)."),
          "Question du sujet : « Quelles sont les caractéristiques du régime de Vichy ? »"),
        S('histoire_geographie', 'Histoire · le régime de Vichy', Q(
            "Quelle mesure montre que l'antisémitisme du régime de Vichy est un antisémitisme d'État, décidé par Vichy lui-même ?",
            ["Le statut des Juifs d'octobre 1940", "L'appel du 18 juin 1940", "La création des FFI en 1944", "La loi de 1905"], "Le statut des Juifs d'octobre 1940",
            "Dès octobre 1940, Vichy exclut les Juifs de nombreuses professions, avant toute exigence allemande. La police française participe ensuite aux rafles, comme celle du Vel d'Hiv (juillet 1942). Versailles relève que cette responsabilité est souvent attribuée à la seule Allemagne."),
          "Question du sujet : « Quelles sont les caractéristiques du régime de Vichy ? »"),
        S('histoire_geographie', 'Histoire · le régime de Vichy', Q(
            "Quelle entrevue engage officiellement la collaboration de Vichy avec l'Allemagne, en octobre 1940 ?",
            ["L'entrevue de Montoire", "La conférence de Yalta", "Le traité de Versailles", "La conférence de Munich"], "L'entrevue de Montoire",
            "Pétain rencontre Hitler à Montoire le 24 octobre 1940. La collaboration sera politique, policière et économique (STO en 1943), et la Milice traque les résistants à partir de 1943."),
          "Question du sujet : « Quelles sont les caractéristiques du régime de Vichy ? »"),
        S('histoire_geographie', 'Géographie · la répartition de la population', Q(
            "Sur un croquis de la répartition de la population française, quel espace représente-t-on en couleur claire (faibles densités) ?",
            ["La « diagonale du vide », du nord-est au sud-ouest", "Le littoral méditerranéen", "La vallée du Rhône", "La région parisienne"], "La « diagonale du vide », du nord-est au sud-ouest",
            "Les faibles densités : la diagonale du vide, les massifs montagneux (Alpes, Pyrénées, Massif central, Corse) et les Landes. Les fortes densités : l'Île-de-France, les métropoles, les littoraux, les grandes vallées, le Nord et l'Est."),
          "Question du sujet : « Représentez sur le fond de carte la répartition de la population française. »"),
        S('histoire_geographie', 'Géographie · la répartition de la population', Q(
            "Quelle est approximativement la densité moyenne de la population en France ?",
            ["Environ 120 habitants au km²", "Environ 12 habitants au km²", "Environ 450 habitants au km²", "Environ 1 000 habitants au km²"], "Environ 120 habitants au km²",
            "La densité moyenne est d'environ 120 hab./km², une donnée utile dans la légende. Les jurys ont relevé une confusion fréquente entre densité et ville : on représente des zones de densité, pas seulement des points."),
          "Question du sujet : « Représentez sur le fond de carte la répartition de la population française. »"),
        # ── EMC ──
        S('emc', "EMC · l'égalité à l'école", Q(
            "Quel texte affirme que « les hommes naissent et demeurent libres et égaux en droits » ?",
            ["La Déclaration des droits de l'homme et du citoyen de 1789 (article 1er)", "La loi Ferry de 1882", "Le Code de l'éducation (article L111-1)", "La Charte de la laïcité à l'école"],
            "La Déclaration des droits de l'homme et du citoyen de 1789 (article 1er)",
            "L'égalité figure aussi dans la devise et dans l'article 1er de la Constitution de 1958. Les copies qui citent la DDHC, la Constitution ou les lois Ferry hors du dossier ont été valorisées (Limoges, Créteil)."),
          "Question du sujet : « Pourquoi l'égalité est-elle considérée comme un principe fondamental de l'école de la République ? »"),
        S('emc', "EMC · l'égalité à l'école", Q(
            "Quelles lois rendent l'école primaire gratuite (1881), puis obligatoire et laïque (1882) ?",
            ["Les lois Ferry", "La loi Guizot", "La loi Falloux", "La loi Debré"], "Les lois Ferry",
            "Les lois Jules Ferry font de l'école le premier lieu d'application de l'égalité républicaine : gratuité en 1881, obligation et laïcité de l'enseignement en 1882."),
          "Question du sujet : « Pourquoi l'égalité est-elle considérée comme un principe fondamental de l'école de la République ? »"),
        S('emc', "EMC · l'égalité à l'école", Q(
            "Selon la note de la DEPP (document 2), quels élèves de petite section obtiennent de meilleurs résultats ?",
            ["Les filles, les élèves nés en début d'année et ceux de milieux favorisés", "Les garçons et les élèves nés en fin d'année", "Tous les élèves obtiennent les mêmes scores", "Seuls les élèves de milieux défavorisés"],
            "Les filles, les élèves nés en début d'année et ceux de milieux favorisés",
            "Le tableau donne des scores, et non des nombres d'élèves (Limoges). L'égalité des droits ne garantit donc pas l'égalité des résultats : l'école doit compenser ces écarts."),
          "Document 2 : note de la DEPP, février 2025 : « En petite section de maternelle, des acquis plus solides pour les élèves nés en début d'année et pour les filles »."),
        S('emc', "EMC · l'égalité à l'école", Q(
            "Lequel de ces dispositifs vise à compenser les inégalités sociales et territoriales à l'école ?",
            ["L'éducation prioritaire (REP, REP+) et le dédoublement des classes", "Le redoublement systématique", "Les classes de niveau", "La suppression des devoirs"],
            "L'éducation prioritaire (REP, REP+) et le dédoublement des classes",
            "L'école agit aussi par l'inclusion (AESH, ULIS), le soutien (APC, PPRE), la différenciation et l'égalité filles-garçons. Ces dispositifs sont trop peu cités dans les copies (Versailles, Nantes, Reims)."),
          "Question du sujet : « Montrez comment l'école met en œuvre le principe d'égalité entre tous les élèves, quelles que soient leurs différences. »"),
        S('emc', "EMC · l'égalité à l'école", Q(
            "Que signifie le sigle EMC ?",
            ["Enseignement moral et civique", "Éducation morale et civique", "Éducation à la morale citoyenne", "Enseignement moral et citoyen"], "Enseignement moral et civique",
            "Limoges relève « éducation morale et civique » dans des copies : c'est une erreur. Ses finalités : respecter autrui, acquérir et partager les valeurs de la République, construire une culture civique."), None),
        # ── Sciences : physique-chimie ──
        S('physique_chimie', "Sciences · le mouvement de l'ISS", Q(
            "L'ISS décrit un cercle autour de la Terre à vitesse constante. Comment qualifier son mouvement dans le référentiel géocentrique ?",
            ["Circulaire uniforme", "Rectiligne uniforme", "Circulaire accéléré", "Curviligne ralenti"], "Circulaire uniforme",
            "Circulaire, car la trajectoire est un cercle ; uniforme, car la valeur de la vitesse est constante. Erreurs relevées : « uniforme » oublié ou remplacé par « rectiligne » (Bordeaux)."), ISS),
        S('physique_chimie', "Sciences · l'altitude de l'ISS", N(
            "L'ISS fait 16 tours en 24 h à 28 000 km/h. Quelle distance parcourt-elle en un tour, en km ?", 42000,
            "Un tour dure 24 ÷ 16 = 1,5 h. Distance : d = v × t = 28 000 × 1,5 = 42 000 km."), ISS),
        S('physique_chimie', "Sciences · l'altitude de l'ISS", N(
            "Le périmètre de l'orbite vaut 42 000 km (on prend π = 3). Le rayon de la Terre vaut 6 370 km. Quelle est l'altitude h de l'ISS, en km ?", 630,
            "2 × π × R = 42 000, donc R = 42 000 ÷ 6 = 7 000 km. h = R − R(Terre) = 7 000 − 6 370 = 630 km : entre 160 et 2 000 km, c'est une orbite basse (LEO). Erreur fréquente : confondre altitude et rayon de l'orbite."), ISS),
        S('physique_chimie', "Sciences · l'énergie à bord de l'ISS", Q(
            "Dans la chaîne énergétique d'un panneau solaire, quelle énergie entre et quelle énergie utile sort ?",
            ["Énergie lumineuse en entrée, énergie électrique en sortie (avec une perte thermique)", "Énergie électrique en entrée, énergie lumineuse en sortie", "Énergie thermique en entrée, énergie chimique en sortie", "Énergie nucléaire en entrée, énergie électrique en sortie"],
            "Énergie lumineuse en entrée, énergie électrique en sortie (avec une perte thermique)",
            "Le panneau convertit l'énergie lumineuse (rayonnement solaire) en énergie électrique ; une partie est perdue sous forme thermique. Bordeaux a relevé des confusions avec l'énergie nucléaire."), ISS),
        # ── Sciences : SVT ──
        S('svt', 'Sciences · la photosynthèse', Q(
            "Quels sont les besoins d'une plante verte pour réaliser la photosynthèse ?",
            ["Dioxyde de carbone, eau, sels minéraux et lumière", "Dioxygène, eau et lumière", "Dioxyde de carbone et glucose", "Lumière seulement"], "Dioxyde de carbone, eau, sels minéraux et lumière",
            "C'est la réponse du corrigé de Bordeaux. Oublier les sels minéraux est « très fréquent ». La photosynthèse rejette du dioxygène : ne la confondez pas avec la respiration."), ISS),
        S('svt', 'Sciences · la photosynthèse', Q(
            "Par où la plante capte-t-elle le dioxyde de carbone de l'air pour la photosynthèse ?",
            ["Par les feuilles (au niveau des stomates)", "Par les racines", "Par les fleurs", "Par la tige uniquement"], "Par les feuilles (au niveau des stomates)",
            "Le CO₂ entre par les stomates des feuilles. L'eau, elle, est puisée par les racines et monte par la tige jusqu'aux feuilles. Créteil a valorisé la mention des stomates."), ISS),
        S('svt', 'Sciences · la photosynthèse', Q(
            "Une feuille panachée est éclairée, son centre masqué, puis traitée au lugol, qui s'assombrit en présence d'amidon. Seule la zone verte et éclairée s'assombrit. Que conclure ?",
            ["La production d'amidon nécessite la chlorophylle et la lumière", "La production d'amidon nécessite seulement la lumière", "La production d'amidon nécessite seulement la chlorophylle", "Le lugol détruit l'amidon des zones blanches"],
            "La production d'amidon nécessite la chlorophylle et la lumière",
            "Zone verte éclairée : amidon. Zone verte masquée : pas d'amidon (rôle de la lumière). Zone blanche éclairée : pas d'amidon (rôle de la chlorophylle). On compare deux zones qui ne diffèrent que d'un facteur."), ISS),
        # ── Sciences : technologie ──
        S('technologie', "Sciences · la régulation thermique de l'ISS", Q(
            "À quel besoin répond le système ACTS de l'ISS (échangeurs et radiateurs orientables) ?",
            ["Réguler la température intérieure de la station", "Produire l'électricité de la station", "Propulser la station sur son orbite", "Recycler l'eau des astronautes"], "Réguler la température intérieure de la station",
            "Il maintient la température dans des limites compatibles avec la vie humaine et le fonctionnement des appareils. Bordeaux attendait le mot « réguler », pas seulement « éviter la surchauffe »."), ISS),
        S('technologie', "Sciences · la régulation thermique de l'ISS", Q(
            "Programme A : si température > 25 °C, orienter les radiateurs vers l'espace ; sinon, si température < 18 °C, les orienter vers la Terre. Le programme B fait l'inverse. Lequel maintient une température stable ?",
            ["Le programme A", "Le programme B", "Les deux", "Aucun des deux"], "Le programme A",
            "Trop chaud : radiateurs vers l'espace pour évacuer la chaleur. Trop froid : vers la Terre pour la conserver. La température reste entre 18 et 25 °C. « Expliquer la logique du contrôle », c'est dire ce qui se passe dans chaque cas."), ISS),
        S('technologie', "Sciences · la régulation thermique de l'ISS", Q(
            "Dans le système ACTS, quel élément permet d'ajuster automatiquement la position des radiateurs ?",
            ["Des capteurs de température et un algorithme de commande", "Les panneaux solaires", "L'isolation multicouche (MLI)", "Les astronautes, à la main"], "Des capteurs de température et un algorithme de commande",
            "Les capteurs mesurent la température, le programme compare aux seuils et commande les moteurs des radiateurs : c'est une chaîne d'information qui pilote une chaîne d'énergie."), ISS),
        # ── Arts ──
        S('arts', 'Arts plastiques · questionner la ressemblance', Q(
            "Avec quel outil David Hockney a-t-il réalisé « 27th March 2020, No. 1 » ?",
            ["Une tablette numérique (iPad)", "La peinture à l'huile sur toile", "La photographie argentique", "La gravure sur cuivre"], "Une tablette numérique (iPad)",
            "L'œuvre est une peinture sur iPad imprimée sur papier et montée sur cinq panneaux (364 × 521 cm). L'outil numérique fait partie des éléments qui éloignent l'image d'une simple observation du réel."),
          "Œuvre du sujet : David Hockney (né en 1937), « 27th March 2020, No. 1 », 2020, Fondation Louis Vuitton."),
        S('arts', 'Arts plastiques · questionner la ressemblance', Q(
            "Le sujet demande si l'image de Hockney est « le résultat d'une simple observation du réel ». Quelle réponse est la plus juste ?",
            ["Non : l'artiste interprète le réel par ses choix de couleurs, de lumière et d'outil", "Oui : c'est une photographie retouchée", "Oui : l'image reproduit exactement le paysage", "Non : c'est une œuvre abstraite sans lien avec le réel"],
            "Non : l'artiste interprète le réel par ses choix de couleurs, de lumière et d'outil",
            "Le thème « questionner la ressemblance » invite à distinguer ce qui rapproche l'image du réel (motif reconnaissable) et ce qui s'en éloigne (couleurs franches, simplification, outil numérique, format monumental)."),
          "Œuvre du sujet : David Hockney, « 27th March 2020, No. 1 », peinture sur iPad imprimée sur papier, 2020."),
        S('arts', "Éducation musicale · le romantisme", Q(
            "Le « Voyage d'hiver » (Winterreise) de Schubert est :",
            ["Un cycle de lieder pour voix et piano", "Un opéra en trois actes", "Une symphonie pour grand orchestre", "Un concerto pour violon"], "Un cycle de lieder pour voix et piano",
            "Le Voyage d'hiver (1827) réunit 24 lieder sur des poèmes de Wilhelm Müller. Ses thèmes (solitude, voyage, illusion, mort) traduisent l'expression des émotions propre au romantisme."),
          "Question du sujet : « En quoi les thèmes de prédilection de Schubert dans le Voyage d'hiver traduisent-ils l'expression des émotions ? »"),
        S('arts', "Éducation musicale · le romantisme", Q(
            "Selon la citation de Novalis donnée dans le sujet, rendre le monde romantique, c'est :",
            ["Faire voir l'ordinaire comme extraordinaire et le fini comme infini", "Représenter le monde le plus fidèlement possible", "Respecter les règles classiques de la composition", "Mettre la raison au-dessus des sentiments"],
            "Faire voir l'ordinaire comme extraordinaire et le fini comme infini",
            "La citation : « éduquer le sens pour voir l'ordinaire comme extraordinaire, le familier comme étrange […], le fini comme infini ». Le romantisme place la subjectivité et l'émotion de l'artiste au centre."),
          "Citation : « Rendre romantique le monde, c'est nous faire prendre conscience de sa magie, de son mystère, de sa merveille. » Novalis (1772-1801)."),
        S('arts', "Éducation musicale · le romantisme", Q(
            "À quelle période se situe le romantisme en musique ?",
            ["Au XIXe siècle", "Au XVIIe siècle", "Au XVIIIe siècle, avant 1750", "Au XXe siècle"], "Au XIXe siècle",
            "Schubert (1797-1828) en est l'un des premiers représentants, avec Schumann, Chopin, Liszt ou Berlioz. Novalis (1772-1801) est un poète du premier romantisme allemand."), None),
        # ── Anglais ──
        S('anglais', 'Anglais · compréhension', Q(
            "Who is Scooby?", ["A therapy dog (a labradoodle)", "A new pupil", "The school principal", "A teacher"], "A therapy dog (a labradoodle)",
            "Scooby the labradoodle is “the newest member of staff” at Mount St Catherine's primary school."), SCOOBY),
        S('anglais', 'Anglais · compréhension', N(
            "How many mainstream schools in Northern Ireland have a therapy dog like Scooby?", 7,
            "« Mount St Catherine's is one of only seven mainstream schools in Northern Ireland with a therapy dog like Scooby. »"), SCOOBY),
        S('anglais', 'Anglais · compréhension', Q(
            "According to the Department of Education, what is a “newcomer” pupil?",
            ["A pupil who speaks a different language at home than the one used at school", "A pupil who has just started primary school", "A pupil with Special Educational Needs", "A pupil who moved from another town"],
            "A pupil who speaks a different language at home than the one used at school",
            "Le texte le définit ainsi. 93 des 160 élèves sont des « newcomers » et environ 60 ont des besoins éducatifs particuliers (SEN)."), SCOOBY),
        S('anglais', 'Anglais · compréhension', Q(
            "What is Jolene McCaul's role?",
            ["She is a teacher of a SEN class and Scooby's foster mum", "She is the principal of the school", "She is a journalist at BBC News NI", "She trains dogs for Assistance Dogs NI"],
            "She is a teacher of a SEN class and Scooby's foster mum",
            "« Jolene McCaul is the teacher […] who is Scooby's foster mum, and takes him home every day. » She was trained by Assistance Dogs NI and teaches in a class for children with SEN."), SCOOBY),
        S('anglais', 'Anglais · compréhension', Q(
            "According to the principal, Ciara Farley, what has improved since Scooby arrived?",
            ["Attendance", "Exam results", "The school canteen", "Teachers' salaries"], "Attendance",
            "« Our attendance has vastly improved. » The children are keen to come to school to see Scooby at the gate."), SCOOBY),
        S('anglais', 'Anglais · compréhension', Q(
            "What change does Jolene McCaul observe in some children?",
            ["Non-verbal children are starting to speak", "Children no longer need to learn to read", "Children are less keen to come to school", "Children are afraid of the dog"],
            "Non-verbal children are starting to speak", "« We have children that are non-verbal that are actually starting to speak. »"), SCOOBY),
        S('anglais', 'Anglais · lexique', Q(
            "In the text, “Our children really are so keen to get to school” means that the children are:",
            ["Very eager to go to school", "Afraid of going to school", "Often late for school", "Tired of going to school"], "Very eager to go to school",
            "« Keen to » = eager to, enthusiastic about doing something."), SCOOBY),
        S('anglais', 'Anglais · lexique', Q(
            "What does the pupils' special song for Scooby show?",
            ["They have adopted him as part of the school community", "They want him to leave the school", "They are learning to train dogs", "They prefer music to animals"],
            "They have adopted him as part of the school community",
            "« The pupils […] have even written a special song for him which they sing at morning assembly. »"), SCOOBY),
        # ── Compléments (mêmes documents) ──
        S('physique_chimie', "Sciences · la régulation thermique de l'ISS", Q(
            "Les radiateurs de l'ISS évacuent la chaleur dans le vide spatial « par rayonnement ». Pourquoi pas par conduction ou convection ?",
            ["Parce que la conduction et la convection ont besoin de matière, absente dans le vide", "Parce que le rayonnement est plus lent", "Parce que l'ammoniac bloque la conduction", "Parce que les radiateurs sont trop froids"],
            "Parce que la conduction et la convection ont besoin de matière, absente dans le vide",
            "Dans le vide, seul le rayonnement (ici infrarouge) transporte l'énergie thermique. C'est aussi pourquoi l'espace « n'a pas d'air pour servir d'isolant naturel »."), ISS),
        S('physique_chimie', "Sciences · le mouvement de l'ISS", N(
            "L'ISS parcourt son orbite 16 fois en 24 heures. Combien de temps dure un tour, en heures ?", 1.5,
            "24 ÷ 16 = 1,5 h, soit 1 h 30 min. C'est pourquoi les astronautes voient 16 levers et couchers de soleil par jour."), ISS),
        S('technologie', "Sciences · la régulation thermique de l'ISS", Q(
            "Dans le système ACTS, quel fluide transporte la chaleur jusqu'aux radiateurs extérieurs ?",
            ["L'ammoniac", "L'eau", "L'air", "L'huile"], "L'ammoniac",
            "La chaleur est d'abord captée par un échangeur à eau, puis transférée à un échangeur à ammoniac relié aux radiateurs orientables."), ISS),
        S('technologie', "Sciences · l'énergie à bord de l'ISS", Q(
            "D'où vient l'énergie électrique qui fait fonctionner les systèmes de l'ISS ?",
            ["De vastes panneaux solaires orientables", "D'un réacteur nucléaire", "De batteries rechargées sur Terre", "D'un moteur à essence"], "De vastes panneaux solaires orientables",
            "Le sujet le précise : « l'énergie électrique nécessaire au fonctionnement de ces systèmes est produite grâce à de vastes panneaux solaires orientables »."), ISS),
        S('svt', 'Sciences · la culture des plantes dans l\'ISS', Q(
            "Les astronautes cultivent les plantes par hydroponie. Qu'est-ce que c'est ?",
            ["Une culture sans terre : les racines baignent dans une solution d'eau et de sels minéraux", "Une culture dans un sol très arrosé", "Une culture sans lumière", "Une culture uniquement sous l'eau de mer"],
            "Une culture sans terre : les racines baignent dans une solution d'eau et de sels minéraux",
            "La plante reçoit l'eau et les sels minéraux par une solution nutritive : la terre n'est qu'un support. Elle a toujours besoin de lumière et de CO₂."), ISS),
        S('svt', 'Sciences · la photosynthèse', Q(
            "Pourquoi décolore-t-on la feuille à l'alcool bouillant avant de la plonger dans le lugol ?",
            ["Pour retirer la chlorophylle verte et voir clairement la coloration due à l'amidon", "Pour produire de l'amidon", "Pour tuer les bactéries", "Pour rendre la feuille plus verte"],
            "Pour retirer la chlorophylle verte et voir clairement la coloration due à l'amidon",
            "Le vert de la chlorophylle masquerait le changement de couleur du lugol (jaune, qui s'assombrit en présence d'amidon)."), ISS),
        S('emc', "EMC · l'égalité à l'école", Q(
            "Selon l'article L111-1 du Code de l'éducation (document 1), quelle est « la première priorité nationale » ?",
            ["L'éducation", "La défense", "La santé", "L'emploi"], "L'éducation",
            "« L'éducation est la première priorité nationale. Le service public de l'éducation est conçu et organisé en fonction des élèves et des étudiants. »"),
          "Document 1 : article L111-1 du Code de l'éducation (modifié en 2021)."),
        S('emc', "EMC · l'égalité à l'école", Q(
            "Le document 1 dit que l'école « veille à la scolarisation inclusive de tous les enfants ». Qu'est-ce que cela signifie ?",
            ["Accueillir tous les enfants, y compris en situation de handicap, en adaptant l'enseignement à leurs besoins", "Regrouper les élèves par niveau", "Réserver l'école aux enfants sans difficulté", "Scolariser les enfants à domicile"],
            "Accueillir tous les enfants, y compris en situation de handicap, en adaptant l'enseignement à leurs besoins",
            "L'école inclusive s'appuie notamment sur les AESH, les ULIS et les projets personnalisés de scolarisation (PPS)."),
          "Document 1 : article L111-1 du Code de l'éducation."),
        S('arts', 'Arts plastiques · questionner la ressemblance', Q(
            "L'œuvre de Hockney mesure 3,6 m sur 5,2 m et est montée sur cinq panneaux. Quel effet produit ce format ?",
            ["Un format monumental qui immerge le spectateur dans le paysage", "Un format intime, à regarder de près", "Un format qui imite une carte postale", "Aucun effet : le format ne compte pas"],
            "Un format monumental qui immerge le spectateur dans le paysage",
            "Le dessin fait sur un petit écran d'iPad est agrandi à l'échelle d'une paroi : le changement d'échelle fait partie des choix qui transforment le rapport au réel."),
          "Œuvre du sujet : David Hockney, « 27th March 2020, No. 1 », 364 × 521 cm, cinq panneaux."),
    ]),
    # ── Ajout : questions complémentaires tirées du même sujet ──
    epreuve('Première épreuve écrite (français et mathématiques)', 20277, [
        S('francais', 'Étude de la langue · voix passive', Q(
            "« Les jugements d'expropriation étaient rendus. » À quelle voix est le verbe ?",
            ["Voix passive", "Voix active", "Voix pronominale", "Forme impersonnelle"], "Voix passive",
            "Auxiliaire être (ici à l'imparfait) + participe passé : voix passive. Le sujet « les jugements » subit l'action ; l'agent (les tribunaux) n'est pas exprimé."), ZOLA),
        S('francais', 'Étude de la langue · temps et modes', Q(
            "« À mesure que le Bonheur des Dames s'élargissait, il semblait que le Vieil Elbeuf diminuât. » Temps et mode de « diminuât » ?",
            ["Imparfait du subjonctif", "Passé simple de l'indicatif", "Imparfait de l'indicatif", "Conditionnel présent"], "Imparfait du subjonctif",
            "Après « il semblait que », le subjonctif est requis ; la concordance des temps de la langue littéraire impose l'imparfait du subjonctif (-ât) après un verbe au passé."), ZOLA),
        S('francais', 'Étude de la langue · type de phrase', Q(
            "« Prenez garde ! ils vous passeraient sur le corps. » À quel mode est « Prenez » ?",
            ["Impératif présent", "Indicatif présent", "Subjonctif présent", "Infinitif"], "Impératif présent",
            "L'impératif, sans sujet exprimé, donne un ordre ou un conseil : la première phrase est injonctive (et exclamative par sa ponctuation)."), ZOLA),
        S('francais', 'Étude de la langue · nature des mots', Q(
            "« Deux bandes de démolisseurs attaquaient déjà la trouée. » Nature de « déjà » ?",
            ["Adverbe", "Adjectif", "Préposition", "Conjonction"], "Adverbe",
            "Invariable, il modifie le sens du verbe en le situant dans le temps : adverbe de temps."), ZOLA),
        S('francais', 'Étude de la langue · pluriels', Q(
            "Une note du sujet rappelle que « baux » est le pluriel de « bail ». Lequel de ces noms en -ail fait aussi son pluriel en -aux ?",
            ["Travail", "Détail", "Rail", "Éventail"], "Travail",
            "Seuls quelques noms en -ail font -aux : bail, corail, émail, soupirail, travail, vantail, vitrail. Les autres prennent un -s : détails, rails, éventails."), ZOLA),
        S('francais', 'Lexique · sens en contexte', Q(
            "« Debout sur le seuil de sa boutique, l'oncle regardait, d'un œil morne. » Que signifie « morne » ?",
            ["Triste et sans éclat", "Joyeux", "Curieux", "Menaçant"], "Triste et sans éclat",
            "Le regard de Baudu dit son abattement devant les travaux du grand magasin qui condamnent son petit commerce."), ZOLA),
        S('francais', 'Lexique · images', Q(
            "Zola décrit les vitrines du Vieil Elbeuf « écrasées sous l'entresol bas, aux baies rondes de prison ». Que suggère cette image ?",
            ["La boutique est comme enfermée, étouffée, condamnée", "La boutique est un lieu de fête", "La boutique est très moderne", "La boutique va s'agrandir"],
            "La boutique est comme enfermée, étouffée, condamnée",
            "L'image de la prison s'ajoute à la « détresse » de la façade : tout dit le déclin du petit commerce face au grand magasin."), ZOLA),
        S('francais', 'Lexique · formation des mots', Q(
            "Comment est formé l'adverbe « obstinément » (ligne 15) ?",
            ["Adjectif « obstiné » + suffixe -ment", "Nom « obstination » + suffixe -ment", "Préfixe ob- + base « stinément »", "Verbe « obstiner » + suffixe -ément"],
            "Adjectif « obstiné » + suffixe -ment",
            "Le suffixe -ment forme des adverbes de manière à partir d'adjectifs. Après un adjectif en -é, on ajoute directement -ment (aisément, obstinément)."), ZOLA),
        S('francais', 'Culture littéraire · Zola', Q(
            "À quel mouvement littéraire Émile Zola est-il rattaché ?",
            ["Le naturalisme", "Le romantisme", "Le classicisme", "Le surréalisme"], "Le naturalisme",
            "Au Bonheur des Dames (1883) appartient au cycle des Rougon-Macquart, « histoire naturelle et sociale d'une famille sous le Second Empire »."), ZOLA),
        S('francais', 'Culture littéraire · Zola', Q(
            "Les grands travaux évoqués dans le texte renvoient aux transformations de Paris menées par :",
            ["Le baron Haussmann, sous le Second Empire", "Louis XIV", "Napoléon Ier", "Le général de Gaulle"], "Le baron Haussmann, sous le Second Empire",
            "La note du sujet précise de ne pas le confondre avec le baron Hartmann, personnage inventé par Zola."), ZOLA),
        S('mathematiques', 'Exercice 1 · tableau et probabilités', N(
            "Combien d'élèves ne pratiquent ni sport ni instrument ?", 150,
            "300 − (120 + 75 − 45) = 300 − 150 = 150 élèves."), EX1),
        S('mathematiques', 'Exercice 1 · tableau et probabilités', N(
            "Combien d'élèves pratiquent un instrument mais pas de sport ?", 30,
            "75 musiciens − 45 qui font aussi du sport = 30."), EX1),
        S('mathematiques', 'Exercice 2 · motif évolutif', N(
            "Combien de carreaux le motif compte-t-il à l'étape 5 ?", 13,
            "On ajoute 3 carreaux à chaque étape : 10 + 3 = 13."), EX2),
        S('mathematiques', 'Exercice 3 · pentagones', N(
            "Quelle est la somme des angles d'un pentagone, en degrés ?", 540,
            "5 × 108° = 540°. On peut aussi découper le pentagone en 3 triangles : 3 × 180° = 540°."), EX3),
        S('mathematiques', 'Exercice 5 · axe gradué', N(
            "Quelle est l'abscisse du milieu du segment [OA], avec a = 1/2 ? (Réponse décimale ou fraction.)", 0.25,
            "a ÷ 2 = 1/4 = 0,25."), EX5),
        S('mathematiques', 'Exercice 5 · axe gradué', Q(
            "Le point C d'abscisse 0,45 appartient-il au segment [AB], avec a = 0,5 et b = 1,375 ?",
            ["Non : 0,45 < 0,5", "Oui : 0,45 est entre 0 et 1", "Oui : 0,45 < 1,375", "On ne peut pas savoir sans calculatrice"], "Non : 0,45 < 0,5",
            "Pour appartenir à [AB], il faut a ≤ c ≤ b. 0,45 est plus petit que 0,5 : C est à gauche de A."), EX5),
    ]),
    epreuve('Seconde épreuve écrite (domaines au choix)', 20268, [
        S('histoire_geographie', 'Histoire · le régime de Vichy', Q(
            "Qu'est-ce que le Service du travail obligatoire (STO), créé en 1943 ?",
            ["L'envoi forcé de jeunes Français travailler en Allemagne", "Un service militaire dans l'armée française", "Un travail bénévole dans les campagnes", "La création des syndicats"],
            "L'envoi forcé de jeunes Français travailler en Allemagne",
            "Le STO montre la collaboration économique de Vichy ; beaucoup de réfractaires rejoignent alors les maquis de la Résistance."), "Question du sujet : « Quelles sont les caractéristiques du régime de Vichy ? »"),
        S('histoire_geographie', 'Histoire · le régime de Vichy', Q(
            "Quel organisme paramilitaire, créé par Vichy en 1943, traque les résistants ?",
            ["La Milice", "Les FFI", "La Gestapo", "Le Conseil national de la Résistance"], "La Milice",
            "La Milice française est une police politique de Vichy. La Gestapo est la police allemande ; les FFI et le CNR appartiennent à la Résistance."), None),
        S('histoire_geographie', 'Histoire · le régime de Vichy', Q(
            "Que se passe-t-il en novembre 1942 ?",
            ["Les Allemands envahissent la zone sud (« zone libre »)", "Pétain obtient les pleins pouvoirs", "Paris est libéré", "L'armistice est signé"], "Les Allemands envahissent la zone sud (« zone libre »)",
            "Après le débarquement allié en Afrique du Nord, toute la France est occupée. Il ne faut pas confondre la zone libre avec la France libre du général de Gaulle."), None),
        S('histoire_geographie', 'Histoire · le régime de Vichy', Q(
            "Comment qualifier le régime de Vichy ?",
            ["Un régime autoritaire, en rupture avec la République", "Une démocratie parlementaire", "Une monarchie constitutionnelle", "La IVe République"], "Un régime autoritaire, en rupture avec la République",
            "Pas d'élections, pas de partis, presse censurée, culte du chef : Vichy n'est pas une République. Versailles conseille de distinguer régime autoritaire, totalitaire et dictature."), None),
        S('histoire_geographie', 'Géographie · la répartition de la population', Q(
            "Quelle région française est la plus peuplée et la plus densément peuplée ?",
            ["L'Île-de-France", "La Bretagne", "L'Auvergne", "La Corse"], "L'Île-de-France",
            "Avec plus de 12 millions d'habitants, l'Île-de-France concentre près d'un Français sur cinq ; c'est le cœur des fortes densités sur un croquis."), None),
        S('histoire_geographie', 'Géographie · la répartition de la population', Q(
            "Sur un croquis, comment représenter des densités de population différentes ?",
            ["Par des plages de couleur graduées, du plus foncé (fortes densités) au plus clair", "Par des flèches", "Par des points de toutes les couleurs au hasard", "En entourant chaque ville"],
            "Par des plages de couleur graduées, du plus foncé (fortes densités) au plus clair",
            "Erreur relevée : entourer les métropoles au lieu de délimiter des zones de densité (Bordeaux, Nantes, Limoges). Titre et légende s'écrivent en noir."), None),
        S('emc', "EMC · l'égalité à l'école", Q(
            "Que proclame l'article 1er de la Constitution de 1958 ?",
            ["La France est une République indivisible, laïque, démocratique et sociale, qui assure l'égalité de tous les citoyens devant la loi", "La France est une monarchie", "Le français est la langue de la République", "L'école est obligatoire de 3 à 16 ans"],
            "La France est une République indivisible, laïque, démocratique et sociale, qui assure l'égalité de tous les citoyens devant la loi",
            "« … sans distinction d'origine, de race ou de religion. » C'est un texte fondateur de l'égalité à citer dans la question 1 du sujet."), None),
        S('emc', "EMC · l'égalité à l'école", Q(
            "Que sont les AESH ?",
            ["Des accompagnants des élèves en situation de handicap", "Des inspecteurs de l'Éducation nationale", "Des assistants de langue", "Des animateurs du périscolaire"], "Des accompagnants des élèves en situation de handicap",
            "Ils participent à l'école inclusive, avec les ULIS et les plans personnalisés (PPS, PAP)."), None),
        S('emc', "EMC · l'égalité à l'école", Q(
            "Le document 3 est une affiche d'élèves de CE2 sur l'égalité filles-garçons. Quel thème de l'EMC illustre-t-elle ?",
            ["La lutte contre les stéréotypes et les discriminations", "La laïcité", "Les institutions européennes", "La sécurité routière"], "La lutte contre les stéréotypes et les discriminations",
            "L'égalité filles-garçons a été « quasiment ignorée » dans les copies (Nantes), alors que l'affiche du dossier y invitait."), None),
        S('physique_chimie', "Sciences · le mouvement de l'ISS", Q(
            "Selon le document 2, sur quel type d'orbite se trouvent les satellites GPS et Galileo ?",
            ["L'orbite moyenne (MEO), entre 2 000 et 35 000 km", "L'orbite basse (LEO)", "L'orbite géostationnaire (GEO)", "À la surface de la Terre"], "L'orbite moyenne (MEO), entre 2 000 et 35 000 km",
            "LEO : 160 à 2 000 km (Hubble, ISS, Starlink) ; MEO : 2 000 à 35 000 km (GPS, Galileo) ; GEO : environ 35 786 km (Meteosat)."), ISS),
        S('physique_chimie', "Sciences · la régulation thermique de l'ISS", Q(
            "À quoi sert l'isolation multicouche (MLI) qui recouvre l'ISS ?",
            ["À limiter les échanges thermiques entre la station et l'espace", "À produire de l'électricité", "À propulser la station", "À protéger des météorites seulement"], "À limiter les échanges thermiques entre la station et l'espace",
            "Dans l'espace, il n'y a pas d'air pour isoler : la MLI protège les modules habités des écarts de température."), ISS),
        S('technologie', "Sciences · l'énergie à bord de l'ISS", Q(
            "Pourquoi les panneaux solaires de l'ISS sont-ils orientables ?",
            ["Pour rester face au Soleil et recevoir le maximum de lumière", "Pour se protéger du froid", "Pour communiquer avec la Terre", "Pour freiner la station"], "Pour rester face au Soleil et recevoir le maximum de lumière",
            "L'ISS fait un tour de Terre en 1 h 30 : l'orientation automatique des panneaux maximise l'énergie lumineuse convertie en électricité."), ISS),
        S('svt', 'Sciences · la photosynthèse', Q(
            "Quel pigment vert permet la photosynthèse dans les feuilles ?",
            ["La chlorophylle", "L'amidon", "Le glucose", "La sève"], "La chlorophylle",
            "La chlorophylle capte l'énergie lumineuse. Les zones blanches d'une feuille panachée n'en ont pas et ne produisent pas d'amidon."), ISS),
        S('svt', 'Sciences · la circulation de l\'eau dans la plante', Q(
            "Quel trajet suit l'eau dans une plante qui la puise dans le sol ?",
            ["Racines → tige → feuilles", "Feuilles → tige → racines", "Fleurs → feuilles → racines", "Elle reste dans les racines"], "Racines → tige → feuilles",
            "L'eau et les sels minéraux (la sève brute) montent des racines jusqu'aux feuilles, où se fait la photosynthèse."), ISS),
        S('arts', 'Éducation musicale · le romantisme', Q(
            "Lequel de ces compositeurs n'est pas romantique ?",
            ["Jean-Sébastien Bach", "Franz Schubert", "Frédéric Chopin", "Robert Schumann"], "Jean-Sébastien Bach",
            "Bach (1685-1750) est un compositeur baroque. Schubert, Chopin, Schumann, Liszt, Berlioz appartiennent au XIXe siècle romantique."), None),
        S('arts', 'Arts plastiques · questionner la ressemblance', Q(
            "David Hockney, auteur de l'œuvre du sujet, est un peintre :",
            ["Britannique, né en 1937, figure du pop art", "Français de la Renaissance", "Italien baroque", "Espagnol cubiste"], "Britannique, né en 1937, figure du pop art",
            "Installé en Normandie pendant le confinement de 2020, il y a peint l'arrivée du printemps sur iPad, d'où le titre daté « 27th March 2020 »."), None),
        S('anglais', 'Anglais · lexique', Q(
            "What is a labradoodle?", ["A cross between a labrador and a poodle", "A kind of cat", "A toy", "A school subject"], "A cross between a labrador and a poodle",
            "Scooby est un chien croisé labrador et caniche (poodle)."), SCOOBY),
        S('anglais', 'Anglais · lexique', Q(
            "“Our attendance has vastly improved.” What does “attendance” mean?",
            ["The fact of being present at school", "The pupils' marks", "The school timetable", "The teachers' salaries"], "The fact of being present at school",
            "Attendance = l'assiduité, la présence. « Vastly » = considérablement."), SCOOBY),
        S('anglais', 'Anglais · lexique', Q(
            "What is a “morning assembly” in a British school?",
            ["A gathering of pupils and staff at the start of the day", "A maths lesson", "A meeting of parents", "A break time"], "A gathering of pupils and staff at the start of the day",
            "C'est lors de l'assemblée du matin que les élèves chantent la chanson écrite pour Scooby."), SCOOBY),
        S('anglais', 'Anglais · compréhension', Q(
            "Jolene McCaul is Scooby's “foster mum”. What does it mean?",
            ["She looks after him and takes him home every day", "She is his vet", "She sold him to the school", "She is his trainer at Assistance Dogs NI"], "She looks after him and takes him home every day",
            "Foster = d'accueil : elle s'occupe du chien et le ramène chez elle chaque soir."), SCOOBY),
    ]),
]
