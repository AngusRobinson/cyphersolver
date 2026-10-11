"""Build validation.tsv for R9407 from pass2/.

1. Each sign of pass2/transcription.txt gets its value from the pass-2 decoder exactly as pass2/decode.py runs it
   (key.txt, the default polyphony set, beam over de-1500s); the decoder's output is decrypt_v7.txt.
2. The current reading, pass2/reading.txt (hand-corrected from that decrypt), is aligned to the decrypt line by line
   at the letter level (difflib). A sign takes the reading's letters at its aligned positions (so the hand
   corrections count); a sign falling on a {?} word, a {V}/{S} name code or a dropped letter is '?'.
Clear text ([..] in the transcription, |..| in the reading) is left out; marginal insertions (m:) are left out, as
decode.py leaves them out."""
import re, sys, os, difflib
H = os.path.dirname(os.path.abspath(__file__))
P2 = os.path.join(H, 'pass2')
sys.path.insert(0, os.path.join(H, '..', '..'))
from lang import lm
M = lm.load('de-1500s', spaces=False)
A = M.A; K = M.order; LP = M.lp
poly = {k: v.split('/') for k, v in (kv.split('=') for kv in 'E=d/ch,n=w/b/t/o,o=b/w,#=g/u,j=s/ch'.split(','))}
key = {}
for l in open(os.path.join(P2, 'key.txt'), encoding='utf8'):
    p = l.split()
    if len(p) >= 2: key[p[0]] = p[1]
def idx(s): return [M.index[c] for c in s if c in M.index]
def lp_next(ctx, c):
    ctx = ctx[-(K-1):]
    if len(ctx) < K-1: return -3.0
    h = 0
    for x in ctx: h = h * A + x
    return float(LP[h * A + c])
def beam(signs, width=40):          # decode.py's beam, keeping the per-sign choice
    beams = [(0.0, [], [])]
    for c in signs:
        opts = poly.get(c, [key.get(c, '')])
        nb = []
        for sc, hist, vals in beams:
            for o in opts:
                s2, h2 = sc, list(hist)
                for ch in idx(o):
                    s2 += lp_next(h2, ch); h2.append(ch)
                nb.append((s2, h2[-(K-1):], vals + [o.replace('_', '')]))
        nb.sort(key=lambda b: -b[0])
        seen, beams = set(), []
        for b in nb:
            k2 = tuple(b[1])
            if k2 in seen: continue
            seen.add(k2); beams.append(b)
            if len(beams) >= width: break
    return beams[0][2]

def letters(s): return re.sub(r'[^a-zäöüß§]', '', s.lower())

reading = {}
for l in open(os.path.join(P2, 'reading.txt'), encoding='utf8'):
    m = re.match(r'(P\d\.\d\d)\s(.*)', l.rstrip('\n'))
    if not m: continue
    r = re.sub(r'\|[^|]*\|', ' ', m.group(2))            # clear Latin
    r = re.sub(r'\{[^}]*\}', '§', r)                      # {?}, {V}, {S}
    r = r.replace('F.G.', 'fg').replace('[', '').replace(']', '')
    r = re.sub(r'\d+', ' ', r)                            # clear numerals
    reading[m.group(1)] = letters(r)

out = ['# model: de-1500s',
       '# source: pass2/transcription.txt + key.txt through the pass2/decode.py beam (= decrypt_v7.txt), aligned letter by letter to the current pass2/reading.txt; mk_validation.py',
       "# note: signs under {?} words and the name codes {V} {S} are '?'; the hourglass F.G. sign reads 'fg'; ligature codes jo/mg as decode.py merges them"]
page = ''; n = 0
for l in open(os.path.join(P2, 'transcription.txt'), encoding='utf8'):
    if l.startswith('=='): page = l.split()[1]; continue
    m = re.match(r'(\d\d)\s+(.*)', l.rstrip('\n'))
    if not m: continue
    lab = f'{page}.{m.group(1)}'
    signs, vals = [], []
    for p in re.split(r'(\[[^\]]*\])', m.group(2)):
        if p.startswith('['): continue
        s = p.replace(':', '').replace('?', '').replace('jo', 'J').replace('mg', 'M').replace(' ', '')
        if s: signs += list(s); vals += beam(s)
    dec = ''.join(letters(v.replace('F.G.', 'fg')) for v in vals)
    rd = reading.get(lab, '')
    sm = difflib.SequenceMatcher(None, dec, rd, autojunk=False)
    cmap = [None] * len(dec); extra = {}
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal' or (op == 'replace' and i2 - i1 == j2 - j1):
            for k in range(i2 - i1): cmap[i1 + k] = rd[j1 + k]
        elif op == 'replace':
            for k in range(i1, i2): cmap[k] = None
            cmap[i1] = rd[j1:j2]
        elif op == 'insert':
            extra[i1 - 1] = extra.get(i1 - 1, '') + rd[j1:j2]
    pos = 0
    for c, v in zip(signs, vals):
        L = len(letters(v.replace('F.G.', 'fg')))
        span = range(pos, pos + L); pos += L
        if L == 0:
            out.append(f'{c}\t-'); n += 1; continue
        parts = [cmap[k] for k in span] + [extra.get(k, '') for k in span]
        got = ''.join(x for x in parts if x)
        if any(x is None for x in (cmap[k] for k in span)) or '§' in got or not got: got = '?'
        out.append(f'{c}\t{got}'); n += 1
open(os.path.join(H, 'validation.tsv'), 'w', encoding='utf8').write('\n'.join(out) + '\n')
print(n, 'tokens')
