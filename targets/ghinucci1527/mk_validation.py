"""Build validation.tsv for R8613 (Ghinucci to Wolsey, Latin): r8613_tokens.txt with key.tsv, as decode.py applies it
(the reading r8613_reading.txt is that output with word division); unknown tokens '?', '-' nulls.
Split from the former targets/superscript/ (14 Oct 2026); Gilino R8572 has its own file in targets/gilino1527/.
"""
import os, re
H = os.path.dirname(os.path.abspath(__file__))
out = ['# model: la',
       '# source: r8613_tokens.txt + key.tsv (decode.py) (mk_validation.py)']

key = {}
for l in open(os.path.join(H, 'key.tsv'), encoding='utf-8'):
    l = l.rstrip('\n')
    if not l or l.startswith('%%'): continue
    t, v = l.split('\t')[:2]; key[t] = v
for l in open(os.path.join(H, 'r8613_tokens.txt'), encoding='utf-8'):
    if l.startswith('#'): continue
    for m in re.finditer(r'\{[^}]*\}|\S+', l):
        t = m.group(0)
        if t.startswith('{'): continue
        v = key.get(t)
        if v is None: out.append(f'{t}\t?')
        elif v == '-': out.append(f'{t}\t-')
        else:
            v = re.sub(r'[^a-z]', '', v.lower())
            out.append(f'{t}\t{v or "?"}')

open(os.path.join(H, 'validation.tsv'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('tokens', len(out) - 2)
