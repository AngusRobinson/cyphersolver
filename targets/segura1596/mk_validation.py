"""Build validation.tsv from token_reading.tsv (decode.py: cipher_tokens.txt + key.json); [null] = '-'."""
import csv, pathlib
H = pathlib.Path(__file__).resolve().parent
rows = list(csv.DictReader(open(H / 'token_reading.tsv', encoding='utf-8'), delimiter='\t'))
out = ['# model: es-golden-age', '# source: token_reading.tsv (decode.py: cipher_tokens.txt + key.json)',
       '# note: grade M values (6 singletons) kept as the recorded reading']
for r in rows:
    v = r['plaintext'].strip()
    out.append(f"{r['token']}\t{'-' if v == '[null]' else (v.lower() or '?')}")
(H / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8'); print(len(rows))
