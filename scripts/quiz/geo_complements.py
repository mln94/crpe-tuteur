# Géographie : notions ajoutées pour que chaque thème du programme (5e, 4e, 3e) compte au moins 30 questions
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ 5e · Thème 1 : La question démographique et l'inégal développement ══
notion('G5-1', 0, F, 'geo-chine-inde', [
  Q("Quel pays est devenu le plus peuplé du monde en 2023 ?", ["L'Inde", "La Chine", "Les États-Unis", "Le Nigeria"], "L'Inde", "L'Inde a dépassé la Chine, dont la population commence à diminuer."),
  Q("Quelle politique la Chine a-t-elle menée de 1979 à 2015 pour limiter les naissances ?", ["La politique de l'enfant unique", "Les allocations familiales", "L'immigration choisie", "Le baby-boom"], "La politique de l'enfant unique", "Elle a fortement réduit la natalité et accéléré le vieillissement."),
  Q("Quel problème démographique la Chine affronte-t-elle aujourd'hui ?", ["Un vieillissement rapide de sa population", "Une natalité très élevée", "Une population très jeune", "Une forte immigration"], "Un vieillissement rapide de sa population", "La part des personnes âgées augmente vite, alors que la population active diminue."),
]),
notion('G5-1', 0, I, 'geo-vieillissement', [
  Q("Qu'appelle-t-on le vieillissement démographique ?", ["L'augmentation de la part des personnes âgées dans la population", "La baisse de l'espérance de vie", "L'augmentation des naissances", "Le départ des jeunes à l'étranger"], "L'augmentation de la part des personnes âgées dans la population", "Il résulte de la baisse de la natalité et de l'allongement de la vie."),
  Q("Quel continent a aujourd'hui la population la plus âgée ?", ["L'Europe", "L'Afrique", "L'Amérique du Sud", "L'Océanie"], "L'Europe", "Le vieillissement est un point commun entre l'Europe, les États-Unis, la Chine et le Japon."),
  Q("Quel pays d'Asie a l'une des populations les plus âgées du monde, avec près de 30 % de plus de 65 ans ?", ["Le Japon", "L'Inde", "Le Pakistan", "Les Philippines"], "Le Japon", "Sa population diminue depuis les années 2010."),
]),
notion('G5-1', 0, D, 'geo-afrique-demographie', [
  Q("Quel pays a l'indice de fécondité le plus élevé du monde, autour de 6 enfants par femme ?", ["Le Niger", "Le Maroc", "L'Afrique du Sud", "L'Égypte"], "Le Niger", "Les pays du Sahel ont les fécondités les plus fortes du monde."),
  Q("Selon l'ONU, quelle part de la population mondiale vivra en Afrique vers 2050 ?", ["Environ un quart", "Environ un dixième", "Environ la moitié", "Environ 5 %"], "Environ un quart", "L'Afrique concentre l'essentiel de la croissance démographique à venir."),
  Q("Pourquoi la population de l'Afrique subsaharienne est-elle très jeune ?", ["Parce que la natalité y reste élevée", "Parce que l'immigration y est forte", "Parce que l'espérance de vie y est la plus longue", "Parce que la mortalité infantile a disparu"], "Parce que la natalité y reste élevée", "Plus de 40 % de la population y a moins de 15 ans."),
]),
notion('G5-1', 1, F, 'geo-odd', [
  Q("Que sont les ODD adoptés par l'ONU en 2015 ?", ["Des objectifs de développement durable à atteindre d'ici 2030", "Des organisations de défense", "Des oléoducs", "Des opérations de maintien de la paix"], "Des objectifs de développement durable à atteindre d'ici 2030", "Le programme de géographie s'appuie sur ces objectifs."),
  N("Combien d'objectifs de développement durable (ODD) l'ONU a-t-elle adoptés en 2015 ?", 17, "Les 17 ODD vont de l'éradication de la pauvreté (ODD 1) aux partenariats (ODD 17)."),
  Q("Quel est l'ODD 1 ?", ["Éradiquer la pauvreté", "Protéger les océans", "Développer les énergies renouvelables", "Réduire les inégalités"], "Éradiquer la pauvreté", "L'ODD 1 vise à éliminer l'extrême pauvreté partout dans le monde."),
]),
notion('G5-1', 1, I, 'geo-pauvrete-monde', [
  Q("Dans quelle région du monde vit aujourd'hui la majorité des personnes en situation d'extrême pauvreté ?", ["En Afrique subsaharienne", "En Europe de l'Ouest", "En Amérique du Nord", "En Océanie"], "En Afrique subsaharienne", "L'extrême pauvreté a beaucoup reculé en Asie depuis les années 1990."),
  Q("Les inégalités de richesse existent-elles aussi à l'intérieur des pays riches ?", ["Oui, on observe pauvreté et inégalités dans tous les pays", "Non, elles n'existent que dans les pays pauvres", "Seulement dans les campagnes", "Seulement en Asie"], "Oui, on observe pauvreté et inégalités dans tous les pays", "Le programme insiste sur ces inégalités sociales à toutes les échelles."),
  Q("Comment appelle-t-on des pays à forte croissance économique, comme le Brésil ou l'Inde ?", ["Des pays émergents", "Des pays les moins avancés", "Des paradis fiscaux", "Des micro-États"], "Des pays émergents", "Ils s'affirment dans l'économie mondiale tout en gardant de fortes inégalités."),
]),
notion('G5-1', 1, D, 'geo-inegalites-monde', [
  Q("Quels pays désignait à l'origine l'acronyme BRICS ?", ["Brésil, Russie, Inde, Chine, Afrique du Sud", "Belgique, Roumanie, Italie, Croatie, Suède", "Bolivie, Russie, Iran, Cuba, Syrie", "Brésil, Royaume-Uni, Inde, Canada, Singapour"], "Brésil, Russie, Inde, Chine, Afrique du Sud", "Le groupe s'est élargi à d'autres pays à partir de 2024."),
  Q("Que représente la « limite Nord-Sud » sur une carte du monde ?", ["Une séparation schématique entre pays riches et pays en développement", "L'équateur", "Une frontière militaire", "La limite des glaces"], "Une séparation schématique entre pays riches et pays en développement", "Elle est aujourd'hui discutée, car les pays émergents brouillent cette opposition."),
  N("Quel est le numéro de l'ODD consacré à l'égalité entre les femmes et les hommes ?", 5, "L'ODD 5 vise l'égalité entre les sexes et l'autonomisation des femmes et des filles."),
]),
# ══ 5e · Thème 2 : Des ressources limitées, à gérer et à renouveler ══
notion('G5-2', 0, F, 'geo-acces-eau', [
  N("Quel est le numéro de l'ODD qui vise l'accès de tous à l'eau salubre et à l'assainissement ?", 6, "Plus de deux milliards de personnes n'ont pas encore accès à une eau potable gérée en toute sécurité."),
  Q("Comment appelle-t-on la transformation de l'eau de mer en eau douce ?", ["Le dessalement", "L'évaporation", "L'irrigation", "La potabilité"], "Le dessalement", "Il consomme beaucoup d'énergie mais se développe dans les pays arides."),
  Q("Qu'est-ce qu'une eau potable ?", ["Une eau que l'on peut boire sans danger pour la santé", "Une eau salée", "Une eau de pluie", "Une eau gazeuse"], "Une eau que l'on peut boire sans danger pour la santé", "Elle doit être traitée et contrôlée."),
]),
notion('G5-2', 0, I, 'geo-energies-renouvelables', [
  Q("Quelle énergie utilise la force du vent ?", ["L'énergie éolienne", "L'énergie géothermique", "L'énergie hydraulique", "L'énergie solaire"], "L'énergie éolienne", "Les éoliennes peuvent être installées à terre ou en mer (offshore)."),
  Q("Quel pays possède le plus grand barrage hydroélectrique du monde, le barrage des Trois-Gorges ?", ["La Chine", "Le Brésil", "Les États-Unis", "L'Égypte"], "La Chine", "Il est construit sur le fleuve Yangzi Jiang."),
  Q("Pourquoi les énergies fossiles posent-elles problème ?", ["Elles émettent des gaz à effet de serre et leurs stocks sont limités", "Elles sont inépuisables", "Elles ne produisent pas d'électricité", "Elles sont interdites partout"], "Elles émettent des gaz à effet de serre et leurs stocks sont limités", "L'ODD 7 encourage le recours aux énergies renouvelables."),
]),
notion('G5-2', 0, D, 'geo-tensions-eau', [
  Q("Quel grand fleuve est au cœur de tensions entre l'Égypte et l'Éthiopie à cause d'un grand barrage ?", ["Le Nil", "Le Niger", "Le Congo", "Le Zambèze"], "Le Nil", "L'Égypte dépend presque entièrement du Nil, dont l'Éthiopie contrôle une partie de l'amont."),
  Q("Comment appelle-t-on un système d'irrigation économe qui apporte l'eau directement au pied des plantes ?", ["Le goutte-à-goutte", "L'irrigation par submersion", "L'aspersion", "Le drainage"], "Le goutte-à-goutte", "Il est très utilisé dans les régions arides, par exemple en Israël."),
  Q("Quelle situation un territoire connaît-il quand ses besoins en eau dépassent durablement ses ressources ?", ["Un stress hydrique", "Une crue", "Un excédent hydrique", "Une marée noire"], "Un stress hydrique", "Le Moyen-Orient et l'Afrique du Nord sont particulièrement concernés."),
]),
notion('G5-2', 1, F, 'geo-agricultures', [
  Q("Comment appelle-t-on l'agriculture qui n'utilise ni pesticides ni engrais chimiques de synthèse ?", ["L'agriculture biologique", "L'agriculture intensive", "L'agriculture productiviste", "L'agriculture hors-sol"], "L'agriculture biologique", "Elle cherche à respecter les sols et la biodiversité."),
  Q("Que vise l'ODD 2 ?", ["Éliminer la faim et promouvoir une agriculture durable", "Développer le tourisme", "Construire des villes", "Réduire le nombre d'agriculteurs"], "Éliminer la faim et promouvoir une agriculture durable", "Il vise aussi la sécurité alimentaire et une meilleure nutrition."),
  Q("Comment appelle-t-on l'agriculture qui produit surtout pour nourrir la famille de l'agriculteur ?", ["L'agriculture vivrière", "L'agriculture commerciale", "L'agriculture de plantation", "L'agrobusiness"], "L'agriculture vivrière", "Elle reste très répandue en Afrique et en Asie du Sud."),
]),
notion('G5-2', 1, I, 'geo-faim-monde', [
  Q("Environ combien de personnes souffrent de la faim dans le monde au milieu des années 2020 ?", ["Environ 700 millions", "Environ 7 millions", "Environ 3 milliards", "Personne"], "Environ 700 millions", "Selon la FAO, environ une personne sur onze souffre de la faim."),
  Q("Quel continent compte la plus forte proportion de personnes sous-alimentées ?", ["L'Afrique", "L'Europe", "L'Amérique du Nord", "L'Océanie"], "L'Afrique", "En nombre absolu, l'Asie compte aussi beaucoup de personnes sous-alimentées."),
  Q("Comment appelle-t-on une alimentation déséquilibrée, par manque ou par excès de certains nutriments ?", ["La malnutrition", "La sous-production", "La surpêche", "La famine"], "La malnutrition", "Elle touche aussi les pays riches, avec l'obésité."),
]),
notion('G5-2', 1, D, 'geo-systemes-alimentaires', [
  Q("Selon la FAO, quelle part de la nourriture produite dans le monde est perdue ou gaspillée ?", ["Environ un tiers", "Environ 1 %", "Environ la moitié", "Environ les trois quarts"], "Environ un tiers", "Réduire le gaspillage fait partie de l'ODD 12 (consommation et production durables)."),
  Q("Comment appelle-t-on l'élevage de poissons, de crevettes ou de coquillages ?", ["L'aquaculture", "L'apiculture", "La sylviculture", "L'aviculture"], "L'aquaculture", "Elle fournit aujourd'hui environ la moitié des produits de la mer consommés."),
  Q("Comment appelle-t-on les cultures destinées surtout à l'exportation, comme le cacao ou le café ?", ["Les cultures commerciales (d'exportation)", "Les cultures vivrières", "Les cultures de jachère", "Les cultures potagères"], "Les cultures commerciales (d'exportation)", "Elles peuvent concurrencer les cultures vivrières pour l'usage des terres."),
]),
# ══ 5e · Thème 3 : L'environnement, du local au planétaire ══
notion('G5-3', 0, F, 'geo-effets-climat', [
  Q("Que deviennent les glaciers des Alpes avec le réchauffement climatique ?", ["Ils reculent et perdent de la masse", "Ils grandissent", "Ils ne changent pas", "Ils se déplacent vers la plaine"], "Ils reculent et perdent de la masse", "La Mer de Glace, à Chamonix, a reculé de plusieurs kilomètres depuis le XIXe siècle."),
  Q("Comment appelle-t-on la dégradation de terres sèches qui deviennent peu fertiles, voire désertiques ?", ["La désertification", "La déforestation", "La périurbanisation", "La salinisation des mers"], "La désertification", "Elle touche notamment le Sahel."),
  Q("Quelle conséquence du réchauffement touche de plus en plus le pourtour méditerranéen en été ?", ["Des sécheresses et des incendies plus fréquents", "Des chutes de neige plus abondantes", "La disparition du soleil", "Une baisse des températures"], "Des sécheresses et des incendies plus fréquents", "Les vagues de chaleur y deviennent plus intenses et plus longues."),
]),
notion('G5-3', 0, I, 'geo-giec-adaptation', [
  Q("Quel groupe d'experts, créé sous l'égide de l'ONU, évalue l'état des connaissances sur le changement climatique ?", ["Le GIEC", "L'OMS", "L'UNESCO", "Le FMI"], "Le GIEC", "Le Groupe d'experts intergouvernemental sur l'évolution du climat publie des rapports de référence."),
  Q("Quels territoires sont particulièrement menacés par la montée du niveau des océans ?", ["Les États insulaires de faible altitude, comme Tuvalu ou les Maldives", "Les hautes montagnes", "Les déserts continentaux", "Les plateaux d'Asie centrale"], "Les États insulaires de faible altitude, comme Tuvalu ou les Maldives", "Certains envisagent déjà de déplacer une partie de leur population."),
  Q("Que signifie « s'adapter » au changement climatique ?", ["Modifier ses aménagements et ses pratiques pour limiter ses effets", "Nier le changement climatique", "Augmenter ses émissions", "Quitter la planète"], "Modifier ses aménagements et ses pratiques pour limiter ses effets", "Exemples : digues, végétalisation des villes, nouvelles cultures."),
]),
notion('G5-3', 0, D, 'geo-attenuation', [
  Q("Comment appelle-t-on les actions qui réduisent les émissions de gaz à effet de serre ?", ["L'atténuation", "L'adaptation", "La résilience", "La vulnérabilité"], "L'atténuation", "Atténuer agit sur les causes ; s'adapter agit sur les effets."),
  Q("Que signifie atteindre la « neutralité carbone » ?", ["Ne pas émettre plus de gaz à effet de serre que ce qui est absorbé", "Ne plus utiliser d'électricité", "Supprimer tout le carbone de la Terre", "Interdire les voitures"], "Ne pas émettre plus de gaz à effet de serre que ce qui est absorbé", "L'Union européenne vise la neutralité carbone en 2050."),
  Q("Quels grands « puits de carbone » naturels absorbent une partie du CO2 émis ?", ["Les océans et les forêts", "Les villes", "Les autoroutes", "Les déserts de sable"], "Les océans et les forêts", "La déforestation réduit donc la capacité d'absorption de la planète."),
]),
notion('G5-3', 1, F, 'geo-risques-sanitaires', [
  Q("Comment appelle-t-on une épidémie qui s'étend à l'échelle mondiale, comme le Covid-19 ?", ["Une pandémie", "Une endémie", "Une famine", "Une canicule"], "Une pandémie", "Les échanges mondiaux accélèrent la diffusion des maladies."),
  N("En quelle année l'OMS qualifie-t-elle le Covid-19 de pandémie ?", 2020, "La déclaration date du 11 mars 2020."),
  Q("Quel organisme de l'ONU est chargé de la santé mondiale ?", ["L'OMS", "La FAO", "L'UNICEF", "L'OMC"], "L'OMS", "L'Organisation mondiale de la santé siège à Genève."),
]),
notion('G5-3', 1, F, 'geo-alea-vulnerabilite', [
  Q("Comment appelle-t-on un phénomène naturel ou technologique potentiellement dangereux (crue, séisme, explosion…) ?", ["Un aléa", "Une résilience", "Une ressource", "Un enjeu"], "Un aléa", "Il devient un risque lorsqu'il menace des populations ou des biens."),
  Q("Que désigne la vulnérabilité d'une société face à un risque ?", ["Sa fragilité, c'est-à-dire l'importance des dommages qu'elle peut subir", "Sa richesse", "Sa population totale", "Sa capacité à exporter"], "Sa fragilité, c'est-à-dire l'importance des dommages qu'elle peut subir", "À aléa égal, les pays pauvres sont souvent plus vulnérables."),
  Q("Quel document chaque école doit-elle préparer pour faire face à un risque majeur ?", ["Le plan particulier de mise en sûreté (PPMS)", "Le projet d'école", "Le règlement intérieur", "Le livret scolaire"], "Le plan particulier de mise en sûreté (PPMS)", "Il prévoit la conduite à tenir et des exercices réguliers."),
]),
notion('G5-3', 1, I, 'geo-catastrophes-technologiques', [
  Q("Quelle catastrophe nucléaire se produit en 1986 en Ukraine, alors en URSS ?", ["Tchernobyl", "Fukushima", "Three Mile Island", "Bhopal"], "Tchernobyl", "Un nuage radioactif touche une grande partie de l'Europe."),
  Q("Quel accident nucléaire suit un séisme et un tsunami au Japon en 2011 ?", ["Fukushima", "Tchernobyl", "Seveso", "Hiroshima"], "Fukushima", "C'est un exemple de risques naturels et technologiques combinés."),
  Q("Comment peut-on schématiser un risque en géographie ?", ["Aléa × vulnérabilité", "Population × superficie", "Richesse ÷ population", "Altitude + température"], "Aléa × vulnérabilité", "Sans enjeux humains exposés, un aléa ne constitue pas un risque."),
]),
notion('G5-3', 1, D, 'geo-precaution', [
  Q("Quel principe impose d'agir pour éviter un dommage grave et irréversible, même sans certitude scientifique complète ?", ["Le principe de précaution", "Le principe pollueur-payeur", "Le principe de subsidiarité", "Le principe de laïcité"], "Le principe de précaution", "Il est souvent invoqué pour les risques sanitaires et environnementaux."),
  Q("Dans quel texte à valeur constitutionnelle le principe de précaution est-il inscrit en France depuis 2005 ?", ["La Charte de l'environnement", "Le Code civil", "La Déclaration de 1789", "Le Code de la route"], "La Charte de l'environnement", "Elle est adossée à la Constitution de 1958."),
  Q("Quelle catastrophe chimique fait des milliers de morts en Inde en 1984 ?", ["Bhopal", "Seveso", "AZF", "Lubrizol"], "Bhopal", "Une fuite de gaz toxique d'une usine de pesticides touche la ville."),
]),

