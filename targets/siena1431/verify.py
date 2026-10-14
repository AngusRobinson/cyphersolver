"""Independent check of the outside solution of Concistoro 2308 nos. 6 and 24 (key DECODE R4755).

Our own transcription (targets/siena1421/transcripts/no06_24all.tok: no. 6 = lines 1-15, no. 24 P2 = lines 16-53,
made 24 Sept 2026 before any key was known) is aligned with the outside reading (reading_no06.txt, reading_no24.txt)
by a dynamic-programming alignment whose substitution costs are re-estimated (EM), seeded from the key sheet R4755
read on the image (SEED below). Prints, per letter: how many of their decrypted letters our decoded transcription
reproduces, the share of their letters left in <...>/{...} (not understood), and the n-gram score of our decode
against a shuffled-key control. Writes decode_no06.txt / decode_no24.txt (our transcription, decoded).

Run from the repository root: PYTHONUTF8=1 python targets/siena1431/verify.py [--seed-only]
--seed-only: no EM; our labels get only the values read off the key sheet by eye (SEED), the non-circular test.
"""
import re, sys, math, random, pathlib
from collections import defaultdict
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))
from lang import lm

LQ, RQ, DOT = '‹', '›', '·'
WORDS = [('Duca di Milano', 'D'), ('Piccinino', 'P'), ('Viniziani', 'V'), ('Fiorentini', 'F'), ('Lucca', 'L')]

def body(fn):
    t = open(fn, encoding='utf8').read()
    t = '\n'.join(l for l in t.split('\n') if not l.startswith('#'))
    t = t.split('\n', 2)[2]                               # drop the "No. x" line
    i = t.index('recomandatione'); return t[t.index(' ', i):]   # drop the clear salutation

def letters(fn):
    t = re.sub(r'\([^)]*\)', '', body(fn)); t = re.sub(r'\[[^\]]*\]', '', t)
    for w, c in WORDS: t = t.replace(w, c)
    out = []
    for ch in t.replace('v', 'u').replace('j', 'i'):
        if ch in 'DPVFL': out.append(ch)
        elif ch.isalpha(): out.append(ch.lower())
        elif ch == DOT: out.append(DOT)
    return out

def understood(fn):
    t = re.sub(r'\([^)]*\)', '', body(fn)); t = re.sub(r'\[[^\]]*\]', '', t)
    for w, _ in WORDS: t = t.replace(w, '#')
    t = t.replace('{', LQ).replace('}', RQ)
    tot = inside = depth = 0
    for ch in t:
        if ch == LQ: depth = 1; continue
        if ch == RQ: depth = 0; continue
        if ch.isalpha() or ch == '#': tot += 1; inside += depth
    return tot, inside

SEED = {'5': 'a', '0': 'a', 'b': 'a', '2': 'b', 'd+': 'c', 'THETA': 'd', 'VENUS': 'e', '3': 'e', 'p': 'e', '6': 'e',
        'ETA': 'g', 'c': 'h', 'x': 'i', '9': 'i', 'g': 'i', '4': 'i', 'm': 'k', 'A': 'l', 'PHI': 'm', 'e': 'n',
        't': 'o', 'T': 'o', '7': 'o', 'SS': 'p', 'W': 'r', 'm+': 's', 'BOX': 't', 'H': 'u', 'E': 'u', 'y': 'u',
        'CIRC': 'L'}

P = defaultdict(lambda: defaultdict(float))
def cost(s, l):
    d = P[s]; n = sum(d.values())
    return -math.log((d.get(l, 0) + 0.05) / (n + 1.5)) if n else math.log(30)

