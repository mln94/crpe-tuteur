# Anglais : notions ajoutées pour couvrir chaque sous-thème du programme du collège (au moins 15 questions)
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ── Outils linguistiques · Phonologie et prosodie ──
notion('OL-8', 0, F, 'ang-phon-s', [
  Q("Comment se prononce le -s final de « watches » ?", ["/ɪz/", "/s/", "/z/", "Il est muet"], "/ɪz/", "Après les sons /s/, /z/, /ʃ/, /tʃ/, /dʒ/, on prononce /ɪz/ : watches, boxes, roses."),
  Q("Dans « Jack's bike », comment se prononce le 's ?", ["/s/", "/z/", "/ɪz/", "Il est muet"], "/s/", "Après une consonne sourde comme /k/, le s se prononce /s/."),
  Q("Dans « dogs », comment se prononce le -s final ?", ["/z/", "/s/", "/ɪz/", "Il est muet"], "/z/", "Après une consonne sonore comme /g/, le s se prononce /z/."),
]),
notion('OL-8', 0, I, 'ang-lettres-muettes', [
  Q("Quelle lettre est muette dans « knife » ?", ["Le k", "Le n", "Le f", "Le i"], "Le k", "Le k ne se prononce pas devant n : knee, know, knight."),
  Q("Quelle lettre est muette dans « autumn » ?", ["Le n final", "Le m", "Le t", "Le u"], "Le n final", "On prononce /ˈɔːtəm/."),
  Q("Dans « Wednesday », quelle lettre ne se prononce pas ?", ["Le premier d", "Le w", "Le s", "Le y"], "Le premier d", "On prononce /ˈwenzdeɪ/."),
]),
notion('OL-8', 0, D, 'ang-accent-intonation', [
  Q("Sur quelle syllabe porte l'accent de « photographer » ?", ["La deuxième : pho-TO-gra-pher", "La première : PHO-to-gra-pher", "La troisième : pho-to-GRA-pher", "La dernière : pho-to-gra-PHER"], "La deuxième : pho-TO-gra-pher", "L'accent se déplace : PHOtograph, phoTOgrapher, photoGRAphic."),
  Q("Sur quelle syllabe porte l'accent de « favourite » ?", ["La première : FA-vou-rite", "La deuxième : fa-VOU-rite", "La dernière : fa-vou-RITE", "Aucune"], "La première : FA-vou-rite", "Le mot se prononce souvent en deux syllabes : /ˈfeɪvrɪt/."),
  Q("Comment évolue généralement l'intonation à la fin d'une question fermée (yes/no question) ?", ["Elle monte", "Elle descend", "Elle reste plate", "Elle s'arrête au milieu"], "Elle monte", "« Do you like tea? » se termine sur une intonation montante."),
]),
# ── Repères culturels · L'Irlande ──
notion('RC-2', 0, F, 'ang-irlande-base', [
  Q("Quelle est la capitale de la République d'Irlande ?", ["Dublin", "Belfast", "Cork", "Edimbourg"], "Dublin", "Belfast est la capitale de l'Irlande du Nord, qui fait partie du Royaume-Uni."),
  Q("Quel saint patron de l'Irlande est fêté le 17 mars ?", ["Saint Patrick", "Saint George", "Saint Andrew", "Saint David"], "Saint Patrick", "La St Patrick's Day est célébrée dans le monde entier."),
  Q("Quelle plante est le symbole de l'Irlande ?", ["Le trèfle (shamrock)", "La rose", "Le chardon", "Le poireau"], "Le trèfle (shamrock)", "La rose est le symbole de l'Angleterre, le chardon celui de l'Écosse."),
]),
notion('RC-2', 0, F, 'ang-irlande-paysages', [
  Q("Quel surnom donne-t-on à l'Irlande pour ses paysages verdoyants ?", ["L'île d'Émeraude (the Emerald Isle)", "L'île de Beauté", "Le pays du Soleil-Levant", "La Big Apple"], "L'île d'Émeraude (the Emerald Isle)", "Le climat doux et humide entretient des prairies très vertes."),
  Q("Quelles falaises célèbres dominent l'océan Atlantique sur la côte ouest de l'Irlande ?", ["Les falaises de Moher", "Les falaises de Douvres", "Les falaises d'Étretat", "Le Grand Canyon"], "Les falaises de Moher", "Elles sont l'un des sites les plus visités du pays."),
  Q("Que signifie « Fáilte », en irlandais, sur de nombreux panneaux ?", ["Bienvenue", "Au revoir", "Attention", "Sortie"], "Bienvenue", "Les panneaux sont souvent bilingues, en irlandais et en anglais."),
]),
notion('RC-2', 0, I, 'ang-irlande-langues', [
  Q("Quelles sont les langues officielles de la République d'Irlande ?", ["L'irlandais (gaélique) et l'anglais", "L'anglais seulement", "Le gaélique écossais et l'anglais", "Le gallois et l'anglais"], "L'irlandais (gaélique) et l'anglais", "L'irlandais est la première langue officielle selon la Constitution."),
  Q("Quelle monnaie utilise la République d'Irlande ?", ["L'euro", "La livre sterling", "Le dollar", "Le franc irlandais"], "L'euro", "L'Irlande du Nord, au Royaume-Uni, utilise la livre sterling."),
  Q("Comment appelle-t-on la partie de l'île d'Irlande qui fait partie du Royaume-Uni ?", ["L'Irlande du Nord", "L'Ulster libre", "L'Écosse", "Le pays de Galles"], "L'Irlande du Nord", "L'île est partagée entre deux États depuis 1921."),
]),
notion('RC-2', 0, I, 'ang-irlande-culture', [
  Q("Quel écrivain irlandais a écrit Ulysse (1922) ?", ["James Joyce", "Charles Dickens", "William Shakespeare", "J. K. Rowling"], "James Joyce", "Le roman se déroule à Dublin en une seule journée."),
  Q("Quel groupe de rock irlandais est mené par le chanteur Bono ?", ["U2", "The Beatles", "Coldplay", "Oasis"], "U2", "Le groupe s'est formé à Dublin en 1976."),
  Q("Quel sport traditionnel irlandais se joue avec une crosse en bois (hurley) et une petite balle ?", ["Le hurling", "Le cricket", "Le baseball", "Le hockey sur glace"], "Le hurling", "C'est l'un des sports gaéliques, avec le football gaélique."),
]),
notion('RC-2', 0, D, 'ang-irlande-histoire', [
  Q("Quelle catastrophe de 1845-1852 a poussé des millions d'Irlandais à émigrer, notamment vers les États-Unis ?", ["La Grande Famine", "Une guerre civile", "Une épidémie de peste", "Un tremblement de terre"], "La Grande Famine", "Une maladie de la pomme de terre a détruit les récoltes."),
  N("En quelle année l'État libre d'Irlande est-il créé, séparé du Royaume-Uni ?", 1922, "Il deviendra plus tard la République d'Irlande."),
  Q("Quel accord de 1998 met fin à trente ans de violences en Irlande du Nord ?", ["L'accord du Vendredi saint (Good Friday Agreement)", "Le traité de Versailles", "L'accord de Paris", "Le traité de Rome"], "L'accord du Vendredi saint (Good Friday Agreement)", "Il met fin à la période appelée « the Troubles »."),
]),
# ── Repères culturels · Les États-Unis ──
notion('RC-3', 0, F, 'ang-usa-fetes', [
  Q("Que célèbre-t-on le 4 juillet aux États-Unis ?", ["La fête de l'Indépendance (Independence Day)", "Thanksgiving", "Halloween", "Noël"], "La fête de l'Indépendance (Independence Day)", "Elle commémore la Déclaration d'indépendance de 1776."),
  Q("Quelle statue, offerte par la France, accueille les arrivants dans le port de New York ?", ["La statue de la Liberté", "Le mont Rushmore", "La statue de Lincoln", "Le Golden Gate"], "La statue de la Liberté", "Elle a été inaugurée en 1886."),
  Q("Quelle fête de novembre réunit les familles américaines autour d'une dinde ?", ["Thanksgiving", "Independence Day", "Easter", "Memorial Day"], "Thanksgiving", "Elle a lieu le quatrième jeudi de novembre."),
]),
notion('RC-3', 0, I, 'ang-usa-institutions', [
  Q("Dans quel bâtiment siège le Congrès américain, à Washington ?", ["Le Capitole", "La Maison-Blanche", "Le Pentagone", "L'Empire State Building"], "Le Capitole", "Le président réside et travaille à la Maison-Blanche."),
  N("Pour combien d'années le président des États-Unis est-il élu ?", 4, "Il ne peut faire que deux mandats."),
  Q("Quelles sont les deux chambres du Congrès des États-Unis ?", ["Le Sénat et la Chambre des représentants", "La Chambre des communes et la Chambre des lords", "L'Assemblée nationale et le Sénat", "Le Parlement et le Conseil"], "Le Sénat et la Chambre des représentants", "La Chambre des communes et la Chambre des lords sont britanniques."),
]),
# ── Repères culturels · Le monde anglophone ──
notion('RC-4', 0, F, 'ang-australie-nz', [
  Q("Quelle est la capitale de l'Australie ?", ["Canberra", "Sydney", "Melbourne", "Perth"], "Canberra", "Sydney est la plus grande ville, mais pas la capitale."),
  Q("Comment appelle-t-on le peuple autochtone de Nouvelle-Zélande ?", ["Les Maoris", "Les Aborigènes", "Les Inuits", "Les Sioux"], "Les Maoris", "Les Aborigènes sont les premiers habitants de l'Australie."),
  Q("Quel animal est l'un des symboles de l'Australie ?", ["Le kangourou", "Le bison", "Le panda", "Le lion"], "Le kangourou", "Il figure sur les armoiries du pays."),
]),
notion('RC-4', 0, I, 'ang-anglophonie-monde', [
  Q("Quel pays a deux langues officielles, l'anglais et le français ?", ["Le Canada", "L'Australie", "L'Irlande", "Les États-Unis"], "Le Canada", "Le Québec est la principale province francophone."),
  Q("Dans quel pays d'Afrique de l'Est, dont la capitale est Nairobi, l'anglais est-il langue officielle avec le swahili ?", ["Le Kenya", "Le Maroc", "Le Sénégal", "Madagascar"], "Le Kenya", "C'est un ancien territoire britannique, membre du Commonwealth."),
  Q("Environ combien de personnes parlent anglais dans le monde, en langue maternelle ou seconde ?", ["Environ 1,5 milliard", "Environ 15 millions", "Environ 150 millions", "Environ 5 milliards"], "Environ 1,5 milliard", "C'est la langue la plus parlée au monde si l'on compte les locuteurs non natifs."),
]),
]
