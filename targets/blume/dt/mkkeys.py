"""Rebuild the key-phrase lists for the dictionary attack (run from the repository root).
keys_big.txt: words (5-28 letters) and 2-3-word phrases (8-28 letters) from lang/corpora; multiword phrases kept if seen twice or <= 12 letters.
keys_phr45.txt: Spanish and German 3-5-word phrases of 12-26 letters not already in keys_big.txt."""
import re, unicodedata, collections
def norm(s):
    s = unicodedata.normalize('NFD', s); return ''.join(c for c in s if c.isalpha() and ord(c) < 128).upper()
def toks(f):
    txt = open(f'lang/corpora/{f}.txt', encoding='utf-8', errors='ignore').read()
    return [t for t in (norm(x) for x in re.findall(r"[^\W\d_]+", txt)) if t]
D = 'targets/blume/dt/'
big = set()
for f, wmax in [('es-gutenberg',3),('de-gutenberg',3),('fr-gutenberg',2),('it-gutenberg',2),('en-gutenberg',2),('la-gutenberg',1),('pt-gutenberg',1)]:
    t = toks(f); c = collections.Counter()
    for k in range(1, wmax + 1):
        for i in range(len(t) - k + 1):
            p = ''.join(t[i:i+k])
            if 8 <= len(p) <= 28 or (k == 1 and 5 <= len(p) <= 28): c[p] += 1
    big.update(p for p, v in c.items() if v >= 2 or len(p) <= 12)
open(D + 'keys_big.txt', 'w').write('\n'.join(sorted(big)))
out = set()
for f in ['es-gutenberg', 'es-quijote', 'de-gutenberg']:
    t = toks(f)
    for k in (3, 4, 5):
        for i in range(len(t) - k + 1):
            p = ''.join(t[i:i+k])
            if 12 <= len(p) <= 26 and p not in big: out.add(p)
open(D + 'keys_phr45.txt', 'w').write('\n'.join(sorted(out)))
