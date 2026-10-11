"""Build validation.tsv: transcription.txt (the runs) read with key.py's KEY (9 = p, the writer's slip in 'Spork',
as decode.py reads it); codes 60 and 64 are '?'."""
import os
H = os.path.dirname(os.path.abspath(__file__))
ns = {}; exec(open(os.path.join(H, 'key.py'), encoding='utf-8').read(), ns)
out = ['# model: la', '# source: transcription.txt with key.py KEY (decode.py); mk_validation.py', '# note: codes 60, 64 unread']
for ln in open(os.path.join(H, 'transcription.txt'), encoding='utf-8'):
    if ln.startswith('#'): continue
    for t in ln.split():
        v = ns['KEY'].get(t, '?')
        out.append(f"{t}\t{'?' if v.startswith('[') else v}")
open(os.path.join(H, 'validation.tsv'), 'w', encoding='utf-8').write('\n'.join(out) + '\n'); print(len(out) - 3)
