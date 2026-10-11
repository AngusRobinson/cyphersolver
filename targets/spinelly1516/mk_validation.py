"""Build validation.tsv: transcription.txt signs (grapheme clusters, words split on spaces) with the NOTES.md table,
the reading in plaintext.txt. dd (two delta) = w is written u + u; x in 'xv' is a clear numeral (left out);
b there = v (numeral)."""
import os, re, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
K = {'φ': 'a', 'τ': 'b', '4': 'c', 'ʒ': 'd', 'o': 'e', 'ρ': 'h', 'e': 'i', 'λ': 'k', 'v': 'l', 'σ': 'l', 'y': 'm',
     'b': 'n', '7': 'o', 'q': 'p', 'c': 'r', 'ʃ': 's', 'k': 't', 'δ': 'u', 'ϑ': 'of', 'ꝁ': 'this', 'w̄': 'that',
     '✱': 'theemperor', 'δ̄': 'll'}
WORD = {'ʒ': 'king'}           # ʒ standing alone at the end of line 2
def clusters(w):
    out = []
    for ch in w:
        if unicodedata.combining(ch) and out: out[-1] += ch
        else: out.append(ch)
    return out
ct = [l for l in open('transcription.txt', encoding='utf-8') if not l.startswith('#')]
words = [clusters(w) for l in ct for w in l.split() if w != '/']
out = ['# model: en-modern', '# source: transcription.txt with the sign table in NOTES.md (reading in plaintext.txt)',
       '# note: one five-line passage only; values per sign from the table (plaintext.txt normalises spelling: loys, entree, monethe); dd = w written u u; numeral x left out, b in xbdai = v']
for w in words:
    if len(w) == 1 and w[0] in WORD: out.append(f'{w[0]}	{WORD[w[0]]}'); continue
    if w[0] == 'x': out.append('x	?'); out.append(f'{w[1]}	v'); out += [f'{s}	{K[s]}' for s in w[2:]]; continue
    out += [f'{s}	{K.get(s, "?")}' for s in w]
open('validation.tsv', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(out) - 3)
