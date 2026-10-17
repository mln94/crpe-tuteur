from qlib import Q, N, C, notion
I = 'intermediaire'
NOTIONS = [
notion('E4-1', 0, I, 'emc-hierarchie-normes', [
  Q("Quel ordre respecte la hiérarchie des normes en France, du plus haut au plus bas ?", ["Loi, Constitution, décret", "Constitution, traités, lois, décrets", "Décrets, lois, Constitution", "Traités, décrets, Constitution"], "Constitution, traités, lois, décrets", "La Constitution est au sommet ; les traités ont une valeur supérieure aux lois, qui s'imposent aux décrets."),
  Q("Un décret peut-il être contraire à une loi ?", ["Oui", "Non, il doit respecter la loi", "Seulement en période électorale", "Oui s'il est signé par le président"], "Non, il doit respecter la loi", "Un texte inférieur doit respecter les textes supérieurs ; sinon il peut être annulé par le juge."),
  Q("Quel juge peut annuler un décret illégal ?", ["Le Conseil d'État", "La cour d'assises", "Le conseil de prud'hommes", "Le tribunal de police"], "Le Conseil d'État", "Le Conseil d'État est la plus haute juridiction administrative."),
]),
notion('E4-1', 0, I, 'emc-qpc', [
  Q("Qu'est-ce qu'une question prioritaire de constitutionnalité (QPC) ?", ["Une question posée au gouvernement", "La possibilité pour un justiciable de contester une loi déjà en vigueur qui porterait atteinte à ses droits constitutionnels", "Un référendum", "Une question d'examen"], "La possibilité pour un justiciable de contester une loi déjà en vigueur qui porterait atteinte à ses droits constitutionnels", "La QPC, créée par la révision de 2008, est appliquée depuis 2010."),
  N("Depuis quelle année la question prioritaire de constitutionnalité est-elle appliquée ?", 2010, "Prévue par la révision constitutionnelle de 2008, la QPC entre en vigueur le 1er mars 2010."),
  Q("Quelle institution tranche une QPC ?", ["Le Parlement", "Le Conseil constitutionnel", "Le Conseil d'État seul", "La Cour européenne des droits de l'homme"], "Le Conseil constitutionnel", "Après filtrage par le Conseil d'État ou la Cour de cassation, le Conseil constitutionnel décide."),
]),
notion('E4-1', 0, I, 'emc-ordres-juridictions', [
  Q("Quels sont les deux ordres de juridiction en France ?", ["Civil et militaire", "Judiciaire et administratif", "National et local", "Pénal et européen"], "Judiciaire et administratif", "L'ordre judiciaire juge les litiges entre personnes privées et les infractions ; l'ordre administratif, les litiges avec l'administration."),
  Q("Quelle est la plus haute juridiction de l'ordre judiciaire ?", ["Le Conseil d'État", "La Cour de cassation", "Le Conseil constitutionnel", "La cour d'appel"], "La Cour de cassation", "La Cour de cassation vérifie la bonne application du droit par les tribunaux."),
  Q("Un parent conteste une décision de la mairie sur l'inscription scolaire. Devant quel tribunal ?", ["Le tribunal administratif", "Le conseil de prud'hommes", "La cour d'assises", "Le tribunal de commerce"], "Le tribunal administratif", "Les litiges avec une administration relèvent du juge administratif."),
]),
notion('E4-1', 1, I, 'emc-liberte-conscience-culte', [
  Q("Que garantit l'article 1er de la loi de 1905 ?", ["La religion d'État", "La liberté de conscience et le libre exercice des cultes", "L'interdiction des cultes", "Le financement des Églises"], "La liberté de conscience et le libre exercice des cultes", "« La République assure la liberté de conscience. Elle garantit le libre exercice des cultes » sous les seules restrictions d'ordre public."),
  Q("Le libre exercice des cultes peut être limité…", ["selon l'humeur du maire", "dans l'intérêt de l'ordre public", "jamais", "pour les religions minoritaires seulement"], "dans l'intérêt de l'ordre public", "La loi de 1905 garantit le libre exercice des cultes sous les seules restrictions édictées dans l'intérêt de l'ordre public."),
  Q("Le blasphème est-il un délit en France ?", ["Oui", "Non, critiquer une religion relève de la liberté d'expression", "Seulement à la télévision", "Seulement contre la religion majoritaire"], "Non, critiquer une religion relève de la liberté d'expression", "En revanche, l'injure ou la provocation à la haine envers des personnes en raison de leur religion est punie."),
]),
notion('E4-1', 1, I, 'emc-charte-laicite', [
  N("Combien d'articles compte la Charte de la laïcité à l'École ?", 15, "La Charte de 2013 comporte 15 articles, affichés dans les écoles et établissements publics."),
  Q("Selon la Charte de la laïcité, un élève peut-il contester un enseignement au nom de ses convictions religieuses ?", ["Oui", "Non, aucun élève ne peut invoquer une conviction religieuse pour contester une question au programme", "Oui, en histoire seulement", "Oui, avec l'accord des parents"], "Non, aucun élève ne peut invoquer une conviction religieuse pour contester une question au programme", "L'article 12 de la Charte protège les enseignements de toute contestation de ce type."),
  Q("Selon la Charte, qu'offre la laïcité de l'École aux élèves ?", ["Une religion commune", "Les conditions pour forger leur personnalité, exercer leur libre arbitre et faire l'apprentissage de la citoyenneté", "Un enseignement religieux obligatoire", "Le droit de refuser les cours"], "Les conditions pour forger leur personnalité, exercer leur libre arbitre et faire l'apprentissage de la citoyenneté", "La laïcité protège les élèves de tout prosélytisme et de toute pression."),
]),
notion('E4-1', 1, I, 'emc-manifestation', [
  Q("Que faut-il faire avant d'organiser une manifestation sur la voie publique ?", ["Rien", "La déclarer à la préfecture ou à la mairie", "Obtenir l'accord du président", "Payer une taxe"], "La déclarer à la préfecture ou à la mairie", "Les manifestations sont soumises à déclaration préalable ; l'autorité peut les interdire en cas de risque pour l'ordre public."),
  Q("La liberté de manifester est…", ["absolue", "garantie mais encadrée pour préserver l'ordre public", "interdite", "réservée aux syndicats"], "garantie mais encadrée pour préserver l'ordre public", "Comme toute liberté, elle s'exerce dans le respect de la loi et des droits d'autrui."),
  Q("Quelle liberté permet aux citoyens de se réunir publiquement pour exprimer une opinion ?", ["La liberté de réunion et de manifestation", "La liberté de commerce", "La liberté de culte uniquement", "La liberté d'entreprendre"], "La liberté de réunion et de manifestation", "Elle participe à l'expression des opinions dans une démocratie."),
]),
notion('E5-1', 0, I, 'emc-ivg-constitution', [
  N("En quelle année la liberté de recourir à l'IVG est-elle inscrite dans la Constitution ?", 2024, "La révision du 8 mars 2024 inscrit à l'article 34 la « liberté garantie à la femme » de recourir à l'IVG."),
  Q("Quelle ministre porte la loi de 1975 dépénalisant l'IVG ?", ["Simone Veil", "Gisèle Halimi", "Françoise Giroud", "Yvette Roudy"], "Simone Veil", "Simone Veil défend la loi devant l'Assemblée nationale en novembre 1974 ; elle est promulguée en janvier 1975."),
  Q("Quelle avocate défend en 1972, au procès de Bobigny, une jeune fille poursuivie pour avortement ?", ["Gisèle Halimi", "Simone Veil", "Olympe de Gouges", "Louise Weiss"], "Gisèle Halimi", "Le procès de Bobigny contribue à l'évolution de la loi."),
]),
notion('E5-1', 0, I, 'emc-inegalites-persistantes', [
  Q("Malgré l'égalité des droits, quelle inégalité persiste entre femmes et hommes ?", ["Le droit de vote", "Des écarts de salaire et de partage des tâches domestiques", "L'accès à l'école", "Le droit d'ouvrir un compte bancaire"], "Des écarts de salaire et de partage des tâches domestiques", "L'égalité des droits ne suffit pas toujours à garantir l'égalité de fait."),
  Q("Quel outil oblige les entreprises d'au moins 50 salariés à mesurer les écarts de salaire entre femmes et hommes ?", ["L'index de l'égalité professionnelle", "Le SMIC", "Le code de la route", "La TVA"], "L'index de l'égalité professionnelle", "Depuis 2019, ces entreprises publient chaque année un index noté sur 100."),
  Q("Que dit la loi sur l'égalité de rémunération entre femmes et hommes ?", ["Elle n'existe pas", "À travail égal ou de valeur égale, salaire égal", "Les hommes doivent être mieux payés", "Elle ne concerne que les fonctionnaires"], "À travail égal ou de valeur égale, salaire égal", "Le principe figure dans le Code du travail depuis 1972."),
]),
notion('E5-1', 1, I, 'emc-sanctions-discrimination', [
  Q("Quelle peine maximale prévoit le Code pénal pour une discrimination commise par une personne ?", ["Une simple amende de 38 €", "3 ans d'emprisonnement et 45 000 € d'amende", "La prison à vie", "Aucune peine"], "3 ans d'emprisonnement et 45 000 € d'amende", "Les peines sont aggravées lorsque la discrimination est commise par une personne dépositaire de l'autorité publique."),
  Q("La saisine du Défenseur des droits est…", ["payante", "gratuite", "réservée aux avocats", "impossible pour un mineur"], "gratuite", "Toute personne, y compris un enfant, peut saisir gratuitement le Défenseur des droits."),
  Q("Comment appelle-t-on une méthode qui consiste à envoyer de fausses candidatures comparables pour détecter une discrimination ?", ["Le testing", "Le casting", "Le coaching", "Le profiling"], "Le testing", "Le testing est reconnu comme moyen de preuve de la discrimination."),
]),
notion('E5-2', 0, I, 'emc-solidarite-generations', [
  Q("Comment appelle-t-on la solidarité par laquelle les actifs financent les retraites des personnes âgées ?", ["La solidarité intergénérationnelle", "La solidarité internationale", "La charité privée", "L'épargne individuelle"], "La solidarité intergénérationnelle", "Le système de retraite par répartition repose sur un pacte entre générations."),
  Q("Comment appelle-t-on une solidarité organisée et financée par l'État pour tous ?", ["La solidarité nationale", "La solidarité familiale", "Le mécénat", "Le bénévolat"], "La solidarité nationale", "Elle s'appuie sur les impôts et les cotisations sociales."),
  Q("Quelle journée de solidarité les salariés effectuent-ils depuis 2004 au profit des personnes âgées et handicapées ?", ["Une journée de travail supplémentaire non rémunérée", "Un jour de grève", "Un jour férié supplémentaire", "Une journée de don du sang"], "Une journée de travail supplémentaire non rémunérée", "Créée après la canicule de 2003, elle finance l'autonomie des personnes âgées et handicapées."),
]),
notion('E5-2', 1, I, 'emc-echelles-solidarite', [
  Q("Quel organisme communal gère l'aide sociale de proximité ?", ["Le centre communal d'action sociale (CCAS)", "La préfecture", "La CAF nationale", "Le Conseil d'État"], "Le centre communal d'action sociale (CCAS)", "Le CCAS accompagne les habitants en difficulté de la commune."),
  Q("Quelle collectivité est chargée de l'aide sociale à l'enfance (ASE) ?", ["La commune", "Le département", "La région", "L'Union européenne"], "Le département", "Le département est le chef de file de l'action sociale : ASE, RSA, autonomie des personnes âgées."),
  Q("Quel fonds européen soutient l'emploi et l'inclusion sociale ?", ["Le Fonds social européen (FSE+)", "La Banque centrale européenne", "Le budget de l'OTAN", "Le Fonds monétaire international"], "Le Fonds social européen (FSE+)", "La solidarité s'exerce aussi à l'échelle européenne."),
]),
notion('E4-2', 0, I, 'emc-missions-armees', [
  Q("Quelles sont les grandes fonctions stratégiques de la défense française ?", ["Uniquement attaquer d'autres pays", "Connaissance-anticipation, prévention, dissuasion, protection, intervention", "Seulement la protection des frontières", "La police municipale"], "Connaissance-anticipation, prévention, dissuasion, protection, intervention", "Le Livre blanc et les revues stratégiques définissent ces fonctions."),
  Q("Quelle opération mobilise des militaires pour protéger le territoire national depuis 2015 ?", ["L'opération Barkhane", "L'opération Sentinelle", "L'opération Serval", "Le plan Orsec"], "L'opération Sentinelle", "Lancée après les attentats de janvier 2015, elle déploie des soldats sur le territoire."),
  Q("Comment appelle-t-on les citoyens volontaires qui renforcent ponctuellement les armées et les forces de sécurité ?", ["Les réservistes", "Les mercenaires", "Les conscrits obligatoires", "Les préfets"], "Les réservistes", "Les réserves opérationnelles regroupent des volontaires formés, mobilisables en renfort."),
]),
notion('E4-2', 1, I, 'emc-desinformation-ingerence', [
  Q("Quel service de l'État lutte contre les ingérences numériques étrangères (manipulations de l'information) ?", ["Viginum", "L'Insee", "Météo-France", "La Poste"], "Viginum", "Créé en 2021, Viginum détecte les campagnes de manipulation de l'information venues de l'étranger."),
  Q("Pourquoi la désinformation menace-t-elle la démocratie ?", ["Elle améliore le débat", "Elle fausse le jugement des citoyens et peut influencer les élections", "Elle n'a aucun effet", "Elle protège les institutions"], "Elle fausse le jugement des citoyens et peut influencer les élections", "Un débat démocratique suppose une information fiable et pluraliste."),
  Q("Quelle loi de 2018 permet de saisir le juge contre la diffusion massive de fausses informations en période électorale ?", ["La loi relative à la lutte contre la manipulation de l'information", "La loi Gayssot", "La loi de 1881 seule", "La loi Ferry"], "La loi relative à la lutte contre la manipulation de l'information", "Elle permet un référé en période électorale contre les fausses informations diffusées massivement."),
]),
notion('E3-1', 0, I, 'emc-conseil-constitutionnel', [
  N("Combien de membres nommés compte le Conseil constitutionnel ?", 9, "Neuf membres sont nommés pour 9 ans (3 par le président, 3 par le président de l'Assemblée, 3 par le président du Sénat) ; les anciens présidents en sont membres de droit."),
  Q("Pour combien d'années les membres du Conseil constitutionnel sont-ils nommés ?", ["5 ans", "6 ans", "9 ans", "À vie"], "9 ans", "Leur mandat de 9 ans n'est pas renouvelable, ce qui garantit leur indépendance."),
  Q("Quel autre rôle le Conseil constitutionnel joue-t-il, en plus du contrôle des lois ?", ["Il nomme les ministres", "Il veille à la régularité des élections nationales", "Il vote le budget", "Il juge les crimes"], "Il veille à la régularité des élections nationales", "Il proclame les résultats de l'élection présidentielle et des référendums, et juge le contentieux électoral."),
]),
notion('E3-1', 0, I, 'emc-dissolution-censure', [
  Q("Qui peut dissoudre l'Assemblée nationale ?", ["Le Premier ministre", "Le président de la République", "Le président du Sénat", "Le Conseil constitutionnel"], "Le président de la République", "L'article 12 permet au président de dissoudre l'Assemblée ; de nouvelles élections législatives ont alors lieu."),
  Q("Que se passe-t-il si une motion de censure est adoptée par l'Assemblée nationale ?", ["Le président démissionne", "Le gouvernement doit démissionner", "Le Sénat est dissous", "Rien"], "Le gouvernement doit démissionner", "La motion de censure met en jeu la responsabilité du gouvernement devant l'Assemblée."),
  Q("Après une dissolution, combien de temps le président doit-il attendre avant de pouvoir dissoudre à nouveau ?", ["Six mois", "Un an", "Deux ans", "Cinq ans"], "Un an", "Il ne peut être procédé à une nouvelle dissolution dans l'année qui suit les élections."),
]),
notion('E3-1', 0, I, 'emc-modes-scrutin', [
  Q("Quel mode de scrutin est utilisé pour l'élection présidentielle ?", ["Proportionnel", "Majoritaire à deux tours", "Tirage au sort", "Majoritaire à un tour"], "Majoritaire à deux tours", "Si aucun candidat n'obtient la majorité absolue au premier tour, les deux premiers s'affrontent au second."),
  Q("Quel mode de scrutin attribue les sièges en fonction du pourcentage de voix obtenues par chaque liste ?", ["Le scrutin majoritaire", "Le scrutin proportionnel", "Le scrutin censitaire", "Le scrutin indirect"], "Le scrutin proportionnel", "La proportionnelle est utilisée notamment pour les élections européennes."),
  Q("Le vote blanc est-il compté dans les suffrages exprimés en France ?", ["Oui", "Non, il est comptabilisé à part mais pas parmi les suffrages exprimés", "Il compte double", "Il est interdit"], "Non, il est comptabilisé à part mais pas parmi les suffrages exprimés", "Depuis 2014, les votes blancs sont décomptés séparément des nuls, sans être des suffrages exprimés."),
]),
notion('E3-1', 0, I, 'emc-revision-constitution', [
  Q("Comment la Constitution peut-elle être révisée, selon l'article 89 ?", ["Par simple décret", "Par référendum ou par le Parlement réuni en Congrès à la majorité des trois cinquièmes", "Par le Conseil constitutionnel seul", "Par le président seul"], "Par référendum ou par le Parlement réuni en Congrès à la majorité des trois cinquièmes", "Le projet doit d'abord être voté dans les mêmes termes par les deux assemblées."),
  Q("Où se réunit le Congrès (Assemblée nationale et Sénat réunis) ?", ["À l'Élysée", "À Versailles", "Au Palais-Bourbon", "À Matignon"], "À Versailles", "Le Congrès se réunit au château de Versailles."),
  Q("Quelle partie de la Constitution ne peut faire l'objet d'aucune révision ?", ["La durée du mandat présidentiel", "La forme républicaine du gouvernement", "Le nombre de députés", "Le nom des ministères"], "La forme républicaine du gouvernement", "L'article 89 interdit de réviser la forme républicaine du gouvernement."),
]),
notion('E3-1', 1, I, 'emc-principes-republique', [
  Q("Dans quel article de la Constitution le principe de laïcité est-il inscrit ?", ["L'article 1er", "L'article 16", "L'article 49", "L'article 89"], "L'article 1er", "L'article 1er déclare la France « République indivisible, laïque, démocratique et sociale »."),
  Q("Quel principe implique que la loi est la même pour tous sur tout le territoire ?", ["L'égalité devant la loi", "La décentralisation", "Le fédéralisme", "La subsidiarité"], "L'égalité devant la loi", "L'article 1er assure l'égalité devant la loi de tous les citoyens sans distinction d'origine, de race ou de religion."),
  Q("La langue de la République est…", ["l'anglais", "le français", "le latin", "toute langue régionale"], "le français", "L'article 2 de la Constitution l'affirme ; les langues régionales appartiennent au patrimoine de la France (article 75-1)."),
]),
notion('E3-2', 0, I, 'emc-independance-medias', [
  Q("Pourquoi la concentration des médias entre les mains de quelques propriétaires pose-t-elle question ?", ["Elle augmente le pluralisme", "Elle peut menacer le pluralisme et l'indépendance éditoriale", "Elle n'a aucun effet", "Elle est interdite"], "Elle peut menacer le pluralisme et l'indépendance éditoriale", "Le pluralisme des courants d'expression est un objectif de valeur constitutionnelle."),
  Q("Qu'est-ce que le secret des sources des journalistes ?", ["L'obligation de révéler ses informateurs", "La protection de l'identité des personnes qui informent les journalistes", "Le droit de mentir", "Une règle de politesse"], "La protection de l'identité des personnes qui informent les journalistes", "Il est protégé par la loi de 1881 (modifiée en 2010) ; c'est une condition de la liberté d'informer."),
  Q("Comment appelle-t-on l'organisation qui classe chaque année les pays selon la liberté de la presse ?", ["Reporters sans frontières", "Amnesty International", "La Croix-Rouge", "Médecins sans frontières"], "Reporters sans frontières", "RSF publie le classement mondial de la liberté de la presse."),
]),
notion('E3-2', 1, I, 'emc-biais-cognitifs', [
  Q("Comment appelle-t-on la tendance à privilégier les informations qui confirment ce que l'on pense déjà ?", ["Le biais de confirmation", "L'esprit critique", "La neutralité", "Le pluralisme"], "Le biais de confirmation", "Ce biais rend plus vulnérable aux fausses informations qui vont dans le sens de nos opinions."),
  Q("Quelle méthode aide à vérifier l'origine d'une photo trouvée en ligne ?", ["La recherche d'image inversée", "L'augmentation de la luminosité", "Le partage immédiat", "La lecture des commentaires"], "La recherche d'image inversée", "Elle permet de retrouver la première publication d'une image et de repérer un détournement."),
  Q("Qu'est-ce qu'un « deepfake » ?", ["Une vidéo ou un son truqué grâce à l'intelligence artificielle", "Une enquête approfondie", "Un média public", "Une émission de radio"], "Une vidéo ou un son truqué grâce à l'intelligence artificielle", "Les hypertrucages font dire ou faire à une personne ce qu'elle n'a jamais dit ou fait."),
]),
notion('E3-3', 0, I, 'emc-histoire-syndicats', [
  N("En quelle année la loi Waldeck-Rousseau autorise-t-elle les syndicats ?", 1884, "La loi du 21 mars 1884 légalise les syndicats professionnels."),
  Q("Quel texte reconnaît le droit syndical à valeur constitutionnelle ?", ["La DDHC de 1789", "Le préambule de la Constitution de 1946", "Le Code civil", "La loi de 1905"], "Le préambule de la Constitution de 1946", "« Tout homme peut défendre ses droits et ses intérêts par l'action syndicale et adhérer au syndicat de son choix. »"),
  Q("Quelle loi de 1864 supprime le délit de coalition et rend possible la grève ?", ["La loi Ollivier", "La loi Le Chapelier", "La loi Ferry", "La loi Falloux"], "La loi Ollivier", "La loi Ollivier (1864) abolit le délit de coalition ; la loi Le Chapelier (1791) l'avait interdit."),
]),
notion('E3-3', 0, I, 'emc-partis-financement', [
  Q("Comment les partis politiques sont-ils notamment financés en France ?", ["Par des dons illimités d'entreprises", "Par une aide publique proportionnelle à leurs résultats et par les dons encadrés de particuliers", "Uniquement par la publicité", "Par la vente de produits"], "Par une aide publique proportionnelle à leurs résultats et par les dons encadrés de particuliers", "Les dons des entreprises aux partis sont interdits depuis 1995."),
  Q("Quel article de la Constitution reconnaît que les partis « concourent à l'expression du suffrage » ?", ["L'article 4", "L'article 16", "L'article 34", "L'article 49"], "L'article 4", "L'article 4 consacre le pluralisme politique."),
  Q("Le pluralisme politique signifie…", ["l'existence d'un parti unique", "la libre existence de plusieurs partis et courants d'opinion", "l'interdiction des partis", "le vote obligatoire"], "la libre existence de plusieurs partis et courants d'opinion", "Le pluralisme est une condition de la démocratie."),
]),
notion('E3-1', 0, I, 'emc-abstention', [
  Q("Qu'est-ce que l'abstention ?", ["Le fait de voter blanc", "Le fait de ne pas aller voter", "Un vote nul", "Un vote par procuration"], "Le fait de ne pas aller voter", "Le taux d'abstention mesure la part des inscrits qui ne votent pas."),
  Q("Qu'est-ce qu'un vote par procuration ?", ["Un vote par Internet", "Confier à un autre électeur le soin de voter à sa place", "Un vote obligatoire", "Un vote au Sénat"], "Confier à un autre électeur le soin de voter à sa place", "Un électeur absent peut donner procuration à un autre électeur."),
  Q("Pourquoi une forte abstention pose-t-elle question en démocratie ?", ["Elle renforce la représentativité", "Elle peut affaiblir la légitimité des élus", "Elle est interdite", "Elle n'a aucun effet"], "Elle peut affaiblir la légitimité des élus", "Des élus choisis par une minorité d'inscrits peuvent voir leur légitimité contestée."),
]),
notion('E4-1', 0, I, 'emc-garde-a-vue', [
  Q("Quel droit a une personne placée en garde à vue ?", ["Aucun", "Être assistée par un avocat et garder le silence", "Choisir son enquêteur", "Rentrer chez elle quand elle veut"], "Être assistée par un avocat et garder le silence", "La réforme de 2011 renforce les droits : avocat, droit de se taire, informer un proche, examen médical."),
  Q("Quelle est en principe la durée maximale d'une garde à vue de droit commun (renouvellement compris) ?", ["24 heures", "48 heures", "7 jours", "1 mois"], "48 heures", "24 heures renouvelables une fois ; des durées plus longues existent pour le terrorisme ou la criminalité organisée."),
  Q("Qui contrôle la garde à vue ?", ["Le maire", "Le procureur de la République", "Le préfet", "Le directeur d'école"], "Le procureur de la République", "Le procureur, magistrat du parquet, contrôle la mesure et peut la prolonger."),
]),
notion('E4-1', 1, I, 'emc-cedh', [
  Q("Où siège la Cour européenne des droits de l'homme ?", ["Bruxelles", "Strasbourg", "Luxembourg", "La Haye"], "Strasbourg", "La CEDH applique la Convention européenne des droits de l'homme (1950)."),
  Q("De quelle organisation dépend la Cour européenne des droits de l'homme ?", ["L'Union européenne", "Le Conseil de l'Europe", "L'ONU", "L'OTAN"], "Le Conseil de l'Europe", "Le Conseil de l'Europe (46 États) est distinct de l'Union européenne (27 États)."),
  Q("Un citoyen français peut-il saisir la Cour européenne des droits de l'homme ?", ["Non, jamais", "Oui, après avoir épuisé les recours devant les juridictions françaises", "Oui, directement sans procès en France", "Seulement par l'intermédiaire du président"], "Oui, après avoir épuisé les recours devant les juridictions françaises", "Le recours individuel est ouvert une fois les voies de recours nationales épuisées."),
]),
notion('E5-1', 1, I, 'emc-accessibilite', [
  Q("Que prévoit la loi de 2005 pour les bâtiments recevant du public ?", ["Rien", "Leur mise en accessibilité aux personnes handicapées", "Leur fermeture", "Leur privatisation"], "Leur mise en accessibilité aux personnes handicapées", "La loi de 2005 impose l'accessibilité des établissements recevant du public."),
  Q("Quel document organise la scolarité d'un élève en situation de handicap ?", ["Le projet personnalisé de scolarisation (PPS)", "Le livret de famille", "Le cahier de textes", "Le règlement intérieur"], "Le projet personnalisé de scolarisation (PPS)", "Le PPS est établi par la MDPH et précise les aménagements et accompagnements nécessaires."),
  Q("Quelle structure départementale évalue les besoins des personnes handicapées ?", ["La MDPH (maison départementale des personnes handicapées)", "La CAF", "La mairie", "Le rectorat seul"], "La MDPH (maison départementale des personnes handicapées)", "La MDPH reconnaît le handicap et attribue aides et compensations."),
]),
notion('E3-1', 0, I, 'emc-cese', [
  Q("Quelle est la « troisième assemblée » de la République, qui représente la société civile ?", ["Le Conseil d'État", "Le Conseil économique, social et environnemental (CESE)", "La Cour des comptes", "Le Conseil constitutionnel"], "Le Conseil économique, social et environnemental (CESE)", "Le CESE conseille le gouvernement et le Parlement ; il peut organiser des conventions citoyennes."),
  Q("Quelle convention citoyenne tirée au sort a travaillé sur le climat en 2019-2020 ?", ["La Convention citoyenne pour le climat", "La Convention de Genève", "Le Congrès de Versailles", "Le Grenelle de l'environnement"], "La Convention citoyenne pour le climat", "150 citoyens tirés au sort ont fait des propositions pour réduire les émissions de gaz à effet de serre."),
  Q("Quelle institution contrôle le bon usage de l'argent public ?", ["La Cour des comptes", "Le Sénat", "La Banque de France", "Le CESE"], "La Cour des comptes", "La Cour des comptes contrôle les comptes publics et évalue les politiques publiques."),
  Q("Quel rôle a principalement le CESE ?", ["Voter les lois", "Rendre des avis consultatifs", "Juger les ministres", "Élire le président"], "Rendre des avis consultatifs", "Le CESE éclaire les décisions publiques, sans pouvoir législatif."),
]),
notion('E4-1', 1, I, 'emc-vie-privee', [
  Q("Quel règlement européen protège les données personnelles depuis 2018 ?", ["Le RGPD", "Le traité de Lisbonne", "Le Code civil", "La loi 1901"], "Le RGPD", "Le règlement général sur la protection des données s'applique dans toute l'Union européenne."),
  Q("À partir de quel âge, en France, un mineur peut-il consentir seul au traitement de ses données par un réseau social ?", ["13 ans", "15 ans", "16 ans", "18 ans"], "15 ans", "La France a fixé cette « majorité numérique » à 15 ans ; en dessous, l'accord d'un parent est requis."),
  Q("Quel droit permet de demander la suppression de données personnelles en ligne ?", ["Le droit à l'effacement (droit à l'oubli)", "Le droit de grève", "Le droit d'asile", "Le droit de vote"], "Le droit à l'effacement (droit à l'oubli)", "Le RGPD reconnaît le droit d'obtenir l'effacement de ses données dans certains cas."),
]),
notion('E3-3', 1, I, 'emc-formes-engagement', [
  Q("Comment appelle-t-on la participation des habitants à la vie de leur quartier, par exemple dans un conseil de quartier ?", ["La démocratie participative", "La monarchie", "La centralisation", "La dictature"], "La démocratie participative", "Elle associe les citoyens aux décisions entre deux élections."),
  Q("Quelle instance permet aux élèves de collège de s'exprimer sur la vie de l'établissement ?", ["Le conseil de la vie collégienne (CVC)", "Le Conseil constitutionnel", "Le conseil municipal", "Le CESE"], "Le conseil de la vie collégienne (CVC)", "Le CVC associe élèves, personnels et parents à la vie du collège."),
  Q("Que permet le budget participatif mis en place par certaines communes ?", ["Aux habitants de proposer et de choisir des projets financés par la commune", "D'augmenter les impôts", "D'élire le maire", "De supprimer le conseil municipal"], "Aux habitants de proposer et de choisir des projets financés par la commune", "C'est un outil de démocratie participative locale."),
]),
notion('E4-1', 0, I, 'emc-decentralisation', [
  N("En quelle année les lois Defferre lancent-elles la décentralisation ?", 1982, "Les lois Defferre de 1982 transfèrent des compétences de l'État aux collectivités territoriales."),
  Q("Qu'est-ce que la décentralisation ?", ["Le renforcement du pouvoir central", "Le transfert de compétences de l'État vers des collectivités élues", "La suppression des communes", "Le fédéralisme"], "Le transfert de compétences de l'État vers des collectivités élues", "La République est décentralisée depuis la révision constitutionnelle de 2003 (article 1er)."),
  Q("Qui représente l'État dans le département ?", ["Le président du conseil départemental", "Le préfet", "Le maire du chef-lieu", "Le député"], "Le préfet", "Le préfet représente l'État et contrôle la légalité des actes des collectivités."),
]),
notion('E5-2', 1, I, 'emc-solidarite-internationale', [
  Q("Quelle organisation humanitaire internationale est née de l'initiative d'Henri Dunant en 1863 ?", ["La Croix-Rouge", "Médecins sans frontières", "L'UNICEF", "Amnesty International"], "La Croix-Rouge", "Le Comité international de la Croix-Rouge porte secours aux victimes des conflits."),
  Q("Quelle agence de l'ONU est chargée de défendre les droits des enfants dans le monde ?", ["L'UNICEF", "L'UNESCO", "L'OMS", "La FAO"], "L'UNICEF", "L'UNICEF agit pour la santé, l'éducation et la protection des enfants."),
  Q("Comment appelle-t-on l'aide financière apportée par les États riches aux pays en développement ?", ["L'aide publique au développement", "Le plan Orsec", "La dette", "Le protectionnisme"], "L'aide publique au développement", "C'est une forme de solidarité internationale organisée par les États."),
]),
notion('E4-2', 1, I, 'emc-cybersecurite', [
  Q("Quelle agence de l'État est chargée de la sécurité des systèmes d'information ?", ["L'ANSSI", "L'Insee", "L'Arcom", "La CAF"], "L'ANSSI", "L'Agence nationale de la sécurité des systèmes d'information protège les administrations et les infrastructures vitales."),
  Q("Quelle pratique renforce la sécurité d'un compte en ligne ?", ["Utiliser le même mot de passe partout", "Activer la double authentification et utiliser des mots de passe solides et différents", "Partager son mot de passe avec ses amis", "Noter son mot de passe sur son écran"], "Activer la double authentification et utiliser des mots de passe solides et différents", "La double authentification ajoute une vérification (code reçu, application) en plus du mot de passe."),
  Q("Comment appelle-t-on un logiciel malveillant qui chiffre les données et exige une rançon ?", ["Un rançongiciel", "Un antivirus", "Un tableur", "Un navigateur"], "Un rançongiciel", "Des hôpitaux et des collectivités ont été victimes de rançongiciels (ransomwares)."),
]),
notion('E3-1', 0, I, 'emc-navette-parlementaire', [
  Q("Comment appelle-t-on l'examen successif d'un texte de loi par l'Assemblée nationale et le Sénat ?", ["La navette parlementaire", "La motion de censure", "Le référendum", "La dissolution"], "La navette parlementaire", "Le texte passe d'une assemblée à l'autre jusqu'à adoption dans les mêmes termes."),
  Q("En cas de désaccord persistant entre les deux assemblées, qui peut avoir le dernier mot ?", ["Le Sénat", "L'Assemblée nationale, à la demande du Gouvernement", "Le Conseil constitutionnel", "Le président du Sénat"], "L'Assemblée nationale, à la demande du Gouvernement", "Après une commission mixte paritaire, le Gouvernement peut demander à l'Assemblée de statuer définitivement."),
  Q("Quelle assemblée représente les collectivités territoriales ?", ["L'Assemblée nationale", "Le Sénat", "Le CESE", "Le Conseil d'État"], "Le Sénat", "L'article 24 de la Constitution confie au Sénat la représentation des collectivités territoriales."),
]),
]
