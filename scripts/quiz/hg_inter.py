from qlib import Q, N, C, notion
I = 'intermediaire'
NOTIONS = [
notion('H5-1', 0, I, 'hg-traite-verdun-843', [
  N("En quelle année le traité de Verdun partage-t-il l'empire carolingien entre les petits-fils de Charlemagne ?", 843, "Le traité de Verdun (843) partage l'empire en trois royaumes entre Charles le Chauve, Lothaire et Louis le Germanique."),
  Q("Entre combien de royaumes l'empire carolingien est-il partagé en 843 ?", ["Deux", "Trois", "Quatre", "Cinq"], "Trois", "Francie occidentale, Francie médiane (Lotharingie) et Francie orientale."),
  Q("Quel royaume issu du partage de 843 est à l'origine de la France ?", ["La Francie occidentale", "La Francie orientale", "La Lotharingie", "La Bourgogne"], "La Francie occidentale", "La Francie occidentale, attribuée à Charles le Chauve, est le noyau du futur royaume de France."),
]),
notion('H5-1', 1, I, 'hg-bagdad-mongols', [
  N("En quelle année les Mongols prennent-ils Bagdad, mettant fin au califat abbasside ?", 1258, "En 1258, les Mongols de Hulagu prennent et pillent Bagdad ; le dernier calife abbasside est exécuté."),
  Q("Quel peuple met fin au califat abbasside de Bagdad en 1258 ?", ["Les Turcs ottomans", "Les Mongols", "Les croisés", "Les Perses sassanides"], "Les Mongols", "L'invasion mongole marque la fin du califat abbasside de Bagdad."),
  Q("Pourquoi Bagdad est-elle un grand centre culturel sous les Abbassides ?", ["Elle est la capitale du Saint-Empire", "Elle accueille savants et traducteurs, comme à la Maison de la sagesse", "Elle est fondée par les Romains", "Elle est la ville sainte du christianisme"], "Elle accueille savants et traducteurs, comme à la Maison de la sagesse", "On y traduit des œuvres grecques et persanes, et les sciences (mathématiques, astronomie, médecine) s'y développent."),
]),
notion('H5-1', 1, I, 'hg-croisades', [
  N("En quelle année le pape Urbain II appelle-t-il à la première croisade ?", 1095, "Au concile de Clermont (1095), Urbain II appelle les chrétiens à partir délivrer Jérusalem."),
  Q("Quelle ville est l'objectif principal de la première croisade ?", ["Constantinople", "Jérusalem", "Bagdad", "Damas"], "Jérusalem", "Les croisés prennent Jérusalem en 1099."),
  Q("Comment appelle-t-on les États fondés par les croisés en Orient ?", ["Les États latins d'Orient", "Les califats chrétiens", "Les comptoirs", "Les thèmes byzantins"], "Les États latins d'Orient", "Le royaume de Jérusalem, le comté d'Édesse, la principauté d'Antioche et le comté de Tripoli."),
]),
notion('H5-2', 0, I, 'hg-prelevements-seigneur', [
  Q("Comment appelle-t-on l'impôt versé à l'Église, environ un dixième des récoltes ?", ["La taille", "La dîme", "La gabelle", "Le cens"], "La dîme", "La dîme est prélevée par l'Église ; la taille et le cens sont dus au seigneur ou au roi."),
  Q("Comment appelle-t-on les taxes que les paysans paient pour utiliser le moulin, le four ou le pressoir du seigneur ?", ["Les banalités", "Les dîmes", "Les octrois", "Les aides"], "Les banalités", "Le seigneur impose l'usage payant de ses équipements : ce sont les banalités."),
  Q("Quel est le statut d'un serf au Moyen Âge ?", ["Un paysan libre", "Un paysan non libre, attaché à la terre du seigneur", "Un chevalier", "Un marchand"], "Un paysan non libre, attaché à la terre du seigneur", "Le serf ne peut quitter la seigneurie ni se marier sans l'autorisation du seigneur."),
]),
notion('H5-2', 1, I, 'hg-communes-medievales', [
  Q("Comment appelle-t-on le document par lequel un seigneur accorde des libertés à une ville ?", ["Une charte de franchise", "Une bulle pontificale", "Un cahier de doléances", "Un capitulaire"], "Une charte de franchise", "La charte reconnaît aux habitants le droit de s'administrer et limite les prélèvements du seigneur."),
  Q("Comment appelle-t-on les associations d'artisans d'un même métier au Moyen Âge ?", ["Les guildes ou corporations", "Les confréries militaires", "Les ordres mendiants", "Les parlements"], "Les guildes ou corporations", "Les corporations réglementent le métier : apprentissage, qualité, prix."),
  Q("Quels nouveaux ordres religieux, comme les franciscains, s'installent dans les villes au XIIIe siècle ?", ["Les ordres mendiants", "Les ordres militaires", "Les chanoines ruraux", "Les ermites"], "Les ordres mendiants", "Franciscains et dominicains vivent de la charité et prêchent en ville."),
]),
notion('H5-2', 2, I, 'hg-etat-monarchique', [
  Q("Quel roi entre en conflit avec le pape Boniface VIII et réunit des états généraux en 1302 ?", ["Philippe Auguste", "Philippe le Bel", "Louis IX", "Charles V"], "Philippe le Bel", "Philippe IV le Bel affirme l'indépendance du roi face au pape."),
  Q("Sous Charles VII, quelles institutions renforcent durablement l'État royal ?", ["Une armée et un impôt permanents", "Un Parlement élu", "La séparation des pouvoirs", "Le suffrage universel"], "Une armée et un impôt permanents", "La taille devient un impôt permanent et une armée permanente est créée au XVe siècle."),
  Q("Comment appelle-t-on les agents qui administrent le domaine royal pour le roi capétien ?", ["Les baillis et sénéchaux", "Les intendants", "Les préfets", "Les ducs"], "Les baillis et sénéchaux", "Créés sous Philippe Auguste, baillis et sénéchaux rendent la justice et lèvent les revenus du roi."),
]),
notion('H5-3', 0, I, 'hg-charles-quint-soliman', [
  Q("Quel empire Soliman le Magnifique dirige-t-il au XVIe siècle ?", ["L'Empire byzantin", "L'Empire ottoman", "L'Empire perse", "L'Empire moghol"], "L'Empire ottoman", "Soliman (1520-1566) porte l'Empire ottoman à son apogée ; il assiège Vienne en 1529."),
  Q("Pourquoi dit-on que sur l'empire de Charles Quint « le soleil ne se couche jamais » ?", ["Il ne contrôle que l'Europe", "Il règne sur des territoires en Europe et en Amérique", "Il vit en Orient", "Il contrôle l'Asie"], "Il règne sur des territoires en Europe et en Amérique", "Charles Quint hérite de l'Espagne et de ses possessions américaines, des Pays-Bas et du Saint-Empire."),
  Q("Quel roi de France s'allie avec Soliman le Magnifique contre Charles Quint ?", ["Henri IV", "François Ier", "Louis XIII", "Charles IX"], "François Ier", "François Ier conclut avec l'Empire ottoman une alliance contre leur adversaire commun, Charles Quint."),
]),
notion('H5-3', 1, I, 'hg-humanisme', [
  Q("Quel humaniste hollandais écrit l'Éloge de la folie ?", ["Montaigne", "Érasme", "Rabelais", "Thomas More"], "Érasme", "Érasme (vers 1467-1536) est l'une des grandes figures de l'humanisme européen."),
  Q("Quel est l'objectif principal des humanistes ?", ["Revenir aux textes antiques et placer l'homme au centre de la réflexion", "Abandonner l'étude du grec et du latin", "Interdire l'imprimerie", "Rejeter toute forme de savoir"], "Revenir aux textes antiques et placer l'homme au centre de la réflexion", "Les humanistes étudient les auteurs grecs et latins et ont confiance dans l'éducation et la raison humaine."),
  Q("Qui fonde l'Église protestante dite réformée à Genève ?", ["Luther", "Calvin", "Zwingli seul", "Henri VIII"], "Calvin", "Jean Calvin organise à Genève une Église réformée, dont se réclament les protestants français."),
]),
notion('H5-3', 2, I, 'hg-henri-iv', [
  Q("Quel roi met fin aux guerres de Religion en France ?", ["Henri III", "Henri IV", "Louis XIII", "Charles IX"], "Henri IV", "Henri IV, protestant converti au catholicisme, signe l'édit de Nantes en 1598."),
  Q("Quelle phrase est traditionnellement attribuée à Henri IV lors de sa conversion ?", ["« L'État, c'est moi »", "« Paris vaut bien une messe »", "« Après moi le déluge »", "« Je suis le roi de France »"], "« Paris vaut bien une messe »", "Henri IV se convertit au catholicisme en 1593 pour être accepté comme roi par les Parisiens."),
  Q("Quel cardinal, principal ministre de Louis XIII, renforce le pouvoir royal ?", ["Mazarin", "Richelieu", "Fleury", "Colbert"], "Richelieu", "Richelieu (ministre de 1624 à 1642) lutte contre les protestants et les grands nobles."),
]),
notion('H4-1', 0, I, 'hg-code-noir-esclavage', [
  N("En quelle année est promulgué le Code noir qui encadre l'esclavage dans les colonies françaises ?", 1685, "Le Code noir (1685) considère l'esclave comme un bien meuble appartenant au maître."),
  Q("Quel produit colonial est au cœur de l'économie des plantations des Antilles au XVIIIe siècle ?", ["Le blé", "Le sucre", "La laine", "Le charbon"], "Le sucre", "Le sucre de canne, produit par des esclaves, fait la richesse de Saint-Domingue et des négociants."),
  Q("Quelle colonie française, la plus riche du XVIIIe siècle, devient indépendante en 1804 sous le nom d'Haïti ?", ["La Martinique", "Saint-Domingue", "La Guadeloupe", "La Louisiane"], "Saint-Domingue", "La révolte des esclaves menée notamment par Toussaint Louverture aboutit à l'indépendance d'Haïti."),
]),
notion('H4-1', 1, I, 'hg-philosophes-lumieres', [
  Q("Quel philosophe défend la séparation des pouvoirs dans De l'esprit des lois ?", ["Voltaire", "Montesquieu", "Rousseau", "Diderot"], "Montesquieu", "Montesquieu (1748) distingue les pouvoirs législatif, exécutif et judiciaire, qui doivent être séparés."),
  Q("Quel philosophe écrit Du contrat social (1762) et défend la souveraineté du peuple ?", ["Voltaire", "Rousseau", "Montesquieu", "Condorcet"], "Rousseau", "Jean-Jacques Rousseau affirme que la souveraineté appartient au peuple."),
  Q("Dans quels lieux les idées des Lumières circulent-elles beaucoup au XVIIIe siècle ?", ["Uniquement dans les églises", "Dans les salons, les cafés et les académies", "Dans les corporations", "Dans les monastères"], "Dans les salons, les cafés et les académies", "Salons, cafés, académies et journaux diffusent les idées nouvelles."),
]),
notion('H4-1', 2, I, 'hg-etats-generaux-1789', [
  Q("Quels sont les trois ordres de la société d'Ancien Régime ?", ["Noblesse, bourgeoisie, peuple", "Clergé, noblesse, tiers état", "Roi, nobles, paysans", "Clergé, armée, tiers état"], "Clergé, noblesse, tiers état", "Le tiers état rassemble plus de 95 % de la population, sans privilèges."),
  Q("Que décident les députés du tiers état lors du serment du Jeu de paume (20 juin 1789) ?", ["De dissoudre l'Assemblée", "De ne pas se séparer avant d'avoir donné une Constitution à la France", "De rétablir les privilèges", "D'élire un empereur"], "De ne pas se séparer avant d'avoir donné une Constitution à la France", "Les députés, réunis dans la salle du Jeu de paume, jurent de rédiger une Constitution."),
  Q("Dans quels documents les Français expriment-ils leurs plaintes avant les états généraux de 1789 ?", ["Les cahiers de doléances", "Les cahiers des charges", "Les registres paroissiaux", "Les lettres de cachet"], "Les cahiers de doléances", "Chaque communauté rédige un cahier de doléances pour présenter ses demandes au roi."),
]),
notion('H4-2', 0, I, 'hg-societe-industrielle', [
  Q("Comment appelle-t-on le départ massif des habitants des campagnes vers les villes au XIXe siècle ?", ["L'exode rural", "La périurbanisation", "La rurbanisation", "La néo-ruralité"], "L'exode rural", "Les paysans quittent les campagnes pour travailler dans les usines des villes."),
  Q("Comment appelle-t-on la classe sociale des ouvriers qui ne possèdent que leur force de travail ?", ["La bourgeoisie", "Le prolétariat", "L'aristocratie", "La paysannerie"], "Le prolétariat", "Les ouvriers forment le prolétariat ; les patrons et investisseurs appartiennent à la bourgeoisie."),
  Q("Qui publie avec Engels le Manifeste du Parti communiste en 1848 ?", ["Proudhon", "Karl Marx", "Jaurès", "Lénine"], "Karl Marx", "Marx analyse la société comme une lutte entre bourgeoisie et prolétariat."),
]),
notion('H4-2', 1, I, 'hg-partage-afrique', [
  Q("Quelle conférence de 1884-1885 fixe des règles pour le partage de l'Afrique entre puissances européennes ?", ["La conférence de Yalta", "La conférence de Berlin", "Le congrès de Vienne", "La conférence de Bandung"], "La conférence de Berlin", "La conférence de Berlin organise la course aux colonies en Afrique."),
  Q("Comment appelle-t-on, dans une colonie, une population dominée et privée de droits politiques ?", ["Des citoyens", "Des indigènes (sujets coloniaux)", "Des colons", "Des métropolitains"], "Des indigènes (sujets coloniaux)", "Les colonisés sont soumis au régime de l'indigénat, sans les droits des citoyens."),
  Q("Quel argument les colonisateurs avancent-ils souvent pour justifier la colonisation au XIXe siècle ?", ["L'égalité des peuples", "Une prétendue « mission civilisatrice »", "Le droit des peuples à disposer d'eux-mêmes", "La lutte contre la mondialisation"], "Une prétendue « mission civilisatrice »", "Cet argument, fondé sur l'idée de supériorité européenne, masque la domination et l'exploitation."),
]),
notion('H4-3', 0, I, 'hg-second-empire', [
  N("En quelle année Louis-Napoléon Bonaparte fait-il un coup d'État ?", 1851, "Le coup d'État du 2 décembre 1851 met fin à la IIe République ; l'Empire est rétabli en 1852."),
  Q("Sous quel nom Louis-Napoléon Bonaparte règne-t-il à partir de 1852 ?", ["Napoléon II", "Napoléon III", "Louis XVIII", "Charles X"], "Napoléon III", "Le Second Empire dure de 1852 à 1870."),
  Q("Quel type de suffrage existe sous la Restauration et la monarchie de Juillet (1815-1848) ?", ["Le suffrage universel", "Le suffrage censitaire", "Le suffrage féminin", "Aucun vote"], "Le suffrage censitaire", "Seuls les hommes payant un certain montant d'impôt (le cens) peuvent voter."),
]),
notion('H4-3', 1, I, 'hg-affaire-dreyfus', [
  Q("De quoi le capitaine Dreyfus est-il accusé à tort en 1894 ?", ["De vol", "D'espionnage au profit de l'Allemagne", "D'assassinat", "De désertion"], "D'espionnage au profit de l'Allemagne", "Condamné à tort, Dreyfus est victime d'une erreur judiciaire nourrie par l'antisémitisme."),
  Q("Quel écrivain publie « J'accuse… ! » en 1898 pour défendre Dreyfus ?", ["Victor Hugo", "Émile Zola", "Anatole France", "Jean Jaurès"], "Émile Zola", "Dans L'Aurore, Zola dénonce les responsables de la condamnation injuste de Dreyfus."),
  Q("Quelle loi votée sous la IIIe République établit la laïcité de l'État en 1905 ?", ["La loi Ferry", "La loi de séparation des Églises et de l'État", "La loi Falloux", "La loi Waldeck-Rousseau"], "La loi de séparation des Églises et de l'État", "La loi du 9 décembre 1905 garantit la liberté de conscience et sépare les Églises de l'État."),
]),
notion('H4-3', 2, I, 'hg-conditions-feminines-xixe', [
  Q("Selon le Code civil de 1804, quelle est la situation juridique de la femme mariée ?", ["Elle est l'égale de son mari", "Elle doit obéissance à son mari et dépend de lui juridiquement", "Elle peut voter", "Elle gère seule ses biens"], "Elle doit obéissance à son mari et dépend de lui juridiquement", "Le Code civil place la femme mariée sous l'autorité du mari."),
  Q("Quelle militante féministe de la fin du XIXe siècle réclame le droit de vote des femmes ?", ["Hubertine Auclert", "Olympe de Gouges", "Simone Veil", "Simone de Beauvoir"], "Hubertine Auclert", "Hubertine Auclert, figure du suffragisme français, milite pour le vote des femmes dès les années 1870-1880."),
  Q("Qui écrit la Déclaration des droits de la femme et de la citoyenne en 1791 ?", ["Olympe de Gouges", "Madame Roland", "George Sand", "Louise Michel"], "Olympe de Gouges", "Olympe de Gouges réclame l'égalité des droits entre femmes et hommes ; elle est guillotinée en 1793."),
]),
notion('H3-1', 0, I, 'hg-violence-de-masse-1914', [
  Q("Quel peuple est victime d'un génocide perpétré par l'Empire ottoman en 1915 ?", ["Les Kurdes", "Les Arméniens", "Les Grecs seulement", "Les Juifs"], "Les Arméniens", "Le génocide des Arméniens (1915-1916) fait environ 1,2 à 1,5 million de victimes."),
  Q("Comment appelle-t-on la mobilisation de toutes les ressources d'un pays (économie, population) pendant la Première Guerre mondiale ?", ["La guerre éclair", "La guerre totale", "La guerre froide", "La drôle de guerre"], "La guerre totale", "Toute la société participe à l'effort de guerre : soldats, ouvrières, propagande, économie."),
  Q("Comment appelle-t-on les soldats français de la Première Guerre mondiale ?", ["Les grognards", "Les poilus", "Les sans-culottes", "Les maquisards"], "Les poilus", "Le surnom de « poilus » désigne les soldats français des tranchées."),
]),
notion('H3-1', 1, I, 'hg-entre-deux-guerres', [
  Q("Quelle crise économique commence en 1929 aux États-Unis ?", ["La crise des subprimes", "La Grande Dépression", "Le choc pétrolier", "La crise de la dette"], "La Grande Dépression", "Le krach boursier d'octobre 1929 à Wall Street déclenche une crise mondiale."),
  Q("Quelle coalition de gauche gouverne la France en 1936 et accorde les congés payés ?", ["Le Bloc national", "Le Front populaire", "Le Cartel des gauches", "L'Union sacrée"], "Le Front populaire", "Le gouvernement de Léon Blum fait voter les congés payés et la semaine de 40 heures."),
  N("En quelle année Hitler devient-il chancelier d'Allemagne ?", 1933, "Hitler est nommé chancelier le 30 janvier 1933 et installe rapidement une dictature."),
]),
notion('H3-1', 2, I, 'hg-tournants-1942-1945', [
  Q("Quelle bataille de 1942-1943 marque un tournant de la guerre sur le front de l'Est ?", ["Verdun", "Stalingrad", "La Marne", "El Alamein"], "Stalingrad", "La capitulation allemande à Stalingrad en février 1943 marque le début du recul allemand à l'Est."),
  N("En quelle année a lieu le débarquement allié en Normandie ?", 1944, "Le 6 juin 1944, les Alliés débarquent en Normandie : c'est le D-Day."),
  Q("Sur quelles villes japonaises les États-Unis lancent-ils des bombes atomiques en août 1945 ?", ["Tokyo et Osaka", "Hiroshima et Nagasaki", "Kyoto et Kobe", "Nagoya et Yokohama"], "Hiroshima et Nagasaki", "Les bombardements des 6 et 9 août 1945 entraînent la capitulation du Japon."),
]),
notion('H3-1', 3, I, 'hg-collaboration', [
  Q("Quelle rafle organisée par la police française en juillet 1942 vise les Juifs de Paris ?", ["La rafle du Vél d'Hiv", "La rafle de Marseille", "La Nuit de Cristal", "La rafle de Lyon"], "La rafle du Vél d'Hiv", "Les 16 et 17 juillet 1942, plus de 13 000 Juifs sont arrêtés, puis déportés."),
  Q("Quel personnage unifie les mouvements de la Résistance intérieure en 1943 ?", ["Jean Moulin", "Pierre Laval", "Philippe Pétain", "Jean Jaurès"], "Jean Moulin", "Envoyé par de Gaulle, Jean Moulin crée le Conseil national de la Résistance en mai 1943."),
  Q("Qu'est-ce que le STO instauré par Vichy en 1943 ?", ["Un service de santé", "Le Service du travail obligatoire en Allemagne", "Un syndicat ouvrier", "Une armée de résistance"], "Le Service du travail obligatoire en Allemagne", "Le STO envoie des jeunes Français travailler en Allemagne ; beaucoup s'y dérobent en rejoignant les maquis."),
]),
notion('H3-2', 0, I, 'hg-independances', [
  N("En quelle année l'Inde devient-elle indépendante ?", 1947, "L'Inde devient indépendante le 15 août 1947, en même temps qu'est créé le Pakistan."),
  Q("Quelle guerre oppose la France au Viêt-minh de 1946 à 1954 ?", ["La guerre d'Algérie", "La guerre d'Indochine", "La guerre de Corée", "La guerre du Vietnam américaine"], "La guerre d'Indochine", "La défaite française à Diên Biên Phu (1954) entraîne la fin de la guerre d'Indochine."),
  Q("Comment appelle-t-on les pays qui refusent de s'aligner sur l'un des deux blocs pendant la guerre froide ?", ["Les pays non alignés", "Les pays satellites", "Les démocraties populaires", "Les pays de l'OTAN"], "Les pays non alignés", "Le mouvement des non-alignés est fondé à Belgrade en 1961, dans la lignée de la conférence de Bandung (1955)."),
]),
notion('H3-2', 1, I, 'hg-crises-guerre-froide', [
  Q("Quelle crise de 1962 met le monde au bord de la guerre nucléaire ?", ["La crise de Berlin", "La crise de Cuba", "La guerre de Corée", "La crise de Suez"], "La crise de Cuba", "L'installation de missiles soviétiques à Cuba provoque une crise majeure en octobre 1962."),
  Q("Quelle alliance militaire est fondée en 1949 autour des États-Unis ?", ["Le pacte de Varsovie", "L'OTAN", "Le Comecon", "L'ONU"], "L'OTAN", "L'Organisation du traité de l'Atlantique Nord réunit les États-Unis et leurs alliés occidentaux."),
  N("En quelle année l'URSS disparaît-elle ?", 1991, "L'URSS est dissoute en décembre 1991, ce qui marque la fin de la guerre froide."),
]),
notion('H3-2', 2, I, 'hg-traites-europeens', [
  N("En quelle année le traité de Maastricht crée-t-il l'Union européenne ?", 1992, "Le traité de Maastricht est signé en 1992 ; il crée l'Union européenne et prévoit la monnaie unique."),
  Q("Quelle communauté créée en 1951 met en commun le charbon et l'acier de six pays ?", ["La CECA", "La CEE", "L'AELE", "L'OTAN"], "La CECA", "La Communauté européenne du charbon et de l'acier est la première étape de la construction européenne."),
  Q("Quel homme politique français propose en 1950 la mise en commun du charbon et de l'acier ?", ["Jean Monnet seul", "Robert Schuman", "Charles de Gaulle", "Jacques Delors"], "Robert Schuman", "La déclaration Schuman du 9 mai 1950 est considérée comme l'acte fondateur de la construction européenne."),
]),
notion('H3-3', 0, I, 'hg-liberation-refondation', [
  N("En quelle année est créée la Sécurité sociale en France ?", 1945, "Les ordonnances d'octobre 1945 créent la Sécurité sociale, inspirée du programme du CNR."),
  Q("Quelle République est fondée en 1946 ?", ["La IIIe République", "La IVe République", "La Ve République", "La IIe République"], "La IVe République", "La IVe République (1946-1958) est un régime parlementaire."),
  Q("Quel principe est inscrit dans le préambule de la Constitution de 1946 ?", ["L'égalité des droits entre femmes et hommes dans tous les domaines", "La monarchie constitutionnelle", "Le suffrage censitaire", "Le droit divin"], "L'égalité des droits entre femmes et hommes dans tous les domaines", "Le préambule de 1946 affirme que « la loi garantit à la femme, dans tous les domaines, des droits égaux à ceux de l'homme »."),
]),
notion('H3-3', 1, I, 'hg-alternance-cohabitation', [
  Q("En 1981, quel président est le premier de gauche élu sous la Ve République ?", ["Valéry Giscard d'Estaing", "François Mitterrand", "Jacques Chirac", "Georges Pompidou"], "François Mitterrand", "L'élection de François Mitterrand en 1981 réalise la première alternance politique de la Ve République."),
  Q("Comment appelle-t-on la situation où le président et le Premier ministre appartiennent à des camps politiques opposés ?", ["L'alternance", "La cohabitation", "La dissolution", "Le référendum"], "La cohabitation", "La première cohabitation a lieu en 1986, entre François Mitterrand et Jacques Chirac."),
  N("En quelle année a lieu la première cohabitation ?", 1986, "Après les législatives de 1986, Jacques Chirac devient Premier ministre de François Mitterrand."),
]),
notion('G5-1', 0, I, 'geo-transition-demographique', [
  Q("Comment appelle-t-on le passage d'une forte natalité et forte mortalité à une faible natalité et faible mortalité ?", ["L'exode rural", "La transition démographique", "Le vieillissement", "L'accroissement naturel"], "La transition démographique", "Pendant la transition, la mortalité baisse d'abord, puis la natalité : la population augmente fortement."),
  Q("Comment calcule-t-on l'accroissement naturel d'une population ?", ["Naissances − décès", "Naissances + décès", "Immigrés − émigrés", "Population ÷ superficie"], "Naissances − décès", "L'accroissement naturel est la différence entre les naissances et les décès ; le solde migratoire s'y ajoute."),
  Q("Qu'est-ce que l'indice de fécondité ?", ["Le nombre de naissances par an", "Le nombre moyen d'enfants par femme", "Le nombre de décès d'enfants", "La part des jeunes"], "Le nombre moyen d'enfants par femme", "Environ 2,1 enfants par femme assurent le renouvellement des générations dans les pays développés."),
]),
notion('G5-3', 1, I, 'geo-prevention-risques', [
  Q("Quelle catastrophe industrielle frappe Toulouse en 2001 ?", ["Lubrizol", "L'explosion de l'usine AZF", "Seveso", "Tchernobyl"], "L'explosion de l'usine AZF", "L'explosion de l'usine AZF, le 21 septembre 2001, fait 31 morts et des milliers de blessés."),
  Q("Comment appelle-t-on la directive européenne qui classe les sites industriels dangereux ?", ["La directive Seveso", "La directive Natura 2000", "La directive Schengen", "La directive nitrates"], "La directive Seveso", "Elle tire son nom de la catastrophe de Seveso en Italie (1976) et impose des mesures de prévention."),
  Q("Quel document réglemente l'urbanisation dans les zones exposées à un risque naturel ?", ["Le plan de prévention des risques (PPR)", "Le plan local de santé", "Le cadastre", "Le plan Marshall"], "Le plan de prévention des risques (PPR)", "Le PPR peut interdire ou encadrer les constructions dans les zones inondables ou exposées."),
]),
notion('G4-1', 0, I, 'geo-etalement-urbain', [
  Q("Comment appelle-t-on l'extension des villes sur les espaces ruraux qui les entourent ?", ["L'étalement urbain", "La densification", "La gentrification", "La désurbanisation"], "L'étalement urbain", "L'étalement urbain consomme des terres agricoles et augmente les déplacements en voiture."),
  Q("Comment appelle-t-on l'installation de populations aisées dans d'anciens quartiers populaires, qui se transforment ?", ["La ghettoïsation", "La gentrification", "La périurbanisation", "La ruralisation"], "La gentrification", "La gentrification fait monter les prix et peut chasser les habitants modestes."),
  Q("Comment appelle-t-on un quartier résidentiel fermé et surveillé, réservé à des habitants aisés ?", ["Une favela", "Une gated community", "Un grand ensemble", "Un bourg"], "Une gated community", "Ces quartiers fermés illustrent la ségrégation socio-spatiale dans certaines villes."),
]),
notion('G4-3', 0, I, 'geo-detroits-ports', [
  Q("Quel canal relie la mer Méditerranée à la mer Rouge ?", ["Le canal de Panama", "Le canal de Suez", "Le canal de Corinthe", "Le canal de Kiel"], "Le canal de Suez", "Ouvert en 1869, le canal de Suez est un passage essentiel entre l'Europe et l'Asie."),
  Q("Quel est le premier port européen par le trafic de marchandises ?", ["Marseille", "Rotterdam", "Le Havre", "Hambourg"], "Rotterdam", "Rotterdam, aux Pays-Bas, est le premier port d'Europe."),
  Q("Quel détroit sépare l'Europe de l'Afrique ?", ["Le détroit d'Ormuz", "Le détroit de Gibraltar", "Le détroit de Malacca", "Le Bosphore"], "Le détroit de Gibraltar", "Gibraltar relie la Méditerranée à l'Atlantique entre l'Espagne et le Maroc."),
]),
notion('G4-2', 0, I, 'geo-flux-migratoires', [
  Q("Quel pays accueille le plus grand nombre d'immigrés au monde ?", ["La France", "Les États-Unis", "L'Allemagne", "Le Canada"], "Les États-Unis", "Les États-Unis comptent environ 50 millions d'immigrés, le plus grand nombre au monde."),
  Q("Comment appelle-t-on l'argent envoyé par les migrants à leur famille restée au pays ?", ["Les remises (transferts de fonds)", "Les subventions", "Les impôts", "Les dividendes"], "Les remises (transferts de fonds)", "Ces transferts représentent une ressource importante pour de nombreux pays en développement."),
  Q("Quelle part des migrations internationales se fait entre pays du Sud ?", ["Presque aucune", "Une part importante, comparable aux migrations Sud-Nord", "100 %", "Uniquement vers l'Europe"], "Une part importante, comparable aux migrations Sud-Nord", "Les migrations Sud-Sud sont aussi nombreuses que les migrations Sud-Nord ; elles sont souvent moins visibles."),
]),
notion('G3-2', 0, I, 'geo-amenagement', [
  Q("Que signifie « aménager le territoire » ?", ["Construire uniquement des routes", "Organiser l'espace pour réduire les inégalités et favoriser le développement", "Augmenter les impôts locaux", "Déplacer la capitale"], "Organiser l'espace pour réduire les inégalités et favoriser le développement", "L'aménagement du territoire répartit équipements et activités pour corriger les déséquilibres."),
  Q("Quel acteur public a longtemps piloté l'aménagement du territoire en France depuis 1963 ?", ["La DATAR", "L'INSEE", "La SNCF", "L'ONU"], "La DATAR", "La DATAR (1963) a orienté l'aménagement : métropoles d'équilibre, villes nouvelles, stations touristiques."),
  Q("Quel grand projet de transport a réduit les distances-temps entre les grandes villes françaises depuis 1981 ?", ["Le TGV", "Le Concorde", "Les canaux", "Le RER seulement"], "Le TGV", "La ligne Paris-Lyon ouvre en 1981 ; le réseau LGV relie aujourd'hui les grandes métropoles."),
  Q("Comment appelle-t-on les collectivités territoriales qui ont la compétence principale en matière d'aménagement et de transports régionaux ?", ["Les communes", "Les régions", "Les cantons", "Les préfectures"], "Les régions", "Depuis la décentralisation, les régions ont des compétences majeures en aménagement, transports (TER) et développement économique."),
]),
notion('H3-3', 2, I, 'hg-mai-68', [
  N("En quelle année se déroulent les événements de « Mai 68 » en France ?", 1968, "En mai-juin 1968, une révolte étudiante puis une grève générale secouent la France."),
  Q("Quels accords de mai 1968 entre gouvernement, patronat et syndicats augmentent notamment le salaire minimum ?", ["Les accords de Grenelle", "Les accords de Matignon", "Les accords d'Évian", "Les accords de Schengen"], "Les accords de Grenelle", "Les accords de Grenelle (27 mai 1968) augmentent le SMIG de 35 % et reconnaissent la section syndicale d'entreprise."),
  Q("Quelle loi de 1967 autorise la contraception en France ?", ["La loi Veil", "La loi Neuwirth", "La loi Roudy", "La loi Royer"], "La loi Neuwirth", "La loi Neuwirth (1967) légalise la contraception ; la loi Veil (1975) dépénalise l'IVG."),
]),
]
