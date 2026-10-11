"""Build validation.tsv for both letters of this target, each with its own key (tokens prefixed W: / G:).

W: R8613 (Ghinucci, Latin): r8613_tokens.txt with key.tsv, as decode.py applies it (the reading r8613_reading.txt
   is that output with word division); unknown tokens '?', '-' nulls.
G: Gilino R8572 (Italian): the token stream of gilino/decode_r8572.py (transcription + corrections, deletions
   skipped, interlined replacements taken) aligned to the hand reading gilino/reading_words.txt by a small DP per
   line: each token emits one of its key alternatives ('a/o', 'con/null' ...), or a null, or one other letter at a
   cost; reading letters with no token (supplied <x>) are skipped at a cost. [tok] in the reading = unread token;
   [word] normalisations and {clear text} are dropped; doubtful words '(?)' are kept as read.
"""
import os, re, sys
H = os.path.dirname(os.path.abspath(__file__))
out = ['# model: it-cinquecento',
       '# source: W: r8613_tokens.txt + key.tsv (decode.py); G: gilino/decode_r8572.py token stream aligned to gilino/reading_words.txt (mk_validation.py)',
       '# note: Italian (Gilino, ~3100 tokens) dominant; the Latin R8613 (~800 tokens) is scored with the Italian model; separate keys, tokens prefixed W:/G:']

# ---- R8613 (Worcester)
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
        if v is None: out.append(f'W:{t}\t?')
        elif v == '-': out.append(f'W:{t}\t-')
        else:
            v = re.sub(r'[^a-z]', '', v.lower())
            out.append(f'W:{t}\t{v or "?"}')
nW = len(out) - 3

# ---- Gilino R8572
G = os.path.join(H, 'gilino'); sys.path.insert(0, G)
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
        out.append(f'G:{t.rstrip("?")}\t{v}')
open(os.path.join(H, 'validation.tsv'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('W', nW, 'G', len(out) - 3 - nW)