# ══ 4e · Thème 1 : L'urbanisation du monde ══
notion('G4-1', 0, F, 'geo-centres-peripheries', [
  Q("Comment appelle-t-on le cœur historique et commerçant d'une ville ?", ["Le centre-ville", "La périphérie", "La banlieue", "Le périurbain"], "Le centre-ville", "Il concentre souvent monuments, commerces et fonctions administratives."),
  Q("Comment appelle-t-on les communes urbaines qui entourent la ville-centre ?", ["La banlieue", "Le centre historique", "Le quartier d'affaires", "La campagne"], "La banlieue", "La ville-centre et sa banlieue forment l'agglomération."),
  Q("Comment appelle-t-on les communes rurales habitées par des citadins qui travaillent en ville ?", ["L'espace périurbain", "Le centre-ville", "Le bidonville", "La métropole"], "L'espace périurbain", "Les habitants y font chaque jour des navettes vers la ville."),
]),
notion('G4-1', 0, I, 'geo-megapoles', [
  Q("Sur quel continent se trouvent aujourd'hui la majorité des mégapoles ?", ["L'Asie", "L'Europe", "L'Océanie", "L'Amérique du Nord"], "L'Asie", "Tokyo, Delhi, Shanghai, Dhaka ou Jakarta comptent parmi les plus grandes."),
  Q("Quelle mégapole d'Amérique latine dépasse 20 millions d'habitants ?", ["Mexico", "Lima", "Bogota", "Santiago du Chili"], "Mexico", "São Paulo dépasse aussi ce seuil."),
  Q("Selon l'ONU, quelle part de l'humanité devrait vivre en ville vers 2050 ?", ["Environ les deux tiers", "Environ un dixième", "Environ un quart", "La totalité"], "Environ les deux tiers", "Plus de la moitié de l'humanité est urbaine depuis 2007."),
]),
notion('G4-1', 0, D, 'geo-ville-durable', [
  Q("Qu'est-ce qu'un écoquartier ?", ["Un quartier conçu pour limiter son impact sur l'environnement", "Un quartier sans habitants", "Une zone industrielle", "Un bidonville rénové"], "Un quartier conçu pour limiter son impact sur l'environnement", "Il associe sobriété énergétique, mixité et transports doux."),
  Q("Comment appelle-t-on le fait de construire la ville sur elle-même pour limiter l'étalement urbain ?", ["La densification", "La périurbanisation", "L'exode urbain", "La rurbanisation"], "La densification", "Elle réutilise des friches ou des terrains déjà urbanisés."),
  Q("Comment appelle-t-on la séparation des groupes sociaux dans des quartiers différents de la ville ?", ["La ségrégation socio-spatiale", "La métropolisation", "La mixité sociale", "La centralité"], "La ségrégation socio-spatiale", "Les quartiers fermés et les bidonvilles en sont deux extrêmes."),
]),
notion('G4-1', 1, F, 'geo-hubs', [
  Q("Quel équipement relie le plus directement une métropole au reste du monde pour les voyageurs ?", ["Un aéroport international", "Une gare de village", "Un marché couvert", "Une piste cyclable"], "Un aéroport international", "Les grands aéroports sont des marqueurs de l'intégration à la mondialisation."),
  Q("Comment appelle-t-on un aéroport qui sert de grande plateforme de correspondance ?", ["Un hub", "Un CBD", "Une ZEE", "Un port franc"], "Un hub", "Dubaï, Londres-Heathrow ou Paris-Charles-de-Gaulle sont des hubs."),
  Q("Quels réseaux, posés au fond des océans, transportent l'essentiel des données d'Internet entre les continents ?", ["Des câbles sous-marins", "Des satellites uniquement", "Des pipelines", "Des lignes de chemin de fer"], "Des câbles sous-marins", "Les métropoles les mieux connectées en sont les points d'arrivée."),
]),
notion('G4-1', 1, I, 'geo-places-financieres', [
  Q("Comment appelle-t-on le principal centre financier de Londres ?", ["La City", "Westminster", "Soho", "Greenwich"], "La City", "Londres est l'une des villes les plus intégrées à la mondialisation."),
  Q("Quelle rue de New York est le symbole de la finance mondiale ?", ["Wall Street", "Broadway", "Fifth Avenue", "Sunset Boulevard"], "Wall Street", "La Bourse de New York y est installée."),
  Q("Quelle cité-État d'Asie est à la fois un grand centre financier et l'un des premiers ports du monde ?", ["Singapour", "Hong Kong", "Monaco", "Bangkok"], "Singapour", "Elle contrôle le détroit de Malacca, au cœur des échanges maritimes."),
]),
notion('G4-1', 1, D, 'geo-villes-du-sud', [
  Q("Qu'appelle-t-on l'économie informelle ?", ["Les activités non déclarées et non encadrées par l'État", "Le commerce en ligne", "L'industrie de pointe", "Les services publics"], "Les activités non déclarées et non encadrées par l'État", "Elle fait vivre une grande partie des citadins des pays en développement."),
  Q("Selon l'ONU, environ quelle part des citadins du monde vit dans des bidonvilles ou des quartiers informels ?", ["Environ un quart", "Environ 1 %", "Environ les trois quarts", "La moitié exactement"], "Environ un quart", "Cela représente plus d'un milliard de personnes."),
  Q("Quelle ville du Brésil est célèbre pour ses favelas, accrochées aux mornes ?", ["Rio de Janeiro", "Brasilia", "Curitiba", "Manaus"], "Rio de Janeiro", "Les favelas y côtoient des quartiers très aisés."),
]),
# ══ 4e · Thème 2 : Les mobilités humaines transnationales ══
notion('G4-2', 0, F, 'geo-mobilites-types', [
  Q("Quel programme européen permet aux étudiants d'étudier dans un autre pays ?", ["Erasmus+", "Schengen", "Frontex", "Interreg"], "Erasmus+", "Les migrations transnationales ont des motifs variés : études, travail, conflits, climat…"),
  Q("Comment appelle-t-on une migration à l'intérieur d'un même pays ?", ["Une migration interne", "Une migration internationale", "Un exil", "Une expatriation"], "Une migration interne", "Les migrations internes, comme l'exode rural, sont les plus nombreuses."),
  Q("Comment appelle-t-on des personnes contraintes de quitter leur région à cause de catastrophes liées au climat ?", ["Des déplacés climatiques", "Des touristes", "Des frontaliers", "Des expatriés"], "Des déplacés climatiques", "La plupart restent à l'intérieur de leur propre pays."),
]),
notion('G4-2', 0, I, 'geo-migrations-sud-sud', [
  Q("Quels pays du golfe Persique accueillent de nombreux travailleurs venus d'Asie du Sud ?", ["Les Émirats arabes unis et le Qatar", "Le Japon et la Corée du Sud", "Le Brésil et l'Argentine", "La Norvège et la Suède"], "Les Émirats arabes unis et le Qatar", "Les immigrés y sont plus nombreux que les nationaux."),
  Q("Vers quel pays migrent de nombreux travailleurs d'Afrique australe ?", ["L'Afrique du Sud", "Le Maroc", "L'Égypte", "Le Tchad"], "L'Afrique du Sud", "C'est un exemple de migration Sud-Sud."),
  Q("Environ combien de migrants internationaux compte-t-on dans le monde au milieu des années 2020 ?", ["Environ 300 millions", "Environ 3 millions", "Environ 3 milliards", "Environ 30 millions"], "Environ 300 millions", "Cela représente moins de 4 % de la population mondiale."),
]),
notion('G4-2', 0, I, 'geo-diasporas', [
  Q("Comment appelle-t-on une population dispersée hors de son pays d'origine mais qui garde des liens avec lui ?", ["Une diaspora", "Une ethnie", "Une minorité", "Une colonie"], "Une diaspora", "Les diasporas entretiennent des liens économiques et culturels avec leur pays."),
  Q("Quel pays a la plus importante diaspora du monde ?", ["L'Inde", "La France", "L'Australie", "Le Canada"], "L'Inde", "Environ 18 millions d'Indiens vivent hors de leur pays."),
  Q("Quel pays reçoit le plus de transferts de fonds de ses émigrés ?", ["L'Inde", "Les États-Unis", "L'Allemagne", "Le Japon"], "L'Inde", "Le Mexique, les Philippines et la Chine suivent."),
]),
notion('G4-2', 0, D, 'geo-asile-frontieres', [
  Q("Quel texte international de 1951 définit le statut de réfugié ?", ["La Convention de Genève", "Le traité de Rome", "L'accord de Paris", "La Charte de l'ONU"], "La Convention de Genève", "Elle protège les personnes qui craignent des persécutions dans leur pays."),
  Q("Quelle agence de l'Union européenne surveille ses frontières extérieures ?", ["Frontex", "Europol", "Eurostat", "Erasmus"], "Frontex", "Elle intervient notamment en Méditerranée."),
  Q("Comment appelle-t-on un pays que les migrants traversent avant d'atteindre leur destination ?", ["Un pays de transit", "Un pays d'origine", "Un pays d'accueil", "Un paradis fiscal"], "Un pays de transit", "La Libye, la Turquie ou le Mexique sont des pays de transit."),
]),
notion('G4-2', 1, F, 'geo-tourisme-effets', [
  Q("Quel effet positif le tourisme a-t-il souvent pour un territoire ?", ["Il crée des emplois et des revenus", "Il fait baisser les prix", "Il supprime la pollution", "Il réduit le trafic aérien"], "Il crée des emplois et des revenus", "Le tourisme est vital pour l'économie de nombreux pays."),
  Q("Comment appelle-t-on un tourisme respectueux de l'environnement et des populations locales ?", ["L'écotourisme", "Le tourisme de masse", "Le tourisme d'affaires", "Le surtourisme"], "L'écotourisme", "Il valorise la découverte de la nature et des cultures locales."),
  Q("Quelle ville italienne fait payer un droit d'entrée aux visiteurs à la journée pour limiter leur nombre ?", ["Venise", "Rome", "Milan", "Turin"], "Venise", "La ville, qui se vide de ses habitants, est un symbole du surtourisme."),
]),
notion('G4-2', 1, I, 'geo-tourisme-monde', [
  Q("Environ combien d'arrivées de touristes internationaux le monde a-t-il compté en 2019, avant la pandémie ?", ["Environ 1,5 milliard", "Environ 15 millions", "Environ 150 millions", "Environ 15 milliards"], "Environ 1,5 milliard", "Le tourisme international est le plus grand mouvement de population jamais connu."),
  Q("Quelle région du monde reçoit le plus de touristes internationaux ?", ["L'Europe", "L'Afrique", "L'Amérique du Sud", "L'Océanie"], "L'Europe", "Elle accueille environ la moitié des arrivées internationales."),
  Q("Comment appelle-t-on un lieu aménagé spécialement pour le tourisme, comme La Grande-Motte ?", ["Une station touristique", "Une métropole", "Une technopole", "Un port de commerce"], "Une station touristique", "La Grande-Motte a été créée dans les années 1960 lors de l'aménagement du littoral languedocien."),
]),
notion('G4-2', 1, D, 'geo-surtourisme', [
  Q("Comment appelle-t-on la saturation d'un lieu par un trop grand nombre de touristes ?", ["Le surtourisme", "L'écotourisme", "La désindustrialisation", "La gentrification"], "Le surtourisme", "Barcelone, Venise ou Dubrovnik en sont des exemples."),
  Q("Quel type de plateforme est accusé de faire monter les loyers dans les centres des villes touristiques ?", ["Les plateformes de location entre particuliers, comme Airbnb", "Les compagnies ferroviaires", "Les agences pour l'emploi", "Les mairies"], "Les plateformes de location entre particuliers, comme Airbnb", "Les logements loués aux touristes sortent du marché locatif pour les habitants."),
  Q("Comment appelle-t-on la transformation d'un quartier ou d'un territoire par le développement du tourisme ?", ["La touristification", "La métropolisation", "La littoralisation", "La rurbanisation"], "La touristification", "Commerces et logements s'adaptent aux visiteurs plus qu'aux habitants."),
]),
# ══ 4e · Thème 3 : Des espaces transformés par la mondialisation ══
notion('G4-3', 0, I, 'geo-oceans-fragiles', [
  N("Quel est le numéro de l'ODD consacré à la conservation des mers et des océans ?", 14, "L'ODD 14 vise à conserver et exploiter durablement les ressources marines."),
  Q("Comment appelle-t-on une pêche excessive qui épuise les stocks de poissons ?", ["La surpêche", "L'aquaculture", "La pêche artisanale", "Le cabotage"], "La surpêche", "Une grande partie des stocks mondiaux sont exploités au maximum ou surexploités."),
  Q("Comment appelle-t-on les grandes accumulations de déchets plastiques formées par les courants océaniques ?", ["Des vortex (ou « continents ») de déchets", "Des récifs coralliens", "Des marées noires", "Des atolls"], "Des vortex (ou « continents ») de déchets", "Le plus connu se trouve dans le nord de l'océan Pacifique."),
]),
notion('G4-3', 0, D, 'geo-routes-maritimes', [
  Q("Quel canal relie l'océan Atlantique à l'océan Pacifique ?", ["Le canal de Panama", "Le canal de Suez", "Le canal de Corinthe", "Le canal du Midi"], "Le canal de Panama", "Inauguré en 1914, il a été élargi en 2016."),
  Q("Quel détroit d'Asie du Sud-Est est l'un des plus fréquentés du monde ?", ["Le détroit de Malacca", "Le détroit de Gibraltar", "Le détroit de Béring", "Le pas de Calais"], "Le détroit de Malacca", "Il relie l'océan Indien à la mer de Chine méridionale."),
  Q("Quel est le premier port du monde pour le trafic de conteneurs ?", ["Shanghai", "Rotterdam", "Le Havre", "New York"], "Shanghai", "Les plus grands ports à conteneurs sont presque tous en Asie de l'Est."),
]),
notion('G4-3', 1, I, 'geo-usa-territoire', [
  Q("Comment appelle-t-on la vieille région industrielle du nord-est des États-Unis, en déclin ?", ["La Rust Belt (ceinture de la rouille)", "La Sun Belt", "La Silicon Valley", "La Corn Belt"], "La Rust Belt (ceinture de la rouille)", "La désindustrialisation y a touché des villes comme Detroit ou Pittsburgh."),
  Q("Quelle frontière est franchie par de nombreux migrants qui veulent entrer aux États-Unis ?", ["La frontière avec le Mexique", "La frontière avec le Canada", "La frontière avec Cuba", "La frontière avec le Brésil"], "La frontière avec le Mexique", "C'est l'une des frontières les plus franchies du monde."),
  Q("Quelles façades concentrent l'essentiel de la population et des activités des États-Unis ?", ["Les façades atlantique et pacifique", "Le centre du pays", "Les Rocheuses", "L'Alaska"], "Les façades atlantique et pacifique", "La littoralisation y reflète l'ouverture du pays sur le monde."),
]),
notion('G4-3', 1, D, 'geo-usa-mondialisation', [
  Q("Quel accord de libre-échange relie les États-Unis, le Canada et le Mexique depuis 2020 ?", ["L'ACEUM (qui a remplacé l'ALENA)", "Le Mercosur", "L'ASEAN", "L'Union européenne"], "L'ACEUM (qui a remplacé l'ALENA)", "L'ALENA était en vigueur depuis 1994."),
  Q("Comment appelle-t-on les usines d'assemblage installées côté mexicain de la frontière avec les États-Unis ?", ["Les maquiladoras", "Les favelas", "Les haciendas", "Les technopoles"], "Les maquiladoras", "Elles profitent d'une main-d'œuvre moins chère et de la proximité du marché américain."),
  Q("Quel grand complexe portuaire de la côte pacifique est la principale porte d'entrée des marchandises asiatiques aux États-Unis ?", ["Los Angeles - Long Beach", "New York - New Jersey", "La Nouvelle-Orléans", "Boston"], "Los Angeles - Long Beach", "Il illustre le basculement des échanges vers le Pacifique."),
]),
notion('G4-3', 2, F, 'geo-afrique-ouest', [
  Q("Quel pays est le premier producteur mondial de cacao ?", ["La Côte d'Ivoire", "Le Brésil", "La Suisse", "Le Maroc"], "La Côte d'Ivoire", "Avec le Ghana, il produit plus de la moitié du cacao mondial."),
  Q("Quel grand fleuve traverse l'Afrique de l'Ouest, du Mali au Nigeria ?", ["Le Niger", "Le Nil", "Le Congo", "L'Orange"], "Le Niger", "Il est vital pour l'agriculture et la pêche des pays sahéliens."),
  Q("Comment appelle-t-on la bande semi-aride qui s'étend au sud du Sahara ?", ["Le Sahel", "Le Maghreb", "La savane équatoriale", "La forêt dense"], "Le Sahel", "C'est une région très exposée aux sécheresses et à l'insécurité."),
]),
notion('G4-3', 2, I, 'geo-afrique-dynamiques', [
  Q("Quelle zone de libre-échange à l'échelle du continent africain est entrée en vigueur en 2021 ?", ["La ZLECAf", "L'ALENA", "Le Mercosur", "L'AELE"], "La ZLECAf", "Elle vise à développer les échanges entre pays africains, encore faibles."),
  Q("Quel pays est devenu un grand investisseur en Afrique, notamment dans les routes, les ports et les chemins de fer ?", ["La Chine", "La Suisse", "L'Islande", "La Nouvelle-Zélande"], "La Chine", "Ces investissements s'inscrivent dans les « nouvelles routes de la soie »."),
  Q("Quelle ressource fait du Nigeria l'un des grands exportateurs d'Afrique ?", ["Le pétrole", "Le cacao", "Le café", "Le coton"], "Le pétrole", "Cette dépendance rend son économie sensible aux variations des cours."),
]),

