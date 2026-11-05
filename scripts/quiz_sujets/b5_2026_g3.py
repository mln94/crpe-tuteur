# Bac+5, session 2026, groupement 3
from slib import S, Q, N, C, epreuve

ROUSSEAU = ("Texte : Jean-Jacques Rousseau, Émile ou de l'Éducation, livre III (1762). Rousseau défend une éducation fondée sur l'expérience "
            "et l'observation de la nature plutôt que sur les livres et les discours.")
REGATE = ("Exercice 2 : une régate au large des îles Chausey. Phares : C (îles Chausey), G (Granville), R (Regnéville). "
          "RG = 20 km, CG = 15 km, CR = 25 km. Le parcours mesure 96 km ; les bateaux partent à 8 h 30.")
RALLYE = "Exercice 4 : un rallye vélo. Distances parcourues : 9 km (126 élèves), 11 km (120), 12 km (140), 15 km (34). Les sponsors versent 1,25 € par kilomètre."
ARCTIQUE = "Sujet de sciences et technologie : la station Tara Polar, un laboratoire flottant en Arctique (banquise, biodiversité, base dérivante)."
REVOLUTION = "Sujet d'histoire et EMC : en CM1, « De l'année 1789 à l'exécution du roi » ; en CP, La Marseillaise, symbole de la République."

