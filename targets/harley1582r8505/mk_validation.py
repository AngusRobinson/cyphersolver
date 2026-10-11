"""Build validation.tsv from final/f1-f4.txt with key.json, tokenised exactly as evalct.py (the 95.1% measure):
dot groups -> DOT (= m), '#NN' nomenclator numbers unread, trailing '?' stripped."""
import json, glob, os
HERE = os.path.dirname(os.path.abspath(__file__))
key = json.load(open(os.path.join(HERE, 'key.json')))
out = ['# model: fr-1600-letters',
       '# source: final/f1-f4.txt (cipher fields) with key.json, tokenised as evalct.py',
       '# note: dot groups written as DOT (= m); nomenclator numbers #NN unread']
for fn in sorted(glob.glob(os.path.join(HERE, 'final', 'f*.txt'))):
    for line in open(fn, encoding='utf-8', errors='replace'):
        if line.startswith('#') or '|' not in line: continue
        p = [x.strip() for x in line.split('|')]
        if len(p) < 3: continue
        for field in p[2::2]:
            for tok in field.replace('/', ' ').split():
                tok = tok.rstrip('?')
                if tok in (':', '.', '..', ':2', ':3', ':4', '::'): tok = 'DOT'
                if not tok or tok == '-': continue
                if tok.startswith('#'): out.append(f'{tok}\t?'); continue
                out.append(f'{tok}\t{key.get(tok, "?")}')
open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(out) - 3)
