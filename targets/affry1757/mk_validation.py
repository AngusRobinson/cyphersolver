"""Build validation.tsv for docs/_validate.py: the code groups of the letters read here (not the eight with Lyonet's
decipherment, not R1071 in code C), in text order, with the value measure_sense.py gives them: key_X.json, then
key_M.json, then H/M inferred values in read/*_new.tsv; 105, 107 and groups valued 'null' or '.' are nulls ('-'); groups with no value '?'.
Groups from the image re-transcriptions transcr/R*.txt where they exist, else view.load('U') (DECODE parse)."""
import os, sys, json, glob
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); os.chdir(HERE)
from view import load
key = json.load(open('key_M.json', encoding='utf8'))
ext = json.load(open('key_X.json', encoding='utf8')) if os.path.exists('key_X.json') else {}
inf = {}
for f in sorted(glob.glob('read/*_new.tsv')):
    for line in open(f, encoding='utf8'):
        p = line.rstrip('\n').split('\t')
        if len(p) >= 3 and p[0].strip().isdigit() and p[2].strip()[:1] in 'HM' and p[2].strip():
            inf.setdefault(p[0].strip(), p[1].split('/')[0].strip())
LYONET = {'R1052', 'R1053', 'R1062', 'R1063', 'R1065', 'R1066', 'R1069', 'R1075'}
NULLS = {'105', '107'}
def val(g):
    g = str(g)
    if g in NULLS: return '-'
    v = ext.get(g) or key.get(g) or inf.get(g)
    if v is None or '?' in v or not v.strip(): return '?'
    if v.strip() in ('null', '.'): return '-'
    return v.strip().strip('{}')
U = load('U')
for f in glob.glob('transcr/R*.txt'):
    r = os.path.basename(f)[:-4]
    U[r] = [int(t.split('|')[0]) for line in open(f, encoding='utf8') if not line.startswith('#') for t in line.split()]
rows = []
for r in sorted(U):
    if r in LYONET: continue
    rows.append(('#', r))
    for g in U[r]: rows.append((str(g), val(g)))
with open('validation.tsv', 'w', encoding='utf8') as f:
    f.write('# model: fr-modern\n# source: transcr/R*.txt (else cipher_U via view.load) with key_X.json, key_M.json, read/*_new.tsv H/M values, as measure_sense.py (mk_validation.py)\n')
    f.write('# note: word-and-syllable code; Lyonet-deciphered letters and R1071 (code C) left out\n')
    for t, v in rows: f.write(f'# {v}\n' if t == '#' else f'{t}\t{v}\n')
print(sum(t != '#' for t, v in rows), sum(t != '#' and v not in '?-' for t, v in rows))
