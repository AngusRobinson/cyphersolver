"""Build validation.tsv for kurtz1639: every cipher token of the tr/ transcriptions (records in decode.py's order),
with the value decode.py gives it (key.json via solve2.value). '' (null) -> '-', '?' or uncertain tokens -> '?'."""
import os, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent; os.chdir(HERE); sys.path.insert(0, str(HERE))
from parse import files, tokens_of
from solve2 import value
from decode import loadkey
h, s = loadkey()
out = ['# model: de-1640s', '# source: tr/IMG_*.txt with key.json, as decode.py (mk_validation.py)',
       '# note: German 1638-39; tokens struck (~) or marked uncertain (?) in the transcription are skipped / unread']
for rec in ['R3812', 'R3811', 'R3813', 'R3814', 'R3815', 'R4625', 'R4645', 'R4734', 'R4736']:
    for f in files([rec]):
        for line in open(f, encoding='utf-8'):
            t = line.strip()
            if not t or t == '#' or t.startswith('#'):
                continue
            for it in tokens_of(t):
                if it[0] == 'clear':
                    continue
                tok = it[1]
                if tok.startswith('~') or tok in ('/', '#ins'):
                    continue
                v = value(tok, h, s) if '?' not in tok else '?'
                out.append(f'{tok}\t{"-" if v == "" else v}')
pathlib.Path('validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(out) - 3)
