"""Build validation.tsv from f59_r7772.txt: the only sign-level transcription in the folder (R7772 f. 59, 126 signs),
paired letter for letter with its decrypt lines (one sign = one letter). The other passages are kept only as
deciphered letters (reading.txt), so they cannot be tested without rebuilding the cipher from the reading."""
import re, pathlib
H = pathlib.Path(__file__).parent
L = (H / 'f59_r7772.txt').read_text(encoding='utf-8').split('# decrypt')
ct = re.findall(r'^L\d: (.*)$', L[0], re.M); pt = re.findall(r'^L\d: (.*)$', L[1], re.M)
out = ['# model: en-1640s', '# source: f59_r7772.txt sign lines L1-L4 paired with its decrypt lines (mk_validation.py)',
       '# note: f. 59 only (the only passage transcribed sign by sign); early modern English 1593, en-1640s chosen for spelling']
for c, p in zip(ct, pt):
    c = re.sub(r'\[blot\]', '', c)
    cs = [x for x in c if not x.isspace() and x not in ',.']
    ps = [x for x in p.lower() if x.isalpha()]
    assert len(cs) == len(ps), (c, p, len(cs), len(ps))
    out += [f'{a}\t{b}' for a, b in zip(cs, ps)]
(H / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
