"""Build validation.tsv from token_ledger.json (decode.py output: one row per sign, literal value)."""
import json, pathlib
H = pathlib.Path(__file__).resolve().parent
L = json.loads((H / 'token_ledger.json').read_text(encoding='utf-8'))
out = ['# model: de-1640s', '# source: token_ledger.json (decode.py: transcription.txt + key.json)',
       '# note: literal values; GEFAE final E kept as recorded (no emendation); U/V one sign read u']
out += [f"{r['sign']}\t{r['literal'].lower()}" for r in L]
(H / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8'); print(len(L))
