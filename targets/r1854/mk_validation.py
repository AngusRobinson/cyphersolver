"""Build validation.tsv: each read image's sign transcription with the key its reading file names
(show.py logic): P2 p2v3.txt + key7.txt; P3 p3_signs.txt + key3_p3.txt; P4 p4v2.txt and P5 p5v2.txt + key4_v2.txt.
P1 (no reading) left out. Tokens carry the image prefix (P2:, P3:, P45:) because each image has its own key.
'_' key values are nulls ('-'); '?' signs and unknown signs are '?'. Code ARW = cardinalis (reading_p2.md), ARO unread."""
import os, re
H = os.path.dirname(os.path.abspath(__file__))

def key(fn):
    k = {}
    for l in open(os.path.join(H, fn), encoding='utf-8'):
        l = l.strip()
        if '=' in l and not l.startswith('//') and not l.startswith('#'):
            a, v = l.rsplit('=', 1); k[a.strip()] = v.strip()
    return k

def val(v):
    if v is None or v.startswith('[?') or v in ('?', '°'): return '?'
    if v == '_': return '-'
    return re.sub(r'[^a-zà-ÿ]', '', v.lower()) or '?'

out = ['# model: la', '# source: p2v3.txt+key7.txt, p3_signs.txt+key3_p3.txt, p4v2.txt/p5v2.txt+key4_v2.txt (show.py logic; mk_validation.py)',
       '# note: P2, P4, P5 Latin; P3 (894 signs) Italian, scored with the Latin model as the dominant language; P1 unread, omitted; tokens prefixed by image (separate keys)']
for pre, tf, kf in (('P2', 'p2v3.txt', 'key7.txt'), ('P3', 'p3_signs.txt', 'key3_p3.txt'),
                    ('P45', 'p4v2.txt', 'key4_v2.txt'), ('P45', 'p5v2.txt', 'key4_v2.txt')):
    K = key(kf)
    if pre == 'P2': K['ARW'] = 'cardinalis'; K['ARO'] = '?'
    for l in open(os.path.join(H, tf), encoding='utf-8'):
        if not l.startswith('L') or ':' not in l: continue
        rest = l.split(':', 1)[1]
        rest = re.sub(r'\{[^}]*\}', ' ', rest)
        for t in rest.split():
            t = t.split('/')[0] if pre == 'P3' and '/' in t and len(t) > 1 else t
            if t == '_' : continue          # separator point, not a sign
            if t == '?': out.append(f'{pre}:?\t?'); continue
            out.append(f'{pre}:{t}\t{val(K.get(t))}')
open(os.path.join(H, 'validation.tsv'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
import collections
print(len(out) - 3, collections.Counter(x.split(':')[0] for x in out[3:]))
