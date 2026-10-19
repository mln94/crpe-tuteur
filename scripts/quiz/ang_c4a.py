# Anglais · Repères culturels, 4e : Sport et société ; Voyages et explorations ; Villes, villages, quartiers (25 questions par niveau)
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ C4-1 · Sport et société ══
notion('C4-1', 0, F, 'ang4-vocabulaire-sport', [
  Q("Que signifie « referee » ?", ["L'arbitre", "Le joueur", "L'entraîneur", "Le supporter"], "L'arbitre", "Coach = entraîneur."),
  Q("Comment dit-on « une équipe » ?", ["A team", "A group only", "A crew", "A club"], "A team", "Teammate = coéquipier."),
  Q("Que signifie « to score a goal » ?", ["Marquer un but", "Rater un but", "Garder le but", "Siffler"], "Marquer un but", "Goalkeeper = gardien de but."),
]),
notion('C4-1', 0, F, 'ang4-basket-baseball', [
  Q("Quel sport a été inventé en 1891 par un professeur canadien aux États-Unis ?", ["Le basket-ball", "Le baseball", "Le hockey", "Le golf"], "Le basket-ball", "James Naismith utilisait des paniers à pêches."),
  Q("Comment s'appelle le championnat professionnel de basket américain ?", ["La NBA", "La NFL", "La MLB", "La NHL"], "La NBA", "National Basketball Association."),
  Q("Quel sport américain se joue avec une batte et un gant, sur un terrain en losange ?", ["Le baseball", "Le cricket", "Le softball uniquement", "Le hockey"], "Le baseball", "On l'appelle « America's pastime »."),
]),
notion('C4-1', 0, F, 'ang4-jeux-olympiques', [
  Q("Quelle ville anglophone a accueilli les Jeux olympiques d'été en 2012 ?", ["Londres", "Sydney", "Atlanta", "Los Angeles"], "Londres", "C'était la troisième fois."),
  Q("Quelle ville américaine accueillera les Jeux olympiques d'été en 2028 ?", ["Los Angeles", "New York", "Chicago", "Miami"], "Los Angeles", "Après Paris 2024 et avant Brisbane 2032."),
  Q("Quelle ville australienne accueillera les Jeux olympiques en 2032 ?", ["Brisbane", "Sydney", "Melbourne", "Perth"], "Brisbane", "Sydney les a accueillis en 2000."),
]),
notion('C4-1', 0, F, 'ang4-sports-us-ligues', [
  Q("Comment s'appelle le championnat professionnel de football américain ?", ["La NFL", "La NBA", "La MLS", "La NHL"], "La NFL", "National Football League."),
  Q("Quel sport se joue dans la NHL ?", ["Le hockey sur glace", "Le baseball", "Le basket-ball", "Le soccer"], "Le hockey sur glace", "Des équipes canadiennes y participent."),
  Q("Comment s'appelle la finale du championnat de baseball américain ?", ["La World Series", "Le Super Bowl", "La Stanley Cup", "Les NBA Finals"], "La World Series", "Malgré son nom, elle n'oppose que des équipes nord-américaines."),
]),
notion('C4-1', 0, F, 'ang4-golf-ecosse', [
  Q("Dans quel pays le golf est-il né ?", ["L'Écosse", "Les États-Unis", "Le Japon", "L'Australie"], "L'Écosse", "Le parcours de St Andrews est le plus ancien."),
  Q("Comment appelle-t-on le terrain de golf en anglais ?", ["A golf course", "A golf field", "A golf pitch", "A golf court"], "A golf course", "Pitch = terrain de foot, court = court de tennis."),
  Q("Que signifie « hole in one » au golf ?", ["Un trou en un coup", "Un trou dans le gazon", "Un coup raté", "Un bunker"], "Un trou en un coup", "C'est un exploit rare."),
]),
notion('C4-1', 0, F, 'ang4-supporters', [
  Q("Que signifie « fan » ?", ["Un supporter, un admirateur", "Un ventilateur uniquement", "Un joueur", "Un entraîneur"], "Un supporter, un admirateur", "Fan vient de « fanatic »."),
  Q("Que signifie « stadium » ?", ["Un stade", "Un studio", "Une étape", "Un gymnase"], "Un stade", "Wembley est le plus célèbre d'Angleterre."),
  Q("Quel stade londonien accueille les finales de football anglais ?", ["Wembley", "Old Trafford", "Anfield", "Twickenham"], "Wembley", "Twickenham est le temple du rugby."),
]),
notion('C4-1', 0, F, 'ang4-sports-hiver', [
  Q("Comment dit-on « patiner » en anglais ?", ["To skate", "To ski", "To slide", "To skip"], "To skate", "Ice skating = patinage."),
  Q("Quel sport de glace, populaire en Écosse, consiste à faire glisser des pierres ?", ["Le curling", "Le hockey", "Le bobsleigh", "Le patinage"], "Le curling", "Il est né en Écosse au XVIe siècle."),
  Q("Quelle ville canadienne a accueilli les Jeux olympiques d'hiver en 2010 ?", ["Vancouver", "Toronto", "Ottawa", "Montréal"], "Vancouver", "Calgary les avait accueillis en 1988."),
]),
notion('C4-1', 0, F, 'ang4-sport-sante', [
  Q("Que signifie « to keep fit » ?", ["Rester en forme", "Garder un objet", "Faire un régime", "S'asseoir"], "Rester en forme", "Fitness = forme physique."),
  Q("Que signifie « healthy » ?", ["En bonne santé, sain", "Malade", "Fatigué", "Lourd"], "En bonne santé, sain", "Unhealthy = mauvais pour la santé."),
  Q("Que signifie « to train » pour un sportif ?", ["S'entraîner", "Prendre le train", "Arbitrer", "Perdre"], "S'entraîner", "Training = entraînement."),
]),
notion('C4-1', 0, I, 'ang4i-jesse-owens-racisme', [
  Q("Quelle joueuse de tennis afro-américaine a été la première à gagner Wimbledon, en 1957 ?", ["Althea Gibson", "Serena Williams", "Venus Williams", "Billie Jean King"], "Althea Gibson", "Elle a ouvert la voie à de nombreuses joueuses."),
  Q("Quel joueur de baseball afro-américain a brisé la ségrégation dans la ligue majeure en 1947 ?", ["Jackie Robinson", "Babe Ruth", "Michael Jordan", "Kobe Bryant"], "Jackie Robinson", "Son numéro 42 est retiré dans toutes les équipes."),
  Q("Quel geste ont fait deux athlètes américains sur le podium des JO de Mexico en 1968 ?", ["Ils ont levé un poing ganté de noir", "Ils ont refusé leur médaille", "Ils ont chanté l'hymne", "Ils ont salué la reine"], "Ils ont levé un poing ganté de noir", "Tommie Smith et John Carlos protestaient contre le racisme."),
]),
notion('C4-1', 0, I, 'ang4i-six-nations', [
  Q("Quel tournoi de rugby réunit l'Angleterre, l'Écosse, le pays de Galles, l'Irlande, la France et l'Italie ?", ["Le Tournoi des Six Nations", "La Coupe du monde", "Le Rugby Championship", "Les Jeux du Commonwealth"], "Le Tournoi des Six Nations", "Il se joue chaque année de février à mars."),
  Q("Comment s'appelle l'équipe de rugby de Nouvelle-Zélande ?", ["Les All Blacks", "Les Wallabies", "Les Springboks", "Les Lions"], "Les All Blacks", "Les Wallabies sont australiens, les Springboks sud-africains."),
  Q("Pourquoi l'Irlande joue-t-elle au rugby avec une seule équipe pour toute l'île ?", ["L'équipe réunit l'Irlande et l'Irlande du Nord", "Par erreur", "Parce que l'Irlande du Nord n'a pas de rugby", "Parce que c'est obligatoire"], "L'équipe réunit l'Irlande et l'Irlande du Nord", "Le sport dépasse ici la frontière politique."),
]),
notion('C4-1', 0, I, 'ang4i-commonwealth-games', [
  Q("Quelle compétition multisport réunit tous les quatre ans les pays du Commonwealth ?", ["Les Jeux du Commonwealth", "Les Jeux olympiques", "Les Jeux panaméricains", "Les X Games"], "Les Jeux du Commonwealth", "Ils existent depuis 1930."),
  Q("Quelle ville écossaise a accueilli les Jeux du Commonwealth en 2026 ?", ["Glasgow", "Édimbourg", "Aberdeen", "Dundee"], "Glasgow", "Elle les avait déjà accueillis en 2014."),
  Q("Quelle course de chevaux célèbre se déroule à Epsom, en Angleterre ?", ["Le Derby", "Le Grand National", "Le Kentucky Derby", "La Melbourne Cup"], "Le Derby", "Le Grand National se court à Liverpool."),
]),
notion('C4-1', 0, I, 'ang4i-sport-argent', [
  Q("Que signifie « sponsor » ?", ["Une entreprise qui finance un sportif ou une équipe", "Un supporter", "Un arbitre", "Un médecin"], "Une entreprise qui finance un sportif ou une équipe", "Les sponsors affichent leur logo sur les maillots."),
  Q("Pourquoi les spots publicitaires du Super Bowl coûtent-ils des millions de dollars ?", ["Plus de 100 millions de téléspectateurs le regardent", "Ils sont très longs", "Ils sont tournés au stade", "Ils sont obligatoires"], "Plus de 100 millions de téléspectateurs le regardent", "C'est l'événement le plus regardé des États-Unis."),
  Q("Que signifie « transfer fee » dans le football ?", ["Le prix de transfert d'un joueur", "Le prix d'un billet", "Le salaire de l'arbitre", "Un ticket de bus"], "Le prix de transfert d'un joueur", "Il peut atteindre des centaines de millions d'euros."),
]),
notion('C4-1', 0, I, 'ang4i-paralympiques', [
  Q("Dans quel hôpital anglais sont nés les Jeux paralympiques ?", ["L'hôpital de Stoke Mandeville", "L'hôpital Saint-Thomas", "Le Royal London Hospital", "L'hôpital de Glasgow"], "L'hôpital de Stoke Mandeville", "Le docteur Ludwig Guttmann y organise des jeux en 1948."),
  Q("Que signifie « wheelchair » ?", ["Un fauteuil roulant", "Une roue de vélo", "Une chaise longue", "Un brancard"], "Un fauteuil roulant", "Le basket fauteuil est un sport paralympique."),
  Q("Quels jeux internationaux, créés par le prince Harry, réunissent des militaires blessés ?", ["Les Invictus Games", "Les Jeux du Commonwealth", "Les X Games", "Les Jeux mondiaux"], "Les Invictus Games", "Ils sont créés en 2014."),
]),
notion('C4-1', 0, I, 'ang4i-comparatifs-sport', [
  Q("Complétez : « He runs ___ than his brother. » (fast)", ["faster", "more fast", "fastest", "more faster"], "faster", "Fast, faster, the fastest."),
  Q("Complétez : « This is the ___ match of the season! » (exciting)", ["most exciting", "excitingest", "more exciting", "excitinger"], "most exciting", "Adjectif long : the most."),
  Q("Complétez : « She is as strong ___ her sister. »", ["as", "than", "that", "like"], "as", "As… as = aussi… que."),
]),
notion('C4-1', 0, I, 'ang4i-sportives-pionnieres', [
  Q("Quelle joueuse de tennis américaine a battu un homme dans « la bataille des sexes » en 1973 ?", ["Billie Jean King", "Serena Williams", "Martina Navratilova", "Chris Evert"], "Billie Jean King", "Elle a lutté pour l'égalité des primes."),
  Q("Quelle équipe de football féminine a remporté quatre Coupes du monde ?", ["Les États-Unis", "L'Angleterre", "Le Brésil", "Le Japon"], "Les États-Unis", "Le football féminin y est très populaire."),
  Q("Quelle équipe a remporté l'Euro féminin de football en 2022 et 2025 ?", ["L'Angleterre (les Lionesses)", "L'Allemagne", "L'Espagne", "La France"], "L'Angleterre (les Lionesses)", "Elle a battu l'Espagne en finale en 2025."),
]),
notion('C4-1', 0, I, 'ang4i-marathons', [
  Q("Quel est le plus ancien marathon annuel du monde, couru depuis 1897 ?", ["Le marathon de Boston", "Le marathon de Londres", "Le marathon de New York", "Le marathon de Berlin"], "Le marathon de Boston", "Il se court le jour des Patriotes, en avril."),
  Q("Quelle distance mesure un marathon ?", ["42,195 km", "10 km", "21 km", "100 km"], "42,195 km", "Un semi-marathon fait 21,1 km."),
  Q("Pourquoi beaucoup de coureurs du marathon de Londres sont-ils déguisés ?", ["Ils collectent des fonds pour des associations caritatives", "C'est obligatoire", "Pour gagner plus vite", "Par tradition militaire"], "Ils collectent des fonds pour des associations caritatives", "C'est la plus grande course caritative du monde."),
]),
notion('C4-1', 0, D, 'ang4d-michael-jordan-lebron', [
  Q("Quel joueur de basket des Chicago Bulls est souvent considéré comme le plus grand de l'histoire ?", ["Michael Jordan", "LeBron James", "Kobe Bryant", "Magic Johnson"], "Michael Jordan", "Il a remporté six titres NBA."),
  Q("Quel joueur français a été élu meilleur débutant de la NBA en 2024 ?", ["Victor Wembanyama", "Tony Parker", "Rudy Gobert", "Evan Fournier"], "Victor Wembanyama", "Il joue aux San Antonio Spurs."),
  Q("Quel joueur de la NBA a dépassé en 2023 le record de points de Kareem Abdul-Jabbar ?", ["LeBron James", "Stephen Curry", "Kevin Durant", "Michael Jordan"], "LeBron James", "Il est devenu le meilleur marqueur de l'histoire."),
]),
notion('C4-1', 0, D, 'ang4d-title-ix', [
  Q("Quelle loi américaine de 1972 interdit les discriminations sexuelles dans les écoles, y compris dans le sport ?", ["Le Title IX", "Le Civil Rights Act", "Le Bill of Rights", "Le New Deal"], "Le Title IX", "Elle a fait exploser la pratique sportive féminine."),
  Q("Quelle footballeuse américaine engagée a mené le combat pour l'égalité salariale avec les hommes ?", ["Megan Rapinoe", "Mia Hamm", "Alex Morgan", "Simone Biles"], "Megan Rapinoe", "Un accord d'égalité salariale est signé en 2022."),
  Q("Quelle gymnaste américaine a parlé publiquement de santé mentale lors des JO de Tokyo ?", ["Simone Biles", "Gabby Douglas", "Nadia Comăneci", "Mary Lou Retton"], "Simone Biles", "Elle est revenue triomphante à Paris 2024."),
]),
notion('C4-1', 0, D, 'ang4d-football-histoire', [
  Q("En quelle année la Football Association anglaise a-t-elle fixé les premières règles du football ?", ["1863", "1900", "1930", "1789"], "1863", "Elle est la plus ancienne fédération du monde."),
  Q("Quelle Coupe du monde l'Angleterre a-t-elle remportée ?", ["Celle de 1966, à domicile", "Celle de 1998", "Celle de 2018", "Aucune"], "Celle de 1966, à domicile", "C'est son seul titre mondial masculin."),
  Q("Quel drame de 1989 dans un stade de Sheffield a transformé la sécurité des stades anglais ?", ["La catastrophe de Hillsborough", "Le Heysel", "Le Blitz", "Le Grand Incendie"], "La catastrophe de Hillsborough", "97 supporters de Liverpool y sont morts."),
]),
notion('C4-1', 0, D, 'ang4d-kaepernick', [
  Q("Quel joueur de football américain s'est agenouillé pendant l'hymne en 2016 pour dénoncer les violences policières ?", ["Colin Kaepernick", "Tom Brady", "Patrick Mahomes", "Peyton Manning"], "Colin Kaepernick", "Le geste « take a knee » s'est répandu."),
  Q("Quel mouvement de 2013 dénonce les violences contre les Afro-Américains ?", ["Black Lives Matter", "#MeToo", "Occupy Wall Street", "Fridays for Future"], "Black Lives Matter", "Il prend de l'ampleur en 2020."),
  Q("Pourquoi le sport est-il une tribune politique aux États-Unis ?", ["Les athlètes célèbres ont une forte audience médiatique", "Le sport est interdit", "Les athlètes sont élus", "La loi l'impose"], "Les athlètes célèbres ont une forte audience médiatique", "Leurs prises de position font débat."),
]),
notion('C4-1', 0, D, 'ang4d-cricket-empire', [
  Q("Quel pays est le plus passionné de cricket, avec la ligue la plus riche (IPL) ?", ["L'Inde", "Les États-Unis", "Le Canada", "L'Irlande"], "L'Inde", "Le cricket y a été introduit par les Britanniques."),
  Q("Comment s'appelle la série de matchs de cricket historique entre l'Angleterre et l'Australie ?", ["The Ashes", "The Derby", "The Super Bowl", "The Classic"], "The Ashes", "Le trophée est une petite urne de cendres."),
  Q("Comment appelle-t-on un match de cricket sur plusieurs jours entre nations ?", ["Un test match", "Un friendly", "Un final", "Un playoff"], "Un test match", "Il peut durer cinq jours."),
]),
notion('C4-1', 0, D, 'ang4d-voix-passive-sport', [
  Q("Transformez à la voix passive : « Usain Bolt broke the record. »", ["The record was broken by Usain Bolt.", "The record broke by Usain Bolt.", "The record is break by Usain Bolt.", "Usain Bolt was broken the record."], "The record was broken by Usain Bolt.", "Be + participe passé + by."),
  Q("Complétez : « The match ___ watched by millions of people. »", ["was", "has", "did", "is being to"], "was", "Voix passive au prétérit."),
  Q("Complétez : « The next Olympics ___ held in Los Angeles. »", ["will be", "will", "are holding", "is held by"], "will be", "Voix passive au futur."),
]),
notion('C4-1', 0, D, 'ang4d-ali-citations', [
  Q("Quelle célèbre devise de Muhammad Ali décrit sa façon de boxer ?", ["« Float like a butterfly, sting like a bee »", "« Just do it »", "« Faster, higher, stronger »", "« Never give up »"], "« Float like a butterfly, sting like a bee »", "« Voler comme un papillon, piquer comme une abeille »."),
  Q("Quel était le nom de naissance de Muhammad Ali ?", ["Cassius Clay", "Joe Frazier", "George Foreman", "Mike Tyson"], "Cassius Clay", "Il change de nom en 1964."),
  Q("Quelle est la devise olympique ?", ["« Faster, Higher, Stronger – Together »", "« Just do it »", "« Be prepared »", "« Play fair »"], "« Faster, Higher, Stronger – Together »", "« Plus vite, plus haut, plus fort – ensemble »."),
]),
notion('C4-1', 0, D, 'ang4d-sport-identite', [
  Q("Quels sports gaéliques sont joués principalement en Irlande ?", ["Le football gaélique et le hurling", "Le baseball et le basket", "Le cricket et le golf", "Le hockey sur glace et le curling"], "Le football gaélique et le hurling", "Ils sont amateurs et très populaires."),
  Q("Pourquoi le hockey sur glace est-il un symbole d'identité canadienne ?", ["Il est né et s'est développé au Canada avec un climat propice", "Il est interdit ailleurs", "Il a été inventé par la reine", "Les Canadiens ne jouent à rien d'autre"], "Il est né et s'est développé au Canada avec un climat propice", "La Coupe Stanley est le trophée le plus ancien d'Amérique du Nord."),
  Q("Quel sport la nation sud-africaine a-t-elle utilisé comme symbole de réconciliation en 1995 ?", ["Le rugby", "Le cricket", "Le football", "Le golf"], "Le rugby", "Nelson Mandela remet la coupe au capitaine blanc François Pienaar."),
]),
# ══ C4-2 · Voyages et explorations ══
notion('C4-2', 0, F, 'ang4-voyage-vocabulaire', [
  Q("Que signifie « luggage » ?", ["Les bagages", "Le langage", "Le billet", "Le passeport"], "Les bagages", "On dit aussi baggage (US)."),
  Q("Comment dit-on « un billet aller-retour » en anglais britannique ?", ["A return ticket", "A round ticket", "A back ticket", "A double ticket"], "A return ticket", "En anglais américain : a round-trip ticket."),
  Q("Que signifie « to book a room » ?", ["Réserver une chambre", "Lire dans une chambre", "Ranger une chambre", "Louer un livre"], "Réserver une chambre", "Booking = réservation."),
]),
notion('C4-2', 0, F, 'ang4-aeroport', [
  Q("Que signifie « boarding pass » ?", ["La carte d'embarquement", "Le passeport", "La valise", "Le contrôle de sécurité"], "La carte d'embarquement", "To board = embarquer."),
  Q("Que signifie « departures » dans un aéroport ?", ["Les départs", "Les arrivées", "Les bagages", "Les douanes"], "Les départs", "Arrivals = les arrivées."),
  Q("Que signifie « flight » ?", ["Un vol (en avion)", "Une fuite", "Un combat", "Un étage"], "Un vol (en avion)", "Fight = combat."),
]),
notion('C4-2', 0, F, 'ang4-colomb-amerique', [
  Q("Qui a atteint l'Amérique en 1492 ?", ["Christophe Colomb", "James Cook", "Vasco de Gama", "Marco Polo"], "Christophe Colomb", "Il pensait être arrivé en Inde."),
  Q("Quel Viking aurait atteint l'Amérique du Nord vers l'an 1000 ?", ["Leif Erikson", "Erik le Rouge", "Ragnar", "Harald"], "Leif Erikson", "Les Vikings ont fondé un camp à Terre-Neuve."),
  Q("Pourquoi les Amérindiens ont-ils été appelés « Indians » ?", ["Colomb pensait être arrivé en Inde", "Ils venaient d'Inde", "C'était leur propre nom", "À cause de leur langue"], "Colomb pensait être arrivé en Inde", "On dit aujourd'hui Native Americans."),
]),
notion('C4-2', 0, F, 'ang4-espace-astronautes', [
  Q("Comment dit-on « fusée » en anglais ?", ["A rocket", "A rock", "A racket", "A spaceship only"], "A rocket", "Racket = raquette."),
  Q("Que signifie « moon landing » ?", ["L'alunissage", "Le décollage", "Le coucher de lune", "Une éclipse"], "L'alunissage", "To land = atterrir."),
  Q("Quelle est la célèbre phrase de Neil Armstrong sur la Lune ?", ["« That's one small step for man, one giant leap for mankind »", "« Houston, we have a problem »", "« To infinity and beyond »", "« I have a dream »"], "« That's one small step for man, one giant leap for mankind »", "« Un petit pas pour l'homme, un bond de géant pour l'humanité »."),
]),
notion('C4-2', 0, F, 'ang4-carte-boussole', [
  Q("Que signifie « map » ?", ["Une carte", "Un plan de cours", "Un menu", "Une boussole"], "Une carte", "Compass = boussole."),
  Q("Comment dit-on « une île » en anglais ?", ["An island", "An isle only", "An iceland", "An inland"], "An island", "Le s est muet."),
  Q("Que signifie « treasure » ?", ["Un trésor", "Un traité", "Un arbre", "Une tresse"], "Un trésor", "Treasure Island = L'Île au trésor."),
]),
notion('C4-2', 0, F, 'ang4-preterit-voyages', [
  Q("Quel est le prétérit de « sail » (naviguer) ?", ["sailed", "sold", "sail", "sailt"], "sailed", "Verbe régulier."),
  Q("Quel est le prétérit de « find » ?", ["found", "finded", "find", "fond"], "found", "Find, found, found."),
  Q("Quel est le prétérit de « leave » ?", ["left", "leaved", "leave", "lefted"], "left", "Leave, left, left."),
]),
notion('C4-2', 0, F, 'ang4-pays-a-visiter', [
  Q("Que signifie « abroad » ?", ["À l'étranger", "À bord", "Au large", "À la maison"], "À l'étranger", "To travel abroad = voyager à l'étranger."),
  Q("Que signifie « sightseeing » ?", ["Le tourisme, la visite des sites", "La vue", "La randonnée", "Un panneau"], "Le tourisme, la visite des sites", "To go sightseeing = visiter."),
  Q("Comment dit-on « faire ses valises » ?", ["To pack", "To pick", "To package", "To fold"], "To pack", "To unpack = défaire ses valises."),
]),
notion('C4-2', 0, F, 'ang4-titanic', [
  Q("Quel paquebot britannique a coulé en 1912 après avoir heurté un iceberg ?", ["Le Titanic", "Le Queen Mary", "Le Lusitania", "Le Mayflower"], "Le Titanic", "Il effectuait son premier voyage vers New York."),
  Q("Que signifie « iceberg » ?", ["Un bloc de glace flottant", "Une montagne enneigée", "Un glacier de montagne", "Une île"], "Un bloc de glace flottant", "La plus grande partie est sous l'eau."),
  Q("Dans quelle ville le Titanic a-t-il été construit ?", ["Belfast", "Londres", "Liverpool", "Glasgow"], "Belfast", "Un musée lui est consacré."),
]),
notion('C4-2', 0, I, 'ang4i-lewis-clark', [
  Q("Quels explorateurs américains ont traversé l'Ouest jusqu'au Pacifique entre 1804 et 1806 ?", ["Lewis et Clark", "Stanley et Livingstone", "Cook et Banks", "Armstrong et Aldrin"], "Lewis et Clark", "Ils sont envoyés par le président Jefferson."),
  Q("Quelle jeune Amérindienne shoshone a guidé l'expédition de Lewis et Clark ?", ["Sacagawea", "Pocahontas", "Moana", "Mulan"], "Sacagawea", "Elle figure sur une pièce d'un dollar."),
  Q("Quel territoire immense les États-Unis ont-ils acheté à la France en 1803 ?", ["La Louisiane", "L'Alaska", "La Floride", "Le Texas"], "La Louisiane", "La superficie du pays double."),
]),
notion('C4-2', 0, I, 'ang4i-ruee-vers-or', [
  Q("Quel événement de 1848 a attiré des centaines de milliers de personnes en Californie ?", ["La ruée vers l'or", "La guerre de Sécession", "La découverte du pétrole", "La construction de Hollywood"], "La ruée vers l'or", "On les appelle les « forty-niners »."),
  Q("Quelle région du Canada a connu une ruée vers l'or à la fin du XIXe siècle ?", ["Le Klondike", "Le Québec", "L'Ontario", "Terre-Neuve"], "Le Klondike", "Jack London s'en est inspiré."),
  Q("Quel écrivain américain a raconté le Grand Nord dans L'Appel de la forêt ?", ["Jack London", "Mark Twain", "John Steinbeck", "Herman Melville"], "Jack London", "Le héros est un chien, Buck."),
]),
notion('C4-2', 0, I, 'ang4i-oregon-trail-pionniers', [
  Q("Comment appelle-t-on les colons qui partaient vers l'Ouest américain en chariot ?", ["Les pionniers", "Les pèlerins", "Les cow-boys uniquement", "Les conquistadors"], "Les pionniers", "Ils empruntaient l'Oregon Trail."),
  Q("Quel moyen de transport a relié l'est et l'ouest des États-Unis en 1869 ?", ["Le premier chemin de fer transcontinental", "Une autoroute", "Un canal", "Une ligne aérienne"], "Le premier chemin de fer transcontinental", "Les deux lignes se rejoignent dans l'Utah."),
  Q("Quelle conséquence la conquête de l'Ouest a-t-elle eue pour les Amérindiens ?", ["Ils ont été chassés de leurs terres et parqués dans des réserves", "Ils ont reçu de nouvelles terres", "Ils ont dirigé le pays", "Aucune"], "Ils ont été chassés de leurs terres et parqués dans des réserves", "La « Piste des larmes » en est un exemple."),
]),
notion('C4-2', 0, I, 'ang4i-everest', [
  Q("Quels hommes ont atteint les premiers le sommet de l'Everest, en 1953 ?", ["Edmund Hillary et Tenzing Norgay", "Lewis et Clark", "Armstrong et Aldrin", "Scott et Amundsen"], "Edmund Hillary et Tenzing Norgay", "Hillary était néo-zélandais, Tenzing népalais."),
  Q("Pourquoi la nouvelle de la conquête de l'Everest est-elle célébrée en Grande-Bretagne en 1953 ?", ["Elle coïncide avec le couronnement d'Élisabeth II", "Elle coïncide avec la fin de la guerre", "C'est un Anglais seul qui l'a gravi", "C'est le jour de Noël"], "Elle coïncide avec le couronnement d'Élisabeth II", "L'expédition était britannique."),
  Q("Quelle est l'altitude de l'Everest ?", ["Environ 8 849 m", "Environ 4 800 m", "Environ 6 000 m", "Environ 12 000 m"], "Environ 8 849 m", "C'est le toit du monde."),
]),
notion('C4-2', 0, I, 'ang4i-robinson-crusoe', [
  Q("Quel personnage de Daniel Defoe survit seul sur une île déserte pendant 28 ans ?", ["Robinson Crusoé", "Gulliver", "Sinbad", "Ulysse"], "Robinson Crusoé", "Le roman paraît en 1719."),
  Q("Comment s'appelle le compagnon de Robinson sur l'île ?", ["Vendredi (Friday)", "Dimanche", "Samedi", "Lundi"], "Vendredi (Friday)", "Il le rencontre un vendredi."),
  Q("De quelle histoire vraie Defoe s'est-il inspiré ?", ["Celle d'un marin écossais abandonné sur une île du Pacifique", "Celle de Christophe Colomb", "Celle de James Cook", "D'aucune"], "Celle d'un marin écossais abandonné sur une île du Pacifique", "Alexander Selkirk, sur l'archipel Juan Fernández."),
]),
notion('C4-2', 0, I, 'ang4i-present-perfect-voyages', [
  Q("Complétez : « I have ___ to Scotland twice. »", ["been", "gone", "went", "go"], "been", "Have been to = être allé (et revenu)."),
  Q("Quelle différence y a-t-il entre « He has gone to Paris » et « He has been to Paris » ?", ["Gone : il y est encore ; been : il y est allé et revenu", "Aucune", "Been : il y est encore", "Gone : il n'y est jamais allé"], "Gone : il y est encore ; been : il y est allé et revenu", "Nuance importante du present perfect."),
  Q("Complétez : « Have you ever ___ a plane? » (take)", ["taken", "took", "take", "taking"], "taken", "Take, took, taken."),
]),
notion('C4-2', 0, I, 'ang4i-shackleton-scott', [
  Q("Quel explorateur britannique est mort en 1912 au retour du pôle Sud ?", ["Robert Falcon Scott", "Ernest Shackleton", "James Cook", "Edmund Hillary"], "Robert Falcon Scott", "Il est arrivé après Amundsen."),
  Q("Quel continent glacé les explorateurs britanniques ont-ils exploré au début du XXe siècle ?", ["L'Antarctique", "L'Arctique", "L'Asie", "L'Australie"], "L'Antarctique", "Il est protégé par un traité depuis 1959."),
  Q("Quel navire de Shackleton, broyé par les glaces en 1915, a été retrouvé en 2022 ?", ["L'Endurance", "Le Titanic", "Le Beagle", "Le Discovery"], "L'Endurance", "Il reposait à 3 000 m de fond."),
]),
notion('C4-2', 0, I, 'ang4i-darwin-beagle', [
  Q("Quel naturaliste britannique a voyagé autour du monde à bord du Beagle ?", ["Charles Darwin", "Isaac Newton", "James Cook", "Alexander Fleming"], "Charles Darwin", "Le voyage dure de 1831 à 1836."),
  Q("Dans quel archipel Darwin a-t-il observé des pinsons qui ont inspiré sa théorie ?", ["Les Galápagos", "Les Canaries", "Les Hébrides", "Les Maldives"], "Les Galápagos", "Ils appartiennent à l'Équateur."),
  Q("Quel livre de Darwin, publié en 1859, expose la théorie de l'évolution ?", ["L'Origine des espèces", "Le Voyage du Beagle", "Principia", "La Descendance de l'homme"], "L'Origine des espèces", "On the Origin of Species."),
]),
notion('C4-2', 0, D, 'ang4d-mayflower-compact', [
  Q("Quel texte les Pilgrims ont-ils signé à bord du Mayflower en 1620 ?", ["Le Mayflower Compact", "La Déclaration d'indépendance", "La Constitution", "La Magna Carta"], "Le Mayflower Compact", "C'est un premier texte d'autogouvernement."),
  Q("Pourquoi les Pilgrims ont-ils quitté l'Angleterre ?", ["Pour pratiquer librement leur religion", "Pour chercher de l'or", "Pour fuir la peste", "Pour faire du commerce d'épices"], "Pour pratiquer librement leur religion", "Ils étaient des puritains séparatistes."),
  Q("Quelle colonie ont-ils fondée dans le Massachusetts ?", ["Plymouth", "Jamestown", "New Amsterdam", "Québec"], "Plymouth", "Ils l'ont nommée d'après le port anglais."),
]),
notion('C4-2', 0, D, 'ang4d-exploration-spatiale-actuelle', [
  Q("Quel programme de la NASA vise à renvoyer des humains sur la Lune ?", ["Artemis", "Apollo", "Gemini", "Mercury"], "Artemis", "Artémis est la sœur jumelle d'Apollon."),
  Q("Quelle entreprise d'Elon Musk développe des fusées réutilisables ?", ["SpaceX", "Blue Origin", "Boeing", "Virgin Galactic"], "SpaceX", "Blue Origin appartient à Jeff Bezos."),
  Q("Quel robot de la NASA explore Mars depuis 2021 avec un petit hélicoptère ?", ["Perseverance", "Curiosity", "Opportunity", "Spirit"], "Perseverance", "L'hélicoptère s'appelle Ingenuity."),
]),
notion('C4-2', 0, D, 'ang4d-recits-voyage', [
  Q("Quel roman de Jules Verne, traduit en anglais, raconte un tour du monde en 80 jours d'un gentleman anglais ?", ["Le Tour du monde en quatre-vingts jours", "Vingt Mille Lieues sous les mers", "Cinq Semaines en ballon", "L'Île mystérieuse"], "Le Tour du monde en quatre-vingts jours", "Le héros s'appelle Phileas Fogg."),
  Q("Quel roman de Jack Kerouac raconte des voyages à travers les États-Unis ?", ["Sur la route (On the Road)", "Les Raisins de la colère", "Moby Dick", "Gatsby le Magnifique"], "Sur la route (On the Road)", "C'est le roman de la Beat Generation."),
  Q("Quel roman de Herman Melville raconte la chasse d'une baleine blanche ?", ["Moby Dick", "L'Île au trésor", "Robinson Crusoé", "Le Vieil Homme et la Mer"], "Moby Dick", "Le capitaine Achab la poursuit."),
]),
notion('C4-2', 0, D, 'ang4d-passe-perfect', [
  Q("Complétez : « When they arrived, the ship ___ already ___. » (leave)", ["had / left", "has / left", "was / leaving", "did / leave"], "had / left", "Le past perfect marque une action antérieure à une autre action passée."),
  Q("Comment forme-t-on le past perfect ?", ["Had + participe passé", "Have + base verbale", "Was + V-ing", "Did + base verbale"], "Had + participe passé", "I had seen, she had gone…"),
  Q("Que signifie « They had never seen the sea before » ?", ["Ils n'avaient jamais vu la mer auparavant.", "Ils ne verront jamais la mer.", "Ils voient la mer pour la première fois aujourd'hui.", "Ils ont vu la mer hier."], "Ils n'avaient jamais vu la mer auparavant.", "Past perfect avec never."),
]),
notion('C4-2', 0, D, 'ang4d-exploratrices', [
  Q("Quelle aviatrice américaine a été la première femme à traverser l'Atlantique en solitaire, en 1932 ?", ["Amelia Earhart", "Bessie Coleman", "Sally Ride", "Valentina Terechkova"], "Amelia Earhart", "Elle disparaît en 1937 au-dessus du Pacifique."),
  Q("Quelle est la première Américaine allée dans l'espace, en 1983 ?", ["Sally Ride", "Amelia Earhart", "Mae Jemison", "Christa McAuliffe"], "Sally Ride", "Mae Jemison est la première Afro-Américaine, en 1992."),
  Q("Quelle mathématicienne afro-américaine de la NASA a calculé les trajectoires des premiers vols spatiaux ?", ["Katherine Johnson", "Ada Lovelace", "Marie Curie", "Rosalind Franklin"], "Katherine Johnson", "Le film Les Figures de l'ombre raconte son histoire."),
]),
notion('C4-2', 0, D, 'ang4d-routes-commerciales', [
  Q("Quelle compagnie commerciale britannique a dominé l'Inde aux XVIIIe et XIXe siècles ?", ["La Compagnie des Indes orientales (East India Company)", "La Hudson's Bay Company", "La Virginia Company", "La Royal Mail"], "La Compagnie des Indes orientales (East India Company)", "Elle avait sa propre armée."),
  Q("Quelle compagnie britannique a dominé le commerce des fourrures au Canada ?", ["La Hudson's Bay Company", "L'East India Company", "La Banque d'Angleterre", "Rolls-Royce"], "La Hudson's Bay Company", "Fondée en 1670, elle est l'une des plus anciennes entreprises du monde."),
  Q("Quel commerce triangulaire passait par les ports de Liverpool et Bristol au XVIIIe siècle ?", ["La traite des esclaves", "Le commerce du thé uniquement", "Le commerce des fourrures", "Le commerce du pétrole"], "La traite des esclaves", "Liverpool abrite aujourd'hui un musée international de l'esclavage."),
]),
notion('C4-2', 0, D, 'ang4d-voyage-durable', [
  Q("Que signifie « carbon footprint » ?", ["L'empreinte carbone", "Une trace de pas dans le charbon", "Un ticket de train", "Une chaussure écologique"], "L'empreinte carbone", "L'avion a une forte empreinte carbone."),
  Q("Que signifie le mot suédois devenu anglais « flight shame » (flygskam) ?", ["La honte de prendre l'avion", "La peur de l'avion", "Le retard d'un vol", "Un vol annulé"], "La honte de prendre l'avion", "Le mouvement encourage le train."),
  Q("Comment dit-on « randonnée » en anglais ?", ["Hiking", "Riding", "Racing", "Sailing"], "Hiking", "To go hiking = faire de la randonnée."),
]),
notion('C4-2', 0, D, 'ang4d-cook-australie', [
  Q("Quel navire commandait James Cook lors de son premier voyage dans le Pacifique ?", ["L'Endeavour", "Le Beagle", "Le Mayflower", "Le Victory"], "L'Endeavour", "Il part de Plymouth en 1768."),
  Q("Où James Cook est-il mort en 1779 ?", ["À Hawaï", "En Australie", "En Angleterre", "En Nouvelle-Zélande"], "À Hawaï", "Lors d'un affrontement avec des habitants."),
  Q("Pourquoi les voyages de Cook sont-ils aujourd'hui débattus en Australie ?", ["Ils ont ouvert la voie à la colonisation et à la dépossession des Aborigènes", "Il n'a jamais existé", "Il a découvert l'Amérique", "Il était australien"], "Ils ont ouvert la voie à la colonisation et à la dépossession des Aborigènes", "Ses statues sont parfois contestées."),
]),
# ══ C4-3 · Villes, villages, quartiers ══
notion('C4-3', 0, F, 'ang4-directions', [
  Q("Que signifie « Go straight on » ?", ["Allez tout droit.", "Tournez à droite.", "Faites demi-tour.", "Arrêtez-vous."], "Allez tout droit.", "Turn right = tournez à droite."),
  Q("Comment demande-t-on son chemin poliment ?", ["Excuse me, how can I get to the station?", "Where is station, you?", "Give me the station!", "Station where is?"], "Excuse me, how can I get to the station?", "Excuse me pour aborder quelqu'un."),
  Q("Que signifie « It's opposite the bank » ?", ["C'est en face de la banque.", "C'est à côté de la banque.", "C'est derrière la banque.", "C'est dans la banque."], "C'est en face de la banque.", "Opposite = en face de."),
]),
notion('C4-3', 0, F, 'ang4-batiments', [
  Q("Que signifie « town hall » ?", ["La mairie", "Une salle de sport", "Le centre commercial", "La gare"], "La mairie", "City hall en anglais américain."),
  Q("Comment dit-on « hôpital » en anglais ?", ["Hospital", "Hostel", "Hotel", "Hospice"], "Hospital", "Hostel = auberge de jeunesse."),
  Q("Que signifie « church » ?", ["Une église", "Une école", "Un château", "Une ferme"], "Une église", "Cathedral = cathédrale."),
]),
notion('C4-3', 0, F, 'ang4-ville-village', [
  Q("Quelle est la différence entre « town » et « village » ?", ["Town est une petite ville, village est plus petit", "Ils sont identiques", "Village est plus grand", "Town désigne une capitale"], "Town est une petite ville, village est plus petit", "City = grande ville."),
  Q("Que signifie « neighbour » (GB) ?", ["Un voisin", "Un quartier", "Un ami d'enfance", "Un nouveau venu"], "Un voisin", "Neighborhood (US) = quartier."),
  Q("Que signifie « downtown » en anglais américain ?", ["Le centre-ville", "La banlieue", "Le bas de la rue", "La campagne"], "Le centre-ville", "Uptown = quartiers résidentiels plus au nord."),
]),
notion('C4-3', 0, F, 'ang4-magasins', [
  Q("Que signifie « shop assistant » ?", ["Un vendeur, une vendeuse", "Un client", "Un caissier de banque", "Un livreur"], "Un vendeur, une vendeuse", "Customer = client."),
  Q("Comment demande-t-on le prix d'un objet ?", ["How much is it?", "How many is it?", "What price you?", "How cost it?"], "How much is it?", "How much does it cost?"),
  Q("Que signifie « mall » aux États-Unis ?", ["Un centre commercial", "Une rue", "Un marché couvert", "Un parc"], "Un centre commercial", "Shopping centre en anglais britannique."),
]),
notion('C4-3', 0, F, 'ang4-londres-quartiers', [
  Q("Quel quartier londonien est célèbre pour son marché aux puces et ses maisons colorées ?", ["Notting Hill (Portobello Road)", "La City", "Westminster", "Canary Wharf"], "Notting Hill (Portobello Road)", "Un film porte son nom."),
  Q("Quelle place de Londres est célèbre pour ses écrans lumineux ?", ["Piccadilly Circus", "Trafalgar Square", "Leicester Square", "Times Square"], "Piccadilly Circus", "Times Square est à New York."),
  Q("Quel quartier de Londres est célèbre pour son marché couvert et ses artistes de rue ?", ["Covent Garden", "Hyde Park", "Greenwich", "Wimbledon"], "Covent Garden", "Il abrite aussi l'Opéra royal."),
]),
notion('C4-3', 0, F, 'ang4-new-york-quartiers', [
  Q("Quel grand parc se trouve au cœur de Manhattan ?", ["Central Park", "Hyde Park", "Golden Gate Park", "Stanley Park"], "Central Park", "Il ouvre en 1858."),
  Q("Quel quartier de New York est le berceau de la culture afro-américaine ?", ["Harlem", "Wall Street", "SoHo", "Chinatown"], "Harlem", "La « Harlem Renaissance » y fleurit dans les années 1920."),
  Q("Quelle place de New York est célèbre pour ses écrans et son réveillon du Nouvel An ?", ["Times Square", "Piccadilly Circus", "Trafalgar Square", "Union Square"], "Times Square", "Une boule lumineuse descend à minuit."),
]),
notion('C4-3', 0, F, 'ang4-vie-quartier', [
  Q("Que signifie « corner shop » au Royaume-Uni ?", ["Une petite épicerie de quartier", "Un magasin d'angle de luxe", "Un supermarché géant", "Un coin de rue"], "Une petite épicerie de quartier", "Elle est souvent ouverte tard."),
  Q("Que signifie « playground » ?", ["Une aire de jeux", "Un terrain de football", "Un théâtre", "Un parking"], "Une aire de jeux", "Ou une cour de récréation."),
  Q("Comment dit-on « une rue piétonne » ?", ["A pedestrian street", "A walking car street", "A foot road", "A pedestrian car"], "A pedestrian street", "Pedestrian = piéton."),
]),
notion('C4-3', 0, F, 'ang4-logement', [
  Q("Que signifie « flat » en anglais britannique ?", ["Un appartement", "Une maison plate", "Une crevaison", "Un plateau"], "Un appartement", "Apartment en anglais américain."),
  Q("Comment dit-on « un immeuble de bureaux » ?", ["An office block", "An office house", "A bureau tower", "A desk building"], "An office block", "Skyscraper = gratte-ciel."),
  Q("Que signifie « to move house » ?", ["Déménager", "Bouger la maison", "Construire une maison", "Visiter une maison"], "Déménager", "Aux États-Unis : to move."),
]),
notion('C4-3', 0, I, 'ang4i-chinatown-quartiers-ethniques', [
  Q("Quel quartier, présent dans de nombreuses villes anglophones, rassemble une communauté d'origine chinoise ?", ["Chinatown", "Little Italy", "Harlem", "Soho"], "Chinatown", "Celui de San Francisco est le plus ancien d'Amérique du Nord."),
  Q("Quel quartier de New York était peuplé d'immigrés italiens ?", ["Little Italy", "Chinatown", "Harlem", "Queens"], "Little Italy", "Il s'est beaucoup réduit."),
  Q("Pourquoi les immigrés se regroupaient-ils dans certains quartiers ?", ["Pour retrouver leur langue, leurs commerces et l'entraide", "Par obligation légale", "Parce que les autres quartiers étaient vides", "Par hasard"], "Pour retrouver leur langue, leurs commerces et l'entraide", "Ces quartiers sont aussi devenus touristiques."),
]),
notion('C4-3', 0, I, 'ang4i-suburbs', [
  Q("Que signifie « suburbs » ?", ["La banlieue résidentielle", "Le centre-ville", "La campagne isolée", "Le métro"], "La banlieue résidentielle", "Aux États-Unis, elle est souvent aisée."),
  Q("Quelle ville américaine nouvelle des années 1950 symbolise la banlieue pavillonnaire ?", ["Levittown", "Manhattan", "Detroit", "Hollywood"], "Levittown", "Des milliers de maisons identiques y ont été construites."),
  Q("Pourquoi les Américains vivant en banlieue dépendent-ils de la voiture ?", ["Les quartiers sont étalés et mal desservis par les transports", "Les voitures sont gratuites", "Les bus sont interdits", "Ils habitent en centre-ville"], "Les quartiers sont étalés et mal desservis par les transports", "On parle d'urban sprawl."),
]),
notion('C4-3', 0, I, 'ang4i-villes-anglaises', [
  Q("Quelle ville anglaise est la deuxième du pays par la population ?", ["Birmingham", "Manchester", "Liverpool", "Bristol"], "Birmingham", "Elle est au cœur des Midlands."),
  Q("Quelle ville anglaise est célèbre pour ses deux clubs de football et les Beatles ?", ["Liverpool", "Leeds", "Oxford", "Bath"], "Liverpool", "Les Beatles ont joué au Cavern Club."),
  Q("Quelle ville thermale anglaise a été fondée par les Romains ?", ["Bath", "Brighton", "Blackpool", "Dover"], "Bath", "Ses thermes romains sont classés à l'Unesco."),
]),
notion('C4-3', 0, I, 'ang4i-relatifs-lieux', [
  Q("Complétez : « This is the street ___ I live. »", ["where", "which", "who", "when"], "where", "Where pour un lieu."),
  Q("Complétez : « The park ___ is near my house is huge. »", ["which (that)", "who", "where", "whose"], "which (that)", "Which / that pour une chose."),
  Q("Complétez : « I remember the day ___ we moved here. »", ["when", "where", "which", "who"], "when", "When pour un moment."),
]),
notion('C4-3', 0, I, 'ang4i-vie-communautaire', [
  Q("Que signifie « community centre » ?", ["Une maison de quartier", "Un centre commercial", "Un hôpital", "Une mairie"], "Une maison de quartier", "On y organise des activités pour les habitants."),
  Q("Qu'est-ce qu'une « block party » aux États-Unis ?", ["Une fête de rue entre voisins", "Une fête dans un immeuble de bureaux", "Une manifestation", "Un concert de rock"], "Une fête de rue entre voisins", "La rue est fermée à la circulation."),
  Q("Que signifie « charity shop » ?", ["Une boutique solidaire de seconde main", "Une banque", "Un magasin de luxe", "Une pharmacie"], "Une boutique solidaire de seconde main", "Les bénéfices vont à des associations."),
]),
notion('C4-3', 0, I, 'ang4i-villes-us', [
  Q("Quelle ville du Nevada est célèbre pour ses casinos ?", ["Las Vegas", "Reno", "Phoenix", "Denver"], "Las Vegas", "Elle est surnommée « Sin City »."),
  Q("Quelle ville de Louisiane est célèbre pour le jazz et le Mardi gras ?", ["La Nouvelle-Orléans", "Houston", "Atlanta", "Nashville"], "La Nouvelle-Orléans", "Son quartier français est très visité."),
  Q("Quelle ville du Tennessee est la capitale de la musique country ?", ["Nashville", "Memphis", "Chicago", "Austin"], "Nashville", "On l'appelle « Music City »."),
]),
notion('C4-3', 0, I, 'ang4i-londres-histoire', [
  Q("Quel incendie a ravagé Londres en 1666 ?", ["Le Grand Incendie de Londres", "Le Blitz", "La peste", "La tempête"], "Le Grand Incendie de Londres", "Il a détruit une grande partie de la City."),
  Q("Quel architecte a reconstruit la cathédrale Saint-Paul après 1666 ?", ["Christopher Wren", "Norman Foster", "John Nash", "Inigo Jones"], "Christopher Wren", "Elle est achevée en 1710."),
  Q("Comment appelle-t-on les bombardements allemands sur Londres en 1940-1941 ?", ["Le Blitz", "Le Brexit", "Le Grand Incendie", "La Bataille d'Angleterre uniquement"], "Le Blitz", "Les Londoniens se réfugiaient dans le métro."),
]),
notion('C4-3', 0, I, 'ang4i-quantifieurs', [
  Q("Complétez : « There are ___ people in the square. » (beaucoup)", ["a lot of", "much", "a little", "few of"], "a lot of", "A lot of convient aux dénombrables et indénombrables."),
  Q("Complétez : « There isn't ___ traffic today. »", ["much", "many", "a few", "lots"], "much", "Traffic est indénombrable."),
  Q("Complétez : « There are only ___ shops in my village. » (quelques-uns)", ["a few", "a little", "much", "any"], "a few", "A few + dénombrable ; a little + indénombrable."),
]),
notion('C4-3', 0, D, 'ang4d-gentrification', [
  Q("Comment appelle-t-on l'arrivée d'habitants aisés dans un quartier populaire, qui fait monter les loyers ?", ["La gentrification", "La périurbanisation", "La ségrégation", "L'exode rural"], "La gentrification", "Le mot vient de « gentry », la petite noblesse anglaise."),
  Q("Quel quartier de New York est un exemple célèbre de gentrification ?", ["Brooklyn (Williamsburg)", "Manhattan Upper East Side", "Staten Island", "Wall Street"], "Brooklyn (Williamsburg)", "Les anciens entrepôts sont devenus des lofts."),
  Q("Quelle sociologue britannique a inventé le mot « gentrification » en 1964 ?", ["Ruth Glass", "Jane Jacobs", "Saskia Sassen", "Margaret Thatcher"], "Ruth Glass", "Elle étudiait Londres."),
]),
notion('C4-3', 0, D, 'ang4d-jane-jacobs', [
  Q("Quelle urbaniste américaine a défendu la vie de quartier contre les autoroutes urbaines à New York ?", ["Jane Jacobs", "Rachel Carson", "Eleanor Roosevelt", "Ruth Glass"], "Jane Jacobs", "Son livre Déclin et survie des grandes villes américaines paraît en 1961."),
  Q("Qu'est-ce que la « High Line » à New York ?", ["Une ancienne voie ferrée aérienne transformée en promenade plantée", "Une ligne de métro", "Une autoroute", "Un pont suspendu"], "Une ancienne voie ferrée aérienne transformée en promenade plantée", "Elle ouvre en 2009."),
  Q("Quel urbaniste a dessiné les grands parcs de New York, dont Central Park ?", ["Frederick Law Olmsted", "Robert Moses", "Christopher Wren", "Le Corbusier"], "Frederick Law Olmsted", "Avec Calvert Vaux."),
]),
notion('C4-3', 0, D, 'ang4d-segregation-urbaine-us', [
  Q("Quelle pratique discriminatoire refusait des prêts immobiliers dans les quartiers noirs américains ?", ["Le redlining", "Le zoning", "Le busing", "Le gerrymandering"], "Le redlining", "Les quartiers étaient entourés de rouge sur les cartes."),
  Q("Quelle ville du Michigan a perdu plus de la moitié de ses habitants depuis 1950 ?", ["Détroit", "Chicago", "Boston", "Seattle"], "Détroit", "La crise de l'automobile l'a frappée."),
  Q("Que signifie « inner city » aux États-Unis ?", ["Les quartiers centraux pauvres", "Les beaux quartiers", "Le quartier des affaires", "La campagne"], "Les quartiers centraux pauvres", "C'est un sens propre à l'anglais américain."),
]),
notion('C4-3', 0, D, 'ang4d-villes-durables', [
  Q("Quelle mesure Londres a-t-elle adoptée en 2003 pour réduire la circulation au centre ?", ["Le péage urbain (congestion charge)", "L'interdiction des bus", "La fermeture du métro", "La gratuité des parkings"], "Le péage urbain (congestion charge)", "Une zone à très faibles émissions (ULEZ) existe aussi."),
  Q("Quelle ville canadienne est souvent citée comme modèle de ville verte ?", ["Vancouver", "Toronto", "Calgary", "Ottawa"], "Vancouver", "Elle vise 100 % d'énergies renouvelables."),
  Q("Que signifie « green belt » autour des villes britanniques ?", ["Une ceinture verte protégée de l'urbanisation", "Une autoroute", "Une piste cyclable", "Un parc d'attractions"], "Une ceinture verte protégée de l'urbanisation", "Elle limite l'étalement urbain."),
]),
notion('C4-3', 0, D, 'ang4d-villages-anglais', [
  Q("Qu'est-ce qu'un « village green » en Angleterre ?", ["Une pelouse commune au centre du village", "Un parc national", "Un terrain de golf privé", "Un jardin potager"], "Une pelouse commune au centre du village", "On y joue parfois au cricket."),
  Q("Quel bâtiment est souvent au cœur des villages anglais, avec l'église ?", ["Le pub", "Le centre commercial", "La gare TGV", "Le gratte-ciel"], "Le pub", "Beaucoup ferment, ce qui inquiète les villageois."),
  Q("Quelle série britannique se déroule dans un village anglais et ses meurtres mystérieux ?", ["Midsomer Murders (Inspecteur Barnaby)", "Friends", "The Simpsons", "Breaking Bad"], "Midsomer Murders (Inspecteur Barnaby)", "Agatha Christie a aussi imaginé Miss Marple au village de St Mary Mead."),
]),
notion('C4-3', 0, D, 'ang4d-mixite-sociale', [
  Q("Que signifie « council estate » au Royaume-Uni ?", ["Un quartier de logements sociaux", "Un domaine du roi", "Un conseil municipal", "Une zone industrielle"], "Un quartier de logements sociaux", "Council = conseil municipal, qui les gère."),
  Q("Que signifie « social housing » ?", ["Le logement social", "Une maison de retraite", "Un réseau social", "Un hôtel"], "Le logement social", "Public housing aux États-Unis."),
  Q("Quel incendie d'une tour de logements sociaux à Londres a fait 72 morts en 2017 ?", ["L'incendie de la tour Grenfell", "Le Grand Incendie", "L'incendie du Parlement", "L'incendie de Notre-Dame"], "L'incendie de la tour Grenfell", "Il a révélé des inégalités et des négligences."),
]),
notion('C4-3', 0, D, 'ang4d-modaux-conseil-ville', [
  Q("Complétez : « You ___ visit the British Museum, it's amazing! » (conseil)", ["should", "mustn't", "can't", "needn't"], "should", "Should = conseil."),
  Q("Complétez : « You ___ take the Tube, it's faster. » (suggestion)", ["could", "couldn't", "mustn't", "won't"], "could", "Could peut exprimer une suggestion."),
  Q("Que signifie « You'd better take an umbrella » ?", ["Tu ferais mieux de prendre un parapluie.", "Tu as pris un parapluie.", "Tu prendras un parapluie.", "Tu n'as pas besoin de parapluie."], "Tu ferais mieux de prendre un parapluie.", "Had better = ferais mieux de."),
]),
notion('C4-3', 0, D, 'ang4d-megacities-anglophones', [
  Q("Quelle mégapole indienne, ancienne Bombay, est la capitale financière du pays ?", ["Mumbai", "Delhi", "Bangalore", "Chennai"], "Mumbai", "Elle abrite Bollywood."),
  Q("Quelle ville nigériane est l'une des plus grandes métropoles d'Afrique ?", ["Lagos", "Abuja", "Accra", "Nairobi"], "Lagos", "Elle compte plus de 15 millions d'habitants."),
  Q("Quelle cité-État anglophone d'Asie est connue pour sa propreté et ses jardins verticaux ?", ["Singapour", "Hong Kong", "Kuala Lumpur", "Bangkok"], "Singapour", "Elle est surnommée « city in a garden »."),
]),
]
