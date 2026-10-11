"""Build validation.tsv for docs/_validate.py: the cipher tokens of ff. 233, 239, 288v (ct_233/239/288.txt, clear
text in [] dropped) with the value key_v4.json gives them, by decode.py's rule (letters 1-53, syllables 54-123,
word-signs from 'names'). Unknown signs ({..}) are '?'; names glossed from context ([affaires]) are given the gloss;
53 (null) is '-'. f. 143 is another key and is left out."""
import json, re, os
HERE = os.path.dirname(os.path.abspath(__file__))
key = json.load(open(os.path.join(HERE, 'key_v4.json'), encoding='utf-8'))
L = {int(k): v for k, v in key['letters'].items()}; B = {int(k): v for k, v in key['blocks'].items()}; N = key.get('names', {})
BLOCK0, NBLK, VOW = 54, 14, 'aeiou'
def dec(t):
    t = t.rstrip('?').rstrip('.')
    if t.isdigit():
        n = int(t)
        if n in L: return L[n]
        if BLOCK0 <= n < BLOCK0 + 5 * NBLK:
            c = B.get(BLOCK0 + 5 * ((n - BLOCK0) // 5), '?'); return c + VOW[(n - BLOCK0) % 5]
        return '?'
    return N.get(t, '?')
rows = []
for fn in ('ct_233.txt', 'ct_239.txt', 'ct_288.txt'):
    for line in open(os.path.join(HERE, fn), encoding='utf-8'):
        if line.startswith('#'): continue
        for t in re.sub(r'\[[^\]]*\]', ' ', line).split():
            if t in ('INS', '/INS'): continue
            v = dec(t)
            if v == '': v = '-'
            elif '{' in v or '?' in v: v = '?'
            else: v = v.strip('[]')
            rows.append((t.rstrip('?').rstrip('.'), v))
with open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf-8') as f:
    f.write('# model: fr-1600-letters\n# source: ct_233.txt, ct_239.txt, ct_288.txt with key_v4.json (decode.py rule; mk_validation.py)\n')
    f.write('# note: word-signs glossed from context (na=affaires, qu=vous, Ra=faictes) given their gloss; unglossed word-signs and 180/215/900 unread\n')
    for t, v in rows: f.write(f'{t}\t{v}\n')
print(len(rows), sum(v not in '?-' for t, v in rows))
