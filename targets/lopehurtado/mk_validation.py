"""Build validation.tsv from the token/value line pairs of the code blocks in read_r9649.md (R9649, the one letter
read in full, from its own contemporary clear f. 268). '∅' (the run-opening mark) is a null; '?' unread.
The other letters are read line by line in prose (r96xx_reading.tsv) with no token alignment and are not included."""
import re, pathlib
H = pathlib.Path(__file__).parent
blocks = re.findall(r'```\n(.*?)```', (H / 'read_r9649.md').read_text(encoding='utf-8'), re.S)
out = ['# model: es-golden-age', '# source: read_r9649.md code blocks (token line / value line pairs) (mk_validation.py)',
       '# note: R9649 only; the other Lope Hurtado letters have no token-level alignment in the folder']
for b in blocks:
    ls = [l for l in b.splitlines() if l.strip()]
    for t, v in zip(ls[::2], ls[1::2]):
        t, v = t.split(), v.split()
        assert len(t) == len(v), (t, v)
        out += [f"{a}\t{'-' if c == '∅' else re.sub(r'\(.*?\)', '', c)}" for a, c in zip(t, v)]
(H / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
