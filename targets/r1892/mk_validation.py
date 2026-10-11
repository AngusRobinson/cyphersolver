"""Build validation.tsv from transcription_p1.txt (French, the dominant page) with apply.py's tokens() and key
(FRENCH on: pair 12 = z). Word signs carry their apply.py SIGNS value; unread pairs/signs are '?'.
Page 2 (Dutch postscript, 900 tokens) is left out: one model per test, and p1 is the larger page."""
import os, sys
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import apply
apply.FRENCH = True
out = ['# model: fr-modern',
       '# source: transcription_p1.txt through apply.py tokens() (key K + 12=z, word-sign table SIGNS); mk_validation.py',
       '# note: page 1 only (French, 1,054 tokens); the Dutch postscript p2 (900 tokens) is left out as a second language']
for line in open(os.path.join(H, 'transcription_p1.txt'), encoding='utf8'):
    for kind, lab, v in apply.tokens(line):
        if kind == 'note': continue
        out.append(f"{lab}\t{v if v else '?'}")
open(os.path.join(H, 'validation.tsv'), 'w', encoding='utf8').write('\n'.join(out) + '\n'); print(len(out) - 3)
