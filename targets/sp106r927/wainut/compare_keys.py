"""Compare the WAINUT transcription and key of R927 with the ones in this folder (key.json, hand_p3.txt, hand_p1.txt).

Standard library only. Run from anywhere:  python targets/sp106r927/wainut/compare_keys.py

Notations
- hand_p*.txt (this folder): archive orientation; shapes A-I named by their sides in that orientation
  (A=RB, B=LRB, C=LB, D=TRB, E=box, F=TLB, G=TR, H=TLR, I=TL), K = stem with a middle bar, '*' = inner stroke,
  digit = dot count.
- wainut/transcription_R927.txt: image turned 90 degrees counter-clockwise; shapes named by their look in that frame
  (D=open left, C=open right, U=open top, L=left+bottom, O=box, J=right+bottom, F=top+left, 7=top+right,
  N=open bottom; E = C with a middle bar, the same sign as C), digit = dot count; no inner-stroke distinction.
Turning the image 90 degrees CCW sends archive sides R->T, T->L, L->B, B->R, which gives the shape map SHAPE below.

Line correspondence: hand_p3.txt c0..c23 (no c7, c12) = WAINUT page 1 lines 00..21 (f. 243; the WAINUT page 1 was
read from image P2 with P3 for the part under the flap); hand_p1.txt c0..c19 = WAINUT page 2 lines 00..19 (f. 241).
"""
import os, json, difflib

HERE = os.path.dirname(os.path.abspath(__file__))
UP = os.path.dirname(HERE)
SHAPE = dict(A='7', B='D', C='J', D='N', E='O', F='U', G='F', H='C', I='L', K='K')


def load_wainut_key():
    key = {}
    for line in open(os.path.join(HERE, 'key_R927.tsv'), encoding='utf-8'):
        f = line.rstrip('\n').split('\t')
        if f[0].startswith('S'):
            key[f[1] + f[2]] = f[3]
    return key


def wainut_lines():
    pages, page = {}, None
    for line in open(os.path.join(HERE, 'transcription_R927.txt'), encoding='utf-8'):
        line = line.strip()
        if line.startswith('## PAGE'):
            page = int(line.split()[-1]); pages[page] = []
            continue
        if page is None or ':' not in line or line.startswith('#'):
            continue
        body = line.split(':', 1)[1].split('#ABOVE')[0]
        toks = []
        for t in body.split():
            if t in ('|', '=', '#,', '#-', '#STRIKE'):
                continue
            if t.startswith('#'):
                toks.append(('#', t)); continue          # code sign or illegible
            raw = t.split('(')[0].replace('?', '')
            if raw[:1] == 'E':
                raw = 'C' + raw[1:]                       # E = C with a middle bar
            toks.append((raw[:1], raw))
        pages[page].append(toks)
    return pages


def bourdeau_lines(fname):
    out = []
    for line in open(os.path.join(UP, fname), encoding='utf-8'):
        line = line.split('#', 1)[0].strip()
        if ':' not in line:
            continue
        toks = []
        for t in line.split(':', 1)[1].split():
            if t in ('=', '/', '[struck]'):
                continue
            if t[0] in '[<@?':
                toks.append(('#', t)); continue
            raw = t.replace('?', '')
            toks.append((SHAPE[raw[0]], raw))
        out.append(toks)
    return out


