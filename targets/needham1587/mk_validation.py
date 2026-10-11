"""Build validation.tsv for needham1587 from cipher.txt with decode.py's key, in text order
(A, the glossed words of line A, C, D, F, G, H). Illegible signs ('?') are unread."""
import pathlib, os, sys
HERE = pathlib.Path(__file__).resolve().parent; os.chdir(HERE); sys.path.insert(0, str(HERE))
from decode import KEY
rows = {}
for line in open('cipher.txt', encoding='utf8'):
    if line.startswith('#') or not line.strip():
        continue
    head, _, rest = line.partition('  ')
    rows[head.strip()] = rest.split()
order = ['A', 'advise', 'enemyes', 'campe nor the towne', 'C', 'D', 'F', 'G', 'H']
assert set(order) == set(rows), rows.keys()
out = ['# model: en-modern', '# source: cipher.txt + decode.py key, via mk_validation.py',
       '# note: lines in text order A (+ the words glossed at the time), C, D, F, G, H; English 1587 (nearest period model en-1640s)']
for r in order:
    for t in rows[r]:
        if t == '|':
            continue
        out.append(f'{t}\t{KEY.get(t, "?")}')
pathlib.Path('validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(out) - 3)
