"""Build validation.tsv for R9426 (transcription.txt) and R9425 (r9425/transcription.txt), mirroring count.py and
r9425/count_r9425.py: letter tokens with key.txt, initials read, codes read only where established (R9426: 248 = und;
R9425: codes.txt null/fixed), words the counts call unread left '?'. Separators z/c and the '-' sign are left out."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..')); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, 'r9425'))
from solve import parse, is_code
from decode import dec, K
import count, count_r9425
from decode_r9425 import load_codes
C25 = load_codes()
out = ['# model: de-1640s',
       '# source: transcription.txt + r9425/transcription.txt, key.txt (decode.py), codes as counted in count.py / r9425/count_r9425.py',
       '# note: separators z/c (word ends) and the line-end sign omitted; R9426 codes other than 248 left unread as recorded; '
       'R9425 words with a doubtful token (DOUBTFUL) left unread whole']
def run(path, codes, unread_words):
    for lid, items in parse(path):
        for it in items:
            if it[0] != 'word': continue
            w = it[1]
            if is_code(w):
                for t in w:
                    if t in K and len(w) == 1: out.append(f'{t}\t{K[t]}'); continue
                    v = codes.get(t)
                    out.append(f'{t}\t{v if v else "?"}')
            else:
                d = dec(w)
                bad = d in unread_words
                for t in w: out.append(f'{t}\t{"?" if bad or t not in K else K[t]}')
run(os.path.join(HERE, 'transcription.txt'), dict(count.CODES_READ), count.UNREAD_WORDS)
run(os.path.join(HERE, 'r9425', 'transcription.txt'),
    {k: v[0].split(" [")[0] for k, v in C25.items() if v[1] in ('null', 'fixed')}, set(count_r9425.DOUBTFUL))
open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(out) - 3)
