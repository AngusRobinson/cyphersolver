"""Build validation.tsv for docs/_validate.py from reading.txt, the group-by-group alignment of both letters in the
petit chiffre (Louvois -> d'Herleville 1690, Feuquieres -> Catinat 1691). Each numbered line of groups is followed
by a line of values; '_' (null/point) and '.' (stop) are written '-', '?' stays unread."""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
L = open(os.path.join(HERE, 'reading.txt'), encoding='utf8').read().splitlines()
rows = []
for i, l in enumerate(L):
    if re.match(r'^\s*\d+(\s+\d+)+\s*$', l) and i + 1 < len(L):
        g = l.split()[1:]; v = L[i + 1].split()
        assert len(g) == len(v), (i, g, v)
        for a, b in zip(g, v):
            rows.append((a, '-' if b in ('_', '.') else b))
with open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf8') as f:
    f.write('# model: fr-grand-siecle\n# source: reading.txt (group-by-group alignment, key_petit_chiffre_1690.tsv) (mk_validation.py)\n')
    f.write("# note: both letters in the code: d'Herleville 1690 (with its printed translation) and Feuquieres 1691\n")
    for a, b in rows: f.write(f'{a}\t{b}\n')
print(len(rows), sum(b not in '?-' for a, b in rows))
