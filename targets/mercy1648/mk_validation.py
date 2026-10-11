"""Build validation.tsv from reading.tsv (one row per cipher token, written by build_reading.py)."""
import csv, pathlib
H = pathlib.Path(__file__).resolve().parent
rows = list(csv.DictReader(open(H / 'reading.tsv', encoding='utf8'), delimiter='\t'))
out = ['# model: es-golden-age', '# source: reading.tsv (build_reading.py: ct_f22.tsv + key.tsv + edits.tsv), one row per cipher token',
       '# note: BOX = name sign (Santibal); edge-lost letters are not tokens']
for r in rows:
    v = r['value'].strip()
    if v.startswith('<'): v = v.strip('<>').lower()
    out.append(f"{r['token']}\t{v if v else '?'}")
(H / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf8'); print(len(out) - 3)
