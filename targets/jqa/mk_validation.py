"""Build validation.tsv for No. 88 (gap88.txt + rem88.txt) with code_table.tsv, as measure.py counts it: groups flagged
in sense88.tsv and groups with lost digits are unread; clear words and catchwords (cw:) left out."""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
tab = {}
for l in open('code_table.tsv', encoding='utf8'):
    p = l.rstrip('\n').split('\t')
    if l.startswith('#') or len(p) < 3 or not p[0].isdigit(): continue
    tab[int(p[0])] = p[1]
flags = set()
for l in open('sense88.tsv', encoding='utf8'):
    p = l.rstrip('\n').split('\t')
    if l.startswith('#') or len(p) < 3: continue
    g, _, k = p[2].partition('@'); flags.add((p[0], int(p[1]), int(g), int(k) if k else 0))
out = ['# model: en-modern', '# source: gap88.txt + rem88.txt (No. 88, 25 June 1812) with code_table.tsv, flags from sense88.tsv (measure.py)',
       '# note: numbered syllabary code of ~1600 numbers; most groups occur once, so the type-permutation test has little to work with']
for f in ('gap88.txt', 'rem88.txt'):
    for i, line in enumerate(open(f, encoding='utf8'), 1):
        seen = {}
        for t in line.split():
            if re.fullmatch(r'\d+x+', t): out.append(f'{t}\t?'); continue
            if not re.fullmatch(r'\d+', t): continue
            seen[t] = seen.get(t, 0) + 1
            v = tab.get(int(t))
            if v is None or (f, i, int(t), 0) in flags or (f, i, int(t), seen[t]) in flags: v = '?'
            out.append(f'{t}\t{v}')
open('validation.tsv', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(out) - 3)
