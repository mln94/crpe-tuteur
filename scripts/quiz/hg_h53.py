# Histoire 5e · Transformations de l'Europe et ouverture sur le monde aux XVIe et XVIIe siècles : au moins 50 questions par niveau
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Facile ══
notion('H5-3', 0, F, 'hg5-vasco-de-gama', [
  Q("Quel navigateur portugais atteint l'Inde par la mer en 1498 ?", ["Vasco de Gama", "Christophe Colomb", "Magellan", "Jacques Cartier"], "Vasco de Gama", "Il contourne l'Afrique."),
  Q("Quel cap au sud de l'Afrique Bartolomeu Dias franchit-il en 1488 ?", ["Le cap de Bonne-Espérance", "Le cap Horn", "Le cap Vert", "Le cap Nord"], "Le cap de Bonne-Espérance", "Il ouvre la route maritime vers l'océan Indien."),
  Q("Quel royaume ouvre la route maritime des épices par le sud de l'Afrique ?", ["Le Portugal", "La France", "L'Angleterre", "Venise"], "Le Portugal", "Lisbonne devient un grand port des épices."),
]),
notion('H5-3', 0, F, 'hg5-instruments-navigation', [
  Q("Quel navire léger et maniable utilisent les grands navigateurs du XVe siècle ?", ["La caravelle", "La galère", "Le drakkar", "Le paquebot"], "La caravelle", "Elle peut remonter contre le vent."),
  Q("Quel instrument indique le nord aux navigateurs ?", ["La boussole", "Le sablier", "Le sextant", "Le télescope"], "La boussole", "Elle vient de Chine."),
  Q("Quel instrument permet de mesurer la hauteur des astres pour connaître sa latitude ?", ["L'astrolabe", "La boussole", "Le baromètre", "L'horloge"], "L'astrolabe", "Il a été perfectionné par les savants arabes."),
]),
notion('H5-3', 1, F, 'hg5-gutenberg', [
  Q("Qui met au point l'imprimerie à caractères mobiles en Europe vers 1450 ?", ["Gutenberg", "Léonard de Vinci", "Galilée", "Luther"], "Gutenberg", "Il travaille à Mayence, en Allemagne."),
  Q("Quel est l'un des premiers grands livres imprimés par Gutenberg ?", ["La Bible", "Le Coran", "Les Essais de Montaigne", "L'Encyclopédie"], "La Bible", "Elle est imprimée vers 1455."),
  Q("Quelle conséquence a l'imprimerie sur les livres ?", ["Ils deviennent plus nombreux et moins chers", "Ils disparaissent", "Ils deviennent tous religieux", "Ils sont réservés au roi"], "Ils deviennent plus nombreux et moins chers", "Les idées circulent beaucoup plus vite."),
]),
notion('H5-3', 1, F, 'hg5-artistes-renaissance', [
  Q("Quel artiste peint le plafond de la chapelle Sixtine au Vatican ?", ["Michel-Ange", "Raphaël", "Botticelli", "Rembrandt"], "Michel-Ange", "Il est aussi l'auteur du David."),
  Q("Quelle ville italienne est considérée comme le berceau de la Renaissance ?", ["Florence", "Milan", "Naples", "Turin"], "Florence", "Brunelleschi, Botticelli ou Léonard y travaillent."),
  Q("Qui a peint La Joconde ?", ["Léonard de Vinci", "Michel-Ange", "Titien", "Raphaël"], "Léonard de Vinci", "Le tableau est conservé au Louvre."),
]),
notion('H5-3', 2, F, 'hg5-chateaux-loire', [
  Q("Quel château de la Loire François Ier fait-il construire à partir de 1519 ?", ["Chambord", "Versailles", "Vincennes", "Fontainebleau"], "Chambord", "Son escalier à double révolution est célèbre."),
  Q("Quel château de la Loire est construit en partie sur le Cher, comme un pont ?", ["Chenonceau", "Amboise", "Blois", "Chinon"], "Chenonceau", "On l'appelle aussi le « château des Dames »."),
  Q("Pourquoi les rois de la Renaissance aiment-ils séjourner dans la vallée de la Loire ?", ["Pour ses paysages, ses forêts de chasse et la proximité de leurs domaines", "Parce que Paris est interdite aux rois", "Pour être près de la mer", "Pour fuir l'Italie"], "Pour ses paysages, ses forêts de chasse et la proximité de leurs domaines", "Les rois y font construire de nombreux châteaux."),
]),
notion('H5-3', 1, F, 'hg5-mecenes', [
  Q("Comment appelle-t-on une personne riche qui protège et finance des artistes ?", ["Un mécène", "Un marchand", "Un prélat", "Un humaniste"], "Un mécène", "Les princes de la Renaissance sont souvent mécènes."),
  Q("Quelle famille de banquiers dirige Florence et protège les artistes à la Renaissance ?", ["Les Médicis", "Les Borgia", "Les Habsbourg", "Les Valois"], "Les Médicis", "Laurent le Magnifique en est la figure la plus célèbre."),
  Q("Pourquoi les princes font-ils travailler de grands artistes ?", ["Pour montrer leur puissance et leur prestige", "Pour payer moins d'impôts", "Pour plaire aux paysans", "Par obligation religieuse"], "Pour montrer leur puissance et leur prestige", "L'art est un instrument politique."),
]),
notion('H5-3', 1, F, 'hg5-guerres-religion', [
  Q("Comment appelle-t-on les protestants français au XVIe siècle ?", ["Les huguenots", "Les ligueurs", "Les jansénistes", "Les anglicans"], "Les huguenots", "Ils sont surtout calvinistes."),
  Q("Entre quelles années ont lieu les guerres de Religion en France ?", ["De 1562 à 1598", "De 1337 à 1453", "De 1618 à 1648", "De 1789 à 1799"], "De 1562 à 1598", "Elles prennent fin avec l'édit de Nantes."),
  Q("Quelle reine mère, épouse d'Henri II, joue un grand rôle pendant les guerres de Religion ?", ["Catherine de Médicis", "Marie-Antoinette", "Anne d'Autriche", "Aliénor d'Aquitaine"], "Catherine de Médicis", "Trois de ses fils deviennent rois."),
]),
notion('H5-3', 2, F, 'hg5-louis-xiv-regne', [
  Q("Quel surnom porte Louis XIV ?", ["Le Roi-Soleil", "Le Bien-Aimé", "Le Sage", "Le Juste"], "Le Roi-Soleil", "Le soleil est son emblème."),
  N("Combien d'années dure le règne de Louis XIV (1643-1715) ?", 72, "C'est le plus long règne de l'histoire de France."),
  Q("Comment appelle-t-on l'ensemble des règles qui organisent la vie de la cour autour du roi ?", ["L'étiquette", "La charte", "Le capitulaire", "La gabelle"], "L'étiquette", "Chaque geste du roi est réglé, du lever au coucher."),
]),
notion('H5-3', 2, F, 'hg5-colbert', [
  Q("Quel ministre de Louis XIV développe le commerce et l'industrie du royaume ?", ["Colbert", "Richelieu", "Mazarin", "Sully"], "Colbert", "Il est contrôleur général des finances à partir de 1665."),
  Q("Comment appelle-t-on les grands ateliers créés ou soutenus par Colbert ?", ["Les manufactures", "Les usines électriques", "Les corporations", "Les comptoirs"], "Les manufactures", "La manufacture des Gobelins produit des tapisseries."),
  Q("Quel est le but de la politique économique de Colbert ?", ["Vendre plus à l'étranger qu'on n'achète, pour enrichir le royaume", "Supprimer tous les impôts", "Interdire le commerce", "Acheter tout à l'étranger"], "Vendre plus à l'étranger qu'on n'achète, pour enrichir le royaume", "On parle de mercantilisme."),
]),
notion('H5-3', 0, F, 'hg5-empire-ottoman', [
  N("En quelle année les Ottomans prennent-ils Constantinople ?", 1453, "C'est la fin de l'Empire byzantin."),
  Q("Quel nom prend Constantinople après sa conquête par les Ottomans ?", ["Istanbul", "Ankara", "Smyrne", "Byzance"], "Istanbul", "Elle devient la capitale de l'Empire ottoman."),
  Q("Quel titre porte le souverain de l'Empire ottoman ?", ["Sultan", "Empereur", "Roi", "Doge"], "Sultan", "Soliman le Magnifique en est le plus célèbre."),
]),
notion('H5-3', 0, F, 'hg5-ameriques-conquete', [
  Q("Comment appelle-t-on les premiers habitants du continent américain ?", ["Les Amérindiens", "Les Européens", "Les Ottomans", "Les Africains"], "Les Amérindiens", "Les Aztèques, les Mayas et les Incas en font partie."),
  Q("Quelle est la principale cause de l'effondrement de la population amérindienne au XVIe siècle ?", ["Les maladies apportées par les Européens", "Les famines dues au froid", "Les guerres entre Aztèques et Incas", "Les tremblements de terre"], "Les maladies apportées par les Européens", "La variole fait des ravages."),
  Q("Quelle richesse les Espagnols recherchent-ils avant tout en Amérique ?", ["L'or et l'argent", "Le charbon", "Le pétrole", "Le blé"], "L'or et l'argent", "La mine d'argent de Potosí devient célèbre."),
]),
notion('H5-3', 1, F, 'hg5-protestants-bible', [
  Q("En quelle langue Luther traduit-il la Bible ?", ["En allemand", "En latin", "En français", "En anglais"], "En allemand", "Il veut que chacun puisse la lire."),
  Q("Pour les protestants, sur quoi repose avant tout la foi ?", ["Sur la Bible", "Sur les décisions du pape", "Sur les reliques", "Sur les indulgences"], "Sur la Bible", "« L'Écriture seule »."),
  Q("Comment appelle-t-on le responsable d'une communauté protestante, qui peut se marier ?", ["Un pasteur", "Un curé", "Un évêque", "Un moine"], "Un pasteur", "Les protestants refusent le célibat obligatoire des prêtres."),
]),
# ══ Intermédiaire ══
notion('H5-3', 0, I, 'hg5i-charles-quint', [
  Q("À quelle grande famille princière appartient Charles Quint ?", ["Les Habsbourg", "Les Valois", "Les Médicis", "Les Bourbons"], "Les Habsbourg", "Il hérite de nombreux territoires par ses grands-parents."),
  N("En quelle année Charles Quint est-il élu empereur du Saint-Empire ?", 1519, "François Ier était aussi candidat."),
  Q("Que fait Charles Quint en 1556, épuisé par ses guerres ?", ["Il abdique et partage ses possessions", "Il se convertit au protestantisme", "Il conquiert la France", "Il devient pape"], "Il abdique et partage ses possessions", "Son fils Philippe II reçoit l'Espagne."),
]),
notion('H5-3', 0, I, 'hg5i-soliman', [
  Q("Quel sultan ottoman règne de 1520 à 1566 ?", ["Soliman le Magnifique", "Mehmed II", "Saladin", "Haroun al-Rachid"], "Soliman le Magnifique", "Les Ottomans l'appellent aussi « le Législateur »."),
  N("En quelle année les Ottomans assiègent-ils Vienne pour la première fois ?", 1529, "La ville résiste."),
  Q("Quelle victoire de 1526 ouvre la Hongrie aux Ottomans ?", ["Mohács", "Lépante", "Pavie", "Marignan"], "Mohács", "Le roi de Hongrie y est tué."),
]),
notion('H5-3', 0, I, 'hg5i-lepante', [
  N("En quelle année a lieu la bataille navale de Lépante ?", 1571, "Elle a lieu près des côtes grecques."),
  Q("Qui affronte la flotte ottomane à Lépante ?", ["La Sainte Ligue, réunie autour de l'Espagne, de Venise et du pape", "La France seule", "L'Angleterre", "Le Portugal"], "La Sainte Ligue, réunie autour de l'Espagne, de Venise et du pape", "C'est une grande victoire chrétienne."),
  Q("Quelle mer est l'enjeu principal des affrontements entre Habsbourg et Ottomans au XVIe siècle ?", ["La Méditerranée", "La mer du Nord", "La mer Baltique", "L'océan Pacifique"], "La Méditerranée", "Ottomans et Espagnols s'en disputent le contrôle."),
]),
notion('H5-3', 0, I, 'hg5i-commerce-atlantique', [
  Q("Quel port espagnol a le monopole du commerce avec l'Amérique au XVIe siècle ?", ["Séville", "Barcelone", "Valence", "Bilbao"], "Séville", "La Casa de Contratación y contrôle le trafic."),
  Q("Comment appelle-t-on les grands navires espagnols qui rapportent l'argent d'Amérique ?", ["Les galions", "Les caravelles", "Les galères", "Les jonques"], "Les galions", "Ils voyagent en convois pour se protéger des pirates."),
  Q("Quelle conséquence a l'afflux d'or et d'argent américain en Europe ?", ["Une forte hausse des prix", "Une baisse des prix", "La disparition de la monnaie", "La fin du commerce"], "Une forte hausse des prix", "On parle de « révolution des prix »."),
]),
notion('H5-3', 0, I, 'hg5i-debut-traite', [
  Q("Quels Européens organisent les premiers la traite des Africains vers l'Amérique ?", ["Les Portugais", "Les Russes", "Les Suédois", "Les Polonais"], "Les Portugais", "D'autres puissances les suivent ensuite."),
  Q("Pour quelles cultures les esclaves africains sont-ils d'abord déportés au Brésil ?", ["Les plantations de canne à sucre", "La culture du blé", "La vigne", "Le coton en Europe"], "Les plantations de canne à sucre", "Le sucre est très recherché en Europe."),
  Q("Pourquoi les colons font-ils venir des esclaves africains en Amérique ?", ["Pour remplacer une main-d'œuvre amérindienne décimée", "Parce que l'Europe manque d'habitants", "Pour peupler les villes européennes", "Par obligation religieuse"], "Pour remplacer une main-d'œuvre amérindienne décimée", "Les maladies et le travail forcé ont tué des millions d'Amérindiens."),
]),
notion('H5-3', 0, I, 'hg5i-valladolid', [
  Q("Quel dominicain espagnol défend les droits des Amérindiens au XVIe siècle ?", ["Bartolomé de Las Casas", "Hernán Cortés", "Ignace de Loyola", "Christophe Colomb"], "Bartolomé de Las Casas", "Il dénonce les violences des conquistadors."),
  N("En quelle année se tient la controverse de Valladolid sur le sort des Amérindiens ?", 1550, "Elle oppose Las Casas à Sepúlveda."),
  Q("Quelle question est au cœur de la controverse de Valladolid ?", ["Les Amérindiens ont-ils une âme et des droits ?", "Faut-il découvrir l'Asie ?", "Le roi doit-il obéir au pape ?", "Faut-il traduire la Bible ?"], "Les Amérindiens ont-ils une âme et des droits ?", "Le débat n'empêche pas la poursuite de l'exploitation."),
]),
notion('H5-3', 1, I, 'hg5i-indulgences', [
  Q("Que dénonce Luther dans ses 95 thèses ?", ["La vente des indulgences", "La traduction de la Bible", "Le pouvoir de l'empereur", "Les croisades"], "La vente des indulgences", "Elles promettaient la rémission des péchés contre de l'argent."),
  Q("Dans quelle ville Luther est-il professeur quand il publie ses thèses ?", ["Wittenberg", "Rome", "Genève", "Paris"], "Wittenberg", "Elle se trouve en Saxe."),
  Q("Devant quelle assemblée Luther refuse-t-il de se rétracter en 1521 ?", ["La diète de Worms", "Le concile de Trente", "Les états généraux", "Le Parlement de Paris"], "La diète de Worms", "Il est mis au ban de l'Empire mais protégé par le prince de Saxe."),
]),
notion('H5-3', 1, I, 'hg5i-calvin', [
  Q("Dans quelle ville Calvin organise-t-il une Église réformée ?", ["Genève", "Wittenberg", "Lyon", "Strasbourg"], "Genève", "On l'a surnommée la « Rome protestante »."),
  Q("Quel ouvrage de Calvin expose sa doctrine ?", ["L'Institution de la religion chrétienne", "Les 95 thèses", "L'Éloge de la folie", "Le Prince"], "L'Institution de la religion chrétienne", "Il paraît en latin en 1536, puis en français."),
  Q("Selon Calvin, comment Dieu choisit-il ceux qui seront sauvés ?", ["Dieu a choisi d'avance les élus (la prédestination)", "Par l'achat d'indulgences", "Par les pèlerinages", "Par le vote des fidèles"], "Dieu a choisi d'avance les élus (la prédestination)", "Cette idée distingue le calvinisme."),
]),
notion('H5-3', 1, I, 'hg5i-anglicanisme', [
  Q("Quel roi d'Angleterre rompt avec le pape en 1534 ?", ["Henri VIII", "Richard Cœur de Lion", "Édouard VI", "Jacques Ier"], "Henri VIII", "Le pape refusait d'annuler son mariage."),
  Q("Comment s'appelle l'Église d'Angleterre dont le roi devient le chef ?", ["L'Église anglicane", "L'Église orthodoxe", "L'Église luthérienne", "L'Église calviniste"], "L'Église anglicane", "L'Acte de suprématie fait du roi le chef de l'Église."),
  Q("Quelle reine, fille d'Henri VIII, installe durablement l'anglicanisme à partir de 1558 ?", ["Élisabeth Ire", "Marie Tudor", "Anne Boleyn", "Victoria"], "Élisabeth Ire", "Sa demi-sœur Marie Tudor avait rétabli le catholicisme."),
]),
notion('H5-3', 1, I, 'hg5i-humanistes-francais', [
  Q("Quel humaniste français écrit Gargantua et Pantagruel ?", ["Rabelais", "Montaigne", "Ronsard", "Molière"], "Rabelais", "Il y défend une éducation complète et joyeuse."),
  Q("Quel humaniste écrit les Essais, où il réfléchit sur lui-même et sur l'humain ?", ["Montaigne", "Rabelais", "Calvin", "Érasme"], "Montaigne", "Il fut aussi maire de Bordeaux."),
  Q("Quelle institution François Ier crée-t-il en 1530 pour enseigner le grec et l'hébreu ?", ["Le Collège des lecteurs royaux (futur Collège de France)", "La Sorbonne", "L'Académie française", "L'École polytechnique"], "Le Collège des lecteurs royaux (futur Collège de France)", "L'enseignement y est libre et gratuit."),
]),
notion('H5-3', 1, I, 'hg5i-copernic-galilee', [
  Q("Quel astronome polonais affirme que la Terre tourne autour du Soleil ?", ["Copernic", "Ptolémée", "Galilée", "Newton"], "Copernic", "Son livre paraît en 1543, l'année de sa mort."),
  Q("Quel savant italien est condamné par l'Église en 1633 pour avoir défendu cette idée ?", ["Galilée", "Copernic", "Léonard de Vinci", "Kepler"], "Galilée", "Il doit renier publiquement ses idées."),
  Q("Quel instrument Galilée perfectionne-t-il pour observer le ciel ?", ["La lunette astronomique", "Le microscope", "Le baromètre", "La boussole"], "La lunette astronomique", "Il découvre ainsi les satellites de Jupiter."),
]),
notion('H5-3', 2, I, 'hg5i-fronde', [
  Q("Comment appelle-t-on la révolte contre le pouvoir royal de 1648 à 1653 ?", ["La Fronde", "La Jacquerie", "La Ligue", "La Commune"], "La Fronde", "Parlementaires puis grands nobles s'y opposent à Mazarin."),
  Q("Quel cardinal gouverne pendant la jeunesse de Louis XIV ?", ["Mazarin", "Richelieu", "Fleury", "Dubois"], "Mazarin", "Il est le principal ministre d'Anne d'Autriche."),
  Q("Quelle conséquence la Fronde a-t-elle sur Louis XIV ?", ["Elle le pousse à se méfier des nobles et de Paris", "Elle le fait abdiquer", "Elle le rend protestant", "Elle lui fait perdre la Normandie"], "Elle le pousse à se méfier des nobles et de Paris", "Il installera sa cour à Versailles."),
]),
notion('H5-3', 2, I, 'hg5i-versailles', [
  N("En quelle année Louis XIV installe-t-il officiellement la cour à Versailles ?", 1682, "Le château devient le centre du pouvoir."),
  Q("Quel jardinier dessine les jardins à la française de Versailles ?", ["André Le Nôtre", "Jules Hardouin-Mansart", "Louis Le Vau", "Charles Le Brun"], "André Le Nôtre", "Les jardins montrent la maîtrise de la nature par le roi."),
  Q("Quelle salle de Versailles célèbre les victoires de Louis XIV ?", ["La galerie des Glaces", "La salle du Jeu de paume", "La chapelle Sixtine", "La salle des Pas perdus"], "La galerie des Glaces", "Elle est achevée en 1684."),
]),
notion('H5-3', 2, I, 'hg5i-armee-louis-xiv', [
  Q("Quel ingénieur construit ou renforce plus de cent forteresses aux frontières pour Louis XIV ?", ["Vauban", "Colbert", "Louvois", "Turenne"], "Vauban", "On parle de la « ceinture de fer »."),
  Q("Quel ministre de la Guerre réorganise l'armée de Louis XIV ?", ["Louvois", "Colbert", "Fouquet", "Mazarin"], "Louvois", "L'armée devient l'une des plus importantes d'Europe."),
  Q("Quelle phrase Louis XIV aurait-il dite à son arrière-petit-fils avant de mourir ?", ["« J'ai trop aimé la guerre »", "« L'État, c'est moi »", "« Après moi le déluge »", "« Paris vaut bien une messe »"], "« J'ai trop aimé la guerre »", "Les guerres ont épuisé le royaume."),
]),
# ══ Avancé ══
notion('H5-3', 0, D, 'hg5d-mehmed-1453', [
  Q("Quel sultan ottoman prend Constantinople en 1453 ?", ["Mehmed II", "Soliman le Magnifique", "Sélim Ier", "Bayezid Ier"], "Mehmed II", "Il est surnommé « le Conquérant »."),
  Q("Quelle arme nouvelle joue un rôle décisif lors du siège de Constantinople ?", ["L'artillerie à poudre (canons)", "L'arc long", "Le feu grégeois", "La cavalerie lourde"], "L'artillerie à poudre (canons)", "Les murailles de la ville cèdent sous les boulets."),
  Q("Que devient la basilique Sainte-Sophie après la prise de Constantinople ?", ["Une mosquée", "Un palais", "Une bibliothèque", "Elle est détruite"], "Une mosquée", "Des minarets lui sont ajoutés."),
]),
notion('H5-3', 1, D, 'hg5d-paix-augsbourg', [
  N("En quelle année la paix d'Augsbourg règle-t-elle le conflit religieux dans le Saint-Empire ?", 1555, "Elle reconnaît le luthéranisme."),
  Q("Quel principe la paix d'Augsbourg établit-elle ?", ["Les sujets suivent la religion de leur prince (cujus regio, ejus religio)", "Chacun choisit librement sa religion", "Seul le catholicisme est permis", "Le pape choisit la religion de chaque État"], "Les sujets suivent la religion de leur prince (cujus regio, ejus religio)", "La liberté de conscience individuelle n'existe pas encore."),
  Q("Quelle confession n'est pas reconnue par la paix d'Augsbourg ?", ["Le calvinisme", "Le luthéranisme", "Le catholicisme", "Aucune"], "Le calvinisme", "Il ne sera reconnu qu'en 1648."),
]),
notion('H5-3', 1, D, 'hg5d-trente-ans', [
  Q("Entre quelles dates se déroule la guerre de Trente Ans ?", ["1618-1648", "1562-1598", "1337-1453", "1701-1714"], "1618-1648", "Elle ravage le Saint-Empire."),
  Q("Quel épisode de 1618 déclenche la guerre de Trente Ans ?", ["La défenestration de Prague", "L'attentat d'Anagni", "La prise de Constantinople", "Le sac de Rome"], "La défenestration de Prague", "Des représentants de l'empereur sont jetés par une fenêtre."),
  Q("Quels traités mettent fin à la guerre de Trente Ans en 1648 ?", ["Les traités de Westphalie", "Le traité de Tordesillas", "Le traité des Pyrénées", "Le traité d'Utrecht"], "Les traités de Westphalie", "Ils fondent un nouvel équilibre européen."),
]),
notion('H5-3', 2, D, 'hg5d-revocation', [
  Q("Par quel édit Louis XIV révoque-t-il l'édit de Nantes en 1685 ?", ["L'édit de Fontainebleau", "L'édit de Villers-Cotterêts", "L'édit de Saint-Germain", "L'édit de Paris"], "L'édit de Fontainebleau", "Le protestantisme est interdit dans le royaume."),
  Q("Comment appelle-t-on le logement forcé de soldats chez les protestants pour les obliger à se convertir ?", ["Les dragonnades", "Les jacqueries", "Les corvées royales", "Les lettres de cachet"], "Les dragonnades", "Les dragons sont des soldats à cheval."),
  Q("Quelle conséquence la révocation a-t-elle pour de nombreux protestants ?", ["Environ 200 000 d'entre eux fuient à l'étranger", "Ils deviennent ministres", "Ils obtiennent de nouveaux droits", "Ils s'installent tous à Versailles"], "Environ 200 000 d'entre eux fuient à l'étranger", "Ils partent vers la Prusse, les Provinces-Unies, l'Angleterre ou la Suisse."),
]),
notion('H5-3', 2, D, 'hg5d-droit-divin', [
  Q("Quel évêque théorise la monarchie absolue de droit divin sous Louis XIV ?", ["Bossuet", "Fénelon", "Pascal", "Richelieu"], "Bossuet", "Pour lui, le roi est le représentant de Dieu sur terre."),
  Q("Que signifie que le roi est « absolu » ?", ["Il concentre tous les pouvoirs, sans contrôle d'une assemblée", "Il est élu à vie par le peuple", "Il partage le pouvoir avec un Parlement élu", "Il obéit au pape"], "Il concentre tous les pouvoirs, sans contrôle d'une assemblée", "Il reste cependant soumis aux lois de Dieu et aux coutumes du royaume."),
  Q("Comment appelle-t-on l'ordre royal permettant d'emprisonner quelqu'un sans jugement ?", ["La lettre de cachet", "La lettre de change", "L'édit royal", "La charte"], "La lettre de cachet", "Elle symbolise l'arbitraire royal."),
]),
notion('H5-3', 2, D, 'hg5d-intendants', [
  Q("Comment appelle-t-on les agents envoyés par le roi dans les provinces pour y appliquer ses décisions au XVIIe siècle ?", ["Les intendants", "Les missi dominici", "Les baillis", "Les préfets"], "Les intendants", "Ils sont chargés de la justice, de la police et des finances."),
  Q("Pourquoi les intendants sont-ils plus dociles que les anciens officiers ?", ["Ils sont nommés et révocables par le roi", "Ils sont élus par la population", "Ils héritent de leur charge", "Ils sont choisis par le pape"], "Ils sont nommés et révocables par le roi", "Les officiers, eux, achetaient leur charge."),
  Q("Quel ministre de Louis XIII généralise les intendants ?", ["Richelieu", "Colbert", "Sully", "Fouquet"], "Richelieu", "L'administration royale se renforce."),
]),
notion('H5-3', 2, D, 'hg5d-francois-ier-pouvoir', [
  N("En quelle année François Ier signe-t-il le concordat de Bologne avec le pape ?", 1516, "Il obtient le droit de nommer les évêques."),
  Q("Quelle entrevue fastueuse réunit François Ier et Henri VIII d'Angleterre en 1520 ?", ["Le camp du Drap d'or", "Le congrès de Vienne", "La paix des Dames", "La diète de Worms"], "Le camp du Drap d'or", "Chaque roi y rivalise de luxe."),
  Q("Quelle défaite de François Ier en 1525 aboutit à sa capture par les troupes de Charles Quint ?", ["Pavie", "Marignan", "Azincourt", "Lépante"], "Pavie", "Il est retenu prisonnier à Madrid."),
]),
notion('H5-3', 1, D, 'hg5d-imprimerie-humanisme', [
  Q("Comment appelle-t-on les livres imprimés avant 1501 ?", ["Les incunables", "Les manuscrits", "Les codex", "Les palimpsestes"], "Les incunables", "Le mot signifie « au berceau »."),
  Q("Quel imprimeur vénitien invente le caractère italique et le livre de poche ?", ["Alde Manuce", "Gutenberg", "Robert Estienne", "Étienne Dolet"], "Alde Manuce", "Il édite les classiques grecs et latins."),
  Q("Quelle ville devient au XVIe siècle l'un des premiers centres d'imprimerie en France ?", ["Lyon", "Brest", "Toulouse", "Lille"], "Lyon", "La ville est aussi une grande place commerciale."),
]),
notion('H5-3', 1, D, 'hg5d-placards', [
  N("En quelle année éclate l'affaire des Placards, affiches hostiles à la messe placardées jusqu'à la porte du roi ?", 1534, "François Ier durcit alors la répression contre les protestants."),
  Q("Quelle attitude François Ier adopte-t-il envers les protestants après l'affaire des Placards ?", ["Il les persécute plus durement", "Il se convertit", "Il leur accorde la liberté de culte", "Il les nomme ministres"], "Il les persécute plus durement", "Des réformés sont brûlés."),
  Q("Quel humaniste imprimeur est brûlé à Paris en 1546 pour hérésie ?", ["Étienne Dolet", "Rabelais", "Montaigne", "Clément Marot"], "Étienne Dolet", "Clément Marot, poète, doit s'exiler."),
]),
notion('H5-3', 1, D, 'hg5d-ligue-assassinats', [
  Q("Comment s'appelle l'alliance catholique dirigée par les Guise pendant les guerres de Religion ?", ["La Sainte Ligue", "La Fronde", "La Hanse", "Le Conseil du roi"], "La Sainte Ligue", "Elle refuse un roi protestant."),
  Q("Quel roi de France est assassiné en 1589 par le moine Jacques Clément ?", ["Henri III", "Henri IV", "Charles IX", "François II"], "Henri III", "Henri de Navarre, protestant, devient l'héritier."),
  Q("Qui assassine Henri IV en 1610 ?", ["Ravaillac", "Jacques Clément", "Damiens", "Cadoudal"], "Ravaillac", "C'est un catholique fanatique."),
]),
notion('H5-3', 1, D, 'hg5d-baroque', [
  Q("Quel style artistique se développe avec la Réforme catholique, mêlant mouvement, émotion et décor abondant ?", ["Le baroque", "Le gothique", "Le roman", "Le néoclassique"], "Le baroque", "Il doit toucher les fidèles."),
  Q("Quel sculpteur et architecte réalise la colonnade de la place Saint-Pierre à Rome ?", ["Le Bernin", "Michel-Ange", "Bramante", "Mansart"], "Le Bernin", "Il est l'un des maîtres du baroque."),
  Q("Quel peintre italien est célèbre pour ses contrastes violents d'ombre et de lumière ?", ["Le Caravage", "Raphaël", "Botticelli", "Titien"], "Le Caravage", "On parle de clair-obscur."),
]),
notion('H5-3', 0, D, 'hg5d-ottomans-pouvoir', [
  Q("Comment s'appellent les soldats d'élite de l'infanterie ottomane ?", ["Les janissaires", "Les mamelouks", "Les conquistadors", "Les mousquetaires"], "Les janissaires", "Ils sont recrutés parmi des enfants chrétiens enlevés et convertis."),
  Q("Quel palais d'Istanbul est la résidence des sultans ottomans ?", ["Topkapi", "L'Alhambra", "Le Kremlin", "L'Escurial"], "Topkapi", "Il domine le Bosphore."),
  Q("Comment appelle-t-on les privilèges commerciaux accordés aux marchands français par les Ottomans en 1536 ?", ["Les capitulations", "Les concordats", "Les capitulaires", "Les franchises urbaines"], "Les capitulations", "Elles scellent l'alliance entre François Ier et Soliman."),
]),
notion('H5-3', 0, D, 'hg5d-empire-portugais', [
  Q("Quel comptoir indien devient le centre de l'empire portugais en Asie en 1510 ?", ["Goa", "Calcutta", "Bombay", "Madras"], "Goa", "Il est conquis par Afonso de Albuquerque."),
  Q("Quel comptoir chinois les Portugais obtiennent-ils au XVIe siècle ?", ["Macao", "Hong Kong", "Shanghai", "Canton"], "Macao", "Il reste portugais jusqu'en 1999."),
  Q("Quel produit fait la richesse du commerce portugais avec l'Asie ?", ["Les épices", "Le charbon", "Le blé", "Le bois de chêne"], "Les épices", "Le poivre, la cannelle et les clous de girofle."),
]),
notion('H5-3', 1, D, 'hg5d-revolution-scientifique', [
  Q("Quel savant allemand découvre que les planètes décrivent des ellipses autour du Soleil ?", ["Kepler", "Copernic", "Galilée", "Tycho Brahe"], "Kepler", "Il publie ses premières lois en 1609."),
  Q("Quel savant anglais formule la loi de la gravitation universelle en 1687 ?", ["Newton", "Darwin", "Halley", "Harvey"], "Newton", "Il unifie la physique de la Terre et du ciel."),
  Q("Quelle académie Colbert fonde-t-il en 1666 ?", ["L'Académie des sciences", "L'Académie française", "L'Académie de médecine", "L'Académie des beaux-arts"], "L'Académie des sciences", "La science devient une affaire d'État."),
]),
notion('H5-3', 2, D, 'hg5d-arts-louis-xiv', [
  Q("Quel cardinal fonde l'Académie française en 1635 ?", ["Richelieu", "Mazarin", "Bossuet", "Fleury"], "Richelieu", "Elle doit fixer la langue française."),
  Q("Quel compositeur d'origine italienne est le musicien favori de Louis XIV ?", ["Jean-Baptiste Lully", "Mozart", "Vivaldi", "Rameau"], "Jean-Baptiste Lully", "Il compose opéras et ballets pour la cour."),
  Q("Quel auteur de comédies, comme Le Bourgeois gentilhomme, est protégé par Louis XIV ?", ["Molière", "Corneille", "Voltaire", "Rousseau"], "Molière", "Ses pièces sont jouées à la cour."),
]),
]
