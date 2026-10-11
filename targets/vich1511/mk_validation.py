"""Build validation.tsv for docs/_validate.py: the three letters read here (N.45, N.57, N.60; the v2
transcriptions that measure.py counts), every token with its decode.py value (LET letters, CODE words/syllables).
Tokens decode.py does not know, and doubtful tokens marked 'x?', are '?' (as measure.py counts them).
The siblings with clerk decipherments (N.12, N.39, N.41) and N.73 (other key) are left out."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from decode import LET, CODE
rows = []
for f in ('n45_pp03-09_v2.txt', 'n45_pp10-15_v2.txt', 'n57_transcription_v2.txt', 'n60_transcription_v2.txt'):
    for l in open(os.path.join(HERE, f), encoding='utf-8'):
        if not l.startswith('L'): continue
        for x in l.split(':', 1)[1].split():
            v = CODE.get(x) or LET.get(x) or '?'
            rows.append((x, v.replace('ñ', 'n') if v != '?' else '?'))
with open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf-8') as f:
    f.write('# model: es-golden-age\n# source: n45_pp03-09_v2.txt, n45_pp10-15_v2.txt, n57_transcription_v2.txt, n60_transcription_v2.txt with decode.py (LET + CODE) (mk_validation.py)\n')
    f.write('# note: nomenclator: code groups carry whole words or syllables; N.60 context-forced groups (flort liga, fiy favor, mat obligado) are in decode.py and so included\n')
    for t, v in rows: f.write(f'{t}\t{v}\n')
print(len(rows), sum(v != '?' for t, v in rows))
