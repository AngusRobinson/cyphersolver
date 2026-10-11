"""Build validation.tsv for R9412 (German, ff. 250-251, 573 of the 929 cipher words; the dominant letter).

Signs: r9411/transcription_r9412.txt. Per-sign values: the key at the head of r9411/run_r9412_final.txt (the R9411
key refitted on German), '_' = null ('-'). The current reading r9411/reading_r9412.txt (read from that decrypt by
hand) is aligned to the signs line by line by a DP (key values and the polyphones in NOTES at no cost, other
letters at a cost); each sign takes the reading's letters it is aligned to. Signs under [..] (unread), [x] (supplied from sense), <...> (conjecture) or a dropped letter
are '?'. Clear text ({..} in the transcription; CAPS and (..) in the reading) is left out.
R9411 (Latin, 356 words) is left out: one validation file takes one language."""
import re, os, difflib
H = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'r9411')

head = open(os.path.join(H, 'run_r9412_final.txt'), encoding='utf-8').readline().split()
KEY = dict(kv.split('=', 1) for kv in head if '=' in kv)

def letters(s): return re.sub(r'[^a-zäöüß§]', '', s.lower())

reading = {}
for ln in open(os.path.join(H, 'reading_r9412.txt'), encoding='utf-8'):
    m = re.match(r'\s*(\d+)\s+(.*)', ln.rstrip('\n'))
    if not m or ln.startswith('#'): continue
    r = m.group(2)
    r = re.sub(r'<[^>]*>', '§', r)
    r = re.sub(r'\[[^\]]*\]', '§', r)
    r = re.sub(r'\([^)]*\)', ' ', r)
    r = re.sub(r'\b[A-Z][A-Z]+\b', ' ', r)
    r = r.replace('Eurn G.', 'eurng').replace('E. G.', 'eg')
    reading[int(m.group(1))] = letters(r)

# polyphones named in NOTES (π b/w/o, 4 e/i, ∃ d/ch, double stem H u/v/k/g) in this transcription's codes
POLY = {'n': ['b', 'w', 'o'], '4': ['e', 'i'], 'E': ['d', 'ch'], 'H': ['u', 'v', 'k', 'g']}
def cands(t):
    c = set(POLY.get(t, []))
    v = KEY.get(t)
    if v and v != '_': c.add(v)
    return c

def align(signs, plain):
    """DP: a sign takes a key/polyphone value (cost 0), one or more '§' (unread) letters (cost 0, written '?'),
    1-3 other letters (cost 1: the reading's value against the key), or nothing (cost 0 for a key null, else 2)."""
    n, m = len(signs), len(plain); INF = 10**9
    best = [[INF]*(m+1) for _ in range(n+1)]; back = [[None]*(m+1) for _ in range(n+1)]; best[0][0] = 0
    for i, s in enumerate(signs):
        for j in range(m+1):
            if best[i][j] == INF: continue
            opts = [(c, 0) for c in cands(s)] + [(plain[j:j+L], 1) for L in (1, 2, 3) if j+L <= m]
            opts.append(('', 0 if KEY.get(s) == '_' else 2))
            k = j
            while k < m and plain[k] == '§': k += 1
            if k > j: opts += [(plain[j:jj], 0) for jj in range(j+1, k+1)]
            for val, pen in opts:
                if plain.startswith(val, j) and best[i][j] + pen < best[i+1][j+len(val)]:
                    best[i+1][j+len(val)] = best[i][j] + pen; back[i+1][j+len(val)] = (j, val)
    if best[n][m] == INF: return None
    pairs, j = [], m
    for i in range(n, 0, -1):
        pj, val = back[i][j]; pairs.append((signs[i-1], val)); j = pj
    return pairs[::-1]

out = ['# model: de-1500s',
       '# source: r9411/transcription_r9412.txt + key of r9411/run_r9412_final.txt, aligned sign by sign (DP over the key and the NOTES polyphones) to r9411/reading_r9412.txt; mk_validation.py',
       "# note: R9412 (German) only; R9411 (Latin, same key) left out; signs under [..], supplies [x] and <conjectures> are '?'"]
for ln in open(os.path.join(H, 'transcription_r9412.txt'), encoding='utf-8'):
    m = re.match(r'(\d+)\s+(.*)', ln.rstrip('\n'))
    if not m: continue
    n = int(m.group(1))
    body = re.sub(r'\{[^}]*\}', ' ', m.group(2))
    signs = [t for t in body.split() if t != ':']
    rd = reading.get(n, '')
    pairs = align(signs, rd)
    if pairs is None:
        out += [f'{t}	?' for t in signs]; continue
    for t, v in pairs:
        out.append(f"{t}	{'-' if v == '' and KEY.get(t) == '_' else '?' if (not v or '§' in v) else v}")
open(os.path.join(os.path.dirname(H), 'validation.tsv'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(out) - 3, 'tokens')
