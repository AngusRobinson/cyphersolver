"""Build validation.tsv for docs/_validate.py: ct2.txt parsed exactly as decode.py does (5 = separator, dropped;
8XXX = code word; 2-digit groups = letters/syllables; a lone digit = punctuation, dropped). Values: DIN, CODE and
CODE_GUESS (the code words the NOTES plaintext prints in parentheses); code groups left as [8xxx] are '?'."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE); sys.path.insert(0, HERE)
from decode import DIN, CODE, CODE_GUESS, load
code = dict(CODE, **CODE_GUESS)
rows = []
for r in load().split('5'):
    i = 0
    while i < len(r):
        if r[i] == '8' and i + 4 <= len(r):
            c = r[i:i+4]; rows.append((c, code.get(c, '?').lower())); i += 4
        elif i + 2 <= len(r):
            g = r[i:i+2]; rows.append((g, DIN.get(g, '?'))); i += 2
        else: i += 1
with open('validation.tsv', 'w', encoding='utf-8') as f:
    f.write('# model: it-modern\n# source: ct2.txt (with the print-error fix in decode.load) and decode.py DIN + CODE + CODE_GUESS (mk_validation.py)\n')
    f.write('# note: syllabic dinomes and a one-part code; code words read from context (CODE_GUESS) counted as read, as in the NOTES plaintext\n')
    for t, v in rows: f.write(f'{t}\t{v}\n')
print(len(rows), sum(v != '?' for t, v in rows))
