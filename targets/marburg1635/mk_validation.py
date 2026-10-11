"""Build validation.tsv from reading_tokens.txt (sign=value per cipher sign, the reading of record)."""
import pathlib
H = pathlib.Path(__file__).parent
out = ['# model: de-1640s', '# source: reading_tokens.txt (sign=value pairs; mk_validation.py)']
for l in (H / 'reading_tokens.txt').read_text(encoding='utf-8').splitlines():
    if l.startswith('#') or ':' not in l: continue
    for p in l.split(':', 1)[1].split():
        if p == '/': continue
        s, _, v = p.rpartition('=')
        out.append(f"{s}\t{v or '?'}")
(H / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
