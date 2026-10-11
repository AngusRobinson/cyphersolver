"""Build validation.tsv from final_v9.txt (the current reading, measured by measure_sense.py).

final_v9.txt gives per line the token list and the reading as text, not token by token, so the reading is aligned
to the tokens here by a small dynamic programme using key_v6.md + key_v7_codes.md (+ shape_pass.md labels):
each token either is a null, emits one letter, emits its code word, emits an unlisted multi-letter value, or takes
one of the [?n] unread slots. Letters the key does not allow cost more, so the alignment follows the key where it can
and the reading text always. The reading is not changed: every letter of the line's reading is assigned to some token
(or, at a cost, left over where the reading supplies letters with no cipher sign).
Clear text in [..] (both sides) and parenthetical supplied/normalised letters '(..)' are dropped; tentative {w:n}
readings are kept as readings.
"""
import re
from pathlib import Path
B = Path(__file__).resolve().parent

NULLS = {'3', '-2', 'r', 'q=', '9', 'ft', 'xo', 'rho', 'd+', '0', 'th', '3r', 'tl', 'XX', 't~', 'CURL_D', 'CURL_D_BAR',
         'X_HOOK', 'NULL_DAG', 'NULL_LOOP', 'NULL_LOOP_BAR', 'e', '3=', 'r.', 'E_DOT'}
LET = {}
txt = (B / 'key_v6.md').read_text(encoding='utf-8')
for m in re.finditer(r'^- ([a-z/]+) = (.*)$', txt, re.M):
    letters = m.group(1).split('/')
    for item in m.group(2).split(', '):
        lab = item.strip().split(' ')[0].strip('`')
        if lab:
            LET.setdefault(lab, set()).update(letters)
LET.setdefault('>', set()).add('o'); LET.setdefault('C_X', set()).add('s'); LET.setdefault('C_U', set()).update('uv')
CODES = {
    '-w': ['the'], 'AND': ['and'], 'B': ['of'], 'B.': ['of'], '.B': ['not'], 'B=': ['shall'], 'B_': ['should'],
    'D': ['to'], 'Y_SCRIPT.': ['to'], 'D=': ['what'], 'D_': ['was'], 'EE': ['were', 'a'], 'EE=': ['where'],
    'EE_': ['will'], 'S_DOTBELOW': ['would', 'will'], 'A=': ['me'], 'G=': ['who'], 'H=': ['in'], 'H_': ['with'],
    'o_': ['have'], 'o=': ['had'], 'O_SMALL': ['hath'], 'q)': ['it'], 'Q': ['is'], 'Q_CIRC': ['is'], '/': ['he'],
    '-4': ['that'], '4': ['that'], '.Z': ['that'], 'Y_SCRIPT_CROSS': ['that'], 'p)': ['this'], 'Ap': ['none'],
    'f': ['be'], '.f': ['be'], 'L_DOTS': ['be'], 'll_BAR': ['they'], 'Y_LATIN': ['for'], 'Y_ETA_UL': ['for'],
    'Y_ETA': ['us'], 'n=_BAR': ['but'], '2.': ['i'], 'Ie': ['i', 'theemperorsambassador'], 'q': ['him'],
    'N.': ['them'], 'D.': ['out'], 'k': ['fair'], 'l': ['words'], 'G': ['thecouncil'], '.G.': ['thecouncil'],
    'cup': ['france'], 'C.': ['thecourt', 'thesaid'], 'C:': ['thatthey'], 'OMEGA_BAR': ['whereunto'],
    'w=': ['whereunto'], 'Too': ['theconstable'], 'n': ['carew'], 'n=': ['therebels'],
    'CIRC_DOT': ['thefrenchking'], 'CIRC_LOOP': ['yourhighness'], 'CIRC_RING': ['theprinceofspain', 'yourhighness'],
    'O_BIG': ['theemperor', 'theemperors'], 'O': ['theemperor'], 'O_DOTABOVE': ['theemperor'],
    'O_DOTBEFORE': ['theemperor'], 'box': ['thelowcountries'], 'CROWNED_BOX': ['england'],
    'E_DOTBEFORE': ['monsieurde'], 'T.': ['me'], 'L2': ['calais'], 'S,': ['be'], '9..': ['it'],
}
UNK = '\x01'


def reading_units(rd):
    rd = re.sub(r'\[\?(\d+)\]', lambda m: UNK * int(m.group(1)), rd)
    rd = re.sub(r'\[[^\]]*\]', ' ', rd)                    # clear text
    rd = re.sub(r'\{([^}:]*):\d+\}', r'\1', rd)             # tentative kept
    rd = re.sub(r'\([^)]*\)', '', rd)                       # supplied / normalised letters
    return [c for c in rd.lower() if c.isalpha() or c == UNK]


def align(toks, chars):
    n, m = len(toks), len(chars)
    INF = 1e9
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    P = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            d = D[i][j]
            if d >= INF: continue
            if j < m:   # reading letter with no cipher token (supplied)
                c = 1.5 if chars[j] != UNK else 3
                if d + c < D[i][j + 1]: D[i][j + 1] = d + c; P[i][j + 1] = (i, j, None)
            if i == n: continue
            t = toks[i]
            opts = [(0, '-', 0 if t in NULLS else 3)]
            if j < m:
                ch = chars[j]
                if ch == UNK:
                    opts.append((1, '?', 0 if t not in NULLS else 1))
                else:
                    allowed = LET.get(t)
                    c = 0 if allowed and ch in allowed else (1.2 if not allowed and t not in CODES else 2)
                    if t in NULLS: c = max(c, 2)
                    opts.append((1, ch, c))
            for w in CODES.get(t, []):
                if ''.join(chars[j:j + len(w)]) == w: opts.append((len(w), w, -0.5))
            for k in range(2, 6):   # unlisted multi-letter value (code word not in the table)
                if j + k <= m and UNK not in chars[j:j + k]:
                    opts.append((k, ''.join(chars[j:j + k]), 2.5 + 0.6 * k))
            for k, val, c in opts:
                if d + c < D[i + 1][j + k]: D[i + 1][j + k] = d + c; P[i + 1][j + k] = (i, j, val)
    out, i, j = [], n, m
    while (i, j) != (0, 0):
        pi, pj, val = P[i][j]
        if pi != i: out.append((toks[pi], val))
        i, j = pi, pj
    return list(reversed(out)), D[n][m]


out = ['# model: en-1640s',
       '# source: final_v9.txt (current reading, measure_sense.py), aligned to tokens with key_v6.md/key_v7_codes.md by mk_validation.py',
       '# note: reading given per line as text; token alignment is a DP fit (see mk_validation.py); tentative {..} readings kept, [?n] unread; bracketed nulls dropped']
total = 0
for L in open(B / 'final_v9.txt', encoding='utf-8'):
    m = re.match(r'(p\d\.\d\d) \| (.*?) \|\| (.*)', L)
    if not m: continue
    ln, tok, rd = m.groups()
    toks = [x for x in re.sub(r'\[[^\]]*\]', ' ', tok).replace('(q)', 'Q').split() if x not in ('.', ':', '..')]
    pairs, cost = align(toks, reading_units(rd))
    total += cost
    out += [f'{t}\t{v}' for t, v in pairs]
(B / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(out) - 3, 'tokens; alignment cost', round(total, 1))
