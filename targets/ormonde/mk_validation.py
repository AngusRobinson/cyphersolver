"""Build validation.tsv from the reading in NOTES.md sections 4 and 4a (figures as printed, ciphertext.txt).
Nulls 91-111 '-'; 26 read r (the reading has ANGRY although the grid gives k); 89, 31, 185, 149 unread."""
import pathlib
H = pathlib.Path(__file__).parent
V = {'65': 'a', '35': 'n', '21': 'g', '26': 'r', '59': 'y', '113': 'with', '186': 'the Lord Deputy', '143': 'the King',
     '28': 'l', '69': 'e', '49': 't', '50': 't', '70': 'e', '44': 'r', '89': '?', '185': '?', '149': '?',
     '10': 'c', '79': 'o', '47': 's', '8': 'b', '270': 'Crosby', '218': 'Secretary Coke', '174': 'Ormonde',
     '221': 'Parliament', '31': '?', '64': 'a', '11': 'c', '85': 'u', '12': 'c', '29': 'l'}
RUNS = ['65 35 21 26 59 98 113 186 108 143', '28 69 49 50 70 44 89', '186 99',
        '93 185 95', '99 149', '98 10 44 79 47 8 59', '270', '95 186 98', '98 218 97', '100 174 103', '111 95 221',
        '93 31 174 99', '64 99 11 79 85 35 12 69 28 29 79 44', '174']
out = ['# model: en-1640s', '# source: ciphertext.txt figure runs with the reading of NOTES.md sections 4/4a (mk_validation.py)',
       '# note: 59 figures only; nulls 91-111 as -']
for r in RUNS:
    for t in r.split():
        out.append(f"{t}\t{'-' if 91 <= int(t) <= 111 else V[t]}")
(H / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
