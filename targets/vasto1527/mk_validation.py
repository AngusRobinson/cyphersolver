"""Build validation.tsv for no. 6 (ff. 16v-17v) from n6_signs.tsv, the reading of record (n6_measure.py).
Tokens are Lasry's sign labels (homophones under one label). Per row, the reading's letters are divided among the
row's tokens by a small DP (each token takes 0-12 letters; cost = edit distance to its label, a flat cost for
unlabelled signs and code groups); a token given no letters is '?'. Rows u/x are unread; a row read as the '[at]'
switch marker or as punctuation '.' is null ('-'); other bracketed readings are unread."""
import re, unicodedata, pathlib
H = pathlib.Path(__file__).parent
def nz(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z]', '', s.replace('v', 'u').replace('j', 'i').replace('y', 'i'))
def lev(a, b):
    d = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        p, d[0] = d[0], i
        for j, y in enumerate(b, 1):
            p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (x != y))
    return d[-1]
def split(toks, reading):
    r = nz(reading); n, m = len(toks), len(r)
    INF = 1e9; D = [[INF] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]; D[0][0] = 0
    for i, t in enumerate(toks):
        lab = None if (t.startswith('[') or t.startswith('<') or t == '?') else nz(t)
        for j in range(m + 1):
            if D[i][j] >= INF: continue
            for L in range(0, min(12, m - j) + 1):
                c = (lev(lab, r[j:j + L]) if lab is not None else (1.0 if L == 0 else 0.5)) + D[i][j]
                if c < D[i + 1][j + L]: D[i + 1][j + L] = c; B[i + 1][j + L] = j
    j, out = m, []
    for i in range(n, 0, -1):
        pj = B[i][j]; out.append(r[pj:j]); j = pj
    return out[::-1]
out = ['# model: es-golden-age', '# source: n6_signs.tsv rows (tokens | reading | status), letters divided among tokens by DP (mk_validation.py)',
       "# note: no. 6 only (no. 10 has no sign transcription, no. 20 unread); tokens are Lasry's labels, homophones merged"]
for line in (H / 'n6_signs.tsv').read_text(encoding='utf-8').splitlines():
    if not line.strip() or line.startswith('#'): continue
    f = line.split('\t'); toks, reading, st = f[1].split(), f[2], f[3]
    if st in 'ux': vals = ['?'] * len(toks)
    elif reading.strip() in ('[at]', '.'): vals = ['-'] * len(toks)
    elif '[' in reading: vals = ['?'] * len(toks)
    else: vals = [v or '?' for v in split(toks, reading)]
    out += [f'{t}\t{v}' for t, v in zip(toks, vals)]
(H / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
