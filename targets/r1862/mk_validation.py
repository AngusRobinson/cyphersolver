"""Build validation.tsv for r1862: every group of tx/groups.txt in order, as written, with decode.py's value
(KEY from ../r1874/key2.json + key_over.json). A clerk's slip (key_over _slips) keeps its written digits as the
token and takes the value he meant; empty values (declared nulls) are '-'; groups without a value are '?'."""
import os, re, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent; os.chdir(HERE); sys.path.insert(0, str(HERE))
import decode as D
out = ['# model: it-cinquecento', '# source: tx/groups.txt with decode.py KEY (r1874 key2.json + key_over.json), mk_validation.py',
       '# note: Italian 1628; clerk slips listed in key_over _slips keep the written group with the meant value']
for l in open('tx/groups.txt', encoding='utf8'):
    m = re.match(r'(P\d L\d+[a-z]?):\s*(.*)', l)
    if not m:
        continue
    lab, body = m.groups(); gi = 0
    for part in re.split(r'(\[CLEAR:[^\]]*\])', body):
        if part.startswith('[CLEAR'):
            continue
        for g in part.split():
            g = re.sub(r'[?^]', '', g)
            s = D.SLIPS.get(f'{lab}:{gi}')
            v = s[1] if s else D.KEY.get(g)
            out.append(f'{g}\t{"?" if v is None else (v or "-")}')
            gi += 1
pathlib.Path('validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(out) - 3)
