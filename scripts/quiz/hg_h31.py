# Histoire 3e · L'Europe, un théâtre majeur des guerres totales (1914-1945) : au moins 50 questions par niveau
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Facile ══
notion('H3-1', 0, F, 'hg3-tranchees', [
  Q("Comment appelle-t-on les fossés creusés par les soldats pour se protéger pendant la Première Guerre mondiale ?", ["Les tranchées", "Les bunkers", "Les remparts", "Les douves"], "Les tranchées", "Le front se fige à partir de fin 1914."),
  Q("Comment appelle-t-on l'espace entre les tranchées ennemies ?", ["Le no man's land", "La ligne Maginot", "Le front populaire", "La zone libre"], "Le no man's land", "C'est une « terre d'aucun homme », ravagée par les obus."),
  Q("Quelles conditions de vie les soldats subissent-ils dans les tranchées ?", ["Boue, froid, rats, poux et bombardements", "Confort et repos", "Chaleur et abondance", "Aucune difficulté"], "Boue, froid, rats, poux et bombardements", "La peur de la mort est permanente."),
]),
notion('H3-1', 0, F, 'hg3-debut-1914', [
  Q("Quel attentat de juin 1914 déclenche la crise qui mène à la guerre ?", ["L'assassinat de l'archiduc François-Ferdinand à Sarajevo", "L'assassinat de Jaurès", "L'incendie du Reichstag", "L'attaque de Pearl Harbor"], "L'assassinat de l'archiduc François-Ferdinand à Sarajevo", "Il est l'héritier de l'Autriche-Hongrie."),
  Q("Quels pays forment la Triple-Entente en 1914 ?", ["France, Royaume-Uni, Russie", "Allemagne, Autriche-Hongrie, Italie", "France, Allemagne, Italie", "États-Unis, Japon, Chine"], "France, Royaume-Uni, Russie", "Elle s'oppose à la Triple-Alliance."),
  Q("Quelle bataille de septembre 1914 arrête l'avancée allemande vers Paris ?", ["La bataille de la Marne", "Verdun", "La Somme", "Stalingrad"], "La bataille de la Marne", "Des taxis parisiens transportent des soldats."),
]),
notion('H3-1', 0, F, 'hg3-armes-1914', [
  Q("Quelle nouvelle arme chimique est utilisée pour la première fois à grande échelle en 1915 ?", ["Les gaz de combat", "La bombe atomique", "Le napalm", "Les missiles"], "Les gaz de combat", "Le gaz moutarde est appelé « ypérite »."),
  Q("Quel engin blindé apparaît sur le champ de bataille en 1916 ?", ["Le char d'assaut", "Le drone", "L'hélicoptère", "Le porte-avions"], "Le char d'assaut", "Il est d'abord britannique."),
  Q("Quelle arme cause la plupart des blessures et des morts pendant la Grande Guerre ?", ["L'artillerie (les obus)", "Les épées", "Les arcs", "Les bombes atomiques"], "L'artillerie (les obus)", "Les soldats sont souvent défigurés : les « gueules cassées »."),
]),
notion('H3-1', 0, F, 'hg3-memoire-1418', [
  Q("Quel monument trouve-t-on dans presque chaque commune de France après 1918 ?", ["Le monument aux morts", "Une statue de Napoléon", "Un arc de triomphe", "Une tour Eiffel"], "Le monument aux morts", "Il porte le nom des soldats tués."),
  Q("Qui repose sous l'Arc de triomphe depuis 1921 ?", ["Le Soldat inconnu", "Napoléon", "Le maréchal Foch", "Clemenceau"], "Le Soldat inconnu", "La flamme du souvenir y est ravivée chaque soir."),
  Q("Combien de soldats français environ sont morts pendant la Première Guerre mondiale ?", ["Environ 1,4 million", "Environ 140 000", "Environ 14 millions", "Environ 400 000"], "Environ 1,4 million", "Près d'un mobilisé sur six."),
]),
notion('H3-1', 1, F, 'hg3-revolution-russe', [
  N("En quelle année éclate la révolution russe ?", 1917, "Elle a lieu en février puis en octobre."),
  Q("Qui prend le pouvoir en Russie en octobre 1917 ?", ["Lénine et les bolcheviks", "Le tsar Nicolas II", "Staline", "Hitler"], "Lénine et les bolcheviks", "Ils fondent un régime communiste."),
  Q("Quel nom prend la Russie communiste en 1922 ?", ["L'URSS", "La Fédération de Russie", "L'Empire russe", "La CEI"], "L'URSS", "Union des républiques socialistes soviétiques."),
]),
notion('H3-1', 1, F, 'hg3-propagande', [
  Q("Comment appelle-t-on l'action de diffuser des idées pour influencer la population ?", ["La propagande", "La démocratie", "La liberté de la presse", "Le débat"], "La propagande", "Les régimes totalitaires l'utilisent massivement."),
  Q("Quelle organisation embrigade la jeunesse allemande sous le nazisme ?", ["Les Jeunesses hitlériennes", "Le scoutisme", "Les Komsomols", "Les Balillas"], "Les Jeunesses hitlériennes", "L'adhésion devient obligatoire en 1936."),
  Q("Quel symbole est l'emblème du parti nazi ?", ["La croix gammée", "La faucille et le marteau", "Le faisceau", "La croix de Lorraine"], "La croix gammée", "La faucille et le marteau sont l'emblème communiste."),
]),
notion('H3-1', 2, F, 'hg3-debut-1939', [
  Q("Quel pays l'Allemagne envahit-elle le 1er septembre 1939 ?", ["La Pologne", "La France", "La Belgique", "L'URSS"], "La Pologne", "La France et le Royaume-Uni déclarent la guerre deux jours plus tard."),
  Q("Quel pays est le seul à résister à l'Allemagne en Europe de l'Ouest à l'été 1940 ?", ["Le Royaume-Uni", "La France", "L'Espagne", "L'Italie"], "Le Royaume-Uni", "Winston Churchill dirige la résistance britannique."),
  Q("Quel Premier ministre britannique promet « du sang, de la sueur et des larmes » en 1940 ?", ["Winston Churchill", "Neville Chamberlain", "Roosevelt", "Clement Attlee"], "Winston Churchill", "Il refuse de négocier avec Hitler."),
]),
notion('H3-1', 2, F, 'hg3-pearl-harbor', [
  Q("Quelle base américaine le Japon attaque-t-il le 7 décembre 1941 ?", ["Pearl Harbor", "Hiroshima", "Midway", "New York"], "Pearl Harbor", "Les États-Unis entrent en guerre."),
  Q("Quel président dirige les États-Unis pendant la majeure partie de la Seconde Guerre mondiale ?", ["Franklin D. Roosevelt", "Truman", "Eisenhower", "Kennedy"], "Franklin D. Roosevelt", "Il meurt en avril 1945."),
  Q("Quels pays forment l'Axe pendant la Seconde Guerre mondiale ?", ["Allemagne, Italie, Japon", "France, Royaume-Uni, URSS", "États-Unis, Chine, URSS", "Espagne, Portugal, Suisse"], "Allemagne, Italie, Japon", "Ils s'opposent aux Alliés."),
]),
notion('H3-1', 2, F, 'hg3-camps', [
  Q("Quel est le plus grand camp de concentration et d'extermination nazi ?", ["Auschwitz-Birkenau", "Dachau", "Drancy", "Buchenwald"], "Auschwitz-Birkenau", "Plus d'un million de personnes y sont assassinées."),
  Q("Dans quels pays se trouvent les centres de mise à mort nazis ?", ["Surtout en Pologne occupée", "En France", "En Angleterre", "En Italie"], "Surtout en Pologne occupée", "Treblinka, Sobibor, Belzec, Auschwitz…"),
  Q("Quelle jeune fille juive a écrit un journal pendant qu'elle se cachait à Amsterdam ?", ["Anne Frank", "Simone Veil", "Hannah Arendt", "Sophie Scholl"], "Anne Frank", "Elle meurt à Bergen-Belsen en 1945."),
]),
notion('H3-1', 3, F, 'hg3-occupation', [
  Q("En combien de zones principales la France est-elle coupée après l'armistice de 1940 ?", ["Deux : zone occupée au nord et zone libre au sud", "Une seule", "Quatre", "Dix"], "Deux : zone occupée au nord et zone libre au sud", "La ligne de démarcation les sépare."),
  Q("Quel document faut-il pour obtenir de la nourriture pendant l'Occupation ?", ["Des tickets de rationnement", "Un passeport", "Un permis de conduire", "Une carte bancaire"], "Des tickets de rationnement", "Les pénuries sont très fortes."),
  Q("Quand la zone libre est-elle envahie par les Allemands ?", ["En novembre 1942", "En juin 1940", "En juin 1944", "En 1945"], "En novembre 1942", "C'est après le débarquement allié en Afrique du Nord."),
]),
notion('H3-1', 3, F, 'hg3-resistants', [
  Q("Quel résistant, unificateur de la Résistance, meurt après avoir été torturé en 1943 ?", ["Jean Moulin", "Charles de Gaulle", "Pierre Brossolette seulement", "Lucie Aubrac"], "Jean Moulin", "Ses cendres sont au Panthéon."),
  Q("Comment appelle-t-on les résistants cachés dans les forêts et les montagnes ?", ["Les maquisards", "Les collabos", "Les miliciens", "Les poilus"], "Les maquisards", "Le maquis du Vercors est célèbre."),
  Q("Quelle résistante lyonnaise fait évader son mari Raymond en 1943 ?", ["Lucie Aubrac", "Simone Veil", "Joséphine Baker", "Germaine Tillion"], "Lucie Aubrac", "Elle témoigne après la guerre dans les écoles."),
]),
notion('H3-1', 3, F, 'hg3-liberation-paris', [
  N("En quelle année Paris est-il libéré ?", 1944, "Le 25 août 1944."),
  Q("Quelle division française entre dans Paris en août 1944 ?", ["La 2e division blindée du général Leclerc", "La Légion étrangère", "La Wehrmacht", "La Milice"], "La 2e division blindée du général Leclerc", "De Gaulle descend les Champs-Élysées le 26 août."),
  Q("Qu'est-ce que le débarquement de Provence d'août 1944 ?", ["Un débarquement allié dans le sud de la France", "Une invasion allemande", "Une révolte paysanne", "Un bombardement de Paris"], "Un débarquement allié dans le sud de la France", "L'armée française de De Lattre y participe."),
]),
# ══ Intermédiaire ══
notion('H3-1', 0, I, 'hg3i-verdun-somme', [
  Q("Combien de temps dure la bataille de Verdun ?", ["Environ dix mois (février-décembre 1916)", "Une semaine", "Un mois", "Quatre ans"], "Environ dix mois (février-décembre 1916)", "Plus de 300 000 soldats y meurent."),
  Q("Quelle route assure le ravitaillement de Verdun ?", ["La Voie sacrée", "La route Napoléon", "La route de la soie", "La Nationale 7"], "La Voie sacrée", "Des milliers de camions y circulent."),
  Q("Quelle offensive franco-britannique de 1916 fait plus d'un million de victimes ?", ["La bataille de la Somme", "Le Chemin des Dames", "La Marne", "Caporetto"], "La bataille de la Somme", "Le premier jour, 20 000 Britanniques sont tués."),
]),
notion('H3-1', 0, I, 'hg3i-arriere', [
  Q("Quel rôle jouent les femmes à l'arrière pendant la Grande Guerre ?", ["Elles remplacent les hommes dans les champs et les usines", "Elles combattent au front", "Elles ne travaillent pas", "Elles votent les lois"], "Elles remplacent les hommes dans les champs et les usines", "Les « munitionnettes » fabriquent des obus."),
  Q("Comment l'État finance-t-il la guerre auprès de la population ?", ["Par des emprunts de guerre", "Par la vente de colonies", "Par la loterie", "Il ne la finance pas"], "Par des emprunts de guerre", "Des affiches incitent à « souscrire »."),
  Q("Comment appelle-t-on le contrôle des informations par l'État pendant la guerre ?", ["La censure", "La propagande seulement", "La liberté de la presse", "Le référendum"], "La censure", "Le Canard enchaîné naît en 1915 pour s'en moquer."),
]),
notion('H3-1', 0, I, 'hg3i-1917', [
  Q("Pourquoi des soldats français se mutinent-ils en 1917 ?", ["Après l'échec sanglant de l'offensive du Chemin des Dames", "Pour rejoindre l'Allemagne", "Parce que la guerre est finie", "Pour réclamer le droit de vote des femmes"], "Après l'échec sanglant de l'offensive du Chemin des Dames", "Pétain améliore leurs conditions et limite les offensives."),
  Q("Quel pays entre en guerre aux côtés de l'Entente en 1917 ?", ["Les États-Unis", "Le Japon", "La Russie", "L'Espagne"], "Les États-Unis", "La guerre sous-marine allemande les y pousse."),
  Q("Quel pays sort de la guerre en 1918 par le traité de Brest-Litovsk ?", ["La Russie bolchevique", "La France", "L'Italie", "La Belgique"], "La Russie bolchevique", "Elle cède de vastes territoires à l'Allemagne."),
]),
notion('H3-1', 0, I, 'hg3i-troupes-coloniales', [
  Q("Comment appelle-t-on les soldats d'Afrique noire mobilisés par la France ?", ["Les tirailleurs sénégalais", "Les zouaves pontificaux", "Les poilus bretons", "Les chasseurs alpins"], "Les tirailleurs sénégalais", "Ils viennent de toute l'Afrique-Occidentale française."),
  Q("Combien d'hommes environ l'empire colonial français fournit-il pendant la Première Guerre mondiale ?", ["Environ 600 000 soldats", "Environ 6 000", "Environ 6 millions", "Aucun"], "Environ 600 000 soldats", "S'y ajoutent des travailleurs coloniaux."),
  Q("Quel pays d'Océanie voit ses soldats (ANZAC) combattre aux Dardanelles en 1915 ?", ["L'Australie et la Nouvelle-Zélande", "Le Japon", "Les Philippines", "Hawaï"], "L'Australie et la Nouvelle-Zélande", "Le 25 avril est un jour de mémoire dans ces pays."),
]),
notion('H3-1', 1, I, 'hg3i-fascisme', [
  Q("Comment Mussolini arrive-t-il au pouvoir en 1922 ?", ["Après la marche sur Rome", "Par une élection libre", "Par un héritage", "Par une révolution communiste"], "Après la marche sur Rome", "Le roi le nomme chef du gouvernement."),
  Q("Quel titre Mussolini se donne-t-il ?", ["Le Duce", "Le Führer", "Le Caudillo", "Le Petit Père des peuples"], "Le Duce", "Il signifie « le guide »."),
  Q("Quel pays l'Italie fasciste envahit-elle en 1935 ?", ["L'Éthiopie", "La Grèce", "L'Albanie", "La Libye"], "L'Éthiopie", "La SDN se montre impuissante."),
]),
notion('H3-1', 1, I, 'hg3i-nazisme-etapes', [
  Q("Quel événement de février 1933 sert de prétexte à Hitler pour suspendre les libertés ?", ["L'incendie du Reichstag", "La Nuit de cristal", "La Nuit des longs couteaux", "L'Anschluss"], "L'incendie du Reichstag", "Les communistes sont accusés."),
  Q("Comment appelle-t-on la police politique du régime nazi ?", ["La Gestapo", "Le NKVD", "La SS seulement", "L'OVRA"], "La Gestapo", "Le NKVD est la police politique soviétique."),
  Q("Comment appelle-t-on le pogrom organisé contre les Juifs d'Allemagne en novembre 1938 ?", ["La Nuit de cristal", "La Nuit des longs couteaux", "La Saint-Barthélemy", "La rafle du Vel' d'Hiv"], "La Nuit de cristal", "Des synagogues et des magasins sont détruits."),
]),
notion('H3-1', 1, I, 'hg3i-stalinisme', [
  Q("Comment appelle-t-on la mise en commun forcée des terres en URSS à partir de 1929 ?", ["La collectivisation", "La privatisation", "La NEP", "La réforme agraire libérale"], "La collectivisation", "Les paysans sont regroupés en kolkhozes."),
  Q("Quelle famine provoquée par la politique stalinienne fait des millions de morts en Ukraine en 1932-1933 ?", ["L'Holodomor", "La Grande Peur", "Le Dust Bowl", "La famine irlandaise"], "L'Holodomor", "Le mot signifie « extermination par la faim »."),
  Q("Comment appelle-t-on les purges sanglantes de 1936-1938 en URSS ?", ["La Grande Terreur", "La révolution culturelle", "La Terreur blanche", "Le Printemps de Prague"], "La Grande Terreur", "Plus de 700 000 personnes sont exécutées."),
]),
notion('H3-1', 1, I, 'hg3i-democraties-1930', [
  Q("Quelle émeute antiparlementaire des ligues d'extrême droite a lieu à Paris en 1934 ?", ["Le 6 février 1934", "Le 14 juillet 1934", "Le 11 novembre 1934", "Le 1er mai 1934"], "Le 6 février 1934", "La gauche s'unit ensuite face au danger fasciste."),
  Q("Quels accords du Front populaire, en 1936, accordent la semaine de 40 heures ?", ["Les accords de Matignon", "Les accords de Grenelle", "Les accords de Munich", "Les accords d'Évian"], "Les accords de Matignon", "Ils accordent aussi les conventions collectives et des hausses de salaires."),
  Q("Quelle guerre civile oppose républicains et nationalistes de 1936 à 1939 ?", ["La guerre d'Espagne", "La guerre de Sécession", "La guerre de Corée", "La guerre d'Indochine"], "La guerre d'Espagne", "Franco l'emporte avec l'aide d'Hitler et de Mussolini."),
]),
notion('H3-1', 2, I, 'hg3i-montee-guerre', [
  Q("Quels accords de 1938 laissent Hitler annexer les Sudètes ?", ["Les accords de Munich", "Les accords de Locarno", "Le pacte germano-soviétique", "Le traité de Versailles"], "Les accords de Munich", "La France et le Royaume-Uni cèdent pour éviter la guerre."),
  Q("Quel pacte de non-agression Hitler signe-t-il avec Staline en août 1939 ?", ["Le pacte germano-soviétique", "Le pacte d'acier", "Le pacte anti-Komintern", "Le pacte de Varsovie"], "Le pacte germano-soviétique", "Il prévoit secrètement le partage de la Pologne."),
  Q("Comment appelle-t-on l'annexion de l'Autriche par l'Allemagne en 1938 ?", ["L'Anschluss", "Le Lebensraum", "Le Blitzkrieg", "Le Reich"], "L'Anschluss", "Elle viole le traité de Versailles."),
]),
notion('H3-1', 2, I, 'hg3i-guerre-eclair', [
  Q("Comment appelle-t-on la stratégie allemande d'attaques rapides avec chars et avions ?", ["La guerre éclair (Blitzkrieg)", "La guerre de position", "La guérilla", "La guerre froide"], "La guerre éclair (Blitzkrieg)", "Elle permet de vaincre la France en six semaines."),
  Q("Quelle opération allemande vise l'URSS en juin 1941 ?", ["L'opération Barbarossa", "L'opération Overlord", "L'opération Torch", "L'opération Dynamo"], "L'opération Barbarossa", "C'est la plus grande invasion de l'histoire."),
  Q("Quelle bataille aérienne de 1940 empêche l'invasion du Royaume-Uni ?", ["La bataille d'Angleterre", "La bataille de France", "La bataille de Midway", "La bataille de l'Atlantique"], "La bataille d'Angleterre", "La Royal Air Force tient bon."),
]),
notion('H3-1', 2, I, 'hg3i-guerre-pacifique', [
  Q("Quelle bataille navale de juin 1942 marque un tournant dans le Pacifique ?", ["Midway", "Pearl Harbor", "Trafalgar", "Lépante"], "Midway", "Le Japon y perd quatre porte-avions."),
  Q("Quelle date marque la capitulation du Japon ?", ["Le 2 septembre 1945", "Le 8 mai 1945", "Le 6 juin 1944", "Le 11 novembre 1918"], "Le 2 septembre 1945", "Elle est signée à bord du cuirassé Missouri."),
  Q("Comment appelle-t-on les pilotes japonais qui s'écrasent volontairement sur les navires ennemis ?", ["Les kamikazes", "Les samouraïs", "Les shoguns", "Les ninjas"], "Les kamikazes", "Le mot signifie « vent divin »."),
]),
notion('H3-1', 3, I, 'hg3i-vichy-politique', [
  Q("Comment appelle-t-on la politique de Pétain qui veut transformer la société française selon des valeurs traditionnelles ?", ["La Révolution nationale", "Le Front populaire", "La Restauration", "La Libération"], "La Révolution nationale", "Elle s'oppose aux valeurs républicaines."),
  Q("Quelle poignée de main d'octobre 1940 symbolise l'entrée dans la collaboration ?", ["Pétain et Hitler à Montoire", "De Gaulle et Churchill à Londres", "Pétain et Mussolini à Rome", "Laval et Staline"], "Pétain et Hitler à Montoire", "Pétain annonce : « J'entre aujourd'hui dans la voie de la collaboration »."),
  N("En quelle année le statut des Juifs est-il promulgué par Vichy pour la première fois ?", 1940, "Il exclut les Juifs de nombreuses professions, sans demande allemande."),
]),
notion('H3-1', 3, I, 'hg3i-france-libre', [
  Q("Comment s'appellent les forces militaires réunies par de Gaulle à Londres ?", ["Les Forces françaises libres", "Les FFI", "La Milice", "Les FTP"], "Les Forces françaises libres", "Elles combattent aux côtés des Alliés."),
  Q("Quelle bataille de 1942, en Libye, voit les Français libres de Koenig résister à Rommel ?", ["Bir Hakeim", "El-Alamein", "Tobrouk", "Monte Cassino"], "Bir Hakeim", "C'est un symbole de la France libre."),
  Q("Quel territoire africain se rallie en premier à la France libre en 1940 ?", ["Le Tchad, avec le gouverneur Félix Éboué", "Le Sénégal", "L'Algérie", "Le Maroc"], "Le Tchad, avec le gouverneur Félix Éboué", "Éboué est inhumé au Panthéon."),
]),
# ══ Avancé ══
notion('H3-1', 0, D, 'hg3d-plan-schlieffen', [
  Q("Comment s'appelle le plan allemand de 1914 prévoyant d'envahir la France par la Belgique ?", ["Le plan Schlieffen", "Le plan XVII", "Le plan Marshall", "Le plan Barbarossa"], "Le plan Schlieffen", "Il vise à vaincre la France avant la Russie."),
  Q("Pourquoi le Royaume-Uni entre-t-il en guerre en août 1914 ?", ["Après la violation de la neutralité belge", "Après l'attaque de Londres", "Pour soutenir l'Allemagne", "Après Pearl Harbor"], "Après la violation de la neutralité belge", "Il garantissait cette neutralité depuis 1839."),
  Q("Comment appelle-t-on l'union de tous les partis français face à la guerre en 1914 ?", ["L'Union sacrée", "Le Front populaire", "Le Bloc national", "Le Cartel des gauches"], "L'Union sacrée", "L'expression est du président Poincaré."),
]),
notion('H3-1', 0, D, 'hg3d-fusilles-exemple', [
  Q("Comment appelle-t-on les soldats exécutés par l'armée française pour désobéissance pendant la Grande Guerre ?", ["Les fusillés pour l'exemple", "Les gueules cassées", "Les embusqués", "Les mutins de Kiel"], "Les fusillés pour l'exemple", "Environ 600 soldats sont exécutés."),
  Q("Comment appelle-t-on les soldats suspectés d'avoir évité le front grâce à des appuis ?", ["Les embusqués", "Les poilus", "Les planqués de Verdun", "Les tirailleurs"], "Les embusqués", "Ils sont mal vus par les combattants."),
  Q("Quelle chanson anonyme de 1917 exprime la colère des soldats ?", ["La Chanson de Craonne", "La Marseillaise", "Le Chant des partisans", "La Madelon"], "La Chanson de Craonne", "Elle est longtemps interdite."),
]),
notion('H3-1', 0, D, 'hg3d-traites-paix', [
  Q("Quel principe défendu par le président Wilson inspire les traités de 1919-1920 ?", ["Le droit des peuples à disposer d'eux-mêmes", "La colonisation", "Le droit divin", "L'équilibre des races"], "Le droit des peuples à disposer d'eux-mêmes", "Il fait partie de ses « 14 points »."),
  Q("Quel traité de 1920 réduit fortement le territoire de la Hongrie ?", ["Le traité de Trianon", "Le traité de Sèvres", "Le traité de Saint-Germain", "Le traité de Neuilly"], "Le traité de Trianon", "La Hongrie perd les deux tiers de son territoire."),
  Q("Comment les Allemands qualifient-ils le traité de Versailles ?", ["De « diktat », une paix imposée", "De paix juste", "D'alliance", "De libération"], "De « diktat », une paix imposée", "Ce ressentiment nourrit le nazisme."),
]),
notion('H3-1', 0, D, 'hg3d-bilan-1418', [
  Q("Combien de morts au total fait la Première Guerre mondiale (militaires et civils) ?", ["Environ 18 à 20 millions", "Environ 1 million", "Environ 60 millions", "Environ 200 000"], "Environ 18 à 20 millions", "Dont environ 10 millions de soldats."),
  Q("Quelle épidémie fait des dizaines de millions de morts en 1918-1919 ?", ["La grippe espagnole", "La peste", "Le choléra", "La tuberculose"], "La grippe espagnole", "Elle tue plus que la guerre elle-même."),
  Q("Quels empires disparaissent à l'issue de la Première Guerre mondiale ?", ["Allemand, austro-hongrois, russe et ottoman", "Britannique et français", "Japonais et chinois", "Aucun"], "Allemand, austro-hongrois, russe et ottoman", "La carte de l'Europe est redessinée."),
]),
notion('H3-1', 1, D, 'hg3d-weimar', [
  Q("Comment appelle-t-on la République allemande de 1919 à 1933 ?", ["La république de Weimar", "Le IIe Reich", "La RFA", "La RDA"], "La république de Weimar", "Elle naît dans une Allemagne vaincue."),
  N("En quelle année l'hyperinflation ruine-t-elle l'Allemagne, un dollar valant 4 200 milliards de marks ?", 1923, "Les économies des classes moyennes sont anéanties."),
  Q("Quelle tentative de coup d'État Hitler mène-t-il à Munich en 1923 ?", ["Le putsch de la Brasserie", "La Nuit des longs couteaux", "L'incendie du Reichstag", "L'Anschluss"], "Le putsch de la Brasserie", "En prison, il écrit Mein Kampf."),
]),
notion('H3-1', 1, D, 'hg3d-nuit-longs-couteaux', [
  Q("Quelle organisation paramilitaire nazie est décapitée lors de la Nuit des longs couteaux en 1934 ?", ["Les SA", "Les SS", "La Gestapo", "La Wehrmacht"], "Les SA", "Leur chef Ernst Röhm est assassiné."),
  Q("Quel titre Hitler prend-il à la mort du président Hindenburg en août 1934 ?", ["Führer et chancelier du Reich", "Kaiser", "Président de la République", "Duce"], "Führer et chancelier du Reich", "Il cumule tous les pouvoirs."),
  Q("Comment appelle-t-on la mise au pas de toute la société par le régime nazi ?", ["La Gleichschaltung", "Le Lebensraum", "L'Anschluss", "La Kristallnacht"], "La Gleichschaltung", "Syndicats et partis sont dissous dès 1933."),
]),
notion('H3-1', 1, D, 'hg3d-culte-chef', [
  Q("Quel trait commun aux régimes totalitaires consiste à vénérer le dirigeant ?", ["Le culte de la personnalité", "Le pluralisme", "La séparation des pouvoirs", "L'alternance"], "Le culte de la personnalité", "Staline est appelé le « Petit Père des peuples »."),
  Q("Quel ministre nazi dirige la propagande ?", ["Joseph Goebbels", "Heinrich Himmler", "Hermann Göring", "Rudolf Hess"], "Joseph Goebbels", "Il contrôle presse, radio et cinéma."),
  Q("Quelle cinéaste réalise Le Triomphe de la volonté pour la propagande nazie ?", ["Leni Riefenstahl", "Marlene Dietrich", "Fritz Lang", "Sergueï Eisenstein"], "Leni Riefenstahl", "Le film montre le congrès de Nuremberg de 1934."),
]),
notion('H3-1', 1, D, 'hg3d-crise-1929-europe', [
  Q("Quel « jeudi noir » d'octobre 1929 marque le krach de Wall Street ?", ["Le 24 octobre 1929", "Le 11 novembre 1929", "Le 1er janvier 1929", "Le 14 juillet 1929"], "Le 24 octobre 1929", "La crise s'étend au monde."),
  Q("Combien de chômeurs l'Allemagne compte-t-elle environ en 1932 ?", ["Environ 6 millions", "Environ 60 000", "Environ 600 000", "Environ 60 millions"], "Environ 6 millions", "La crise favorise la montée du parti nazi."),
  Q("Quelle politique Roosevelt lance-t-il en 1933 face à la crise ?", ["Le New Deal", "Le plan Marshall", "Le libre-échange intégral", "La Prohibition"], "Le New Deal", "L'État intervient dans l'économie."),
]),
notion('H3-1', 2, D, 'hg3d-guerre-aneantissement', [
  Q("Comment appelle-t-on une guerre qui vise à détruire totalement l'ennemi, y compris les civils ?", ["Une guerre d'anéantissement", "Une guerre en dentelles", "Une guerre froide", "Une guerre de position"], "Une guerre d'anéantissement", "C'est le cas sur le front de l'Est."),
  Q("Combien de morts fait environ la Seconde Guerre mondiale ?", ["Environ 60 millions", "Environ 6 millions", "Environ 20 millions", "Environ 600 millions"], "Environ 60 millions", "Plus de la moitié sont des civils."),
  Q("Quel pays compte le plus de morts pendant la Seconde Guerre mondiale ?", ["L'URSS", "La France", "Les États-Unis", "Le Royaume-Uni"], "L'URSS", "Environ 26 millions de morts."),
]),
notion('H3-1', 2, D, 'hg3d-bombardements', [
  Q("Quelle ville allemande est détruite par un bombardement allié massif en février 1945 ?", ["Dresde", "Munich", "Bonn", "Francfort"], "Dresde", "Des dizaines de milliers de civils y meurent."),
  Q("Quelle ville basque est bombardée par l'aviation allemande en 1937 ?", ["Guernica", "Bilbao", "Madrid", "Barcelone"], "Guernica", "Picasso en fait un tableau célèbre."),
  Q("Combien de jours dure le siège de Leningrad ?", ["Environ 900 jours", "Environ 9 jours", "Environ 90 jours", "Environ 9 000 jours"], "Environ 900 jours", "Près d'un million de civils y meurent, surtout de faim."),
]),
notion('H3-1', 2, D, 'hg3d-shoah-etapes', [
  Q("Comment appelle-t-on les quartiers fermés où les nazis enferment les Juifs en Pologne ?", ["Les ghettos", "Les kibboutz", "Les camps de vacances", "Les mellahs"], "Les ghettos", "Celui de Varsovie est le plus grand."),
  N("En quelle année a lieu l'insurrection du ghetto de Varsovie ?", 1943, "Elle est écrasée en mai 1943."),
  Q("Combien de Juifs environ sont assassinés pendant la Shoah ?", ["Près de 6 millions", "Environ 600 000", "Environ 60 000", "Environ 20 millions"], "Près de 6 millions", "Environ les deux tiers des Juifs d'Europe."),
]),
notion('H3-1', 2, D, 'hg3d-proces-nuremberg', [
  Q("Quel procès juge les principaux dirigeants nazis en 1945-1946 ?", ["Le procès de Nuremberg", "Le procès de Riom", "Le procès Eichmann", "Le procès de Moscou"], "Le procès de Nuremberg", "Il est mené par les vainqueurs."),
  Q("Quelle nouvelle notion juridique est définie lors du procès de Nuremberg ?", ["Le crime contre l'humanité", "Le crime de lèse-majesté", "La haute trahison", "Le délit de presse"], "Le crime contre l'humanité", "Le mot « génocide » est forgé par Raphael Lemkin en 1944."),
  N("En quelle année Adolf Eichmann est-il jugé à Jérusalem ?", 1961, "Le procès donne la parole aux survivants."),
]),
notion('H3-1', 3, D, 'hg3d-vichy-shoah', [
  Q("Par quel camp du nord de Paris passent la plupart des Juifs déportés de France ?", ["Drancy", "Gurs", "Compiègne", "Rivesaltes"], "Drancy", "Environ 63 000 y transitent."),
  Q("Combien de Juifs sont déportés de France pendant la guerre ?", ["Environ 75 000", "Environ 7 500", "Environ 750 000", "Environ 7 millions"], "Environ 75 000", "Très peu reviennent."),
  Q("Quel président reconnaît en 1995 la responsabilité de l'État français dans la déportation des Juifs ?", ["Jacques Chirac", "François Mitterrand", "Charles de Gaulle", "Nicolas Sarkozy"], "Jacques Chirac", "Il le fait lors de la commémoration du Vel' d'Hiv."),
]),
notion('H3-1', 3, D, 'hg3d-milice-cnr', [
  Q("Quelle force paramilitaire française traque les résistants à partir de 1943 ?", ["La Milice", "La Gestapo", "Les FFI", "La Garde républicaine"], "La Milice", "Elle est créée par Joseph Darnand."),
  Q("Quel organisme réunit en 1943 les mouvements de résistance, les partis et les syndicats ?", ["Le Conseil national de la Résistance (CNR)", "Le Comité de salut public", "Le gouvernement de Vichy", "L'ONU"], "Le Conseil national de la Résistance (CNR)", "Sa première réunion a lieu à Paris le 27 mai 1943."),
  Q("Combien d'habitants une division SS massacre-t-elle à Oradour-sur-Glane le 10 juin 1944 ?", ["642", "42", "6 420", "Aucun"], "642", "Le village martyr a été conservé en ruines."),
]),
notion('H3-1', 3, D, 'hg3d-epuration', [
  Q("Comment appelle-t-on la punition des collaborateurs à la Libération ?", ["L'épuration", "L'amnistie", "La réconciliation", "La décolonisation"], "L'épuration", "Elle est d'abord sauvage puis légale."),
  Q("À quelle peine Pétain est-il condamné en 1945 ?", ["À mort, peine commuée en détention à perpétuité", "À l'exil en Espagne", "À une simple amende", "Il est acquitté"], "À mort, peine commuée en détention à perpétuité", "De Gaulle commue la peine en raison de son âge."),
  Q("Quel chef du gouvernement de Vichy est exécuté en 1945 ?", ["Pierre Laval", "Philippe Pétain", "François Darlan", "Joseph Darnand"], "Pierre Laval", "Darnand est aussi exécuté la même année."),
]),
]
