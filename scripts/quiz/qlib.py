# Outils de rédaction : chaque notion = 3 formulations (ou plus) d'une même compétence
import re
def Q(q, choix, rep, expl): return {'type': 'qcm', 'question': q, 'choix': choix, 'reponse': rep, 'explication': expl}
def N(q, rep, expl, tol=0): return {'type': 'numerique', 'question': q, 'choix': [], 'reponse': str(rep), 'explication': expl, 'tolerance': tol}
def C(q, phrase, expl):
    # phrase avec la réponse entre crochets : « Le chat mange [la souris]. »
    toks, sel, inside = [], [], False
    for t in re.findall(r"\[|\]|[^\s\[\]]+", phrase.replace('’', "'")):
        if t == '[': inside = True; continue
        if t == ']': inside = False; continue
        m = re.match(r"^(.*?)([.,;:!?»]+)$", t)
        parts = [m.group(1), m.group(2)] if m and m.group(1) else [t]
        for p in parts:
            if not p: continue
            if inside and re.search(r"\w", p): sel.append(len(toks))
            toks.append(p)
    assert sel, phrase
    return {'type': 'cliquer_mot', 'question': q, 'choix': toks, 'reponse': ','.join(map(str, sel)), 'explication': expl}
def notion(ref, obj, niveau, cle, variantes):
    assert niveau in ('facile', 'intermediaire', 'difficile') and len(variantes) >= 3
    return {'ref': ref, 'obj': obj, 'niveau': niveau, 'notion': cle, 'variantes': variantes}
