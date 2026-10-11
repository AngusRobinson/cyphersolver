"""Build validation.tsv from transcription/june1676_tx.txt with the key as scripts/decode.py applies it
(key_letters/key_words/key_codes + corrections.tsv, default options). One line per cipher token:
spelled-sequence numbers as '<n>' (one letter each), colon words as '<n>:', letter-prefixed codes as 'x123'.
Superscript endings (clear additions) are left out of the reading; clear text (~...~) is skipped."""
import re, csv
from pathlib import Path
B = Path(__file__).resolve().parent

def load(fn):
    d = {}
    for l in open(B / 'key' / fn, encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        p = l.rstrip('\n').split('\t')
        d[p[0]] = p[1]
    return d

L = load('key_letters.tsv'); W = load('key_words.tsv'); C = load('key_codes.tsv')
for row in csv.DictReader(open(B / 'key' / 'corrections.tsv', encoding='utf-8'), delimiter='\t'):
    code = row['code']
    (W if code.endswith(':') else C)[code.rstrip(':')] = row['reading']

def clean(v):
    v = (v or '').strip()
    if not v or v.startswith('?'): return '?'
    return re.sub(r'[\s\-]', '', v).lower()

out = ['# model: nl-modern',
       '# source: transcription/june1676_tx.txt + key/key_letters,key_words,key_codes.tsv + corrections.tsv, as scripts/decode.py (mk_validation.py)',
       '# note: 17th-century Dutch scored with the modern Dutch model (no period Dutch model); superscript endings omitted']
for line in open(B / 'transcription' / 'june1676_tx.txt', encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    lid, rest = line.split(' ', 1)
    rest = re.sub(r'~[^~]*~', ' ', rest)
    toks = re.findall(r'\[ins|\]|\{[^}]*\}(?:\^\w+)?|\d+:-?(?:\^\w+)?|[a-zA-Z]\d+(?:\^\w+)?', rest)
    for t in toks:
        if t in ('[ins', ']'): continue
        if t.startswith('{'):
            for n in re.match(r'\{([^}]*)\}', t).group(1).split(','):
                n = n.strip()
                out.append(f'{n}\t{clean(L.get(n))}')
            continue
        m = re.match(r'(\d+):', t)
        if m:
            out.append(f'{m.group(1)}:\t{clean(W.get(m.group(1)))}'); continue
        m = re.match(r'([a-zA-Z])(\d+)', t)
        k = m.group(1).lower() + m.group(2)
        out.append(f'{k}\t{clean(C.get(k))}')
(B / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(out) - 3)
