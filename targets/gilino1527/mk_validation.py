"""Build validation.tsv for Gilino R8572 (Italian): the token stream of decode_r8572.py (transcription + corrections,
deletions skipped, interlined replacements taken) aligned to the hand reading reading_words.txt by a small DP per line:
each token emits one of its key alternatives ('a/o', 'con/null' ...), or a null, or one other letter at a cost; reading
letters with no token (supplied <x>) are skipped at a cost. [tok] in the reading = unread token; [word] normalisations
and {clear text} are dropped; doubtful words '(?)' are kept as read.
Split from the former targets/superscript/ (14 Oct 2026); Ghinucci R8613 has its own file in targets/ghinucci1527/.
"""
import os, re, sys
H = os.path.dirname(os.path.abspath(__file__))
out = ['# model: it-cinquecento',
       '# source: decode_r8572.py token stream aligned to reading_words.txt (mk_validation.py)']

G = H; sys.path.insert(0, G)
cwd = os.getcwd(); os.chdir(G)
src = open('decode_r8572.py', encoding='utf-8').read().split('if __name__')[0]
ns = {'__file__': os.path.join(G, 'decode_r8572.py'), '__name__': 'dec'}
exec(src, ns)
L = dict(ns['load_lines']()); KEY = ns['KEY']
os.chdir(cwd)

def cipher_tokens(toks):
    r = []
    for t in toks:
        if t.startswith('{') or t.startswith('[del'): continue
        if t.startswith('[above:'): r += t[7:-1].split(); continue
        r.append(t)
    return r

UNK = '\x01'
def alts(t):
    v = KEY.get(t.rstrip('?'), (None,))[0]
    if v is None: return None
    a = []
    for x in v.split('/'):
        x = '' if x == 'null' else re.sub(r'[^a-zà-ÿ]', '', x.lower())
        a.append(x)
    return a

def align(toks, chars):
    n, m = len(toks), len(chars); INF = 1e9
    D = [[INF] * (m + 1) for _ in range(n + 1)]; P = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            d = D[i][j]
            if d >= INF: continue
            if j < m:
                c = d + (1.5 if chars[j] != UNK else 4)
                if c < D[i][j + 1]: D[i][j + 1] = c; P[i][j + 1] = (i, j, None)
            if i == n: continue
            A = alts(toks[i]); opts = []
            if A is None:
                opts.append((0, '-', 3))
                if j < m: opts.append((1, '?' if chars[j] == UNK else chars[j], 0.5 if chars[j] == UNK else 1.5))
            else:
                opts.append((0, '-', 0 if '' in A else 3))
                for a in A:
                    if a and ''.join(chars[j:j + len(a)]) == a: opts.append((len(a), a, 0))
                if j < m:
                    if chars[j] == UNK: opts.append((1, '?', 0))
                    else: opts.append((1, chars[j], 2))
            for k, val, c in opts:
                if d + c < D[i + 1][j + k]: D[i + 1][j + k] = d + c; P[i + 1][j + k] = (i, j, val)
    r, i, j = [], n, m
    while (i, j) != (0, 0):
        pi, pj, val = P[i][j]
        if pi != i: r.append((toks[pi], val))
        i, j = pi, pj
    return list(reversed(r))

W = {}
for l in open(os.path.join(G, 'reading_words.txt'), encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    i, t = l.rstrip('\n').split('\t', 1); W[i] = t
for lid, toks in L.items():
    ct = cipher_tokens(toks)
    body = re.sub(r'\{[^}]*\}', ' ', W.get(lid, ''))
    names = set(t.rstrip('?') for t in ct)
    body = re.sub(r'\[([^\]]*)\]', lambda m: ' ' + UNK + ' ' if m.group(1).rstrip('?') in names else ' ', body)
    body = body.replace('(?)', '')
    chars = [c for c in body.lower() if c.isalpha() or c == UNK]
    for t, v in align(ct, chars):
        out.append(f'{t.rstrip("?")}\t{v}')
open(os.path.join(H, 'validation.tsv'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('tokens', len(out) - 2)
