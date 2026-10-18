# Histoire : notions ajoutées pour que chaque thème du programme (5e, 4e, 3e) compte au moins 30 questions
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ── 5e · Thème 1 : Chrétientés et islam (VIe-XIIIe siècles), des mondes en contact ──
notion('H5-1', 0, F, 'hg-justinien', [
  Q("Quel empereur byzantin du VIe siècle fait construire la basilique Sainte-Sophie à Constantinople ?", ["Justinien", "Charlemagne", "Constantin", "Clovis"], "Justinien", "Justinien règne de 527 à 565 ; Sainte-Sophie est achevée en 537."),
  Q("Quel titre porte l'empereur byzantin ?", ["Basileus", "Calife", "Pharaon", "Doge"], "Basileus", "Le basileus est à la fois chef politique et protecteur de l'Église."),
  Q("Quelle grande œuvre juridique est réalisée sous Justinien ?", ["Un recueil des lois romaines (le Code Justinien)", "La Déclaration des droits de l'homme", "Le Code civil", "La Grande Charte"], "Un recueil des lois romaines (le Code Justinien)", "Ce code rassemble et organise le droit romain."),
]),
notion('H5-1', 1, I, 'hg-echanges-mediterranee', [
  Q("D'où viennent les chiffres dits « arabes », transmis à l'Europe par le monde musulman ?", ["De l'Inde", "De la Grèce", "De Rome", "De la Chine"], "De l'Inde", "Les savants arabes les ont adoptés puis transmis, avec le zéro."),
  Q("Quel savant persan, auteur du « Canon de la médecine », est lu en Europe pendant des siècles ?", ["Avicenne (Ibn Sina)", "Galilée", "Hippocrate", "Averroès"], "Avicenne (Ibn Sina)", "Son ouvrage est traduit en latin et enseigné dans les universités européennes."),
  Q("Quelle ville d'al-Andalus devient la capitale d'un califat omeyyade en 929 ?", ["Cordoue", "Tolède", "Séville", "Grenade"], "Cordoue", "Cordoue est alors l'une des plus grandes villes d'Europe."),
]),
# ── 5e · Thème 2 : Société, Église et pouvoir politique dans l'Occident féodal ──
notion('H5-2', 0, F, 'hg-chateau-fort', [
  Q("Comment appelle-t-on la grande tour principale d'un château fort ?", ["Le donjon", "Le beffroi", "Le clocher", "Le pont-levis"], "Le donjon", "Le donjon est la résidence du seigneur et le dernier refuge en cas d'attaque."),
  Q("Comment appelle-t-on la cérémonie par laquelle un jeune noble devient chevalier ?", ["L'adoubement", "Le sacre", "Le baptême", "L'hommage"], "L'adoubement", "Il reçoit ses armes, souvent une épée et des éperons."),
  Q("Quelle est la forme des premiers châteaux, aux Xe et XIe siècles ?", ["Une tour en bois sur une butte de terre (motte castrale)", "Un palais de marbre", "Une forteresse de béton", "Une tente de toile"], "Une tour en bois sur une butte de terre (motte castrale)", "Les châteaux en pierre se généralisent ensuite, à partir du XIe siècle."),
]),
notion('H5-2', 0, I, 'hg-defrichements', [
  Q("Comment appelle-t-on la conquête de nouvelles terres agricoles sur la forêt, du XIe au XIIIe siècle ?", ["Les défrichements", "L'exode rural", "Les enclosures", "La transhumance"], "Les défrichements", "Ils accompagnent la forte croissance de la population."),
  Q("Quelle pratique agricole partage les terres en trois parties qui changent de culture chaque année ?", ["L'assolement triennal", "La jachère permanente", "La monoculture", "L'irrigation"], "L'assolement triennal", "Une partie reste en jachère chaque année, ce qui améliore les rendements."),
  Q("Quel outil permet de mieux retourner la terre à partir du XIe siècle ?", ["La charrue à versoir", "Le tracteur", "La houe en bois", "La moissonneuse"], "La charrue à versoir", "Tirée par des animaux, elle laboure plus profondément que l'araire."),
]),
notion('H5-2', 1, I, 'hg-cathedrales-universites', [
  Q("Quel style architectural apparaît au XIIe siècle, avec de hautes cathédrales lumineuses et de grands vitraux ?", ["Le gothique", "Le roman", "Le baroque", "Le classique"], "Le gothique", "Notre-Dame de Paris et Chartres sont des cathédrales gothiques."),
  Q("Quel style précède le gothique, avec des murs épais et des voûtes en plein cintre ?", ["Le roman", "Le baroque", "L'art nouveau", "Le néoclassique"], "Le roman", "L'art roman domine aux XIe et XIIe siècles."),
  Q("Quel collège parisien, fondé vers 1257, a donné son nom à une célèbre université ?", ["La Sorbonne", "Le Collège de France", "Polytechnique", "La Bastille"], "La Sorbonne", "Il est fondé par Robert de Sorbon pour accueillir des étudiants en théologie."),
]),
# ── 5e · Thème 3 : Transformations de l'Europe et ouverture sur le monde aux XVIe et XVIIe siècles ──
notion('H5-3', 2, F, 'hg-francois-ier', [
  N("En quelle année François Ier remporte-t-il la bataille de Marignan ?", 1515, "Marignan (1515) ouvre son règne par une victoire en Italie."),
  Q("Quel artiste italien François Ier invite-t-il en France, où il meurt en 1519 ?", ["Léonard de Vinci", "Michel-Ange", "Raphaël", "Botticelli"], "Léonard de Vinci", "Il s'installe au Clos Lucé, près du château royal d'Amboise."),
  Q("Que décide l'ordonnance de Villers-Cotterêts (1539) ?", ["Les actes officiels sont rédigés en français", "La fin des guerres de Religion", "La création de l'Académie française", "L'abolition du servage"], "Les actes officiels sont rédigés en français", "Le français remplace le latin dans les actes de justice et d'administration."),
]),
notion('H5-3', 0, D, 'hg-conquetes-amerique', [
  Q("Quel conquistador espagnol fait tomber l'Empire aztèque (1519-1521) ?", ["Hernán Cortés", "Francisco Pizarro", "Vasco de Gama", "Magellan"], "Hernán Cortés", "Il prend la capitale Tenochtitlan, à l'emplacement de l'actuelle Mexico."),
  Q("Quel empire d'Amérique du Sud Francisco Pizarro conquiert-il à partir de 1532 ?", ["L'Empire inca", "L'Empire aztèque", "L'Empire maya", "L'Empire ottoman"], "L'Empire inca", "L'empereur inca Atahualpa est capturé puis exécuté."),
  Q("Quel traité de 1494 partage les terres nouvellement découvertes entre l'Espagne et le Portugal ?", ["Le traité de Tordesillas", "Le traité de Verdun", "Le traité de Westphalie", "Le traité d'Utrecht"], "Le traité de Tordesillas", "Une ligne tracée dans l'Atlantique sépare les zones des deux royaumes ; le Brésil revient au Portugal."),
]),
# ── 4e · Thème 2 : L'Europe et le monde au XIXe siècle ──
notion('H4-2', 0, F, 'hg-energies-transports', [
  Q("Quel ingénieur écossais améliore la machine à vapeur à la fin du XVIIIe siècle ?", ["James Watt", "Thomas Edison", "Gustave Eiffel", "Louis Pasteur"], "James Watt", "Son invention rend la vapeur utilisable dans les usines."),
  Q("Quel moyen de transport, développé grâce à la machine à vapeur, réduit les distances au XIXe siècle ?", ["Le chemin de fer", "L'avion", "L'automobile électrique", "La montgolfière"], "Le chemin de fer", "Le réseau ferré se développe dans toute l'Europe à partir des années 1830-1840."),
  Q("Quelles énergies marquent la seconde révolution industrielle, à la fin du XIXe siècle ?", ["L'électricité et le pétrole", "Le charbon et le bois", "Le vent et l'eau", "Le nucléaire et le solaire"], "L'électricité et le pétrole", "Elles s'ajoutent au charbon, énergie de la première révolution industrielle."),
]),
notion('H4-2', 0, F, 'hg-sciences-xixe', [
  Q("Quel savant publie « L'Origine des espèces » en 1859, sur l'évolution des êtres vivants ?", ["Charles Darwin", "Louis Pasteur", "Isaac Newton", "Albert Einstein"], "Charles Darwin", "Sa théorie de la sélection naturelle bouleverse la vision religieuse du monde."),
  Q("Quel savant français met au point le vaccin contre la rage en 1885 ?", ["Louis Pasteur", "Marie Curie", "Claude Bernard", "Pierre Curie"], "Louis Pasteur", "Il sauve le jeune Joseph Meister, mordu par un chien enragé."),
  Q("Pour quelle découverte Marie Curie reçoit-elle le prix Nobel de physique en 1903 ?", ["La radioactivité", "L'électricité", "La pénicilline", "Les rayons du soleil"], "La radioactivité", "Elle le partage avec Pierre Curie et Henri Becquerel ; elle reçoit un second Nobel en 1911."),
]),
notion('H4-2', 0, I, 'hg-question-sociale', [
  Q("Que fait la loi de 1841 en France ?", ["Elle limite le travail des enfants dans les usines", "Elle crée la Sécurité sociale", "Elle donne le droit de vote aux femmes", "Elle abolit l'esclavage"], "Elle limite le travail des enfants dans les usines", "Elle interdit le travail en usine avant 8 ans."),
  N("En quelle année le droit de grève est-il reconnu en France ?", 1864, "La loi Ollivier (1864) supprime le délit de coalition."),
  N("En quelle année la loi Waldeck-Rousseau autorise-t-elle les syndicats en France ?", 1884, "Les ouvriers peuvent désormais s'organiser légalement pour défendre leurs intérêts."),
]),
notion('H4-2', 0, I, 'hg-emigration-xixe', [
  Q("Quelle catastrophe pousse des centaines de milliers d'Irlandais à émigrer entre 1845 et 1852 ?", ["La Grande Famine, due à une maladie de la pomme de terre", "Une guerre civile", "Un tremblement de terre", "La peste"], "La Grande Famine, due à une maladie de la pomme de terre", "Environ un million d'Irlandais meurent et plus d'un million émigrent."),
  Q("Vers quel pays partent la plupart des émigrants européens au XIXe siècle ?", ["Les États-Unis", "La Russie", "La Chine", "L'Australie"], "Les États-Unis", "Ellis Island, à New York, accueille les immigrants à partir de 1892."),
  Q("Quel peuple européen fournit de nombreux émigrants vers l'Amérique et la France à la fin du XIXe siècle ?", ["Les Italiens", "Les Suisses", "Les Britanniques", "Les Suédois"], "Les Italiens", "La pauvreté des campagnes du Sud pousse des millions d'Italiens à partir."),
]),
notion('H4-2', 0, D, 'hg-1848-europe', [
  Q("Comment appelle-t-on la vague de révolutions qui traverse l'Europe en 1848 ?", ["Le printemps des peuples", "La Belle Époque", "La Restauration", "Les Trente Glorieuses"], "Le printemps des peuples", "Des soulèvements éclatent en France, dans les États allemands et italiens, en Autriche et en Hongrie."),
  Q("Quelle idée les révolutionnaires de 1848 défendent-ils en Italie, en Allemagne ou en Hongrie ?", ["Le droit des peuples à former une nation", "Le retour de la monarchie absolue", "La colonisation de l'Afrique", "La fin de l'industrie"], "Le droit des peuples à former une nation", "L'idée de nationalité progresse, même si la plupart des révolutions échouent."),
  Q("Quelle mesure de 1848 cherche à garantir le « droit au travail » aux chômeurs parisiens ?", ["Les ateliers nationaux", "Les congés payés", "Le Code civil", "Les lois Ferry"], "Les ateliers nationaux", "Leur fermeture en juin 1848 provoque une insurrection ouvrière réprimée."),
]),
notion('H4-2', 1, I, 'hg-societe-coloniale', [
  Q("Quel régime juridique, instauré en Algérie en 1881, soumet les colonisés à des règles et sanctions particulières ?", ["Le code de l'indigénat", "Le Code civil", "La Déclaration des droits de l'homme", "Le Concordat"], "Le code de l'indigénat", "Il est ensuite étendu à d'autres colonies françaises."),
  Q("Comment appelle-t-on un Européen installé dans une colonie ?", ["Un colon", "Un indigène", "Un émigré politique", "Un protectorat"], "Un colon", "La société coloniale est marquée par l'inégalité entre colons et colonisés."),
  Q("Quel homme politique justifie en 1885 la colonisation par le « devoir de civiliser » les peuples dits « inférieurs » ?", ["Jules Ferry", "Victor Schœlcher", "Jean Jaurès", "Georges Clemenceau"], "Jules Ferry", "Clemenceau lui répond en dénonçant cette prétendue supériorité."),
]),
notion('H4-2', 1, D, 'hg-empire-colonial-francais', [
  Q("Quelle grande île de l'océan Indien la France conquiert-elle en 1895-1896 ?", ["Madagascar", "La Réunion", "Maurice", "Sri Lanka"], "Madagascar", "L'île devient une colonie française en 1896."),
  Q("Quelle fédération de colonies françaises est créée en Afrique en 1895, avec Dakar pour capitale à partir de 1902 ?", ["L'Afrique-Occidentale française (AOF)", "L'Union indochinoise", "Le Maghreb", "Le Commonwealth"], "L'Afrique-Occidentale française (AOF)", "L'AEF (Afrique-Équatoriale française) est créée en 1910."),
  Q("Quel ensemble colonial français est créé en Asie du Sud-Est en 1887 ?", ["L'Indochine française", "L'Inde française", "Les Philippines", "L'Indonésie"], "L'Indochine française", "Elle regroupe notamment le Tonkin, l'Annam, la Cochinchine et le Cambodge."),
]),
# ── 4e · Thème 3 : Société, culture et politique dans la France du XIXe siècle ──
notion('H4-3', 1, F, 'hg-1870-1871', [
  Q("Quelle défaite de septembre 1870 entraîne la chute de Napoléon III ?", ["Sedan", "Waterloo", "Verdun", "Austerlitz"], "Sedan", "L'empereur est fait prisonnier par les Prussiens."),
  Q("Qui proclame la République à l'Hôtel de Ville de Paris le 4 septembre 1870 ?", ["Léon Gambetta", "Jules Ferry", "Adolphe Thiers", "Victor Hugo"], "Léon Gambetta", "La IIIe République naît en pleine guerre contre la Prusse."),
  Q("Quels territoires la France perd-elle au profit de l'Allemagne en 1871 ?", ["L'Alsace et une partie de la Lorraine (Moselle)", "La Savoie et Nice", "La Corse", "La Bretagne"], "L'Alsace et une partie de la Lorraine (Moselle)", "Le traité de Francfort (1871) les annexe à l'Empire allemand."),
]),
notion('H4-3', 1, I, 'hg-culture-republicaine', [
  N("En quelle année le 14 juillet devient-il fête nationale ?", 1880, "La IIIe République enracine ses symboles : fête nationale, hymne, Marianne."),
  N("En quelle année La Marseillaise devient-elle définitivement l'hymne national ?", 1879, "Composée en 1792, elle avait déjà été hymne national en 1795."),
  Q("Avec les lois Ferry de 1882, jusqu'à quel âge l'instruction est-elle obligatoire ?", ["13 ans", "16 ans", "10 ans", "18 ans"], "13 ans", "L'instruction est obligatoire de 6 à 13 ans ; elle passe à 16 ans en 1959."),
]),
notion('H4-3', 2, F, 'hg-femmes-xixe-vie', [
  Q("Quelle institutrice, figure de la Commune de Paris en 1871, est déportée en Nouvelle-Calédonie ?", ["Louise Michel", "George Sand", "Olympe de Gouges", "Marie Curie"], "Louise Michel", "Elle devient une figure du mouvement ouvrier et anarchiste."),
  Q("En 1900, les Françaises ont-elles le droit de vote ?", ["Non", "Oui, depuis 1848", "Oui, depuis 1789", "Seulement les femmes mariées"], "Non", "Elles l'obtiennent en 1944 et votent pour la première fois en 1945."),
  Q("Quel métier féminin se développe fortement avec l'école de la IIIe République ?", ["Institutrice", "Ingénieure", "Députée", "Magistrate"], "Institutrice", "Les écoles normales forment les institutrices dans chaque département."),
]),
notion('H4-3', 2, D, 'hg-femmes-xixe-droits', [
  Q("Que crée la loi Camille Sée de 1880 ?", ["Des lycées publics de jeunes filles", "Le droit de vote des femmes", "Le divorce", "Les crèches"], "Des lycées publics de jeunes filles", "Leur enseignement ne prépare toutefois pas encore au baccalauréat."),
  Q("Quelle femme est la première à obtenir le baccalauréat en France, en 1861 ?", ["Julie-Victoire Daubié", "Marie Curie", "Louise Michel", "Hubertine Auclert"], "Julie-Victoire Daubié", "Elle doit obtenir une autorisation exceptionnelle pour se présenter."),
  N("En quelle année une loi permet-elle à la femme mariée de disposer librement de son salaire ?", 1907, "Jusque-là, le Code civil de 1804 la plaçait sous l'autorité de son mari."),
]),
# ── 3e · Thème 2 : Le monde depuis 1945 ──
notion('H3-2', 1, D, 'hg-debuts-guerre-froide', [
  Q("Quel plan américain de 1947 aide la reconstruction de l'Europe de l'Ouest ?", ["Le plan Marshall", "Le plan Schuman", "Le New Deal", "Le plan Delors"], "Le plan Marshall", "L'URSS refuse cette aide pour elle et ses pays satellites."),
  Q("Quelle crise de 1948-1949 voit l'URSS couper les accès terrestres à Berlin-Ouest ?", ["Le blocus de Berlin", "La crise de Cuba", "La guerre de Corée", "Le printemps de Prague"], "Le blocus de Berlin", "Les Occidentaux ravitaillent la ville par un pont aérien."),
  Q("Quelle alliance militaire regroupe l'URSS et ses alliés à partir de 1955 ?", ["Le pacte de Varsovie", "L'OTAN", "L'ONU", "La CEE"], "Le pacte de Varsovie", "Il répond à l'OTAN, fondée en 1949."),
]),
notion('H3-2', 3, I, 'hg-cooperation-mondiale', [
  N("En quelle année l'ONU est-elle fondée ?", 1945, "La Charte des Nations unies est signée à San Francisco en juin 1945."),
  Q("Quel accord international sur le climat est adopté lors de la COP21 en 2015 ?", ["L'accord de Paris", "Le protocole de Kyoto", "Le traité de Rome", "Les accords d'Évian"], "L'accord de Paris", "Il vise à limiter le réchauffement nettement en dessous de 2 °C."),
  Q("Quelle grande conférence de 1992, à Rio de Janeiro, popularise le développement durable ?", ["Le Sommet de la Terre", "La conférence de Yalta", "La conférence de Bandung", "Le G7"], "Le Sommet de la Terre", "Il lance notamment la convention des Nations unies sur le climat."),
]),
# ── 3e · Thème 3 : Françaises et Français dans une République repensée ──
notion('H3-3', 0, D, 'hg-reformes-liberation', [
  Q("Quelle grande entreprise automobile est nationalisée en 1945 ?", ["Renault", "Peugeot", "Citroën", "Michelin"], "Renault", "Louis Renault était accusé de collaboration ; l'entreprise devient la Régie Renault."),
  Q("Quelle institution créée en 1945 permet aux salariés d'être représentés dans les entreprises ?", ["Le comité d'entreprise", "Le Sénat", "Le Conseil d'État", "La Cour des comptes"], "Le comité d'entreprise", "Il s'inscrit dans le programme social du Conseil national de la Résistance."),
  Q("Quel type de régime la Constitution de la IVe République (1946) met-elle en place ?", ["Un régime parlementaire", "Une monarchie", "Un régime présidentiel fort", "Une dictature"], "Un régime parlementaire", "L'Assemblée nationale y domine ; l'instabilité gouvernementale est forte."),
]),
notion('H3-3', 1, I, 'hg-presidents-ve', [
  Q("Qui succède au général de Gaulle à la présidence de la République en 1969 ?", ["Georges Pompidou", "Valéry Giscard d'Estaing", "François Mitterrand", "Jacques Chirac"], "Georges Pompidou", "De Gaulle démissionne après l'échec de son référendum d'avril 1969."),
  Q("Quel président est élu en 1974 et fait abaisser la majorité à 18 ans ?", ["Valéry Giscard d'Estaing", "Georges Pompidou", "François Mitterrand", "Jacques Chirac"], "Valéry Giscard d'Estaing", "Son septennat est marqué par des réformes de société."),
  Q("Quel président est élu en 1995 ?", ["Jacques Chirac", "Nicolas Sarkozy", "François Mitterrand", "Lionel Jospin"], "Jacques Chirac", "Il est réélu en 2002 ; le quinquennat s'applique à partir de ce second mandat."),
]),
notion('H3-3', 2, D, 'hg-mutations-societe', [
  Q("Comment l'économiste Jean Fourastié appelle-t-il la période de forte croissance de 1945 à 1975 ?", ["Les Trente Glorieuses", "La Belle Époque", "Les Années folles", "La Grande Dépression"], "Les Trente Glorieuses", "La croissance, le plein emploi et la consommation de masse transforment la société."),
  N("En quelle année le premier choc pétrolier frappe-t-il les économies occidentales ?", 1973, "La hausse brutale du prix du pétrole ouvre une période de chômage de masse."),
  Q("Quelle mesure de 1976 permet aux travailleurs immigrés de faire venir leur famille en France ?", ["Le regroupement familial", "Le droit du sol", "La loi Veil", "Le service civique"], "Le regroupement familial", "L'immigration change alors de nature : elle devient familiale et durable."),
]),
]
