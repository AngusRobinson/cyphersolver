"""Build validation.tsv for docs/_validate.py from runs.txt (sign-level transcription of 22 runs, ff. 80, 88, 92).

The reading is word-level (READING.md, graded H/M/I). A cipher word is given its reading letter by letter only where
READING.md (consolidated + second full-resolution pass) gives the word at grade H or M AND its sign count equals the
letter count, so the alignment is unambiguous; two exceptions: f88e 'Ah7V' read 'there' (H) and f80c 'Ah7A'
read 'these' (the solver drops final e) are written t-h-e-r and t-h-e-s. Every other sign is '?': unread words, I-grade guesses (Naples, Portugals, Bruges, Brede),
words whose length does not match the signs (letters, charge, arriving, subiects), and code signs ([◻], 7 = the
Queen). ff. 96-97 are not in runs.txt and are left out."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
READ = {  # (run, word index) -> reading
    ('f80a', 0): 'in', ('f80a', 1): 'the',
    ('f80b', 0): 'not', ('f80b', 1): 'be', ('f80b', 3): 'the', ('f80b', 4): 'haven', ('f80b', 5): 'is',
    ('f80c', 4): 'to', ('f80c', 5): 'thes', ('f80c', 6): 'termes',
    ('f80d', 0): 'armada',
    ('f80e', 0): 'armad',
    ('f80g', 0): 'forwarde',
    ('f80h', 0): 'action',
    ('f88a', 0): 'captain',
    ('f88c', 0): 'the', ('f88c', 1): 'haven',
    ('f88d', 0): 'rain', ('f88d', 1): 'spoil',
    ('f88h', 1): 'italians',
    ('f88i', 3): 'antonio',
    ('f88e', 1): 'ther',
}
rows = []
for line in open(os.path.join(HERE, 'runs.txt'), encoding='utf8'):
    if line.startswith('#') or '|' not in line: continue
    rid, b, w, a = [x.strip() for x in line.split('|')]
    for wi, word in enumerate(w.split()):
        if word.startswith('['): rows.append((word, '?')); continue
        r = READ.get((rid, wi))
        if r is not None: assert len(r) == len(word), (rid, wi, word, r)
        for k, s in enumerate(word): rows.append((s, r[k] if r else '?'))
with open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf8') as f:
    f.write('# model: en-modern\n# source: runs.txt signs with the H/M word readings of READING.md where sign count = letter count (mk_validation.py)\n')
    f.write('# note: word readings come from a candidate-set word solver plus context; letter alignment is by position within the word\n')
    for s, r in rows: f.write(f'{s}\t{r}\n')
print(len(rows), sum(r != '?' for s, r in rows))
