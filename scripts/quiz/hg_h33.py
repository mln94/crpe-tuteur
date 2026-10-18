# Histoire 3e · Françaises et Français dans une République repensée : au moins 50 questions par niveau
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Facile ══
notion('H3-3', 0, F, 'hg3-gprf', [
  Q("Qui dirige le Gouvernement provisoire de la République française à la Libération ?", ["Le général de Gaulle", "Philippe Pétain", "Vincent Auriol", "Pierre Laval"], "Le général de Gaulle", "Il démissionne en janvier 1946."),
  Q("Comment appelle-t-on le gouvernement qui dirige la France de 1944 à 1946 ?", ["Le Gouvernement provisoire de la République française (GPRF)", "Le régime de Vichy", "La Ve République", "Le Directoire"], "Le Gouvernement provisoire de la République française (GPRF)", "Il rétablit la République."),
  Q("Quel régime est déclaré « nul et non avenu » à la Libération ?", ["Le régime de Vichy", "La IIIe République", "La IVe République", "Le Second Empire"], "Le régime de Vichy", "Pour de Gaulle, la République n'a jamais cessé d'exister."),
]),
notion('H3-3', 0, F, 'hg3-secu', [
  Q("À quoi sert la Sécurité sociale ?", ["À protéger contre la maladie, la vieillesse et les accidents du travail", "À assurer la défense du pays", "À organiser les élections", "À gérer la police"], "À protéger contre la maladie, la vieillesse et les accidents du travail", "Elle repose sur la solidarité."),
  Q("Quel ministre communiste met en place la Sécurité sociale en 1945-1946 ?", ["Ambroise Croizat", "Maurice Thorez", "Jean Moulin", "Pierre Mendès France"], "Ambroise Croizat", "Le haut fonctionnaire Pierre Laroque y contribue aussi."),
  Q("Qu'est-ce que les allocations familiales ?", ["Une aide versée aux familles avec enfants", "Un impôt sur les familles", "Une amende", "Une prime aux soldats"], "Une aide versée aux familles avec enfants", "Elles soutiennent la natalité."),
]),
notion('H3-3', 0, F, 'hg3-baby-boom', [
  Q("Comment appelle-t-on la forte hausse des naissances après 1945 ?", ["Le baby-boom", "L'exode rural", "Le papy-boom", "La transition démographique"], "Le baby-boom", "Il dure jusqu'au milieu des années 1960."),
  Q("Comment évolue la population française pendant les Trente Glorieuses ?", ["Elle augmente fortement", "Elle diminue", "Elle reste stable", "Elle est divisée par deux"], "Elle augmente fortement", "Elle passe d'environ 40 à plus de 50 millions."),
  Q("Pourquoi la France fait-elle appel à des travailleurs immigrés après la guerre ?", ["Pour reconstruire et faire tourner les usines", "Pour peupler les colonies", "Pour remplacer les soldats", "Pour faire baisser la natalité"], "Pour reconstruire et faire tourner les usines", "Ils viennent d'Italie, d'Espagne, du Portugal et du Maghreb."),
]),
notion('H3-3', 1, F, 'hg3-constitution-1958', [
  Q("Comment la Constitution de 1958 est-elle adoptée ?", ["Par référendum", "Par le roi", "Par l'armée", "Sans vote"], "Par référendum", "Près de 80 % de « oui »."),
  Q("Qui rédige pour l'essentiel la Constitution de 1958 avec de Gaulle ?", ["Michel Debré", "Georges Pompidou", "Jean Monnet", "René Coty"], "Michel Debré", "Il devient le premier Premier ministre de la Ve République."),
  Q("Quel pouvoir la Ve République renforce-t-elle ?", ["Le pouvoir du président de la République", "Le pouvoir du Parlement seul", "Le pouvoir des préfets", "Le pouvoir du roi"], "Le pouvoir du président de la République", "Le régime de la IVe République était jugé instable."),
]),
notion('H3-3', 1, F, 'hg3-institutions', [
  Q("Qui nomme le Premier ministre ?", ["Le président de la République", "Les députés", "Le Sénat", "Le Conseil constitutionnel"], "Le président de la République", "Le Premier ministre dirige le gouvernement."),
  Q("Comment s'appellent les deux assemblées du Parlement français ?", ["L'Assemblée nationale et le Sénat", "Le Conseil d'État et la Cour des comptes", "Le gouvernement et le Sénat", "L'Élysée et Matignon"], "L'Assemblée nationale et le Sénat", "Elles votent les lois."),
  Q("Où réside le président de la République ?", ["Au palais de l'Élysée", "À l'hôtel Matignon", "Au palais Bourbon", "Au palais du Luxembourg"], "Au palais de l'Élysée", "Matignon est la résidence du Premier ministre."),
]),
notion('H3-3', 1, F, 'hg3-presidents', [
  Q("Qui est président de la République de 1981 à 1995 ?", ["François Mitterrand", "Jacques Chirac", "Valéry Giscard d'Estaing", "Georges Pompidou"], "François Mitterrand", "Il fait deux septennats."),
  Q("Quel président est élu en 2007 ?", ["Nicolas Sarkozy", "François Hollande", "Jacques Chirac", "Emmanuel Macron"], "Nicolas Sarkozy", "Il succède à Jacques Chirac."),
  Q("Quel président est élu en 2017 ?", ["Emmanuel Macron", "François Hollande", "Nicolas Sarkozy", "Marine Le Pen"], "Emmanuel Macron", "Il est réélu en 2022."),
]),
notion('H3-3', 1, F, 'hg3-referendum', [
  Q("Qu'est-ce qu'un référendum ?", ["Un vote où les citoyens répondent par oui ou non à une question", "L'élection des députés", "Une manifestation", "Une loi votée par le Sénat"], "Un vote où les citoyens répondent par oui ou non à une question", "C'est une forme de démocratie directe."),
  Q("Pourquoi de Gaulle démissionne-t-il en 1969 ?", ["Après l'échec d'un référendum", "Après une défaite militaire", "Pour raison de santé", "Après un coup d'État"], "Après l'échec d'un référendum", "Il portait sur la régionalisation et le Sénat."),
  Q("Qui élit le président de la République depuis 1962 ?", ["Tous les citoyens électeurs", "Les députés", "Les maires", "Les sénateurs"], "Tous les citoyens électeurs", "C'est le suffrage universel direct."),
]),
notion('H3-3', 2, F, 'hg3-trente-glorieuses', [
  Q("Quelle période de forte croissance économique suit la Seconde Guerre mondiale en France ?", ["Les Trente Glorieuses", "La Belle Époque", "Les Années folles", "La Grande Dépression"], "Les Trente Glorieuses", "De 1945 à 1975 environ."),
  Q("Quel objet se répand dans les foyers français dans les années 1960 et change les loisirs ?", ["La télévision", "Le smartphone", "Le phonographe", "Le télégraphe"], "La télévision", "Il n'y a d'abord qu'une seule chaîne."),
  Q("Quelle voiture populaire symbolise l'accès à l'automobile dans les années 1950 ?", ["La 2 CV Citroën", "La Ferrari", "La Tesla", "La Bugatti"], "La 2 CV Citroën", "La 4 CV Renault est aussi très populaire."),
]),
notion('H3-3', 2, F, 'hg3-consommation', [
  Q("Comment appelle-t-on une société où l'on achète de plus en plus de biens ?", ["Une société de consommation", "Une société d'ordres", "Une société féodale", "Une société rurale"], "Une société de consommation", "Elle se développe pendant les Trente Glorieuses."),
  N("En quelle année ouvre le premier hypermarché en France ?", 1963, "Il ouvre à Sainte-Geneviève-des-Bois."),
  Q("Quels équipements ménagers se diffusent dans les foyers pendant les Trente Glorieuses ?", ["Réfrigérateur et machine à laver", "Ordinateur et smartphone", "Cheminée et lavoir", "Rouet et métier à tisser"], "Réfrigérateur et machine à laver", "Ils allègent les tâches domestiques."),
]),
notion('H3-3', 2, F, 'hg3-simone-veil', [
  Q("Quelle ministre de la Santé fait voter la loi autorisant l'IVG en 1975 ?", ["Simone Veil", "Édith Cresson", "Gisèle Halimi", "Simone de Beauvoir"], "Simone Veil", "Elle est rescapée d'Auschwitz."),
  Q("Quelle fonction Simone Veil occupe-t-elle à partir de 1979 ?", ["Présidente du Parlement européen", "Présidente de la République", "Première ministre", "Maire de Paris"], "Présidente du Parlement européen", "C'est la première présidente élue au suffrage universel."),
  N("En quelle année Simone Veil entre-t-elle au Panthéon ?", 2018, "Elle y repose avec son mari Antoine."),
]),
notion('H3-3', 2, F, 'hg3-ecole-masse', [
  Q("Quel collège unique est créé en 1975 ?", ["Le collège unique pour tous les élèves (réforme Haby)", "Un collège réservé aux garçons", "Un collège militaire", "Un collège privé"], "Le collège unique pour tous les élèves (réforme Haby)", "Tous les élèves suivent le même cursus après le primaire."),
  Q("Jusqu'à quel âge l'instruction est-elle obligatoire depuis 1959 ?", ["16 ans", "13 ans", "18 ans", "11 ans"], "16 ans", "C'est la réforme Berthoin."),
  Q("Comment évolue le nombre de bacheliers à partir des années 1960 ?", ["Il augmente très fortement", "Il diminue", "Il reste stable", "Le bac est supprimé"], "Il augmente très fortement", "On parle de démocratisation scolaire."),
]),
notion('H3-3', 2, F, 'hg3-loisirs-vacances', [
  Q("Combien de semaines de congés payés les salariés obtiennent-ils en 1982 ?", ["Cinq", "Deux", "Trois", "Huit"], "Cinq", "Deux semaines en 1936, trois en 1956, quatre en 1969."),
  Q("Quelle durée légale du travail hebdomadaire est fixée en 1982 ?", ["39 heures", "40 heures", "35 heures", "48 heures"], "39 heures", "Les 35 heures arrivent en 2000."),
  Q("Quel âge de départ à la retraite est fixé en 1982 ?", ["60 ans", "65 ans", "55 ans", "70 ans"], "60 ans", "Il sera ensuite repoussé."),
]),
notion('H3-3', 0, F, 'hg3-nationalisations', [
  Q("Que signifie « nationaliser » une entreprise ?", ["La faire passer sous le contrôle de l'État", "La vendre à l'étranger", "La fermer", "La diviser en petites entreprises"], "La faire passer sous le contrôle de l'État", "C'est le cas de Renault, de la SNCF ou d'EDF."),
  Q("Quelle entreprise publique de l'électricité est créée en 1946 ?", ["EDF", "TotalEnergies", "Orange", "Air France"], "EDF", "Électricité de France."),
  Q("Pourquoi l'État nationalise-t-il des entreprises à la Libération ?", ["Pour reconstruire le pays et punir la collaboration de certains patrons", "Pour les vendre ensuite", "Pour supprimer les emplois", "Pour plaire aux États-Unis"], "Pour reconstruire le pays et punir la collaboration de certains patrons", "Renault est nationalisé pour faits de collaboration."),
]),
notion('H3-3', 1, F, 'hg3-alternance', [
  Q("Qu'est-ce que l'alternance politique ?", ["Le passage du pouvoir d'une majorité à une autre par les élections", "Un coup d'État", "Une guerre civile", "Un changement de Constitution"], "Le passage du pouvoir d'une majorité à une autre par les élections", "La première grande alternance de la Ve République a lieu en 1981."),
  Q("Quel parti remporte les élections de 1981 avec Mitterrand ?", ["Le Parti socialiste", "Le RPR", "Le Parti radical", "Le Front national"], "Le Parti socialiste", "La gauche gouverne pour la première fois sous la Ve République."),
  Q("Quel président est élu en 2012 ?", ["François Hollande", "Nicolas Sarkozy", "Emmanuel Macron", "Jacques Chirac"], "François Hollande", "C'est une nouvelle alternance."),
]),
# ══ Intermédiaire ══
notion('H3-3', 0, I, 'hg3i-vote-femmes-details', [
  Q("Quel texte de 1944 accorde le droit de vote aux femmes ?", ["L'ordonnance du 21 avril 1944", "La Constitution de 1958", "La loi Veil", "Le Code civil"], "L'ordonnance du 21 avril 1944", "Elle est prise par le Comité français de libération nationale à Alger."),
  Q("Lors de quelles élections les Françaises votent-elles pour la première fois, en avril 1945 ?", ["Les élections municipales", "L'élection présidentielle", "Les élections européennes", "Un référendum sur l'euro"], "Les élections municipales", "Elles votent ensuite aux législatives d'octobre 1945."),
  Q("Combien de femmes sont élues députées en 1945 ?", ["33", "0", "300", "3"], "33", "Elles sont environ 5 % des élus."),
]),
notion('H3-3', 0, I, 'hg3i-programme-cnr', [
  Q("Comment s'intitule le programme du CNR adopté en mars 1944 ?", ["« Les Jours heureux »", "« Liberté, égalité, fraternité »", "« Travail, Famille, Patrie »", "« Le Changement »"], "« Les Jours heureux »", "Il prépare la France d'après-guerre."),
  Q("Quelles mesures prévoit le programme du CNR ?", ["Sécurité sociale, nationalisations, retour aux libertés", "Retour de la monarchie", "Abolition du suffrage universel", "Fin de l'école publique"], "Sécurité sociale, nationalisations, retour aux libertés", "Il est largement appliqué en 1944-1946."),
  Q("Quel organisme de planification est créé en 1946 sous la direction de Jean Monnet ?", ["Le Commissariat général du Plan", "La Banque de France", "Le Conseil constitutionnel", "La CECA"], "Le Commissariat général du Plan", "Il oriente la reconstruction."),
]),
notion('H3-3', 0, I, 'hg3i-ive-republique-instabilite', [
  Q("Quel défaut est souvent reproché à la IVe République ?", ["L'instabilité gouvernementale", "Un président trop puissant", "L'absence d'élections", "Une monarchie déguisée"], "L'instabilité gouvernementale", "Elle connaît 24 gouvernements en 12 ans."),
  Q("Quel président du Conseil met fin à la guerre d'Indochine en 1954 ?", ["Pierre Mendès France", "Guy Mollet", "Antoine Pinay", "Robert Schuman"], "Pierre Mendès France", "Il reste moins de huit mois au pouvoir."),
  Q("Quel événement provoque la chute de la IVe République ?", ["La crise algérienne de mai 1958", "La défaite de 1940", "Mai 68", "La crise de 1929"], "La crise algérienne de mai 1958", "De Gaulle est rappelé au pouvoir."),
]),
notion('H3-3', 1, I, 'hg3i-de-gaulle-politique', [
  Q("Quelle politique de Gaulle mène-t-il vis-à-vis des États-Unis ?", ["Une politique d'indépendance nationale", "Un alignement total", "Une rupture diplomatique", "Une alliance militaire exclusive"], "Une politique d'indépendance nationale", "La France quitte le commandement intégré de l'OTAN en 1966."),
  N("En quelle année la France fait-elle exploser sa première bombe atomique ?", 1960, "C'est la naissance de la force de dissuasion."),
  Q("Comment appelle-t-on la force nucléaire française ?", ["La force de dissuasion (force de frappe)", "La ligne Maginot", "La Grande Armée", "La force d'interposition"], "La force de dissuasion (force de frappe)", "Elle garantit l'indépendance de la France."),
]),
notion('H3-3', 1, I, 'hg3i-conseil-constitutionnel', [
  Q("Quel est le rôle du Conseil constitutionnel ?", ["Vérifier que les lois respectent la Constitution", "Élire le président", "Juger les crimes", "Diriger le gouvernement"], "Vérifier que les lois respectent la Constitution", "Il est créé en 1958."),
  Q("Combien de membres nommés compte le Conseil constitutionnel ?", ["Neuf", "Cinq", "Quinze", "Cent"], "Neuf", "Les anciens présidents en sont membres de droit."),
  Q("Quelle réforme de 2008 permet aux citoyens de contester une loi devant le Conseil constitutionnel lors d'un procès ?", ["La question prioritaire de constitutionnalité (QPC)", "Le référendum d'initiative citoyenne", "Le quinquennat", "La parité"], "La question prioritaire de constitutionnalité (QPC)", "Elle est en place depuis 2010."),
]),
notion('H3-3', 1, I, 'hg3i-quinquennat', [
  N("En quelle année un référendum réduit-il le mandat présidentiel à cinq ans ?", 2000, "Le quinquennat s'applique à partir de 2002."),
  Q("Combien de mandats consécutifs un président peut-il exercer depuis la révision de 2008 ?", ["Deux", "Un", "Trois", "Sans limite"], "Deux", "Cette limite est une nouveauté."),
  Q("Pourquoi les élections législatives suivent-elles la présidentielle depuis 2002 ?", ["Pour donner une majorité au président élu", "Pour remplacer le Sénat", "Pour choisir le Premier ministre directement", "Par hasard"], "Pour donner une majorité au président élu", "Cela limite les cohabitations."),
]),
notion('H3-3', 1, I, 'hg3i-decentralisation', [
  Q("Quelles lois de 1982 donnent plus de pouvoirs aux collectivités locales ?", ["Les lois de décentralisation (lois Defferre)", "Les lois Ferry", "Les lois Auroux", "Les lois Veil"], "Les lois de décentralisation (lois Defferre)", "Le pouvoir du préfet est réduit."),
  Q("Quelles collectivités deviennent de véritables collectivités territoriales en 1982 ?", ["Les régions", "Les cantons", "Les provinces", "Les arrondissements"], "Les régions", "Leurs conseillers sont élus à partir de 1986."),
  Q("Qui exerce désormais le pouvoir exécutif dans le département ?", ["Le président du conseil départemental", "Le préfet seul", "Le maire du chef-lieu", "Le Premier ministre"], "Le président du conseil départemental", "Avant 1982, c'était le préfet."),
]),
notion('H3-3', 2, I, 'hg3i-feminisme-1970', [
  Q("Quel mouvement féministe naît en France en 1970 ?", ["Le MLF (Mouvement de libération des femmes)", "Les suffragettes", "La Ligue des droits de l'homme", "Le MRP"], "Le MLF (Mouvement de libération des femmes)", "Il dépose une gerbe à la femme du Soldat inconnu."),
  Q("Quel texte de 1971, signé par 343 femmes, réclame le droit à l'avortement ?", ["Le manifeste des 343", "L'appel du 18 Juin", "J'accuse…!", "Le Deuxième Sexe"], "Le manifeste des 343", "Les signataires déclarent avoir avorté, ce qui est alors illégal."),
  Q("Quelle avocate défend en 1972 une jeune fille poursuivie pour avortement lors du procès de Bobigny ?", ["Gisèle Halimi", "Simone Veil", "Robert Badinter", "Christiane Taubira"], "Gisèle Halimi", "Le procès prépare la loi Veil."),
]),
notion('H3-3', 2, I, 'hg3i-femmes-droits-civils', [
  N("En quelle année les femmes mariées peuvent-elles ouvrir un compte bancaire et travailler sans l'autorisation de leur mari ?", 1965, "C'est la réforme des régimes matrimoniaux."),
  Q("Quelle notion remplace la « puissance paternelle » en 1970 ?", ["L'autorité parentale", "L'autorité maritale", "Le droit d'aînesse", "La tutelle"], "L'autorité parentale", "Les deux parents décident ensemble."),
  N("En quelle année le divorce par consentement mutuel est-il instauré ?", 1975, "Il simplifie les procédures."),
]),
notion('H3-3', 2, I, 'hg3i-immigration', [
  Q("Quel quartier d'habitat précaire accueille de nombreux immigrés près de Paris dans les années 1960 ?", ["Les bidonvilles (comme celui de Nanterre)", "Les quartiers haussmanniens", "Les cités-jardins", "Les châteaux"], "Les bidonvilles (comme celui de Nanterre)", "Ils sont résorbés dans les années 1970."),
  Q("Quelle marche de 1983, partie de Marseille, réclame l'égalité et dénonce le racisme ?", ["La marche pour l'égalité et contre le racisme", "La marche du sel", "La marche sur Rome", "La marche des femmes sur Versailles"], "La marche pour l'égalité et contre le racisme", "Les médias l'appellent la « marche des Beurs »."),
  Q("Que décide le gouvernement en 1974 face à la crise ?", ["Il suspend l'immigration de travail", "Il ouvre totalement les frontières", "Il rétablit le travail forcé", "Il expulse tous les immigrés"], "Il suspend l'immigration de travail", "Le regroupement familial est autorisé en 1976."),
]),
notion('H3-3', 2, I, 'hg3i-crise-1970', [
  Q("Quel phénomène économique s'installe en France à partir du milieu des années 1970 ?", ["Le chômage de masse", "Le plein-emploi", "La croissance de 10 % par an", "Une pénurie de main-d'œuvre"], "Le chômage de masse", "Il dépasse 2 millions au début des années 1980."),
  Q("Quelles régions industrielles sont touchées par la fermeture des mines et de la sidérurgie ?", ["Le Nord et la Lorraine", "La Côte d'Azur et la Corse", "La Bretagne et la Normandie", "Paris intra-muros"], "Le Nord et la Lorraine", "On parle de désindustrialisation."),
  Q("Comment appelle-t-on la nouvelle pauvreté qui apparaît dans les années 1980 ?", ["La « nouvelle pauvreté » et l'exclusion", "La misère ouvrière du XIXe", "La pauvreté rurale du Moyen Âge", "La famine"], "La « nouvelle pauvreté » et l'exclusion", "Les Restos du cœur sont créés en 1985 par Coluche."),
]),
notion('H3-3', 2, I, 'hg3i-urbanisation', [
  Q("Comment appelle-t-on les grands ensembles d'immeubles construits dans les années 1950-1970 ?", ["Les grands ensembles (HLM)", "Les hôtels particuliers", "Les corons", "Les bastides"], "Les grands ensembles (HLM)", "Ils répondent à la crise du logement."),
  Q("Quel prêtre lance un appel en faveur des sans-abri pendant l'hiver 1954 ?", ["L'abbé Pierre", "Jean-Paul II", "Mère Teresa", "Sœur Emmanuelle"], "L'abbé Pierre", "Il fonde Emmaüs."),
  Q("Quelle part des Français vit en ville en 1975 ?", ["Environ les trois quarts", "Environ un quart", "Environ la moitié", "Presque tous"], "Environ les trois quarts", "Elle était d'environ la moitié en 1945."),
]),
notion('H3-3', 1, I, 'hg3i-mai-68-suite', [
  Q("Quelle décision de Gaulle prend-il pour sortir de la crise de mai 1968 ?", ["Il dissout l'Assemblée nationale", "Il démissionne aussitôt", "Il déclare la guerre", "Il suspend la Constitution"], "Il dissout l'Assemblée nationale", "Les gaullistes remportent largement les élections de juin."),
  Q("Quel slogan célèbre est associé à mai 1968 ?", ["« Il est interdit d'interdire »", "« Travail, Famille, Patrie »", "« Enrichissez-vous »", "« Yes we can »"], "« Il est interdit d'interdire »", "Il exprime le refus de l'autorité."),
  Q("Quel quartier parisien est le cœur de la révolte étudiante de 1968 ?", ["Le Quartier latin", "La Défense", "Montmartre", "Le Marais"], "Le Quartier latin", "Des barricades y sont dressées."),
]),
# ══ Avancé ══
notion('H3-3', 0, D, 'hg3d-constitution-1946', [
  Q("Comment la Constitution de la IVe République est-elle adoptée ?", ["Par référendum, en octobre 1946, après l'échec d'un premier projet", "Par décret de De Gaulle", "Par le Sénat seul", "Sans vote"], "Par référendum, en octobre 1946, après l'échec d'un premier projet", "Le premier projet a été rejeté en mai 1946."),
  Q("Quel discours de 1946 expose les idées constitutionnelles de De Gaulle ?", ["Le discours de Bayeux", "L'appel du 18 Juin", "Le discours de Phnom Penh", "Le discours de Brazzaville"], "Le discours de Bayeux", "Il y défend un exécutif fort."),
  Q("Quel est le premier président de la IVe République ?", ["Vincent Auriol", "René Coty", "Charles de Gaulle", "Albert Lebrun"], "Vincent Auriol", "Il est élu en 1947."),
]),
notion('H3-3', 0, D, 'hg3d-tripartisme', [
  Q("Comment appelle-t-on l'alliance de gouvernement de 1946-1947 entre communistes, socialistes et démocrates-chrétiens ?", ["Le tripartisme", "Le Front populaire", "L'Union sacrée", "La cohabitation"], "Le tripartisme", "Le PCF, la SFIO et le MRP."),
  Q("Pourquoi les ministres communistes sont-ils renvoyés du gouvernement en mai 1947 ?", ["Dans le contexte de la guerre froide et de grèves", "Pour corruption", "À cause d'une guerre", "Pour avoir trahi la Résistance"], "Dans le contexte de la guerre froide et de grèves", "Ils ne reviendront au gouvernement qu'en 1981."),
  Q("Quel parti est le premier parti de France en voix à la Libération ?", ["Le Parti communiste français", "Le RPF", "Le Parti radical", "Le Front national"], "Le Parti communiste français", "Il est surnommé le « parti des 75 000 fusillés »."),
]),
notion('H3-3', 0, D, 'hg3d-comite-entreprise', [
  Q("Quel organisme de 1945 représente les familles auprès des pouvoirs publics ?", ["L'Union nationale des associations familiales (UNAF)", "La CAF seulement", "Le Planning familial", "L'Unédic"], "L'Union nationale des associations familiales (UNAF)", "La politique familiale est une priorité."),
  Q("Quelle école est créée en 1945 pour former les hauts fonctionnaires ?", ["L'École nationale d'administration (ENA)", "L'École polytechnique", "Sciences Po", "L'École normale supérieure"], "L'École nationale d'administration (ENA)", "Elle est remplacée par l'INSP en 2022."),
  Q("Quel organisme de recherche est développé à la Libération pour l'énergie atomique ?", ["Le Commissariat à l'énergie atomique (CEA)", "Le CNRS", "L'INSERM", "Le CNES"], "Le Commissariat à l'énergie atomique (CEA)", "Il est créé en 1945."),
]),
notion('H3-3', 0, D, 'hg3d-femmes-resistance-politique', [
  Q("Combien de femmes sont faites compagnons de la Libération ?", ["Six", "Soixante", "Six cents", "Aucune"], "Six", "Sur 1 038 compagnons."),
  Q("Quelles résistantes entrent au Panthéon en 2015 ?", ["Germaine Tillion et Geneviève de Gaulle-Anthonioz", "Lucie Aubrac et Simone Veil", "Joséphine Baker et Marie Curie", "Louise Michel et George Sand"], "Germaine Tillion et Geneviève de Gaulle-Anthonioz", "Avec Pierre Brossolette et Jean Zay."),
  Q("Quelle artiste et résistante entre au Panthéon en 2021 ?", ["Joséphine Baker", "Édith Piaf", "Simone Signoret", "Juliette Gréco"], "Joséphine Baker", "Elle était aussi engagée contre le racisme."),
]),
notion('H3-3', 1, D, 'hg3d-pouvoirs-president', [
  Q("Quel pouvoir permet au président de dissoudre l'Assemblée nationale ?", ["L'article 12 de la Constitution", "L'article 16", "L'article 49-3", "L'article 1er"], "L'article 12 de la Constitution", "Il ne peut le faire qu'une fois par an."),
  Q("Quel « domaine » est traditionnellement réservé au président sous la Ve République ?", ["La défense et la politique étrangère", "L'éducation", "La santé", "Les transports"], "La défense et la politique étrangère", "On parle de « domaine réservé »."),
  Q("Que peut faire l'Assemblée nationale pour renverser le gouvernement ?", ["Voter une motion de censure", "Destituer le président directement", "Dissoudre le Sénat", "Organiser un référendum"], "Voter une motion de censure", "C'est très rare : en 1962, puis en 2024."),
]),
notion('H3-3', 1, D, 'hg3d-cohabitations', [
  Q("Qui est Premier ministre lors de la première cohabitation (1986-1988) ?", ["Jacques Chirac", "Édouard Balladur", "Lionel Jospin", "Michel Rocard"], "Jacques Chirac", "Sous la présidence de Mitterrand."),
  Q("Qui est Premier ministre lors de la cohabitation de 1993-1995 ?", ["Édouard Balladur", "Jacques Chirac", "Lionel Jospin", "Alain Juppé"], "Édouard Balladur", "Mitterrand est encore président."),
  Q("Quelle est la plus longue cohabitation de la Ve République ?", ["Chirac président, Jospin Premier ministre (1997-2002)", "Mitterrand-Chirac", "Mitterrand-Balladur", "Macron-Philippe"], "Chirac président, Jospin Premier ministre (1997-2002)", "Elle dure cinq ans."),
]),
notion('H3-3', 1, D, 'hg3d-referendums-ve', [
  Q("Sur quoi porte le référendum de 1962 qui approuve l'indépendance de l'Algérie ?", ["Les accords d'Évian", "La Constitution", "Le quinquennat", "Maastricht"], "Les accords d'Évian", "Plus de 90 % de « oui »."),
  Q("Quel attentat contre de Gaulle, en 1962, précède le référendum sur l'élection du président ?", ["L'attentat du Petit-Clamart", "L'attentat de la rue de Rennes", "L'attentat de Charonne", "L'attentat d'Orly"], "L'attentat du Petit-Clamart", "Il est organisé par l'OAS."),
  N("En quelle année a eu lieu le dernier référendum national en France ?", 2005, "Il portait sur la Constitution européenne."),
]),
notion('H3-3', 1, D, 'hg3d-parite', [
  N("En quelle année une loi impose-t-elle la parité des candidatures aux élections ?", 2000, "Elle suit la révision constitutionnelle de 1999."),
  Q("Quelle femme est la première Première ministre en France, en 1991 ?", ["Édith Cresson", "Élisabeth Borne", "Ségolène Royal", "Simone Veil"], "Édith Cresson", "Élisabeth Borne est la deuxième, en 2022."),
  Q("Quelle femme est la première candidate du second tour d'une présidentielle, en 2007 ?", ["Ségolène Royal", "Marine Le Pen", "Arlette Laguiller", "Valérie Pécresse"], "Ségolène Royal", "Elle affronte Nicolas Sarkozy."),
]),
notion('H3-3', 2, D, 'hg3d-lois-societe', [
  Q("Quelle loi de 1972 impose l'égalité de rémunération entre hommes et femmes ?", ["La loi du 22 décembre 1972", "La loi Veil", "La loi Neuwirth", "La loi Roudy"], "La loi du 22 décembre 1972", "Elle reste longtemps peu appliquée."),
  Q("Quelle ministre des Droits de la femme fait voter en 1983 une loi sur l'égalité professionnelle ?", ["Yvette Roudy", "Simone Veil", "Édith Cresson", "Françoise Giroud"], "Yvette Roudy", "Elle fait aussi rembourser l'IVG en 1982."),
  N("En quelle année l'homosexualité est-elle dépénalisée en France ?", 1982, "Le mariage pour tous est voté en 2013."),
]),
notion('H3-3', 2, D, 'hg3d-mutations-agricoles', [
  Q("Comment évolue la part des agriculteurs dans la population active entre 1945 et 1975 ?", ["Elle passe d'environ un tiers à moins de 10 %", "Elle augmente", "Elle reste stable", "Elle double"], "Elle passe d'environ un tiers à moins de 10 %", "On parle de la « fin des paysans »."),
  Q("Quel sociologue publie La Fin des paysans en 1967 ?", ["Henri Mendras", "Pierre Bourdieu", "Jean Fourastié", "Raymond Aron"], "Henri Mendras", "Il décrit la modernisation agricole."),
  Q("Comment appelle-t-on le regroupement des parcelles agricoles pour faciliter la mécanisation ?", ["Le remembrement", "La collectivisation", "La jachère", "Le défrichement"], "Le remembrement", "Il transforme les paysages ruraux."),
]),
notion('H3-3', 2, D, 'hg3d-tertiarisation', [
  Q("Comment appelle-t-on le secteur des services ?", ["Le secteur tertiaire", "Le secteur primaire", "Le secteur secondaire", "Le secteur quaternaire seulement"], "Le secteur tertiaire", "Il emploie la majorité des actifs dès les années 1970."),
  Q("Quel groupe social progresse fortement pendant les Trente Glorieuses ?", ["Les cadres et employés (classes moyennes)", "Les paysans", "Les nobles", "Les artisans ruraux"], "Les cadres et employés (classes moyennes)", "La société se tertiarise."),
  Q("Quelle part des femmes de 25 à 49 ans travaille vers 1990 ?", ["Environ les trois quarts", "Environ un dixième", "Environ un quart", "Toutes"], "Environ les trois quarts", "Le travail féminin progresse fortement depuis les années 1960."),
]),
notion('H3-3', 2, D, 'hg3d-jeunesse-culture', [
  Q("Quelle émission de radio des années 1960 symbolise la culture « yé-yé » ?", ["Salut les copains", "Le Masque et la Plume", "Les Grosses Têtes", "Radio Londres"], "Salut les copains", "Johnny Hallyday et Sylvie Vartan en sont les idoles."),
  Q("Quel concert réunit 150 000 jeunes place de la Nation en 1963 ?", ["Le concert de Salut les copains", "Woodstock", "Live Aid", "La fête de la musique"], "Le concert de Salut les copains", "La jeunesse devient un groupe social à part."),
  N("En quelle année est créée la fête de la Musique ?", 1982, "Elle est lancée par Jack Lang."),
]),
notion('H3-3', 2, D, 'hg3d-contraception', [
  Q("Quel député fait voter la loi autorisant la contraception en 1967 ?", ["Lucien Neuwirth", "Robert Badinter", "Michel Debré", "Jacques Chaban-Delmas"], "Lucien Neuwirth", "Les décrets d'application tardent jusqu'en 1972."),
  Q("Quelle association, fondée en 1956 sous le nom de « Maternité heureuse », milite pour la contraception ?", ["Le Planning familial", "Emmaüs", "Les Restos du cœur", "SOS Racisme"], "Le Planning familial", "Il prend ce nom en 1960."),
  Q("Quel ouvrage de Simone de Beauvoir (1949) est un texte fondateur du féminisme ?", ["Le Deuxième Sexe", "Les Mandarins", "La Force de l'âge", "Mémoires d'une jeune fille rangée"], "Le Deuxième Sexe", "« On ne naît pas femme, on le devient »."),
]),
notion('H3-3', 2, D, 'hg3d-abolition-peine-mort', [
  N("En quelle année a lieu la dernière exécution capitale en France ?", 1977, "Hamida Djandoubi est guillotiné à Marseille."),
  Q("En quelle année l'abolition de la peine de mort est-elle inscrite dans la Constitution ?", ["2007", "1981", "1958", "1995"], "2007", "Elle avait été abolie par la loi en 1981."),
  Q("Quel avocat, devenu ministre de la Justice, défend l'abolition devant l'Assemblée en 1981 ?", ["Robert Badinter", "Gisèle Halimi", "Jacques Vergès", "Christiane Taubira"], "Robert Badinter", "Il entre au Panthéon en 2025."),
]),
]
