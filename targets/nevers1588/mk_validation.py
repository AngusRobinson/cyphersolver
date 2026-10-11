"""Build validation.tsv for f. 62 (ciphertext.txt + reading.tsv) and f. 131 (f131/ciphertext.txt + f131/reading.tsv).
Signs are paired with the reading's letters by f131/decode.py's DP aligner (key = r3708 KEY + additions + f. 131
values). f. 62 runs are unspaced in ciphertext.txt and split here by key.md's rule: '1' followed by a digit or by
d/s/b/r is one sign (11-19, 1d, 1s, 1b, 1r); any other '1' is a bare 1 (= i). Code numbers inside runs ([10],
[40m], <72>) and struck signs (#) are left out of the alignment; code numbers are written '?'. Letters the reading
marks '?' (unread) make the sign aligned to them '?'."""
import os, sys, re, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('f131dec', os.path.join(H, 'f131', 'decode.py'))
f131 = importlib.util.module_from_spec(spec); spec.loader.exec_module(f131)

def split62(r):
    out, j = [], 0
    while j < len(r):
        if r[j] == '[':
            k = r.index(']', j); out.append('<' + r[j+1:k] + '>'); j = k + 1; continue
        if r[j] == '1' and j + 1 < len(r) and (r[j+1].isdigit() or r[j+1] in 'dsbr'):
            out.append(r[j:j+2]); j += 2; continue
        out.append(r[j]); j += 1
    return out

# candidate values: key.md's table (first token of each comma-separated cell entry) + r3708/f131 KEY
CAND = {k: set(f131.norm(c) for c in v) for k, v in f131.KEY.items()}
for k, v in f131.NEW131.items(): CAND.setdefault(k, set()).update(v)
for line in open(os.path.join(H, 'key.md'), encoding='utf8'):
    m = re.match(r'\| ([a-z /]+) \| (.*) \|$', line.strip())
    if not m or m.group(1) == 'plain': continue
    for item in m.group(2).split(','):
        sg = item.strip().split(' ')[0]
        if sg: CAND.setdefault(sg, set()).update(x.strip() for x in m.group(1).split('/'))
CAND['e'] = CAND.get('e', set()) | {'t'}

def align(signs, plain):
    """DP: each sign takes a key value (cost 0), or 1-2 other letters (cost 1, a value only the reading gives),
    or nothing (cost 2, unexplained). Returns [(sign, value, tag)], cost."""
    plain = f131.norm(plain); n, m = len(signs), len(plain); INF = 10**9
    best = [[INF]*(m+1) for _ in range(n+1)]; back = [[None]*(m+1) for _ in range(n+1)]; best[0][0] = 0
    for i, s in enumerate(signs):
        for j in range(m+1):
            if best[i][j] == INF: continue
            opts = [(c, 0) for c in CAND.get(s, ())] + [(plain[j:j+L], 1) for L in (1, 2) if j+L <= m] + [('', 2)]
            for val, pen in opts:
                if plain.startswith(val, j) and best[i][j] + pen < best[i+1][j+len(val)]:
                    best[i+1][j+len(val)] = best[i][j] + pen; back[i+1][j+len(val)] = (j, val, pen)
    if best[n][m] == INF: return None, INF
    pairs, j = [], m
    for i in range(n, 0, -1):
        pj, val, pen = back[i][j]; pairs.append((signs[i-1], val, 'NEW' if pen else '')); j = pj
    return pairs[::-1], best[n][m]

def emit(out, signs, plain, rid):
    letters = [s for s in signs if s != '#' and not s.startswith('<')]
    pairs, cost = align(letters, plain)
    if pairs is None:
        print('no alignment', rid, plain); out += [f'{s}\t?' for s in signs if s != '#']; return
    it = iter(pairs)
    for s in signs:
        if s == '#': continue
        if s.startswith('<'): out.append(f'{s}\t?'); continue
        sg, val, tag = next(it)
        out.append(f"{sg}\t{'?' if '?' in val else val}")
    if cost: print(rid, 'cost', cost, [(s, v) for s, v, t in pairs if t == 'NEW'])

out = ['# model: fr-1600-letters',
       '# source: ciphertext.txt + reading.tsv (f. 62), f131/ciphertext.txt + f131/reading.tsv (f. 131), aligned by a DP over key.md candidate values (+ r3708/f131 KEY); mk_validation.py',
       "# note: code numbers inside runs are '?'; f. 62 runs split into signs by key.md's rule; struck signs left out"]
for line in open(os.path.join(H, 'reading.tsv'), encoding='utf8'):
    rid, ct, rd = line.rstrip('\n').split('\t')[:3]
    signs = split62(ct.replace(' ', ''))
    if rid == 'R12': signs = ['<20>'] + split62(ct[2:])   # clear code 20 ('mais encore 20') written into the run
    plain = re.sub(r'\[?\d+m?\]?( mil)?', '', rd).replace(' ', '')   # '40 mil' = the code [40m]
    emit(out, signs, plain, rid)
ct, rd = f131.load()
for rid, signs in ct.items():
    emit(out, signs, re.sub(r'<\d+>', '', rd[rid][0]).replace(' ', ''), rid)
open(os.path.join(H, 'validation.tsv'), 'w', encoding='utf8').write('\n'.join(out) + '\n')
print(len(out) - 3, 'tokens')
