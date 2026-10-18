# Histoire 3e · Le monde depuis 1945 : au moins 50 questions par niveau
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Facile ══
notion('H3-2', 0, F, 'hg3-gandhi', [
  Q("Quelle méthode Gandhi utilise-t-il pour lutter contre les Britanniques ?", ["La non-violence et la désobéissance civile", "La guérilla", "Le terrorisme", "La guerre ouverte"], "La non-violence et la désobéissance civile", "La marche du sel de 1930 en est un exemple."),
  Q("Quels deux États naissent de la partition de l'Inde britannique en 1947 ?", ["L'Inde et le Pakistan", "L'Inde et la Chine", "Le Pakistan et l'Iran", "L'Inde et le Népal"], "L'Inde et le Pakistan", "La partition provoque d'immenses violences."),
  N("En quelle année Gandhi est-il assassiné ?", 1948, "Il est tué par un nationaliste hindou."),
]),
notion('H3-2', 0, F, 'hg3-algerie-guerre', [
  N("En quelle année commence la guerre d'Algérie ?", 1954, "Elle débute le 1er novembre, la « Toussaint rouge »."),
  Q("Quel mouvement indépendantiste algérien mène la lutte armée contre la France ?", ["Le FLN", "L'OAS", "Le Viêt-minh", "L'ANC"], "Le FLN", "Front de libération nationale."),
  Q("Comment appelle-t-on les Français d'Algérie qui rejoignent la métropole en 1962 ?", ["Les pieds-noirs", "Les harkis", "Les colons du Maroc", "Les rapatriés d'Indochine"], "Les pieds-noirs", "Près d'un million quittent l'Algérie."),
]),
notion('H3-2', 0, F, 'hg3-afrique-independances', [
  Q("Comment appelle-t-on l'année 1960, où 17 pays d'Afrique deviennent indépendants ?", ["L'année de l'Afrique", "L'année de l'Europe", "L'année des Nations", "L'année zéro"], "L'année de l'Afrique", "La plupart sont d'anciennes colonies françaises."),
  Q("Quel pays d'Afrique de l'Ouest dirigé par Léopold Sédar Senghor devient indépendant en 1960 ?", ["Le Sénégal", "Le Ghana", "Le Nigeria", "Le Kenya"], "Le Sénégal", "Senghor est aussi un grand poète."),
  Q("Quel pays devient en 1957 la première colonie d'Afrique noire indépendante ?", ["Le Ghana", "Le Sénégal", "Le Congo", "Madagascar"], "Le Ghana", "Kwame Nkrumah le dirige."),
]),
notion('H3-2', 0, F, 'hg3-colonisation-fin', [
  Q("Quelle guerre mondiale affaiblit les puissances coloniales et accélère la décolonisation ?", ["La Seconde Guerre mondiale", "La Première Guerre mondiale", "La guerre de Cent Ans", "La guerre froide"], "La Seconde Guerre mondiale", "Les colonisés ont aussi combattu pour les Alliés."),
  Q("Quelle organisation, créée en 1945, défend le droit des peuples à disposer d'eux-mêmes ?", ["L'ONU", "L'OTAN", "La CEE", "Le pacte de Varsovie"], "L'ONU", "Sa charte proclame ce principe."),
  Q("Comment appelle-t-on un pays qui vient d'obtenir son indépendance ?", ["Un nouvel État", "Une colonie", "Un protectorat", "Une métropole"], "Un nouvel État", "Il doit construire ses institutions."),
]),
notion('H3-2', 1, F, 'hg3-blocs', [
  Q("Quel système politique et économique défendent les États-Unis pendant la guerre froide ?", ["La démocratie libérale et le capitalisme", "Le communisme", "La monarchie absolue", "Le fascisme"], "La démocratie libérale et le capitalisme", "On parle du bloc de l'Ouest."),
  Q("Quel modèle défend l'URSS ?", ["Le communisme", "Le capitalisme", "La monarchie", "L'anarchisme"], "Le communisme", "On parle du bloc de l'Est."),
  Q("Comment Churchill appelle-t-il en 1946 la frontière qui sépare l'Europe en deux ?", ["Le rideau de fer", "Le mur de Berlin", "La ligne Maginot", "La ligne Oder-Neisse"], "Le rideau de fer", "Il traverse l'Europe de la Baltique à l'Adriatique."),
]),
notion('H3-2', 1, F, 'hg3-berlin', [
  Q("En combien de zones l'Allemagne est-elle divisée après 1945 ?", ["Quatre", "Deux", "Trois", "Six"], "Quatre", "Américaine, britannique, française et soviétique."),
  Q("Quels deux États allemands naissent en 1949 ?", ["La RFA et la RDA", "La Prusse et la Bavière", "L'Autriche et la Suisse", "L'Allemagne et la Pologne"], "La RFA et la RDA", "La RFA à l'Ouest, la RDA à l'Est."),
  N("En quelle année l'Allemagne est-elle réunifiée ?", 1990, "Le 3 octobre 1990."),
]),
notion('H3-2', 1, F, 'hg3-course-espace', [
  Q("Quel pays lance le premier satellite artificiel, Spoutnik, en 1957 ?", ["L'URSS", "Les États-Unis", "La France", "La Chine"], "L'URSS", "C'est un choc pour les Américains."),
  Q("Qui est le premier homme dans l'espace en 1961 ?", ["Youri Gagarine", "Neil Armstrong", "Thomas Pesquet", "Buzz Aldrin"], "Youri Gagarine", "Il est soviétique."),
  N("En quelle année Neil Armstrong marche-t-il sur la Lune ?", 1969, "C'est la mission Apollo 11."),
]),
notion('H3-2', 1, F, 'hg3-armes-nucleaires', [
  Q("Pourquoi parle-t-on de « guerre froide » ?", ["Les deux Grands ne s'affrontent jamais directement", "Elle se déroule en hiver", "Elle a lieu au pôle Nord", "Personne n'y meurt"], "Les deux Grands ne s'affrontent jamais directement", "Ils s'affrontent indirectement dans d'autres pays."),
  Q("Quelle arme rend un affrontement direct entre les deux Grands trop dangereux ?", ["L'arme nucléaire", "Le char", "Le fusil", "Le sous-marin classique"], "L'arme nucléaire", "On parle d'« équilibre de la terreur »."),
  N("En quelle année l'URSS fait-elle exploser sa première bombe atomique ?", 1949, "Les États-Unis perdent leur monopole."),
]),
notion('H3-2', 2, F, 'hg3-ue-symboles', [
  Q("Combien d'étoiles figurent sur le drapeau européen ?", ["Douze", "Vingt-sept", "Six", "Quinze"], "Douze", "Ce nombre symbolise la perfection, pas le nombre de pays."),
  Q("Quel est l'hymne de l'Union européenne ?", ["L'Ode à la joie de Beethoven", "La Marseillaise", "God Save the King", "Le Boléro de Ravel"], "L'Ode à la joie de Beethoven", "Il est extrait de la 9e symphonie."),
  Q("Quel jour est célébrée la journée de l'Europe ?", ["Le 9 mai", "Le 14 juillet", "Le 1er janvier", "Le 11 novembre"], "Le 9 mai", "En souvenir de la déclaration Schuman de 1950."),
]),
notion('H3-2', 2, F, 'hg3-ue-institutions', [
  Q("Dans quelle ville siège le Parlement européen ?", ["Strasbourg", "Paris", "Londres", "Rome"], "Strasbourg", "Il siège aussi à Bruxelles."),
  Q("Comment sont élus les députés européens ?", ["Au suffrage universel direct par les citoyens", "Par les présidents", "Par tirage au sort", "Par le pape"], "Au suffrage universel direct par les citoyens", "Depuis 1979."),
  Q("Combien de pays compte l'Union européenne depuis le départ du Royaume-Uni ?", ["27", "28", "12", "15"], "27", "Le Royaume-Uni est sorti en 2020."),
]),
notion('H3-2', 2, F, 'hg3-europe-libre-circulation', [
  Q("Quel espace permet de circuler sans contrôle aux frontières entre de nombreux pays européens ?", ["L'espace Schengen", "La zone euro", "Le Conseil de l'Europe", "L'OTAN"], "L'espace Schengen", "Les accords sont signés en 1985."),
  Q("Quel programme permet aux étudiants d'étudier dans un autre pays européen ?", ["Erasmus", "Galileo", "Airbus", "Schengen"], "Erasmus", "Il est créé en 1987."),
  Q("Quel pays a quitté l'Union européenne après un référendum en 2016 ?", ["Le Royaume-Uni", "La Suisse", "La Norvège", "La Grèce"], "Le Royaume-Uni", "On parle du Brexit."),
]),
notion('H3-2', 3, F, 'hg3-attentats-2001', [
  N("En quelle année ont lieu les attentats contre les tours jumelles de New York ?", 2001, "Le 11 septembre 2001."),
  Q("Quelle organisation terroriste revendique les attentats du 11 septembre 2001 ?", ["Al-Qaïda", "L'IRA", "L'ETA", "Le Hamas"], "Al-Qaïda", "Elle est dirigée par Oussama Ben Laden."),
  Q("Quel pays les États-Unis attaquent-ils en octobre 2001 en réponse aux attentats ?", ["L'Afghanistan", "L'Irak", "L'Iran", "La Syrie"], "L'Afghanistan", "Le régime des talibans y protège Al-Qaïda."),
]),
notion('H3-2', 3, F, 'hg3-mondialisation', [
  Q("Comment appelle-t-on la mise en relation croissante des différentes parties du monde par les échanges ?", ["La mondialisation", "La colonisation", "La guerre froide", "La décolonisation"], "La mondialisation", "Elle s'accélère après 1989."),
  Q("Quel outil de communication transforme le monde à partir des années 1990 ?", ["Internet", "Le télégraphe", "La radio", "Le minitel seulement"], "Internet", "Il relie des milliards de personnes."),
  Q("Quel pays devient la deuxième puissance économique mondiale au XXIe siècle ?", ["La Chine", "La France", "Le Brésil", "Le Japon"], "La Chine", "Elle dépasse le Japon en 2010."),
]),
notion('H3-2', 1, F, 'hg3-fin-urss', [
  Q("Quel dirigeant soviétique lance des réformes à partir de 1985 ?", ["Mikhaïl Gorbatchev", "Staline", "Brejnev", "Poutine"], "Mikhaïl Gorbatchev", "Il est le dernier dirigeant de l'URSS."),
  Q("Que devient la Russie après la disparition de l'URSS ?", ["Un État indépendant, la Fédération de Russie", "Une colonie américaine", "Une monarchie", "Une partie de la Chine"], "Un État indépendant, la Fédération de Russie", "Boris Eltsine en est le premier président."),
  Q("Combien d'États indépendants naissent de l'éclatement de l'URSS ?", ["Quinze", "Deux", "Cinquante", "Cinq"], "Quinze", "Ce sont les anciennes républiques soviétiques."),
]),
# ══ Intermédiaire ══
notion('H3-2', 0, I, 'hg3i-dien-bien-phu', [
  N("En quelle année l'armée française est-elle vaincue à Diên Biên Phu ?", 1954, "La défaite met fin à la guerre d'Indochine."),
  Q("Quel dirigeant communiste vietnamien proclame l'indépendance en 1945 ?", ["Hô Chi Minh", "Mao Zedong", "Pol Pot", "Sukarno"], "Hô Chi Minh", "Il dirige le Viêt-minh."),
  Q("Quels accords de 1954 divisent le Vietnam en deux le long du 17e parallèle ?", ["Les accords de Genève", "Les accords d'Évian", "Les accords de Paris", "Les accords de Camp David"], "Les accords de Genève", "Le Nord est communiste, le Sud pro-occidental."),
]),
notion('H3-2', 0, I, 'hg3i-de-gaulle-algerie', [
  Q("Quelle crise de mai 1958 à Alger ramène de Gaulle au pouvoir ?", ["Le putsch du 13 mai 1958", "La Toussaint rouge", "La bataille d'Alger", "Le putsch des généraux de 1961"], "Le putsch du 13 mai 1958", "La IVe République s'effondre."),
  Q("Quelle organisation clandestine s'oppose violemment à l'indépendance de l'Algérie ?", ["L'OAS", "Le FLN", "Le MNA", "L'ALN"], "L'OAS", "Organisation armée secrète."),
  Q("Comment appelle-t-on les Algériens musulmans qui ont combattu aux côtés de l'armée française ?", ["Les harkis", "Les pieds-noirs", "Les fellaghas", "Les moudjahidines"], "Les harkis", "Beaucoup sont massacrés après 1962, d'autres sont mal accueillis en France."),
]),
notion('H3-2', 0, I, 'hg3i-suez-1956', [
  Q("Quel dirigeant égyptien nationalise le canal de Suez en 1956 ?", ["Nasser", "Sadate", "Moubarak", "Farouk"], "Nasser", "Il devient un héros du monde arabe."),
  Q("Quels pays attaquent l'Égypte lors de la crise de Suez ?", ["Le Royaume-Uni, la France et Israël", "Les États-Unis et l'URSS", "L'Italie et l'Espagne", "La Turquie et l'Iran"], "Le Royaume-Uni, la France et Israël", "Ils doivent se retirer sous la pression des deux Grands."),
  Q("Que montre la crise de Suez ?", ["Le déclin des anciennes puissances coloniales face aux deux Grands", "La force de la France", "La victoire du Royaume-Uni", "La fin de la guerre froide"], "Le déclin des anciennes puissances coloniales face aux deux Grands", "Les États-Unis et l'URSS imposent le cessez-le-feu."),
]),
notion('H3-2', 0, I, 'hg3i-nouveaux-etats-defis', [
  Q("Quel défi économique rencontrent souvent les nouveaux États ?", ["La pauvreté et la dépendance aux exportations de matières premières", "Un excès d'industries", "Une population trop âgée", "Un manque de terres"], "La pauvreté et la dépendance aux exportations de matières premières", "On parle de pays en développement."),
  Q("Comment appelle-t-on la domination économique qui persiste après l'indépendance ?", ["Le néocolonialisme", "Le mercantilisme", "Le féodalisme", "L'isolationnisme"], "Le néocolonialisme", "L'ancienne métropole garde souvent une forte influence."),
  Q("Quel type de régime s'installe dans de nombreux nouveaux États africains ?", ["Des régimes à parti unique", "Des démocraties pluralistes durables", "Des monarchies absolues", "Des républiques fédérales"], "Des régimes à parti unique", "Les coups d'État militaires sont nombreux."),
]),
notion('H3-2', 1, I, 'hg3i-guerres-chaudes', [
  Q("Quelle guerre oppose le Nord communiste et le Sud pro-américain de 1950 à 1953 en Asie ?", ["La guerre de Corée", "La guerre du Vietnam", "La guerre d'Afghanistan", "La guerre du Golfe"], "La guerre de Corée", "Elle se termine au 38e parallèle."),
  Q("Quelle guerre engage massivement les États-Unis en Asie du Sud-Est jusqu'en 1973 ?", ["La guerre du Vietnam", "La guerre de Corée", "La guerre d'Indochine", "La guerre des Six Jours"], "La guerre du Vietnam", "Elle provoque d'immenses manifestations pacifistes."),
  Q("Quel pays l'URSS envahit-il en 1979 ?", ["L'Afghanistan", "La Pologne", "Cuba", "Le Vietnam"], "L'Afghanistan", "Les Soviétiques s'y enlisent jusqu'en 1989."),
]),
notion('H3-2', 1, I, 'hg3i-doctrines', [
  Q("Quelle doctrine américaine de 1947 vise à contenir l'expansion du communisme ?", ["La doctrine Truman (endiguement)", "La doctrine Monroe", "La doctrine Jdanov", "La doctrine Brejnev"], "La doctrine Truman (endiguement)", "Le mot anglais est « containment »."),
  Q("Quelle doctrine soviétique de 1947 dénonce l'impérialisme américain ?", ["La doctrine Jdanov", "La doctrine Truman", "Le plan Marshall", "La doctrine Monroe"], "La doctrine Jdanov", "Elle divise le monde en deux camps."),
  Q("Comment appelle-t-on la période de détente amorcée après la crise de Cuba ?", ["La coexistence pacifique et la détente", "La guerre fraîche", "La guerre totale", "Le printemps des peuples"], "La coexistence pacifique et la détente", "Un « téléphone rouge » relie Washington et Moscou."),
]),
notion('H3-2', 1, I, 'hg3i-revoltes-est', [
  Q("Quel soulèvement de 1956 contre la domination soviétique est écrasé par les chars ?", ["L'insurrection de Budapest", "Le Printemps de Prague", "Solidarność", "La révolution de velours"], "L'insurrection de Budapest", "La Hongrie reste dans le bloc soviétique."),
  Q("Comment appelle-t-on la tentative de libéralisation en Tchécoslovaquie en 1968 ?", ["Le Printemps de Prague", "La révolution de velours", "La révolution orange", "Le dégel"], "Le Printemps de Prague", "Il est écrasé par les troupes du pacte de Varsovie."),
  Q("Quel syndicat indépendant, dirigé par Lech Wałęsa, s'oppose au régime communiste polonais ?", ["Solidarność", "La CGT", "Le Komsomol", "La Stasi"], "Solidarność", "Il est fondé en 1980 à Gdańsk."),
]),
notion('H3-2', 2, I, 'hg3i-elargissements', [
  Q("Quels pays rejoignent la CEE en 1973 ?", ["Le Royaume-Uni, l'Irlande et le Danemark", "L'Espagne et le Portugal", "La Pologne et la Hongrie", "La Suède et la Finlande"], "Le Royaume-Uni, l'Irlande et le Danemark", "C'est le premier élargissement."),
  N("En quelle année dix nouveaux pays, surtout d'Europe de l'Est, rejoignent-ils l'Union européenne ?", 2004, "C'est le plus grand élargissement."),
  Q("Quels pays rejoignent la CEE en 1986 après la fin de leurs dictatures ?", ["L'Espagne et le Portugal", "La Grèce et Chypre", "L'Autriche et la Suède", "La Croatie et la Slovénie"], "L'Espagne et le Portugal", "La Grèce était entrée en 1981."),
]),
notion('H3-2', 2, I, 'hg3i-reconciliation', [
  Q("Quel traité de 1963 scelle la réconciliation franco-allemande ?", ["Le traité de l'Élysée", "Le traité de Rome", "Le traité de Versailles", "Le traité de Maastricht"], "Le traité de l'Élysée", "Il est signé par de Gaulle et Adenauer."),
  Q("Quels dirigeants se tiennent la main à Verdun en 1984 ?", ["François Mitterrand et Helmut Kohl", "De Gaulle et Adenauer", "Chirac et Schröder", "Macron et Merkel"], "François Mitterrand et Helmut Kohl", "C'est un symbole de la réconciliation."),
  Q("Quel chancelier allemand signe le traité de 1963 avec de Gaulle ?", ["Konrad Adenauer", "Willy Brandt", "Helmut Kohl", "Angela Merkel"], "Konrad Adenauer", "Il est le premier chancelier de la RFA."),
]),
notion('H3-2', 2, I, 'hg3i-euro', [
  N("En quelle année l'euro est-il créé comme monnaie de compte, avant les pièces et billets ?", 1999, "Les pièces et billets arrivent en 2002."),
  Q("Quelle institution, basée à Francfort, gère l'euro ?", ["La Banque centrale européenne", "La Commission européenne", "Le Parlement européen", "La Banque de France"], "La Banque centrale européenne", "Elle fixe les taux d'intérêt."),
  Q("Quel traité prévoit la création de la monnaie unique ?", ["Le traité de Maastricht", "Le traité de Rome", "Le traité de Lisbonne", "Le traité de l'Élysée"], "Le traité de Maastricht", "Il est signé en 1992."),
]),
notion('H3-2', 3, I, 'hg3i-conflits-moyen-orient', [
  N("En quelle année l'État d'Israël est-il créé ?", 1948, "Une guerre éclate aussitôt avec les pays arabes voisins."),
  Q("Quelle guerre de 2003 voit les États-Unis renverser Saddam Hussein ?", ["La guerre d'Irak", "La guerre du Golfe de 1991", "La guerre d'Afghanistan", "La guerre du Kippour"], "La guerre d'Irak", "La France s'y oppose à l'ONU."),
  Q("Quelle guerre civile ravage la Syrie à partir de 2011 ?", ["La guerre civile syrienne", "La guerre du Liban", "La guerre des Six Jours", "La guerre Iran-Irak"], "La guerre civile syrienne", "Elle suit les « printemps arabes »."),
]),
notion('H3-2', 3, I, 'hg3i-printemps-arabes', [
  Q("Dans quel pays commencent les « printemps arabes » fin 2010 ?", ["La Tunisie", "L'Égypte", "Le Maroc", "La Libye"], "La Tunisie", "Le président Ben Ali s'enfuit en janvier 2011."),
  Q("Quel président égyptien est renversé en 2011 ?", ["Hosni Moubarak", "Nasser", "Sadate", "Kadhafi"], "Hosni Moubarak", "La place Tahrir au Caire est le cœur de la contestation."),
  Q("Quel rôle jouent les réseaux sociaux dans les printemps arabes ?", ["Ils aident à mobiliser et à diffuser les images", "Aucun", "Ils sont interdits partout", "Ils remplacent les élections"], "Ils aident à mobiliser et à diffuser les images", "Facebook et Twitter sont très utilisés."),
]),
notion('H3-2', 3, I, 'hg3i-ukraine', [
  Q("Quelle péninsule ukrainienne la Russie annexe-t-elle en 2014 ?", ["La Crimée", "Le Donbass", "Odessa", "La Transnistrie"], "La Crimée", "L'annexion n'est pas reconnue par la communauté internationale."),
  N("En quelle année la Russie lance-t-elle une invasion à grande échelle de l'Ukraine ?", 2022, "Le 24 février 2022."),
  Q("Quelle alliance militaire la Finlande et la Suède rejoignent-elles après 2022 ?", ["L'OTAN", "Le pacte de Varsovie", "L'ONU", "Le G7"], "L'OTAN", "La Finlande y entre en 2023, la Suède en 2024."),
]),
# ══ Avancé ══
notion('H3-2', 0, D, 'hg3d-indonesie-madagascar', [
  Q("Quelle révolte de 1947 contre la France est durement réprimée à Madagascar ?", ["L'insurrection malgache", "La révolte des Mau-Mau", "La révolte de Sétif", "La révolte des Boxers"], "L'insurrection malgache", "La répression fait des dizaines de milliers de morts."),
  Q("Quels massacres de mai 1945 en Algérie annoncent la guerre d'indépendance ?", ["Les massacres de Sétif et Guelma", "La Toussaint rouge", "La bataille d'Alger", "Le 17 octobre 1961"], "Les massacres de Sétif et Guelma", "Ils ont lieu le jour de la victoire en Europe."),
  Q("Quel dirigeant proclame l'indépendance de l'Indonésie face aux Pays-Bas en 1945 ?", ["Sukarno", "Hô Chi Minh", "Nehru", "Suharto"], "Sukarno", "Les Pays-Bas la reconnaissent en 1949."),
]),
notion('H3-2', 0, D, 'hg3d-afrique-sud', [
  Q("Comment appelle-t-on le régime de ségrégation raciale en Afrique du Sud de 1948 à 1991 ?", ["L'apartheid", "Le code de l'indigénat", "Le Jim Crow", "Le système des castes"], "L'apartheid", "Le mot signifie « séparation » en afrikaans."),
  Q("Quel dirigeant de l'ANC passe 27 ans en prison avant de devenir président en 1994 ?", ["Nelson Mandela", "Desmond Tutu", "Steve Biko", "Thabo Mbeki"], "Nelson Mandela", "Il reçoit le prix Nobel de la paix en 1993."),
  Q("Quel président sud-africain blanc négocie la fin de l'apartheid avec Mandela ?", ["Frederik de Klerk", "Pieter Botha", "Jacob Zuma", "Ian Smith"], "Frederik de Klerk", "Ils partagent le prix Nobel de la paix."),
]),
notion('H3-2', 0, D, 'hg3d-guerre-algerie-violences', [
  Q("Quelle pratique de l'armée française pendant la guerre d'Algérie est dénoncée par des intellectuels comme Henri Alleg ?", ["La torture", "Le travail forcé", "Le blocus", "Les bombardements atomiques"], "La torture", "Son livre La Question est saisi en 1958."),
  Q("Que se passe-t-il à Paris le 17 octobre 1961 ?", ["La police réprime violemment une manifestation d'Algériens", "Un attentat du FLN à la tour Eiffel", "La signature de la paix", "Le retour des pieds-noirs"], "La police réprime violemment une manifestation d'Algériens", "Des dizaines de manifestants sont tués."),
  Q("Quelle manifestation contre l'OAS fait neuf morts au métro Charonne en 1962 ?", ["La manifestation du 8 février 1962", "Mai 68", "Le 6 février 1934", "La marche des Beurs"], "La manifestation du 8 février 1962", "La police charge les manifestants."),
]),
notion('H3-2', 0, D, 'hg3d-mouvement-non-alignes', [
  Q("Quel dirigeant yougoslave est l'un des fondateurs du mouvement des non-alignés ?", ["Tito", "Staline", "Ceaușescu", "Milošević"], "Tito", "Il a rompu avec Staline en 1948."),
  Q("Dans quelle ville se tient en 1961 la première conférence des non-alignés ?", ["Belgrade", "Bandung", "Le Caire", "New Delhi"], "Belgrade", "Elle réunit 25 pays."),
  Q("Quel Premier ministre indien est l'une des grandes figures du non-alignement ?", ["Nehru", "Gandhi", "Indira Gandhi", "Modi"], "Nehru", "Il gouverne l'Inde de 1947 à 1964."),
]),
notion('H3-2', 1, D, 'hg3d-cuba-details', [
  Q("Qui prend le pouvoir à Cuba en 1959 ?", ["Fidel Castro", "Che Guevara", "Batista", "Allende"], "Fidel Castro", "Il se rapproche de l'URSS."),
  Q("Quel débarquement anti-castriste, soutenu par la CIA, échoue en 1961 ?", ["La baie des Cochons", "Pearl Harbor", "La baie de Guantánamo", "Le débarquement de Normandie"], "La baie des Cochons", "C'est un échec pour Kennedy."),
  Q("Qu'obtient Kennedy en échange du retrait des missiles soviétiques de Cuba ?", ["Il promet de ne pas envahir Cuba et retire ensuite ses missiles de Turquie", "Il cède Berlin-Ouest", "Il quitte l'OTAN", "Rien"], "Il promet de ne pas envahir Cuba et retire ensuite ses missiles de Turquie", "Le retrait de Turquie reste secret."),
]),
notion('H3-2', 1, D, 'hg3d-chine-communiste', [
  N("En quelle année Mao Zedong proclame-t-il la République populaire de Chine ?", 1949, "Le 1er octobre 1949."),
  Q("Quelle campagne de Mao (1966-1976) vise à éliminer les opposants et les « vieilles idées » ?", ["La révolution culturelle", "Le Grand Bond en avant", "La Longue Marche", "Les Cent Fleurs"], "La révolution culturelle", "Les gardes rouges en sont les acteurs."),
  Q("Quelle rupture divise le camp communiste à partir de 1960 ?", ["La rupture sino-soviétique", "La rupture avec Cuba", "La rupture avec la RDA", "La rupture avec le Vietnam"], "La rupture sino-soviétique", "La Chine et l'URSS deviennent rivales."),
]),
notion('H3-2', 1, D, 'hg3d-traites-desarmement', [
  Q("Quel traité de 1972 limite les armes stratégiques des deux Grands ?", ["SALT I", "START", "TNP", "Pacte de Varsovie"], "SALT I", "Il marque la détente."),
  Q("Quel président américain relance la course aux armements dans les années 1980 avec la « guerre des étoiles » ?", ["Ronald Reagan", "Jimmy Carter", "Richard Nixon", "Bill Clinton"], "Ronald Reagan", "C'est l'Initiative de défense stratégique."),
  Q("Quel traité de 1968 vise à empêcher la diffusion des armes nucléaires ?", ["Le traité de non-prolifération (TNP)", "Le traité de Rome", "Le traité de Moscou", "Le traité FNI"], "Le traité de non-prolifération (TNP)", "La France le signe en 1992."),
]),
notion('H3-2', 1, D, 'hg3d-chute-democraties-populaires', [
  Q("Comment appelle-t-on la chute pacifique du régime communiste en Tchécoslovaquie en 1989 ?", ["La révolution de velours", "Le Printemps de Prague", "La révolution orange", "La révolution des œillets"], "La révolution de velours", "Václav Havel devient président."),
  Q("Quel dictateur roumain est renversé et exécuté en décembre 1989 ?", ["Nicolae Ceaușescu", "Erich Honecker", "Todor Jivkov", "Enver Hoxha"], "Nicolae Ceaușescu", "C'est la seule révolution violente de 1989."),
  Q("Quels mots russes désignent les réformes de Gorbatchev ?", ["Perestroïka et glasnost", "Spoutnik et Soyouz", "Kolkhoze et sovkhoze", "Goulag et NKVD"], "Perestroïka et glasnost", "Restructuration et transparence."),
]),
notion('H3-2', 2, D, 'hg3d-ced-echec', [
  Q("Quel projet d'armée européenne est rejeté par l'Assemblée française en 1954 ?", ["La Communauté européenne de défense (CED)", "La CECA", "Euratom", "L'espace Schengen"], "La Communauté européenne de défense (CED)", "La construction européenne se concentre ensuite sur l'économie."),
  Q("Quelle politique commune, lancée en 1962, soutient les agriculteurs européens ?", ["La politique agricole commune (PAC)", "Le marché unique", "L'euro", "Erasmus"], "La politique agricole commune (PAC)", "Elle représente longtemps l'essentiel du budget européen."),
  Q("Quelle crise de 1965-1966 voit la France pratiquer la « politique de la chaise vide » ?", ["La France boycotte les réunions européennes", "La France quitte l'OTAN", "La France sort de l'euro", "La France refuse Schengen"], "La France boycotte les réunions européennes", "Le compromis de Luxembourg y met fin."),
]),
notion('H3-2', 2, D, 'hg3d-referendums-europe', [
  N("En quelle année les Français rejettent-ils par référendum le traité établissant une Constitution pour l'Europe ?", 2005, "Les Néerlandais le rejettent aussi."),
  Q("Quel traité de 2007 reprend une grande partie du projet de Constitution européenne ?", ["Le traité de Lisbonne", "Le traité de Nice", "Le traité d'Amsterdam", "Le traité de Maastricht"], "Le traité de Lisbonne", "Il entre en vigueur en 2009."),
  Q("Quel résultat obtient en France le référendum sur Maastricht en 1992 ?", ["Un « oui » très serré (environ 51 %)", "Un « non » massif", "Un « oui » à 90 %", "Il est annulé"], "Un « oui » très serré (environ 51 %)", "L'Europe divise les Français."),
]),
notion('H3-2', 2, D, 'hg3d-fondateurs-europe', [
  Q("Quel Français, conseiller de Schuman, est considéré comme le « père de l'Europe » ?", ["Jean Monnet", "Winston Churchill", "Jacques Delors", "Charles de Gaulle"], "Jean Monnet", "Il préside la Haute Autorité de la CECA."),
  Q("Quel président de la Commission européenne (1985-1995) relance la construction européenne ?", ["Jacques Delors", "Jean Monnet", "Ursula von der Leyen", "José Manuel Barroso"], "Jacques Delors", "Il prépare le marché unique et l'euro."),
  Q("Quelle conception de l'Europe défend le général de Gaulle ?", ["Une « Europe des nations » qui préserve la souveraineté des États", "Une Europe fédérale", "Une Europe dirigée par les États-Unis", "Le refus de toute Europe"], "Une « Europe des nations » qui préserve la souveraineté des États", "Il s'oppose à l'entrée du Royaume-Uni."),
]),
notion('H3-2', 3, D, 'hg3d-rwanda-yougoslavie', [
  N("En quelle année a lieu le génocide des Tutsi au Rwanda ?", 1994, "Environ 800 000 personnes sont tuées en trois mois."),
  Q("Quel massacre de 1995 en Bosnie est qualifié de génocide par la justice internationale ?", ["Srebrenica", "Sarajevo", "Vukovar", "Mostar"], "Srebrenica", "Plus de 8 000 hommes et garçons musulmans y sont tués."),
  Q("Quel tribunal juge les crimes commis en ex-Yougoslavie ?", ["Le Tribunal pénal international pour l'ex-Yougoslavie (TPIY)", "Le tribunal de Nuremberg", "La Cour de cassation", "Le Conseil d'État"], "Le Tribunal pénal international pour l'ex-Yougoslavie (TPIY)", "Il siège à La Haye."),
]),
notion('H3-2', 3, D, 'hg3d-multipolarite', [
  Q("Comment appelle-t-on un monde organisé autour de plusieurs grandes puissances ?", ["Un monde multipolaire", "Un monde bipolaire", "Un monde unipolaire", "Un monde colonial"], "Un monde multipolaire", "Il succède à la domination américaine des années 1990."),
  Q("Quel groupe réunit le Brésil, la Russie, l'Inde, la Chine et l'Afrique du Sud ?", ["Les BRICS", "Le G7", "L'OTAN", "L'OPEP"], "Les BRICS", "Il s'élargit en 2024."),
  Q("Quelle cour, créée en 2002, juge les individus accusés de génocide et de crimes contre l'humanité ?", ["La Cour pénale internationale", "La Cour internationale de justice", "La Cour européenne des droits de l'homme", "Le Conseil de sécurité"], "La Cour pénale internationale", "Elle siège à La Haye."),
]),
notion('H3-2', 3, D, 'hg3d-terrorisme-jihadiste', [
  Q("Quelle organisation proclame un « califat » en Irak et en Syrie en 2014 ?", ["L'État islamique (Daech)", "Al-Qaïda", "Le Hezbollah", "Les talibans"], "L'État islamique (Daech)", "Il est vaincu militairement en 2017-2019."),
  Q("Quels attentats frappent Paris et Saint-Denis le 13 novembre 2015 ?", ["Les attentats du Bataclan, des terrasses et du Stade de France", "L'attentat de Charlie Hebdo", "L'attentat de Nice", "L'attentat du RER Saint-Michel"], "Les attentats du Bataclan, des terrasses et du Stade de France", "Ils font 130 morts."),
  Q("Quel pays les talibans reprennent-ils en 2021 après le retrait américain ?", ["L'Afghanistan", "L'Irak", "Le Pakistan", "La Syrie"], "L'Afghanistan", "Ils avaient été chassés en 2001."),
]),
]
