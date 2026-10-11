"""Build validation.tsv: each cipher letter of ct.txt as token '<alphabet>:<letter>' (alphabet per line as in run.py),
with the letter of reading.txt (the corrected French, reading of record) it stands for. Per line, the key decrypt
(decrypt.dec) is aligned with the reading's letters by edit distance; a cipher letter takes the reading letter it is
matched or substituted with; letters facing a gap or a bracketed conjecture/unread stretch ([..], [parler]) are '?'."""
import re, unicodedata, pathlib, sys
H = pathlib.Path(__file__).parent; sys.path.insert(0, str(H))
from decrypt import dec
def norm(s):
    s = unicodedata.normalize('NFD', s); s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.lower().replace('j', 'i')
C = 'DGLNR'; k = None; ctl = []
for line in (H / 'ct.txt').read_text(encoding='utf-8').splitlines():
    if line.startswith('#') or not line: continue
    if line[1:2] == ':': k = line[0]; line = line[2:]
    else: k = C[(C.index(k) + 1) % 5]
    ctl.append((k, [c for c in line.lower().replace('j', 'i') if c.isalpha()]))
rdl = [l for l in (H / 'reading.txt').read_text(encoding='utf-8').splitlines() if re.match(r'\[[DGLNR]\]', l)]
assert len(rdl) == len(ctl), (len(rdl), len(ctl))
out = ['# model: fr-modern', '# source: ct.txt (alphabet per line as run.py) aligned with reading.txt via decrypt.py (mk_validation.py)',
       '# note: token = alphabet:letter (five alphabets D G L N R); bracketed conjectures in reading.txt left unread']
for (k, cl), r in zip(ctl, rdl):
    r = r[3:]
    r = re.sub(r'\(\?\)', '', r)
    r = re.sub(r'\[[^\]]*\]', lambda m: '#' * max(2, len(re.sub(r'[^A-Za-z]', '', m.group(0)))), r)
    rl = [c for c in norm(r) if c.isalpha() or c == '#']
    d = [dec(k, c) for c in cl]
    n, m = len(d), len(rl)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + (0 if d[i-1] == rl[j-1] else 1))
    i, j, vals = n, m, []
    while i > 0:
        if j > 0 and D[i][j] == D[i-1][j-1] + (0 if d[i-1] == rl[j-1] else 1):
            vals.append(rl[j-1] if rl[j-1] != '#' else '?'); i -= 1; j -= 1
        elif D[i][j] == D[i-1][j] + 1:
            vals.append('?'); i -= 1
        else:
            j -= 1
    vals.reverse()
    out += [f'{k}:{c}\t{v}' for c, v in zip(cl, vals)]
(H / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
