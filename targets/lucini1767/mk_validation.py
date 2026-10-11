"""Build validation.tsv: cipher.txt parsed and read with decrypt.py (Lasry's key + the corrections in NOTES).
5 = null ('-'); 8107 open ('?'); u|v read as u."""
import re, pathlib, sys, os
H = pathlib.Path(__file__).resolve().parent
os.chdir(H); sys.path.insert(0, str(H))
from decrypt import dec
d = re.sub(r'\D', '', ''.join(l for l in open('cipher.txt') if not l.startswith('#')))
toks, out = dec(d)
lines = ['# model: it-modern', '# source: cipher.txt via decrypt.py (key DOC_R120_D3314 + NOTES corrections); mk_validation.py',
         "# note: 5 = null; 8107 open"]
for t, o in zip(toks, out):
    v = '-' if o == '_' else '?' if o.startswith('<') else o.replace('u|v', 'u')
    lines.append(f'{t}\t{v}')
(H / 'validation.tsv').write_text('\n'.join(lines) + '\n', encoding='utf-8'); print(len(toks))
