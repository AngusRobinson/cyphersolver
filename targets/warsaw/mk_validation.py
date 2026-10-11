"""Build validation.tsv for warsaw (R1408) from decode.py's tokens (image corrections applied) and key.
Nulls a m p n -> '-'; the word codes (three-figure groups, glossed from context only) and {03} {04} -> '?'."""
import os, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent; os.chdir(HERE); sys.path.insert(0, str(HERE))
import decode as D
out = ['# model: it-cinquecento', '# source: ct.txt via decode.py tokens() (IMAGE_FIX applied) and its key, mk_validation.py',
       '# note: Italian 1627; nulls a m p n as -; the ten word codes (context glosses, not read) and 03 04 unread']
for t in D.tokens():
    if t in D.NULLS: v = '-'
    elif t in D.PAIRS: v = D.PAIRS[t]
    elif t in D.CODES: v = '?'
    elif t in D.SYLL: v = '?' if D.SYLL[t].startswith('{') else D.SYLL[t]
    elif t in D.ALPHA: v = D.ALPHA[t]
    else: v = '?'
    out.append(f'{t}\t{v}')
pathlib.Path('validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
