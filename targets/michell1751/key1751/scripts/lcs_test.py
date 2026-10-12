"""Blind test of the frozen cabinet key v1 on R1957, without any alignment.

Decode R1957 with key_cabinet_v1_frozen.tsv (72 entries, built only from the six Fagel 5177 letters), keep the decoded
whole words (no endings, syllables or single letters except 'a'), and take the longest common subsequence (LCS) with the
words of PC 8 no. 5263. Controls: the same decoded words shuffled (500 times) against 5263, and the decoded words
against 12 other PC letters to Michell (not used for the key).

usage: python scripts/lcs_test.py     (from targets/michell1751/key1751/)
expected (11 Oct 2026): decoded words 168, PC words 460, LCS 123, shuffled mean 58.9, max 65, p 0.0"""
import os, sys, random
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import decode as b
from common import DATA, nz, lcs, pc_letters, pc_words


def words_of_decode(key, path):
    toks = [t for t in b.load_cipher(path) if t[0] != '||']
    out = []
    for code, v, conf, fl in b.decode(key, toks):
        if v == '·' or v.startswith('-') or v.endswith('-') or v.startswith('<'):
            continue
        v = nz(v.split('/')[0])
        if len(v) <= 1 and v not in ('a',):
            continue
        out += v.split()
    return out


if __name__ == '__main__':
    PC = pc_letters()
    key = b.load_key(os.path.join(DATA, 'key_cabinet_v1_frozen.tsv'))
    D = words_of_decode(key, os.path.join(DATA, 'R1957_tx.txt'))
    P = pc_words(PC, '5263')
    obs = lcs(D, P)
    rng = random.Random(0)
    sh = []
    for _ in range(500):
        x = D[:]; rng.shuffle(x); sh.append(lcs(x, P))
    print('decoded words', len(D), 'PC words', len(P), 'LCS obs', obs, 'shuffled mean', round(float(np.mean(sh)), 1),
          'max', max(sh), 'p', float(np.mean(np.array(sh) >= obs)))
    used = ('5263', '5169', '5197', '5208', '5227', '5231', '5253')
    others = [n for n, d in PC.items() if not n.startswith('_') and 'MICHELL' in d['title'] and n not in used]
    for n in others[:12]:
        Q = pc_words(PC, n)
        print('vs PC', n, len(Q), 'LCS', lcs(D, Q), 'shuffled-mean',
              round(float(np.mean([lcs(rng.sample(D, len(D)), Q) for _ in range(50)])), 1))
