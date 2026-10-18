# Histoire 5e · Chrétientés et islam (VIe-XIIIe siècles), des mondes en contact : au moins 50 questions par niveau
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Facile ══
notion('H5-1', 0, F, 'hg5-clovis', [
  Q("Quel roi des Francs se fait baptiser à Reims vers 500 ?", ["Clovis", "Charlemagne", "Hugues Capet", "Pépin le Bref"], "Clovis", "Son baptême rapproche les Francs de l'Église de Rome."),
  Q("À quelle dynastie appartient Clovis ?", ["Les Mérovingiens", "Les Carolingiens", "Les Capétiens", "Les Valois"], "Les Mérovingiens", "Les Carolingiens leur succèdent au VIIIe siècle."),
  Q("Quel évêque baptise Clovis ?", ["Remi, évêque de Reims", "Le pape Léon III", "Saint Martin", "Saint Louis"], "Remi, évêque de Reims", "Le baptême de Clovis fait de Reims une ville symbolique de la monarchie."),
]),
notion('H5-1', 0, F, 'hg5-aix-la-chapelle', [
  Q("Quelle ville Charlemagne choisit-il pour installer son palais principal ?", ["Aix-la-Chapelle", "Paris", "Rome", "Reims"], "Aix-la-Chapelle", "Il y réside souvent à la fin de son règne."),
  Q("Dans quel pays actuel se trouve Aix-la-Chapelle ?", ["L'Allemagne", "La France", "L'Italie", "La Belgique"], "L'Allemagne", "Elle s'appelle Aachen en allemand."),
  Q("Comment appelle-t-on la chapelle construite par Charlemagne dans son palais d'Aix ?", ["La chapelle palatine", "La Sainte-Chapelle", "La chapelle Sixtine", "La basilique Saint-Pierre"], "La chapelle palatine", "« Palatine » signifie « du palais »."),
]),
notion('H5-1', 0, F, 'hg5-missi-dominici', [
  Q("Comment s'appellent les envoyés de Charlemagne qui contrôlent les comtes dans l'empire ?", ["Les missi dominici", "Les chevaliers", "Les moines", "Les baillis"], "Les missi dominici", "Ils voyagent par deux : un laïc et un religieux."),
  Q("Qui administre une région (un comté) au nom de Charlemagne ?", ["Un comte", "Un calife", "Un pape", "Un sultan"], "Un comte", "L'empire compte plusieurs centaines de comtés."),
  Q("Pourquoi Charlemagne envoie-t-il des missi dominici dans son empire ?", ["Pour vérifier que ses ordres sont appliqués", "Pour faire du commerce", "Pour construire des routes", "Pour lever des armées étrangères"], "Pour vérifier que ses ordres sont appliqués", "L'empire est immense et difficile à contrôler."),
]),
notion('H5-1', 0, F, 'hg5-renaissance-carolingienne', [
  Q("Comment appelle-t-on le renouveau des écoles et des savoirs sous Charlemagne ?", ["La renaissance carolingienne", "La Renaissance italienne", "Les Lumières", "L'humanisme"], "La renaissance carolingienne", "Charlemagne veut des clercs mieux formés."),
  Q("Où les moines recopient-ils les manuscrits au Moyen Âge ?", ["Dans le scriptorium du monastère", "Dans une imprimerie", "Dans un château fort", "Dans une mosquée"], "Dans le scriptorium du monastère", "L'imprimerie n'apparaît en Europe qu'au XVe siècle."),
  Q("Comment appelle-t-on l'écriture claire mise au point à l'époque de Charlemagne, ancêtre de nos lettres minuscules ?", ["La minuscule caroline", "L'écriture cunéiforme", "Les hiéroglyphes", "L'alphabet cyrillique"], "La minuscule caroline", "Elle rend les textes plus lisibles."),
]),
notion('H5-1', 1, F, 'hg5-mahomet', [
  Q("Comment appelle-t-on Mahomet dans l'islam ?", ["Le Prophète", "Le calife", "Le pape", "Le sultan"], "Le Prophète", "Pour les musulmans, il reçoit la révélation de Dieu (Allah)."),
  Q("Dans quelle ville naît Mahomet, vers 570 ?", ["La Mecque", "Bagdad", "Jérusalem", "Damas"], "La Mecque", "C'est la première ville sainte de l'islam."),
  Q("Vers quelle ville Mahomet part-il en 622 (l'Hégire) ?", ["Médine", "Le Caire", "Cordoue", "Constantinople"], "Médine", "Médine est la deuxième ville sainte de l'islam."),
]),
notion('H5-1', 1, F, 'hg5-piliers-islam', [
  Q("Combien de piliers (obligations principales) compte l'islam ?", ["Cinq", "Trois", "Sept", "Dix"], "Cinq", "La profession de foi, la prière, l'aumône, le jeûne du ramadan et le pèlerinage."),
  Q("Comment appelle-t-on le mois de jeûne des musulmans ?", ["Le ramadan", "Le carême", "Le hajj", "L'Hégire"], "Le ramadan", "Le jeûne a lieu du lever au coucher du soleil."),
  Q("Vers quelle ville les musulmans font-ils le pèlerinage, au moins une fois dans leur vie s'ils le peuvent ?", ["La Mecque", "Jérusalem", "Rome", "Bagdad"], "La Mecque", "Ce pèlerinage s'appelle le hajj."),
]),
notion('H5-1', 1, F, 'hg5-mosquee', [
  Q("Comment appelle-t-on le lieu de prière des musulmans ?", ["La mosquée", "L'église", "La synagogue", "Le temple"], "La mosquée", "La prière du vendredi y rassemble les fidèles."),
  Q("Comment appelle-t-on la tour d'une mosquée ?", ["Le minaret", "Le clocher", "Le donjon", "Le beffroi"], "Le minaret", "C'est de là que l'on appelle à la prière."),
  Q("Comment appelle-t-on la personne qui appelle les fidèles à la prière ?", ["Le muezzin", "Le calife", "L'imam", "Le vizir"], "Le muezzin", "L'imam, lui, dirige la prière."),
]),
notion('H5-1', 1, F, 'hg5-jerusalem', [
  Q("Quelle ville est sacrée à la fois pour les juifs, les chrétiens et les musulmans ?", ["Jérusalem", "La Mecque", "Rome", "Constantinople"], "Jérusalem", "Elle est au cœur des croisades."),
  Q("Quel monument musulman à coupole dorée est construit à Jérusalem à la fin du VIIe siècle ?", ["Le Dôme du Rocher", "Sainte-Sophie", "La Grande Mosquée de Cordoue", "La Kaaba"], "Le Dôme du Rocher", "Il est achevé vers 691."),
  Q("Quel lieu chrétien de Jérusalem abrite, selon la tradition, le tombeau du Christ ?", ["Le Saint-Sépulcre", "Le Vatican", "Le mont Saint-Michel", "Saint-Jacques-de-Compostelle"], "Le Saint-Sépulcre", "Les croisés veulent le reprendre."),
]),
notion('H5-1', 0, F, 'hg5-art-byzantin', [
  Q("Comment appelle-t-on une image religieuse peinte sur bois dans le monde byzantin ?", ["Une icône", "Une fresque", "Un vitrail", "Une tapisserie"], "Une icône", "Les icônes sont au cœur de la piété orthodoxe."),
  Q("Avec quoi décore-t-on les murs et les coupoles des églises byzantines ?", ["Des mosaïques", "Des affiches", "Des tapis", "Des miroirs"], "Des mosaïques", "Elles sont faites de petits cubes de pierre ou de verre doré."),
  Q("Quelle ville d'Italie conserve les célèbres mosaïques de Justinien et de l'impératrice Théodora ?", ["Ravenne", "Venise", "Florence", "Milan"], "Ravenne", "Elles se trouvent dans la basilique Saint-Vital."),
]),
notion('H5-1', 1, F, 'hg5-poitiers-732', [
  Q("Quel chef franc arrête une armée arabe près de Poitiers en 732 ?", ["Charles Martel", "Charlemagne", "Clovis", "Roland"], "Charles Martel", "Il est le grand-père de Charlemagne."),
  N("En quelle année a lieu la bataille de Poitiers entre Charles Martel et une armée arabe ?", 732, "Cette victoire renforce le prestige de sa famille, les futurs Carolingiens."),
  Q("Quel lien de parenté unit Charles Martel et Charlemagne ?", ["Charles Martel est son grand-père", "Charles Martel est son fils", "Charles Martel est son frère", "Ils n'ont aucun lien"], "Charles Martel est son grand-père", "Pépin le Bref, fils de Charles Martel, est le père de Charlemagne."),
]),
notion('H5-1', 1, F, 'hg5-expansion-arabe', [
  Q("Comment appelle-t-on la partie de la péninsule Ibérique sous domination musulmane ?", ["Al-Andalus", "La Gaule", "Le Maghreb", "La Castille"], "Al-Andalus", "Le nom a donné celui de l'Andalousie."),
  N("En quelle année les troupes arabo-berbères entrent-elles dans la péninsule Ibérique ?", 711, "Elles franchissent le détroit de Gibraltar."),
  Q("Jusqu'où s'étend le monde musulman au milieu du VIIIe siècle ?", ["De l'Espagne jusqu'à l'Indus", "De la France jusqu'à la Chine", "De l'Égypte jusqu'à la Grèce seulement", "Uniquement en Arabie"], "De l'Espagne jusqu'à l'Indus", "L'expansion a été très rapide après la mort de Mahomet (632)."),
]),
notion('H5-1', 1, F, 'hg5-monotheismes', [
  Q("Comment appelle-t-on une religion qui croit en un seul Dieu ?", ["Une religion monothéiste", "Une religion polythéiste", "Une mythologie", "Une philosophie"], "Une religion monothéiste", "Le judaïsme, le christianisme et l'islam sont monothéistes."),
  Q("Quel est le livre sacré des chrétiens ?", ["La Bible", "Le Coran", "La Torah seule", "Les Védas"], "La Bible", "Elle réunit l'Ancien et le Nouveau Testament."),
  Q("Comment appelle-t-on les chrétiens de l'Empire byzantin après la séparation de 1054 ?", ["Les orthodoxes", "Les protestants", "Les catholiques", "Les cathares"], "Les orthodoxes", "Les chrétiens d'Occident sont appelés catholiques."),
]),
# ══ Intermédiaire ══
notion('H5-1', 0, I, 'hg5i-pepin-le-bref', [
  Q("Quel roi, père de Charlemagne, devient en 751 le premier roi carolingien ?", ["Pépin le Bref", "Charles Martel", "Louis le Pieux", "Childéric III"], "Pépin le Bref", "Il écarte le dernier roi mérovingien."),
  N("En quelle année Pépin le Bref devient-il roi des Francs ?", 751, "Il est ensuite sacré par le pape en 754."),
  Q("Quel geste religieux donne au roi carolingien un caractère sacré ?", ["Le sacre (onction d'huile sainte)", "Le couronnement par l'empereur byzantin", "L'élection par le peuple", "Le baptême d'un prince étranger"], "Le sacre (onction d'huile sainte)", "Le roi apparaît choisi par Dieu."),
]),
notion('H5-1', 0, I, 'hg5i-gouverner-empire', [
  Q("Comment appelle-t-on les textes de loi promulgués par Charlemagne ?", ["Les capitulaires", "Les décrets royaux", "Les chartes de franchise", "Les édits"], "Les capitulaires", "Ils sont divisés en chapitres (capitula)."),
  Q("Que doivent prêter tous les hommes libres à Charlemagne ?", ["Un serment de fidélité", "Un impôt sur le sel", "Un serment au pape", "Un service en mer"], "Un serment de fidélité", "Charlemagne s'appuie sur la fidélité personnelle."),
  Q("Pourquoi Charlemagne gouverne-t-il en se déplaçant souvent ?", ["Pour imposer sa présence dans un empire très vaste", "Parce qu'il n'a pas de palais", "Pour fuir les Vikings", "Pour visiter le pape chaque mois"], "Pour imposer sa présence dans un empire très vaste", "Il ne s'installe durablement à Aix qu'à la fin de son règne."),
]),
notion('H5-1', 0, I, 'hg5i-conquetes-charlemagne', [
  Q("Contre quel peuple païen de Germanie Charlemagne mène-t-il plus de trente ans de guerres ?", ["Les Saxons", "Les Lombards", "Les Vikings", "Les Mongols"], "Les Saxons", "Ils sont soumis et convertis de force."),
  Q("De quel royaume d'Italie Charlemagne devient-il roi en 774 ?", ["Le royaume des Lombards", "Le royaume de Sicile", "Le royaume de Naples", "Le royaume d'Aragon"], "Le royaume des Lombards", "Il protège ainsi le pape."),
  Q("Quel épisode de 778, dans les Pyrénées, a inspiré la Chanson de Roland ?", ["La bataille de Roncevaux", "La bataille de Poitiers", "Le traité de Verdun", "Le sacre de Charlemagne"], "La bataille de Roncevaux", "L'arrière-garde de Charlemagne y est massacrée."),
]),
notion('H5-1', 1, I, 'hg5i-omeyyades-abbassides', [
  Q("Quelle dynastie de califes a pour capitale Damas jusqu'en 750 ?", ["Les Omeyyades", "Les Abbassides", "Les Fatimides", "Les Ottomans"], "Les Omeyyades", "Elle est renversée par les Abbassides en 750."),
  N("En quelle année le calife abbasside al-Mansur fonde-t-il Bagdad ?", 762, "Bagdad devient l'une des plus grandes villes du monde."),
  Q("Où un prince omeyyade survivant fonde-t-il un émirat indépendant en 756 ?", ["À Cordoue, en al-Andalus", "À Damas", "Au Caire", "À Médine"], "À Cordoue, en al-Andalus", "L'émirat devient un califat en 929."),
]),
notion('H5-1', 1, I, 'hg5i-maison-sagesse', [
  Q("Comment s'appelle le grand centre de savoir et de traduction de Bagdad au IXe siècle ?", ["La Maison de la sagesse", "La Sorbonne", "L'Académie de Platon", "La bibliothèque d'Alexandrie"], "La Maison de la sagesse", "On y traduit en arabe des œuvres grecques."),
  Q("De quelle langue les savants de Bagdad traduisent-ils surtout les œuvres d'Aristote et de Ptolémée ?", ["Du grec", "Du latin", "Du chinois", "Du français"], "Du grec", "Ces traductions transmettront plus tard ces savoirs à l'Occident."),
  Q("Quel support d'écriture, venu de Chine, se diffuse dans le monde musulman à partir du VIIIe siècle ?", ["Le papier", "Le parchemin", "Le papyrus", "La tablette d'argile"], "Le papier", "Des fabriques de papier existent à Bagdad vers 800."),
]),
notion('H5-1', 1, I, 'hg5i-commerce-monde-musulman', [
  Q("Comment appelle-t-on la pièce d'or du monde musulman médiéval ?", ["Le dinar", "Le denier", "Le florin", "Le ducat"], "Le dinar", "Le dirham est la pièce d'argent."),
  Q("Comment appelle-t-on un convoi de marchands et de chameaux traversant le désert ?", ["Une caravane", "Une flotte", "Une croisade", "Une ambassade"], "Une caravane", "Les caravanes relient l'Afrique, l'Arabie et l'Asie."),
  Q("Comment appelle-t-on le marché d'une ville du monde musulman ?", ["Le souk", "La foire", "Le forum", "Le bazar de Venise"], "Le souk", "On y trouve épices, tissus et métaux précieux."),
]),
notion('H5-1', 1, I, 'hg5i-sunnites-chiites', [
  Q("Comment appelle-t-on les musulmans qui considèrent qu'Ali, gendre de Mahomet, aurait dû lui succéder ?", ["Les chiites", "Les sunnites", "Les soufis", "Les Omeyyades"], "Les chiites", "« Chiite » vient de « parti d'Ali »."),
  Q("Comment appelle-t-on les musulmans majoritaires, qui suivent la tradition (sunna) du Prophète ?", ["Les sunnites", "Les chiites", "Les orthodoxes", "Les Mamelouks"], "Les sunnites", "Ils représentent la grande majorité des musulmans."),
  Q("Quelle question est à l'origine de la division entre sunnites et chiites ?", ["La succession de Mahomet à la tête de la communauté", "Le choix de la langue du Coran", "La date du ramadan", "La conquête de l'Espagne"], "La succession de Mahomet à la tête de la communauté", "Cette division apparaît dès le VIIe siècle."),
]),
notion('H5-1', 1, I, 'hg5i-coran', [
  Q("En quelle langue le Coran est-il écrit ?", ["En arabe", "En grec", "En latin", "En hébreu"], "En arabe", "L'arabe devient la langue du savoir dans le monde musulman."),
  Q("Comment s'appellent les chapitres du Coran ?", ["Les sourates", "Les versets bibliques", "Les psaumes", "Les capitulaires"], "Les sourates", "Le Coran compte 114 sourates."),
  Q("Comment appelle-t-on les paroles et actes attribués au Prophète, qui complètent le Coran ?", ["Les hadiths", "Les fatwas", "Les icônes", "Les minarets"], "Les hadiths", "Ils forment la sunna, la tradition."),
]),
notion('H5-1', 0, I, 'hg5i-byzance-rome', [
  Q("De quel empire l'Empire byzantin est-il l'héritier ?", ["De l'Empire romain d'Orient", "De l'Empire perse", "De l'Empire carolingien", "De l'Empire mongol"], "De l'Empire romain d'Orient", "Les Byzantins se nomment eux-mêmes « Romains »."),
  Q("Quelle langue est la plus parlée dans l'Empire byzantin ?", ["Le grec", "Le latin", "L'arabe", "Le francique"], "Le grec", "Le latin recule après le VIe siècle."),
  Q("Quel empereur romain fonde Constantinople en 330 ?", ["Constantin", "Justinien", "Auguste", "Néron"], "Constantin", "La ville porte son nom."),
]),
notion('H5-1', 1, I, 'hg5i-croisades-acteurs', [
  Q("Quel sultan reprend Jérusalem aux croisés en 1187 ?", ["Saladin", "Haroun al-Rachid", "Soliman le Magnifique", "Mehmed II"], "Saladin", "Sa victoire provoque la troisième croisade."),
  Q("Quel roi d'Angleterre participe à la troisième croisade ?", ["Richard Cœur de Lion", "Henri VIII", "Guillaume le Conquérant", "Édouard III"], "Richard Cœur de Lion", "Il affronte Saladin sans reprendre Jérusalem."),
  Q("Quel roi de France meurt devant Tunis en 1270, lors de la dernière grande croisade ?", ["Saint Louis (Louis IX)", "Philippe Auguste", "Charles VII", "Louis XIV"], "Saint Louis (Louis IX)", "Il est canonisé en 1297."),
]),
notion('H5-1', 1, I, 'hg5i-ordres-militaires', [
  Q("Comment appelle-t-on les ordres de moines-soldats créés pour défendre les États latins d'Orient ?", ["Les ordres militaires", "Les ordres mendiants", "Les corporations", "Les universités"], "Les ordres militaires", "Les Templiers et les Hospitaliers en sont les plus connus."),
  Q("Quel ordre militaire, fondé à Jérusalem, est supprimé par le pape en 1312 sous la pression du roi Philippe le Bel ?", ["Les Templiers", "Les Hospitaliers", "Les Chevaliers teutoniques", "Les Franciscains"], "Les Templiers", "Le roi convoitait leurs richesses."),
  Q("Quelle forteresse de Syrie, tenue par les Hospitaliers, est l'un des plus célèbres châteaux des croisés ?", ["Le krak des Chevaliers", "Le château de Versailles", "La tour de Londres", "Carcassonne"], "Le krak des Chevaliers", "Il est inscrit au patrimoine mondial."),
]),
notion('H5-1', 1, I, 'hg5i-venise-genes', [
  Q("Quelles cités italiennes dominent le commerce entre l'Occident et l'Orient au Moyen Âge ?", ["Venise et Gênes", "Rome et Naples", "Paris et Londres", "Milan et Turin"], "Venise et Gênes", "Leurs flottes rapportent épices et soieries."),
  Q("Comment appelle-t-on un établissement de marchands installé dans une ville étrangère ?", ["Un comptoir", "Un monastère", "Un fief", "Un califat"], "Un comptoir", "Venise possède des comptoirs à Constantinople et en Méditerranée orientale."),
  Q("Quels produits précieux venus d'Orient sont très recherchés en Occident ?", ["Les épices et la soie", "Le blé et le bois", "Le charbon et le fer", "Le vin et le fromage"], "Les épices et la soie", "Le poivre vaut alors très cher."),
]),
notion('H5-1', 1, I, 'hg5i-cordoue-tolede', [
  Q("Quel monument de Cordoue, agrandi pendant deux siècles, est célèbre pour sa forêt de colonnes et d'arcs bicolores ?", ["La Grande Mosquée de Cordoue", "Sainte-Sophie", "Le Dôme du Rocher", "L'Alhambra"], "La Grande Mosquée de Cordoue", "Elle est transformée en cathédrale après la reconquête de 1236."),
  Q("Quelle ville d'Espagne devient au XIIe siècle un grand centre de traduction de l'arabe vers le latin ?", ["Tolède", "Madrid", "Barcelone", "Saint-Jacques-de-Compostelle"], "Tolède", "Chrétiens, juifs et musulmans y collaborent."),
  Q("Quel philosophe né à Cordoue au XIIe siècle a commenté Aristote ?", ["Averroès (Ibn Rushd)", "Avicenne", "Thomas d'Aquin", "Érasme"], "Averroès (Ibn Rushd)", "Ses commentaires sont très lus dans les universités d'Occident."),
]),
# ══ Avancé ══
notion('H5-1', 0, D, 'hg5d-justinien-reconquete', [
  Q("Quel général de Justinien reconquiert l'Afrique du Nord et l'Italie au VIe siècle ?", ["Bélisaire", "Charles Martel", "Saladin", "Constantin"], "Bélisaire", "Justinien rêve de restaurer l'Empire romain."),
  Q("Quelle révolte éclate à Constantinople en 532 et manque de renverser Justinien ?", ["La sédition Nika", "La Jacquerie", "La révolte des Ciompi", "La Fronde"], "La sédition Nika", "L'impératrice Théodora aurait convaincu Justinien de ne pas fuir."),
  Q("Quelle impératrice, épouse de Justinien, joue un grand rôle politique ?", ["Théodora", "Irène", "Aliénor", "Blanche de Castille"], "Théodora", "Elle figure sur les mosaïques de Ravenne."),
]),
notion('H5-1', 0, D, 'hg5d-saint-empire', [
  Q("Quel roi de Germanie est couronné empereur à Rome en 962 ?", ["Otton Ier", "Charles le Chauve", "Hugues Capet", "Frédéric Barberousse"], "Otton Ier", "Il restaure le titre impérial en Occident."),
  Q("Comment appelle-t-on l'empire fondé par Otton Ier ?", ["Le Saint-Empire romain germanique", "L'Empire byzantin", "L'Empire carolingien", "L'Empire latin de Constantinople"], "Le Saint-Empire romain germanique", "Il dure jusqu'en 1806."),
  Q("De quel royaume issu du partage de Verdun le Saint-Empire est-il en grande partie l'héritier ?", ["La Francie orientale", "La Francie occidentale", "Le royaume d'Aquitaine", "Le royaume de Bourgogne"], "La Francie orientale", "Elle revient à Louis le Germanique en 843."),
]),
notion('H5-1', 0, D, 'hg5d-serments-strasbourg', [
  N("En quelle année sont prononcés les Serments de Strasbourg ?", 842, "Ils précèdent d'un an le traité de Verdun."),
  Q("Quels petits-fils de Charlemagne s'allient par les Serments de Strasbourg contre leur frère Lothaire ?", ["Charles le Chauve et Louis le Germanique", "Pépin et Carloman", "Hugues Capet et Robert le Pieux", "Clovis et Childéric"], "Charles le Chauve et Louis le Germanique", "Ils se partagent ensuite l'empire avec Lothaire."),
  Q("Pourquoi les Serments de Strasbourg sont-ils célèbres pour l'histoire de la langue ?", ["C'est l'un des premiers textes écrits en langue romane, ancêtre du français", "C'est le premier texte écrit en latin", "C'est le premier livre imprimé", "C'est la première traduction du Coran"], "C'est l'un des premiers textes écrits en langue romane, ancêtre du français", "Ils sont aussi rédigés en langue germanique."),
]),
notion('H5-1', 1, D, 'hg5d-pouvoir-calife', [
  Q("Quel titre du calife signifie « commandeur des croyants » ?", ["Amir al-mu'minin", "Basileus", "Imperator", "Sultan"], "Amir al-mu'minin", "Le calife réunit pouvoir politique et autorité religieuse."),
  Q("Comment appelle-t-on le principal ministre du calife abbasside ?", ["Le vizir", "L'émir", "Le cadi", "Le muezzin"], "Le vizir", "Il dirige l'administration de l'empire."),
  Q("Comment appelle-t-on le gouverneur d'une province ou un chef militaire dans le monde musulman ?", ["Un émir", "Un vizir", "Un calife", "Un imam"], "Un émir", "Certains émirs deviennent presque indépendants."),
]),
notion('H5-1', 1, D, 'hg5d-dhimmis', [
  Q("Quel statut ont les juifs et les chrétiens vivant en terre d'islam au Moyen Âge ?", ["Ils sont « protégés » (dhimmis) en échange d'un impôt", "Ils sont tous réduits en esclavage", "Ils ont exactement les mêmes droits que les musulmans", "Ils sont expulsés"], "Ils sont « protégés » (dhimmis) en échange d'un impôt", "Ils peuvent pratiquer leur religion, avec des restrictions."),
  Q("Comment s'appelle l'impôt spécifique payé par les dhimmis ?", ["La jizya", "La dîme", "La taille", "La gabelle"], "La jizya", "C'est un impôt par tête."),
  Q("Pourquoi parle-t-on de « coexistence » entre religions dans certaines villes comme Cordoue ou Bagdad ?", ["Des communautés de religions différentes y vivent et travaillent ensemble, sans égalité complète", "Toutes les religions y sont interdites", "Une seule religion y est tolérée", "Les habitants changent de religion chaque année"], "Des communautés de religions différentes y vivent et travaillent ensemble, sans égalité complète", "Cette coexistence n'exclut pas les tensions."),
]),
notion('H5-1', 1, D, 'hg5d-savants-arabes', [
  Q("Quel savant de Bagdad, au IXe siècle, a donné son nom au mot « algorithme » ?", ["Al-Khwarizmi", "Avicenne", "Averroès", "Ibn Battuta"], "Al-Khwarizmi", "Son traité est aussi à l'origine du mot « algèbre »."),
  Q("Quel savant arabe du XIe siècle, né à Bassora, est un pionnier de l'optique ?", ["Ibn al-Haytham (Alhazen)", "Saladin", "Haroun al-Rachid", "Al-Idrisi"], "Ibn al-Haytham (Alhazen)", "Il étudie la lumière et la vision par l'expérience."),
  Q("D'où viennent les chiffres dits « arabes » transmis à l'Europe ?", ["De l'Inde, par l'intermédiaire des savants arabes", "De la Grèce antique", "De Rome", "Des Vikings"], "De l'Inde, par l'intermédiaire des savants arabes", "Ils incluent le zéro."),
]),
notion('H5-1', 0, D, 'hg5d-seldjoukides', [
  Q("Quel peuple turc musulman bat l'armée byzantine à Manzikert en 1071 ?", ["Les Turcs seldjoukides", "Les Mongols", "Les Ottomans", "Les Arabes omeyyades"], "Les Turcs seldjoukides", "Ils s'emparent ensuite d'une grande partie de l'Anatolie."),
  N("En quelle année l'armée byzantine est-elle vaincue à Manzikert ?", 1071, "Cette défaite affaiblit durablement Byzance."),
  Q("Quelle conséquence la menace turque a-t-elle sur les relations entre Byzance et l'Occident ?", ["L'empereur byzantin demande l'aide de l'Occident, ce qui contribue à la première croisade", "Byzance se convertit à l'islam", "Byzance devient vassale de la France", "Les relations sont totalement rompues"], "L'empereur byzantin demande l'aide de l'Occident, ce qui contribue à la première croisade", "Le pape Urbain II lance l'appel en 1095."),
]),
notion('H5-1', 1, D, 'hg5d-premiere-croisade', [
  N("En quelle année les croisés prennent-ils Jérusalem ?", 1099, "La prise de la ville s'accompagne de massacres."),
  Q("Quel seigneur, chef de la première croisade, prend le titre d'« avoué du Saint-Sépulcre » ?", ["Godefroy de Bouillon", "Richard Cœur de Lion", "Saint Louis", "Bohémond"], "Godefroy de Bouillon", "Il refuse le titre de roi."),
  Q("Quel État est fondé par les croisés en 1099 ?", ["Le royaume latin de Jérusalem", "Le califat de Cordoue", "Le Saint-Empire", "Le royaume de Sicile"], "Le royaume latin de Jérusalem", "Il disparaît en 1291 avec la chute d'Acre."),
]),
notion('H5-1', 1, D, 'hg5d-mongols-mamelouks', [
  Q("Quel petit-fils de Gengis Khan dirige la prise de Bagdad en 1258 ?", ["Hulagu", "Kubilai", "Tamerlan", "Attila"], "Hulagu", "Le dernier calife abbasside de Bagdad est exécuté."),
  Q("Quelle armée arrête les Mongols à la bataille d'Aïn Djalout, en 1260 ?", ["L'armée des Mamelouks d'Égypte", "L'armée byzantine", "Les croisés", "Les Seldjoukides"], "L'armée des Mamelouks d'Égypte", "Cette victoire protège l'Égypte."),
  Q("Quel chef unifie les tribus mongoles et fonde leur empire au début du XIIIe siècle ?", ["Gengis Khan", "Saladin", "Charlemagne", "Soliman"], "Gengis Khan", "L'Empire mongol devient le plus vaste empire continental de l'histoire."),
]),
notion('H5-1', 1, D, 'hg5d-reconquista', [
  Q("Comment appelle-t-on la reconquête progressive de la péninsule Ibérique par les royaumes chrétiens ?", ["La Reconquista", "La croisade des Albigeois", "La Contre-Réforme", "La Renaissance"], "La Reconquista", "Elle s'achève avec la prise de Grenade en 1492."),
  N("En quelle année le roi de Castille reprend-il Tolède ?", 1085, "Tolède devient ensuite un grand centre de traduction."),
  Q("Quelle bataille de 1212 marque un tournant décisif de la Reconquista ?", ["Las Navas de Tolosa", "Hastings", "Bouvines", "Poitiers"], "Las Navas de Tolosa", "Les royaumes chrétiens y battent les Almohades."),
]),
notion('H5-1', 1, D, 'hg5d-sicile', [
  Q("Quel peuple venu de Normandie conquiert la Sicile musulmane au XIe siècle ?", ["Les Normands", "Les Vikings danois", "Les Francs", "Les Byzantins"], "Les Normands", "La conquête est achevée en 1091."),
  Q("Quelle ville, capitale du roi Roger II, mêle arts byzantin, arabe et latin ?", ["Palerme", "Naples", "Venise", "Rome"], "Palerme", "La chapelle palatine de Palerme en est un exemple."),
  Q("Quel géographe arabe réalise une grande carte du monde pour le roi Roger II de Sicile ?", ["Al-Idrisi", "Ibn Battuta", "Al-Khwarizmi", "Averroès"], "Al-Idrisi", "Son ouvrage est achevé vers 1154."),
]),
notion('H5-1', 0, D, 'hg5d-cyrille-methode', [
  Q("Quels frères byzantins évangélisent les Slaves au IXe siècle ?", ["Cyrille et Méthode", "Pierre et Paul", "Romulus et Rémus", "Benoît et Bernard"], "Cyrille et Méthode", "Ils créent un alphabet pour écrire la langue slave."),
  Q("Quel alphabet, utilisé aujourd'hui en Russie, tient son nom de saint Cyrille ?", ["L'alphabet cyrillique", "L'alphabet latin", "L'alphabet grec", "L'alphabet arabe"], "L'alphabet cyrillique", "Il dérive de l'alphabet grec."),
  N("En quelle année le prince Vladimir de Kiev se convertit-il au christianisme orthodoxe ?", 988, "La Russie devient ainsi une terre orthodoxe."),
]),
notion('H5-1', 0, D, 'hg5d-quatrieme-croisade', [
  N("En quelle année les croisés de la quatrième croisade s'emparent-ils de Constantinople ?", 1204, "Ils pillent la ville chrétienne."),
  Q("Quelle cité italienne finance et oriente la quatrième croisade vers Constantinople ?", ["Venise", "Florence", "Gênes", "Milan"], "Venise", "Elle y gagne de nombreux comptoirs."),
  Q("Quel État les croisés fondent-ils à Constantinople en 1204 ?", ["L'Empire latin de Constantinople", "Le royaume de Jérusalem", "Le Saint-Empire", "Le califat de Bagdad"], "L'Empire latin de Constantinople", "Les Byzantins reprennent la ville en 1261."),
]),
notion('H5-1', 0, D, 'hg5d-charlemagne-haroun', [
  Q("Avec quel calife de Bagdad Charlemagne échange-t-il des ambassades ?", ["Haroun al-Rachid", "Saladin", "Al-Mansur", "Abd al-Rahman"], "Haroun al-Rachid", "Ils ont un adversaire commun : les Omeyyades d'Espagne."),
  Q("Quel animal exotique le calife offre-t-il à Charlemagne en 802 ?", ["Un éléphant", "Une girafe", "Un lion", "Un chameau"], "Un éléphant", "Il s'appelait Abul-Abbas."),
  Q("Que montrent ces ambassades entre l'empire carolingien et le califat abbasside ?", ["Des contacts diplomatiques entre la chrétienté et l'islam", "Une guerre permanente", "Une conversion de Charlemagne à l'islam", "Une fusion des deux empires"], "Des contacts diplomatiques entre la chrétienté et l'islam", "Les mondes sont en contact, pas seulement en conflit."),
]),
notion('H5-1', 0, D, 'hg5d-papaute-carolingiens', [
  Q("Quel pape vient en Gaule sacrer Pépin le Bref en 754 ?", ["Étienne II", "Léon III", "Urbain II", "Grégoire VII"], "Étienne II", "En échange, Pépin protège le pape contre les Lombards."),
  Q("Comment appelle-t-on les territoires donnés au pape par Pépin le Bref en 756 ?", ["Les États pontificaux", "Le Saint-Empire", "Les États latins d'Orient", "La Francie médiane"], "Les États pontificaux", "Le pape devient aussi un souverain temporel."),
  Q("Pourquoi l'alliance entre les Carolingiens et la papauté est-elle importante ?", ["Le pape légitime le pouvoir des Carolingiens, qui protègent le pape", "Le pape devient roi des Francs", "Les Carolingiens deviennent papes", "Elle n'a aucune conséquence"], "Le pape légitime le pouvoir des Carolingiens, qui protègent le pape", "Elle culmine avec le couronnement impérial de l'an 800."),
]),
notion('H5-1', 0, D, 'hg5d-sources-charlemagne', [
  Q("Quel lettré de la cour écrit une Vie de Charlemagne peu après sa mort ?", ["Éginhard", "Alcuin", "Grégoire de Tours", "Joinville"], "Éginhard", "C'est une source essentielle, mais à lire avec esprit critique."),
  Q("Comment appelle-t-on un manuscrit orné de peintures et de lettres décorées ?", ["Un manuscrit enluminé", "Un incunable", "Un palimpseste", "Une chronique"], "Un manuscrit enluminé", "Les enluminures sont des sources pour l'historien."),
  Q("Pourquoi l'historien doit-il lire avec prudence la Vie de Charlemagne écrite par un proche de l'empereur ?", ["Parce qu'elle cherche à glorifier l'empereur", "Parce qu'elle est écrite en arabe", "Parce qu'elle date du XXe siècle", "Parce qu'elle a été écrite par un ennemi"], "Parce qu'elle cherche à glorifier l'empereur", "Il faut confronter les sources."),
]),
]
