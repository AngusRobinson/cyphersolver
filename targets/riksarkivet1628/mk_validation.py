"""Build validation.tsv for the two Bremen letters (R4330, R4331), the only read part of this target.
bremen_decoded.txt is bremen_transcription.txt (3 header lines more) with cipher runs replaced by <decipherment>, using
the band key in its header. Each transcription line is aligned with its decoded line (difflib on the tokens): number
tokens replaced by a <..> group take their band-key letter; numbers left as written in the decoded file take the
nomenclator value NOTES gives (4 wir, 5 H. Christian, 7 H. Georg, 32 Bistum Minden, 59 Salvius) or stay unread."""
import os, re, difflib
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
BANDS = dict(zip(range(8, 104, 4), 'agntbhoucipwdkqxelryfmsz'))
def band(n): return BANDS.get(n - (n - 8) % 4) if 8 <= n <= 103 else None
NOM = {4: 'wir', 5: 'HChristian', 7: 'HGeorg', 32: 'BistumMinden', 59: 'Salvius'}
T = open('bremen_transcription.txt', encoding='utf-8').read().splitlines()
D = open('bremen_decoded.txt', encoding='utf-8').read().splitlines()[3:]
assert len(T) == len(D)
out = ['# model: de-1640s', '# source: bremen_transcription.txt aligned with bremen_decoded.txt (band key in its header); R4330-R4331 only',
       '# note: R4282, R4284, R4306 and the other records are unread and left out; numbers the decoded file leaves as written are nomenclator or unread']
num = lambda s: re.fullmatch(r'\d+', s.strip('.,:;()'))
for t, d in zip(T, D):
    if t.startswith(('#', 'GLOSS', '[')) or not t.strip(): continue
    tt = re.sub(r'\[[^\]]*\]', ' ', t).split()
    dd = re.sub(r'\[[^\]]*\]', ' ', re.sub(r'<[^>]*>', ' <G> ', d)).split()
    raw = set()
    for a, b, n in difflib.SequenceMatcher(None, tt, dd, autojunk=False).get_matching_blocks():
        raw.update(range(a, a + n))
    for i, tok in enumerate(tt):
        if not num(tok): continue
        n = int(tok.strip('.,:;()'))
        if n > 103: continue                      # years and amounts in the clear text
        if i in raw:
            v = NOM.get(n, '?') if n in NOM else '?'
            if n < 8 and n not in NOM: continue   # a clear small numeral
        else:
            v = band(n) or '?'
        out.append(f'{n}\t{v}')
open('validation.tsv', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(out) - 3)
