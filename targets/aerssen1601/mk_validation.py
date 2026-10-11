"""Build validation.tsv from evidence/attestation_25may.tsv (25 May) and transcription/2jun1601.md (2 June).
Grade-I values (inferred from context, not attested: 45' Essex, 20^ ba, 88' Bruxelles) and unread codes are '?'."""
import pathlib, csv
H = pathlib.Path(__file__).parent
out = ['# model: fr-1600-letters',
       '# source: evidence/attestation_25may.tsv (25 May, 61 tokens) + transcription/2jun1601.md TOK/SEG (2 June, 11 tokens); mk_validation.py',
       "# note: grade-I contextual values (45' Essex, 20^ ba, 88' Bruxelles) and 47' left unread"]
for r in csv.DictReader(open(H/'evidence/attestation_25may.tsv', encoding='utf-8'), delimiter='\t'):
    v = r['value'] if r['grade'] in ('C', 'M', 'H') and r['value'] != '?' else '?'
    out.append(f"{r['token']}\t{v}")
jun = [('8','la'),('20^','?'),('17','u'),('28^','de'),('k^','ri'),('24','e'),('95\'','ambassadeur'),
       ('36^','du'),('10+','Roy'),('23','a'),("88'",'?')]
tok = "8 20^ 17 28^ k^ 24 95' 36^ 10+ 23 88'".split()
assert [t for t,_ in jun] == tok
out += [f'{t}\t{v}' for t, v in jun]
(H/'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
