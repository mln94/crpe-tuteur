# Outils de rédaction du « Quiz sujets » : chaque question vient d'un sujet officiel du CRPE (2025, 2026).
# Mêmes types que le quiz normal (scripts/quiz/qlib.py) : Q (QCM), N (réponse numérique), C (mot à cliquer).
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'quiz'))
from qlib import Q, N, C  # noqa: E402,F401

MATIERES = ('francais', 'mathematiques', 'histoire_geographie', 'emc', 'svt', 'physique_chimie', 'technologie', 'arts', 'anglais')


def pdf(media):
    """Lien du sujet officiel sur devenirenseignant.gouv.fr (numéro à la fin du nom du PDF)."""
    return f'https://www.devenirenseignant.gouv.fr/media/{media}/download'


def S(matiere, partie, q, contexte=None):
    """Question rattachée à une matière et à une partie du sujet (« Exercice 2 · motif évolutif »).
    contexte : extrait du texte, données de l'exercice ou du document, affiché au-dessus de la question."""
    assert matiere in MATIERES, matiere
    q = dict(q)
    q.update(matiere=matiere, partie=partie, contexte=contexte)
    return q


def epreuve(nom, media, questions):
    """Une épreuve d'un sujet : son nom (« Première épreuve écrite »), son PDF officiel et ses questions."""
    return {'nom': nom, 'pdf': pdf(media), 'questions': questions}
