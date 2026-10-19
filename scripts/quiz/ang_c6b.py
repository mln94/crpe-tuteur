# Anglais · Repères culturels, 6e : Pays et paysages ; Imaginaire, contes et légendes ; Arts et expression des sentiments (25 questions par niveau)
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ C6-3 · Pays et paysages ══
notion('C6-3', 0, F, 'ang6-pays-capitales', [
  Q("Quelle est la capitale du Royaume-Uni ?", ["Londres", "Édimbourg", "Dublin", "Cardiff"], "Londres", "Édimbourg est la capitale de l'Écosse, Cardiff celle du pays de Galles."),
  Q("Quelle est la capitale des États-Unis ?", ["Washington, D.C.", "New York", "Los Angeles", "Chicago"], "Washington, D.C.", "D.C. signifie District of Columbia."),
  Q("Quelle est la capitale du Canada ?", ["Ottawa", "Toronto", "Montréal", "Vancouver"], "Ottawa", "Toronto est la plus grande ville."),
]),
notion('C6-3', 0, F, 'ang6-paysages-vocabulaire', [
  Q("Que signifie « mountain » ?", ["Montagne", "Rivière", "Forêt", "Plage"], "Montagne", "River = rivière, forest = forêt."),
  Q("Comment dit-on « plage » en anglais ?", ["Beach", "Coast", "Cliff", "Island"], "Beach", "Cliff = falaise, island = île."),
  Q("Que signifie « lake » ?", ["Lac", "Mer", "Désert", "Colline"], "Lac", "Hill = colline."),
]),
notion('C6-3', 0, F, 'ang6-animaux-sauvages', [
  Q("Comment dit-on « ours » en anglais ?", ["Bear", "Wolf", "Fox", "Deer"], "Bear", "Wolf = loup, fox = renard, deer = cerf."),
  Q("Quel animal est un symbole du Canada et figure sur une pièce de 5 cents ?", ["Le castor (beaver)", "Le kangourou", "Le kiwi", "Le lion"], "Le castor (beaver)", "La feuille d'érable figure sur le drapeau."),
  Q("Quel oiseau qui ne vole pas est le symbole de la Nouvelle-Zélande ?", ["Le kiwi", "L'aigle", "Le perroquet", "Le cygne"], "Le kiwi", "Les Néo-Zélandais sont surnommés « Kiwis »."),
]),
notion('C6-3', 0, F, 'ang6-points-cardinaux', [
  Q("Comment dit-on « nord » en anglais ?", ["North", "South", "East", "West"], "North", "South = sud, East = est, West = ouest."),
  Q("Où se trouve l'Écosse par rapport à l'Angleterre ?", ["Au nord", "Au sud", "À l'est", "À l'ouest"], "Au nord", "Le pays de Galles est à l'ouest."),
  Q("Que signifie « the Far West » aux États-Unis ?", ["L'Ouest lointain, conquis au XIXe siècle", "Le nord du Canada", "La côte est", "Le sud du Mexique"], "L'Ouest lointain, conquis au XIXe siècle", "C'est le décor des westerns."),
]),
notion('C6-3', 0, F, 'ang6-drapeaux', [
  Q("Comment appelle-t-on le drapeau du Royaume-Uni ?", ["L'Union Jack", "Le Stars and Stripes", "Le Maple Leaf", "Le Tricolore"], "L'Union Jack", "Il réunit les croix de saint Georges, saint André et saint Patrick."),
  Q("Combien d'étoiles compte le drapeau des États-Unis ?", ["50", "13", "48", "100"], "50", "Une par État ; les 13 bandes rappellent les 13 colonies."),
  Q("Quelle feuille figure sur le drapeau du Canada ?", ["Une feuille d'érable", "Une feuille de chêne", "Un trèfle", "Une feuille de palmier"], "Une feuille d'érable", "Le sirop d'érable est une spécialité canadienne."),
]),
notion('C6-3', 0, F, 'ang6-pays-anglophones-carte', [
  Q("Dans quel océan se trouvent les îles Britanniques ?", ["L'océan Atlantique", "L'océan Pacifique", "L'océan Indien", "L'océan Arctique"], "L'océan Atlantique", "La Manche les sépare de la France."),
  Q("Sur quel continent se trouve l'Australie ?", ["L'Océanie", "L'Asie", "L'Afrique", "L'Amérique"], "L'Océanie", "C'est à la fois un pays et un continent."),
  Q("Quel pays anglophone d'Afrique a pour plus grande ville Lagos ?", ["Le Nigeria", "Le Kenya", "L'Afrique du Sud", "Le Ghana"], "Le Nigeria", "L'anglais y est langue officielle."),
]),
notion('C6-3', 0, F, 'ang6-monuments', [
  Q("Comment s'appelle la grande horloge du palais de Westminster, à Londres ?", ["Big Ben", "Tower Bridge", "London Eye", "Buckingham"], "Big Ben", "C'est en fait le nom de la cloche ; la tour s'appelle Elizabeth Tower."),
  Q("Où vit le roi d'Angleterre à Londres ?", ["Au palais de Buckingham", "À la tour de Londres", "À Westminster", "À Windsor uniquement"], "Au palais de Buckingham", "La relève de la garde y attire les touristes."),
  Q("Quelle statue géante se dresse à l'entrée du port de New York ?", ["La statue de la Liberté", "Le Christ rédempteur", "La statue de Lincoln", "Le Penseur"], "La statue de la Liberté", "Elle a été offerte par la France."),
]),
notion('C6-3', 0, I, 'ang6i-parcs-nationaux', [
  Q("Quel parc national américain, le premier du monde, est célèbre pour ses geysers ?", ["Yellowstone", "Yosemite", "Grand Canyon", "Everglades"], "Yellowstone", "Il est créé en 1872."),
  Q("Quel immense ravin creusé par le fleuve Colorado se trouve en Arizona ?", ["Le Grand Canyon", "La Vallée de la Mort", "Le Mont Rushmore", "Les chutes du Niagara"], "Le Grand Canyon", "Il fait près de 1,8 km de profondeur."),
  Q("Quelles célèbres chutes d'eau se trouvent à la frontière entre le Canada et les États-Unis ?", ["Les chutes du Niagara", "Les chutes Victoria", "Les chutes d'Iguazu", "Les chutes Angel"], "Les chutes du Niagara", "Les chutes Victoria sont en Afrique australe."),
]),
notion('C6-3', 0, I, 'ang6i-australie-nature', [
  Q("Quel immense rocher rouge sacré pour les Aborigènes se trouve au centre de l'Australie ?", ["Uluru (Ayers Rock)", "Le mont Everest", "Ben Nevis", "Le mont Cook"], "Uluru (Ayers Rock)", "L'ascension est interdite depuis 2019."),
  Q("Comment s'appelle l'intérieur désertique de l'Australie ?", ["L'Outback", "Le Bush seulement", "Le Sahara", "La Prairie"], "L'Outback", "Il est très peu peuplé."),
  Q("Quel animal australien dort jusqu'à 20 heures par jour dans les eucalyptus ?", ["Le koala", "Le kangourou", "L'émeu", "Le wombat"], "Le koala", "Il se nourrit de feuilles d'eucalyptus."),
]),
notion('C6-3', 0, I, 'ang6i-royaume-uni-nations', [
  Q("Combien de nations composent le Royaume-Uni ?", ["Quatre", "Deux", "Trois", "Six"], "Quatre", "Angleterre, Écosse, pays de Galles et Irlande du Nord."),
  Q("Quelle est la capitale de l'Irlande du Nord ?", ["Belfast", "Dublin", "Cork", "Derry"], "Belfast", "Dublin est la capitale de la république d'Irlande."),
  Q("Quel est le plus haut sommet du Royaume-Uni, en Écosse ?", ["Ben Nevis", "Snowdon", "Scafell Pike", "Le mont Blanc"], "Ben Nevis", "Il culmine à 1 345 m."),
]),
notion('C6-3', 0, I, 'ang6i-comparatifs', [
  Q("Complétez : « London is ___ than Oxford. » (big)", ["bigger", "more big", "biggest", "more bigger"], "bigger", "Adjectif court : -er + than."),
  Q("Complétez : « The Nile is the ___ river in the world. » (long)", ["longest", "longer", "most long", "more longest"], "longest", "Superlatif d'un adjectif court : the + -est."),
  Q("Complétez : « This beach is ___ than that one. » (beautiful)", ["more beautiful", "beautifuller", "most beautiful", "beautifulest"], "more beautiful", "Adjectif long : more + adjectif + than."),
]),
notion('C6-3', 0, I, 'ang6i-climat-saisons', [
  Q("Comment dit-on « été » en anglais ?", ["Summer", "Spring", "Autumn", "Winter"], "Summer", "Spring = printemps, autumn (GB) / fall (US) = automne."),
  Q("Que signifie « fall » en anglais américain ?", ["L'automne", "La chute d'eau", "L'hiver", "Le printemps"], "L'automne", "Les Britanniques disent autumn."),
  Q("Pourquoi c'est l'été en Australie quand c'est l'hiver en Europe ?", ["L'Australie est dans l'hémisphère Sud", "L'Australie est plus proche du Soleil", "Il n'y a pas d'hiver en Europe", "À cause des océans"], "L'Australie est dans l'hémisphère Sud", "Noël s'y fête souvent à la plage."),
]),
notion('C6-3', 0, I, 'ang6i-animaux-afrique-inde', [
  Q("Quel animal national de l'Inde est un grand félin rayé ?", ["Le tigre du Bengale", "Le lion", "Le léopard", "Le guépard"], "Le tigre du Bengale", "L'Inde est un pays où l'anglais est langue officielle associée."),
  Q("Comment dit-on « éléphant » en anglais ?", ["Elephant", "Elefant", "Eliphant", "Elephan"], "Elephant", "Attention à l'orthographe : ph."),
  Q("Que sont les « Big Five » lors d'un safari en Afrique du Sud ?", ["Lion, léopard, éléphant, rhinocéros, buffle", "Cinq grandes villes", "Cinq montagnes", "Cinq fleuves"], "Lion, léopard, éléphant, rhinocéros, buffle", "Ce sont les animaux les plus recherchés."),
]),
notion('C6-3', 0, I, 'ang6i-there-is-are', [
  Q("Complétez : « There ___ a lot of mountains in Scotland. »", ["are", "is", "be", "have"], "are", "There are + pluriel ; there is + singulier."),
  Q("Que signifie « There is a castle on the hill » ?", ["Il y a un château sur la colline.", "Le château est là-bas.", "Il y avait un château.", "Le château est sur la mer."], "Il y a un château sur la colline.", "There is = il y a."),
  Q("Quelle est la forme négative de « There are some lakes » ?", ["There aren't any lakes.", "There isn't some lakes.", "There are no any lakes.", "There not are lakes."], "There aren't any lakes.", "Any dans les phrases négatives."),
]),
notion('C6-3', 0, I, 'ang6i-transports', [
  Q("Comment appelle-t-on le métro de Londres ?", ["The Tube (the Underground)", "The Subway", "The Metro", "The Train"], "The Tube (the Underground)", "À New York, c'est the subway."),
  Q("Quels taxis noirs sont typiques de Londres ?", ["Les black cabs", "Les yellow cabs", "Les tuk-tuks", "Les rickshaws"], "Les black cabs", "Les taxis jaunes sont typiques de New York."),
  Q("De quel côté de la route roule-t-on au Royaume-Uni ?", ["À gauche", "À droite", "Au milieu", "Indifféremment"], "À gauche", "Comme en Irlande, en Australie et en Inde."),
]),
notion('C6-3', 0, D, 'ang6d-geographie-usa', [
  Q("Combien d'États compte l'Australie ?", ["Six États et deux territoires", "Cinquante États", "Treize États", "Quatre États"], "Six États et deux territoires", "Comme la Nouvelle-Galles du Sud ou le Queensland."),
  Q("Quel État américain est un archipel du Pacifique ?", ["Hawaï", "L'Alaska", "La Floride", "La Californie"], "Hawaï", "Il devient le 50e État en 1959."),
  Q("Quel est le plus grand État des États-Unis par la superficie ?", ["L'Alaska", "Le Texas", "La Californie", "Le Montana"], "L'Alaska", "Il a été acheté à la Russie en 1867."),
]),
notion('C6-3', 0, D, 'ang6d-environnement', [
  Q("Quel immense récif corallien se trouve au large de l'Australie ?", ["La Grande Barrière de corail", "La barrière de Belize", "Le récif de Floride", "La mer de Corail seule"], "La Grande Barrière de corail", "Elle est menacée par le réchauffement."),
  Q("Que signifie « endangered species » ?", ["Des espèces menacées", "Des espèces dangereuses", "Des espèces disparues", "Des espèces protégées par la loi uniquement"], "Des espèces menacées", "Extinct = disparu."),
  Q("Que signifie « to recycle » ?", ["Recycler", "Faire du vélo", "Répéter", "Jeter"], "Recycler", "Reduce, reuse, recycle."),
]),
notion('C6-3', 0, D, 'ang6d-superlatifs-irreguliers', [
  Q("Quel est le comparatif de « good » ?", ["better", "gooder", "more good", "best"], "better", "Good, better, the best."),
  Q("Quel est le superlatif de « bad » ?", ["the worst", "the baddest", "the worse", "the most bad"], "the worst", "Bad, worse, the worst."),
  Q("Complétez : « Australia is ___ from France than Ireland. » (far)", ["farther (further)", "farer", "more far", "farest"], "farther (further)", "Far, farther / further, the farthest / furthest."),
]),
notion('C6-3', 0, D, 'ang6d-iles-britanniques', [
  Q("Quelle île au large de l'Écosse est célèbre pour ses poneys ?", ["Les Shetland", "Wight", "Man", "Jersey"], "Les Shetland", "Les poneys Shetland sont très petits."),
  Q("Quelles îles anglo-normandes sont proches des côtes françaises ?", ["Jersey et Guernesey", "Les Hébrides", "Les Orcades", "Les Scilly"], "Jersey et Guernesey", "Victor Hugo y a vécu en exil."),
  Q("Quel est le plus long fleuve du Royaume-Uni ?", ["La Severn", "La Tamise", "La Clyde", "La Mersey"], "La Severn", "La Tamise traverse Londres."),
]),
notion('C6-3', 0, D, 'ang6d-peuples-autochtones', [
  Q("Comment appelle-t-on les premiers habitants de l'Australie ?", ["Les Aborigènes", "Les Maoris", "Les Inuits", "Les Sioux"], "Les Aborigènes", "Ils y vivent depuis plus de 50 000 ans."),
  Q("Quel peuple autochtone vit dans le Grand Nord canadien ?", ["Les Inuits", "Les Maoris", "Les Aborigènes", "Les Zoulous"], "Les Inuits", "Le Nunavut est leur territoire."),
  Q("Quelle danse guerrière maorie est exécutée par les All Blacks avant leurs matchs ?", ["Le haka", "Le hula", "La gigue", "Le tango"], "Le haka", "Le hula est une danse hawaïenne."),
]),
notion('C6-3', 0, D, 'ang6d-villes-surnoms', [
  Q("Quelle ville américaine est surnommée « the Big Apple » ?", ["New York", "Chicago", "Boston", "San Francisco"], "New York", "Chicago est « the Windy City »."),
  Q("Quelle ville est surnommée « the Windy City » ?", ["Chicago", "Miami", "Seattle", "Denver"], "Chicago", "Elle est au bord du lac Michigan."),
  Q("Quel célèbre pont rouge traverse la baie de San Francisco ?", ["Le Golden Gate", "Le Brooklyn Bridge", "Le Tower Bridge", "Le Sydney Harbour Bridge"], "Le Golden Gate", "Il est inauguré en 1937."),
]),
notion('C6-3', 0, D, 'ang6d-meteo-gb', [
  Q("Que signifie l'expression « It's raining cats and dogs » ?", ["Il pleut des cordes.", "Il pleut des animaux.", "Il fait un temps de chien.", "Il neige beaucoup."], "Il pleut des cordes.", "C'est une expression idiomatique."),
  Q("Que signifie « foggy » ?", ["Brumeux", "Ensoleillé", "Orageux", "Glacial"], "Brumeux", "Le brouillard londonien (fog) est célèbre."),
  Q("Quelle échelle de température utilisent les Américains ?", ["Les degrés Fahrenheit", "Les degrés Celsius", "Les kelvins", "Les degrés Réaumur"], "Les degrés Fahrenheit", "32 °F = 0 °C."),
]),
notion('C6-3', 0, D, 'ang6d-unites-mesure', [
  Q("Quelle unité de distance utilise-t-on au Royaume-Uni sur les panneaux routiers ?", ["Le mile", "Le kilomètre", "Le mètre", "Le yard"], "Le mile", "1 mile ≈ 1,6 km."),
  Q("Combien de centimètres environ mesure un pied (foot) ?", ["Environ 30 cm", "Environ 3 cm", "Environ 100 cm", "Environ 12 cm"], "Environ 30 cm", "Un pied = 12 pouces (inches)."),
  Q("Que signifie « a pint » au Royaume-Uni ?", ["Une mesure de liquide d'environ un demi-litre", "Un pain", "Une pinte de sable", "Un poids d'un kilo"], "Une mesure de liquide d'environ un demi-litre", "Environ 0,57 litre."),
]),
notion('C6-3', 0, D, 'ang6d-routes-mythiques', [
  Q("Quelle route mythique traversait les États-Unis de Chicago à Los Angeles ?", ["La Route 66", "La Route 1", "L'Interstate 95", "La Pan-American Highway"], "La Route 66", "Elle est surnommée « Mother Road »."),
  Q("Quelle région du centre des États-Unis est couverte de grandes plaines agricoles ?", ["Les Grandes Plaines (Great Plains)", "Les Appalaches", "Les Rocheuses", "Le Bayou"], "Les Grandes Plaines (Great Plains)", "On y cultive blé et maïs."),
  Q("Quelle chaîne de montagnes traverse l'ouest des États-Unis et du Canada ?", ["Les Rocheuses (Rocky Mountains)", "Les Appalaches", "Les Highlands", "Les Pennines"], "Les Rocheuses (Rocky Mountains)", "Les Appalaches sont à l'est."),
]),
# ══ C6-4 · Imaginaire, contes et légendes ══
notion('C6-4', 0, F, 'ang6-contes-classiques', [
  Q("Comment s'appelle Cendrillon en anglais ?", ["Cinderella", "Snow White", "Sleeping Beauty", "Rapunzel"], "Cinderella", "Snow White = Blanche-Neige."),
  Q("Que signifie « Once upon a time » ?", ["Il était une fois", "Un jour peut-être", "Il y a longtemps, la fin", "Une fois par semaine"], "Il était une fois", "C'est le début des contes."),
  Q("Comment se termine souvent un conte en anglais ?", ["And they lived happily ever after.", "The end is near.", "Once upon a time.", "Goodbye forever."], "And they lived happily ever after.", "« Ils vécurent heureux pour toujours »."),
]),
notion('C6-4', 0, F, 'ang6-creatures', [
  Q("Que signifie « giant » ?", ["Un géant", "Un nain", "Un fantôme", "Un dragon"], "Un géant", "Dwarf = nain."),
  Q("Comment dit-on « fantôme » en anglais ?", ["Ghost", "Witch", "Elf", "Troll"], "Ghost", "Les maisons hantées sont haunted houses."),
  Q("Que signifie « fairy » ?", ["Une fée", "Une sorcière", "Une princesse", "Une reine"], "Une fée", "Fairy tale = conte de fées."),
]),
notion('C6-4', 0, F, 'ang6-boucle-or', [
  Q("Dans quel conte anglais une fillette entre-t-elle dans la maison de trois ours ?", ["Boucles d'or (Goldilocks)", "Le Petit Chaperon rouge", "Hansel et Gretel", "Peter Pan"], "Boucles d'or (Goldilocks)", "Elle goûte trois bols de porridge."),
  Q("Dans « Jack and the Beanstalk », que fait pousser Jack ?", ["Un haricot magique géant", "Un arbre d'or", "Une citrouille", "Une rose"], "Un haricot magique géant", "Il grimpe jusqu'au château d'un géant."),
  Q("Comment s'appelle le Petit Chaperon rouge en anglais ?", ["Little Red Riding Hood", "Little Red Hat", "Red Little Girl", "Small Red Cap"], "Little Red Riding Hood", "Hood = capuche."),
]),
notion('C6-4', 0, F, 'ang6-halloween-monstres', [
  Q("Quel légume creuse-t-on pour faire une lanterne à Halloween ?", ["La citrouille (pumpkin)", "La carotte", "Le chou", "La pomme de terre"], "La citrouille (pumpkin)", "On l'appelle jack-o'-lantern."),
  Q("Que signifie « scary » ?", ["Effrayant", "Drôle", "Triste", "Gentil"], "Effrayant", "To be scared = avoir peur."),
  Q("Comment dit-on « chauve-souris » en anglais ?", ["Bat", "Bird", "Owl", "Spider"], "Bat", "Owl = hibou, spider = araignée."),
]),
notion('C6-4', 0, F, 'ang6-disney', [
  Q("Quel film de Disney raconte l'histoire d'une sirène qui veut devenir humaine ?", ["La Petite Sirène (The Little Mermaid)", "Frozen", "Moana", "Cinderella"], "La Petite Sirène (The Little Mermaid)", "Il s'inspire d'un conte d'Andersen."),
  Q("Comment s'appelle La Reine des neiges en anglais ?", ["Frozen", "Snow Queen Movie", "Ice Princess", "Winter"], "Frozen", "Le film sort en 2013."),
  Q("Quel personnage de Disney est un pantin de bois dont le nez s'allonge quand il ment ?", ["Pinocchio", "Dumbo", "Bambi", "Aladdin"], "Pinocchio", "Le conte est italien."),
]),
notion('C6-4', 0, F, 'ang6-magie-vocabulaire', [
  Q("Que signifie « magic wand » ?", ["Une baguette magique", "Un chapeau magique", "Un balai", "Un chaudron"], "Une baguette magique", "Broom = balai."),
  Q("Comment dit-on « sort (formule magique) » en anglais ?", ["A spell", "A wand", "A potion", "A curse only"], "A spell", "To cast a spell = jeter un sort."),
  Q("Que signifie « castle » ?", ["Un château", "Une grotte", "Une forêt", "Un village"], "Un château", "Les contes se passent souvent dans des châteaux."),
]),
notion('C6-4', 0, F, 'ang6-harry-potter', [
  Q("Comment s'appelle l'école de sorcellerie de Harry Potter ?", ["Poudlard (Hogwarts)", "Narnia", "Neverland", "Wonderland"], "Poudlard (Hogwarts)", "Elle se trouve en Écosse dans les romans."),
  Q("Quel sport de sorciers se joue sur des balais ?", ["Le Quidditch", "Le cricket", "Le polo", "Le hockey"], "Le Quidditch", "Harry est attrapeur."),
  Q("Comment les sorciers appellent-ils les personnes sans pouvoirs magiques dans Harry Potter ?", ["Les Moldus (Muggles)", "Les Elfes", "Les Géants", "Les Gobelins"], "Les Moldus (Muggles)", "Muggle est entré dans le dictionnaire anglais."),
]),
notion('C6-4', 0, F, 'ang6-nursery-rhymes', [
  Q("Quel personnage d'une comptine anglaise est un œuf assis sur un mur ?", ["Humpty Dumpty", "Jack Sprat", "Old MacDonald", "Little Bo Peep"], "Humpty Dumpty", "Il tombe et personne ne peut le réparer."),
  Q("Comment commence la comptine « Twinkle, twinkle, little ___ » ?", ["star", "moon", "sun", "cat"], "star", "C'est l'air de « Ah ! vous dirai-je, maman »."),
  Q("Quelle comptine parle d'une ferme et de ses animaux ?", ["Old MacDonald Had a Farm", "London Bridge Is Falling Down", "Baa, Baa, Black Sheep seulement", "Hickory Dickory Dock"], "Old MacDonald Had a Farm", "« E-I-E-I-O ! »"),
]),
notion('C6-4', 0, I, 'ang6i-preterit-contes', [
  Q("Quel temps utilise-t-on pour raconter un conte ?", ["Le prétérit", "Le présent continu", "Le futur", "L'impératif"], "Le prétérit", "Once upon a time, there was a princess…"),
  Q("Quel est le prétérit de « go » ?", ["went", "goed", "gone", "goes"], "went", "Go, went, gone."),
  Q("Complétez : « The wolf ___ the door. » (knock, au passé)", ["knocked", "knock", "knocks", "was knock"], "knocked", "Verbe régulier : -ed."),
]),
notion('C6-4', 0, I, 'ang6i-alice', [
  Q("Quel animal pressé entraîne Alice au pays des merveilles ?", ["Un lapin blanc", "Un chat noir", "Une souris grise", "Un hibou"], "Un lapin blanc", "Il répète « I'm late! »."),
  Q("Quel chat qui sourit apparaît et disparaît dans Alice au pays des merveilles ?", ["Le chat du Cheshire", "Le chat botté", "Garfield", "Tom"], "Le chat du Cheshire", "Seul son sourire reste visible."),
  Q("Quelle reine crie « Off with their heads! » dans Alice ?", ["La Reine de cœur", "La Reine des neiges", "Élisabeth Ire", "La Reine Victoria"], "La Reine de cœur", "« Qu'on leur coupe la tête ! »"),
]),
notion('C6-4', 0, I, 'ang6i-narnia-tolkien', [
  Q("Par quel meuble les enfants entrent-ils dans le monde de Narnia ?", ["Une armoire", "Un tiroir", "Une cheminée", "Un miroir"], "Une armoire", "Le Lion, la Sorcière blanche et l'Armoire magique (1950), de C. S. Lewis."),
  Q("Quel auteur britannique a écrit Le Hobbit et Le Seigneur des anneaux ?", ["J. R. R. Tolkien", "C. S. Lewis", "Roald Dahl", "Lewis Carroll"], "J. R. R. Tolkien", "Il était professeur à Oxford."),
  Q("Quel lion est le roi de Narnia ?", ["Aslan", "Simba", "Mufasa", "Scar"], "Aslan", "Simba est dans Le Roi lion."),
]),
notion('C6-4', 0, I, 'ang6i-roald-dahl', [
  Q("Quel géant gentil attrape les rêves dans un roman de Roald Dahl ?", ["Le BGG (Bon Gros Géant)", "Hagrid", "Gulliver", "Le géant égoïste"], "Le BGG (Bon Gros Géant)", "The BFG, Big Friendly Giant (1982)."),
  Q("Quel garçon gagne un ticket d'or pour visiter la chocolaterie de Willy Wonka ?", ["Charlie Bucket", "Matilda", "James", "Danny"], "Charlie Bucket", "Charlie et la Chocolaterie (1964)."),
  Q("Dans « James et la Grosse Pêche », où James voyage-t-il ?", ["Dans une pêche géante", "Dans un ballon", "Dans un sous-marin", "Sur un dragon"], "Dans une pêche géante", "Il est accompagné d'insectes géants."),
]),
notion('C6-4', 0, I, 'ang6i-fantomes-gb', [
  Q("Quel pays est réputé pour ses châteaux hantés, comme celui d'Édimbourg ?", ["L'Écosse", "L'Australie", "Le Canada", "Les États-Unis"], "L'Écosse", "Les « ghost tours » y sont très populaires."),
  Q("Quel monstre du folklore écossais vivrait dans un lac des Highlands ?", ["Nessie, le monstre du loch Ness", "Bigfoot", "Le Yéti", "Le kraken"], "Nessie, le monstre du loch Ness", "Les photos célèbres étaient des canulars."),
  Q("Quelle créature poilue géante vivrait dans les forêts d'Amérique du Nord ?", ["Bigfoot (Sasquatch)", "Nessie", "Le leprechaun", "Le banshee"], "Bigfoot (Sasquatch)", "Aucune preuve scientifique de son existence."),
]),
notion('C6-4', 0, I, 'ang6i-connecteurs-recit', [
  Q("Que signifie « suddenly » dans un récit ?", ["Soudain", "Ensuite", "Finalement", "D'abord"], "Soudain", "Then = ensuite, finally = finalement, first = d'abord."),
  Q("Quel mot introduit la fin d'une histoire ?", ["In the end", "First", "Once upon a time", "Suddenly"], "In the end", "Ou finally."),
  Q("Que signifie « one day » ?", ["Un jour", "Une fois par jour", "Aujourd'hui", "Demain"], "Un jour", "Il fait avancer le récit."),
]),
notion('C6-4', 0, I, 'ang6i-peter-pan-neverland', [
  Q("Comment s'appelle la fée qui accompagne Peter Pan ?", ["La fée Clochette (Tinker Bell)", "La fée Morgane", "La fée bleue", "Maléfique"], "La fée Clochette (Tinker Bell)", "Elle est jalouse de Wendy."),
  Q("Quel pirate est l'ennemi de Peter Pan ?", ["Le capitaine Crochet (Captain Hook)", "Barbe-Noire", "Jack Sparrow", "Long John Silver"], "Le capitaine Crochet (Captain Hook)", "Un crocodile a mangé sa main."),
  Q("Comment s'appelle le pays imaginaire de Peter Pan en anglais ?", ["Neverland", "Wonderland", "Narnia", "Oz"], "Neverland", "Les enfants n'y grandissent jamais."),
]),
notion('C6-4', 0, I, 'ang6i-magicien-oz', [
  Q("Comment s'appelle la petite fille du Kansas emportée par une tornade au pays d'Oz ?", ["Dorothy", "Alice", "Wendy", "Matilda"], "Dorothy", "Le Magicien d'Oz (1900), de L. Frank Baum."),
  Q("Quelle route doit suivre Dorothy pour atteindre la Cité d'émeraude ?", ["La route de briques jaunes", "La route de la soie", "La voie lactée", "La route 66"], "La route de briques jaunes", "The Yellow Brick Road."),
  Q("Quel compagnon de Dorothy cherche un cerveau ?", ["L'épouvantail", "Le lion peureux", "L'homme de fer-blanc", "Le chien Toto"], "L'épouvantail", "L'homme de fer cherche un cœur, le lion du courage."),
]),
notion('C6-4', 0, D, 'ang6d-legendes-galloises', [
  Q("Quelle fée irlandaise pousse des cris annonçant une mort ?", ["La banshee", "La fée Clochette", "La sirène", "La Dame du Lac"], "La banshee", "Le mot vient du gaélique."),
  Q("Quelle dame mystérieuse remet l'épée Excalibur au roi Arthur ?", ["La Dame du Lac", "Morgane", "Guenièvre", "Viviane la sorcière noire"], "La Dame du Lac", "Elle la reprend à la mort d'Arthur."),
  Q("Dans quelle île légendaire Arthur blessé est-il emmené ?", ["Avalon", "Atlantis", "Neverland", "Utopia"], "Avalon", "On le dit endormi, prêt à revenir."),
]),
notion('C6-4', 0, D, 'ang6d-sleepy-hollow-poe', [
  Q("Quel cavalier sans tête hante la vallée de Sleepy Hollow ?", ["Le cavalier sans tête (Headless Horseman)", "Le chevalier noir", "Le fantôme de l'Opéra", "Dracula"], "Le cavalier sans tête (Headless Horseman)", "Légende écrite par Washington Irving (1820)."),
  Q("Quel auteur américain a écrit des récits d'horreur comme Le Chat noir ?", ["Edgar Allan Poe", "Stephen King", "Mark Twain", "Herman Melville"], "Edgar Allan Poe", "Il est aussi l'inventeur du récit policier."),
  Q("Quel auteur irlandais a créé Dracula en 1897 ?", ["Bram Stoker", "Mary Shelley", "Oscar Wilde", "Robert Louis Stevenson"], "Bram Stoker", "Mary Shelley a créé Frankenstein."),
]),
notion('C6-4', 0, D, 'ang6d-past-continuous-recit', [
  Q("Complétez : « The princess ___ when the dragon arrived. » (sleep)", ["was sleeping", "slept was", "is sleeping", "sleeps"], "was sleeping", "Le prétérit en be + ing décrit le décor d'un récit."),
  Q("Que décrit le prétérit en be + ing ?", ["Une action en cours dans le passé", "Une action future", "Une habitude présente", "Un ordre"], "Une action en cours dans le passé", "While she was walking, she saw a wolf."),
  Q("Complétez : « While Jack ___ up the beanstalk, the giant woke up. » (climb)", ["was climbing", "climbed was", "climbs", "is climbing"], "was climbing", "While + be + ing au passé."),
]),
notion('C6-4', 0, D, 'ang6d-frankenstein-jekyll', [
  Q("Quelle autrice britannique a écrit Frankenstein en 1818 ?", ["Mary Shelley", "Jane Austen", "Emily Brontë", "Virginia Woolf"], "Mary Shelley", "Elle avait 20 ans."),
  Q("Quel personnage de Stevenson se transforme en un double maléfique, Mr Hyde ?", ["Le docteur Jekyll", "Le docteur Frankenstein", "Sherlock Holmes", "Dorian Gray"], "Le docteur Jekyll", "L'Étrange Cas du docteur Jekyll et de M. Hyde (1886)."),
  Q("Quel roman d'aventures de Stevenson met en scène des pirates et une carte au trésor ?", ["L'Île au trésor", "Robinson Crusoé", "Moby Dick", "Peter Pan"], "L'Île au trésor", "Long John Silver en est le pirate célèbre."),
]),
notion('C6-4', 0, D, 'ang6d-mythes-grecs-anglais', [
  Q("Quelle série de romans de Rick Riordan mêle dieux grecs et adolescents américains ?", ["Percy Jackson", "Harry Potter", "Narnia", "Hunger Games"], "Percy Jackson", "Percy est le fils de Poséidon."),
  Q("Quelle série de C. S. Lewis compte sept romans ?", ["Le Monde de Narnia", "Harry Potter", "Le Seigneur des anneaux", "La Croisée des mondes"], "Le Monde de Narnia", "Harry Potter compte aussi sept tomes."),
  Q("Quel auteur britannique a écrit la trilogie À la croisée des mondes (His Dark Materials) ?", ["Philip Pullman", "Terry Pratchett", "Neil Gaiman", "J. R. R. Tolkien"], "Philip Pullman", "L'héroïne s'appelle Lyra."),
]),
notion('C6-4', 0, D, 'ang6d-genres-litteraires', [
  Q("Comment appelle-t-on un récit court avec une morale, souvent avec des animaux ?", ["Une fable", "Un roman", "Un poème épique", "Une biographie"], "Une fable", "Les fables d'Ésope sont connues en anglais."),
  Q("Que signifie « fantasy » comme genre littéraire ?", ["La fantasy : récits de mondes imaginaires et magiques", "Le roman policier", "La science-fiction uniquement", "Le roman historique"], "La fantasy : récits de mondes imaginaires et magiques", "Tolkien en est le maître."),
  Q("Qu'est-ce qu'un « cliffhanger » ?", ["Une fin de chapitre qui laisse en suspens", "Un alpiniste", "Une fin heureuse", "Un résumé"], "Une fin de chapitre qui laisse en suspens", "Il donne envie de lire la suite."),
]),
notion('C6-4', 0, D, 'ang6d-heros-folklore-us', [
  Q("Quel bûcheron géant du folklore américain est accompagné d'un bœuf bleu ?", ["Paul Bunyan", "Johnny Appleseed", "Davy Crockett", "Pecos Bill"], "Paul Bunyan", "Il aurait creusé le Grand Canyon."),
  Q("Quel personnage du folklore américain aurait planté des pommiers dans tout le pays ?", ["Johnny Appleseed", "Paul Bunyan", "Rip Van Winkle", "Tom Thumb"], "Johnny Appleseed", "Il a réellement existé : John Chapman."),
  Q("Quel personnage de Washington Irving s'endort vingt ans dans les montagnes ?", ["Rip Van Winkle", "Ichabod Crane", "Huckleberry Finn", "Paul Bunyan"], "Rip Van Winkle", "Il se réveille après la guerre d'Indépendance."),
]),
notion('C6-4', 0, D, 'ang6d-dickens-noel', [
  Q("Quel vieil avare reçoit la visite de trois fantômes la nuit de Noël ?", ["Ebenezer Scrooge", "Oliver Twist", "Fagin", "Mr Bean"], "Ebenezer Scrooge", "Un chant de Noël (A Christmas Carol), de Charles Dickens (1843)."),
  Q("Quelle expression Scrooge répète-t-il pour se moquer de Noël ?", ["« Bah! Humbug! »", "« Ho ho ho! »", "« Merry Christmas! »", "« Cheers! »"], "« Bah! Humbug! »", "Humbug = balivernes."),
  Q("Quel orphelin de Dickens demande « Please, sir, I want some more » ?", ["Oliver Twist", "David Copperfield", "Pip", "Scrooge"], "Oliver Twist", "Il réclame un peu plus de gruau."),
]),
# ══ C6-5 · Arts et expression des sentiments ══
notion('C6-5', 0, F, 'ang6-emotions', [
  Q("Que signifie « happy » ?", ["Heureux", "Triste", "En colère", "Fatigué"], "Heureux", "Sad = triste, angry = en colère."),
  Q("Comment dit-on « J'ai peur » ?", ["I'm scared (afraid).", "I have fear.", "I'm angry.", "I'm tired."], "I'm scared (afraid).", "On utilise be + adjectif."),
  Q("Que signifie « bored » ?", ["Qui s'ennuie", "Ennuyeux", "Fatigué", "Surpris"], "Qui s'ennuie", "Boring = ennuyeux (qui ennuie)."),
]),
notion('C6-5', 0, F, 'ang6-instruments', [
  Q("Comment dit-on « batterie » (instrument) en anglais ?", ["Drums", "Battery", "Bass", "Bells"], "Drums", "Battery = pile électrique."),
  Q("Que signifie « violin » ?", ["Violon", "Violoncelle", "Contrebasse", "Alto"], "Violon", "Cello = violoncelle."),
  Q("Complétez : « She plays ___ piano. »", ["the", "a", "—", "an"], "the", "Play the + instrument."),
]),
notion('C6-5', 0, F, 'ang6-groupes-musique', [
  Q("Quel groupe de Liverpool est le plus célèbre de l'histoire du rock ?", ["Les Beatles", "Les Rolling Stones", "Queen", "Oasis"], "Les Beatles", "John, Paul, George et Ringo."),
  Q("Quel chanteur américain est surnommé « le roi du rock'n'roll » ?", ["Elvis Presley", "Michael Jackson", "Bob Dylan", "Frank Sinatra"], "Elvis Presley", "Il vivait à Graceland, à Memphis."),
  Q("Quel chanteur américain est surnommé « le roi de la pop » ?", ["Michael Jackson", "Elvis Presley", "Prince", "Justin Bieber"], "Michael Jackson", "Thriller (1982) est l'album le plus vendu de l'histoire."),
]),
notion('C6-5', 0, F, 'ang6-couleurs-art', [
  Q("Que signifie « painting » ?", ["Un tableau (une peinture)", "Un dessin au crayon", "Une sculpture", "Une photo"], "Un tableau (une peinture)", "Drawing = dessin."),
  Q("Comment dit-on « pinceau » en anglais ?", ["Brush", "Pencil", "Pen", "Rubber"], "Brush", "Pencil = crayon."),
  Q("Quelle couleur obtient-on en mélangeant blue et yellow ?", ["Green", "Purple", "Orange", "Brown"], "Green", "Red + yellow = orange."),
]),
notion('C6-5', 0, F, 'ang6-gouts-sentiments', [
  Q("Que signifie « I love it! » ?", ["J'adore !", "Je déteste !", "C'est moyen.", "Je ne sais pas."], "J'adore !", "I hate it! = je déteste !"),
  Q("Comment dit-on « C'est magnifique ! » ?", ["It's beautiful!", "It's ugly!", "It's boring!", "It's funny!"], "It's beautiful!", "Ugly = laid."),
  Q("Que signifie « I don't mind » ?", ["Ça m'est égal.", "Je ne pense pas.", "Je n'aime pas.", "Je ne sais pas."], "Ça m'est égal.", "Do you mind…? = Cela vous dérange-t-il… ?"),
]),
notion('C6-5', 0, F, 'ang6-danse-theatre', [
  Q("Que signifie « to dance » ?", ["Danser", "Chanter", "Jouer la comédie", "Dessiner"], "Danser", "To sing = chanter."),
  Q("Comment dit-on « une pièce de théâtre » ?", ["A play", "A game", "A film", "A show-off"], "A play", "Play est à la fois un verbe et un nom."),
  Q("Quel théâtre londonien en bois a été reconstruit à l'identique de celui de Shakespeare ?", ["Le Globe", "Le Royal Albert Hall", "Covent Garden", "Le Palladium"], "Le Globe", "Il a rouvert en 1997."),
]),
notion('C6-5', 0, F, 'ang6-chansons-enfants', [
  Q("Quelle chanson chante-t-on pour un anniversaire en anglais ?", ["Happy Birthday to You", "Jingle Bells", "Twinkle, Twinkle", "Auld Lang Syne"], "Happy Birthday to You", "Elle est connue dans le monde entier."),
  Q("Quelle chanson de Noël parle de grelots ?", ["Jingle Bells", "Silent Night", "White Christmas", "Let It Snow"], "Jingle Bells", "Jingle = tinter."),
  Q("Quelle chanson écossaise est chantée au Nouvel An en se tenant les mains ?", ["Auld Lang Syne", "Amazing Grace", "Yesterday", "God Save the King"], "Auld Lang Syne", "Les paroles sont du poète Robert Burns."),
]),
notion('C6-5', 0, I, 'ang6i-emotions-avancees', [
  Q("Que signifie « jealous » ?", ["Jaloux", "Joyeux", "Gêné", "Fier"], "Jaloux", "Proud = fier, embarrassed = gêné."),
  Q("Quelle est la différence entre « excited » et « exciting » ?", ["Excited = enthousiaste ; exciting = passionnant", "Ils sont identiques", "Excited = ennuyeux", "Exciting = fatigué"], "Excited = enthousiaste ; exciting = passionnant", "-ed : ce que l'on ressent ; -ing : ce qui provoque."),
  Q("Que signifie « I'm worried about the test » ?", ["Je suis inquiet pour le contrôle.", "Je suis content du contrôle.", "J'ai raté le contrôle.", "J'ai fini le contrôle."], "Je suis inquiet pour le contrôle.", "Worried about = inquiet à propos de."),
]),
notion('C6-5', 0, I, 'ang6i-peintres', [
  Q("Quel peintre britannique est célèbre pour ses paysages de lumière et de brume, comme Pluie, vapeur et vitesse ?", ["William Turner", "David Hockney", "Banksy", "Thomas Gainsborough"], "William Turner", "Il annonce l'impressionnisme."),
  Q("Quel artiste américain du pop art a peint des boîtes de soupe Campbell ?", ["Andy Warhol", "Jackson Pollock", "Edward Hopper", "Roy Lichtenstein"], "Andy Warhol", "Il a aussi réalisé des portraits de Marilyn Monroe."),
  Q("Quel artiste de rue britannique anonyme est célèbre pour ses pochoirs, comme La Petite Fille au ballon ?", ["Banksy", "Keith Haring", "Basquiat", "Hockney"], "Banksy", "Son identité reste officiellement secrète."),
]),
notion('C6-5', 0, I, 'ang6i-musees', [
  Q("Quel musée de Londres abrite des momies égyptiennes et la pierre de Rosette ?", ["Le British Museum", "La Tate Modern", "La National Gallery", "Le Victoria and Albert Museum"], "Le British Museum", "L'entrée y est gratuite."),
  Q("Quel musée d'art moderne londonien est installé dans une ancienne centrale électrique ?", ["La Tate Modern", "Le British Museum", "Le Louvre", "Le MoMA"], "La Tate Modern", "Elle ouvre en 2000 au bord de la Tamise."),
  Q("Quel grand musée d'art de New York est surnommé « the Met » ?", ["Le Metropolitan Museum of Art", "Le MoMA", "Le Guggenheim", "Le Smithsonian"], "Le Metropolitan Museum of Art", "Il se trouve au bord de Central Park."),
]),
notion('C6-5', 0, I, 'ang6i-comedies-musicales', [
  Q("Quel quartier de New York est célèbre pour ses comédies musicales ?", ["Broadway", "Wall Street", "Harlem", "Brooklyn"], "Broadway", "À Londres, c'est le West End."),
  Q("Quelle comédie musicale raconte l'histoire du Roi lion ?", ["The Lion King", "Cats", "Les Misérables", "Mamma Mia!"], "The Lion King", "Elle est jouée depuis 1997."),
  Q("Quel compositeur britannique a créé Cats et Le Fantôme de l'Opéra ?", ["Andrew Lloyd Webber", "Elton John", "Paul McCartney", "Benjamin Britten"], "Andrew Lloyd Webber", "Ce sont deux immenses succès."),
]),
notion('C6-5', 0, I, 'ang6i-express-opinion', [
  Q("Comment donne-t-on son avis en anglais ?", ["In my opinion, …", "In my head of, …", "For me opinion, …", "As my thinking, …"], "In my opinion, …", "On peut aussi dire I think that…"),
  Q("Que signifie « I agree with you » ?", ["Je suis d'accord avec toi.", "Je ne suis pas d'accord.", "Je suis en retard.", "Je t'entends."], "Je suis d'accord avec toi.", "I disagree = je ne suis pas d'accord."),
  Q("Complétez : « What do you think ___ this song? »", ["of", "to", "at", "on"], "of", "What do you think of / about… ?"),
]),
notion('C6-5', 0, I, 'ang6i-cinema-animation', [
  Q("Quel studio américain a réalisé Toy Story, premier long métrage entièrement en images de synthèse ?", ["Pixar", "DreamWorks", "Warner Bros.", "Aardman"], "Pixar", "Le film sort en 1995."),
  Q("Quel studio britannique a créé Wallace et Gromit en pâte à modeler ?", ["Aardman", "Pixar", "Disney", "Ghibli"], "Aardman", "Il est basé à Bristol."),
  Q("Comment s'appelle le cow-boy de Toy Story ?", ["Woody", "Buzz", "Rex", "Andy"], "Woody", "Buzz l'Éclair est le ranger de l'espace."),
]),
notion('C6-5', 0, I, 'ang6i-poesie-enfants', [
  Q("Qu'est-ce qu'un limerick ?", ["Un petit poème humoristique de cinq vers", "Une chanson de Noël", "Un conte de fées", "Une pièce de théâtre"], "Un petit poème humoristique de cinq vers", "Edward Lear l'a rendu populaire."),
  Q("Que signifie « rhyme » ?", ["La rime", "Le rythme", "Le refrain", "Le titre"], "La rime", "Cat / hat riment."),
  Q("Quel mot rime avec « moon » ?", ["Spoon", "Man", "Mine", "Mean"], "Spoon", "« Hey Diddle Diddle… the cow jumped over the moon »."),
]),
notion('C6-5', 0, I, 'ang6i-musique-genres', [
  Q("Quel genre musical est né à La Nouvelle-Orléans au début du XXe siècle ?", ["Le jazz", "Le rap", "La country", "Le punk"], "Le jazz", "Louis Armstrong en est une grande figure."),
  Q("Quel genre musical est né dans le Bronx, à New York, dans les années 1970 ?", ["Le hip-hop (rap)", "Le jazz", "Le blues", "Le rock"], "Le hip-hop (rap)", "Il réunit rap, DJing, breakdance et graffiti."),
  Q("Quel genre musical, né en Jamaïque, est associé à Bob Marley ?", ["Le reggae", "La salsa", "Le blues", "La soul"], "Le reggae", "La Jamaïque est un pays anglophone."),
]),
notion('C6-5', 0, D, 'ang6d-sentiments-adjectifs-ed-ing', [
  Q("Complétez : « The film was really ___. » (ennuyeux)", ["boring", "bored", "bore", "boredom"], "boring", "Boring décrit ce qui provoque l'ennui."),
  Q("Complétez : « I was ___ by the ending. » (surpris)", ["surprised", "surprising", "surprise", "surprisingly"], "surprised", "-ed : ce que l'on ressent."),
  Q("Que signifie « a frightening story » ?", ["Une histoire effrayante", "Une histoire où l'on a peur", "Une histoire courte", "Une histoire drôle"], "Une histoire effrayante", "Frightened = effrayé."),
]),
notion('C6-5', 0, D, 'ang6d-shakespeare', [
  Q("Dans quelle ville est né William Shakespeare ?", ["Stratford-upon-Avon", "Londres", "Oxford", "Cambridge"], "Stratford-upon-Avon", "Il y est né en 1564."),
  Q("Quelle célèbre réplique prononce Hamlet ?", ["« To be or not to be, that is the question »", "« Romeo, Romeo, wherefore art thou Romeo? »", "« All the world's a stage »", "« Is this a dagger? »"], "« To be or not to be, that is the question »", "« Être ou ne pas être, telle est la question »."),
  Q("Quelle pièce de Shakespeare met en scène deux jeunes amants de Vérone ?", ["Roméo et Juliette", "Macbeth", "Othello", "La Tempête"], "Roméo et Juliette", "Leurs familles, les Montaigu et les Capulet, se haïssent."),
]),
notion('C6-5', 0, D, 'ang6d-hockney-hopper', [
  Q("Quel peintre britannique est célèbre pour ses piscines californiennes, comme A Bigger Splash ?", ["David Hockney", "Francis Bacon", "Lucian Freud", "Turner"], "David Hockney", "Il est né en 1937 à Bradford."),
  Q("Quel peintre américain a représenté la solitude urbaine dans Nighthawks (1942) ?", ["Edward Hopper", "Norman Rockwell", "Andy Warhol", "Grant Wood"], "Edward Hopper", "On y voit un café la nuit."),
  Q("Quel tableau de Grant Wood montre un fermier et sa fille tenant une fourche ?", ["American Gothic", "Nighthawks", "Campbell's Soup Cans", "The Scream"], "American Gothic", "Il est peint en 1930."),
]),
notion('C6-5', 0, D, 'ang6d-musique-gb-moderne', [
  Q("Quel groupe britannique de Freddie Mercury a chanté Bohemian Rhapsody ?", ["Queen", "The Beatles", "Coldplay", "Oasis"], "Queen", "La chanson date de 1975."),
  Q("Quelle chanteuse britannique a sorti l'album 21 avec Rolling in the Deep ?", ["Adele", "Amy Winehouse", "Dua Lipa", "Lily Allen"], "Adele", "Elle vient de Londres."),
  Q("Quel chanteur britannique a écrit Shape of You ?", ["Ed Sheeran", "Harry Styles", "Sam Smith", "Elton John"], "Ed Sheeran", "La chanson sort en 2017."),
]),
notion('C6-5', 0, D, 'ang6d-exclamations', [
  Q("Complétez : « ___ a beautiful painting! »", ["What", "How", "So", "Such"], "What", "What + a + adjectif + nom !"),
  Q("Complétez : « ___ beautiful it is! »", ["How", "What", "Such", "Which"], "How", "How + adjectif !"),
  Q("Que signifie « What a pity! » ?", ["Quel dommage !", "Quelle pitié de toi !", "Quelle peur !", "Quelle chance !"], "Quel dommage !", "What luck! = quelle chance !"),
]),
notion('C6-5', 0, D, 'ang6d-art-vocabulaire', [
  Q("Que signifie « portrait » en anglais ?", ["Un portrait", "Un paysage", "Une nature morte", "Un autoportrait uniquement"], "Un portrait", "Landscape = paysage, still life = nature morte."),
  Q("Comment dit-on « nature morte » en anglais ?", ["A still life", "A dead nature", "A landscape", "A sketch"], "A still life", "Sketch = esquisse."),
  Q("Que signifie « in the foreground » dans la description d'un tableau ?", ["Au premier plan", "À l'arrière-plan", "Au centre", "En haut à droite"], "Au premier plan", "In the background = à l'arrière-plan."),
]),
notion('C6-5', 0, D, 'ang6d-musiciens-classiques', [
  Q("Quel compositeur allemand installé à Londres a écrit le Messie et Water Music ?", ["Haendel (Handel)", "Bach", "Mozart", "Beethoven"], "Haendel (Handel)", "Il a obtenu la nationalité britannique."),
  Q("Quel compositeur britannique a écrit Les Planètes (The Planets) ?", ["Gustav Holst", "Edward Elgar", "Benjamin Britten", "Henry Purcell"], "Gustav Holst", "Chaque mouvement représente une planète."),
  Q("Quel compositeur anglais a écrit Pomp and Circumstance, joué lors des remises de diplômes américaines ?", ["Edward Elgar", "Gustav Holst", "Haendel", "John Williams"], "Edward Elgar", "La marche n° 1 est célèbre."),
]),
notion('C6-5', 0, D, 'ang6d-poetes-celebres', [
  Q("Quel poète écossais a écrit Auld Lang Syne et est fêté chaque 25 janvier ?", ["Robert Burns", "William Wordsworth", "Lord Byron", "Walter Scott"], "Robert Burns", "C'est la Burns Night, avec du haggis."),
  Q("Quel poète anglais romantique a écrit un célèbre poème sur des jonquilles (Daffodils) ?", ["William Wordsworth", "John Keats", "Shakespeare", "T. S. Eliot"], "William Wordsworth", "« I wandered lonely as a cloud… »"),
  Q("Quel recueil de poèmes de T. S. Eliot a inspiré la comédie musicale Cats ?", ["Old Possum's Book of Practical Cats", "The Waste Land", "Four Quartets", "Leaves of Grass"], "Old Possum's Book of Practical Cats", "Il paraît en 1939."),
]),
notion('C6-5', 0, D, 'ang6d-musique-films', [
  Q("Quel compositeur américain a écrit les musiques de Star Wars, Harry Potter et Jurassic Park ?", ["John Williams", "Hans Zimmer", "Ennio Morricone", "Danny Elfman"], "John Williams", "Il a reçu plusieurs Oscars."),
  Q("Quel compositeur a écrit la musique du Roi lion et d'Inception ?", ["Hans Zimmer", "John Williams", "Alan Menken", "Howard Shore"], "Hans Zimmer", "Il est d'origine allemande et travaille à Hollywood."),
  Q("Quelle chanson de Frozen est devenue un succès mondial ?", ["Let It Go", "Hakuna Matata", "Under the Sea", "A Whole New World"], "Let It Go", "Elle est interprétée par Idina Menzel."),
]),
]