def align(c, p, gap=6.0):
    n, m = len(c), len(p); INF = 1e18
    D = [[INF] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            v = D[i][j]
            if v >= INF: continue
            if i < n and j < m and v + cost(c[i], p[j]) < D[i + 1][j + 1]:
                D[i + 1][j + 1] = v + cost(c[i], p[j]); B[i + 1][j + 1] = 0
            if i < n and v + gap < D[i + 1][j]: D[i + 1][j] = v + gap; B[i + 1][j] = 1
            if j < m and v + gap < D[i][j + 1]: D[i][j + 1] = v + gap; B[i][j + 1] = 2
    i, j, pairs = n, m, []
    while i or j:
        b = B[i][j]
        if b == 0: pairs.append((c[i - 1], p[j - 1])); i -= 1; j -= 1
        elif b == 1: pairs.append((c[i - 1], None)); i -= 1
        else: pairs.append((None, p[j - 1])); j -= 1
    return pairs[::-1]

lines = (ROOT / 'targets/siena1421/transcripts/no06_24all.tok').read_text().split('\n')
docs = [('no06', ' '.join(lines[:15]).split(), HERE / 'reading_no06.txt'),
        ('no24', ' '.join(lines[15:]).split(), HERE / 'reading_no24.txt')]
docs = [(n, c, letters(f), f) for n, c, f in docs]
for k, v in SEED.items(): P[k][v] = 20
SEED_ONLY = '--seed-only' in sys.argv
for it in range(0 if SEED_ONLY else 6):
    allp = [x for _, c, p, _ in docs for x in align(c, p)]
    P = defaultdict(lambda: defaultdict(float))
    for s, l in allp:
        if s and l: P[s][l] += 1

key, kset = {}, {}
if SEED_ONLY: P = defaultdict(lambda: defaultdict(float), {k: defaultdict(float, {v: 20}) for k, v in SEED.items()})
for s, d in P.items():
    n = sum(d.values()); l, c = max(d.items(), key=lambda x: x[1])
    if c >= 3 and c / n >= 0.6 and l.isalpha(): key[s] = l
    if c >= 3: kset[s] = {x for x, v in d.items() if v >= max(3, 0.15 * n) and x.isalpha()}

m = lm.load('it-cinquecento', spaces=False)
def score(txt): return m.per_char(lm.norm(txt, 'early', spaces=False))
for name, c, p, f in docs:
    pairs = [(s, l) for s, l in align(c, p) if s and l]
    lets = [x for x in p if x != DOT]
    one = sum(1 for s, l in pairs if key.get(s) == l)
    many = sum(1 for s, l in pairs if l in kset.get(s, ()))
    tot, inside = understood(f)
    dec = [key.get(s, '.') for s in c]
    ours = ''.join(x for x in dec if x.islower())
    ctl = []
    for r in range(20):
        vals = list(key.values()); random.Random(r).shuffle(vals); k2 = dict(zip(key, vals))
        ctl.append(score(''.join(k2[s] for s in c if s in k2 and k2[s].islower())))
    theirs = ''.join(x for x in p if x.islower())
    print(f'{name}: our tokens {len(c)}, their decrypted letters {len(lets)}')
    print(f'  our transcription decoded = their letter: {one}/{len(lets)} = {one/len(lets):.1%} (one value per label); '
          f'{many}/{len(lets)} = {many/len(lets):.1%} (labels our transcribers merged count for each key sign they cover)')
    print(f'  their letters inside <...>/{{...}} (decrypted, not understood): {inside}/{tot} = {inside/tot:.1%}; '
          f'understood {1-inside/tot:.1%}')
    print(f'  LM it-cinquecento order 5 per char: their reading {score(theirs):.3f}; our decode {score(ours):.3f}; '
          f'shuffled-key control mean {sum(ctl)/len(ctl):.3f}, best of 20 {max(ctl):.3f}')
    if SEED_ONLY: continue
    (HERE / f'decode_{name}.txt').write_text(
        f'# Our transcription of {name} (targets/siena1421/transcripts/no06_24all.tok) decoded with key R4755 as mapped\n'
        '# onto our sign labels by verify.py. "." = label with no key value (nulls, rare or merged signs); capitals =\n'
        '# word signs (L Lucca, P Piccinino, D Duca di Milano, V Viniziani, F Fiorentini). No word division.\n'
        + '\n'.join(''.join(dec[i:i + 80]) for i in range(0, len(dec), 80)) + '\n', encoding='utf8')

# ---- the "watch it decipher" passage: the opening of no. 6 (our transcription, line 1 to mid line 3) ----
if not SEED_ONLY:
    import json
    GLYPH = {'THETA': 'θ', 'PHI': 'φ', 'VENUS': '♀', 'YCROSS': 'ɥ+', 'BOX': '□', 'W': 'ω', 'SS': 'ʃʃ', 'm+': 'm+',
             'd+': 'đ', 'ETA': 'η', 'CIRC': '⊙', 'A': 'ƒɔ', 'c^': 'ᶜc', 'AP': 'a)', 'INT': '∫', 'LT': 'ɭ', 'SL': '/',
             'SP': 'ʃp', 'Q': 'Ω', 'RX': '℞', 'RP': 'ꟼ', 'h_': 'ɧ', 'XL': 'ϰ', 'PCT': '%', 'EQO': '⊜'}
    name, c, p, f = docs[0]
    raw = re.sub(r'\([^)]*\)', '', body(f)); raw = re.sub(r'\[[^\]]*\]', '', raw)
    for w, k in WORDS: raw = raw.replace(w, k)
    starts, prev = [], ' '
    for ch in raw.replace('v', 'u'):
        if ch.isalpha() or ch == DOT:
            starts.append(prev in ' ,;:.\n'); prev = ch
        elif ch in ' ,;:.\n': prev = ' '
    pairs = align(c, p); toks = []; j = 0; n = 0
    for s, l in pairs:
        if l is not None:
            if starts[j] and toks: toks.append({'g': '', 'p': ' ', 'cls': 'plain'})
            j += 1
        if s is None: continue
        n += 1
        if n > 150: break
        v = key.get(s)
        if l and l in kset.get(s, ()) and l.islower(): v = l
        if v is None: toks.append({'g': GLYPH.get(s, s), 'p': '·', 'cls': 'null'})
        elif v.isupper(): toks.append({'g': GLYPH.get(s, s), 'p': {'L': 'Lucca', 'P': 'Piccinino'}.get(v, v), 'cls': 'code'})
        else: toks.append({'g': GLYPH.get(s, s), 'p': v, 'cls': '' if l == v else 'unc'})
    rev = {'slug': 'siena1431', 'anchor': 'method',
           'title': 'No. 6: the opening, deciphered from our own transcription',
           'caption': 'The first 150 cipher signs of no. 6 (ASSi Concistoro 2308, no. 6), as transcribed here in September 2026 '
                      'before any key was known, decoded with key R4755. Grey dots are nulls or signs our transcription '
                      'does not separate; signs marked uncertain decode to a letter other than the submitted reading.',
           'unit': 'signs', 'key_note': 'Key DECODE R4755, "Cifra cum Christofano ...", mapped onto our sign labels (key_R4755.tsv).',
           'tokens': toks}
    (ROOT / 'docs/reveal/siena1431.json').write_text(json.dumps(rev, ensure_ascii=False, indent=1) + '\n', encoding='utf8')

# ---- validation.tsv for docs/_validate.py: each of our tokens with the letter of the submitted reading it aligns with ----
if not SEED_ONLY:
    W = {'L': 'lucca', 'P': 'piccinino', 'D': 'ducadimilano', 'V': 'viniziani', 'F': 'fiorentini'}
    rows = ['# model: it-cinquecento', '# source: targets/siena1421/transcripts/no06_24all.tok aligned (verify.py) with reading_no06.txt, reading_no24.txt',
            '# note: our blind transcription; reading = the outside solver\'s letter at that position; "-" = token aligned with nothing (null)']
    for name, c, p, f in docs:
        for s, l in align(c, p):
            if s is None: continue
            rows.append(f'{s}\t' + ('-' if l is None or l == DOT else W.get(l, l)))
    (HERE / 'validation.tsv').write_text('\n'.join(rows) + '\n', encoding='utf8')
