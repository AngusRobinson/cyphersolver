"""Build validation.tsv from measure.py's PASSAGES (the reading aligned sign by sign with the key.json decrypt of
cipher.txt): '{x}' = the sign read x against its key value, '?' = unread, '.' = the null vt ('-')."""
import os, re, sys
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import measure
key, L = measure.lines()
out = ['# model: it-cinquecento', '# source: cipher.txt + measure.py PASSAGES (sign-aligned reading, key.json); mk_validation.py',
       "# note: unread signs '?'; the null vt '-'"]
for name, (ls, spec) in measure.PASSAGES.items():
    toks = [t for l in ls for t in L[l]]
    units = re.findall(r'\{.\}|.', spec.replace(' ', ''))
    assert len(units) == len(toks), (name, len(units), len(toks))
    for t, u in zip(toks, units):
        v = u.strip('{}')
        out.append(f"{t}\t{'-' if v == '.' else v}")
open(os.path.join(H, 'validation.tsv'), 'w', encoding='utf8').write('\n'.join(out) + '\n'); print(len(out) - 3)
