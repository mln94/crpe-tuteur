#!/usr/bin/env python3
"""Assemble les questions du quiz (fichiers de ce dossier) avec leur rattachement au programme.

Usage : python3 scripts/quiz/construire.py <matiere> [<matiere>...] > lignes.json
- français et maths : référentiel lu dans un export JSON des tables programme_*_cycle4_*_grouped
  (variable d'environnement PROGRAMME_JSON) ;
- autres matières : référentiel.py (table programme_cycle4_disciplines).
"""
import collections, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from referentiel import R, EMC_NOTIONS, SVT_NOTIONS, PC_NOTIONS, TECH_NOTIONS

FICHIERS = {
    'mathematiques': ['m_facile', 'm_inter', 'm_difficile', 'm_complements'],
    'francais': ['f_facile', 'f_inter', 'f_difficile', 'f_lecture', 'f_culture'],
    'histoire_geographie': ['hg_facile', 'hg_inter', 'hg_difficile', 'hg_complements', 'geo_complements'],
    'emc': ['emc_facile', 'emc_inter', 'emc_difficile', 'emc_complements'],
    'svt': ['svt_facile', 'svt_inter', 'svt_difficile', 'svt_complements'],
    'physique_chimie': ['pc_facile', 'pc_inter', 'pc_difficile', 'pc_complements'],
    'technologie': ['techno_facile', 'techno_inter', 'techno_difficile', 'techno_complements'],
    'arts': ['arts_facile', 'arts_inter', 'arts_difficile'],
    'anglais': ['anglais_facile', 'anglais_inter', 'anglais_difficile'],
}
REF = {(m, c): dict(classe=cl, theme=t, sous_theme=st, objectifs=o) for m, c, cl, t, st, s, o in R}

def ref_fm(ref, obj, prog):
    i = int(ref[1:])
    if ref[0] == 'M':
        r = next(x for x in prog['programme_mathématique_cycle4_grouped'] if x['id'] == i)
        objs = [l.strip()[2:].strip() for l in (r['objectifs_apprentissage'] or '').split('\n') if l.strip().startswith('-')]
    else:
        r = next(x for x in prog['programme_francais_cycle4_objectifs_grouped'] if x['id'] == i)
        objs = r['objectifs_apprentissage']
    objectif = objs[obj] if obj is not None else r['sous_categorie']
    # Culture littéraire et artistique : chaque objectif est un long paragraphe ; on garde son intitulé
    if r['thematique'] == 'Culture littéraire et artistique':
        objectif = objectif.split(' - ')[0]
    return dict(classe=r['classe'], theme=r['thematique'], sous_theme=r['sous_categorie'], objectif=objectif)

def lignes(matiere, prog=None):
    rows, vues, niveaux = [], set(), collections.Counter()
    for mod in FICHIERS[matiere]:
        for n in __import__(mod).NOTIONS:
            assert n['notion'] not in vues, n['notion']; vues.add(n['notion'])
            ref, obj = n['ref'], n['obj']
            plan = {'emc': EMC_NOTIONS, 'svt': SVT_NOTIONS, 'physique_chimie': PC_NOTIONS, 'technologie': TECH_NOTIONS}.get(matiere, {})
            if n['notion'] in plan:
                ref, obj = plan[n['notion']]  # notions rattachées après coup à une section du programme (EMC, SVT, physique-chimie, technologie)
            if matiere in ('mathematiques', 'francais'):
                meta = ref_fm(ref, obj, prog)
            else:
                r = REF[(matiere, ref)]
                meta = dict(classe=r['classe'], theme=r['theme'], sous_theme=r['sous_theme'], objectif=r['objectifs'][obj])
                if matiere in ('emc', 'svt', 'physique_chimie', 'technologie'):
                    # Thème suivi : domaine et section (« Respecter autrui · Respect d'autrui ») ; sous-thème : l'objet d'enseignement
                    meta.update(theme=f"{r['theme']} · {r['sous_theme']}", sous_theme=meta['objectif'])
                if matiere == 'histoire_geographie':
                    # Thème suivi dans la progression : discipline, classe et titre officiel (« Histoire 5e · Chrétientés et islam… ») ;
                    # sous-thème : le point du programme (« Byzance et l'Europe carolingienne. »)
                    titre = re.sub(r'^Thème \d+ : ', '', r['sous_theme'])
                    meta.update(theme=f"{r['theme']} {r['classe']} · {titre}", sous_theme=meta['objectif'])
            for v in n['variantes']:
                if v['type'] == 'qcm': assert v['reponse'] in v['choix'] and len(set(v['choix'])) == len(v['choix']), v['question']
                niveaux[n['niveau']] += 1
                rows.append(dict(matiere=matiere, ordre=len(rows) + 1, question=v['question'], choix=v['choix'], reponse=v['reponse'],
                                 explication=v['explication'], niveau=n['niveau'], type=v['type'], notion=n['notion'],
                                 programme_ref=ref + ('' if obj is None else f".{obj}"), tolerance=v.get('tolerance', 0), **meta))
    print(matiere, dict(niveaux), len(rows), 'questions,', len(vues), 'notions', file=sys.stderr)
    return rows

if __name__ == '__main__':
    prog = json.load(open(os.environ['PROGRAMME_JSON'])) if os.environ.get('PROGRAMME_JSON') else None
    out = []
    for m in sys.argv[1:]: out += lignes(m, prog)
    json.dump(out, sys.stdout, ensure_ascii=False)
