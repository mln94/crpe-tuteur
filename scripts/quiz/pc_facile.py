from qlib import Q, N, C, notion
F = 'facile'
NOTIONS = [
notion('P-1', 0, F, 'pc-etats-matiere', [
  Q("Quels sont les trois principaux états de la matière ?", ["Solide, liquide, gazeux", "Chaud, tiède, froid", "Lourd, léger, moyen", "Dur, mou, fluide"], "Solide, liquide, gazeux", "La même substance (l'eau) peut exister sous ces trois états : glace, eau liquide, vapeur."),
  Q("Quel état de la matière a une forme propre ?", ["Le liquide", "Le solide", "Le gaz", "Aucun"], "Le solide", "Un liquide prend la forme de son récipient ; un gaz occupe tout l'espace disponible."),
  Q("Quel état de la matière est compressible ?", ["Le solide", "Le liquide", "Le gaz", "Aucun"], "Le gaz", "Les particules d'un gaz sont éloignées : on peut le comprimer, comme l'air d'une pompe à vélo."),
]),
notion('P-1', 0, F, 'pc-changements-etat', [
  Q("Comment appelle-t-on le passage de l'état solide à l'état liquide ?", ["La solidification", "La fusion", "La vaporisation", "La condensation"], "La fusion", "La glace fond : c'est une fusion. Le passage inverse est la solidification."),
  Q("Comment appelle-t-on le passage de l'état gazeux à l'état liquide ?", ["La fusion", "La liquéfaction (condensation liquide)", "La sublimation", "La vaporisation"], "La liquéfaction (condensation liquide)", "La buée sur une vitre froide résulte de la liquéfaction de la vapeur d'eau de l'air."),
  Q("Comment appelle-t-on le passage direct de l'état solide à l'état gazeux ?", ["La fusion", "La sublimation", "La solidification", "L'ébullition"], "La sublimation", "La neige carbonique (CO₂ solide) se sublime à température ambiante."),
]),
notion('P-1', 0, F, 'pc-temperatures-eau', [
  N("À quelle température (en °C) l'eau pure se solidifie-t-elle, à la pression atmosphérique normale ?", 0, "L'eau pure gèle et la glace fond à 0 °C : la température reste constante pendant le changement d'état."),
  N("À quelle température (en °C) l'eau pure bout-elle, à la pression atmosphérique normale ?", 100, "Pendant l'ébullition, la température reste constante à 100 °C."),
  Q("Pendant la fusion de la glace pure, la température…", ["augmente régulièrement", "reste constante à 0 °C", "diminue", "dépasse 100 °C"], "reste constante à 0 °C", "Un corps pur change d'état à température constante : c'est un palier."),
]),
notion('P-1', 0, F, 'pc-conservation-masse', [
  Q("Lors de la fusion de 200 g de glace, quelle masse d'eau liquide obtient-on ?", ["Moins de 200 g", "200 g", "Plus de 200 g", "On ne peut pas savoir"], "200 g", "La masse se conserve lors d'un changement d'état."),
  Q("Lors de la solidification de l'eau, le volume…", ["reste identique", "augmente", "diminue", "devient nul"], "augmente", "La glace occupe plus de volume que l'eau liquide : une bouteille pleine peut éclater au congélateur."),
  Q("Pourquoi un glaçon flotte-t-il sur l'eau ?", ["Il est plus lourd", "La glace est moins dense que l'eau liquide", "Il contient de l'air seulement", "Par hasard"], "La glace est moins dense que l'eau liquide", "Sa masse volumique (environ 0,92 g/cm³) est inférieure à celle de l'eau (1 g/cm³)."),
]),
notion('P-1', 0, F, 'pc-masse-volumique', [
  N("Quelle est la masse (en kg) de 1 litre d'eau ?", 1, "La masse volumique de l'eau est d'environ 1 kg/L, soit 1 g/cm³."),
  N("Quelle est la masse (en g) de 250 mL d'eau ?", 250, "1 mL d'eau a une masse d'environ 1 g, donc 250 mL ont une masse de 250 g."),
  Q("Un objet de masse volumique 0,8 g/cm³ placé dans l'eau…", ["coule", "flotte", "se dissout", "explose"], "flotte", "Un objet moins dense que l'eau (1 g/cm³) flotte."),
]),
notion('P-1', 0, F, 'pc-melanges', [
  Q("Comment appelle-t-on un mélange dans lequel on ne distingue pas les constituants à l'œil nu ?", ["Un mélange hétérogène", "Un mélange homogène", "Un corps pur", "Un solide"], "Un mélange homogène", "L'eau sucrée est un mélange homogène ; l'eau boueuse, un mélange hétérogène."),
  Q("Quelle technique permet de séparer le sable de l'eau ?", ["La filtration", "L'évaporation seule", "La dissolution", "La fusion"], "La filtration", "Le filtre retient les particules solides ; le liquide qui passe est le filtrat."),
  Q("Comment récupérer le sel dissous dans de l'eau salée ?", ["Par filtration", "Par évaporation de l'eau", "Par décantation", "Par aimantation"], "Par évaporation de l'eau", "C'est le principe des marais salants."),
]),
notion('P-1', 0, F, 'pc-dissolution', [
  Q("Dans l'eau sucrée, comment appelle-t-on le sucre ?", ["Le solvant", "Le soluté", "La solution", "Le mélange hétérogène"], "Le soluté", "Le sucre (soluté) se dissout dans l'eau (solvant) pour former une solution."),
  Q("Lorsqu'on dissout 10 g de sel dans 100 g d'eau, quelle est la masse de la solution ?", ["100 g", "110 g", "90 g", "10 g"], "110 g", "La masse se conserve lors d'une dissolution : 100 + 10 = 110 g."),
  Q("Comment appelle-t-on une solution qui ne peut plus dissoudre de soluté ?", ["Une solution diluée", "Une solution saturée", "Un corps pur", "Un solvant"], "Une solution saturée", "Au-delà de la solubilité, le soluté ne se dissout plus et se dépose au fond."),
]),
notion('P-1', 0, F, 'pc-air', [
  N("Quel est le pourcentage approximatif de dioxygène dans l'air ?", 21, "L'air contient environ 78 % de diazote et 21 % de dioxygène."),
  Q("Quel gaz est le plus abondant dans l'air ?", ["Le dioxygène", "Le diazote", "Le dioxyde de carbone", "L'hydrogène"], "Le diazote", "Le diazote représente environ 78 % de l'air."),
  Q("L'air a-t-il une masse ?", ["Non", "Oui, environ 1,2 g par litre", "Seulement en altitude", "Seulement quand il fait froid"], "Oui, environ 1,2 g par litre", "Un ballon gonflé est plus lourd qu'un ballon dégonflé."),
]),
notion('P-1', 0, F, 'pc-atomes-molecules', [
  Q("De quoi la matière est-elle constituée à l'échelle microscopique ?", ["De cellules", "D'atomes et de molécules", "De cristaux uniquement", "De rien"], "D'atomes et de molécules", "Les molécules sont formées d'atomes liés entre eux."),
  Q("Combien d'atomes contient une molécule d'eau (H₂O) ?", ["Deux", "Trois", "Quatre", "Un"], "Trois", "Deux atomes d'hydrogène et un atome d'oxygène."),
  Q("Quel est le symbole chimique de l'oxygène ?", ["Ox", "O", "Og", "Oy"], "O", "H pour l'hydrogène, C pour le carbone, N pour l'azote, O pour l'oxygène."),
]),
notion('P-1', 1, F, 'pc-combustion', [
  Q("Quels sont les trois éléments nécessaires à une combustion (triangle du feu) ?", ["Eau, air, terre", "Combustible, comburant (dioxygène) et source de chaleur", "Bois, papier, carton", "Lumière, son, chaleur"], "Combustible, comburant (dioxygène) et source de chaleur", "Supprimer l'un des trois éteint le feu."),
  Q("Quel gaz est produit par la combustion du carbone ?", ["Le dioxygène", "Le dioxyde de carbone", "L'hydrogène", "L'azote"], "Le dioxyde de carbone", "Carbone + dioxygène → dioxyde de carbone."),
  Q("Quel réactif est indispensable à toute combustion dans l'air ?", ["Le diazote", "Le dioxygène", "L'eau", "Le CO₂"], "Le dioxygène", "Le dioxygène est le comburant : une bougie s'éteint sous un bocal quand il est consommé."),
]),
notion('P-1', 1, F, 'pc-test-co2', [
  Q("Quel réactif met en évidence le dioxyde de carbone ?", ["Le sulfate de cuivre", "L'eau de chaux, qui se trouble", "L'eau iodée", "Le papier pH"], "L'eau de chaux, qui se trouble", "L'eau de chaux devient trouble (blanchâtre) en présence de CO₂."),
  Q("Quel test met en évidence la présence d'eau ?", ["L'eau de chaux", "Le sulfate de cuivre anhydre, qui devient bleu", "L'allumette", "La flamme"], "Le sulfate de cuivre anhydre, qui devient bleu", "Le sulfate de cuivre anhydre, blanc, devient bleu au contact de l'eau."),
  Q("Quel test met en évidence le dioxygène ?", ["Une bûchette incandescente qui se rallume", "L'eau de chaux", "Le papier pH", "L'aimant"], "Une bûchette incandescente qui se rallume", "Le dioxygène ravive la combustion d'une bûchette incandescente."),
]),
notion('P-1', 1, F, 'pc-physique-chimique', [
  Q("Quelle transformation est chimique ?", ["La fonte du beurre", "La cuisson d'un œuf", "Le sucre qui se dissout", "L'eau qui gèle"], "La cuisson d'un œuf", "De nouvelles substances apparaissent : c'est une transformation chimique, irréversible ici."),
  Q("Qu'est-ce qui caractérise une transformation chimique ?", ["Un simple changement d'état", "Des réactifs disparaissent et de nouveaux produits se forment", "La masse diminue toujours", "Rien ne change"], "Des réactifs disparaissent et de nouveaux produits se forment", "La masse totale se conserve, mais les espèces chimiques changent."),
  Q("La rouille qui se forme sur le fer est…", ["une transformation physique", "une transformation chimique", "un changement d'état", "une dissolution"], "une transformation chimique", "Le fer réagit avec le dioxygène et l'eau pour former de la rouille."),
]),
notion('P-1', 1, F, 'pc-ph', [
  N("Quelle valeur de pH correspond à une solution neutre ?", 7, "pH < 7 : solution acide ; pH = 7 : neutre ; pH > 7 : basique."),
  Q("Le jus de citron (pH ≈ 2) est…", ["acide", "neutre", "basique", "salé"], "acide", "Plus le pH est petit, plus la solution est acide."),
  Q("Quel instrument ou papier permet de mesurer le pH ?", ["Le thermomètre", "Le papier pH ou le pH-mètre", "La balance", "Le voltmètre"], "Le papier pH ou le pH-mètre", "Le papier pH change de couleur selon l'acidité."),
]),
notion('P-1', 2, F, 'pc-soleil-etoile', [
  Q("Qu'est-ce que le Soleil ?", ["Une planète", "Une étoile", "Un satellite", "Une galaxie"], "Une étoile", "Le Soleil est une étoile qui produit sa propre lumière."),
  Q("Comment s'appelle notre galaxie ?", ["Andromède", "La Voie lactée", "La Grande Ourse", "Orion"], "La Voie lactée", "La Voie lactée contient des centaines de milliards d'étoiles."),
  Q("La Lune est…", ["une étoile", "le satellite naturel de la Terre", "une planète", "une comète"], "le satellite naturel de la Terre", "La Lune tourne autour de la Terre et réfléchit la lumière du Soleil."),
]),
notion('P-1', 2, F, 'pc-annee-lumiere', [
  Q("Qu'est-ce qu'une année-lumière ?", ["Une durée", "Une distance : celle parcourue par la lumière en un an", "Une vitesse", "Une masse"], "Une distance : celle parcourue par la lumière en un an", "Une année-lumière vaut environ 9 500 milliards de kilomètres."),
  Q("Pourquoi utilise-t-on l'année-lumière en astronomie ?", ["Parce que les distances sont immenses", "Parce que c'est plus joli", "Pour mesurer le temps", "Pour mesurer la masse des étoiles"], "Parce que les distances sont immenses", "L'étoile la plus proche du Soleil est à plus de 4 années-lumière."),
  Q("Combien de temps environ la lumière du Soleil met-elle pour atteindre la Terre ?", ["8 secondes", "8 minutes", "8 heures", "8 jours"], "8 minutes", "La lumière parcourt les 150 millions de kilomètres en environ 8 minutes 20 secondes."),
]),
notion('P-1', 2, F, 'pc-phases-lune', [
  Q("Pourquoi voit-on la Lune sous différentes formes (phases) ?", ["Elle change de taille", "Selon sa position, on voit une partie plus ou moins grande de sa face éclairée par le Soleil", "La Terre lui fait de l'ombre chaque jour", "Les nuages la cachent"], "Selon sa position, on voit une partie plus ou moins grande de sa face éclairée par le Soleil", "L'ombre de la Terre n'explique que les éclipses de Lune."),
  Q("Combien de temps dure environ un cycle complet des phases de la Lune ?", ["7 jours", "Environ 29,5 jours", "365 jours", "24 heures"], "Environ 29,5 jours", "C'est la lunaison, d'une nouvelle lune à la suivante."),
  Q("Que se passe-t-il lors d'une éclipse de Soleil ?", ["La Terre passe entre le Soleil et la Lune", "La Lune passe entre le Soleil et la Terre", "Le Soleil s'éteint", "La Lune s'éloigne"], "La Lune passe entre le Soleil et la Terre", "Lors d'une éclipse de Lune, c'est la Terre qui se place entre le Soleil et la Lune."),
]),
notion('P-2', 0, F, 'pc-vitesse-calcul', [
  N("Une voiture parcourt 120 km en 2 h. Quelle est sa vitesse moyenne (en km/h) ?", 60, "v = d / t = 120 / 2 = 60 km/h."),
  N("Un cycliste roule à 15 km/h pendant 3 h. Quelle distance parcourt-il (en km) ?", 45, "d = v × t = 15 × 3 = 45 km."),
  N("Un coureur parcourt 100 m en 10 s. Quelle est sa vitesse moyenne (en m/s) ?", 10, "v = 100 / 10 = 10 m/s."),
]),
notion('P-2', 0, F, 'pc-trajectoire', [
  Q("Quelle est la trajectoire de la valve d'une roue de vélo vue par le cycliste ?", ["Rectiligne", "Circulaire", "Elle ne bouge pas", "En zigzag"], "Circulaire", "Par rapport au vélo, la valve décrit un cercle."),
  Q("Un mouvement dont la trajectoire est une droite est dit…", ["circulaire", "rectiligne", "curviligne", "oscillant"], "rectiligne", "Une bille qui roule en ligne droite a un mouvement rectiligne."),
  Q("Un mouvement dont la vitesse ne change pas est dit…", ["accéléré", "uniforme", "ralenti", "circulaire"], "uniforme", "La vitesse reste constante ; il peut être rectiligne ou circulaire."),
]),
notion('P-2', 0, F, 'pc-relativite-mouvement', [
  Q("Un passager assis dans un train en marche est-il immobile ?", ["Oui, toujours", "Il est immobile par rapport au train mais en mouvement par rapport au quai", "Il est en mouvement par rapport à tout", "Non, jamais"], "Il est immobile par rapport au train mais en mouvement par rapport au quai", "Le mouvement dépend de l'objet de référence choisi (le référentiel)."),
  Q("Comment appelle-t-on l'objet par rapport auquel on décrit un mouvement ?", ["Le référentiel", "La trajectoire", "La vitesse", "La force"], "Le référentiel", "On précise toujours le référentiel : sol, train, Soleil…"),
  Q("Par rapport au Soleil, la Terre est…", ["immobile", "en mouvement", "toujours au même endroit", "en mouvement rectiligne"], "en mouvement", "La Terre tourne autour du Soleil (révolution) et sur elle-même (rotation)."),
]),
notion('P-2', 0, F, 'pc-conversion-vitesse', [
  N("Convertissez 72 km/h en m/s.", 20, "Pour passer des km/h aux m/s, on divise par 3,6 : 72 ÷ 3,6 = 20 m/s."),
  N("Convertissez 10 m/s en km/h.", 36, "Pour passer des m/s aux km/h, on multiplie par 3,6 : 10 × 3,6 = 36 km/h."),
  N("Combien de mètres parcourt-on en une heure à 1 m/s ?", 3600, "Une heure compte 3 600 secondes : 1 m/s × 3 600 s = 3 600 m, soit 3,6 km/h."),
]),
notion('P-2', 1, F, 'pc-poids-masse', [
  Q("Quelle est la différence entre la masse et le poids ?", ["Aucune", "La masse est une quantité de matière (kg) ; le poids est une force (N) due à l'attraction de la Terre", "Le poids se mesure en kg", "La masse change sur la Lune"], "La masse est une quantité de matière (kg) ; le poids est une force (N) due à l'attraction de la Terre", "Sur la Lune, la masse reste la même mais le poids est environ six fois plus faible."),
  Q("Quelle est l'unité de mesure d'une force ?", ["Le kilogramme", "Le newton", "Le mètre", "Le joule"], "Le newton", "Le poids, comme toute force, s'exprime en newtons (N)."),
  Q("Quel instrument mesure une force ?", ["La balance", "Le dynamomètre", "Le thermomètre", "Le chronomètre"], "Le dynamomètre", "La balance mesure une masse ; le dynamomètre, une force."),
]),
notion('P-2', 1, F, 'pc-calcul-poids', [
  N("Quel est le poids (en N) d'un objet de 2 kg sur Terre ? On prend g = 10 N/kg.", 20, "P = m × g = 2 × 10 = 20 N."),
  N("Un objet pèse 50 N sur Terre (g = 10 N/kg). Quelle est sa masse (en kg) ?", 5, "m = P / g = 50 / 10 = 5 kg."),
  Q("Sur la Lune, la masse d'un astronaute…", ["diminue", "reste la même", "augmente", "devient nulle"], "reste la même", "La masse ne dépend pas du lieu ; le poids, si."),
]),
notion('P-2', 1, F, 'pc-actions-mecaniques', [
  Q("Un aimant qui attire un clou exerce une action…", ["de contact", "à distance", "chimique", "thermique"], "à distance", "L'action magnétique, comme la gravitation, s'exerce à distance."),
  Q("Quand on pousse une porte, l'action exercée est…", ["à distance", "de contact", "magnétique", "nulle"], "de contact", "La main est en contact avec la porte."),
  Q("Quelle force fait tomber les objets vers le sol ?", ["La force magnétique", "Le poids (attraction de la Terre)", "Le vent", "La force électrique"], "Le poids (attraction de la Terre)", "La Terre attire tous les objets : c'est la gravitation."),
]),
notion('P-3', 0, F, 'pc-formes-energie', [
  Q("Quelle forme d'énergie possède un objet en mouvement ?", ["L'énergie cinétique", "L'énergie chimique", "L'énergie nucléaire", "L'énergie lumineuse"], "L'énergie cinétique", "L'énergie cinétique augmente avec la masse et surtout avec la vitesse."),
  Q("Quelle forme d'énergie est stockée dans les aliments et les carburants ?", ["Cinétique", "Chimique", "Lumineuse", "Électrique"], "Chimique", "Elle est libérée lors de réactions chimiques comme la combustion ou la respiration."),
  Q("Quelle forme d'énergie une lampe produit-elle principalement ?", ["Énergie lumineuse (et thermique)", "Énergie cinétique", "Énergie chimique", "Énergie nucléaire"], "Énergie lumineuse (et thermique)", "Une lampe convertit l'énergie électrique en énergie lumineuse, avec des pertes sous forme de chaleur."),
]),
notion('P-3', 0, F, 'pc-sources-energie', [
  Q("Laquelle de ces sources d'énergie est renouvelable ?", ["Le gaz naturel", "L'énergie hydraulique", "Le charbon", "L'uranium"], "L'énergie hydraulique", "Les barrages utilisent l'énergie de l'eau, qui se renouvelle grâce au cycle de l'eau."),
  Q("Quelle source d'énergie utilise une centrale nucléaire ?", ["Le vent", "L'uranium", "Le charbon", "Le soleil"], "L'uranium", "L'uranium est une ressource non renouvelable."),
  Q("Quel appareil convertit l'énergie lumineuse du Soleil en énergie électrique ?", ["Une éolienne", "Un panneau photovoltaïque", "Un barrage", "Une pile"], "Un panneau photovoltaïque", "Les panneaux solaires thermiques, eux, chauffent de l'eau."),
]),
notion('P-3', 0, F, 'pc-conversions', [
  Q("Quelle conversion d'énergie réalise une éolienne ?", ["Électrique → mécanique", "Mécanique (vent) → électrique", "Chimique → lumineuse", "Thermique → chimique"], "Mécanique (vent) → électrique", "Le vent fait tourner les pales, entraînant un alternateur qui produit de l'électricité."),
  Q("Quelle conversion réalise une pile ?", ["Chimique → électrique", "Électrique → chimique", "Lumineuse → électrique", "Mécanique → thermique"], "Chimique → électrique", "Une pile transforme l'énergie chimique de ses réactifs en énergie électrique."),
  Q("Quelle conversion réalise un moteur électrique ?", ["Électrique → mécanique (et thermique)", "Mécanique → électrique", "Chimique → lumineuse", "Thermique → électrique"], "Électrique → mécanique (et thermique)", "Une partie de l'énergie est perdue sous forme de chaleur."),
]),
notion('P-3', 1, F, 'pc-unites-energie', [
  Q("Quelle est l'unité d'énergie du système international ?", ["Le watt", "Le joule", "Le volt", "Le newton"], "Le joule", "L'énergie électrique consommée est souvent exprimée en kilowattheures (kWh)."),
  Q("Quelle est l'unité de puissance ?", ["Le joule", "Le watt", "L'ampère", "Le mètre"], "Le watt", "La puissance indique l'énergie transférée chaque seconde : 1 W = 1 J/s."),
  N("Un appareil de 1 000 W fonctionne pendant 2 h. Combien de kWh consomme-t-il ?", 2, "E = P × t = 1 kW × 2 h = 2 kWh."),
]),
notion('P-3', 1, F, 'pc-conservation-energie', [
  Q("Que dit le principe de conservation de l'énergie ?", ["L'énergie peut être créée", "L'énergie ne se crée ni ne disparaît : elle se transforme ou se transfère", "L'énergie disparaît toujours", "L'énergie n'existe pas"], "L'énergie ne se crée ni ne disparaît : elle se transforme ou se transfère", "Une partie de l'énergie est souvent « perdue » sous forme de chaleur, mais elle n'est pas détruite."),
  Q("Lors du freinage d'une voiture, en quoi l'énergie cinétique est-elle surtout transformée ?", ["En énergie lumineuse", "En énergie thermique (les freins chauffent)", "En énergie nucléaire", "En énergie chimique"], "En énergie thermique (les freins chauffent)", "Certaines voitures électriques récupèrent une partie de cette énergie (freinage régénératif)."),
  Q("Qu'est-ce que le rendement d'un appareil ?", ["Sa vitesse", "La part de l'énergie reçue qui est convertie en énergie utile", "Son prix", "Sa masse"], "La part de l'énergie reçue qui est convertie en énergie utile", "Une lampe LED a un bien meilleur rendement qu'une lampe à incandescence."),
]),
notion('P-3', 2, F, 'pc-circuit', [
  Q("Pour qu'une lampe s'allume, le circuit doit être…", ["ouvert", "fermé", "coupé", "sans générateur"], "fermé", "Le courant ne circule que dans une boucle fermée comprenant un générateur."),
  Q("Quel élément fournit l'énergie électrique dans un circuit simple ?", ["L'interrupteur", "Le générateur (pile)", "La lampe", "Le fil"], "Le générateur (pile)", "Le générateur fournit l'énergie ; les récepteurs (lampe, moteur) la convertissent."),
  Q("Quand l'interrupteur est ouvert…", ["la lampe brille", "le courant ne circule pas", "la pile se recharge", "la lampe brille plus fort"], "le courant ne circule pas", "Un interrupteur ouvert coupe la boucle du circuit."),
]),
notion('P-3', 2, F, 'pc-conducteurs-isolants', [
  Q("Lequel de ces matériaux est un bon conducteur électrique ?", ["Le plastique", "Le cuivre", "Le bois sec", "Le verre"], "Le cuivre", "Les métaux sont conducteurs ; les fils électriques sont en cuivre."),
  Q("Pourquoi les fils électriques sont-ils entourés de plastique ?", ["Pour la couleur", "Parce que le plastique est un isolant qui protège", "Pour conduire mieux", "Pour être plus lourds"], "Parce que le plastique est un isolant qui protège", "La gaine isolante évite les contacts dangereux et les courts-circuits."),
  Q("L'eau du robinet est-elle conductrice ?", ["Non, jamais", "Oui, elle conduit le courant, d'où le danger de l'électricité près de l'eau", "Seulement chaude", "Seulement gelée"], "Oui, elle conduit le courant, d'où le danger de l'électricité près de l'eau", "Il ne faut jamais manipuler un appareil électrique avec les mains mouillées."),
]),
notion('P-3', 2, F, 'pc-court-circuit', [
  Q("Qu'est-ce qu'un court-circuit ?", ["Un circuit très court", "Une liaison directe entre les bornes d'un générateur par un fil conducteur, sans récepteur", "Un circuit éteint", "Un circuit avec deux lampes"], "Une liaison directe entre les bornes d'un générateur par un fil conducteur, sans récepteur", "Le courant devient très intense : risque d'échauffement et d'incendie."),
  Q("Quel dispositif protège une installation contre les courts-circuits ?", ["Un interrupteur", "Un fusible ou un disjoncteur", "Une lampe", "Une prise multiple"], "Un fusible ou un disjoncteur", "Il coupe automatiquement le courant en cas d'intensité trop forte."),
  Q("À partir de quelle tension le courant du secteur (230 V) est-il dangereux pour l'être humain ?", ["Il n'est jamais dangereux", "Il est dangereux : on ne travaille jamais sur le secteur", "Seulement au-dessus de 1 000 V", "Seulement la nuit"], "Il est dangereux : on ne travaille jamais sur le secteur", "À l'école, on n'utilise que des piles et des générateurs de faible tension."),
]),
notion('P-3', 2, F, 'pc-serie-derivation', [
  Q("Dans un circuit en série avec deux lampes, si l'une grille…", ["l'autre continue de briller", "l'autre s'éteint aussi", "l'autre brille plus fort", "le générateur explose"], "l'autre s'éteint aussi", "En série, il n'y a qu'une seule boucle : le circuit est ouvert."),
  Q("Dans un montage en dérivation, si une lampe grille…", ["toutes s'éteignent", "les autres continuent de briller", "le circuit explose", "les autres brillent moins"], "les autres continuent de briller", "Chaque lampe est sur sa propre boucle : c'est pourquoi les installations domestiques sont en dérivation."),
  Q("Comment sont branchées les prises électriques d'une maison ?", ["En série", "En dérivation", "Sans fil", "Au hasard"], "En dérivation", "Chaque appareil reçoit ainsi la même tension et fonctionne indépendamment."),
]),
notion('P-3', 2, F, 'pc-unites-electriques', [
  Q("Quelle est l'unité de la tension électrique ?", ["L'ampère", "Le volt", "Le watt", "L'ohm"], "Le volt", "La tension se mesure en volts (V) avec un voltmètre."),
  Q("Quelle est l'unité de l'intensité du courant ?", ["Le volt", "L'ampère", "Le joule", "Le newton"], "L'ampère", "L'intensité se mesure en ampères (A) avec un ampèremètre."),
  Q("Comment branche-t-on un voltmètre pour mesurer la tension aux bornes d'une lampe ?", ["En série", "En dérivation", "Sans fil", "À la place de la pile"], "En dérivation", "Le voltmètre se branche en dérivation ; l'ampèremètre, en série."),
]),
notion('P-4', 0, F, 'pc-vitesse-lumiere', [
  Q("Quelle est la vitesse de la lumière dans le vide, environ ?", ["340 m/s", "300 000 km/s", "3 000 km/h", "1 000 m/s"], "300 000 km/s", "C'est la plus grande vitesse possible ; 340 m/s est la vitesse du son dans l'air."),
  Q("La lumière peut-elle se propager dans le vide ?", ["Oui", "Non", "Seulement la nuit", "Seulement dans l'espace proche"], "Oui", "La lumière des étoiles traverse le vide spatial jusqu'à nous."),
  Q("Pourquoi voit-on l'éclair avant d'entendre le tonnerre ?", ["L'éclair se produit avant", "La lumière se propage beaucoup plus vite que le son", "Le son se perd", "Par hasard"], "La lumière se propage beaucoup plus vite que le son", "Le son parcourt environ 1 km en 3 secondes, la lumière presque instantanément."),
]),
notion('P-4', 0, F, 'pc-son', [
  N("Quelle est la vitesse approximative du son dans l'air (en m/s) ?", 340, "Le son se propage à environ 340 m/s dans l'air, plus vite dans l'eau et les solides."),
  Q("Le son peut-il se propager dans le vide ?", ["Oui", "Non, il a besoin d'un milieu matériel", "Seulement les sons aigus", "Seulement dans l'espace"], "Non, il a besoin d'un milieu matériel", "Le son est une vibration qui se transmet de proche en proche dans la matière."),
  Q("Qu'est-ce qui produit un son ?", ["Un objet qui vibre", "Un objet immobile", "La lumière", "La chaleur"], "Un objet qui vibre", "La corde d'une guitare ou la membrane d'un haut-parleur vibrent."),
]),
notion('P-4', 0, F, 'pc-frequence-son', [
  Q("Quelle est l'unité de la fréquence d'un son ?", ["Le décibel", "Le hertz", "Le mètre", "Le volt"], "Le hertz", "La fréquence indique le nombre de vibrations par seconde : plus elle est élevée, plus le son est aigu."),
  Q("Quel est le domaine des fréquences audibles par l'oreille humaine ?", ["De 2 à 200 Hz", "De 20 Hz à 20 000 Hz", "De 20 000 à 200 000 Hz", "De 0 à 10 Hz"], "De 20 Hz à 20 000 Hz", "En dessous : infrasons ; au-dessus : ultrasons, perçus par certains animaux (chauve-souris, dauphins)."),
  Q("En quelle unité mesure-t-on le niveau sonore ?", ["En hertz", "En décibels (dB)", "En watts", "En mètres"], "En décibels (dB)", "Au-delà de 85 dB, une exposition prolongée peut abîmer l'audition."),
]),
notion('P-4', 1, F, 'pc-propagation-lumiere', [
  Q("Comment la lumière se propage-t-elle dans un milieu homogène et transparent ?", ["En ligne droite", "En zigzag", "En cercle", "Elle ne se propage pas"], "En ligne droite", "C'est la propagation rectiligne de la lumière, modélisée par des rayons lumineux."),
  Q("Pourquoi un objet opaque produit-il une ombre ?", ["Il absorbe le son", "Il arrête la lumière qui se propage en ligne droite", "Il émet de l'obscurité", "Il réfléchit tout"], "Il arrête la lumière qui se propage en ligne droite", "L'ombre portée est la zone que la lumière ne peut pas atteindre."),
  Q("Si la source de lumière se rapproche d'un objet, son ombre portée sur un mur…", ["diminue", "s'agrandit", "disparaît", "change de couleur"], "s'agrandit", "Plus la source est proche de l'objet, plus le cône d'ombre est large."),
]),
notion('P-4', 0, F, 'pc-sources-lumiere', [
  Q("Lequel de ces objets est une source primaire de lumière ?", ["La Lune", "Le Soleil", "Un miroir", "Une feuille de papier"], "Le Soleil", "Une source primaire produit sa propre lumière ; la Lune diffuse la lumière qu'elle reçoit du Soleil."),
  Q("Pourquoi voit-on un objet qui ne produit pas de lumière ?", ["Il émet des rayons", "Il diffuse une partie de la lumière qu'il reçoit vers nos yeux", "Nos yeux émettent de la lumière", "Par magie"], "Il diffuse une partie de la lumière qu'il reçoit vers nos yeux", "Pour voir, il faut que de la lumière entre dans l'œil."),
  Q("Pourquoi une feuille paraît-elle verte ?", ["Elle absorbe le vert", "Elle diffuse surtout la lumière verte et absorbe les autres couleurs", "Elle produit de la lumière verte", "Elle est transparente"], "Elle diffuse surtout la lumière verte et absorbe les autres couleurs", "La couleur d'un objet dépend de la lumière qu'il diffuse."),
]),
notion('P-4', 1, F, 'pc-decomposition-lumiere', [
  Q("Que montre un arc-en-ciel ?", ["Que la lumière blanche est composée de plusieurs couleurs", "Que la pluie est colorée", "Que le Soleil change de couleur", "Que l'air est bleu"], "Que la lumière blanche est composée de plusieurs couleurs", "Les gouttes d'eau décomposent la lumière blanche du Soleil."),
  Q("Quel objet permet de décomposer la lumière blanche ?", ["Un prisme", "Un aimant", "Une loupe", "Un thermomètre"], "Un prisme", "Newton a montré au XVIIe siècle que la lumière blanche est un mélange de couleurs."),
  N("Combien de couleurs distingue-t-on traditionnellement dans un arc-en-ciel ?", 7, "Violet, indigo, bleu, vert, jaune, orangé, rouge : le spectre est en réalité continu."),
]),
notion('P-4', 1, F, 'pc-signaux-communication', [
  Q("Quel type de signal transporte les informations d'un téléphone portable ?", ["Un signal sonore direct", "Des ondes électromagnétiques (ondes radio)", "Un signal lumineux visible", "Un câble obligatoire"], "Des ondes électromagnétiques (ondes radio)", "Les ondes radio se propagent dans l'air et dans le vide."),
  Q("Quel signal circule dans une fibre optique ?", ["Du son", "De la lumière", "De l'eau", "Du courant électrique uniquement"], "De la lumière", "La fibre optique guide la lumière par réflexions successives, à très haut débit."),
  Q("Quelle technologie utilise des ultrasons pour observer un bébé dans le ventre de sa mère ?", ["La radiographie", "L'échographie", "L'IRM", "Le scanner"], "L'échographie", "L'échographie utilise des ultrasons, sans danger pour le fœtus."),
]),
notion('P-1', 0, F, 'pc-volumes-unites', [
  N("Combien de millilitres y a-t-il dans 1 litre ?", 1000, "1 L = 1 000 mL = 100 cL."),
  N("À combien de cm³ correspond 1 mL ?", 1, "1 mL = 1 cm³ et 1 L = 1 dm³."),
  Q("Quel instrument permet de mesurer précisément un volume de liquide ?", ["Une éprouvette graduée", "Une balance", "Un thermomètre", "Un dynamomètre"], "Une éprouvette graduée", "On lit le volume au bas du ménisque, l'œil à hauteur de la surface du liquide."),
]),
notion('P-2', 0, F, 'pc-duree-distance', [
  N("Un train roule à 300 km/h. Combien de temps (en h) met-il pour parcourir 900 km ?", 3, "t = d / v = 900 / 300 = 3 h."),
  N("Un piéton marche à 5 km/h. Quelle distance (en km) parcourt-il en 30 minutes ?", 2.5, "30 min = 0,5 h, donc d = 5 × 0,5 = 2,5 km."),
  N("Le son parcourt environ 340 m par seconde. En combien de secondes parcourt-il 1 020 m ?", 3, "t = 1 020 / 340 = 3 s : c'est pourquoi on estime la distance d'un orage en comptant les secondes."),
]),
notion('P-1', 0, F, 'pc-corps-pur', [
  Q("Lequel de ces liquides est un corps pur ?", ["L'eau de mer", "L'eau distillée", "Le jus d'orange", "Le lait"], "L'eau distillée", "Un corps pur n'est constitué que d'une seule espèce chimique."),
  Q("Comment reconnaître qu'un liquide est un corps pur lors de son ébullition ?", ["Sa température augmente sans arrêt", "Sa température reste constante pendant le changement d'état", "Il change de couleur", "Il devient solide"], "Sa température reste constante pendant le changement d'état", "Un mélange ne présente pas de palier de température bien net."),
  Q("L'eau minérale est…", ["un corps pur", "un mélange (eau et sels minéraux dissous)", "un gaz", "un solide"], "un mélange (eau et sels minéraux dissous)", "L'étiquette indique les sels minéraux qu'elle contient."),
]),
notion('P-3', 0, F, 'pc-economies-energie', [
  Q("Quel type d'ampoule consomme le moins d'énergie pour le même éclairage ?", ["L'ampoule à incandescence", "L'ampoule LED", "L'ampoule halogène", "La bougie"], "L'ampoule LED", "Les LED ont un bien meilleur rendement et durent beaucoup plus longtemps."),
  Q("Quel geste réduit la consommation électrique à la maison ?", ["Laisser les appareils en veille", "Éteindre complètement les appareils et les lumières inutiles", "Ouvrir le réfrigérateur souvent", "Chauffer fenêtres ouvertes"], "Éteindre complètement les appareils et les lumières inutiles", "Les veilles représentent une part non négligeable de la consommation."),
  Q("Pourquoi isoler une maison permet-il d'économiser de l'énergie ?", ["Cela la rend plus jolie", "Cela limite les pertes de chaleur", "Cela produit de l'électricité", "Cela augmente le chauffage"], "Cela limite les pertes de chaleur", "Une bonne isolation réduit les besoins de chauffage."),
]),
notion('P-1', 0, F, 'pc-masse-mesure', [
  Q("Quel instrument mesure une masse ?", ["Un dynamomètre", "Une balance", "Une éprouvette", "Un thermomètre"], "Une balance", "La masse s'exprime en kilogrammes (kg) ou en grammes (g)."),
  N("Combien de grammes y a-t-il dans 1,5 kg ?", 1500, "1 kg = 1 000 g, donc 1,5 kg = 1 500 g."),
  N("Un récipient vide pèse 120 g ; rempli d'eau, il pèse 370 g. Quelle est la masse d'eau (en g) ?", 250, "370 − 120 = 250 g : on retire la masse du récipient (la tare)."),
]),
notion('P-1', 0, F, 'pc-temperature', [
  Q("Quel instrument mesure une température ?", ["Un baromètre", "Un thermomètre", "Un ampèremètre", "Une balance"], "Un thermomètre", "La température s'exprime couramment en degrés Celsius (°C)."),
  Q("Température et chaleur sont-elles la même chose ?", ["Oui", "Non : la température mesure l'agitation des particules ; la chaleur est un transfert d'énergie", "Oui, en hiver seulement", "Non, la chaleur se mesure en °C"], "Non : la température mesure l'agitation des particules ; la chaleur est un transfert d'énergie", "La chaleur passe spontanément du corps chaud vers le corps froid."),
  Q("Quand on met une cuillère en métal dans un bol de soupe chaude, la chaleur passe…", ["de la cuillère vers la soupe", "de la soupe vers la cuillère", "dans aucun sens", "uniquement vers l'air"], "de la soupe vers la cuillère", "Le transfert thermique va toujours du plus chaud vers le plus froid."),
]),
notion('P-2', 1, F, 'pc-gravitation', [
  Q("Quelle interaction maintient la Lune en orbite autour de la Terre ?", ["La force magnétique", "L'interaction gravitationnelle", "Le vent solaire", "La force électrique"], "L'interaction gravitationnelle", "Tous les objets qui ont une masse s'attirent : c'est la gravitation, décrite par Newton."),
  Q("Pourquoi les planètes tournent-elles autour du Soleil ?", ["Elles sont poussées par le vent", "Elles sont attirées par le Soleil, dont la masse est énorme", "Par hasard", "Le Soleil les repousse"], "Elles sont attirées par le Soleil, dont la masse est énorme", "L'attraction du Soleil courbe leur trajectoire en orbite."),
  Q("La gravitation est une action…", ["de contact", "à distance et attractive", "à distance et répulsive", "uniquement chimique"], "à distance et attractive", "Elle est d'autant plus forte que les masses sont grandes et proches."),
]),
notion('P-3', 2, F, 'pc-securite-electrique', [
  Q("Quel geste est dangereux ?", ["Débrancher un appareil en tirant sur la prise", "Introduire un objet métallique dans une prise de courant", "Éteindre la lumière en sortant", "Utiliser une pile de 4,5 V en classe"], "Introduire un objet métallique dans une prise de courant", "Le corps humain conduit le courant : risque d'électrisation ou d'électrocution."),
  Q("Pourquoi ne faut-il jamais s'approcher d'une ligne électrique tombée au sol ?", ["Elle est froide", "Elle peut être encore sous tension et provoquer une électrocution", "Elle est sale", "Elle peut exploser comme un pétard"], "Elle peut être encore sous tension et provoquer une électrocution", "Il faut s'éloigner et alerter les secours."),
  Q("Quel numéro d'urgence européen peut-on composer partout dans l'Union européenne ?", ["15", "112", "17", "18"], "112", "En France, on peut aussi appeler le 15 (SAMU), le 17 (police) ou le 18 (pompiers)."),
]),
notion('P-4', 0, F, 'pc-echo', [
  Q("Qu'est-ce qu'un écho ?", ["Un son qui se réfléchit sur un obstacle et revient", "Un son très aigu", "Un son produit par la lumière", "Un son qui s'arrête"], "Un son qui se réfléchit sur un obstacle et revient", "La chauve-souris se repère grâce à l'écho de ses ultrasons."),
  Q("Quel appareil utilise l'écho des ultrasons pour mesurer la profondeur de la mer ?", ["Le sonar", "Le thermomètre", "Le baromètre", "Le prisme"], "Le sonar", "On mesure la durée de l'aller-retour du son pour calculer la distance."),
  N("Un son met 2 s pour faire l'aller-retour jusqu'à une falaise (vitesse 340 m/s). À quelle distance (en m) est la falaise ?", 340, "Le son parcourt 340 × 2 = 680 m aller-retour, donc la falaise est à 680 / 2 = 340 m."),
]),
notion('P-4', 1, F, 'pc-dangers-lumiere', [
  Q("Pourquoi ne faut-il jamais regarder le Soleil directement, même lors d'une éclipse ?", ["Cela fait éternuer", "Son rayonnement peut brûler la rétine de façon irréversible", "Cela rend daltonien", "Il n'y a aucun danger"], "Son rayonnement peut brûler la rétine de façon irréversible", "Il faut des lunettes spéciales homologuées pour observer une éclipse."),
  Q("Quel rayonnement invisible du Soleil provoque les coups de soleil ?", ["L'infrarouge", "L'ultraviolet", "Les ondes radio", "Le son"], "L'ultraviolet", "Les UV abîment la peau ; crème solaire, chapeau et lunettes protègent."),
  Q("Quel rayonnement invisible ressent-on comme de la chaleur près d'un feu ?", ["L'infrarouge", "L'ultraviolet", "Les rayons X", "Le son"], "L'infrarouge", "Les caméras thermiques détectent le rayonnement infrarouge."),
]),
]
