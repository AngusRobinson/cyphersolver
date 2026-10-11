"""Build validation.tsv for sp106r927: the letter f. 243 (hand_p3.txt) then f. 241 (hand_p1.txt), sign by sign, with
the value dec2.py gives (key.json, polyphones resolved by the LM). Signs the project's reading.txt marks as not read
(<...>) or as code/name signs ({...}) are '?', as are lost signs. f. 242 (a copy of f. 243) is left out."""
import os, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent; os.chdir(HERE); sys.path.insert(0, str(HERE))
import dec2
marked = {}
for l in open('reading.txt', encoding='utf-8'):
    if l.startswith('p') and '|' in l:
        lab, dec, _ = [x.strip() for x in l.split('|', 2)]
        marked[lab] = dec
out = ['# model: fr-1600-letters', '# source: hand_p3.txt + hand_p1.txt decoded by dec2.py (key.json); marks from reading.txt; mk_validation.py',
       '# note: letter order f. 243 -> f. 241; f. 242 (copy of f. 243) left out; <..> and {..} signs of reading.txt unread']
for page, path in (('p3', 'hand_p3.txt'), ('p1', 'hand_p1.txt')):
    for lab, toks in dec2.tokens(path):
        key = f'{page}.{lab}'
        if key not in marked:
            print('no reading line for', key); continue
        dec = dec2.decode_line(toks)
        flags, bad, code = [], False, False
        for ch in marked[key]:
            if ch == ' ': continue
            if ch == '<': bad = True; continue
            if ch == '>': bad = False; continue
            if ch == '{': code = True; continue
            if ch == '}': code = False; continue
            flags.append((ch, bad or code))
        assert ''.join(c for c, _ in flags) == ''.join(dec), (key, marked[key], ''.join(dec))
        for t, d, (c, unread) in zip(toks, dec, flags):
            out.append(f'{t.rstrip("?")}\t{"?" if unread or d == "_" else d}')
pathlib.Path('validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(out) - 3)
