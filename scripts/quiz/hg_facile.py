from qlib import Q, N, C, notion
F = 'facile'
NOTIONS = [
notion('H5-1', 0, F, 'hg-charlemagne', [
  N("En quelle année Charlemagne est-il couronné empereur d'Occident ?", 800, "Charlemagne est couronné empereur par le pape Léon III à Rome, le 25 décembre 800."),
  Q("Qui couronne Charlemagne empereur en 800 ?", ["Le roi de France", "Le pape", "L'empereur byzantin", "Les seigneurs francs"], "Le pape", "Le pape Léon III le couronne à Rome : l'Église légitime ainsi le pouvoir impérial."),
  Q("Comment appelle-t-on la dynastie de Charlemagne ?", ["Mérovingiens", "Carolingiens", "Capétiens", "Valois"], "Carolingiens", "Le nom vient de Carolus, Charles en latin. Les Mérovingiens précèdent, les Capétiens suivent (987)."),
]),
notion('H5-1', 0, F, 'hg-byzance', [
  Q("Quelle est la capitale de l'Empire byzantin ?", ["Rome", "Constantinople", "Bagdad", "Jérusalem"], "Constantinople", "Constantinople (aujourd'hui Istanbul) est la capitale de l'Empire romain d'Orient, ou Empire byzantin."),
  Q("Quel est le nom actuel de Constantinople ?", ["Ankara", "Istanbul", "Athènes", "Le Caire"], "Istanbul", "Constantinople, prise par les Ottomans en 1453, est devenue Istanbul."),
  Q("Quelle religion domine l'Empire byzantin ?", ["L'islam", "Le christianisme orthodoxe", "Le judaïsme", "Le bouddhisme"], "Le christianisme orthodoxe", "Byzance est chrétienne ; après la rupture de 1054 avec Rome, on parle de christianisme orthodoxe."),
]),
notion('H5-1', 1, F, 'hg-naissance-islam', [
  N("En quelle année a lieu l'Hégire, point de départ du calendrier musulman ?", 622, "En 622, Mahomet quitte La Mecque pour Médine : c'est l'Hégire, an 1 du calendrier musulman."),
  Q("Dans quelle région naît l'islam au VIIe siècle ?", ["La péninsule Arabique", "L'Égypte", "La Perse", "L'Espagne"], "La péninsule Arabique", "Mahomet prêche à La Mecque et à Médine, dans la péninsule Arabique."),
  Q("Comment s'appelle le livre sacré de l'islam ?", ["La Bible", "La Torah", "Le Coran", "Les Évangiles"], "Le Coran", "Pour les musulmans, le Coran rassemble la parole de Dieu révélée à Mahomet."),
]),
notion('H5-1', 1, F, 'hg-califat', [
  Q("Comment appelle-t-on le successeur de Mahomet à la tête de la communauté musulmane ?", ["Le sultan", "Le calife", "L'imam", "Le vizir"], "Le calife", "Le calife est le successeur du prophète ; le territoire qu'il gouverne est un califat."),
  Q("Quelle ville devient la capitale du califat abbasside au VIIIe siècle ?", ["Damas", "Bagdad", "Le Caire", "Cordoue"], "Bagdad", "Fondée en 762, Bagdad est la capitale des Abbassides et un grand centre culturel et scientifique."),
  Q("Quelle ville était la capitale du califat omeyyade ?", ["Damas", "Bagdad", "La Mecque", "Constantinople"], "Damas", "Les Omeyyades (661-750) gouvernent depuis Damas, avant que les Abbassides ne fondent Bagdad."),
]),
notion('H5-2', 0, F, 'hg-seigneurie', [
  Q("Comment appelle-t-on le domaine sur lequel un seigneur exerce son pouvoir ?", ["Une commune", "Une seigneurie", "Une paroisse", "Un comté urbain"], "Une seigneurie", "Le seigneur domine les paysans de sa seigneurie : il rend la justice, prélève des taxes et impose des corvées."),
  Q("Comment appelle-t-on un noble qui a prêté hommage à un seigneur plus puissant ?", ["Un serf", "Un vassal", "Un bourgeois", "Un clerc"], "Un vassal", "Par l'hommage, le vassal promet fidélité et aide à son seigneur, qui lui accorde un fief."),
  Q("Qu'est-ce qu'une corvée au Moyen Âge ?", ["Une taxe sur le sel", "Un travail gratuit dû au seigneur", "Une fête religieuse", "Un impôt royal"], "Un travail gratuit dû au seigneur", "Les paysans doivent travailler gratuitement certains jours sur les terres du seigneur."),
]),
notion('H5-2', 1, F, 'hg-villes-medievales', [
  Q("Comment appelle-t-on les habitants des villes au Moyen Âge ?", ["Les serfs", "Les bourgeois", "Les vilains", "Les clercs"], "Les bourgeois", "Le bourgeois est l'habitant du bourg, la ville : artisan, marchand…"),
  Q("Comment s'appellent les grands marchés où se rencontrent les marchands de toute l'Europe, comme en Champagne ?", ["Les foires", "Les halles royales", "Les comptoirs", "Les bourses"], "Les foires", "Aux XIIe et XIIIe siècles, les foires de Champagne sont un carrefour du commerce européen."),
  Q("Quel bâtiment symbolise souvent la liberté d'une ville médiévale dans le nord de la France et en Flandre ?", ["Le donjon", "Le beffroi", "Le cloître", "La motte castrale"], "Le beffroi", "Le beffroi abrite la cloche et souvent les archives de la commune : il symbolise ses libertés."),
]),
notion('H5-2', 2, F, 'hg-capetiens', [
  N("En quelle année Hugues Capet devient-il roi, fondant la dynastie capétienne ?", 987, "Hugues Capet est élu roi en 987 ; ses descendants règnent pendant des siècles."),
  Q("Quel roi capétien est aussi appelé Saint Louis ?", ["Louis VI", "Louis IX", "Louis XI", "Louis XIV"], "Louis IX", "Louis IX (1226-1270), canonisé en 1297, est connu sous le nom de Saint Louis."),
  Q("Quel roi remporte la bataille de Bouvines en 1214 ?", ["Philippe Auguste", "Philippe le Bel", "Charles VII", "Louis IX"], "Philippe Auguste", "La victoire de Philippe Auguste à Bouvines renforce le pouvoir royal capétien."),
]),
notion('H5-2', 2, F, 'hg-guerre-cent-ans', [
  Q("Quels royaumes s'affrontent pendant la guerre de Cent Ans ?", ["France et Espagne", "France et Angleterre", "Angleterre et Écosse", "France et Saint-Empire"], "France et Angleterre", "La guerre de Cent Ans (1337-1453) oppose les rois de France et d'Angleterre."),
  Q("Quel personnage aide Charles VII à se faire sacrer à Reims en 1429 ?", ["Jeanne d'Arc", "Du Guesclin", "Richelieu", "Aliénor d'Aquitaine"], "Jeanne d'Arc", "Jeanne d'Arc fait lever le siège d'Orléans et conduit Charles VII au sacre de Reims."),
  N("En quelle année se termine la guerre de Cent Ans ?", 1453, "La bataille de Castillon (1453) marque la fin de la guerre : les Anglais ne gardent que Calais."),
]),
notion('H5-3', 0, F, 'hg-grandes-decouvertes', [
  N("En quelle année Christophe Colomb atteint-il l'Amérique ?", 1492, "Le 12 octobre 1492, Christophe Colomb, au service de l'Espagne, atteint les Antilles."),
  Q("Au service de quel royaume Christophe Colomb navigue-t-il ?", ["Portugal", "Espagne", "Angleterre", "France"], "Espagne", "Ce sont les Rois catholiques d'Espagne qui financent son expédition de 1492."),
  Q("Quel navigateur réalise, avec son équipage, le premier tour du monde (1519-1522) ?", ["Vasco de Gama", "Magellan", "Jacques Cartier", "Bartolomeu Dias"], "Magellan", "Magellan meurt en route, mais son expédition achève le premier tour du monde en 1522."),
]),
notion('H5-3', 1, F, 'hg-reforme', [
  Q("Qui lance la Réforme protestante en 1517 ?", ["Calvin", "Martin Luther", "Érasme", "Jan Hus"], "Martin Luther", "En 1517, le moine allemand Martin Luther critique la vente des indulgences : c'est le début de la Réforme."),
  N("En quelle année Luther publie-t-il ses 95 thèses ?", 1517, "Ses 95 thèses de 1517 contre les indulgences marquent le début de la Réforme protestante."),
  Q("Quelle invention favorise la diffusion rapide des idées de la Réforme ?", ["La boussole", "L'imprimerie", "La lunette astronomique", "Le moulin à vent"], "L'imprimerie", "L'imprimerie à caractères mobiles, mise au point par Gutenberg vers 1450, diffuse rapidement les textes."),
]),
notion('H5-3', 1, F, 'hg-edit-nantes', [
  N("En quelle année Henri IV signe-t-il l'édit de Nantes ?", 1598, "L'édit de Nantes (1598) met fin aux guerres de Religion et accorde une liberté de culte limitée aux protestants."),
  Q("Que permet l'édit de Nantes ?", ["L'interdiction du protestantisme", "Une liberté de culte limitée pour les protestants", "La séparation de l'Église et de l'État", "L'expulsion des catholiques"], "Une liberté de culte limitée pour les protestants", "L'édit établit une coexistence encadrée entre catholiques et protestants."),
  Q("Quel massacre de protestants a lieu à Paris en 1572 ?", ["La Saint-Barthélemy", "Les Vêpres siciliennes", "La Fronde", "La Saint-Michel"], "La Saint-Barthélemy", "Le 24 août 1572, des milliers de protestants sont massacrés : c'est la Saint-Barthélemy."),
]),
notion('H5-3', 2, F, 'hg-louis-xiv', [
  Q("Quel roi fait construire le château de Versailles et y installe la cour ?", ["Louis XIII", "Louis XIV", "Louis XV", "Henri IV"], "Louis XIV", "Louis XIV, le « Roi-Soleil », installe la cour à Versailles en 1682."),
  Q("Comment appelle-t-on le régime où le roi concentre tous les pouvoirs, comme sous Louis XIV ?", ["La monarchie constitutionnelle", "La monarchie absolue", "La république", "La féodalité"], "La monarchie absolue", "Le roi absolu, de droit divin, ne partage son pouvoir avec aucune institution."),
  Q("Quel édit Louis XIV révoque-t-il en 1685 ?", ["L'édit de Nantes", "L'édit de Villers-Cotterêts", "L'édit de Paulette", "L'édit de Saint-Germain"], "L'édit de Nantes", "Par l'édit de Fontainebleau (1685), Louis XIV révoque l'édit de Nantes : le protestantisme est interdit."),
]),
notion('H4-1', 0, F, 'hg-commerce-triangulaire', [
  Q("Quels continents relie le commerce triangulaire ?", ["Europe, Asie, Océanie", "Europe, Afrique, Amérique", "Afrique, Asie, Amérique", "Europe, Amérique, Asie"], "Europe, Afrique, Amérique", "Les navires partent d'Europe vers l'Afrique, transportent des captifs vers l'Amérique, puis rapportent des produits coloniaux en Europe."),
  Q("Quel grand port français est l'un des principaux ports négriers au XVIIIe siècle ?", ["Nantes", "Strasbourg", "Lyon", "Lille"], "Nantes", "Nantes, comme Bordeaux, La Rochelle et Le Havre, s'enrichit grâce à la traite atlantique."),
  Q("Que transportent les navires négriers d'Afrique vers l'Amérique ?", ["Du sucre", "Des captifs réduits en esclavage", "Des armes", "Du coton brut"], "Des captifs réduits en esclavage", "Des millions d'Africains sont déportés vers les plantations d'Amérique : c'est la traite négrière."),
]),
notion('H4-1', 1, F, 'hg-lumieres', [
  Q("Quel philosophe des Lumières a écrit Candide ?", ["Rousseau", "Voltaire", "Diderot", "Montesquieu"], "Voltaire", "Voltaire publie Candide en 1759 ; il y critique l'intolérance et l'optimisme naïf."),
  Q("Quelle grande œuvre collective dirigée par Diderot et d'Alembert diffuse les idées des Lumières ?", ["Le Contrat social", "L'Encyclopédie", "L'Esprit des lois", "Les Essais"], "L'Encyclopédie", "L'Encyclopédie (1751-1772) rassemble les savoirs de l'époque et diffuse l'esprit critique."),
  Q("Sur quoi les philosophes des Lumières veulent-ils fonder la connaissance et la société ?", ["La tradition", "La raison", "La religion uniquement", "La force"], "La raison", "Les Lumières défendent la raison, la liberté, la tolérance et critiquent l'absolutisme."),
]),
notion('H4-1', 2, F, 'hg-revolution-1789', [
  N("En quelle année a lieu la prise de la Bastille ?", 1789, "Le 14 juillet 1789, le peuple de Paris prend la Bastille, symbole de l'arbitraire royal."),
  Q("Quel texte adopté en août 1789 affirme que « les hommes naissent et demeurent libres et égaux en droits » ?", ["La Constitution de 1791", "La Déclaration des droits de l'homme et du citoyen", "Le Code civil", "Le serment du Jeu de paume"], "La Déclaration des droits de l'homme et du citoyen", "La DDHC est adoptée le 26 août 1789 par l'Assemblée nationale constituante."),
  Q("Que décide l'Assemblée dans la nuit du 4 août 1789 ?", ["La mort du roi", "L'abolition des privilèges", "La création de l'Empire", "La séparation de l'Église et de l'État"], "L'abolition des privilèges", "La nuit du 4 août 1789, les députés abolissent les privilèges et les droits féodaux."),
]),
notion('H4-1', 2, F, 'hg-napoleon', [
  N("En quelle année Napoléon Bonaparte est-il sacré empereur ?", 1804, "Napoléon se fait sacrer empereur des Français le 2 décembre 1804 à Notre-Dame de Paris."),
  Q("Quel recueil de lois civiles est promulgué sous Napoléon en 1804 ?", ["La Charte", "Le Code civil", "Le Concordat", "La Constitution de l'an I"], "Le Code civil", "Le Code civil (1804) unifie le droit et consacre l'égalité devant la loi et la propriété."),
  Q("Quelle bataille de 1815 marque la défaite définitive de Napoléon ?", ["Austerlitz", "Waterloo", "Iéna", "Wagram"], "Waterloo", "Vaincu à Waterloo en juin 1815, Napoléon est exilé à Sainte-Hélène. Austerlitz (1805) fut une victoire."),
]),
notion('H4-2', 0, F, 'hg-revolution-industrielle', [
  Q("Quelle source d'énergie est au cœur de la première révolution industrielle ?", ["Le pétrole", "Le charbon", "L'électricité", "Le nucléaire"], "Le charbon", "Le charbon alimente les machines à vapeur des usines, des locomotives et des navires."),
  Q("Quelle machine symbolise la première révolution industrielle ?", ["Le moteur électrique", "La machine à vapeur", "Le moteur à explosion", "L'ordinateur"], "La machine à vapeur", "Perfectionnée par James Watt à la fin du XVIIIe siècle, elle mécanise la production et les transports."),
  Q("Dans quel pays commence la révolution industrielle ?", ["En France", "Au Royaume-Uni", "En Allemagne", "Aux États-Unis"], "Au Royaume-Uni", "Elle débute au Royaume-Uni à la fin du XVIIIe siècle, puis gagne l'Europe au XIXe siècle."),
]),
notion('H4-2', 1, F, 'hg-colonisation', [
  Q("Quel pays possède le plus vaste empire colonial au début du XXe siècle ?", ["La France", "Le Royaume-Uni", "L'Allemagne", "L'Espagne"], "Le Royaume-Uni", "L'Empire britannique, « sur lequel le soleil ne se couche jamais », est le plus vaste ; l'empire français est le deuxième."),
  Q("Quel territoire d'Afrique du Nord la France commence-t-elle à conquérir en 1830 ?", ["Le Maroc", "L'Algérie", "La Tunisie", "L'Égypte"], "L'Algérie", "La conquête de l'Algérie commence en 1830 et dure plusieurs décennies."),
  Q("Comment appelle-t-on un territoire dominé et administré par une puissance étrangère ?", ["Une métropole", "Une colonie", "Une république", "Une principauté"], "Une colonie", "La colonie est dominée par la métropole, qui l'administre et en exploite les ressources."),
]),
notion('H4-3', 0, F, 'hg-suffrage-1848', [
  N("En quelle année le suffrage universel masculin est-il instauré en France ?", 1848, "En 1848, la IIe République instaure le suffrage universel masculin : tous les hommes de plus de 21 ans votent."),
  Q("Qui obtient le droit de vote en 1848 ?", ["Tous les citoyens, hommes et femmes", "Tous les hommes majeurs", "Les seuls propriétaires", "Les nobles"], "Tous les hommes majeurs", "Le suffrage est universel mais seulement masculin : les femmes n'obtiendront le vote qu'en 1944."),
  Q("Qui fait abolir l'esclavage dans les colonies françaises en 1848 ?", ["Victor Schoelcher", "Jules Ferry", "Lamartine seul", "Napoléon III"], "Victor Schoelcher", "Victor Schoelcher est à l'origine du décret d'abolition du 27 avril 1848."),
]),
notion('H4-3', 1, F, 'hg-troisieme-republique', [
  N("En quelle année la IIIe République est-elle proclamée ?", 1870, "Elle est proclamée le 4 septembre 1870, après la défaite de Napoléon III à Sedan."),
  Q("Quelle allégorie représente la République française ?", ["Clovis", "Marianne", "Jeanne d'Arc", "Vercingétorix"], "Marianne", "Marianne, coiffée du bonnet phrygien, symbolise la République."),
  Q("Quelles lois de 1881-1882 rendent l'école primaire gratuite, obligatoire et laïque ?", ["Les lois Ferry", "Les lois Falloux", "Les lois Guizot", "Les lois Debré"], "Les lois Ferry", "Les lois Jules Ferry sont un pilier de la IIIe République et de l'enracinement républicain."),
]),
notion('H3-1', 0, F, 'hg-premiere-guerre', [
  Q("Quelles sont les dates de la Première Guerre mondiale ?", ["1912-1916", "1914-1918", "1916-1920", "1939-1945"], "1914-1918", "La Première Guerre mondiale dure de 1914 à 1918."),
  Q("Que se passe-t-il le 11 novembre 1918 ?", ["La déclaration de guerre", "La signature de l'armistice", "Le traité de Versailles", "La bataille de Verdun"], "La signature de l'armistice", "L'armistice met fin aux combats ; le traité de Versailles est signé en 1919."),
  N("En quelle année a lieu la bataille de Verdun ?", 1916, "La bataille de Verdun dure de février à décembre 1916 et fait plus de 300 000 morts."),
]),
notion('H3-1', 1, F, 'hg-totalitarismes', [
  Q("Qui dirige l'Allemagne nazie à partir de 1933 ?", ["Mussolini", "Hitler", "Staline", "Franco"], "Hitler", "Adolf Hitler devient chancelier en 1933 et instaure une dictature totalitaire."),
  Q("Qui dirige l'URSS de la fin des années 1920 à 1953 ?", ["Lénine", "Staline", "Trotski", "Khrouchtchev"], "Staline", "Staline impose en URSS un régime totalitaire communiste, marqué par la terreur de masse."),
  Q("Qui dirige l'Italie fasciste à partir de 1922 ?", ["Hitler", "Mussolini", "Franco", "Salazar"], "Mussolini", "Benito Mussolini prend le pouvoir après la marche sur Rome en 1922."),
]),
notion('H3-1', 2, F, 'hg-seconde-guerre', [
  N("En quelle année commence la Seconde Guerre mondiale en Europe ?", 1939, "Après l'invasion de la Pologne par l'Allemagne, la France et le Royaume-Uni déclarent la guerre en septembre 1939."),
  N("En quelle année se termine la Seconde Guerre mondiale ?", 1945, "L'Allemagne capitule le 8 mai 1945 et le Japon le 2 septembre 1945."),
  Q("Comment appelle-t-on le génocide des Juifs d'Europe perpétré par les nazis ?", ["La Shoah", "Le Goulag", "La Nuit de Cristal seulement", "L'Anschluss"], "La Shoah", "Environ six millions de Juifs sont assassinés, notamment dans les centres de mise à mort comme Auschwitz-Birkenau."),
]),
notion('H3-1', 3, F, 'hg-vichy-resistance', [
  Q("Quel personnage lance un appel à la résistance depuis Londres le 18 juin 1940 ?", ["Philippe Pétain", "Charles de Gaulle", "Jean Moulin", "Pierre Laval"], "Charles de Gaulle", "Depuis Londres, à la BBC, le général de Gaulle appelle les Français à poursuivre le combat."),
  Q("Qui dirige le régime de Vichy ?", ["Charles de Gaulle", "Philippe Pétain", "Léon Blum", "Georges Clemenceau"], "Philippe Pétain", "Le maréchal Pétain obtient les pleins pouvoirs en juillet 1940 et collabore avec l'Allemagne nazie."),
  Q("Quelle est la devise du régime de Vichy ?", ["Liberté, Égalité, Fraternité", "Travail, Famille, Patrie", "Honneur et Patrie", "Un peuple, un but, une foi"], "Travail, Famille, Patrie", "Vichy remplace la devise républicaine par « Travail, Famille, Patrie »."),
]),
notion('H3-2', 1, F, 'hg-guerre-froide', [
  Q("Quelles puissances s'opposent pendant la guerre froide ?", ["France et Allemagne", "États-Unis et URSS", "Chine et Japon", "Royaume-Uni et URSS seulement"], "États-Unis et URSS", "La guerre froide (1947-1991) oppose le bloc américain et le bloc soviétique, sans affrontement direct."),
  N("En quelle année tombe le mur de Berlin ?", 1989, "Le 9 novembre 1989, le mur de Berlin tombe ; l'Allemagne est réunifiée en 1990."),
  N("En quelle année le mur de Berlin est-il construit ?", 1961, "Le mur est érigé en août 1961 par la RDA pour empêcher la fuite des Allemands de l'Est vers l'Ouest."),
]),
notion('H3-2', 2, F, 'hg-construction-europeenne', [
  N("En quelle année est signé le traité de Rome qui crée la Communauté économique européenne ?", 1957, "Le traité de Rome (1957) crée la CEE entre six pays fondateurs."),
  Q("Combien de pays fondent la Communauté économique européenne en 1957 ?", ["Quatre", "Six", "Neuf", "Douze"], "Six", "France, RFA, Italie, Belgique, Pays-Bas et Luxembourg sont les six fondateurs."),
  Q("Quelle monnaie est mise en circulation en 2002 dans plusieurs pays de l'Union européenne ?", ["L'ECU", "L'euro", "Le franc européen", "Le mark"], "L'euro", "Les pièces et billets en euros circulent depuis le 1er janvier 2002."),
]),
notion('H3-2', 0, F, 'hg-decolonisation', [
  N("En quelle année l'Algérie devient-elle indépendante ?", 1962, "Après une guerre de huit ans (1954-1962), l'Algérie devient indépendante en juillet 1962."),
  Q("Comment appelle-t-on le processus par lequel les colonies obtiennent leur indépendance ?", ["La colonisation", "La décolonisation", "La mondialisation", "La réunification"], "La décolonisation", "Après 1945, la plupart des colonies d'Asie et d'Afrique accèdent à l'indépendance."),
  Q("Quel leader mène l'Inde vers l'indépendance par la non-violence ?", ["Nehru seul", "Gandhi", "Mao", "Hô Chi Minh"], "Gandhi", "Gandhi prône la désobéissance civile non violente ; l'Inde devient indépendante en 1947."),
]),
notion('H3-3', 1, F, 'hg-cinquieme-republique', [
  N("En quelle année est fondée la Ve République ?", 1958, "La Constitution de la Ve République est approuvée par référendum le 28 septembre 1958."),
  Q("Qui est le premier président de la Ve République ?", ["Georges Pompidou", "Charles de Gaulle", "René Coty", "François Mitterrand"], "Charles de Gaulle", "Charles de Gaulle est président de 1959 à 1969."),
  Q("Depuis 1962, comment le président de la République est-il élu ?", ["Par le Parlement", "Au suffrage universel direct", "Par le Sénat", "Par les maires"], "Au suffrage universel direct", "La réforme de 1962, adoptée par référendum, instaure l'élection du président au suffrage universel direct."),
]),
notion('H3-3', 0, F, 'hg-vote-femmes', [
  N("En quelle année les femmes obtiennent-elles le droit de vote en France ?", 1944, "L'ordonnance du 21 avril 1944 accorde le droit de vote et d'éligibilité aux femmes."),
  N("En quelle année les Françaises votent-elles pour la première fois ?", 1945, "Elles votent pour la première fois aux élections municipales d'avril 1945."),
  Q("Quel organisme fondé pendant la guerre prévoit dans son programme la Sécurité sociale ?", ["Le Conseil national de la Résistance", "Le gouvernement de Vichy", "La SDN", "Le Sénat"], "Le Conseil national de la Résistance", "Le programme du CNR (1944) inspire les grandes réformes de la Libération, dont la Sécurité sociale (1945)."),
]),
notion('H3-3', 2, F, 'hg-societe-1950-1980', [
  Q("Quelle loi de 1975 autorise l'interruption volontaire de grossesse ?", ["La loi Veil", "La loi Neuwirth", "La loi Roudy", "La loi Badinter"], "La loi Veil", "Portée par Simone Veil, ministre de la Santé, la loi est adoptée en janvier 1975."),
  N("En quelle année l'âge de la majorité passe-t-il de 21 à 18 ans en France ?", 1974, "La loi du 5 juillet 1974 abaisse la majorité civile et électorale à 18 ans."),
  Q("En 1981, quelle peine est abolie en France à l'initiative de Robert Badinter ?", ["La prison à vie", "La peine de mort", "Les travaux forcés", "Le bagne"], "La peine de mort", "La loi du 9 octobre 1981 abolit la peine de mort."),
]),
notion('G5-1', 0, F, 'geo-population-mondiale', [
  Q("Combien d'habitants compte environ la Terre en 2025 ?", ["4 milliards", "6 milliards", "8 milliards", "12 milliards"], "8 milliards", "La population mondiale a dépassé 8 milliards d'habitants en 2022."),
  Q("Quels sont les deux pays les plus peuplés du monde ?", ["Chine et États-Unis", "Inde et Chine", "Inde et Indonésie", "Chine et Russie"], "Inde et Chine", "L'Inde et la Chine comptent chacune plus de 1,4 milliard d'habitants ; l'Inde est devenue le pays le plus peuplé en 2023."),
  Q("Quel continent connaît aujourd'hui la plus forte croissance démographique ?", ["L'Europe", "L'Afrique", "L'Amérique du Nord", "L'Océanie"], "L'Afrique", "L'Afrique a la fécondité la plus élevée : sa population pourrait doubler d'ici 2050."),
]),
notion('G5-1', 1, F, 'geo-idh', [
  Q("Que mesure l'indice de développement humain (IDH) ?", ["Seulement la richesse", "La santé, l'éducation et le niveau de vie", "La superficie d'un pays", "La croissance de la population"], "La santé, l'éducation et le niveau de vie", "L'IDH combine l'espérance de vie, la durée de scolarisation et le revenu par habitant."),
  Q("Entre quelles valeurs est compris l'IDH ?", ["0 et 1", "0 et 10", "0 et 100", "1 et 1 000"], "0 et 1", "Plus l'IDH est proche de 1, plus le pays est développé."),
  Q("Comment appelle-t-on la situation d'une personne qui ne peut pas satisfaire ses besoins essentiels ?", ["La pauvreté", "La croissance", "Le développement", "La mondialisation"], "La pauvreté", "La pauvreté est l'insuffisance de ressources pour satisfaire les besoins essentiels (alimentation, logement, santé…)."),
]),
notion('G5-2', 0, F, 'geo-energies', [
  Q("Laquelle de ces énergies est renouvelable ?", ["Le pétrole", "Le gaz naturel", "L'énergie solaire", "Le charbon"], "L'énergie solaire", "Les énergies renouvelables (soleil, vent, eau…) ne s'épuisent pas à l'échelle humaine."),
  Q("Comment appelle-t-on les énergies issues de la décomposition très lente de matières organiques (pétrole, charbon, gaz) ?", ["Énergies renouvelables", "Énergies fossiles", "Énergies nucléaires", "Énergies durables"], "Énergies fossiles", "Ces énergies sont limitées et leur combustion émet du CO₂, principal gaz à effet de serre."),
  Q("Quelle est la principale source de production d'électricité en France ?", ["Le charbon", "Le nucléaire", "Le pétrole", "L'éolien"], "Le nucléaire", "Le nucléaire produit environ les deux tiers de l'électricité française."),
]),
notion('G5-2', 1, F, 'geo-alimentation', [
  Q("Comment appelle-t-on le fait de ne pas manger suffisamment pour couvrir ses besoins en énergie ?", ["La malnutrition", "La sous-nutrition", "La surnutrition", "L'autosuffisance"], "La sous-nutrition", "La sous-nutrition est un manque de calories ; la malnutrition est un déséquilibre (carences ou excès)."),
  Q("Comment appelle-t-on la situation où toute une population a accès à une nourriture suffisante et saine ?", ["L'insécurité alimentaire", "La sécurité alimentaire", "La famine", "L'exode rural"], "La sécurité alimentaire", "La sécurité alimentaire suppose une nourriture suffisante, saine et accessible à tous."),
  Q("Comment appelle-t-on l'agriculture qui utilise beaucoup de machines, d'engrais et de produits pour produire beaucoup ?", ["L'agriculture vivrière", "L'agriculture productiviste", "L'agriculture biologique", "La cueillette"], "L'agriculture productiviste", "Elle produit beaucoup mais peut épuiser les sols et polluer ; l'agriculture vivrière sert à nourrir la famille."),
]),
notion('G5-3', 0, F, 'geo-changement-climatique', [
  Q("Quel gaz est le principal responsable du renforcement de l'effet de serre par les activités humaines ?", ["L'oxygène", "Le dioxyde de carbone", "L'azote", "L'hélium"], "Le dioxyde de carbone", "Le CO₂ issu de la combustion des énergies fossiles renforce l'effet de serre et réchauffe le climat."),
  Q("Quelle est une conséquence du réchauffement climatique ?", ["La baisse du niveau des mers", "La montée du niveau des mers", "L'extension des glaciers", "La fin des sécheresses"], "La montée du niveau des mers", "La fonte des glaces et la dilatation de l'eau font monter le niveau des océans, menaçant les littoraux."),
  Q("Quel accord international de 2015 vise à limiter le réchauffement climatique ?", ["Le protocole de Kyoto", "L'accord de Paris", "Le traité de Rome", "L'accord de Schengen"], "L'accord de Paris", "L'accord de Paris (COP21) vise à contenir le réchauffement nettement sous 2 °C."),
]),
notion('G5-3', 1, F, 'geo-risques', [
  Q("En géographie, comment se définit un risque ?", ["Uniquement par un phénomène naturel", "Par la rencontre d'un aléa et d'une population vulnérable", "Par une catastrophe passée", "Par un accident industriel seulement"], "Par la rencontre d'un aléa et d'une population vulnérable", "Il n'y a risque que si un aléa (séisme, crue…) menace des enjeux humains vulnérables."),
  Q("Comment appelle-t-on la capacité d'une société à se relever après une catastrophe ?", ["La vulnérabilité", "La résilience", "L'aléa", "La prévention"], "La résilience", "La résilience est la capacité à faire face à une catastrophe et à s'en remettre."),
  Q("Lequel de ces risques est un risque technologique ?", ["Une inondation", "L'explosion d'une usine chimique", "Un séisme", "Un cyclone"], "L'explosion d'une usine chimique", "Les risques technologiques sont liés aux activités humaines (industrie, nucléaire, transport de matières dangereuses)."),
]),
notion('G4-1', 0, F, 'geo-urbanisation', [
  Q("Depuis 2007 environ, quelle part de la population mondiale vit en ville ?", ["Moins d'un quart", "Plus de la moitié", "Plus des trois quarts", "Exactement un tiers"], "Plus de la moitié", "Depuis 2007, plus d'un être humain sur deux est citadin."),
  Q("Comment appelle-t-on la croissance de la part de la population vivant en ville ?", ["L'exode urbain", "L'urbanisation", "La ruralisation", "La périurbanisation"], "L'urbanisation", "L'urbanisation est l'augmentation de la population urbaine et l'extension des villes."),
  Q("Comment appelle-t-on les quartiers d'habitat précaire dans de nombreuses villes des pays pauvres ?", ["Les banlieues pavillonnaires", "Les bidonvilles", "Les centres d'affaires", "Les technopôles"], "Les bidonvilles", "Les bidonvilles, construits sans autorisation avec des matériaux de récupération, manquent d'équipements."),
]),
notion('G4-1', 1, F, 'geo-metropoles', [
  Q("Comment appelle-t-on une grande ville qui concentre des fonctions de commandement à l'échelle mondiale ?", ["Une ville moyenne", "Une métropole mondiale", "Un village", "Une ville-dortoir"], "Une métropole mondiale", "New York, Londres, Tokyo ou Paris concentrent sièges sociaux, places financières et institutions internationales."),
  Q("Comment appelle-t-on une agglomération de plus de 10 millions d'habitants ?", ["Une mégapole", "Une métropole régionale", "Une conurbation", "Une technopole"], "Une mégapole", "Une mégapole se définit par sa taille (plus de 10 millions d'habitants), comme Tokyo, Delhi ou Lagos."),
  Q("Comment appelle-t-on le quartier des affaires d'une grande ville, comme La Défense ?", ["Le CBD", "La banlieue", "Le périurbain", "Le centre historique"], "Le CBD", "Le CBD (Central Business District) rassemble bureaux, sièges sociaux et activités financières."),
]),
notion('G4-2', 0, F, 'geo-migrations', [
  Q("Comment appelle-t-on une personne qui quitte son pays pour s'installer dans un autre ?", ["Un touriste", "Un migrant", "Un frontalier", "Un nomade"], "Un migrant", "Un migrant change de lieu de résidence de façon durable ; il est émigré pour son pays de départ et immigré pour son pays d'arrivée."),
  Q("Comment appelle-t-on une personne qui fuit son pays pour échapper à des persécutions et qui obtient une protection ?", ["Un expatrié", "Un réfugié", "Un saisonnier", "Un touriste"], "Un réfugié", "Le statut de réfugié est défini par la convention de Genève (1951)."),
  Q("Quel est le principal facteur des migrations dans le monde ?", ["Le tourisme", "La recherche d'un emploi et de meilleures conditions de vie", "Les études uniquement", "Le climat agréable"], "La recherche d'un emploi et de meilleures conditions de vie", "Les migrations économiques sont les plus nombreuses, même si les conflits et le climat jouent aussi."),
]),
notion('G4-2', 1, F, 'geo-tourisme', [
  Q("Quel est le pays le plus visité au monde par les touristes internationaux ?", ["Les États-Unis", "La France", "L'Espagne", "La Chine"], "La France", "La France accueille environ 90 à 100 millions de touristes internationaux par an."),
  Q("Comment appelle-t-on une personne qui voyage hors de son domicile au moins une nuit pour ses loisirs ?", ["Un migrant", "Un touriste", "Un pendulaire", "Un réfugié"], "Un touriste", "Le touriste se déplace temporairement, au moins une nuit et moins d'un an, hors de son lieu de vie."),
  Q("Quel est l'un des effets négatifs du tourisme de masse ?", ["La création d'emplois", "La dégradation de certains milieux naturels", "La valorisation du patrimoine", "Les revenus pour les habitants"], "La dégradation de certains milieux naturels", "Le surtourisme peut dégrader les milieux, saturer les sites et faire monter les prix pour les habitants."),
]),
notion('G4-3', 0, F, 'geo-mers-oceans', [
  Q("Quelle part du commerce mondial (en volume) passe par la mer ?", ["Environ 10 %", "Environ 50 %", "Environ 80 à 90 %", "100 %"], "Environ 80 à 90 %", "La grande majorité des marchandises voyage par voie maritime, souvent en conteneurs."),
  Q("Comment appelle-t-on l'espace maritime de 200 milles nautiques où un État exploite seul les ressources ?", ["Les eaux internationales", "La zone économique exclusive (ZEE)", "Le plateau continental", "Le détroit"], "La zone économique exclusive (ZEE)", "La ZEE s'étend jusqu'à 200 milles nautiques (environ 370 km) des côtes."),
  Q("Quelle grande boîte métallique standardisée a révolutionné le transport maritime ?", ["La palette", "Le conteneur", "Le vrac", "La citerne"], "Le conteneur", "Le conteneur facilite le chargement et le transfert entre bateaux, trains et camions."),
]),
notion('G3-1', 0, F, 'geo-aires-urbaines', [
  Q("Comment appelle-t-on l'espace autour d'une ville où les habitants vivent en maison mais travaillent souvent en ville ?", ["Le centre-ville", "L'espace périurbain", "Le CBD", "Le désert rural"], "L'espace périurbain", "Le périurbain s'étend autour des villes ; ses habitants font souvent des trajets quotidiens vers la ville."),
  Q("Comment appelle-t-on les personnes qui font chaque jour l'aller-retour entre leur domicile et leur travail ?", ["Les touristes", "Les navetteurs (migrants pendulaires)", "Les saisonniers", "Les nomades"], "Les navetteurs (migrants pendulaires)", "Les migrations pendulaires sont les déplacements quotidiens domicile-travail."),
  Q("Quelle part de la population française vit dans l'aire d'attraction d'une ville ?", ["Environ un tiers", "Environ la moitié", "Plus des quatre cinquièmes", "Moins de 10 %"], "Plus des quatre cinquièmes", "Environ 93 % des Français vivent dans l'aire d'attraction d'une ville : la France est très urbanisée."),
]),
notion('G3-3', 0, F, 'geo-union-europeenne', [
  N("Combien d'États membres compte l'Union européenne depuis le départ du Royaume-Uni en 2020 ?", 27, "Depuis le Brexit (2020), l'Union européenne compte 27 États membres."),
  Q("Quel espace permet la libre circulation des personnes sans contrôle aux frontières intérieures ?", ["La zone euro", "L'espace Schengen", "Le Conseil de l'Europe", "L'OTAN"], "L'espace Schengen", "L'espace Schengen supprime les contrôles aux frontières intérieures entre les pays membres."),
  Q("Dans quelle ville siège le Parlement européen ?", ["Bruxelles", "Strasbourg", "Luxembourg", "Francfort"], "Strasbourg", "Le Parlement européen siège officiellement à Strasbourg (avec des activités à Bruxelles)."),
]),
notion('G3-2', 1, F, 'geo-outre-mer', [
  N("Combien de départements et régions d'outre-mer (DROM) compte la France ?", 5, "Guadeloupe, Martinique, Guyane, La Réunion et Mayotte sont les cinq DROM."),
  Q("Lequel de ces territoires est un département et région d'outre-mer ?", ["La Polynésie française", "La Réunion", "La Nouvelle-Calédonie", "Saint-Pierre-et-Miquelon"], "La Réunion", "La Réunion est un DROM ; les autres sont des collectivités à statut particulier."),
  Q("Dans quel océan se trouve La Réunion ?", ["Océan Atlantique", "Océan Indien", "Océan Pacifique", "Mer des Caraïbes"], "Océan Indien", "La Réunion et Mayotte se trouvent dans l'océan Indien ; la Guadeloupe et la Martinique, dans la mer des Caraïbes."),
]),
notion('G3-1', 2, F, 'geo-faible-densite', [
  Q("Comment appelle-t-on la diagonale de faibles densités qui traverse la France du nord-est au sud-ouest ?", ["La dorsale européenne", "La « diagonale du vide »", "Le croissant fertile", "L'arc atlantique"], "La « diagonale du vide »", "Cette bande de territoires peu peuplés va des Ardennes aux Landes ; l'expression est aujourd'hui nuancée."),
  Q("Quel atout peuvent valoriser les espaces de faible densité ?", ["Une forte concentration industrielle", "Le cadre de vie, le tourisme et le patrimoine naturel", "Les grands aéroports internationaux", "Les quartiers d'affaires"], "Le cadre de vie, le tourisme et le patrimoine naturel", "Ces espaces attirent des néo-ruraux et des touristes, et développent agriculture de qualité et tourisme vert."),
  Q("Comment appelle-t-on l'installation de citadins à la campagne ?", ["L'exode rural", "La néo-ruralité", "La métropolisation", "La littoralisation"], "La néo-ruralité", "Les néo-ruraux quittent la ville pour s'installer à la campagne, inversant l'ancien exode rural."),
]),
notion('G3-1', 1, F, 'geo-espaces-productifs', [
  Q("Comment appelle-t-on le déplacement des activités et des populations vers les littoraux ?", ["La littoralisation", "La désindustrialisation", "La périurbanisation", "La rurbanisation"], "La littoralisation", "Les littoraux concentrent ports, industries, tourisme et habitants."),
  Q("Comment appelle-t-on la baisse de la part de l'industrie dans l'emploi et l'économie d'un pays ?", ["L'industrialisation", "La désindustrialisation", "La tertiarisation", "La délocalisation"], "La désindustrialisation", "Les anciennes régions industrielles (mines, sidérurgie, textile) ont perdu beaucoup d'emplois."),
  Q("À quel secteur d'activité appartiennent le commerce, les transports et la santé ?", ["Primaire", "Secondaire", "Tertiaire", "Quaternaire"], "Tertiaire", "Le secteur tertiaire regroupe les services ; il emploie environ les trois quarts des actifs français."),
]),
notion('H4-1', 2, F, 'hg-republique-1792', [
  N("En quelle année la première République est-elle proclamée en France ?", 1792, "La République est proclamée le 22 septembre 1792, après la chute de la monarchie le 10 août."),
  Q("Quel roi est guillotiné en janvier 1793 ?", ["Louis XIV", "Louis XV", "Louis XVI", "Charles X"], "Louis XVI", "Louis XVI, jugé par la Convention, est exécuté le 21 janvier 1793."),
  Q("Comment appelle-t-on la période de 1793-1794 marquée par une répression très dure sous la Convention ?", ["La Restauration", "La Terreur", "Le Directoire", "Les Cent-Jours"], "La Terreur", "Pendant la Terreur, des milliers de suspects sont exécutés ; elle prend fin avec la chute de Robespierre en 1794."),
]),
notion('G5-2', 0, F, 'geo-eau', [
  Q("Quelle part de l'eau présente sur Terre est de l'eau douce ?", ["Environ 3 %", "Environ 30 %", "Environ 50 %", "Environ 97 %"], "Environ 3 %", "Environ 97 % de l'eau est salée ; l'eau douce ne représente qu'environ 3 %, dont une grande partie est gelée."),
  Q("Quel secteur consomme le plus d'eau douce dans le monde ?", ["L'industrie", "L'agriculture", "Les usages domestiques", "Le tourisme"], "L'agriculture", "L'irrigation représente environ 70 % des prélèvements d'eau douce dans le monde."),
  Q("Comment appelle-t-on la situation d'un territoire où les besoins en eau dépassent les ressources disponibles ?", ["Le stress hydrique", "L'irrigation", "La désalinisation", "L'érosion"], "Le stress hydrique", "Le stress hydrique touche notamment les régions arides et les zones à forte croissance démographique."),
]),
notion('H3-1', 0, F, 'hg-traite-versailles', [
  N("En quelle année est signé le traité de Versailles qui règle le sort de l'Allemagne après la Première Guerre mondiale ?", 1919, "Le traité de Versailles est signé le 28 juin 1919, dans la galerie des Glaces."),
  Q("Quelle région la France récupère-t-elle en 1919 grâce au traité de Versailles ?", ["La Savoie", "L'Alsace-Moselle", "La Corse", "La Bretagne"], "L'Alsace-Moselle", "Annexée par l'Allemagne en 1871, l'Alsace-Moselle redevient française en 1919."),
  Q("Quelle organisation internationale est créée en 1919-1920 pour préserver la paix ?", ["L'ONU", "La Société des Nations (SDN)", "L'OTAN", "L'Union européenne"], "La Société des Nations (SDN)", "La SDN est créée après la Première Guerre mondiale ; l'ONU la remplace en 1945."),
]),
notion('G4-3', 1, F, 'geo-etats-unis', [
  Q("Comment appelle-t-on la région du sud des États-Unis, attractive grâce à son climat et à ses activités nouvelles ?", ["La Manufacturing Belt", "La Sun Belt", "Le Midwest", "La Nouvelle-Angleterre"], "La Sun Belt", "La Sun Belt (« ceinture du soleil ») attire habitants et entreprises de haute technologie."),
  Q("Quelle mégalopole s'étend de Boston à Washington ?", ["La Mégalopolis du Nord-Est (BosWash)", "La Sun Belt", "La Silicon Valley", "La Rust Belt"], "La Mégalopolis du Nord-Est (BosWash)", "Cette mégalopole concentre de grandes métropoles (New York, Philadelphie…) et des fonctions de commandement."),
  Q("Quelle région de Californie est célèbre pour ses entreprises du numérique ?", ["La Silicon Valley", "La Rust Belt", "Le Corn Belt", "Le Texas"], "La Silicon Valley", "Près de San Francisco, la Silicon Valley concentre de grandes entreprises du numérique et des universités."),
]),
]
