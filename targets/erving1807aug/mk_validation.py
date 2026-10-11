"""Build validation.tsv from aligned.txt (1,145 groups, the reading NOTES.md measures).
Token = the group as aligned (caret ^ kept: a plural-marked group is its own cipher form; '#' = partly hidden, dropped
when the number is complete). Reading: the aligned value; '?' for X (no value), for conjectures (value with '?') and
for groups whose digits are lost in the binding (X inside the number). '(sic...)' notes are dropped (Erving's slip
read as intended, as in the project's reading)."""
import pathlib, re
H = pathlib.Path(__file__).resolve().parent
out = ['# model: en-modern',
       '# source: aligned.txt (group=value per run, NOTES Method step 2); mk_validation.py',
       "# note: X, conjectures ('?') and groups with digits lost in the binding are '?'; caret ^ kept as part of the token"]
for line in (H / 'aligned.txt').read_text(encoding='utf-8').splitlines():
    if line.startswith('#') or '|' not in line: continue
    for item in line.split('|', 1)[1].split():
        tok, _, val = item.partition('=')
        tok = tok.replace('#', '')
        val = re.sub(r'\(sic[^)]*\)', '', val)
        if 'X' in tok or val == 'X' or '?' in val or not val: val = '?'
        out.append(f'{tok}\t{val}')
(H / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(out) - 3, 'tokens')
