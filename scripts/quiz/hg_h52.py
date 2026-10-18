# Histoire 5e · Société, Église et pouvoir politique dans l'Occident féodal (XIe-XVe siècles) : au moins 50 questions par niveau
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Facile ══
notion('H5-2', 0, F, 'hg5-trois-ordres', [
  Q("Selon les clercs du Moyen Âge, en combien d'ordres la société est-elle divisée ?", ["Trois", "Deux", "Quatre", "Cinq"], "Trois", "Ceux qui prient, ceux qui combattent et ceux qui travaillent."),
  Q("Comment appelle-t-on « ceux qui prient » ?", ["Le clergé", "La noblesse", "Les paysans", "Les bourgeois"], "Le clergé", "Il comprend les prêtres, les moines et les évêques."),
  Q("Qui sont « ceux qui travaillent » dans la société médiévale ?", ["Surtout les paysans", "Les chevaliers", "Les évêques", "Les rois"], "Surtout les paysans", "Ils forment l'immense majorité de la population."),
]),
notion('H5-2', 0, F, 'hg5-vie-paysanne', [
  Q("Où vit la grande majorité de la population au Moyen Âge ?", ["À la campagne", "En ville", "Dans les monastères", "Dans les châteaux"], "À la campagne", "Plus de 9 personnes sur 10 sont des paysans."),
  Q("Quel bâtiment est au cœur de la vie du village médiéval ?", ["L'église paroissiale", "La mairie", "L'école", "Le marché couvert"], "L'église paroissiale", "Le cimetière l'entoure souvent."),
  Q("Quel outil sert aux paysans à couper les céréales ?", ["La faucille", "La herse", "Le fléau", "La charrue"], "La faucille", "Le fléau sert ensuite à battre les épis."),
]),
notion('H5-2', 0, F, 'hg5-chevalier', [
  Q("Comment appelle-t-on la chemise de métal portée par le chevalier ?", ["La cotte de mailles", "L'armure de plates", "Le haubert de cuir", "Le bouclier"], "La cotte de mailles", "Elle est faite de petits anneaux de fer."),
  Q("Comment appelle-t-on les combats d'entraînement entre chevaliers ?", ["Les tournois", "Les croisades", "Les jacqueries", "Les foires"], "Les tournois", "Ils permettent de montrer sa valeur et de gagner des rançons."),
  Q("Comment appelle-t-on le cheval de combat du chevalier ?", ["Le destrier", "Le palefroi", "Le mulet", "Le poney"], "Le destrier", "Le palefroi est le cheval de voyage."),
]),
notion('H5-2', 0, F, 'hg5-moines-abbayes', [
  Q("Comment appelle-t-on un monastère dirigé par un abbé ?", ["Une abbaye", "Une cathédrale", "Une paroisse", "Une commanderie"], "Une abbaye", "Les moines y vivent à l'écart du monde."),
  Q("Quelle règle de vie suivent de nombreux moines d'Occident ?", ["La règle de saint Benoît", "La règle de saint Louis", "Le Code civil", "La règle de saint Martin"], "La règle de saint Benoît", "Elle partage la journée entre prière, travail et lecture."),
  Q("Quelle devise résume la vie des moines bénédictins ?", ["« Prie et travaille » (Ora et labora)", "« Liberté, égalité, fraternité »", "« Dieu le veut »", "« Montjoie Saint-Denis »"], "« Prie et travaille » (Ora et labora)", "Les moines défrichent et copient des manuscrits."),
]),
notion('H5-2', 0, F, 'hg5-cluny-citeaux', [
  Q("Quelle grande abbaye bourguignonne est fondée en 910 ?", ["Cluny", "Cîteaux", "Le Mont-Saint-Michel", "Fontenay"], "Cluny", "Elle devient la tête d'un vaste réseau de monastères."),
  Q("Comment appelle-t-on les moines de l'ordre fondé à Cîteaux en 1098 ?", ["Les cisterciens", "Les franciscains", "Les dominicains", "Les jésuites"], "Les cisterciens", "Ils recherchent la simplicité et la pauvreté."),
  Q("Quel moine cistercien célèbre prêche la deuxième croisade en 1146 ?", ["Saint Bernard de Clairvaux", "Saint François d'Assise", "Saint Benoît", "Saint Dominique"], "Saint Bernard de Clairvaux", "Il est l'une des grandes voix de l'Église du XIIe siècle."),
]),
notion('H5-2', 1, F, 'hg5-artisans-ville', [
  Q("Pourquoi les villes médiévales sont-elles entourées de remparts ?", ["Pour se protéger des attaques", "Pour empêcher les habitants de sortir", "Pour décorer la ville", "Pour retenir l'eau"], "Pour se protéger des attaques", "Les portes sont fermées la nuit."),
  Q("Comment appelle-t-on le jeune qui apprend un métier auprès d'un maître artisan ?", ["Un apprenti", "Un vassal", "Un serf", "Un moine"], "Un apprenti", "Il devient ensuite compagnon, puis parfois maître."),
  Q("Que doit réaliser un compagnon pour devenir maître artisan ?", ["Un chef-d'œuvre", "Un pèlerinage", "Un tournoi", "Un serment au roi"], "Un chef-d'œuvre", "C'est l'origine du mot."),
]),
notion('H5-2', 1, F, 'hg5-cathedrale', [
  Q("Quelle cathédrale de Paris est construite à partir de 1163 ?", ["Notre-Dame", "Le Sacré-Cœur", "Saint-Denis", "La Sainte-Chapelle"], "Notre-Dame", "Elle est achevée au milieu du XIVe siècle."),
  Q("À quoi servent les vitraux des églises médiévales, en plus de laisser passer la lumière ?", ["À raconter des scènes de la Bible aux fidèles", "À indiquer l'heure", "À protéger du froid uniquement", "À afficher les lois du roi"], "À raconter des scènes de la Bible aux fidèles", "La plupart des fidèles ne savent pas lire."),
  Q("Qui dirige la construction d'une cathédrale ?", ["L'évêque, avec un maître d'œuvre", "Le roi seul", "Les chevaliers", "Le pape lui-même"], "L'évêque, avec un maître d'œuvre", "Les chantiers durent souvent plus d'un siècle."),
]),
notion('H5-2', 2, F, 'hg5-philippe-auguste', [
  Q("Quel roi fait construire le Louvre comme forteresse vers 1190 ?", ["Philippe Auguste", "Saint Louis", "Charles VII", "François Ier"], "Philippe Auguste", "Il fait aussi entourer Paris d'une enceinte."),
  Q("Quelle région Philippe Auguste reprend-il au roi d'Angleterre en 1204 ?", ["La Normandie", "La Bretagne", "La Provence", "L'Alsace"], "La Normandie", "Le domaine royal s'agrandit fortement."),
  Q("Quel surnom porte le roi Philippe II ?", ["Auguste", "Le Bel", "Le Sage", "Le Bien-Aimé"], "Auguste", "Il agrandit le royaume, comme l'empereur romain Auguste."),
]),
notion('H5-2', 2, F, 'hg5-saint-louis', [
  Q("Où, selon la tradition, Saint Louis rendait-il la justice sous un chêne ?", ["À Vincennes", "À Versailles", "À Reims", "À Avignon"], "À Vincennes", "Le roi apparaît comme le grand justicier du royaume."),
  Q("Quel édifice Saint Louis fait-il construire à Paris pour abriter la couronne d'épines ?", ["La Sainte-Chapelle", "Notre-Dame", "Le Louvre", "La basilique Saint-Denis"], "La Sainte-Chapelle", "Elle est consacrée en 1248."),
  Q("De quel roi Saint Louis est-il le petit-fils ?", ["Philippe Auguste", "Hugues Capet", "Philippe le Bel", "Charles VII"], "Philippe Auguste", "Son père, Louis VIII, règne peu de temps."),
]),
notion('H5-2', 2, F, 'hg5-valois', [
  Q("Quelle dynastie succède aux Capétiens directs en 1328 ?", ["Les Valois", "Les Bourbons", "Les Carolingiens", "Les Plantagenêts"], "Les Valois", "Ce sont des Capétiens d'une branche cadette."),
  Q("Quel est le premier roi de la dynastie des Valois ?", ["Philippe VI", "Charles VII", "Louis XI", "François Ier"], "Philippe VI", "Il devient roi en 1328."),
  N("En quelle année commence la guerre de Cent Ans ?", 1337, "Elle dure en réalité jusqu'en 1453, avec des trêves."),
]),
notion('H5-2', 1, F, 'hg5-peste-noire', [
  Q("Quelle épidémie frappe l'Europe à partir de 1347 ?", ["La peste noire", "La grippe espagnole", "Le choléra", "La variole"], "La peste noire", "Elle arrive par les ports de la Méditerranée."),
  Q("Quelle part environ de la population européenne meurt de la peste noire ?", ["Entre un tiers et la moitié", "Un dixième", "Les trois quarts", "Presque personne"], "Entre un tiers et la moitié", "Des villages entiers disparaissent."),
  Q("Par quoi la peste se transmet-elle surtout aux humains ?", ["Par les puces des rats", "Par l'eau des rivières", "Par le froid", "Par les chevaux"], "Par les puces des rats", "Les médecins du temps ignorent cette cause."),
]),
notion('H5-2', 0, F, 'hg5-pelerinages', [
  Q("Vers quelle ville d'Espagne se dirige un grand pèlerinage médiéval ?", ["Saint-Jacques-de-Compostelle", "Madrid", "Séville", "Tolède"], "Saint-Jacques-de-Compostelle", "On y vénère le tombeau de l'apôtre Jacques."),
  Q("Quel symbole porte le pèlerin de Compostelle ?", ["La coquille Saint-Jacques", "La croix rouge", "La fleur de lys", "Le croissant"], "La coquille Saint-Jacques", "Elle sert aussi de petite écuelle."),
  Q("Comment appelle-t-on les restes d'un saint vénérés par les fidèles ?", ["Des reliques", "Des icônes", "Des enluminures", "Des ex-voto"], "Des reliques", "Elles attirent les pèlerins vers les églises."),
]),
# ══ Intermédiaire ══
notion('H5-2', 1, I, 'hg5i-marchands-banque', [
  Q("Quel document permet à un marchand de payer à distance sans transporter de pièces ?", ["La lettre de change", "Le billet de banque", "La charte de franchise", "Le capitulaire"], "La lettre de change", "Elle est utilisée par les marchands italiens."),
  Q("Quelle ville de Flandre est un grand centre de la draperie et du commerce au XIVe siècle ?", ["Bruges", "Lyon", "Bordeaux", "Marseille"], "Bruges", "Les marchands italiens et hanséatiques s'y rencontrent."),
  Q("Comment appelle-t-on ceux qui changent les monnaies et prêtent de l'argent ?", ["Les changeurs, ancêtres des banquiers", "Les baillis", "Les échevins", "Les jongleurs"], "Les changeurs, ancêtres des banquiers", "Le mot « banque » vient du banc où ils travaillaient."),
]),
notion('H5-2', 1, I, 'hg5i-hanse', [
  Q("Comment s'appelle l'association de villes marchandes d'Europe du Nord au Moyen Âge ?", ["La Hanse", "La Ligue lombarde", "La Commune", "La Fronde"], "La Hanse", "Elle domine le commerce de la Baltique et de la mer du Nord."),
  Q("Quelle ville allemande est le principal centre de la Hanse ?", ["Lübeck", "Munich", "Cologne", "Berlin"], "Lübeck", "Elle est surnommée la « reine de la Hanse »."),
  Q("Quels produits la Hanse transporte-t-elle surtout ?", ["Bois, céréales, fourrures, poissons salés", "Épices et soie", "Café et sucre", "Or et diamants"], "Bois, céréales, fourrures, poissons salés", "Le hareng salé est un produit essentiel."),
]),
notion('H5-2', 1, I, 'hg5i-universites', [
  Q("Quelle ville d'Italie abrite l'une des plus anciennes universités d'Europe ?", ["Bologne", "Venise", "Naples", "Rome"], "Bologne", "Elle est réputée pour l'enseignement du droit."),
  Q("En quelle langue enseigne-t-on dans les universités médiévales ?", ["En latin", "En français", "En grec", "En arabe"], "En latin", "C'est la langue commune des savants d'Europe."),
  Q("Quel grand théologien enseigne à l'université de Paris au XIIIe siècle ?", ["Thomas d'Aquin", "Érasme", "Luther", "Voltaire"], "Thomas d'Aquin", "Il concilie la foi chrétienne et la philosophie d'Aristote."),
]),
notion('H5-2', 0, I, 'hg5i-feodalite', [
  Q("Comment appelle-t-on la terre confiée par un seigneur à son vassal ?", ["Un fief", "Une tenure servile", "Un alleu", "Une commune"], "Un fief", "En échange, le vassal doit fidélité et services."),
  Q("Comment appelle-t-on le seigneur à qui un vassal prête hommage ?", ["Son suzerain", "Son serf", "Son évêque", "Son bailli"], "Son suzerain", "Le roi est en principe le suzerain suprême."),
  Q("Que doit le vassal à son seigneur ?", ["L'aide (surtout militaire) et le conseil", "Uniquement de l'argent", "Rien du tout", "Sa terre"], "L'aide (surtout militaire) et le conseil", "Le seigneur lui doit protection et entretien."),
]),
notion('H5-2', 0, I, 'hg5i-paix-de-dieu', [
  Q("Comment appelle-t-on le mouvement par lequel l'Église cherche à limiter les violences des chevaliers vers l'an mil ?", ["La paix de Dieu", "La croisade", "La Reconquista", "La guerre sainte"], "La paix de Dieu", "Elle protège les clercs, les paysans et les églises."),
  Q("Que interdit la « trêve de Dieu » ?", ["De combattre certains jours de la semaine et pendant les fêtes religieuses", "De construire des châteaux", "De faire du commerce", "De se marier"], "De combattre certains jours de la semaine et pendant les fêtes religieuses", "La guerre est interdite du jeudi soir au lundi matin."),
  Q("Quel modèle l'Église propose-t-elle aux chevaliers ?", ["Le chevalier chrétien, protecteur des faibles", "Le chevalier pillard", "Le chevalier marchand", "Le chevalier moine uniquement"], "Le chevalier chrétien, protecteur des faibles", "C'est l'idéal de la chevalerie."),
]),
notion('H5-2', 0, I, 'hg5i-eglise-sanctions', [
  Q("Quelle sanction l'Église peut-elle prononcer en excluant un fidèle de la communauté ?", ["L'excommunication", "Le bannissement", "La corvée", "La taille"], "L'excommunication", "L'excommunié est privé des sacrements."),
  Q("Comment appelle-t-on un chrétien que l'Église accuse de s'écarter de la foi officielle ?", ["Un hérétique", "Un païen", "Un infidèle", "Un pèlerin"], "Un hérétique", "L'hérésie est sévèrement réprimée."),
  Q("Comment appelle-t-on le tribunal de l'Église créé au XIIIe siècle pour poursuivre les hérétiques ?", ["L'Inquisition", "Le Parlement", "Le concile", "La Curie"], "L'Inquisition", "Elle est souvent confiée aux dominicains."),
]),
notion('H5-2', 2, I, 'hg5i-domaine-royal', [
  Q("Comment appelle-t-on les terres gouvernées directement par le roi ?", ["Le domaine royal", "Le royaume tout entier", "Les fiefs des vassaux", "Les États pontificaux"], "Le domaine royal", "Il est petit à l'avènement d'Hugues Capet."),
  Q("Par quels moyens les rois capétiens agrandissent-ils leur domaine ?", ["Conquêtes, mariages, héritages et confiscations", "Uniquement par l'achat", "Par des élections", "Par des échanges avec le pape"], "Conquêtes, mariages, héritages et confiscations", "Le mariage avec l'héritière de Champagne en est un exemple."),
  Q("Comment appelle-t-on, dans le Midi, l'agent royal équivalent du bailli ?", ["Le sénéchal", "Le prévôt des marchands", "Le connétable", "Le chancelier"], "Le sénéchal", "Baillis et sénéchaux représentent le roi dans les provinces."),
]),
notion('H5-2', 2, I, 'hg5i-impots-roi', [
  Q("Comment s'appelle l'impôt royal sur le sel ?", ["La gabelle", "La taille", "La dîme", "Le cens"], "La gabelle", "Il devient très impopulaire."),
  Q("Comment s'appelle l'impôt direct royal payé surtout par les paysans ?", ["La taille", "La gabelle", "La jizya", "Le tonlieu"], "La taille", "Le clergé et la noblesse en sont exemptés."),
  Q("Pourquoi le roi a-t-il besoin d'impôts réguliers à la fin du Moyen Âge ?", ["Pour payer une armée permanente et son administration", "Pour construire des églises", "Pour financer les foires", "Pour payer les papes"], "Pour payer une armée permanente et son administration", "La guerre de Cent Ans pousse à cette évolution."),
]),
notion('H5-2', 2, I, 'hg5i-parlement-justice', [
  Q("Quel est le rôle du Parlement de Paris au Moyen Âge ?", ["C'est la cour de justice suprême du roi", "C'est une assemblée élue qui vote les lois", "C'est un conseil de moines", "C'est un marché"], "C'est la cour de justice suprême du roi", "Il n'a rien d'un parlement au sens actuel."),
  Q("Que peut faire un sujet mécontent d'un jugement seigneurial, à partir du XIIIe siècle ?", ["Faire appel à la justice du roi", "Rien du tout", "S'adresser au pape seulement", "Changer de royaume"], "Faire appel à la justice du roi", "L'appel renforce l'autorité royale."),
  Q("Pourquoi rendre la justice renforce-t-il le pouvoir du roi ?", ["Le roi apparaît comme le garant de la paix et de l'ordre dans tout le royaume", "Parce que la justice rapporte des terres", "Parce que les seigneurs n'ont plus de justice", "Parce que le pape le lui interdit"], "Le roi apparaît comme le garant de la paix et de l'ordre dans tout le royaume", "Saint Louis incarne ce roi justicier."),
]),
notion('H5-2', 2, I, 'hg5i-cent-ans-batailles', [
  Q("Quelle bataille de 1346 voit les archers anglais écraser la chevalerie française ?", ["Crécy", "Bouvines", "Marignan", "Castillon"], "Crécy", "Les arcs longs anglais sont redoutables."),
  Q("Quelle grande défaite française a lieu en 1415 face au roi Henri V ?", ["Azincourt", "Poitiers 732", "Orléans", "Formigny"], "Azincourt", "Une grande partie de la noblesse française y périt."),
  Q("Quelle ville assiégée par les Anglais est délivrée en 1429 ?", ["Orléans", "Paris", "Calais", "Bordeaux"], "Orléans", "Jeanne d'Arc y joue un rôle décisif."),
]),
notion('H5-2', 0, I, 'hg5i-essor-campagnes', [
  Q("Quel équipement se répand dans les campagnes pour moudre le grain, d'abord grâce à l'eau puis au vent ?", ["Le moulin", "Le pressoir", "La forge", "Le four à pain"], "Le moulin", "Le seigneur impose souvent l'usage de son moulin."),
  Q("Comment évolue la population de l'Occident entre l'an mil et 1300 ?", ["Elle augmente fortement", "Elle diminue de moitié", "Elle reste stable", "Elle disparaît des campagnes"], "Elle augmente fortement", "Elle double peut-être, avant la crise du XIVe siècle."),
  Q("Comment appelle-t-on les nouveaux villages créés lors de la mise en culture de nouvelles terres ?", ["Des villeneuves", "Des faubourgs", "Des abbayes", "Des communes urbaines"], "Des villeneuves", "On parle aussi de sauvetés ou de bastides dans le Sud-Ouest."),
]),
notion('H5-2', 2, I, 'hg5i-hastings', [
  N("En quelle année Guillaume, duc de Normandie, conquiert-il l'Angleterre à la bataille de Hastings ?", 1066, "Il devient roi d'Angleterre tout en restant vassal du roi de France."),
  Q("Quel surnom porte Guillaume, duc de Normandie, après sa victoire de 1066 ?", ["Le Conquérant", "Le Bâtard seulement", "Cœur de Lion", "Le Pieux"], "Le Conquérant", "On l'appelait aussi Guillaume le Bâtard avant la conquête."),
  Q("Quelle broderie de près de 70 mètres raconte la conquête de l'Angleterre par Guillaume ?", ["La tapisserie de Bayeux", "La tapisserie de l'Apocalypse", "Le retable de Gand", "La Dame à la licorne"], "La tapisserie de Bayeux", "C'est une source historique exceptionnelle."),
]),
# ══ Avancé ══
notion('H5-2', 0, D, 'hg5d-cathares', [
  Q("Contre quels hérétiques du Languedoc le pape lance-t-il une croisade en 1209 ?", ["Les cathares", "Les vaudois", "Les hussites", "Les protestants"], "Les cathares", "On parle de croisade des Albigeois."),
  Q("Quelle forteresse cathare tombe en 1244, suivie du bûcher de plus de 200 cathares ?", ["Montségur", "Carcassonne", "Albi", "Toulouse"], "Montségur", "C'est l'un des derniers refuges cathares."),
  Q("Quelle conséquence politique a la croisade des Albigeois ?", ["Le Languedoc est progressivement rattaché au domaine royal", "La Provence devient anglaise", "Le pape s'installe à Toulouse", "Les cathares fondent un royaume"], "Le Languedoc est progressivement rattaché au domaine royal", "Le comté de Toulouse revient à la couronne en 1271."),
]),
notion('H5-2', 0, D, 'hg5d-reforme-gregorienne', [
  Q("Quel pape lance au XIe siècle une grande réforme de l'Église qui porte son nom ?", ["Grégoire VII", "Urbain II", "Léon III", "Innocent III"], "Grégoire VII", "Il veut libérer l'Église de l'emprise des laïcs."),
  Q("Quel empereur vient s'humilier devant le pape à Canossa en 1077 ?", ["Henri IV", "Otton Ier", "Frédéric II", "Charles Quint"], "Henri IV", "Il demande la levée de son excommunication."),
  Q("Comment appelle-t-on le conflit entre le pape et l'empereur sur la nomination des évêques ?", ["La querelle des Investitures", "Le Grand Schisme", "La guerre de Cent Ans", "La Fronde"], "La querelle des Investitures", "Elle se règle par le concordat de Worms en 1122."),
]),
notion('H5-2', 2, D, 'hg5d-philippe-le-bel-papaute', [
  Q("Quel épisode de 1303 voit des envoyés de Philippe le Bel s'en prendre au pape Boniface VIII ?", ["L'attentat d'Anagni", "Le concile de Trente", "La paix d'Arras", "Le sacre de Reims"], "L'attentat d'Anagni", "Il montre l'affirmation du roi face au pape."),
  Q("Dans quelle ville la papauté s'installe-t-elle à partir de 1309 ?", ["Avignon", "Paris", "Lyon", "Reims"], "Avignon", "Les papes y résident jusqu'en 1377."),
  Q("Comment appelle-t-on la période (1378-1417) où deux, puis trois papes se disputent la tête de l'Église ?", ["Le Grand Schisme d'Occident", "Le schisme de 1054", "La Réforme", "La querelle des Investitures"], "Le Grand Schisme d'Occident", "Il affaiblit l'autorité de la papauté."),
]),
notion('H5-2', 1, D, 'hg5d-revoltes-1358', [
  Q("Quel prévôt des marchands de Paris se révolte contre le pouvoir royal en 1358 ?", ["Étienne Marcel", "Jacques Cœur", "Bertrand du Guesclin", "Jacques Bonhomme"], "Étienne Marcel", "Il est assassiné la même année."),
  Q("Comment appelle-t-on la révolte paysanne de 1358 en Île-de-France et en Picardie ?", ["La Jacquerie", "La Fronde", "La Commune", "Les Croquants"], "La Jacquerie", "Le nom vient de « Jacques Bonhomme », surnom des paysans."),
  Q("Dans quel contexte éclatent ces révoltes de 1358 ?", ["Après la défaite de Poitiers (1356) et la capture du roi Jean le Bon", "Après la victoire de Bouvines", "Pendant la Renaissance", "Après la mort de Saint Louis"], "Après la défaite de Poitiers (1356) et la capture du roi Jean le Bon", "Le royaume traverse une grave crise."),
]),
notion('H5-2', 2, D, 'hg5d-charles-v', [
  Q("Quel roi, surnommé « le Sage », redresse le royaume après 1364 ?", ["Charles V", "Charles VI", "Jean le Bon", "Louis XI"], "Charles V", "Il reprend une grande partie des terres perdues."),
  Q("Quel chef de guerre breton, connétable de Charles V, mène la reconquête contre les Anglais ?", ["Bertrand du Guesclin", "Étienne Marcel", "Jacques Cœur", "Roland"], "Bertrand du Guesclin", "Il pratique une guerre d'usure."),
  Q("Quelle collection Charles V rassemble-t-il au Louvre ?", ["Une grande bibliothèque", "Une ménagerie", "Un trésor de reliques uniquement", "Une collection d'armes à feu"], "Une grande bibliothèque", "Elle est à l'origine de la future Bibliothèque nationale."),
]),
notion('H5-2', 2, D, 'hg5d-traite-troyes', [
  N("En quelle année le traité de Troyes désigne-t-il le roi d'Angleterre Henri V comme héritier du royaume de France ?", 1420, "Le dauphin Charles est déshérité."),
  Q("Quel roi de France fou signe le traité de Troyes ?", ["Charles VI", "Charles V", "Charles VII", "Louis XI"], "Charles VI", "Il souffre de crises de folie depuis 1392."),
  Q("Quelle guerre civile déchire la France au début du XVe siècle ?", ["La guerre entre Armagnacs et Bourguignons", "La guerre des Deux-Roses", "Les guerres de Religion", "La guerre de Sécession"], "La guerre entre Armagnacs et Bourguignons", "Les Bourguignons s'allient aux Anglais."),
]),
notion('H5-2', 2, D, 'hg5d-proces-jeanne', [
  Q("Dans quelle ville Jeanne d'Arc est-elle jugée puis brûlée en 1431 ?", ["Rouen", "Orléans", "Reims", "Paris"], "Rouen", "La ville est alors aux mains des Anglais."),
  Q("Quel évêque préside le procès de Jeanne d'Arc ?", ["Pierre Cauchon", "Thomas Becket", "Suger", "Remi"], "Pierre Cauchon", "Il est allié aux Anglais."),
  N("En quelle année un nouveau procès réhabilite-t-il Jeanne d'Arc ?", 1456, "Elle est canonisée en 1920."),
]),
notion('H5-2', 2, D, 'hg5d-louis-xi', [
  Q("Quel roi de France affronte le duc de Bourgogne Charles le Téméraire ?", ["Louis XI", "Charles VIII", "Louis XII", "Philippe le Bel"], "Louis XI", "Il préfère la ruse et la diplomatie à la guerre."),
  Q("Où Charles le Téméraire est-il tué en 1477 ?", ["Devant Nancy", "À Dijon", "À Paris", "À Bruges"], "Devant Nancy", "Sa mort permet à Louis XI de récupérer la Bourgogne."),
  Q("Quel surnom les adversaires de Louis XI lui donnent-ils, en raison de ses intrigues ?", ["« L'universelle aragne » (araignée)", "« Le Bien-Aimé »", "« Le Lion »", "« Le Hutin »"], "« L'universelle aragne » (araignée)", "Il tisse sa toile de diplomatie."),
]),
notion('H5-2', 0, D, 'hg5d-servage', [
  Q("Comment appelle-t-on l'acte par lequel un seigneur rend un serf libre ?", ["L'affranchissement", "L'adoubement", "L'hommage", "L'excommunication"], "L'affranchissement", "Il se multiplie à partir du XIIe siècle, souvent contre paiement."),
  Q("Comment appelle-t-on le droit qui empêche un serf de transmettre librement ses biens à ses enfants ?", ["La mainmorte", "La gabelle", "La dîme", "Le droit d'aînesse"], "La mainmorte", "Le seigneur prélève une part de l'héritage."),
  Q("Comment appelle-t-on la taxe que paie un serf pour épouser une personne d'une autre seigneurie ?", ["Le formariage", "Le chevage", "Le cens", "Le péage"], "Le formariage", "Le chevage est une petite taxe annuelle par tête."),
]),
notion('H5-2', 0, D, 'hg5d-seigneurie-banale', [
  Q("Comment appelle-t-on le pouvoir du seigneur de commander, juger et punir les habitants de sa seigneurie ?", ["Le ban", "Le fief", "La dîme", "Le cens"], "Le ban", "On parle de seigneurie banale."),
  Q("Qu'est-ce que la seigneurie foncière ?", ["L'ensemble des terres du seigneur, exploitées directement ou confiées à des tenanciers", "Le droit de lever une armée", "Le droit de battre monnaie", "Le pouvoir religieux de l'évêque"], "L'ensemble des terres du seigneur, exploitées directement ou confiées à des tenanciers", "La réserve est exploitée grâce aux corvées."),
  Q("Comment appelle-t-on la redevance annuelle payée par un paysan pour la terre qu'il exploite ?", ["Le cens", "La taille royale", "La gabelle", "Le formariage"], "Le cens", "Il est souvent payé en argent ou en nature."),
]),
notion('H5-2', 1, D, 'hg5d-gothique-technique', [
  Q("Quel élément d'architecture permet aux bâtisseurs gothiques de répartir le poids des voûtes ?", ["La croisée d'ogives", "La voûte en berceau", "Le linteau", "La coupole"], "La croisée d'ogives", "Elle permet des murs plus minces et de grandes baies."),
  Q("Comment appelle-t-on les arcs extérieurs qui soutiennent les murs d'une cathédrale gothique ?", ["Les arcs-boutants", "Les arcs en plein cintre", "Les contreforts romans", "Les colonnes doriques"], "Les arcs-boutants", "Ils permettent d'élever les murs très haut."),
  Q("Quel abbé fait reconstruire l'abbatiale de Saint-Denis au XIIe siècle, souvent considérée comme le premier édifice gothique ?", ["Suger", "Bernard de Clairvaux", "Pierre Cauchon", "Alcuin"], "Suger", "Il veut une église baignée de lumière."),
]),
notion('H5-2', 1, D, 'hg5d-ordres-mendiants', [
  Q("Quel saint italien fonde au début du XIIIe siècle un ordre fondé sur la pauvreté absolue ?", ["Saint François d'Assise", "Saint Benoît", "Saint Bernard", "Saint Louis"], "Saint François d'Assise", "Ses frères sont appelés franciscains."),
  Q("Quel ordre est fondé par saint Dominique pour prêcher contre l'hérésie ?", ["Les dominicains (frères prêcheurs)", "Les cisterciens", "Les templiers", "Les bénédictins"], "Les dominicains (frères prêcheurs)", "Ils jouent un grand rôle dans les universités."),
  Q("Pourquoi les ordres mendiants s'installent-ils surtout dans les villes ?", ["Pour prêcher auprès des citadins et vivre de leurs aumônes", "Pour fuir les campagnes trop pauvres", "Pour y construire des châteaux", "Pour y fonder des banques"], "Pour prêcher auprès des citadins et vivre de leurs aumônes", "Ils accompagnent l'essor urbain."),
]),
notion('H5-2', 2, D, 'hg5d-monnaie-royale', [
  Q("Quelle pièce d'argent Saint Louis fait-il frapper en 1266 ?", ["Le gros tournois", "Le dinar", "Le florin", "Le franc"], "Le gros tournois", "Il circule dans toute l'Europe."),
  Q("Pourquoi le roi impose-t-il sa monnaie dans tout le royaume ?", ["Pour affirmer son autorité et faciliter les échanges", "Pour remplacer toutes les monnaies étrangères du monde", "Pour supprimer l'impôt", "Pour payer le pape"], "Pour affirmer son autorité et faciliter les échanges", "Battre monnaie est un droit souverain."),
  Q("Quelle pièce d'or, frappée par Jean le Bon en 1360 pour payer sa rançon, porte le nom de « franc » ?", ["Le franc à cheval", "Le louis d'or", "L'écu de Saint Louis", "Le ducat"], "Le franc à cheval", "Le mot « franc » signifie ici « libre », comme le roi libéré."),
]),
notion('H5-2', 1, D, 'hg5d-gouvernement-urbain', [
  Q("Comment appelle-t-on les magistrats qui gouvernent de nombreuses villes du Midi au Moyen Âge ?", ["Les consuls", "Les échevins", "Les baillis", "Les sénéchaux"], "Les consuls", "Le terme vient de la Rome antique."),
  Q("Comment appelle-t-on les magistrats municipaux des villes du nord de la France ?", ["Les échevins", "Les consuls", "Les tribuns", "Les vizirs"], "Les échevins", "Ils sont souvent dirigés par un maire."),
  Q("Que gagne une ville qui obtient une charte de franchise ?", ["Des libertés : s'administrer, rendre la justice, lever des taxes", "Le droit de battre monnaie royale", "L'indépendance totale vis-à-vis du roi", "Le droit d'élire le pape"], "Des libertés : s'administrer, rendre la justice, lever des taxes", "Ces libertés sont souvent achetées au seigneur."),
]),
notion('H5-2', 1, D, 'hg5d-peste-consequences', [
  Q("Quelle communauté est injustement accusée de répandre la peste et victime de massacres en 1348-1349 ?", ["Les juifs", "Les moines", "Les marchands italiens", "Les chevaliers"], "Les juifs", "Ces violences frappent de nombreuses villes d'Europe."),
  Q("Comment appelle-t-on les groupes de fidèles qui se fouettent en public pour expier les péchés pendant la peste ?", ["Les flagellants", "Les pénitents blancs", "Les cathares", "Les franciscains"], "Les flagellants", "L'Église finit par les condamner."),
  Q("Quelle conséquence économique la peste a-t-elle dans les campagnes ?", ["La main-d'œuvre manque, ce qui pousse les salaires à la hausse", "Les salaires baissent fortement", "Les terres deviennent plus chères", "Rien ne change"], "La main-d'œuvre manque, ce qui pousse les salaires à la hausse", "Les autorités tentent de bloquer les salaires."),
]),
notion('H5-2', 0, D, 'hg5d-sources-medievales', [
  Q("Comment appelle-t-on l'inventaire des terres, des tenanciers et des redevances d'un grand domaine ?", ["Un polyptyque", "Un cartulaire", "Une chronique", "Un psautier"], "Un polyptyque", "Celui de l'abbaye de Saint-Germain-des-Prés, au IXe siècle, est célèbre."),
  Q("Comment appelle-t-on le recueil des copies de chartes conservées par une abbaye ou une seigneurie ?", ["Un cartulaire", "Un polyptyque", "Un missel", "Un bestiaire"], "Un cartulaire", "Il permet de retrouver droits et possessions."),
  Q("Quel recueil, rédigé à l'abbaye de Saint-Denis, raconte l'histoire des rois de France ?", ["Les Grandes Chroniques de France", "La Chanson de Roland", "Le Roman de Renart", "La Légende dorée"], "Les Grandes Chroniques de France", "C'est une histoire officielle de la monarchie."),
]),
notion('H5-2', 2, D, 'hg5d-sacre-royal', [
  Q("Dans quelle cathédrale sont sacrés la plupart des rois de France ?", ["Reims", "Notre-Dame de Paris", "Saint-Denis", "Chartres"], "Reims", "En souvenir du baptême de Clovis."),
  Q("Comment appelle-t-on la fiole contenant l'huile du sacre, selon la tradition apportée par une colombe ?", ["La Sainte Ampoule", "Le Saint Graal", "Le ciboire", "La couronne d'épines"], "La Sainte Ampoule", "Elle renforce le caractère sacré du roi."),
  Q("Quel pouvoir de guérison attribue-t-on au roi sacré ?", ["Guérir les écrouelles en touchant les malades", "Guérir la peste", "Rendre la vue aux aveugles", "Ressusciter les morts"], "Guérir les écrouelles en touchant les malades", "« Le roi te touche, Dieu te guérit »."),
]),
notion('H5-2', 0, D, 'hg5d-vassalite-roi', [
  Q("Quel grand vassal du roi de France est aussi roi d'Angleterre à partir de 1154 ?", ["Henri II Plantagenêt", "Guillaume le Conquérant", "Richard III", "Henri V"], "Henri II Plantagenêt", "Il possède plus de terres en France que le roi lui-même."),
  Q("Quelle duchesse apporte l'Aquitaine aux Plantagenêts par son mariage de 1152 ?", ["Aliénor d'Aquitaine", "Blanche de Castille", "Isabeau de Bavière", "Anne de Bretagne"], "Aliénor d'Aquitaine", "Elle avait d'abord épousé le roi de France Louis VII."),
  Q("Pourquoi la situation des Plantagenêts menace-t-elle le roi capétien ?", ["Son vassal est plus puissant que lui", "Ils sont alliés du pape contre lui", "Ils refusent le christianisme", "Ils contrôlent Paris"], "Son vassal est plus puissant que lui", "Philippe Auguste reprendra une grande partie de ces terres."),
]),
]
