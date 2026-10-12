"""Sequential coherence of a partial decode: how many adjacent pairs of decoded whole words are attested word bigrams in
an 18th-c. French corpus, against random permutations of the same decoded values over the same positions (2000).
A partial key that is right gives more attested neighbours than its own values shuffled.

usage: python scripts/coherence.py <key.tsv> <cipher.txt> <corpus.txt> [<corpus.txt> ...] [--limit N]
The corpus files are concatenated and the first N characters (default 6,000,000) are used.
Result of 11 Oct 2026 (envoy table from envoy_key.py, R1955_tx.txt, WAINUT's 18th-c. diplomatic French corpus, see
NOTES): 30 adjacent decoded pairs, 19 attested, permutation mean 11.1, p 0.001."""
import sys, os, re, random, unicodedata
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import decode as b


def nz(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')


args = [a for a in sys.argv[1:] if not a.startswith('--')]
limit = 6000000
if '--limit' in sys.argv:
    limit = int(sys.argv[sys.argv.index('--limit') + 1]); args.remove(str(limit))
keyp, ciph, corpora = args[0], args[1], args[2:]
txt = nz(''.join(open(c, encoding='utf8', errors='ignore').read() for c in corpora)[:limit])
W = re.sub(r"[^a-z' ]+", ' ', txt).replace("'", "' ").split()
BG = set(zip(W, W[1:]))
key = b.load_key(keyp)
toks = [t for t in b.load_cipher(ciph) if t[0] != '||']
vals = []
for d in b.decode(key, toks):
    v = d[1]
    if v == '·' or v.startswith('<') or '-' in v or len(v.split()) != 1:
        vals.append(None); continue
    vals.append(nz(v.split('/')[0]))


def score(vs):
    return sum(1 for a, c in zip(vs, vs[1:]) if a and c and (a, c) in BG)


obs = score(vals)
pos = [i for i, v in enumerate(vals) if v]
pool = [vals[i] for i in pos]
rng = random.Random(1); sims = []
for _ in range(2000):
    rng.shuffle(pool); vs = [None] * len(vals)
    for i, v in zip(pos, pool):
        vs[i] = v
    sims.append(score(vs))
pairs = sum(1 for a, c in zip(vals, vals[1:]) if a and c)
print(ciph, 'corpus words', len(W), 'adjacent decoded pairs', pairs, 'attested', obs,
      'perm mean %.1f' % np.mean(sims), 'p(>=)', np.mean(np.array(sims) >= obs))
