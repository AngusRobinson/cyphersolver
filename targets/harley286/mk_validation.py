"""Build validation.tsv from transcription.tsv (glyph column vs Latin column, the reading of record).
Per line, glyph words are aligned with Latin words by a small DP (1:1, 1:2 and 2:1 word groups, skips allowed);
a group is paired letter by letter only when its sign count equals the Latin letter count (y = the ii ligature
counts 2); signs in unpaired groups are '?'. Margin notes and struck words dropped. Uncertain glyphs written [x]
count as the sign x; Latin [x] supplied letters are tried without and with."""
import re, pathlib
H = pathlib.Path(__file__).parent
out = ['# model: la', '# source: transcription.tsv glyph and Latin columns aligned word by word (mk_validation.py)',
       "# note: words whose sign count does not match the Latin letter count are left unread ('?')"]
def gsplit(w):
    return [c for c in re.sub(r'[\[\]]', '', w) if c not in '.-()+,;:']
def pair(gws, lws):
    signs = [x for w in gws for x in gsplit(w)]
    wid = [2 if s == 'y' else 1 for s in signs]
    for cand in (re.sub(r'\[[^\]]*\]', '', ' '.join(lws)), ' '.join(lws)):
        lat = re.sub(r'[^A-Za-z]', '', cand).lower()
        if sum(wid) == len(lat):
            vals, i = [], 0
            for w in wid: vals.append(lat[i:i + w]); i += w
            return list(zip(signs, vals))
    return None
nsig = npair = 0
for line in (H / 'transcription.tsv').read_text(encoding='utf-8').splitlines()[1:]:
    f = line.split('\t')
    if len(f) < 3: continue
    g, l = f[1], f[2]
    g = re.sub(r'\[(margin|lighter|bottom)[^\]]*\]', ' ', g); g = re.sub(r'\[[^\]]*struck\]', ' ', g)
    l = re.sub(r'\[(margin|lighter|bottom)[^\]]*\]', ' ', l)
    l = re.sub(r'\[[^\]]*struck\]|\[struck\]|\[=[^\]]*\]|\[\?\]|\{\?\}|\.\.\.', ' ', l)
    gw = [w for w in g.split() if gsplit(w)]
    lw = [w for w in l.split() if re.sub(r'[^A-Za-z]', '', w)]
    n, m = len(gw), len(lw)
    best = {(0, 0): (0, None)}
    for i in range(n + 1):
        for j in range(m + 1):
            if (i, j) not in best: continue
            sc = best[(i, j)][0]
            moves = [(1, 0), (0, 1)] + [(a, b) for a in (1, 2) for b in (1, 2) if a + b <= 3]
            for a, b in moves:
                if i + a > n or j + b > m: continue
                p = pair(gw[i:i + a], lw[j:j + b]) if a and b else None
                gain = sum(1 for _ in p) if p else 0
                if (a and b) and not p: continue
                k = (i + a, j + b)
                if k not in best or best[k][0] < sc + gain:
                    best[k] = (sc + gain, (i, j, p, a))
    seq, k = [], (n, m)
    while k != (0, 0):
        i, j, p, a = best[k][1]
        seq.append((i, a, p)); k = (i, j)
    for i, a, p in reversed(seq):
        if a == 0: continue
        if p: out += [f'{s}\t{v}' for s, v in p]; npair += len(p)
        else: out += [f'{s}\t?' for w in gw[i:i + a] for s in gsplit(w)]
        nsig += sum(len(gsplit(w)) for w in gw[i:i + a])
print('signs', nsig, 'paired', npair)
(H / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
