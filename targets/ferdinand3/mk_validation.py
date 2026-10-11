"""Build validation.tsv for the 1635/1640 key (R1889 + R1890). R1887 (1634, different symbol set and key) is left out.
R1889: work/align1889.txt (cipher tokens aligned with the draft R954, word by word): the draft's letter per token when
the word lengths agree, else the key value (key1889.json, 6 = e). R1890: tokens from work/parse1890.py with the
amendments and key of work/dec1890.py (key1889.json + key1890_extra.json)."""
import json, os, sys, io, contextlib, pathlib
W = pathlib.Path(__file__).parent / 'work'
os.chdir(W); sys.path.insert(0, str(W))
key = json.load(open('key1889.json')); key['6'] = 'e'
out = ['# model: la',
       '# source: R1889 work/align1889.txt (+key1889.json), R1890 work/parse1890.py tokens with work/dec1890.py key and amendments; mk_validation.py',
       '# note: R1887 (1634, other key and symbol set) not included; R1889 per-token reading = the draft R954 letter where word lengths match']
for l in open('align1889.txt', encoding='utf8'):
    if l.startswith('#') or '|' not in l: continue
    c, w = l.split('|'); c = c.split(); w = w.strip()
    if len(c) == len(w) and '?' not in w:
        out += [f'{t}\t{ch}' for t, ch in zip(c, w)]
    else:
        out += [f"{t}\t{key.get(t, '?')}" for t in c]
with contextlib.redirect_stdout(io.StringIO()):
    import dec1890 as d
for L in d.lines:
    for t in L:
        v = d.key.get(t)
        out.append(f"{t if t else '?'}\t{v if v and t else '?'}")
(W.parent / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
