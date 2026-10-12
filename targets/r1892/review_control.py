"""Review control for PR #31 (WAINUT). Per-occurrence rank control for the WAINUT added sign values, plus leave-one-out of the strict measure.
run from targets/r1892/wainut with PYTHONUTF8=1."""
import os, sys, io, contextlib
sys.path.insert(0, os.path.abspath('../../r2242')); sys.path.insert(0, os.path.abspath('../../..'))
os.environ['STRICT'] = '0'
import measure_sense as ms
from lang import lm
import numpy as np

F = 'transcription_p2_wainut_tr.txt'
m = lm.load('nl-modern', spaces=False)
ap = ms.load_apply('.', 'nl-modern')
ADDED = dict(ap.ADDED)
POOL = sorted(set([v for v, g in ADDED.values()] + '''de het een en van in te dat die is op aan met als voor zich niet
zyn er maar om ook al door over uit dan wel zo zal kan ik u ue hy wy zy zulks myn ons hun naar by tot nog was had
zoude zouden heeft hebben worden mogelyk engeland daar hier waar wat zeer meer'''.split()))
lines = open(F, encoding='utf8').read().split('\n')


def line_lp(toks):
    """total LP of the longest read runs of a token list (unread tokens break runs), per char mean over all."""
    tot = 0.0; n = 0; run = ''
    for v in toks + [None]:
        if v is None:
            if run:
                lp = ms.charlp(m, run); tot += lp[m.order - 1:].sum(); n += len(run) - m.order + 1
            run = ''
        else:
            run += v
    return tot


res = {}
for li, line in enumerate(lines, 1):
    toks = [t for t in ap.tokens(line) if t[0] != 'note']
    vals = [ms.nrm(x[2], 'nl-modern') if x[2] else None for x in toks]
    for idx, (kind, lab2, v) in enumerate(toks):
        if lab2 not in ADDED:
            continue
        sc = {}
        for c in POOL:
            vv = vals[:]; vv[idx] = ms.nrm(c, 'nl-modern'); sc[c] = line_lp(vv)
        rank = sorted(sc, key=lambda c: -sc[c])
        prop = ADDED[lab2][0]
        res.setdefault(lab2, []).append((li, rank.index(prop) + 1, rank[:3]))

print(f'pool size {len(POOL)}')
for lab, occ in res.items():
    print(lab, ADDED[lab], ' '.join(f'L{li}:#{r}' for li, r, _ in occ), '| top3 first occ', occ[0][2])

# leave-one-out on strict measure
os.environ['STRICT'] = '1'
def measure(drop=None):
    import importlib
    ms.STRICT = True
    a = ms.load_apply('.', 'nl-modern')
    if drop:
        a.SIGNS.pop(drop, None)
    orig = ms.load_apply
    ms.load_apply = lambda f, mdl='': a
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ms.run('.', 'nl-modern', [F])
    ms.load_apply = orig
    return buf.getvalue().strip().split('\n')[-1]
print('all:', measure())
for lab in ADDED:
    if ADDED[lab][1] == 'M':
        print('drop', lab, measure(lab))