# ══ 3e · Thème 1 : Dynamiques territoriales de la France contemporaine ══
notion('G3-1', 0, I, 'geo-aires-attraction', [
  Q("Quelle est la deuxième aire d'attraction de France par sa population, après Paris ?", ["Lyon", "Marseille", "Lille", "Toulouse"], "Lyon", "L'aire d'attraction de Lyon compte environ 2,3 millions d'habitants."),
  Q("Comment l'Insee appelle-t-il l'ensemble formé par une ville et les communes dont les actifs viennent y travailler ?", ["Une aire d'attraction d'une ville", "Un département", "Une région", "Un canton"], "Une aire d'attraction d'une ville", "Ce zonage a remplacé celui des « aires urbaines » en 2020."),
  Q("Comment appelle-t-on la commune principale d'une agglomération ?", ["La ville-centre", "La commune périurbaine", "La banlieue", "Le bourg rural"], "La ville-centre", "Elle concentre souvent les emplois et les services."),
]),
notion('G3-1', 0, D, 'geo-periurbanisation', [
  Q("Quel moyen de transport a rendu possible la forte périurbanisation en France depuis les années 1970 ?", ["L'automobile", "Le tramway", "Le TGV", "L'avion"], "L'automobile", "La voiture permet de vivre loin de son lieu de travail."),
  Q("Quel problème environnemental la périurbanisation pose-t-elle ?", ["L'artificialisation des sols agricoles et naturels", "La hausse de la natalité", "La disparition des villes", "La baisse du trafic routier"], "L'artificialisation des sols agricoles et naturels", "Lotissements, routes et zones commerciales consomment des terres."),
  Q("Quelle loi de 2021 fixe l'objectif de « zéro artificialisation nette » des sols en 2050 ?", ["La loi Climat et résilience", "La loi Littoral", "La loi Montagne", "La loi Ferry"], "La loi Climat et résilience", "Elle vise à diviser par deux le rythme d'artificialisation d'ici 2031."),
]),
notion('G3-1', 1, F, 'geo-industrie-france', [
  Q("Quelle ville est le grand centre de l'industrie aéronautique en France, avec Airbus ?", ["Toulouse", "Brest", "Strasbourg", "Dijon"], "Toulouse", "Elle forme un pôle de compétitivité aéronautique et spatial."),
  Q("Quel port est le premier port français pour le trafic de conteneurs ?", ["Le Havre", "Brest", "La Rochelle", "Nice"], "Le Havre", "Avec Rouen et Paris, il forme l'ensemble portuaire HAROPA, sur l'axe Seine."),
  Q("Comment appelle-t-on une zone industrielle construite au bord d'un grand port, comme Fos-sur-Mer ?", ["Une zone industrialo-portuaire (ZIP)", "Un parc naturel", "Un quartier d'affaires", "Une station balnéaire"], "Une zone industrialo-portuaire (ZIP)", "Les industries lourdes y reçoivent directement les matières premières importées."),
]),
notion('G3-1', 1, I, 'geo-agriculture-france', [
  Q("Quel pays est le premier producteur agricole de l'Union européenne ?", ["La France", "Malte", "Le Luxembourg", "La Finlande"], "La France", "Elle représente près d'un cinquième de la production agricole européenne."),
  Q("Quelle grande région agricole est le principal espace céréalier de France ?", ["Le Bassin parisien (Beauce, Brie)", "La Corse", "Les Alpes du Nord", "La Guyane"], "Le Bassin parisien (Beauce, Brie)", "Les grandes exploitations y pratiquent une agriculture très productive."),
  Q("De quelle céréale la France est-elle le premier producteur de l'Union européenne ?", ["Le blé", "Le riz", "Le maïs doux uniquement", "Le sorgho"], "Le blé", "Une grande partie est exportée, ce qui fait de l'agriculture un atout commercial."),
]),
notion('G3-1', 2, I, 'geo-montagnes-france', [
  Q("Quelle activité fait vivre de nombreuses stations des Alpes en hiver ?", ["Les sports d'hiver (ski)", "La pêche en mer", "La riziculture", "L'industrie automobile"], "Les sports d'hiver (ski)", "Le manque de neige lié au réchauffement pousse les stations à se diversifier."),
  Q("Quel est le premier parc national créé en France, en 1963 ?", ["La Vanoise", "Les Cévennes", "Les Écrins", "Port-Cros"], "La Vanoise", "Les parcs nationaux protègent des milieux naturels remarquables."),
  Q("Comment appelle-t-on un parc qui associe protection de la nature et développement des activités locales, comme celui du Vercors ?", ["Un parc naturel régional", "Un parc d'attractions", "Un parc d'activités", "Un parc éolien"], "Un parc naturel régional", "Ils couvrent une part importante du territoire, souvent des espaces de faible densité."),
]),
notion('G3-1', 2, D, 'geo-renouveau-rural', [
  Q("Comment appelle-t-on le regain de population que connaissent certaines campagnes françaises ?", ["Le renouveau rural", "L'exode rural", "La désertification industrielle", "La métropolisation"], "Le renouveau rural", "Retraités, néoruraux et télétravailleurs s'y installent."),
  Q("Quel équipement est devenu essentiel pour attirer des télétravailleurs dans les espaces ruraux ?", ["L'accès à Internet à très haut débit", "Un aéroport international", "Un quartier d'affaires", "Une autoroute à huit voies"], "L'accès à Internet à très haut débit", "La fracture numérique est une inégalité territoriale."),
  Q("Quel atout les espaces de faible densité peuvent-ils valoriser auprès des visiteurs ?", ["Leurs paysages et leur patrimoine, à travers le tourisme vert", "Leurs gratte-ciel", "Leurs embouteillages", "Leurs grandes zones industrielles"], "Leurs paysages et leur patrimoine, à travers le tourisme vert", "Ce ne sont pas seulement des marges délaissées."),
]),
# ══ 3e · Thème 2 : Pourquoi et comment aménager le territoire ? ══
notion('G3-2', 0, F, 'geo-collectivites', [
  Q("Quel acteur décide et finance les grands aménagements nationaux, comme les lignes à grande vitesse ?", ["L'État", "Une commune seule", "Une association de quartier", "Une école"], "L'État", "Il agit aujourd'hui avec les collectivités territoriales et l'Union européenne."),
  Q("Quelle collectivité territoriale est chargée des lycées ?", ["La région", "La commune", "Le département", "L'État seul"], "La région", "La région s'occupe aussi des transports régionaux (TER)."),
  Q("Quelle collectivité territoriale est chargée des collèges ?", ["Le département", "La région", "La commune", "L'Union européenne"], "Le département", "Les écoles primaires relèvent des communes."),
]),
notion('G3-2', 0, F, 'geo-transports-amenagement', [
  N("En quelle année la première ligne de TGV relie-t-elle Paris à Lyon ?", 1981, "Le TGV a réduit les distances-temps entre Paris et les grandes villes."),
  Q("Comment est organisé le réseau ferré et autoroutier français hérité de l'histoire ?", ["En étoile autour de Paris", "En cercle autour de Lyon", "En ligne droite de Brest à Nice", "Sans aucune organisation"], "En étoile autour de Paris", "Les liaisons transversales entre villes de province restent moins développées."),
  Q("Comment appelle-t-on un lieu qui relie plusieurs modes de transport (train, bus, tramway, vélo) ?", ["Un pôle multimodal", "Une zone franche", "Un hub financier", "Un échangeur autoroutier"], "Un pôle multimodal", "Il facilite les correspondances et réduit l'usage de la voiture."),
]),
notion('G3-2', 0, I, 'geo-inegalites-territoires', [
  Q("Comment appelle-t-on les quartiers urbains en difficulté ciblés en priorité par la politique de la ville ?", ["Les quartiers prioritaires (QPV)", "Les quartiers d'affaires", "Les centres historiques", "Les écoquartiers"], "Les quartiers prioritaires (QPV)", "Ils concentrent chômage et pauvreté."),
  Q("Comment appelle-t-on un territoire où l'accès aux médecins est très difficile ?", ["Un désert médical", "Une zone blanche", "Un espace périurbain", "Une technopole"], "Un désert médical", "Il touche surtout des espaces ruraux, mais aussi certaines banlieues."),
  Q("Quel programme national aide depuis 2018 à revitaliser le centre des villes moyennes ?", ["Action cœur de ville", "Erasmus+", "Le plan Marshall", "Le Grand Paris Express"], "Action cœur de ville", "Il finance la rénovation des logements et des commerces de centre-ville."),
]),
notion('G3-2', 0, I, 'geo-croquis', [
  Q("Comment appelle-t-on une représentation cartographique simplifiée qui montre l'organisation d'un territoire ?", ["Un croquis", "Une photographie aérienne", "Un tableau statistique", "Une frise chronologique"], "Un croquis", "Il est accompagné d'une légende organisée et d'un titre."),
  Q("À quoi sert la légende d'une carte ou d'un croquis ?", ["À expliquer la signification des figurés utilisés", "À donner le nom de l'auteur", "À indiquer le prix de la carte", "À décorer la carte"], "À expliquer la signification des figurés utilisés", "Une légende organisée regroupe les figurés en parties."),
  Q("Quel type de figuré représente des flux, comme des migrations ou des échanges ?", ["Des flèches", "Des aplats de couleur", "Des points", "Des hachures"], "Des flèches", "Les aplats représentent des surfaces, les points des lieux."),
]),
notion('G3-2', 0, D, 'geo-amenagement-europe', [
  Q("Quel fonds européen finance des projets pour réduire les écarts de développement entre régions ?", ["Le FEDER", "Le FMI", "La BCE", "Frontex"], "Le FEDER", "Le Fonds européen de développement régional cofinance routes, équipements et innovation."),
  Q("Quel ouvrage relie la France au Royaume-Uni depuis 1994 ?", ["Le tunnel sous la Manche", "Le viaduc de Millau", "Le pont de Normandie", "Le tunnel du Mont-Blanc"], "Le tunnel sous la Manche", "Il est emprunté par l'Eurostar et des navettes pour véhicules."),
  Q("Quel grand projet ferroviaire européen, très débattu, doit relier Lyon à Turin ?", ["La ligne Lyon-Turin", "Le Grand Paris Express", "La LGV Atlantique", "Le RER E"], "La ligne Lyon-Turin", "Il illustre les débats que suscitent les grands aménagements."),
]),
notion('G3-2', 1, F, 'geo-outremer-carte', [
  Q("Dans quelle mer se trouve la Martinique ?", ["La mer des Caraïbes (Antilles)", "La mer du Nord", "La mer Méditerranée", "La mer Baltique"], "La mer des Caraïbes (Antilles)", "La Martinique et la Guadeloupe forment les Antilles françaises."),
  Q("Quel atout majeur les outre-mer apportent-ils à la France ?", ["Une immense zone économique exclusive (ZEE)", "Des grandes plaines céréalières", "Les principaux centres financiers", "Toutes les centrales nucléaires"], "Une immense zone économique exclusive (ZEE)", "Grâce à eux, la France possède la deuxième ZEE du monde."),
  Q("Sur quelle île française de l'océan Indien se trouve le volcan du Piton de la Fournaise ?", ["La Réunion", "Mayotte", "La Martinique", "Tahiti"], "La Réunion", "C'est l'un des volcans les plus actifs du monde."),
]),
notion('G3-2', 1, I, 'geo-drom', [
  Q("Quel département et région d'outre-mer se trouve en Amérique du Sud ?", ["La Guyane", "La Guadeloupe", "La Réunion", "Mayotte"], "La Guyane", "C'est le plus vaste département français, couvert en grande partie par la forêt amazonienne."),
  Q("Quelle installation stratégique se trouve à Kourou, en Guyane ?", ["Le Centre spatial guyanais", "Une centrale nucléaire", "Le siège de l'ONU", "Le port du Havre"], "Le Centre spatial guyanais", "Les fusées Ariane y sont lancées, grâce à la proximité de l'équateur."),
  Q("Quel territoire est devenu le 101e département français en 2011 ?", ["Mayotte", "La Martinique", "La Polynésie française", "Saint-Pierre-et-Miquelon"], "Mayotte", "C'est le département le plus pauvre et le plus jeune de France."),
]),
notion('G3-2', 1, D, 'geo-outremer-defis', [
  Q("Comment l'Union européenne désigne-t-elle les départements et régions d'outre-mer ?", ["Des régions ultrapériphériques (RUP)", "Des pays associés", "Des États membres", "Des zones franches"], "Des régions ultrapériphériques (RUP)", "Ils font partie de l'UE et reçoivent des aides spécifiques."),
  Q("Quelles difficultés partagent la plupart des DROM ?", ["Un chômage élevé et une vie chère", "Une population très âgée partout", "Un manque d'espace maritime", "Un climat polaire"], "Un chômage élevé et une vie chère", "L'éloignement et l'insularité renchérissent les produits importés."),
  Q("Quel territoire français du Pacifique a un statut particulier issu des accords de Nouméa (1998) ?", ["La Nouvelle-Calédonie", "La Réunion", "La Guyane", "La Corse"], "La Nouvelle-Calédonie", "Ses habitants ont été consultés à plusieurs reprises sur l'indépendance."),
]),
# ══ 3e · Thème 3 : La France et l'Union européenne ══
notion('G3-3', 0, F, 'geo-ue-symboles', [
  Q("Dans quelle ville siège la Commission européenne ?", ["Bruxelles", "Strasbourg", "Luxembourg", "Francfort"], "Bruxelles", "La Banque centrale européenne siège à Francfort."),
  Q("À quoi ressemble le drapeau de l'Union européenne ?", ["Un cercle de 12 étoiles dorées sur fond bleu", "Une croix blanche sur fond rouge", "Trois bandes verticales bleu, blanc, rouge", "Une étoile par État membre sur fond blanc"], "Un cercle de 12 étoiles dorées sur fond bleu", "Le nombre d'étoiles ne dépend pas du nombre d'États : il symbolise l'unité."),
  Q("Quelle est la devise de l'Union européenne ?", ["« Unie dans la diversité »", "« Liberté, Égalité, Fraternité »", "« Un pour tous, tous pour un »", "« In God We Trust »"], "« Unie dans la diversité »", "Elle a été adoptée en 2000."),
]),
notion('G3-3', 0, I, 'geo-ue-territoire', [
  Q("Quel est le pays le plus peuplé de l'Union européenne ?", ["L'Allemagne", "La France", "L'Italie", "L'Espagne"], "L'Allemagne", "Elle compte environ 84 millions d'habitants ; la France arrive en deuxième position."),
  Q("Comment appelle-t-on l'axe le plus peuplé et le plus riche d'Europe, qui s'étend de Londres à Milan ?", ["La dorsale européenne", "Le Sahel", "La Sun Belt", "La diagonale des faibles densités"], "La dorsale européenne", "On l'appelle aussi la « banane bleue »."),
  Q("Quelle est la capitale la plus peuplée de l'Union européenne ?", ["Berlin", "Paris", "Rome", "Madrid"], "Berlin", "Paris intra-muros compte environ 2 millions d'habitants, Berlin plus de 3,5 millions."),
]),
notion('G3-3', 0, I, 'geo-ue-politiques', [
  Q("Quelle politique européenne soutient les agriculteurs depuis 1962 ?", ["La politique agricole commune (PAC)", "La politique de la ville", "La politique monétaire", "Le pacte de Varsovie"], "La politique agricole commune (PAC)", "La France en est la première bénéficiaire."),
  Q("Comment appelle-t-on l'espace où marchandises, services, capitaux et personnes circulent librement dans l'UE ?", ["Le marché unique", "La zone euro", "L'OTAN", "Le Commonwealth"], "Le marché unique", "Il est en place depuis 1993."),
  Q("Quel traité, signé en 2007, réforme le fonctionnement des institutions de l'UE ?", ["Le traité de Lisbonne", "Le traité de Rome", "Le traité de Versailles", "Le traité de Verdun"], "Le traité de Lisbonne", "Il est entré en vigueur en 2009."),
]),
notion('G3-3', 0, D, 'geo-ue-elargissements', [
  N("En quelle année l'Union européenne accueille-t-elle dix nouveaux pays, surtout d'Europe centrale et orientale ?", 2004, "C'est le plus grand élargissement de son histoire."),
  Q("Quel pays a quitté l'Union européenne en 2020 ?", ["Le Royaume-Uni", "La Norvège", "La Suisse", "L'Islande"], "Le Royaume-Uni", "Le Brexit avait été décidé par référendum en 2016."),
  Q("Quel pays est le dernier à être entré dans l'Union européenne, en 2013 ?", ["La Croatie", "La Pologne", "La Bulgarie", "L'Ukraine"], "La Croatie", "D'autres pays, comme l'Ukraine ou la Moldavie, sont candidats."),
]),
notion('G3-3', 0, D, 'geo-transfrontalier', [
  Q("Comment appelle-t-on les personnes qui vivent en France et travaillent en Suisse ou au Luxembourg ?", ["Des travailleurs frontaliers", "Des expatriés", "Des réfugiés", "Des saisonniers agricoles"], "Des travailleurs frontaliers", "Plusieurs centaines de milliers de Français sont concernés."),
  Q("Quel programme européen finance la coopération entre régions frontalières ?", ["Interreg", "Erasmus+", "Horizon Europe", "Galileo"], "Interreg", "Il soutient des projets communs de transport, de santé ou d'environnement."),
  Q("Quelle agglomération transfrontalière associe Lille à des villes belges ?", ["L'Eurométropole Lille-Kortrijk-Tournai", "Le Grand Genève", "L'Eurodistrict Strasbourg-Ortenau", "La métropole Aix-Marseille"], "L'Eurométropole Lille-Kortrijk-Tournai", "Le Grand Genève et l'Eurodistrict Strasbourg-Ortenau sont d'autres exemples, avec la Suisse et l'Allemagne."),
]),
notion('G3-3', 1, F, 'geo-francophonie', [
  Q("Environ combien de personnes parlent français dans le monde ?", ["Environ 320 millions", "Environ 32 millions", "Environ 3 milliards", "Environ 3 millions"], "Environ 320 millions", "Le français est l'une des langues les plus parlées du monde, surtout grâce à l'Afrique."),
  Q("Quel musée parisien est le plus visité au monde ?", ["Le Louvre", "Le musée d'Orsay", "Le centre Pompidou", "Le musée Grévin"], "Le Louvre", "Le rayonnement culturel fait partie de l'influence de la France."),
  Q("Quel réseau d'établissements diffuse la langue et la culture françaises à l'étranger ?", ["L'Alliance française", "La SNCF", "L'Insee", "Météo-France"], "L'Alliance française", "Elle est présente dans plus de 130 pays."),
]),
notion('G3-3', 1, I, 'geo-france-puissance', [
  Q("La France possède-t-elle l'arme nucléaire ?", ["Oui, c'est l'une des puissances nucléaires reconnues", "Non", "Seulement en Europe avec l'Allemagne", "Seulement depuis 2020"], "Oui, c'est l'une des puissances nucléaires reconnues", "La dissuasion nucléaire est un pilier de sa défense depuis les années 1960."),
  Q("Grâce à quoi la France est-elle présente dans tous les océans du globe ?", ["Ses territoires d'outre-mer", "Ses fleuves", "Ses montagnes", "Ses autoroutes"], "Ses territoires d'outre-mer", "Ils lui donnent aussi une ZEE d'environ 10 millions de km²."),
  Q("Où se situe l'économie française parmi les économies du monde (par le PIB) ?", ["Parmi les dix premières", "Au-delà de la cinquantième place", "À la première place", "Parmi les vingt dernières"], "Parmi les dix premières", "Elle est la deuxième économie de l'Union européenne, après l'Allemagne."),
]),
notion('G3-3', 1, D, 'geo-europe-monde', [
  Q("Quel est le premier partenaire commercial de la France ?", ["L'Allemagne", "Le Japon", "Le Brésil", "L'Australie"], "L'Allemagne", "Les échanges de la France se font surtout avec les autres pays de l'UE."),
  Q("Dans quelle ville siège la Cour européenne des droits de l'homme ?", ["Strasbourg", "Bruxelles", "La Haye", "Genève"], "Strasbourg", "Elle dépend du Conseil de l'Europe, qui regroupe 46 États, au-delà de l'UE."),
  Q("Quel ensemble est le premier donateur d'aide publique au développement dans le monde ?", ["L'Union européenne et ses États membres", "La Russie", "L'Arabie saoudite", "Le Japon seul"], "L'Union européenne et ses États membres", "Cette aide est un instrument de l'influence européenne dans le monde."),
]),
]