def main():
    wk = load_wainut_key()
    bk = json.load(open(os.path.join(UP, 'key.json'), encoding='utf-8'))
    inv = {v: k for k, v in SHAPE.items()}

    print('1. Key, sign by sign (WAINUT sign -> same sign in key.json notation, plain form without inner stroke)')
    same = poly = diff = 0
    for s, letter in sorted(wk.items(), key=lambda x: x[1]):
        b = inv[s[0]] + s[1:]
        bv = bk.get(b, '-')
        wl = letter.split('/')
        if bv == letter or bv in wl:
            tag = 'same'; same += 1
        elif set(bv.split('/')) & set(wl):
            tag = 'his value is a polyphone that includes ours'; poly += 1
        else:
            tag = 'DIFFERENT'; diff += 1
        print(f'   {s:3} = {letter:4}  key.json {b:3} = {bv:4}  {tag}')
    print(f'   {len(wk)} WAINUT signs: {same} same value, {poly} polyphone in key.json containing our value, {diff} different')
    extra = sorted(k for k in bk if k[0] in SHAPE and '*' not in k and (SHAPE[k[0]] + k[1:]) not in wk)
    print('   key.json signs with no WAINUT counterpart:', ', '.join(f'{k}={bk[k]}' for k in extra))
    print('   key.json inner-stroke signs (WAINUT does not separate them):',
          ', '.join(f'{k}={bk[k]}' for k in sorted(bk) if '*' in k))

    print('\n2. Transcriptions, line by line (signs aligned on shape with difflib; code signs and lost signs left out)')
    wl = wainut_lines()
    pairs = [('f. 243', wl[1], bourdeau_lines('hand_p3.txt')), ('f. 241', wl[2], bourdeau_lines('hand_p1.txt'))]
    T = dict(w=0, b=0, m=0, full=0, letters=0)
    for name, W, B in pairs:
        assert len(W) == len(B), (name, len(W), len(B))
        nw = nb = m = full = lt = 0
        for wt, bt in zip(W, B):
            wt = [t for t in wt if t[0] != '#']; bt = [t for t in bt if t[0] != '#']
            nw += len(wt); nb += len(bt)
            sm = difflib.SequenceMatcher(None, [t[0] for t in wt], [t[0] for t in bt], autojunk=False)
            for a, b, n in sm.get_matching_blocks():
                for i in range(n):
                    x, y = wt[a + i][1], bt[b + i][1]
                    m += 1
                    if x[1:] == y.replace('*', '')[1:]:
                        full += 1
                    lw = wk.get(x, '?'); lb = bk.get(y, '?')
                    if lw != '?' and set(lw.split('/')) & set(lb.split('/')):
                        lt += 1
        print(f'   {name}: WAINUT {nw} signs, key.json files {nb} signs; {m} aligned on shape; '
              f'of these {full} ({100*full/m:.1f}%) also have the same dot count; '
              f'{lt} ({100*lt/m:.1f}%) decode to the same letter (each with its own key; a polyphone '
              f'counts when one of its values is ours)')
        T['w'] += nw; T['b'] += nb; T['m'] += m; T['full'] += full; T['letters'] += lt
    print(f'   both pages: {T["m"]} aligned; same dots {T["full"]} ({100*T["full"]/T["m"]:.1f}%); '
          f'same letter {T["letters"]} ({100*T["letters"]/T["m"]:.1f}%)')

    print('\n3. The signature (f. 241, last word of the subscription line)')
    wsig = [t[1] for t in wl[2][18]][-5:]
    bsig = [t[1] for t in bourdeau_lines('hand_p1.txt')[18]][-5:]
    raw = open(os.path.join(UP, 'hand_p1.txt'), encoding='utf-8').read().split('c18:')[1].split('\n')[0].split()[-5:]
    print('   WAINUT  :', ' '.join(wsig), '->', ''.join(wk.get(x, '?') for x in wsig),
          '(first sign marked uncertain in the transcription: 7?2)')
    print('   key.json:', ' '.join(raw), '=', ' '.join(SHAPE[x[0]] + x[1:] for x in bsig), '->',
          ''.join(bk.get(x, '?') for x in bsig))
    for i, (x, y) in enumerate(zip(wsig, bsig), 1):
        print(f'   sign {i}: shape {"same" if x[0] == SHAPE[y[0]] else "different"}, dots {x[1:]} vs {y[1:]}')

    print('\n4. Code signs, line by line (WAINUT #67/#6/#@ against hand_p*.txt @ and <67>)')
    for name, W, fname, labs in (('f. 243', wl[1], 'hand_p3.txt', [f'c{i}' for i in range(24) if i not in (7, 12)]),
                                 ('f. 241', wl[2], 'hand_p1.txt', [f'c{i}' for i in range(20)])):
        B = bourdeau_lines(fname)
        for i, (wt, bt) in enumerate(zip(W, B)):
            wc = [t[1] for t in wt if t[1] in ('#67', '#6', '#@')]
            bc = [t[1] for t in bt if t[1] in ('@', '<67>')]
            if wc or bc:
                print(f'   {name} WAINUT line {i:02d} / {labs[i]}: {" ".join(wc):12} | {" ".join(bc)}')


if __name__ == '__main__':
    main()
