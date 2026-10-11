"""Build validation.tsv for docs/_validate.py from reading-tokens.tsv (prepare_reading.py: key-potocka.json applied
token by token). Potocka's nine letters only; R7524 (Mniszech, another and unread system) is left out."""
import os, csv
HERE = os.path.dirname(os.path.abspath(__file__))
rows = [r for r in csv.DictReader(open(os.path.join(HERE, 'reading-tokens.tsv'), encoding='utf8'), delimiter='\t')
        if r['record'] != '7524']
with open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf8') as f:
    f.write('# model: fr-modern\n# source: reading-tokens.tsv (prepare_reading.py, key-potocka.json), records R7525-R7536; R7524 left out (mk_validation.py)\n')
    f.write('# note: French letters 1714-16; the R7526 postscript (about 160 tokens) is Polish and is scored with the French model; person codes 87/94/100/270 and 73 unread\n')
    for r in rows: f.write(f"{r['cipher']}\t{r['plain'] if r['plain'] not in ('', '?') else '?'}\n")
print(len(rows))
