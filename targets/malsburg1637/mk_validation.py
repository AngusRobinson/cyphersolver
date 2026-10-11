"""Build validation.tsv: every f0NN.txt except the duplicate ff. 30-31, tokens as measure.py's runs() gives them
(key.txt digit table and letter signs, codes.txt values, '=' prefix dropped). Open codes/signs unread; single figures
(numerals) left unread, they carry no letters. The f. 12 letter-cipher block (another system) is not included."""
import os, re, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); os.chdir(HERE)
sys.argv = sys.argv[:1]
from measure import runs
out = ['# model: de-1640s',
       '# source: f003-f029, f032-f033 .txt (not the duplicate f030-f031) via measure.py runs(), key.txt + codes.txt',
       '# note: German dominant; f. 32 is a French letter in the same key (kept); numerals and open codes unread; f. 12 alphabetic block excluded']
n = 0
for f in sorted(glob.glob('f0[0-9][0-9].txt')):
    if f in ('f030.txt', 'f031.txt'): continue
    for run in runs(f):
        for raw, val in run:
            t = raw.rstrip("'?_")
            if val is None or val.isdigit(): v = '?'
            else: v = val.lstrip('=')
            out.append(f'{t}\t{v}'); n += 1
open('validation.tsv', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(n)
