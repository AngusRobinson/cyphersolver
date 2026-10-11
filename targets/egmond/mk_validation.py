"""Build validation.tsv for egmond: body_revision3.txt with the two raised insertions in place (as decode_audited.py),
then the address (address_audited.json); values from audited_key.json / the address key."""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent
key = json.loads((root / 'audited_key.json').read_text(encoding='utf-8'))['tokens']
lines = (root / 'body_revision3.txt').read_text().splitlines()
out = ['# model: fr-1530-despatches', '# source: body_revision3.txt + insertion7/15.json + address_audited.json with audited_key.json (as decode_audited.py), mk_validation.py',
       '# note: French, 1530s']
anchors = {7: ['B', 'V', 'CE'], 15: ['J', 'V', 'CE']}
for n, line in enumerate(lines, 1):
    toks = line.split()
    if n in anchors:
        a = anchors[n]
        i = [i for i in range(len(toks) - len(a) + 1) if toks[i:i + len(a)] == a][0]
        ins = json.loads((root / f'insertion{n}.json').read_text())['tokens']
        toks = toks[:i] + ins + toks[i:]
    out += [f'{t}\t{key[t] or "-"}' for t in toks]
address = json.loads((root / 'address_audited.json').read_text(encoding='utf-8'))
for line in address['lines']:
    out += [f'A:{t}\t{address["key"][t] or "-"}' for t in line]
(root / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(out) - 3)
