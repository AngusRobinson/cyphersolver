"""Build validation.tsv: every cipher group of r2239_groups.txt decoded with the rebuilt list
(r2237_assign.txt + r2237_inferred.txt, as pairs.py / show.py do). Clear words skipped; groups that decode with
unknown letters ('.' or '~') are '?'."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE); sys.path.insert(0, HERE)
import wordtable as W
src = open('r2237_assign.txt', encoding='utf8').read() + open('r2237_inferred.txt', encoding='utf8').read()
open('_a', 'w', encoding='utf8').write(src); L, Ln, c = W.build('_a'); os.remove('_a')
out = ['# model: fr-modern', '# source: r2239_groups.txt decoded with r2237_assign.txt + r2237_inferred.txt (wordtable.py, as pairs.py)',
       '# note: R2239 only; groups decoding with unknown letters left unread (?); clear words skipped']
for ln in open('r2239_groups.txt', encoding='utf8'):
    if ln.startswith('#') or not ln.strip(): continue
    for g in ln.split():
        if W.parse(g) is None: continue
        d = W.decode_group(g, L, Ln)
        out.append(f'{g}\t{d if d and "." not in d and "~" not in d else "?"}')
open('validation.tsv', 'w', encoding='utf8').write('\n'.join(out) + '\n'); print(len(out) - 3)
