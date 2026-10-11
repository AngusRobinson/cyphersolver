"""Build validation.tsv: tx/R*.txt cipher lines (C:) with the frozen key key.json, token by token (as read/R*.txt)."""
import json, glob, pathlib
HERE = pathlib.Path(__file__).parent
KEY = json.load(open(HERE / 'key.json', encoding='utf-8'))
out = ['# model: es-golden-age',
       '# source: tx/R985-R998.txt (C: lines) with key.json, as in read/R*.txt',
       '# note: all 14 letters; key "" = null; groups not in key.json unread']
for f in sorted(glob.glob(str(HERE / 'tx' / 'R*.txt'))):
    for line in open(f, encoding='utf-8'):
        if not line.startswith('C:'): continue
        for t in line[2:].split():
            t = t.rstrip('?')
            if not t: continue
            v = KEY.get(t)
            out.append(f'{t}\t{"?" if v is None else ("-" if v == "" else v)}')
(HERE / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(out) - 3, 'tokens')
