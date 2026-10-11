"""Build validation.tsv for docs/_validate.py.

Tokens: the key units of transcription/<fol>.txt, segmented longest-first exactly as decrypt.py does (bracketed
doubtful transcriptions [..] dropped, as decrypt.py drops them). Reading: the current readings
reading_152r-154r.txt + reading_154v-156v.txt, letter-aligned to the mechanical decrypt line by line (difflib):
a unit whose letter sits in an 'equal' or same-length 'replace' block gets the reading's letter; units in unequal
blocks and in [..] (unread) words get '?'. Whole-word codes (pour, roy, et, sieur) get the word when the reading
has it at that place. Null units ('-' in key.txt) are written '-'."""
import os, re, sys, unicodedata, difflib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from decrypt import lines, load_key

key = load_key(); units = sorted((k for k in key if not k.startswith('=')), key=len, reverse=True)
R = {}
for fn in ('reading_152r-154r.txt', 'reading_154v-156v.txt'):
    for l in open(os.path.join(HERE, fn), encoding='utf8'):
        if l.startswith('#') or '\t' not in l: continue
        a, b = l.rstrip('\n').split('\t', 1); R[a] = b

def nl(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if c.isascii() and (c.isalpha() or c == '#'))
    return s.replace('v', 'u').replace('j', 'i')

rows = []
for fol, n, ct in lines():
    lab = f'{fol}.{n:02d}'
    words = re.sub(r'\[[^\]]*\]', ' ', ct).replace('=', '').split()
    toks = []   # (unit, mechanical string)
    for w in words:
        if '=' + w in key: toks.append((w, key['=' + w].lower(), True)); continue
        i = 0
        while i < len(w):
            for u in units:
                if w.startswith(u, i):
                    v = key[u]; toks.append((u, '' if v == '-' else v, False)); i += len(u); break
            else:
                toks.append((w[i], '?', False)); i += 1
    rd = R.get(lab, '')
    rd = re.sub(r'\[\.\.\]', '#', rd).replace('[', '').replace(']', '')
    rn = nl(rd)
    mech = ''; spans = []
    for u, v, code in toks:
        v2 = nl(v) if v != '?' else '?'
        spans.append((len(mech), len(mech) + len(v2))); mech += v2
    val = [None] * len(mech)
    for op, a1, a2, b1, b2 in difflib.SequenceMatcher(None, mech, rn, autojunk=False).get_opcodes():
        if op == 'equal' or (op == 'replace' and a2 - a1 == b2 - b1):
            for k in range(a2 - a1):
                c = rn[b1 + k]
                val[a1 + k] = c if c != '#' else None
    for (u, v, code), (s, e) in zip(toks, spans):
        if s == e: rows.append((u, '-')); continue
        got = val[s:e]
        if code: rows.append((u, v if all(g is not None for g in got) else '?'))
        else: rows.append((u, got[0] if got[0] else '?'))
with open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf8') as f:
    f.write('# model: fr-1530-despatches\n# source: transcription/*.txt units (decrypt.py segmentation, key.txt) aligned to reading_152r-154r.txt + reading_154v-156v.txt (mk_validation.py)\n')
    f.write('# note: letters taken from the reading where it aligns with the mechanical decrypt (equal or same-length replace); else ?\n')
    for u, r in rows: f.write(f'{u}\t{r}\n')
import collections
print(len(rows), collections.Counter('read' if r not in ('?', '-') else r for u, r in rows))
