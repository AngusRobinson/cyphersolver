"""Build validation.tsv: f130_signs.txt zipped with reading_f130.tsv (one reading character per cipher token,
as scripts/measure.py pairs them). '-' null, '?' open."""
from pathlib import Path
B = Path(__file__).resolve().parent
def rows(p):
    return [l.rstrip('\n').split('\t') for l in open(B / p, encoding='utf-8') if l.strip() and not l.startswith('# ')]
T = {n: s.split() for n, s in rows('f130_signs.txt') if not n.endswith('.clear')}
R = {n: r.replace(' ', '') for n, r in rows('reading_f130.tsv')}
out = ['# model: fr-1600-letters', '# source: f130_signs.txt + reading_f130.tsv (as scripts/measure.py), key.tsv',
       '# note: f. 130 only (f. 128 is the key source, its reading is the gloss)']
for n, S in T.items():
    r = R[n]; assert len(r) == len(S), n
    out += [f'{s}\t{c}' for s, c in zip(S, r)]
(B / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8'); print(len(out) - 3)
