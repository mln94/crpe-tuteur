#!/usr/bin/env python3
"""Assemble les questions du « Quiz sujets » dans data/quiz-sujets.js (module importé par app.js).

Un fichier par sujet officiel : b3_2026_g1.py = bac+3, session 2026, groupement 1 ; b5_2025_supp.py = session supplémentaire.
Identifiant d'une question : <fichier>-<rang> (ex. b3_2026_g1-12). Pour garder la progression des candidats,
on ajoute les nouvelles questions à la fin d'une épreuve ou dans une nouvelle épreuve, sans réordonner les anciennes.

Usage : python3 scripts/quiz_sujets/construire.py
"""
import collections, glob, importlib, json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
from slib import MATIERES  # noqa: E402

SORTIE = os.path.join(ICI, '..', '..', 'data', 'quiz-sujets.js')


def libelle(m):
    g = m.group(3)
    return 'Session supplémentaire' if g == 'supp' else f'Groupement {g[1:]}'


def main():
    lignes, comptes = [], collections.Counter()
    for f in sorted(glob.glob(os.path.join(ICI, 'b[35]_20[0-9][0-9]_*.py'))):
        nom = os.path.basename(f)[:-3]
        m = re.fullmatch(r'b([35])_(\d{4})_(g[123]|supp)', nom)
        assert m, f'nom de fichier inattendu : {nom}'
        concours, session = f'bac{m.group(1)}', int(m.group(2))
        rang = 0
        for ep in importlib.import_module(nom).QUESTIONS:
            for q in ep['questions']:
                rang += 1
                assert q['matiere'] in MATIERES
                if q['type'] == 'qcm':
                    assert q['reponse'] in q['choix'] and len(set(q['choix'])) == len(q['choix']), q['question']
                if q['type'] == 'numerique':
                    float(q['reponse'])
                assert q['explication'].strip(), q['question']
                lignes.append(dict(id=f'{nom}-{rang}', concours=concours, session=session, sujet=libelle(m), epreuve=ep['nom'], pdf=ep['pdf'],
                                   matiere=q['matiere'], partie=q['partie'], contexte=q.get('contexte') or '', type=q['type'],
                                   question=q['question'], choix=q['choix'], reponse=q['reponse'], explication=q['explication'],
                                   tolerance=q.get('tolerance', 0)))
                comptes[(concours, q['matiere'])] += 1
    ids = [x['id'] for x in lignes]
    assert len(ids) == len(set(ids))
    os.makedirs(os.path.dirname(SORTIE), exist_ok=True)
    with open(SORTIE, 'w', encoding='utf-8') as out:
        out.write('// Généré par scripts/quiz_sujets/construire.py : ne pas modifier à la main.\n// Questions du « Quiz sujets », tirées des sujets officiels du CRPE (réponses comprises : lu seulement par le serveur).\nexport default ')
        json.dump(lignes, out, ensure_ascii=False, separators=(',', ':'))
        out.write(';\n')
    for c in ('bac3', 'bac5'):
        print(c, ' · '.join(f'{m} {comptes[(c, m)]}' for m in MATIERES), '· total', sum(comptes[(c, m)] for m in MATIERES), file=sys.stderr)
    print(len(lignes), 'questions →', os.path.relpath(SORTIE), file=sys.stderr)


if __name__ == '__main__':
    main()
