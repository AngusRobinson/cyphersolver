"""Build validation.tsv from reading_pr20.txt (decode_pr20.py: KEY_AND_DECRYPTION.txt token lines with the PR #20 key).
6 (word space) reads as nothing ('-'); figures under a blot ([hidden]) are '?'."""
import pathlib, re
H = pathlib.Path(__file__).resolve().parent
src = H / 'decode_pr20.py'
KEY = eval(re.search(r'KEY = (\{.*?\})', src.read_text(encoding='utf-8'), re.S).group(1))
out = ['# model: fr-1530-despatches',
       '# source: reading_pr20.txt token lines (KEY_AND_DECRYPTION.txt) with the PR #20 key in decode_pr20.py; mk_validation.py',
       "# note: 6 = word space read as '-'; blotted figures '?'; the May insertions appear in both witnesses f77 and f79 (no. 37/38), both kept as in the project's measure"]
for line in (H / 'reading_pr20.txt').read_text(encoding='utf-8').splitlines():
    lab, t, dec, gloss = line.split('\t')
    for x in t.split('|'):
        h = x.count('[hidden]'); x = x.replace('+[hidden]', '').replace('[hidden]', '')
        if x: out.append(f"{x}\t{'-' if KEY.get(x) == ' ' else KEY.get(x, '?')}")
        out += ['?\t?'] * h
(H / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(out) - 3)
