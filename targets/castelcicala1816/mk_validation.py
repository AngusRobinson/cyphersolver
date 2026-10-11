"""Build validation.tsv: transcripts/R*.txt groups (corpus.py) with key.tsv, as apply.py does. 5-figure groups = null."""
import os, sys, pathlib
HERE = pathlib.Path(__file__).parent; os.chdir(HERE); sys.path.insert(0, str(HERE))
from corpus import C, OTHER
K = {}
for l in open('key.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    a, b = l.rstrip('\n').split('\t')[:2]; K[a] = b
out = ['# model: it-modern',
       '# source: transcripts/R*.txt via corpus.py, key.tsv applied as in apply.py (reading_partial.txt)',
       '# note: R9586/R9588 (other code) left out; 5-figure groups are nulls (apply.py); groups with ? unread; key grades G/X/I all used']
for r, ts in C.items():
    if r in OTHER: continue
    for t in ts:
        if len(t) >= 5 and '?' not in t: out.append(f'{t}\t-'); continue
        out.append(f'{t}\t{K.get(t, "?")}')
open('validation.tsv', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(out) - 3)
