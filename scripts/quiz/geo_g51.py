# Géographie 5e · La question démographique et l'inégal développement : au moins 50 questions par niveau
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Facile ══
notion('G5-1', 0, F, 'geo5-natalite', [
  Q("Comment appelle-t-on le nombre de naissances dans une population pendant une année ?", ["La natalité", "La mortalité", "La fécondité", "L'espérance de vie"], "La natalité", "On l'exprime souvent en taux pour 1 000 habitants."),
  Q("Comment appelle-t-on le nombre de décès dans une population pendant une année ?", ["La mortalité", "La natalité", "La migration", "La densité"], "La mortalité", "Elle a fortement baissé grâce aux progrès médicaux."),
  Q("Que se passe-t-il quand il y a plus de naissances que de décès ?", ["La population augmente", "La population diminue", "La population ne change jamais", "La population vieillit forcément"], "La population augmente", "C'est l'accroissement naturel positif."),
]),
notion('G5-1', 0, F, 'geo5-esperance-vie', [
  Q("Qu'est-ce que l'espérance de vie ?", ["Le nombre moyen d'années que peut espérer vivre un nouveau-né", "L'âge de la retraite", "L'âge moyen de la population", "Le nombre d'enfants par femme"], "Le nombre moyen d'années que peut espérer vivre un nouveau-né", "Elle mesure les conditions de santé d'un pays."),
  Q("Quelle est environ l'espérance de vie à la naissance en France ?", ["Environ 83 ans", "Environ 50 ans", "Environ 65 ans", "Environ 100 ans"], "Environ 83 ans", "Les femmes vivent en moyenne plus longtemps que les hommes."),
  Q("Pourquoi l'espérance de vie a-t-elle augmenté dans le monde ?", ["Grâce aux progrès de la médecine, de l'hygiène et de l'alimentation", "Parce que le climat s'est réchauffé", "Parce que les gens travaillent plus", "Parce qu'il y a moins d'enfants"], "Grâce aux progrès de la médecine, de l'hygiène et de l'alimentation", "Les vaccins ont joué un rôle majeur."),
]),
notion('G5-1', 0, F, 'geo5-densite', [
  Q("Qu'est-ce que la densité de population ?", ["Le nombre d'habitants par km²", "Le nombre total d'habitants", "Le nombre de villes", "Le nombre de naissances"], "Le nombre d'habitants par km²", "Elle mesure la répartition de la population."),
  Q("Comment appelle-t-on une région où vivent très nombreux habitants ?", ["Un foyer de peuplement", "Un désert humain", "Une zone vide", "Un front pionnier"], "Un foyer de peuplement", "Asie de l'Est, Asie du Sud et Europe sont les trois grands foyers."),
  Q("Quels milieux sont souvent des « déserts humains » ?", ["Les déserts chauds, les régions polaires et les hautes montagnes", "Les grandes plaines fertiles", "Les littoraux tempérés", "Les vallées des grands fleuves"], "Les déserts chauds, les régions polaires et les hautes montagnes", "Les contraintes naturelles y sont fortes."),
]),
notion('G5-1', 0, F, 'geo5-foyers-peuplement', [
  Q("Quels sont les trois grands foyers de peuplement du monde ?", ["Asie de l'Est, Asie du Sud et Europe", "Afrique du Nord, Australie et Canada", "Amazonie, Sibérie et Sahara", "Groenland, Alaska et Patagonie"], "Asie de l'Est, Asie du Sud et Europe", "Ils réunissent la majorité de l'humanité."),
  Q("Sur quel continent vit plus de la moitié de la population mondiale ?", ["L'Asie", "L'Afrique", "L'Europe", "L'Amérique"], "L'Asie", "Environ 60 % des humains y vivent."),
  Q("Où se concentre souvent la population dans un pays ?", ["Près des littoraux et des grands fleuves", "Au sommet des montagnes", "Dans les déserts", "Près des pôles"], "Près des littoraux et des grands fleuves", "L'eau et les échanges attirent les hommes."),
]),
notion('G5-1', 0, F, 'geo5-population-france', [
  Q("Combien d'habitants compte environ la France ?", ["Environ 68 millions", "Environ 30 millions", "Environ 150 millions", "Environ 10 millions"], "Environ 68 millions", "Outre-mer compris."),
  Q("Quel est le pays le plus peuplé d'Afrique ?", ["Le Nigeria", "L'Égypte", "L'Afrique du Sud", "Le Maroc"], "Le Nigeria", "Il compte plus de 220 millions d'habitants."),
  Q("Quel est le troisième pays le plus peuplé du monde ?", ["Les États-Unis", "Le Brésil", "La Russie", "L'Indonésie"], "Les États-Unis", "Après l'Inde et la Chine."),
]),
notion('G5-1', 0, F, 'geo5-pyramide-ages', [
  Q("Quel graphique représente la population par âge et par sexe ?", ["La pyramide des âges", "Le diagramme climatique", "Le croquis", "La courbe de température"], "La pyramide des âges", "Les hommes sont à gauche, les femmes à droite."),
  Q("Une pyramide des âges à base large signifie que la population est…", ["jeune", "âgée", "en diminution", "stable"], "jeune", "Il y a beaucoup d'enfants."),
  Q("Une pyramide des âges en forme de « toupie » ou d'« urne » indique une population…", ["vieillissante", "très jeune", "en forte croissance", "rurale"], "vieillissante", "La base se rétrécit : il y a moins de naissances."),
]),
notion('G5-1', 1, F, 'geo5-pays-riches-pauvres', [
  Q("Quel indicateur mesure la richesse produite dans un pays en un an ?", ["Le PIB (produit intérieur brut)", "L'IDH", "La densité", "La natalité"], "Le PIB (produit intérieur brut)", "On le divise souvent par le nombre d'habitants."),
  Q("Quel continent compte le plus de pays parmi les moins avancés (PMA) ?", ["L'Afrique", "L'Europe", "L'Amérique du Nord", "L'Océanie"], "L'Afrique", "Les PMA sont les pays les plus pauvres du monde."),
  Q("Laquelle de ces situations est un signe de pauvreté ?", ["Ne pas avoir accès à l'eau potable", "Avoir une voiture", "Partir en vacances à l'étranger", "Avoir un ordinateur portable"], "Ne pas avoir accès à l'eau potable", "Environ 2 milliards de personnes n'y ont pas un accès sûr."),
]),
notion('G5-1', 1, F, 'geo5-scolarisation', [
  Q("Pourquoi l'école est-elle importante pour le développement ?", ["Elle permet d'apprendre, de mieux se soigner et de trouver un emploi", "Elle ne sert à rien", "Elle remplace le travail", "Elle est réservée aux riches"], "Elle permet d'apprendre, de mieux se soigner et de trouver un emploi", "L'éducation est un pilier du développement."),
  Q("Comment appelle-t-on la capacité à lire et à écrire ?", ["L'alphabétisation", "La scolarisation", "La natalité", "L'urbanisation"], "L'alphabétisation", "Le taux d'alphabétisation entre dans l'IDH."),
  Q("Qui sont le plus souvent privés d'école dans les pays pauvres ?", ["Les filles des zones rurales", "Les garçons des villes", "Les enfants des riches", "Personne"], "Les filles des zones rurales", "La scolarisation des filles est un levier de développement."),
]),
notion('G5-1', 1, F, 'geo5-acces-sante', [
  Q("Pourquoi la mortalité infantile est-elle plus forte dans les pays pauvres ?", ["Manque de soins, de vaccins, d'eau potable et de nourriture", "Parce qu'il fait chaud", "Parce que les enfants y sont plus nombreux", "Ce n'est pas le cas"], "Manque de soins, de vaccins, d'eau potable et de nourriture", "Elle a toutefois beaucoup baissé depuis 1990."),
  Q("Qu'est-ce que la mortalité infantile ?", ["Le nombre d'enfants qui meurent avant un an", "Le nombre de personnes âgées qui meurent", "Le nombre d'accidents de la route", "Le nombre de naissances"], "Le nombre d'enfants qui meurent avant un an", "On l'exprime pour 1 000 naissances."),
  Q("Quelle maladie, transmise par un moustique, tue encore beaucoup d'enfants en Afrique ?", ["Le paludisme", "La grippe", "La varicelle", "Le rhume"], "Le paludisme", "Les moustiquaires aident à s'en protéger."),
]),
notion('G5-1', 1, F, 'geo5-inegalites-locales', [
  Q("Dans une même ville, peut-on trouver des quartiers très riches et très pauvres ?", ["Oui", "Non, jamais", "Seulement en Europe", "Seulement à la campagne"], "Oui", "Les inégalités existent à toutes les échelles."),
  Q("Quelle ville d'Inde abrite l'un des plus grands bidonvilles d'Asie, Dharavi ?", ["Mumbai", "Delhi", "Calcutta", "Bangalore"], "Mumbai", "Il est voisin de quartiers d'affaires très riches."),
  Q("Comment appelle-t-on l'écart entre les plus riches et les plus pauvres ?", ["Les inégalités", "La croissance", "La densité", "L'urbanisation"], "Les inégalités", "Elles s'observent entre pays et à l'intérieur des pays."),
]),
notion('G5-1', 0, F, 'geo5-croissance-mondiale', [
  Q("Combien d'habitants comptait la Terre vers 1950 ?", ["Environ 2,5 milliards", "Environ 8 milliards", "Environ 500 millions", "Environ 15 milliards"], "Environ 2,5 milliards", "La population a plus que triplé depuis."),
  N("Vers quelle année la Terre a-t-elle dépassé 8 milliards d'habitants ?", 2022, "Selon l'ONU, le 15 novembre 2022."),
  Q("Comment appelle-t-on la très forte croissance de la population mondiale au XXe siècle ?", ["L'explosion démographique", "Le déclin démographique", "L'exode rural", "La transition énergétique"], "L'explosion démographique", "Elle est due à la baisse de la mortalité."),
]),
notion('G5-1', 0, F, 'geo5-jeunes-vieux', [
  Q("Dans quel continent la population est-elle la plus jeune ?", ["L'Afrique", "L'Europe", "L'Amérique du Nord", "L'Océanie"], "L'Afrique", "L'âge médian y est inférieur à 20 ans."),
  Q("Quel défi pose une population très jeune ?", ["Construire assez d'écoles et créer des emplois", "Payer beaucoup de retraites", "Construire des maisons de retraite", "Réduire le nombre d'écoles"], "Construire assez d'écoles et créer des emplois", "Les jeunes arrivent nombreux sur le marché du travail."),
  Q("Quel défi pose une population âgée ?", ["Financer les retraites et la santé des personnes âgées", "Construire beaucoup d'écoles", "Nourrir beaucoup d'enfants", "Créer des crèches partout"], "Financer les retraites et la santé des personnes âgées", "La part des actifs diminue."),
]),
notion('G5-1', 1, F, 'geo5-carte-idh', [
  Q("Quel pays a l'un des IDH les plus élevés du monde ?", ["La Suisse ou la Norvège", "Le Niger", "Le Tchad", "La Somalie"], "La Suisse ou la Norvège", "Ils sont régulièrement en tête du classement."),
  Q("Quelle couleur indique souvent les pays les plus développés sur une carte de l'IDH ?", ["La plus foncée de la légende", "Toujours le blanc", "Toujours le rouge vif", "Il n'y a pas de légende"], "La plus foncée de la légende", "Il faut toujours lire la légende d'une carte."),
  Q("Quelle région du monde concentre les IDH les plus faibles ?", ["L'Afrique subsaharienne", "L'Europe du Nord", "L'Amérique du Nord", "L'Asie de l'Est"], "L'Afrique subsaharienne", "Le Niger, le Tchad ou la Somalie sont en bas du classement."),
]),
# ══ Intermédiaire ══
notion('G5-1', 0, I, 'geo5i-taux-demographiques', [
  Q("Un pays a un taux de natalité de 30 ‰ et un taux de mortalité de 10 ‰. Quel est son taux d'accroissement naturel ?", ["20 ‰", "40 ‰", "3 ‰", "10 ‰"], "20 ‰", "Natalité moins mortalité."),
  Q("Que signifie le symbole ‰ ?", ["Pour mille", "Pour cent", "Pour un million", "Par kilomètre carré"], "Pour mille", "Les taux démographiques sont souvent exprimés pour 1 000 habitants."),
  N("Un pays compte 2 millions d'habitants sur 100 000 km². Quelle est sa densité (hab./km²) ?", 20, "2 000 000 ÷ 100 000 = 20."),
]),
notion('G5-1', 0, I, 'geo5i-seuil-remplacement', [
  Q("Quel indice de fécondité assure le renouvellement des générations dans les pays développés ?", ["Environ 2,1 enfants par femme", "Environ 1 enfant par femme", "Environ 4 enfants par femme", "Environ 6 enfants par femme"], "Environ 2,1 enfants par femme", "On parle de seuil de remplacement des générations."),
  Q("Quel est environ l'indice de fécondité en France au milieu des années 2020 ?", ["Environ 1,6", "Environ 3", "Environ 0,5", "Environ 5"], "Environ 1,6", "Il est en baisse depuis 2010."),
  Q("Quel pays a l'un des indices de fécondité les plus bas du monde, inférieur à 1 ?", ["La Corée du Sud", "Le Niger", "Le Nigeria", "L'Inde"], "La Corée du Sud", "Elle est autour de 0,7 enfant par femme."),
]),
notion('G5-1', 0, I, 'geo5i-etapes-transition', [
  Q("Lors de la première phase de la transition démographique, qu'est-ce qui baisse en premier ?", ["La mortalité", "La natalité", "La population", "L'espérance de vie"], "La mortalité", "La natalité reste forte : la population augmente vite."),
  Q("Que se passe-t-il à la fin de la transition démographique ?", ["Natalité et mortalité sont faibles ; la croissance ralentit", "Natalité et mortalité sont fortes", "La population explose", "Il n'y a plus de naissances"], "Natalité et mortalité sont faibles ; la croissance ralentit", "C'est le cas de l'Europe aujourd'hui."),
  Q("Quel continent est encore au milieu de sa transition démographique ?", ["L'Afrique subsaharienne", "L'Europe", "L'Amérique du Nord", "L'Asie de l'Est"], "L'Afrique subsaharienne", "La natalité y reste élevée."),
]),
notion('G5-1', 0, I, 'geo5i-inde', [
  Q("Combien d'habitants compte environ l'Inde ?", ["Plus de 1,4 milliard", "Environ 400 millions", "Environ 800 millions", "Environ 3 milliards"], "Plus de 1,4 milliard", "Elle dépasse la Chine depuis 2023."),
  Q("Quel grand fleuve sacré concentre une très forte densité de population en Inde ?", ["Le Gange", "Le Nil", "Le Mékong", "L'Amazone"], "Le Gange", "Sa vallée est l'une des plus peuplées du monde."),
  Q("Pourquoi l'Inde est-elle un « géant démographique » encore jeune ?", ["Sa natalité reste plus élevée que celle de la Chine", "Sa mortalité est très forte", "Elle accueille beaucoup d'immigrés", "Elle a interdit les naissances"], "Sa natalité reste plus élevée que celle de la Chine", "Sa fécondité est proche de 2 enfants par femme."),
]),
notion('G5-1', 0, I, 'geo5i-politiques-natalistes', [
  Q("Comment appelle-t-on une politique qui encourage les naissances ?", ["Une politique nataliste", "Une politique antinataliste", "Une politique migratoire", "Une politique industrielle"], "Une politique nataliste", "Elle repose sur des aides aux familles."),
  Q("Quel pays européen mène une politique nataliste forte, avec des aides fiscales pour les mères de famille nombreuse ?", ["La Hongrie", "La Suisse", "Le Portugal", "L'Irlande"], "La Hongrie", "Sa fécondité reste pourtant basse."),
  Q("Quel type de politique la Chine a-t-elle adopté depuis 2021 ?", ["Elle autorise trois enfants par couple et encourage les naissances", "Elle impose l'enfant unique", "Elle interdit les naissances", "Elle impose cinq enfants"], "Elle autorise trois enfants par couple et encourage les naissances", "Elle redoute le vieillissement."),
]),
notion('G5-1', 0, I, 'geo5i-croissance-effets', [
  Q("Quel effet une forte croissance démographique peut-elle avoir dans un pays pauvre ?", ["Une pression sur les ressources, les écoles et les emplois", "Une baisse des besoins", "Un vieillissement rapide", "La disparition des villes"], "Une pression sur les ressources, les écoles et les emplois", "Mais une population jeune est aussi une ressource."),
  Q("Comment appelle-t-on l'avantage d'avoir beaucoup d'actifs et peu de personnes à charge ?", ["Le dividende démographique", "Le baby-boom", "Le papy-boom", "L'exode rural"], "Le dividende démographique", "Il a favorisé l'essor de l'Asie de l'Est."),
  Q("Quel effet la croissance démographique a-t-elle sur les villes des pays du Sud ?", ["Une croissance urbaine très rapide, avec des bidonvilles", "Leur disparition", "Leur vieillissement", "Aucun effet"], "Une croissance urbaine très rapide, avec des bidonvilles", "Lagos ou Kinshasa grandissent très vite."),
]),
notion('G5-1', 0, I, 'geo5i-projections', [
  Q("Selon l'ONU, combien d'habitants la Terre pourrait-elle compter vers 2080 ?", ["Environ 10,3 milliards", "Environ 5 milliards", "Environ 20 milliards", "Environ 8 milliards, sans changement"], "Environ 10,3 milliards", "Le pic serait atteint au milieu des années 2080."),
  Q("Quelle population devrait baisser d'ici 2050 ?", ["Celle de nombreux pays d'Europe et d'Asie de l'Est", "Celle du Nigeria", "Celle de l'Afrique entière", "Celle de l'Inde"], "Celle de nombreux pays d'Europe et d'Asie de l'Est", "Le Japon perd déjà des habitants."),
  Q("Pourquoi la croissance de la population mondiale ralentit-elle ?", ["Parce que la fécondité baisse presque partout", "Parce que la mortalité augmente", "Parce que les migrations s'arrêtent", "Elle ne ralentit pas"], "Parce que la fécondité baisse presque partout", "La fécondité mondiale est passée de 5 à environ 2,3."),
]),
notion('G5-1', 1, I, 'geo5i-extreme-pauvrete', [
  Q("Quel seuil la Banque mondiale utilise-t-elle pour définir l'extrême pauvreté ?", ["Environ 3 dollars par jour et par personne", "100 dollars par jour", "10 centimes par mois", "1 000 dollars par jour"], "Environ 3 dollars par jour et par personne", "Le seuil a été relevé de 2,15 à 3 dollars en 2025."),
  Q("Comment a évolué la part de la population mondiale en extrême pauvreté depuis 1990 ?", ["Elle a fortement baissé", "Elle a doublé", "Elle n'a pas bougé", "Elle a triplé"], "Elle a fortement baissé", "Grâce surtout à la croissance de l'Asie."),
  Q("Quel pays a sorti des centaines de millions de personnes de l'extrême pauvreté depuis 1980 ?", ["La Chine", "Le Niger", "Haïti", "Le Soudan du Sud"], "La Chine", "Grâce à une croissance économique rapide."),
]),
notion('G5-1', 1, I, 'geo5i-pib-habitant', [
  Q("Comment calcule-t-on le PIB par habitant ?", ["On divise le PIB par le nombre d'habitants", "On multiplie le PIB par la population", "On additionne les salaires", "On compte les entreprises"], "On divise le PIB par le nombre d'habitants", "Il permet de comparer des pays de tailles différentes."),
  Q("Quel pays a le PIB le plus élevé du monde ?", ["Les États-Unis", "La Chine", "Le Japon", "L'Allemagne"], "Les États-Unis", "La Chine est deuxième."),
  Q("Pourquoi un pays peut-il avoir un PIB élevé et un PIB par habitant moyen ?", ["Parce qu'il est très peuplé", "Parce qu'il est petit", "Parce qu'il est désertique", "C'est impossible"], "Parce qu'il est très peuplé", "C'est le cas de la Chine ou de l'Inde."),
]),
notion('G5-1', 1, I, 'geo5i-acteurs-developpement', [
  Q("Comment appelle-t-on les associations humanitaires indépendantes des États ?", ["Les ONG", "Les ODD", "Les PMA", "Les BRICS"], "Les ONG", "Organisations non gouvernementales, comme Médecins sans frontières."),
  Q("Quelle institution financière internationale prête aux pays pour financer leur développement ?", ["La Banque mondiale", "La Banque de France", "La Bourse de Paris", "L'OMS"], "La Banque mondiale", "Elle est créée en 1944."),
  Q("Qu'est-ce que le microcrédit ?", ["De petits prêts accordés à des personnes pauvres pour créer une activité", "Un très gros prêt à un État", "Une carte bancaire", "Un impôt"], "De petits prêts accordés à des personnes pauvres pour créer une activité", "Muhammad Yunus a reçu le prix Nobel de la paix en 2006 pour cela."),
]),
notion('G5-1', 1, I, 'geo5i-nord-sud-nuances', [
  Q("Pourquoi l'opposition simple « Nord riche / Sud pauvre » est-elle trop simple aujourd'hui ?", ["Parce que de nombreux pays du Sud se sont enrichis et que des pauvres vivent au Nord", "Parce que tous les pays sont égaux", "Parce que le Sud est plus riche que le Nord", "Parce qu'il n'y a plus de pauvreté"], "Parce que de nombreux pays du Sud se sont enrichis et que des pauvres vivent au Nord", "On parle de « Suds » au pluriel."),
  Q("Quel petit pays du Golfe a l'un des PIB par habitant les plus élevés du monde ?", ["Le Qatar", "Le Yémen", "L'Afghanistan", "Le Soudan"], "Le Qatar", "Grâce au gaz naturel."),
  Q("Quel pays d'Asie est passé de la pauvreté à un niveau de vie élevé en un demi-siècle ?", ["La Corée du Sud", "Le Népal", "Le Bangladesh", "Le Laos"], "La Corée du Sud", "C'est l'un des « dragons » asiatiques."),
]),
notion('G5-1', 1, I, 'geo5i-inegalites-genre', [
  Q("Qui travaille le plus souvent sans être payé (tâches domestiques, eau, bois) dans les pays pauvres ?", ["Les femmes et les filles", "Les hommes", "Les personnes âgées seulement", "Personne"], "Les femmes et les filles", "Cela limite leur accès à l'école et à l'emploi."),
  Q("Pourquoi la scolarisation des filles fait-elle baisser la fécondité ?", ["Elles se marient plus tard et maîtrisent mieux leur fécondité", "Parce que l'école l'interdit", "Parce qu'elles quittent le pays", "Ce n'est pas le cas"], "Elles se marient plus tard et maîtrisent mieux leur fécondité", "C'est un levier essentiel du développement."),
  Q("Quel indicateur de l'ONU mesure les inégalités entre femmes et hommes ?", ["L'indice d'inégalité de genre", "Le PIB", "La densité", "L'indice de fécondité"], "L'indice d'inégalité de genre", "Il est publié avec l'IDH."),
]),
notion('G5-1', 1, I, 'geo5i-acces-electricite', [
  Q("Environ combien de personnes n'ont pas accès à l'électricité dans le monde ?", ["Environ 700 millions", "Environ 7 millions", "Environ 4 milliards", "Personne"], "Environ 700 millions", "Surtout en Afrique subsaharienne."),
  Q("Quelle solution se développe dans les villages africains sans réseau électrique ?", ["Les panneaux solaires individuels ou les mini-réseaux", "Les centrales nucléaires", "Les éoliennes géantes en mer", "Les centrales à charbon dans chaque village"], "Les panneaux solaires individuels ou les mini-réseaux", "Le solaire est adapté aux zones isolées."),
  Q("Quel outil a permis à des millions d'Africains d'accéder à des services bancaires ?", ["Le paiement par téléphone mobile", "Le chèque", "La carte bancaire en or", "Le distributeur dans chaque village"], "Le paiement par téléphone mobile", "M-Pesa au Kenya en est l'exemple le plus connu."),
]),
notion('G5-1', 0, I, 'geo5i-recensement', [
  Q("Comment appelle-t-on le comptage officiel de la population d'un pays ?", ["Le recensement", "Le sondage", "Le cadastre", "L'état civil"], "Le recensement", "En France, il est réalisé par l'Insee."),
  Q("Quel organisme réalise le recensement en France ?", ["L'Insee", "La CNIL", "Météo-France", "La SNCF"], "L'Insee", "Institut national de la statistique et des études économiques."),
  Q("Pourquoi le recensement est-il utile ?", ["Pour prévoir les écoles, les hôpitaux et les transports nécessaires", "Pour fixer les notes scolaires", "Pour élire le président", "Pour calculer la météo"], "Pour prévoir les écoles, les hôpitaux et les transports nécessaires", "Il aide les pouvoirs publics à aménager le territoire."),
]),
# ══ Avancé ══
notion('G5-1', 0, D, 'geo5d-age-median', [
  Q("Qu'est-ce que l'âge médian d'une population ?", ["L'âge qui partage la population en deux moitiés égales", "L'âge moyen des décès", "L'âge de la majorité", "L'âge de la retraite"], "L'âge qui partage la population en deux moitiés égales", "La moitié est plus jeune, l'autre plus âgée."),
  Q("Quel est environ l'âge médian au Niger ?", ["Environ 15 ans", "Environ 45 ans", "Environ 30 ans", "Environ 60 ans"], "Environ 15 ans", "C'est l'un des plus bas du monde."),
  Q("Quel est environ l'âge médian au Japon ?", ["Près de 49 ans", "Environ 15 ans", "Environ 25 ans", "Environ 70 ans"], "Près de 49 ans", "C'est l'un des plus élevés du monde."),
]),
notion('G5-1', 0, D, 'geo5d-taux-dependance', [
  Q("Qu'est-ce que le rapport de dépendance démographique ?", ["Le rapport entre les jeunes et les âgés d'une part, et les actifs d'autre part", "Le rapport entre villes et campagnes", "Le rapport entre hommes et femmes", "Le nombre d'immigrés"], "Le rapport entre les jeunes et les âgés d'une part, et les actifs d'autre part", "Il mesure la charge qui pèse sur les actifs."),
  Q("Pourquoi le rapport de dépendance est-il élevé à la fois au Niger et au Japon ?", ["Au Niger à cause des jeunes, au Japon à cause des personnes âgées", "Pour les mêmes raisons", "Parce qu'ils ont la même population", "Il n'est élevé dans aucun des deux"], "Au Niger à cause des jeunes, au Japon à cause des personnes âgées", "Les défis sont donc très différents."),
  Q("Comment appelle-t-on l'arrivée à l'âge de la retraite des générations nombreuses du baby-boom ?", ["Le papy-boom", "Le baby-boom", "Le dividende démographique", "La transition urbaine"], "Le papy-boom", "Il pèse sur les systèmes de retraite."),
]),
notion('G5-1', 0, D, 'geo5d-solde-migratoire', [
  Q("Comment appelle-t-on la différence entre les entrées et les sorties de migrants d'un pays ?", ["Le solde migratoire", "Le solde naturel", "Le taux de natalité", "La densité"], "Le solde migratoire", "Ajouté au solde naturel, il donne la variation de population."),
  Q("Pourquoi la population de l'Allemagne augmente-t-elle malgré plus de décès que de naissances ?", ["Grâce à un solde migratoire positif", "Grâce à une forte natalité", "Grâce à une forte mortalité", "Elle diminue fortement"], "Grâce à un solde migratoire positif", "L'immigration compense le solde naturel négatif."),
  Q("Quel pays d'Europe de l'Est perd des habitants à cause d'une faible natalité et de l'émigration ?", ["La Bulgarie", "La France", "L'Irlande", "Le Luxembourg"], "La Bulgarie", "Elle a perdu près d'un quart de sa population depuis 1990."),
]),
notion('G5-1', 0, D, 'geo5d-japon-declin', [
  Q("Depuis quand la population du Japon diminue-t-elle ?", ["Depuis la fin des années 2000", "Depuis 1945", "Depuis 1800", "Elle augmente"], "Depuis la fin des années 2000", "Le pays perd plusieurs centaines de milliers d'habitants par an."),
  Q("Quelle solution le Japon utilise-t-il pour compenser le manque de main-d'œuvre ?", ["La robotisation et, plus récemment, un peu d'immigration", "Une forte natalité", "L'exode rural", "Le travail des enfants"], "La robotisation et, plus récemment, un peu d'immigration", "L'immigration reste limitée."),
  Q("Quel phénomène touche les villages japonais ?", ["Ils se vident et vieillissent (dépeuplement rural)", "Ils se remplissent de jeunes", "Ils deviennent des mégapoles", "Ils sont tous détruits"], "Ils se vident et vieillissent (dépeuplement rural)", "Des millions de maisons sont abandonnées."),
]),
notion('G5-1', 0, D, 'geo5d-sex-ratio', [
  Q("Qu'est-ce que le sex-ratio à la naissance ?", ["Le nombre de garçons pour 100 filles à la naissance", "Le nombre de mariages", "Le nombre de femmes actives", "La part des femmes au Parlement"], "Le nombre de garçons pour 100 filles à la naissance", "Il est naturellement d'environ 105."),
  Q("Pourquoi le sex-ratio est-il déséquilibré en Chine et en Inde ?", ["À cause de la préférence pour les garçons et des avortements sélectifs", "À cause du climat", "À cause des migrations", "Il n'est pas déséquilibré"], "À cause de la préférence pour les garçons et des avortements sélectifs", "Des millions de femmes « manquent »."),
  Q("Quelle conséquence ce déséquilibre a-t-il en Chine ?", ["Des millions d'hommes ne trouvent pas d'épouse", "Une hausse de la natalité", "Une baisse de l'espérance de vie", "Aucune"], "Des millions d'hommes ne trouvent pas d'épouse", "On parle des « branches nues »."),
]),
notion('G5-1', 0, D, 'geo5d-malthus', [
  Q("Quel penseur anglais du XVIIIe siècle craignait que la population croisse plus vite que les ressources ?", ["Thomas Malthus", "Adam Smith", "Karl Marx", "Charles Darwin"], "Thomas Malthus", "Son Essai sur le principe de population paraît en 1798."),
  Q("Pourquoi les craintes de Malthus ne se sont-elles pas réalisées à l'échelle mondiale ?", ["Grâce aux progrès agricoles qui ont fait croître la production", "Parce que la population a baissé", "Parce que les guerres ont tout réglé", "Elles se sont réalisées partout"], "Grâce aux progrès agricoles qui ont fait croître la production", "La production alimentaire a augmenté plus vite que la population."),
  Q("Quelle économiste danoise a montré que la croissance démographique pouvait stimuler l'innovation agricole ?", ["Ester Boserup", "Rachel Carson", "Esther Duflo", "Elinor Ostrom"], "Ester Boserup", "Elle s'oppose à la vision malthusienne."),
]),
notion('G5-1', 0, D, 'geo5d-fecondite-baisse-causes', [
  Q("Quel facteur explique le mieux la baisse de la fécondité dans le monde ?", ["L'éducation des filles et l'urbanisation", "La hausse des températures", "La baisse de l'espérance de vie", "L'augmentation de la mortalité"], "L'éducation des filles et l'urbanisation", "L'accès à la contraception joue aussi."),
  Q("Pourquoi les familles rurales pauvres ont-elles souvent beaucoup d'enfants ?", ["Les enfants aident aux travaux et assurent les vieux jours de leurs parents", "Par obligation légale", "Parce que l'école est obligatoire", "Parce que la mortalité est nulle"], "Les enfants aident aux travaux et assurent les vieux jours de leurs parents", "En l'absence de retraite, les enfants sont une sécurité."),
  Q("Quel pays musulman a connu une baisse de fécondité très rapide, de plus de 6 à moins de 2 enfants par femme ?", ["L'Iran", "Le Niger", "Le Tchad", "L'Afghanistan"], "L'Iran", "En une vingtaine d'années, entre 1985 et 2005."),
]),
notion('G5-1', 1, D, 'geo5d-gini', [
  Q("Quel coefficient mesure les inégalités de revenus à l'intérieur d'un pays ?", ["Le coefficient de Gini", "L'IDH", "Le taux de natalité", "Le PIB"], "Le coefficient de Gini", "Il varie de 0 (égalité parfaite) à 1 (inégalité maximale)."),
  Q("Quel pays a l'un des coefficients de Gini les plus élevés du monde ?", ["L'Afrique du Sud", "La Suède", "La Slovaquie", "Le Danemark"], "L'Afrique du Sud", "C'est un héritage de l'apartheid."),
  Q("Comment appelle-t-on une moyenne qui cache de grands écarts ?", ["Une moyenne trompeuse qu'il faut compléter par la répartition", "Une médiane", "Un indice parfait", "Un pourcentage"], "Une moyenne trompeuse qu'il faut compléter par la répartition", "Le PIB par habitant ne dit rien de la répartition des richesses."),
]),
notion('G5-1', 1, D, 'geo5d-pma', [
  Q("Que signifie le sigle PMA en géographie du développement ?", ["Pays les moins avancés", "Pays moyennement aisés", "Pays membres associés", "Politique monétaire africaine"], "Pays les moins avancés", "L'ONU en compte environ 44."),
  Q("Sur quels critères l'ONU classe-t-elle un pays parmi les PMA ?", ["Revenu par habitant, capital humain et vulnérabilité économique", "Superficie et climat", "Nombre de villes", "Langue officielle"], "Revenu par habitant, capital humain et vulnérabilité économique", "Les critères sont revus tous les trois ans."),
  Q("Quel pays d'Asie, en forte croissance, est en voie de sortir de la liste des PMA ?", ["Le Bangladesh", "Le Japon", "La Chine", "Singapour"], "Le Bangladesh", "Le Népal et le Laos sont aussi en voie de sortie."),
]),
notion('G5-1', 1, D, 'geo5d-dette-aide', [
  Q("Pourquoi la dette est-elle un frein au développement de certains pays pauvres ?", ["Le remboursement absorbe une part des ressources qui pourraient financer l'école ou la santé", "Elle n'a aucun effet", "Elle enrichit automatiquement les pays", "Elle est interdite"], "Le remboursement absorbe une part des ressources qui pourraient financer l'école ou la santé", "Des annulations de dette ont eu lieu dans les années 2000."),
  Q("Quelle initiative des années 1990-2000 a permis d'alléger la dette des pays pauvres très endettés ?", ["L'initiative PPTE", "Le plan Marshall", "Le traité de Maastricht", "Le protocole de Kyoto"], "L'initiative PPTE", "Pays pauvres très endettés."),
  Q("Quelle institution internationale prête aux États en crise financière ?", ["Le Fonds monétaire international (FMI)", "L'Unesco", "L'OMS", "La FAO"], "Le Fonds monétaire international (FMI)", "Il impose souvent des conditions de rigueur."),
]),
notion('G5-1', 1, D, 'geo5d-rente-ressources', [
  Q("Comment appelle-t-on le paradoxe de pays riches en ressources naturelles mais restés pauvres ?", ["La « malédiction des ressources »", "Le dividende démographique", "La transition démographique", "Le développement durable"], "La « malédiction des ressources »", "La rente profite souvent à une minorité."),
  Q("Quel pays riche en minerais (cobalt, cuivre) reste l'un des plus pauvres du monde ?", ["La république démocratique du Congo", "La Norvège", "L'Australie", "Le Canada"], "La république démocratique du Congo", "Les conflits et la corruption freinent son développement."),
  Q("Quel pays utilise sa rente pétrolière pour alimenter un grand fonds souverain au profit des générations futures ?", ["La Norvège", "Le Nigeria", "Le Venezuela", "Le Soudan"], "La Norvège", "Son fonds est le plus grand du monde."),
]),
notion('G5-1', 1, D, 'geo5d-classes-moyennes', [
  Q("Quel groupe social se développe fortement dans les pays émergents ?", ["Les classes moyennes", "La noblesse", "Les esclaves", "Les paysans sans terre uniquement"], "Les classes moyennes", "Elles accèdent à la consommation de masse."),
  Q("Quel pays d'Amérique latine a créé en 2003 la « Bolsa Família », aide aux familles pauvres conditionnée à la scolarisation ?", ["Le Brésil", "Le Chili", "Le Mexique", "Cuba"], "Le Brésil", "Elle a contribué à réduire la pauvreté."),
  Q("Comment appelle-t-on les pays qui ne sont ni parmi les plus pauvres ni parmi les plus riches ?", ["Les pays à revenu intermédiaire", "Les PMA", "Les pays du G7", "Les pays enclavés"], "Les pays à revenu intermédiaire", "La majorité des pauvres du monde y vivent."),
]),
notion('G5-1', 1, D, 'geo5d-idhi', [
  Q("Que mesure l'IDH ajusté aux inégalités (IDHI) ?", ["Le développement en tenant compte de sa répartition dans la population", "Uniquement le PIB", "La densité", "Les inégalités entre pays seulement"], "Le développement en tenant compte de sa répartition dans la population", "Il est toujours inférieur ou égal à l'IDH."),
  Q("Quel organisme publie l'IDH chaque année ?", ["Le PNUD (Programme des Nations unies pour le développement)", "La Banque de France", "L'OTAN", "L'Union européenne"], "Le PNUD (Programme des Nations unies pour le développement)", "L'IDH est créé en 1990."),
  Q("Quel économiste indien a inspiré l'IDH par sa réflexion sur les « capabilités » ?", ["Amartya Sen", "Muhammad Yunus", "Gandhi", "Nehru"], "Amartya Sen", "Il reçoit le prix Nobel d'économie en 1998."),
]),
notion('G5-1', 1, D, 'geo5d-inegalites-france', [
  Q("Quel département de France métropolitaine a le taux de pauvreté le plus élevé ?", ["La Seine-Saint-Denis", "Les Hauts-de-Seine", "La Haute-Savoie", "Les Yvelines"], "La Seine-Saint-Denis", "Elle jouxte pourtant Paris, très riche."),
  Q("Quel territoire français a le taux de pauvreté le plus élevé ?", ["Mayotte", "Paris", "L'Alsace", "La Bretagne"], "Mayotte", "Plus des trois quarts de ses habitants vivent sous le seuil de pauvreté national."),
  Q("Comment l'Insee définit-il le seuil de pauvreté en France ?", ["60 % du revenu médian", "La moitié du SMIC", "1 euro par jour", "Le revenu minimum des pays pauvres"], "60 % du revenu médian", "La pauvreté est donc relative."),
]),
]
