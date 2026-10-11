"""Build validation.tsv from the word-aligned session-3 files ct_f154/154v/156/156v/160/164/174.txt (measure.py format).
Each read group's '=' reading is split over its tokens (lengths from the values key.tsv gives each label, fewest
mismatches; y = i, j = i, v = u). Groups whose length cannot be split that way are left unread ('?'), counted and printed. Unread groups
({..}) are '?'. Struck signs (~) are left out, as in measure.py. f. 124 (other file format, 100 tokens) is not included."""
import os, re, sys, unicodedata, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); os.chdir(HERE)
from measure import parse
def nz(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'\(.*?\)', '', s)
    return re.sub(r'[^a-z]', '', s).replace('j', 'i').replace('v', 'u').replace('y', 'i')
ALT = collections.defaultdict(set)
for l in open('key.tsv', encoding='utf-8'):
    if l.startswith('#') or l.startswith('label'): continue
    f = l.rstrip('\n').split('\t')
    if len(f) < 3: continue
    for v in re.split(r'/', re.sub(r'\(.*?\)', lambda m: '/' + m.group(0)[1:-1] + '/', f[2])):
        v = nz(v)
        if v: ALT[f[0]].add(v)
def split(toks, target):
    """Min-mismatch split of the group's reading over its tokens: each token takes a substring as long as one of its
    key values (or 1 letter); cost 1 where the substring is not one of its key values. The token's reading is the
    substring of the project's reading, whatever the key says."""
    memo = {}
    def go(i, p):
        if i == len(toks): return (0, []) if p == len(target) else None
        if (i, p) in memo: return memo[(i, p)]
        alts = ALT.get(toks[i], set()); best = None
        for L in sorted({len(v) for v in alts} | {1}):
            sub = target[p:p + L]
            if len(sub) < L: continue
            rest = go(i + 1, p + L)
            if rest is None: continue
            c = rest[0] + (0 if sub in alts else 1)
            if best is None or c < best[0]: best = (c, [sub] + rest[1])
        memo[(i, p)] = best; return best
    r = go(0, 0)
    return r
out = ['# model: fr-1600-letters',
       '# source: ct_f154.txt ct_f154v.txt ct_f156.txt ct_f156v.txt ct_f160.txt ct_f164.txt ct_f174.txt (= reading lines), key.tsv',
       '# note: group readings split over tokens with key.tsv values; groups not splittable that way left unread; f. 124 not included']
bad = tot = mism = 0
for fn in ['ct_f154.txt', 'ct_f154v.txt', 'ct_f156.txt', 'ct_f156v.txt', 'ct_f160.txt', 'ct_f164.txt', 'ct_f174.txt']:
    for cur, toks, rd in parse(fn):
        for g, r in zip(toks, rd):
            if not g: continue
            tot += len(g)
            if not r or r.startswith('{'):
                out += [f'{t}\t?' for t in g]; continue
            s = split(g, nz(r))
            if s is not None: mism += s[0]; s = s[1]
            if s is None:
                bad += len(g); out += [f'{t}\t?' for t in g]
                if '-v' in sys.argv: print('no split', fn, cur, g, r)
            else: out += [f'{t}\t{v}' for t, v in zip(g, s)]
open('validation.tsv', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(tot, 'tokens;', mism, 'tokens whose reading differs from their key value;', bad, 'in groups that do not split with key values (left unread)')
