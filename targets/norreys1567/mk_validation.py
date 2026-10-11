"""Build validation.tsv: the sibling groups NOTES.md counts as read with Tomokiyo's Cecil-Norris table, token by token
with the table as applied in work/tomokiyo_apply.py (M), plus the name signs the NOTES read (French King, Protestants,
Prince, Admiral). Groups NOTES leaves garbled or unread are left out; signs not in the table are unread."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'work'))
from tomokiyo_apply import M, groups
READ = {('N670706', '1'), ('N680206', '1'), ('N680206', '2'), ('N680206', '3'), ('N680206', '4'), ('N680206', '7'),
        ('N680206', '16'), ('N680209', '1'), ('N680209', '3'), ('N680209', '4'), ('N680209', '7'), ('N680224', '8')}
NAMES = {('N680206', '5'): 'theFrenchKing', ('N680206', '13'): 'theFrenchKing', ('N680209', '5'): 'theFrenchKing',
         ('N680309', '1'): 'theFrenchKing', ('N680209', '6'): 'theProtestants', ('N680209', '8'): 'thePrince',
         ('N680209', '9'): 'theAdmiral', ('N680224', '2'): 'theProtestants', ('N680224', '3'): 'thePrince',
         ('N680224', '4'): 'theAdmiral'}
out = ['# model: en-modern',
       '# source: transcription.txt with Tomokiyo\'s table as in work/tomokiyo_apply.py; read groups and name signs as listed in NOTES.md',
       '# note: only the groups NOTES reads (Steuarde, Lesly, earl, Rothes, papystes, reaums, stayid, demaund, reason, peac, ruin, remayn) and the read name signs; garbled groups left out']
for d, k, toks in groups():
    if (d, k) in NAMES:
        out += [f'{t}\t{NAMES[(d, k)]}' for t in toks]
    elif (d, k) in READ:
        out += [f'{t}\t{"?" if t.startswith("#") else M.get(t, "?")}' for t in toks]
open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(out) - 3)
