-- Outils de réponse (droite graduée, repère, tableau à compléter) pour les questions qui ne se résolvent pas
-- seulement par du texte. Ajout seul. Réglages lus par landing/outils-reponse.js ; null = pas d'outil.
alter table public.exercices_maths add column if not exists outil_reponse jsonb;

-- Droites graduées
update public.exercices_maths set outil_reponse = '[{"type":"droite","titre":"Place les points D et E sur la droite graduée","min":-3,"max":4,"pas":0.5,"etiquettes":1,"points":["D","E"],"deja":[{"nom":"B","x":-2},{"nom":"A","x":3}]}]' where id = 56;
update public.exercices_maths set outil_reponse = '[{"type":"droite","titre":"Place les points E et F sur la droite graduée","min":-5,"max":5,"pas":1,"points":["E","F"],"deja":[{"nom":"A","x":-3},{"nom":"C","x":-1},{"nom":"B","x":2},{"nom":"D","x":4}]}]' where id = 110;
update public.exercices_maths set outil_reponse = '[{"type":"droite","titre":"Place les cinq nombres sur la droite graduée","min":-16,"max":14,"pas":1,"etiquettes":5,"points":["−15","−3","0","+7","+12"]}]' where id = 144;

-- Repères
update public.exercices_maths set outil_reponse = '[{"type":"repere","titre":"Place le point D dans le repère","xmin":-4,"xmax":4,"ymin":-3,"ymax":5,"points":["D"],"deja":[{"nom":"A","x":2,"y":3},{"nom":"B","x":-1,"y":4},{"nom":"C","x":0,"y":-2}]}]' where id = 69;
update public.exercices_maths set outil_reponse = '[{"type":"repere","titre":"(c) Place l''image M'' du point M par la translation de vecteur u(3 ; −1)","xmin":-1,"xmax":6,"ymin":-2,"ymax":4,"points":["M''"],"deja":[{"nom":"M","x":1,"y":2}]}]' where id = 48;
update public.exercices_maths set outil_reponse = '[{"type":"repere","titre":"Place les points du tableau dans le repère (A pour x = −2, B pour x = −1, etc.)","xmin":-3,"xmax":4,"ymin":-5,"ymax":7,"points":["A","B","C","D","E","F"]}]' where id = 181;
update public.exercices_maths set outil_reponse = '[{"type":"repere","titre":"Place les points A, B, C, D, E dans le repère","xmin":-1,"xmax":5,"ymin":-1,"ymax":13,"etiquettesy":2,"points":["A","B","C","D","E"]}]' where id = 205;

-- Tableau + repère
update public.exercices_maths set outil_reponse = '[{"type":"tableau","titre":"Complète le tableau de proportionnalité","lignes":[["Surface (m²)",1,2,3,4,5],["Nombre de bulbes",null,null,null,null,null]]},{"type":"repere","titre":"Place les points obtenus (A pour 1 m², B pour 2 m², etc.)","xmin":0,"xmax":6,"ymin":0,"ymax":22,"pasy":2,"etiquettesy":4,"points":["A","B","C","D","E"]}]' where id = 170;
update public.exercices_maths set outil_reponse = '[{"type":"tableau","titre":"a) Complète le tableau de valeurs","lignes":[["x",-3,-2,-1,0,1,2,3],["x²",null,null,null,null,null,null,null]]},{"type":"repere","titre":"b) Place les points (A pour x = −3, B pour x = −2, etc.)","xmin":-4,"xmax":4,"ymin":-1,"ymax":10,"points":["A","B","C","D","E","F","G"]}]' where id = 209;

-- Tableaux à compléter
update public.exercices_maths set outil_reponse = '[{"type":"tableau","titre":"Valeur de chaque variable à la fin du programme","lignes":[["Variable","a","b","c","d"],["Valeur finale",null,null,null,null]]}]' where id = 17;
update public.exercices_maths set outil_reponse = '[{"type":"tableau","titre":"3) Tableau vrai / faux","choix":["Vrai","Faux"],"lignes":[["Condition","−3","0","5"],["A : nombre > 0",null,null,null],["B : nombre < 0",null,null,null],["C : nombre = 0",null,null,null]]}]' where id = 33;
update public.exercices_maths set outil_reponse = '[{"type":"tableau","titre":"Classe les nombres (sépare-les par des points-virgules)","entete_colonne":false,"lignes":[["Strictement positif","Nul","Strictement négatif"],[null,null,null]]}]' where id = 94;
update public.exercices_maths set outil_reponse = '[{"type":"tableau","titre":"Complète le tableau des carrés","lignes":[["n",0,1,2,3,4,5,6,7,8,9,10,11,12],["n²",null,null,null,null,null,null,null,null,null,null,null,null,null]]}]' where id = 97;
update public.exercices_maths set outil_reponse = '[{"type":"tableau","titre":"Complète la ligne des effectifs cumulés croissants","lignes":[["Note",8,10,12,14,16],["Effectif",3,6,8,5,3],["Effectif cumulé croissant",null,null,null,null,null]]}]' where id = 111;
update public.exercices_maths set outil_reponse = '[{"type":"tableau","titre":"Complète le tableau d''effectifs et de fréquences","lignes":[["Issue","Effectif","Fréquence (arrondie à 0,01)"],["Face",24,null],["Pile",16,null],["Total",null,null]]}]' where id = 155;
update public.exercices_maths set outil_reponse = '[{"type":"tableau","titre":"1. Tableau des issues (1er lancer en ligne, 2e lancer en colonne)","lignes":[["1er \\ 2e","P","F"],["P",null,null],["F",null,null]]}]' where id = 175;
update public.exercices_maths set outil_reponse = '[{"type":"tableau","titre":"Tableau de valeurs du périmètre","lignes":[["c (cm)",1,2,3,4,5,10],["P (cm)",null,null,null,null,null,null]]}]' where id = 195;
