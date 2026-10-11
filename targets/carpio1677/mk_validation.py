"""Build validation.tsv: DECODE's transcriptions (img/DOC_R*.txt, git-ignored; read from the main checkout if absent
here) through parse.load and dec.tr, i.e. the key in NOTES.md exactly as dec.py applies it. The three-letter code
names in the NOTES table carry their table meaning; the ones marked (?) there, and {..}/[..] (unparsed or unknown
tokens), are '?'. Nulls ('_') are '-'."""
import sys, glob, pathlib, os
H = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(H))
from parse import load
from dec import tr
img = H / 'img'
if not img.exists():
    img = pathlib.Path('C:/Users/dbour/cypher/targets/carpio1677/img')
CODES = {'sen': 'elrey', 'gin': 'sm', 'jin': 'sm', 'jen': 'sm', 'gus': 'principe', 'mus': 'principe',
         'quol': 'inglaterra', 'ana': 'napoles', 'ten': 'francia', 'den': 'francia', 'pon': 'armada',
         'san': 'bruselas', 'gon': 'senor', 'ran': 'gobernador', 'xan': 'gobernador', 'xon': 'guerra',
         'lun': 'carta', 'men': 'reino'}
out = ['# model: es-golden-age',
       '# source: img/DOC_R1002..R1011 (DECODE transcriptions) via parse.py + dec.py tr(); code names from the NOTES table; mk_validation.py',
       "# note: code names marked (?) in NOTES (tan, cun, iles, 14+) and DECODE slips shown as {..}/[..] are '?'; R1010 'Jen' (Reino) taken as S.M. like jen elsewhere"]
for f in sorted(glob.glob(str(img / 'DOC_R*.txt'))):
    for t in load(f):
        low = t.lower()
        if t == 'Jen' and 'R1010' in f: v = 'reino'
        elif low in CODES: v = CODES[low]
        else:
            v = tr(t)
            if v == '_': v = '-'
            elif v.startswith('{') or v.startswith('[') or low in ('tan', 'cun', 'iles'): v = '?'
            elif v == 'V.S.': v = 'vs'
        out.append(f'{t}\t{v}')
(H / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(out) - 3, 'tokens')
