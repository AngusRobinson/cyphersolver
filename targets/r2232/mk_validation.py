"""Build validation.tsv: ct.txt cipher groups decoded with key R2233 as decrypt.py does (mechanical, token by token).
Clear-text words (capitals) left out; groups that decode to a numeral or fraction left unread."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from decrypt import d
out = ['# model: fr-modern', '# source: ct.txt with key R2233 via decrypt.py (decrypt_raw.txt)',
       '# note: the few slips corrected by word in reading.txt (bienfaisante, subsistance, voue, signature) keep their mechanical value']
for l in open(os.path.join(HERE, 'ct.txt'), encoding='utf8'):
    if l.startswith('#'): continue
    for t in l.replace('|', ' ').split():
        if not re.fullmatch(r'\d+(\.\d)?', t): continue
        v = d(t)
        out.append(f'{t}\t{v if re.fullmatch(r"[^\W\d_]+", v) else "?"}')
open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(out) - 3)
