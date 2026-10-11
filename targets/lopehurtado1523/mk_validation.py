"""Build validation.tsv for docs/_validate.py: every cipher token of the eight letters with the value
decode_merged.py gives it from key_merged.tsv (confirmed and probable entries; 'possible'/'rejected' are dropped there).
Compound tokens that decode_merged splits into keyed signs are written one sign per line. Unkeyed tokens are '?'.
Values: i/j -> i, u/v -> u; other two-way values '?'; V.Md -> vuestra magestad, ReyFr/ReyIng -> rey de francia/inglaterra;
a trailing '-' (word part) is dropped."""
import os, sys, re, io
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
so = sys.stdout
import decode_merged as dm
sys.stdout = so

def val(p):
    p = {'V.Md': 'vuestra magestad', 'ReyFr': 'rey de francia', 'ReyIng': 'rey de inglaterra'}.get(p, p)
    p = p.replace('_', ' ').rstrip('-').lstrip('-')
    if p in ('i/j', 'j/i'): return 'i'
    if p in ('u/v', 'v/u'): return 'u'
    if '/' in p or '?' in p or not p.strip(): return '?'
    return p

K = dm.load_key()
rows = []
for rec, lines in dm.letters().items():
    for lab, s in lines:
        for t in dm.tokens(s):
            if t == '|': continue
            if t in K: rows.append((t, val(K[t][0])))
            else:
                seg = dm.segment(t, K)
                if seg:
                    i = 0
                    while i < len(t):          # re-run the greedy split to keep the sign names
                        for j in range(len(t), i, -1):
                            if t[i:j] in K: rows.append((t[i:j], val(K[t[i:j]][0]))); i = j; break
                else: rows.append((t, '?'))
with io.open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf8') as f:
    f.write('# model: es-golden-age\n# source: transcriptions read by decode_merged.py (r9683/r9695/r9867/r9846/r9667_cipher.txt, read_r9866/68/69.md) with key_merged.tsv (mk_validation.py)\n')
    f.write('# note: reading = the merged key applied token by token (confirmed + probable values), as decode_merged.py prints it; read in part\n')
    for t, v in rows: f.write(f'{t}\t{v}\n')
sys.stderr.write('%d tokens, %d valued\n' % (len(rows), sum(v != '?' for t, v in rows)))
