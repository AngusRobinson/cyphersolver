"""Build validation.tsv for docs/_validate.py: every cipher sign of ff. 133-134 and f. 139 paired with the letter
the project's reading gives it, using decode.py's own alignment (reading.tsv / reading_f139.tsv). Code numbers
inside runs are written with '?' (their meaning is only partly identified)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import decode

out = ['# model: fr-1600-letters',
       '# source: ciphertext.txt + reading.tsv, ciphertext_f139.txt + reading_f139.tsv, aligned by decode.align (mk_validation.py)',
       '# note: polyphonic signs (9 = a/h/r etc.); code numbers inside runs left unread (?)']
for part in ('', 'f139'):
    ct, rd = decode.runs(part)
    for rid, signs in ct.items():
        pairs, left = decode.align(signs, rd[rid][0].replace(' ', ''), rid)
        for s, p, c in pairs:
            out.append(f'<{s.strip("<>")}>\t?' if c == 'code' else f'{s}\t{p}')
open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf8').write('\n'.join(out) + '\n')
print(len(out) - 3, 'tokens')
