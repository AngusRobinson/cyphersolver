"""Build validation.tsv: ct_neal.txt with key.json, unread spans and emendation exactly as in decode.py."""
import json, os, re, sys, pathlib
HERE = pathlib.Path(__file__).parent
src = (HERE/'decode.py').read_text(encoding='utf-8')
ns = {}
for name in ('UNREAD', 'CODELETTERS', 'EMEND'):
    m = re.search(rf'^{name} = (\{{.*?\n\}}|\{{.*?\}})', src, re.S | re.M)
    ns[name] = eval(re.sub(r'#.*', '', m.group(1)))
key = json.load(open(HERE/'key.json', encoding='utf-8'))
out = ['# model: de-1640s', '# source: ct_neal.txt + key.json, unread spans / emendation / 7xx code letters from decode.py (mk_validation.py)',
       '# note: three-digit word codes (no key) unread; S4 #20 encipherer slip read as n as in reading.md']
for l in open(HERE/'ct_neal.txt', encoding='utf-8'):
    if not l.startswith('S'): continue
    p = l.split(); s, toks = p[0], p[1:]
    for i, t in enumerate(toks):
        if len(t) == 3:
            out.append(f"{t}\t{ns['CODELETTERS'].get(t, '?')}"); continue
        un = any(a <= i <= b for a, b in ns['UNREAD'].get(s, []))
        v = ns['EMEND'].get((s, i), key.get(t, '?'))
        out.append(f"{t}\t{'?' if un else v}")
(HERE/'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
