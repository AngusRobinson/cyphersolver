"""Build validation.tsv for armstrong: every code group of the 14 despatches in despatches.py, in order, with the
value despatches.py renders for it (pencil H, known plaintext C, M, inferred, additions, multi-group CONTEXT values).
The git-ignored inputs (fo/*.html, fix972.json, sense972.json) are read from the main checkout when absent here."""
import builtins, os, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
MAIN = pathlib.Path('C:/Users/dbour/cypher/targets/armstrong')
os.chdir(HERE); sys.path.insert(0, str(HERE))
_open = builtins.open
_exists = os.path.exists
def _redir(f, *a, **k):
    s = str(f).replace(chr(92), '/')
    if not _exists(s) and (s.startswith('fo/') or s in ('fix972.json', 'sense972.json')):
        f = MAIN / s
    return _open(f, *a, **k)
builtins.open = _redir
os.path.exists = lambda p: _exists(p) or (str(p) in ('fix972.json', 'sense972.json') and _exists(MAIN / str(p)))
import despatches as P

def val(r):
    r = r.strip()
    if not r or '(null)' in r or not re.search(r'[A-Za-z]', r):
        return '-'
    return r
lines = ['# model: en-modern',
         '# source: despatches.py (14 THE=972 despatches, 1807-1810, incl. the 30 Aug 1808 PS) via mk_validation.py',
         '# note: one-part-ish nomenclator code; a token is a code group, reading = the syllable/word despatches.py gives it; '
         'punctuation and (null) values as -; unread groups ?']
n = 0
for key in P.DESPATCHES:
    segs = P.groups_of(key)
    for k, v in segs:
        if k != 'c':
            continue
        ctx = {}
        ints = [(p, g) for p, g in enumerate(v) if isinstance(g, int)]
        for q in range(len(ints)):
            for pat, vals in P.CONTEXT.items():
                if tuple(g for _, g in ints[q:q + len(pat)]) == pat:
                    for t, (p, _) in enumerate(ints[q:q + len(pat)]):
                        ctx[p] = vals[t]
        for p, g in enumerate(v):
            if not isinstance(g, int):
                continue
            if p in ctx:
                r = ctx[p]
            else:
                r, c = P.reading(g)
            lines.append(f'{g}\t{"?" if r is None else val(r)}'); n += 1
(HERE / 'validation.tsv').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(n, 'groups')
