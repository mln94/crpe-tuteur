"""Montages de captures d'écran de l'application pour les emails et Instagram (style des emails Quiz CRPE).

Usage :
  python3 scripts/nouveaute_montage.py eventail sortie.png capture1.png capture2.png capture3.png [--fond '#fff7ed'] [--bord '#fed7aa']
      trois écrans en éventail : celui du milieu devant, les deux autres inclinés derrière
  python3 scripts/nouveaute_montage.py cadre sortie.png capture.png [--fond '#fff7ed'] [--bord '#fed7aa'] [--hauteur 1300]
      un seul écran, cadre arrondi et ombre douce
Les captures (téléphone, 430 px de large en 2x) viennent de scripts/nouveaute_captures.mjs.
"""
import sys
from PIL import Image, ImageDraw, ImageFilter


def couleur(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def ecran(chemin, largeur, hauteur_max=None, bord=(254, 215, 170), rayon=44, epaisseur=10):
    """Capture redimensionnée, coins arrondis et liseré coloré (comme un téléphone)."""
    im = Image.open(chemin).convert('RGB')
    if hauteur_max and im.height * largeur / im.width > hauteur_max:
        im = im.crop((0, 0, im.width, int(hauteur_max * im.width / largeur)))
    im = im.resize((largeur, round(im.height * largeur / im.width)), Image.LANCZOS)
    w, h = im.width + 2 * epaisseur, im.height + 2 * epaisseur
    cadre = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    masque = Image.new('L', (w, h), 0)
    ImageDraw.Draw(masque).rounded_rectangle((0, 0, w - 1, h - 1), rayon + epaisseur, fill=255)
    cadre.paste(Image.new('RGBA', (w, h), bord + (255,)), (0, 0), masque)
    m2 = Image.new('L', im.size, 0)
    ImageDraw.Draw(m2).rounded_rectangle((0, 0, im.width - 1, im.height - 1), rayon, fill=255)
    cadre.paste(im, (epaisseur, epaisseur), m2)
    return cadre


def avec_ombre(img, flou=28, decalage=(0, 18), opacite=70):
    marge = flou * 3
    w, h = img.width + 2 * marge, img.height + 2 * marge
    out = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ombre = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    a = img.split()[3].point(lambda v: v * opacite // 255)
    ombre.paste((120, 53, 15, 255), (marge + decalage[0], marge + decalage[1]), a)
    out = Image.alpha_composite(out, ombre.filter(ImageFilter.GaussianBlur(flou)))
    out.alpha_composite(img, (marge, marge))
    return out


def eventail(sortie, captures, fond, bord):
    toile = Image.new('RGBA', (1200, 900), fond + (255,))
    poses = [(-8, 300, 470), (8, 900, 470), (0, 600, 450)]  # angle, centre x, centre y ; le dernier est devant
    ordre = [captures[0], captures[2], captures[1]]
    for (angle, cx, cy), c in zip(poses, ordre):
        larg = 320 if angle else 360
        e = avec_ombre(ecran(c, larg, hauteur_max=640 if angle else 740, bord=bord))
        e = e.rotate(angle, resample=Image.BICUBIC, expand=True)
        toile.alpha_composite(e, (cx - e.width // 2, cy - e.height // 2))
    toile.convert('RGB').save(sortie, optimize=True)


def cadre_seul(sortie, capture, fond, bord, hauteur):
    e = avec_ombre(ecran(capture, 560, hauteur_max=hauteur, bord=bord))
    toile = Image.new('RGBA', (e.width + 40, e.height + 20), fond + (255,))
    toile.alpha_composite(e, (20, 0))
    toile.convert('RGB').save(sortie, optimize=True)


if __name__ == '__main__':
    args = sys.argv[1:]
    opts = {'--fond': '#fff7ed', '--bord': '#fed7aa', '--hauteur': '1300'}
    for k in list(opts):
        if k in args:
            i = args.index(k); opts[k] = args[i + 1]; del args[i:i + 2]
    mode, sortie, *caps = args
    fond, bord = couleur(opts['--fond']), couleur(opts['--bord'])
    if mode == 'eventail':
        eventail(sortie, caps, fond, bord)
    else:
        cadre_seul(sortie, caps[0], fond, bord, int(opts['--hauteur']))
    print('montage →', sortie)
