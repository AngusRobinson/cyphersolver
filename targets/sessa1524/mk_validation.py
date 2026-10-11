"""Build validation.tsv from the (a) cipher / (b) reading line pairs of r9873_cipher.txt and r9898_cipher.txt
(pass 17, the files measure_read.py measures). These are Sessa letters in the same cipher as ff. 128-131 (the
f. 128 passage itself is only nine lines, read in prose in NOTES, with no token-aligned reading).

Per line pair: (a) tokens with clear text ("..." quotes, ..., f~) removed; 'v db' (null paragraph opener) = nulls.
(b) is split into pieces: hyphen/space separated, a bracket [x y=val] is one piece standing for the cipher tokens
x y (joined here as one token x_y, as the project treats it as one group), plain words are one known group.
{..} runs (letters without sense) keep their letters when they split into the same number of pieces as tokens.
A line pair is used only when the piece count equals the token count; other lines are written as '?' (unaligned).
Open groups [x] are '?', tentative values [x=val?] are taken as recorded (counted as read by measure_read.py)."""
import re, os
H = os.path.dirname(os.path.abspath(__file__))
out = ['# model: es-golden-age',
       '# source: r9873_cipher.txt + r9898_cipher.txt (a)/(b) line pairs, pass 17; mk_validation.py',
       "# note: sibling letters R9873 (14 Apr 1524) and R9898 (24 Feb 1525) in the f. 128 cipher; line pairs whose (b) pieces do not match the (a) token count are written '?'; multi-token groups joined with _"]

def a_tokens(s):
    s = re.sub(r'"[^"]*"', ' ', s).replace('...', ' ')
    return [t for t in s.split() if t != 'f~']

def b_pieces(s):
    s = re.sub(r'"[^"]*"', ' ', s)
    s = re.sub(r'\([^()]*\)', ' ', s)
    s = s.replace('...', ' ').replace('¶', ' ').replace('/', ' ')
    s = re.sub(r'->.*', '', s)
    out = []
    for m in re.finditer(r'\[[^\]]*\]|\{[^}]*\}|[^\s\-\[\]{}]+', s):
        w = m.group(0)
        if w.startswith('{'):
            for p in re.split(r'[\s-]+', w.strip('{}')):
                if p: out.append(('?', p))     # letters without sense: the key's letters are not recoverable token-wise
        elif w.startswith('['):
            body = w[1:-1]
            if '=' in body:
                toks, val = body.split('=', 1); out.append((toks.strip(), val.strip().rstrip('?')))
            else:
                out.append((body.strip(), '?'))
        else:
            out.append((None, w.strip('?')))
    return out

used = skipped = 0
for path in ('r9873_cipher.txt', 'r9898_cipher.txt'):
    L = open(os.path.join(H, path), encoding='utf-8').read().splitlines()
    for i, ln in enumerate(L):
        m = re.match(r'\s*(\d+)a\s(.*)', ln)
        if not m or i + 1 >= len(L): continue
        mb = re.match(r'\s*(\d+)b\s(.*)', L[i + 1])
        if not mb or mb.group(1) != m.group(1): continue
        toks = a_tokens(m.group(2)); pcs = b_pieces(mb.group(2))
        # null opener v db
        nulls = []
        if toks[:2] == ['v', 'db'] and (not pcs or pcs[0][0] != 'v db'):
            nulls = ['v', 'db']; toks = toks[2:]
        # expand: a bracket piece naming its tokens consumes that many tokens
        pairs, k, ok = [], 0, True
        for names, val in pcs:
            n = len(names.split()) if names and names != '?' else 1
            if names and names != '?' and toks[k:k + n] != names.split():
                n = 1 if names.count(' ') == 0 else n
            if k + n > len(toks): ok = False; break
            pairs.append(('_'.join(toks[k:k + n]), val)); k += n
        ok = ok and k == len(toks)
        out += [f'{t}\t-' for t in nulls]
        if ok:
            out += [f'{t}\t{v}' for t, v in pairs]; used += len(pairs)
        else:
            out += [f'{t}\t?' for t in toks]; skipped += len(toks)
open(os.path.join(H, 'validation.tsv'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('aligned', used, 'unaligned', skipped)
