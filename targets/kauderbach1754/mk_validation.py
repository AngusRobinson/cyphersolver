"""Build validation.tsv: the code pairs of cipher/R*.txt (nulls 5/8 already removed) with key.json applied
(the key decode.py and read/machine_R*.txt use). Pairs not in the key, and the few unsplit 4-digit runs, are '?'."""
import json, glob, os
HERE = os.path.dirname(os.path.abspath(__file__))
K = json.load(open(os.path.join(HERE, 'key.json')))
out = ['# model: fr-modern', '# source: cipher/R1043..R2082.txt (pairs after null removal) + key.json (mk_validation.py)',
       '# note: 5 and 8 single-digit nulls were removed in cipher/ and are not listed; capital-letter clear sigla are not in cipher/']
for f in sorted(glob.glob(os.path.join(HERE, 'cipher', 'R*.txt'))):
    for t in open(f, encoding='utf-8-sig').read().split():
        out.append(f'{t}\t{K.get(t, "?")}')
open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf-8').write('\n'.join(out) + '\n'); print(len(out) - 3)