QUESTIONS = [
    epreuve('Épreuve écrite disciplinaire de français', 20148, [
        S('francais', 'Étude de la langue · accords', Q(
            "« Il faut des sentiments qu'il n'a point éprouvés. » Pourquoi « éprouvés » est-il au masculin pluriel ?",
            ["Il s'accorde avec le COD « qu' » (des sentiments), placé avant l'auxiliaire avoir", "Il s'accorde avec le sujet « il »", "Un participe passé avec avoir s'accorde toujours au pluriel", "Il s'accorde avec « point »"],
            "Il s'accorde avec le COD « qu' » (des sentiments), placé avant l'auxiliaire avoir",
            "Le pronom relatif « que » reprend « des sentiments » et est COD de « a éprouvés » : placé avant l'auxiliaire avoir, il impose l'accord."), ROUSSEAU),
        S('francais', 'Étude de la langue · accords', Q(
            "« L'on observe les objets qui rendent reconnaissable le lieu de son coucher. » Avec quel mot « reconnaissable » s'accorde-t-il ?",
            ["Avec « le lieu », dont il est l'attribut", "Avec « les objets »", "Avec « l'on »", "Il est invariable"], "Avec « le lieu », dont il est l'attribut",
            "Les objets rendent le lieu reconnaissable : « reconnaissable » est attribut du COD « le lieu » (masculin singulier), et non des « objets »."), ROUSSEAU),
        S('francais', 'Étude de la langue · nature et fonction', Q(
            "« Rendez votre élève attentif aux phénomènes de la nature. » Fonction de « attentif » ?",
            ["Attribut du COD « votre élève »", "Épithète de « élève »", "Attribut du sujet", "Complément circonstanciel de manière"], "Attribut du COD « votre élève »",
            "Avec « rendre », l'adjectif donne une qualité au COD par l'intermédiaire du verbe : c'est un attribut du COD (comme « on le trouve sympathique »)."), ROUSSEAU),
        S('francais', 'Étude de la langue · nature et fonction', Q(
            "« Que ne commencez-vous par lui montrer l'objet même, afin qu'il sache au moins de quoi vous lui parlez ! » Nature de « afin qu'il sache au moins de quoi vous lui parlez » ?",
            ["Subordonnée conjonctive circonstancielle de but", "Subordonnée relative", "Subordonnée complétive", "Subordonnée circonstancielle de cause"], "Subordonnée conjonctive circonstancielle de but",
            "« Afin que » introduit le but et entraîne le subjonctif (« sache »)."), ROUSSEAU),
        S('francais', 'Étude de la langue · nature et fonction', Q(
            "« La verdure a pris durant la nuit une vigueur nouvelle. » Fonction de « durant la nuit » ?",
            ["Complément circonstanciel de temps", "COD du verbe prendre", "Complément du nom « verdure »", "Sujet"], "Complément circonstanciel de temps",
            "Groupe nominal prépositionnel, déplaçable et supprimable : complément circonstanciel (complément de phrase) de temps. Le COD est « une vigueur nouvelle »."), ROUSSEAU),
        S('francais', 'Étude de la langue · réécriture', Q(
            "Réécrivez avec « ils » : « Qu'il ne sache rien parce que vous le lui avez dit, mais parce qu'il l'a compris lui-même. »",
            ["Qu'ils ne sachent rien parce que vous le leur avez dit, mais parce qu'ils l'ont compris eux-mêmes.",
             "Qu'ils ne sachent rien parce que vous le leurs avez dit, mais parce qu'ils l'ont compris eux-même.",
             "Qu'ils ne savent rien parce que vous le leur avez dit, mais parce qu'ils l'ont compris lui-même.",
             "Qu'ils ne sachent rien parce que vous les leur avez dit, mais parce qu'ils l'ont compris eux-mêmes."],
            "Qu'ils ne sachent rien parce que vous le leur avez dit, mais parce qu'ils l'ont compris eux-mêmes.",
            "« Leur », pronom personnel, est invariable (jamais « leurs » devant un verbe). « Lui-même » devient « eux-mêmes ». Le subjonctif (sachent) est maintenu."), ROUSSEAU),
        S('francais', 'Étude de la langue · type et forme', Q(
            "« Ne tenez point à l'enfant des discours qu'il ne peut entendre. » Type et forme de la phrase ?",
            ["Injonctive ; forme négative", "Déclarative ; forme négative", "Interrogative ; forme emphatique", "Exclamative ; forme passive"], "Injonctive ; forme négative",
            "Le verbe à l'impératif (« tenez ») donne un ordre : phrase injonctive. « Ne… point » marque la forme négative."), ROUSSEAU),
        S('francais', 'Étude de la langue · propositions', N(
            "« Une belle soirée on va se promener dans un lieu favorable, où l'horizon bien découvert laisse voir à plein le soleil couchant, et l'on observe les objets qui rendent reconnaissable le lieu de son coucher. » Combien de propositions compte cette phrase ?", 4,
            "Quatre verbes conjugués : va (se promener), laisse (voir), observe, rendent. Deux propositions coordonnées par « et » ; chacune a sa subordonnée relative (« où… », « qui… »)."), ROUSSEAU),
        S('francais', 'Lexique · formation des mots', Q(
            "Comment est formé « géographie » ?",
            ["Composition savante : géo- (la terre) + -graphie (écrire, décrire)", "Dérivation : géo + suffixe -ie", "Mot simple venu du latin", "Composition française : géant + graphie"], "Composition savante : géo- (la terre) + -graphie (écrire, décrire)",
            "Deux éléments grecs : la géographie est la description de la Terre. Avec géo- : géologie, géomètre ; avec -graphie : orthographe, photographie."), ROUSSEAU),
        S('francais', 'Lexique · sens en contexte', Q(
            "« Les oiseaux en chœur se réunissent et saluent de concert le père de la vie. » Qui est « le père de la vie » ?",
            ["Le soleil, désigné par une périphrase", "Le maître", "Dieu, nommé directement", "L'enfant Émile"], "Le soleil, désigné par une périphrase",
            "La scène décrit le lever du soleil. Les oiseaux sont personnifiés : ils « saluent » l'astre qui fait vivre la nature."), ROUSSEAU),
    ]),
    epreuve('Épreuve écrite disciplinaire de mathématiques', 20160, [
        S('mathematiques', 'Exercice 2 · Pythagore', Q(
            "RG = 20 km, CG = 15 km, CR = 25 km. Le triangle RGC est-il rectangle ?",
            ["Oui, en G : 15² + 20² = 25²", "Oui, en C", "Non : 15 + 20 ≠ 25", "On ne peut pas savoir sans figure"], "Oui, en G : 15² + 20² = 25²",
            "225 + 400 = 625 = 25². Par la réciproque du théorème de Pythagore, le triangle est rectangle au sommet opposé au plus grand côté [CR], c'est-à-dire en G."), REGATE),
        S('mathematiques', 'Exercice 2 · vitesse', N(
            "Le bateau A part à 8 h 30 et arrive à 14 h 54 après 96 km. Quelle est sa vitesse moyenne, en km/h ?", 15,
            "Durée : 6 h 24 min = 6,4 h (24 min = 0,4 h). 96 ÷ 6,4 = 15 km/h."), REGATE),
        S('mathematiques', 'Exercice 2 · conversions', N(
            "Le bateau B avance à 3,9 m/s. Quelle est sa vitesse en km/h ?", 14.04,
            "On multiplie par 3,6 : 3,9 × 3,6 = 14,04 km/h. Classement : A (15 km/h), C (14,5 km/h), puis B. B arrive vers 15 h 20 (96 ÷ 14,04 ≈ 6 h 50 min)."), REGATE),
        S('mathematiques', 'Exercice 2 · PPCM', N(
            "Le phare de Granville émet un signal toutes les 12 s, celui de Chausey toutes les 18 s. Ils émettent ensemble à 8 h 30. Au bout de combien de secondes émettront-ils à nouveau ensemble ?", 36,
            "On cherche le plus petit multiple commun de 12 et 18 : 36 secondes."), REGATE),
        S('mathematiques', 'Exercice 3 · vrai ou faux', Q(
            "Affirmation : « Si AM = MB, alors M est le milieu de [AB]. » Vrai ou faux ?",
            ["Faux : M peut être n'importe quel point de la médiatrice de [AB]", "Vrai", "Faux : il faut AM = 2MB", "Vrai si A et B sont distincts"], "Faux : M peut être n'importe quel point de la médiatrice de [AB]",
            "Les points équidistants de A et B forment la médiatrice de [AB]. M est le milieu seulement s'il est aussi sur le segment [AB]."), None),
        S('mathematiques', 'Exercice 3 · probabilités', Q(
            "Dans un jeu de 32 cartes, on tire une carte au hasard. Quelle est la probabilité d'obtenir un valet ou un cœur ?",
            ["11/32", "12/32", "3/8", "1/4"], "11/32",
            "4 valets + 8 cœurs = 12, mais le valet de cœur est compté deux fois : 11 cartes. P = 11/32."), None),
        S('mathematiques', 'Exercice 3 · vrai ou faux', Q(
            "Affirmation : « Le carré d'un nombre entier impair est un nombre entier impair. » Vrai ou faux ?",
            ["Vrai", "Faux"], "Vrai",
            "Un impair s'écrit 2k + 1. (2k + 1)² = 4k² + 4k + 1 = 2(2k² + 2k) + 1 : c'est un impair. Un calcul littéral prouve le cas général ; des exemples ne suffisent pas."), None),
        S('mathematiques', 'Exercice 4 · conversions', N(
            "Une roue de vélo mesure 26 pouces de diamètre ; 1 pouce = 2,54 cm. Quel est son diamètre, en cm ?", 66.04,
            "26 × 2,54 = 66,04 cm (valeur exacte)."), None),
        S('mathematiques', 'Exercice 4 · périmètre', N(
            "Une roue de 66,04 cm de diamètre fait 6 124 tours. Quelle distance parcourt-elle, en km, arrondie au dixième ?", 12.7,
            "Un tour = π × 66,04 cm ≈ 207,5 cm. 6 124 × π × 0,6604 m ≈ 12 706 m ≈ 12,7 km. Le périmètre d'un cercle vaut π × diamètre.", tol=0.05), None),
        S('mathematiques', 'Exercice 4 · statistiques', N(
            "Quelle somme l'école recevra-t-elle des sponsors, en euros ?", 5805,
            "Distance totale : 9 × 126 + 11 × 120 + 12 × 140 + 15 × 34 = 1 134 + 1 320 + 1 680 + 510 = 4 644 km. 4 644 × 1,25 = 5 805 €."), RALLYE),
        S('mathematiques', 'Exercice 4 · statistiques', Q(
            "Un enseignant affirme que moins de deux cinquièmes des élèves ont parcouru 12 km ou plus. A-t-il raison ?",
            ["Non : 174 élèves sur 420, soit environ 41 %, plus que 2/5 (40 %)", "Oui : 174 est inférieur à 420", "Oui : 34 élèves seulement ont fait 15 km", "Non : plus de la moitié ont fait 12 km ou plus"],
            "Non : 174 élèves sur 420, soit environ 41 %, plus que 2/5 (40 %)",
            "12 km ou plus : 140 + 34 = 174 élèves. 2/5 de 420 = 168. 174 > 168, l'affirmation est fausse."), RALLYE),
        S('mathematiques', 'Exercice 4 · statistiques', N(
            "Quelle est la distance médiane parcourue, en km ?", 11,
            "420 élèves : la médiane est entre la 210e et la 211e valeur. Effectifs cumulés : 126, puis 246. Les deux valeurs sont 11 km. (La moyenne vaut 4 644 ÷ 420 ≈ 11,06 km.)"), RALLYE),
    ]),
    epreuve("Épreuve écrite d'application (sciences, histoire-géographie-EMC ou arts)", 20172, [
        # ── Sciences ──
        S('physique_chimie', "Sciences · la formation de la banquise", Q(
            "Lors de la solidification de l'eau déminéralisée, la courbe de température présente un palier à 0 °C. Que se passe-t-il pendant ce palier ?",
            ["L'eau change d'état (liquide et solide coexistent) à température constante", "L'eau continue de refroidir", "L'eau se réchauffe", "L'eau s'évapore"],
            "L'eau change d'état (liquide et solide coexistent) à température constante",
            "Un corps pur change d'état à température constante. L'eau salée, qui est un mélange, ne présente pas de palier net et se solidifie en dessous de 0 °C : c'est la différence entre les deux courbes."), ARCTIQUE),
        S('physique_chimie', "Sciences · l'effet d'albédo", Q(
            "Deux récipients d'eau, l'un recouvert de noir, l'autre de blanc, sont exposés au soleil. Dans lequel la température monte-t-elle le plus vite ?",
            ["Le récipient noir : une surface sombre absorbe davantage le rayonnement", "Le récipient blanc", "Les deux au même rythme", "Aucun des deux"],
            "Le récipient noir : une surface sombre absorbe davantage le rayonnement",
            "C'est l'effet d'albédo : la banquise blanche renvoie une grande partie du rayonnement solaire ; l'océan sombre qui la remplace l'absorbe et se réchauffe, ce qui accélère la fonte."), ARCTIQUE),
        S('svt', 'Sciences · la classification', Q(
            "En biologie, qu'est-ce qu'un « attribut » ?",
            ["Un caractère que possède un être vivant (par exemple des poils, des mâchoires, un squelette interne)", "Le nom de l'espèce", "Le milieu où vit l'animal", "Ce que l'animal mange"],
            "Un caractère que possède un être vivant (par exemple des poils, des mâchoires, un squelette interne)",
            "La classification phylogénétique regroupe les espèces qui partagent des attributs, en groupes emboîtés. On ne classe jamais sur un attribut absent."), ARCTIQUE),
        S('svt', 'Sciences · la classification', Q(
            "L'ours polaire, la morue, le requin et le macareux partagent un attribut que n'ont pas le krill, la littorine et la mye. Lequel ?",
            ["Un squelette interne avec une colonne vertébrale (ce sont des vertébrés)", "Des poils", "Des plumes", "Des nageoires"],
            "Un squelette interne avec une colonne vertébrale (ce sont des vertébrés)",
            "Le krill est un crustacé, la littorine et la mye sont des mollusques. Parmi ces vertébrés, seul l'ours a des poils et des mamelles : c'est un mammifère."), ARCTIQUE),
        S('svt', 'Sciences · le réseau trophique arctique', Q(
            "Quelle conséquence la surpêche de la morue polaire peut-elle avoir sur le réseau trophique ?",
            ["Moins de nourriture pour ses prédateurs (phoques, oiseaux, puis ours), et une augmentation possible de ses proies", "Aucune conséquence", "Plus de phoques et d'ours", "La disparition immédiate de la banquise"],
            "Moins de nourriture pour ses prédateurs (phoques, oiseaux, puis ours), et une augmentation possible de ses proies",
            "Dans un réseau trophique, retirer une espèce perturbe celles qui la mangent et celles qu'elle mange : les espèces sont interdépendantes."), ARCTIQUE),
        S('technologie', 'Sciences · la propulsion de la base', Q(
            "Dans un système de propulsion « moteur, réducteur, axe, hélice », quel est le rôle du réducteur ?",
            ["Adapter la vitesse de rotation du moteur avant de la transmettre à l'hélice", "Produire l'énergie électrique", "Transformer la rotation en poussée dans l'eau", "Diriger le bateau"],
            "Adapter la vitesse de rotation du moteur avant de la transmettre à l'hélice",
            "Le moteur convertit l'énergie en rotation, le réducteur adapte la vitesse (et augmente le couple), l'axe transmet le mouvement, l'hélice crée la poussée dans l'eau."), ARCTIQUE),
        S('technologie', 'Sciences · la démarche technologique', Q(
            "Défi : « réaliser un bateau qui avance tout seul ». Quel critère simple les élèves peuvent-ils utiliser pour comparer les prototypes ?",
            ["La distance parcourue (ou la durée) sur un trajet donné, dans les mêmes conditions", "La couleur du bateau", "Le nombre de matériaux utilisés", "L'avis de chaque élève sur la beauté du bateau"],
            "La distance parcourue (ou la durée) sur un trajet donné, dans les mêmes conditions",
            "Un critère mesurable permet de tester et de valider une solution, comme le demande la démarche technologique au cycle 3 (concevoir, réaliser, tester)."), ARCTIQUE),
        # ── Histoire et EMC ──
        S('histoire_geographie', 'Histoire · de 1789 à l\'exécution du roi', Q(
            "Quel événement du 14 juillet 1789 est devenu le symbole de la Révolution ?",
            ["La prise de la Bastille", "La Déclaration des droits de l'homme", "L'exécution de Louis XVI", "La fête de la Fédération"], "La prise de la Bastille",
            "Le peuple parisien s'empare de la forteresse-prison, symbole de l'arbitraire royal. Le dossier contenait un dessin de Claude Cholat, l'un des « vainqueurs de la Bastille »."), REVOLUTION),
        S('histoire_geographie', "Histoire · de 1789 à l'exécution du roi", Q(
            "Que décide l'Assemblée dans la nuit du 4 août 1789 ?",
            ["L'abolition des privilèges", "La proclamation de la République", "L'exécution du roi", "La création des départements"], "L'abolition des privilèges",
            "Les privilèges de la noblesse et du clergé sont abolis ; le 26 août est adoptée la Déclaration des droits de l'homme et du citoyen."), REVOLUTION),
        S('histoire_geographie', "Histoire · de 1789 à l'exécution du roi", Q(
            "Quand la Première République est-elle proclamée ?",
            ["En septembre 1792", "En juillet 1789", "En janvier 1793", "En 1848"], "En septembre 1792",
            "La Convention abolit la royauté le 21 septembre 1792 ; le 22 septembre devient le premier jour de l'an I de la République (décrets cités dans le dossier)."), REVOLUTION),
        S('histoire_geographie', "Histoire · de 1789 à l'exécution du roi", Q(
            "À quelle date Louis XVI est-il guillotiné ?",
            ["Le 21 janvier 1793", "Le 14 juillet 1789", "Le 10 août 1792", "Le 9 thermidor an II (1794)"], "Le 21 janvier 1793",
            "Il est exécuté sur la place de la Révolution, l'actuelle place de la Concorde, à Paris. Le repère de CM1 s'intitule « De l'année 1789 à l'exécution du roi »."), REVOLUTION),
        S('emc', 'EMC · La Marseillaise', Q(
            "Qui a composé La Marseillaise, et en quelle année ?",
            ["Rouget de Lisle, en 1792", "Hector Berlioz, en 1830", "Victor Hugo, en 1848", "Napoléon Bonaparte, en 1804"], "Rouget de Lisle, en 1792",
            "Composé à Strasbourg sous le titre « Chant de guerre pour l'armée du Rhin », il est popularisé par les volontaires marseillais montant à Paris, d'où son nom."), REVOLUTION),
        S('emc', 'EMC · les symboles de la République', Q(
            "Quel texte fait aujourd'hui de La Marseillaise l'hymne national ?",
            ["La Constitution de 1958 (article 2)", "La Déclaration des droits de l'homme de 1789", "La loi de 1905", "Le Code de l'éducation"], "La Constitution de 1958 (article 2)",
            "L'article 2 cite l'emblème (le drapeau tricolore), l'hymne (La Marseillaise), la devise (Liberté, Égalité, Fraternité) et le principe (gouvernement du peuple, par le peuple et pour le peuple)."), None),
        S('emc', 'EMC · les symboles de la République', Q(
            "Lequel de ces éléments n'est pas un symbole officiel de la République française ?",
            ["La tour Eiffel", "Le drapeau bleu, blanc, rouge", "La Marseillaise", "Marianne"], "La tour Eiffel",
            "Symboles de la République : le drapeau, l'hymne, la devise, Marianne, le 14 Juillet et le coq. La tour Eiffel est un monument célèbre, pas un symbole officiel."), None),
        # ── Arts ──
        S('arts', 'Arts du visuel · cycle 1', Q(
            "Quel motif caractérise l'œuvre de Yayoi Kusama, utilisée dans la séance « Ma citrouille à pois » ?",
            ["Les pois (points ronds) répétés", "Les rayures noires et blanches", "Les carrés de couleurs primaires", "Les coulures de peinture"], "Les pois (points ronds) répétés",
            "L'artiste japonaise (née en 1929) couvre ses œuvres, comme ses citrouilles (« Dancing Pumpkin », 2020), de pois répétés à l'infini."),
          "Dossier d'arts du visuel (petite et moyenne section) : une fiche de préparation « Ma citrouille à pois comme Yayoi Kusama », à analyser."),
        S('arts', 'Arts du visuel · cycle 1', Q(
            "Quel risque présente une séance où les élèves de maternelle doivent faire « une citrouille à pois comme Yayoi Kusama » ?",
            ["La reproduction à l'identique d'un modèle, au détriment de l'exploration et de l'invention", "Les élèves ne connaissent pas les citrouilles", "Les pois sont trop difficiles à dessiner", "L'œuvre est trop ancienne"],
            "La reproduction à l'identique d'un modèle, au détriment de l'exploration et de l'invention",
            "La référence à l'œuvre doit nourrir la pratique sans devenir un modèle à copier : le programme de maternelle insiste sur l'exploration libre et l'expérimentation des outils et des matériaux."),
          "Document 2 : « La référence iconique est une donnée importante du dispositif didactique… » (B.-A. Gaillot)."),
        S('arts', 'Éducation musicale · le chant', Q(
            "Selon les ressources d'accompagnement, comment apprend-on un chant à l'école ?",
            ["Par imitation, phrase par phrase, à partir du modèle vocal de l'enseignant", "En lisant la partition", "En écoutant uniquement l'enregistrement une fois", "En apprenant les paroles par écrit avant de chanter"],
            "Par imitation, phrase par phrase, à partir du modèle vocal de l'enseignant",
            "La voix de l'enseignant sert de modèle ; le chant s'apprend par fragments, avec une mise en voix préalable (échauffement corporel et vocal)."),
          "Dossier d'éducation musicale (CE2) : la chanson « Le troupeau » de Morgan Jourdain (2021) et la ressource Éduscol « Le chant, principes de mise en œuvre »."),
    ]),
    # ── Ajout : questions complémentaires tirées du même sujet ──
    epreuve('Épreuve écrite disciplinaire de français', 20148, [
        S('francais', 'Étude de la langue · accords', Q(
            "« Continuez d'être clair, simple et froid. » Pourquoi ces adjectifs sont-ils au masculin singulier ?",
            ["Ils sont attributs du sujet sous-entendu, le maître (« vous » de politesse) à qui Rousseau s'adresse", "Ils sont invariables", "Ils s'accordent avec « être »", "Ils qualifient l'enfant"],
            "Ils sont attributs du sujet sous-entendu, le maître (« vous » de politesse) à qui Rousseau s'adresse",
            "Avec un « vous » de politesse désignant un seul homme, l'attribut reste au masculin singulier."), ROUSSEAU),
        S('francais', 'Étude de la langue · nature et fonction', Q(
            "« Pour nourrir sa curiosité, ne vous pressez jamais de la satisfaire. » Nature et fonction de « la » ?",
            ["Pronom personnel, COD de « satisfaire » (il reprend « sa curiosité »)", "Article défini", "Pronom personnel, sujet", "Pronom relatif"], "Pronom personnel, COD de « satisfaire » (il reprend « sa curiosité »)",
            "Satisfaire quoi ? la curiosité. Le pronom est placé devant l'infinitif dont il est complément."), ROUSSEAU),
        S('francais', 'Étude de la langue · type et forme', Q(
            "« C'est dans le cœur de l'homme qu'est la vie du spectacle de la nature. » Type et forme ?",
            ["Déclarative ; forme emphatique", "Interrogative ; forme négative", "Injonctive ; forme emphatique", "Exclamative ; forme passive"], "Déclarative ; forme emphatique",
            "« C'est… que » met en relief le complément « dans le cœur de l'homme »."), ROUSSEAU),
        S('francais', 'Étude de la langue · réécriture', Q(
            "Réécrivez avec « ils » : « Si jamais vous substituez dans son esprit l'autorité à la raison, il ne raisonnera plus. »",
            ["Si jamais vous substituez dans leur esprit l'autorité à la raison, ils ne raisonneront plus.", "Si jamais vous substituez dans leurs esprit l'autorité à la raison, ils ne raisonnera plus.", "Si jamais vous substituez dans son esprit l'autorité à la raison, ils ne raisonneront plus.", "Si jamais vous substituez dans leur esprits l'autorité à la raison, ils ne raisonnerons plus."],
            "Si jamais vous substituez dans leur esprit l'autorité à la raison, ils ne raisonneront plus.",
            "Logique distributive : chacun a un esprit, d'où « leur esprit » au singulier (« leurs esprits » serait aussi possible). Le verbe s'accorde : ils raisonneront."), ROUSSEAU),
        S('francais', 'Lexique · formation des mots', Q(
            "Lequel de ces mots est formé avec l'élément « -graphie » (écrire) ?",
            ["Orthographe", "Géologie", "Géomètre", "Géode"], "Orthographe",
            "Ortho- (droit) + -graphe : écrire correctement. Géologie et géomètre sont formés avec géo- (la terre)."), ROUSSEAU),
        S('francais', 'Culture littéraire · Rousseau', Q(
            "À quel siècle et à quel mouvement appartient Rousseau, auteur d'« Émile ou de l'Éducation » (1762) ?",
            ["Au XVIIIe siècle, au temps des Lumières", "Au XVIIe siècle classique", "Au XIXe siècle romantique", "Au XVIe siècle humaniste"], "Au XVIIIe siècle, au temps des Lumières",
            "Avec Voltaire, Diderot ou Montesquieu, Rousseau appartient aux Lumières, qui défendent la raison et l'esprit critique, au cœur du sujet de réflexion."), ROUSSEAU),
        S('francais', 'Compréhension · l\'éducation selon Rousseau', Q(
            "Pour enseigner la géographie, que conseille Rousseau ?",
            ["Montrer d'abord l'objet même, dans la nature, plutôt que des globes et des cartes", "Commencer par apprendre les cartes par cœur", "Lire des récits de voyage", "Faire dessiner des globes"],
            "Montrer d'abord l'objet même, dans la nature, plutôt que des globes et des cartes",
            "« Pourquoi toutes ces représentations ? Que ne commencez-vous par lui montrer l'objet même ! » : l'expérience avant le discours."), ROUSSEAU),
    ]),
    epreuve('Épreuve écrite disciplinaire de mathématiques', 20160, [
        S('mathematiques', 'Exercice 2 · heures et durées', Q(
            "Le bateau B avance à 14,04 km/h sur 96 km et part à 8 h 30. À quelle heure arrive-t-il, à la minute près ?",
            ["15 h 20", "14 h 54", "15 h 10", "14 h 20"], "15 h 20",
            "96 ÷ 14,04 ≈ 6,838 h, soit 6 h 50 min (0,838 × 60 ≈ 50). 8 h 30 + 6 h 50 = 15 h 20."), REGATE),
        S('mathematiques', 'Exercice 2 · classement', Q(
            "Bateau A : 15 km/h ; bateau B : 3,9 m/s ; bateau C : 14,5 km/h. Quel est le classement ?",
            ["A, puis C, puis B", "B, puis A, puis C", "C, puis A, puis B", "A, puis B, puis C"], "A, puis C, puis B",
            "3,9 m/s = 14,04 km/h. Il faut comparer des vitesses dans la même unité."), REGATE),
        S('mathematiques', 'Exercice 4 · statistiques', N(
            "Rallye : 9 km (126 élèves), 11 km (120), 12 km (140), 15 km (34). Quelle est la distance moyenne, en km, arrondie au centième ?", 11.06,
            "4 644 km ÷ 420 élèves ≈ 11,06 km.", tol=0.005), RALLYE),
        S('mathematiques', 'Exercice 4 · aires', N(
            "Un quart de disque a un rayon de 0,6 m. Quelle est son aire, en m², arrondie au centième ?", 0.28,
            "π × 0,6² ÷ 4 = π × 0,36 ÷ 4 ≈ 0,28 m².", tol=0.005), None),
        S('mathematiques', 'Exercice 3 · fonctions', Q(
            "f(x) = −2x + … et g(x) = 7x sont des fonctions dont les droites se coupent en A. Comment trouver l'abscisse de A ?",
            ["Résoudre l'équation f(x) = g(x)", "Calculer f(0)", "Calculer g(0)", "Additionner f(x) et g(x)"], "Résoudre l'équation f(x) = g(x)",
            "Le point d'intersection a la même image par les deux fonctions. On reporte ensuite l'abscisse trouvée dans g pour obtenir l'ordonnée."), None),
    ]),
    epreuve("Épreuve écrite d'application (sciences, histoire-géographie-EMC ou arts)", 20172, [
        S('physique_chimie', 'Sciences · la formation de la banquise', Q(
            "Quelle différence voit-on entre la courbe de solidification de l'eau déminéralisée et celle de l'eau salée ?",
            ["L'eau pure a un palier à 0 °C ; l'eau salée n'a pas de palier net et se solidifie en dessous de 0 °C", "Elles sont identiques", "L'eau salée gèle au-dessus de 0 °C", "L'eau pure ne gèle pas"],
            "L'eau pure a un palier à 0 °C ; l'eau salée n'a pas de palier net et se solidifie en dessous de 0 °C",
            "Un corps pur change d'état à température constante ; un mélange, non. C'est pourquoi l'eau de mer gèle vers −1,8 °C."), ARCTIQUE),
        S('physique_chimie', "Sciences · l'effet d'albédo", Q(
            "Qu'est-ce que l'albédo ?",
            ["La part du rayonnement solaire renvoyée par une surface", "La température de l'océan", "La masse de la banquise", "Un gaz à effet de serre"], "La part du rayonnement solaire renvoyée par une surface",
            "La neige et la glace ont un fort albédo (elles renvoient beaucoup de lumière) ; l'océan sombre, un faible albédo. La fonte de la banquise accélère donc le réchauffement."), ARCTIQUE),
        S('physique_chimie', "Sciences · l'effet d'albédo", Q(
            "Dans l'expérience des récipients noir et blanc, quel est le seul paramètre qui doit varier ?",
            ["La couleur de la surface", "La quantité d'eau", "La durée d'exposition", "La température de départ"], "La couleur de la surface",
            "Même quantité d'eau, même température initiale, même éclairage, même durée : on ne change qu'un facteur pour pouvoir conclure."), ARCTIQUE),
        S('svt', "Sciences · le réseau trophique arctique", Q(
            "Dans l'Arctique, quels êtres vivants sont à la base du réseau trophique ?",
            ["Les algues microscopiques (dont celles de la glace de mer)", "Les ours polaires", "Les baleines", "Les phoques"], "Les algues microscopiques (dont celles de la glace de mer)",
            "Producteurs primaires, elles fabriquent leur matière par photosynthèse. L'ours polaire est un superprédateur, au sommet."), ARCTIQUE),
        S('svt', "Sciences · la classification", Q(
            "Un élève dit que l'ours polaire est plus proche de la morue que du macareux parce qu'ils vivent tous deux dans l'eau. Quelle est l'erreur ?",
            ["Il classe selon le milieu de vie, et non selon les attributs partagés", "Il a raison", "Il confond l'ours et le phoque", "Il oublie que la morue est un mammifère"],
            "Il classe selon le milieu de vie, et non selon les attributs partagés",
            "L'ours et le macareux partagent par exemple des poumons et des membres : ils sont plus proches entre eux que de la morue. Un document organisé par milieux peut induire cette erreur."), ARCTIQUE),
        S('svt', "Sciences · actions humaines", Q(
            "Pourquoi des polluants peuvent-ils se retrouver en forte concentration chez les ours polaires et les populations qui mangent des animaux marins ?",
            ["Ils s'accumulent le long des chaînes alimentaires (bioaccumulation)", "Ils sont produits par les ours", "Ils viennent de la glace pure", "Ils disparaissent dans l'eau"],
            "Ils s'accumulent le long des chaînes alimentaires (bioaccumulation)",
            "Chaque prédateur concentre les polluants de ses proies : les espèces au sommet en contiennent le plus."), ARCTIQUE),
        S('technologie', 'Sciences · la base scientifique Tara Polar', Q(
            "Dans la propulsion « moteur, réducteur, axe, hélice », quel élément transforme la rotation en poussée dans l'eau ?",
            ["L'hélice", "Le moteur", "Le réducteur", "L'axe"], "L'hélice",
            "Le moteur produit la rotation, le réducteur adapte la vitesse, l'axe transmet le mouvement, l'hélice pousse l'eau et fait avancer le bateau."), ARCTIQUE),
        S('technologie', 'Sciences · la démarche technologique', Q(
            "Dans quel ordre se déroule la démarche technologique en classe ?",
            ["Identifier le besoin, imaginer des solutions, réaliser un prototype, le tester, l'améliorer", "Tester, puis imaginer, puis identifier le besoin", "Réaliser sans réfléchir, puis tester", "Lire une notice et la recopier"],
            "Identifier le besoin, imaginer des solutions, réaliser un prototype, le tester, l'améliorer",
            "Pour le défi « un bateau qui avance tout seul », les élèves comparent ensuite leurs prototypes selon un critère mesurable."), ARCTIQUE),
        S('histoire_geographie', "Histoire · de 1789 à l'exécution du roi", Q(
            "Quel texte, adopté le 26 août 1789, proclame que « les hommes naissent et demeurent libres et égaux en droits » ?",
            ["La Déclaration des droits de l'homme et du citoyen", "La Constitution de 1958", "Le serment du Jeu de paume", "Le Code civil"], "La Déclaration des droits de l'homme et du citoyen",
            "Elle pose les grands principes de la Révolution : liberté, égalité devant la loi, souveraineté de la nation."), REVOLUTION),
        S('histoire_geographie', "Histoire · de 1789 à l'exécution du roi", Q(
            "Pourquoi la Révolution est-elle une rupture avec l'ordre monarchique ?",
            ["Le pouvoir ne vient plus de Dieu et du roi, mais de la nation, et les privilèges sont abolis", "Le roi garde tous ses pouvoirs", "La noblesse devient plus puissante", "L'Église gouverne le pays"],
            "Le pouvoir ne vient plus de Dieu et du roi, mais de la nation, et les privilèges sont abolis",
            "De la monarchie absolue de droit divin à la République : c'est l'enjeu du repère de CM1 « De l'année 1789 à l'exécution du roi »."), REVOLUTION),
        S('histoire_geographie', "Histoire · de 1789 à l'exécution du roi", Q(
            "Que se passe-t-il le 20 juin 1789 dans la salle du Jeu de paume ?",
            ["Les députés du tiers état jurent de ne pas se séparer avant d'avoir donné une Constitution à la France", "Le roi est arrêté", "La Bastille est prise", "La République est proclamée"],
            "Les députés du tiers état jurent de ne pas se séparer avant d'avoir donné une Constitution à la France",
            "C'est le serment du Jeu de paume, peu après la transformation des États généraux en Assemblée nationale."), None),
        S('emc', 'EMC · La Marseillaise', Q(
            "Sous quel titre La Marseillaise a-t-elle d'abord été composée, en 1792 ?",
            ["Chant de guerre pour l'armée du Rhin", "Hymne à la joie", "Le Chant du départ", "La Carmagnole"], "Chant de guerre pour l'armée du Rhin",
            "Elle doit son nom aux volontaires marseillais qui la chantèrent en montant à Paris. Elle devient hymne national en 1795."), REVOLUTION),
        S('emc', 'EMC · La Marseillaise', Q(
            "Avec des élèves de CP, comment aborder La Marseillaise ?",
            ["L'écouter, en apprendre le premier couplet et le refrain, comprendre qu'elle est un symbole de la République et l'attitude à avoir quand on l'entend", "Analyser toutes les paroles mot à mot", "La faire recopier", "Ne pas en parler"],
            "L'écouter, en apprendre le premier couplet et le refrain, comprendre qu'elle est un symbole de la République et l'attitude à avoir quand on l'entend",
            "Au CP, on part de situations vécues (une cérémonie, un match) et l'on relie l'hymne aux autres symboles : drapeau, devise, Marianne."), REVOLUTION),
        S('arts', 'Arts du visuel · cycle 1', Q(
            "Selon le programme de maternelle, qu'attend-on d'une activité d'arts du visuel en petite ou moyenne section ?",
            ["Que les enfants explorent librement outils, matériaux et gestes, et découvrent des œuvres", "Qu'ils reproduisent exactement une œuvre", "Qu'ils apprennent l'histoire de l'art", "Qu'ils colorient sans dépasser"],
            "Que les enfants explorent librement outils, matériaux et gestes, et découvrent des œuvres",
            "La référence à une artiste comme Yayoi Kusama nourrit l'imaginaire ; elle ne doit pas devenir un modèle à copier."), None),
        S('arts', 'Éducation musicale · le chant', Q(
            "Pourquoi commencer une séance de chant par une mise en voix ?",
            ["Pour préparer le corps et la voix : posture, respiration, échauffement vocal", "Pour occuper le temps", "Pour évaluer les élèves", "Pour choisir un soliste"],
            "Pour préparer le corps et la voix : posture, respiration, échauffement vocal",
            "C'est une étape recommandée par les ressources « Le chant, principes de mise en œuvre » citées dans le dossier."), None),
    ]),
]
