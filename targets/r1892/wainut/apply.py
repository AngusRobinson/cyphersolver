"""../apply.py with the WAINUT sign values added for the split labels of relabel_p2.py (see ../NOTES.md).

Used through ../../r2242/measure_sense.py, which loads <folder>/apply.py:
  STRICT=1 python ../../r2242/measure_sense.py . nl-modern transcription_p2_wainut_tr.txt
WAINUT_SHUFFLE=<seed> permutes the added values among the added signs (a control: see NOTES).
"""
import os, random
_parent = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'apply.py')
exec(compile(open(_parent, encoding='utf8').read(), _parent, 'exec'))

ADDED = {
    '<zo-I>': ('zo', 'M'), '<c~>': ('zal', 'M'), '<gamma-z>': ('zulks', 'M'), '<r-sign>': ('dat', 'M'),
    '<C-loop>': ('UE', 'M'), '<Y-bar>': ('ik', 'M'), '<phi-stem>': ('uit', 'M'), '<dot-stroke>': ('aan', 'M'),
    '<leaf-check>': ('van', 'M'),
    '<Delta>': ('kan', 'I'), '<inf>': ('daar', 'I'), '<Psi>': ('over', 'I'), '<e-ess>': ('zyn', 'I'),
    '<I-sign>': ('Engeland', 'I'), '<cross-m>': ('mogelyk', 'I'),
}
if os.environ.get('WAINUT_SHUFFLE'):
    _labs = list(ADDED); _vals = [ADDED[k][0] for k in _labs]; _p = _vals[:]
    _r = random.Random(int(os.environ['WAINUT_SHUFFLE']))
    while any(a == b for a, b in zip(_p, _vals)):
        _r.shuffle(_p)
    ADDED = {k: (v, ADDED[k][1]) for k, v in zip(_labs, _p)}
SIGNS.update(ADDED)
