"""No. 24: apply the run-by-run revisions to reading_no24.txt -> reading_no24_rev.txt and measure (verify.py `understood`).
Each edit: (line of our transcription, old, new, tokens, evidence, status) ; status I = image-checked, C = constrained
by context + LM (counted), Z = z/4 key correction."""
import re, sys, pathlib
D = pathlib.Path(__file__).resolve().parent
src = (D / 'verify.py').read_text(encoding='utf8')
exec(src.split('SEED = ')[0].replace('from lang import lm', ''))

E = [
 # batch 1
 (7, 'n[o]ie ‹vict› sonno', 'n[o]ie vi sonno', '4 x F', '4 = u (key column); "per le molte noie vi sonno ogni dì"', 'Z'),
 (8, 'grann ‹digniacciatie› e', 'grandi ghiacciatie e', 'THETA x INT ETA c t 0 0 d+ E h d+ q 5 BOX x 6',
  'c = h (plain c on the image, not the e-like n); +o = i; E, h nulls: "e grandi ghiacciate" (great frosts; a February letter)', 'I'),
 (8, 'gl[i] ‹chamino› le', 'gl[i] chamino le', 'B d+ e b PHI t 0 c THETA h', 'letters as read; "e gli chamino le convien fare" (the roads he has to take)', 'C'),
 (8, '‹easprepensoo› pochi', '‹easpro› penso pochi', '3 d m+ SS W 8 h SS pp c^ m+ T', '"penso pochi dì" (I think, in a few days); the first five letters stay open', 'C'),
 (9, 'perché ‹aorlteaposi› cominca a diria ‹aaree› perché', 'perché e or \'l tenpo si cominca a dirizare; perché',
  '3 B t W A BOX YCROSS c^ SS 7 E m+ x ... x S u d W 6 SP', 'So-compound = z (image: S with the small o attached after x); "perché e\' or \'l tenpo si cominca a dirizare" (the weather begins to mend)', 'I'),
 (12, 'a{a} Lucca ‹evscet› di Fiorentini', 'a{a} Lucca e uscit[i] di Fiorentini', 'E pp E m+ d+ g BOX', 'g = i (key); "ambassadors ... and exiles of the Florentines" (the fuorusciti)', 'C'),
 (14, 'e ‹fanto›, q[u]anto', 'e fano, q[u]anto', '0 t 5 c^ B a 7 t', 't = f, B and a nulls: "e fanno, quanto l\'è posibile"', 'C'),
 (19, 'continuo ‹alvrechie›;', "continuo a l'vrechie;", 'd A 9 c W PHI d+ c t 0 pp E', '"io li so continuo a l\'orecchie" (I keep at his ear)', 'C'),
 (28, '‹dvctdisterli› (duca d\'Osterlich?)', "duc[a] d'Isterlic (duca d'Osterlich)", 'E THETA E d+ a THETA g m+ a YCROSS W A y d+ E h', 'Albert V of Austria; Osterlich/Isterlich', 'C'),
 (28, 'che è a ‹qacto› re', 'che è a facto re', 't d d+ BOX t AP', 't = f: "che è [stato] facto re d\'Ongnaria" (made King of Hungary, Dec 1437)', 'C'),
 (24, 'uno ‹svvfai›‹iglioatire› a Lucca', 'uno ‹svv›fa[m]iglio a dire a Lucca', 'm+ g a 0 t b y x ETA A l 0 T AP 0 THETA y W VENUS', '"à mandato uno [suo] famiglio a dire a Lucca" (sent a servant to say)', 'C'),
 (20, '‹lnpossa› conprendare ‹lvivera› Lucca', 'le possa conprendare lui verà Lucca', 'B A 6 SS T m+ E m+ 0 | A 9 q H pp W 5', '"per questa le possa comprendere: lui verrà [a] Lucca"', 'C'),
 (37, 'gar[z]{a}one', 'gar{a}zone', '0 W 0 S u 7 c 3', 'So-compound = z: "garzone"', 'Z'),
 # batch 2
 (2, "‹prerdom› ‹·› sare'", "‹prerao› Duca di Milano sare'", 'SS W 6 W 0 7 PHI+', 'image: the line-end Φ is point-framed (·Φ·), the word sign Duca di Milano, not m: "... il Duca di Milano sare\' disposto di soccorrere Lucca"', 'I'),
 (15, '‹loachamenaqano› assai', 'lo a Chamerino; assai', 'A t 5 d+ c d PHI 6 W t W c^ THETA E', 'image: our "t W" is "+o" (the i-sign); "fanno, quanto l\'è posibile, a e cond[urlo] lo a Chamerino", parallel to "di condurlo a Lucca"', 'I'),
 (6, 'sol‹nparqiirdicid› ‹roe›', 'sol‹n› per quind{g}ci d ‹roe›', 'e SS 6 W INT t 4 g c^ THETA ETA d+ x THETA', '4 = u, t = q: "per quindici d[ì]"; the sign after d (η or ʒ) not certain on the image', 'C'),
 (31, "per lo ‹qnala› soto", "per lo q‹n›ale soto", 't e u A g', '"per lo quale sono morti quatordici gente nel camino"', 'C'),
 (30, "no[n] ‹avinga› [a]dvegna", "no[n] avinga [a]dvegna", '5 9 x c ETA d E', '"se questa [gu]era non avinga" (avvenga)', 'C'),
 (37, "ritorni a q[u]a ‹asalr› per", "ritorni a casa ‹l› per", 'd+ 0 m+ 5 A h', 'd+ = c: "il garzone ritorni a casa per solecitare"', 'C'),
 (17, "licen[t]ia ‹·epaga·›", "licen[t]ia [de'] Viniziani ‹epaga·›", 'RX+', 'image: point-framed ℞ = Viniziani (word sign the reading had dropped)', 'I'),
 (19, "‹··› io li so", "[a'] Viniziani; io li so", 'RX+ x THETA', 'image: point-framed ℞ = Viniziani; x THETA = "io"', 'I'),
 (30, '‹eqnleodiaferraerapeo› pro‹·›ente', '‹eqnleodi› a Fer‹la›era pe[r] lo pro‹·›ente', 'Q SP t e A 6 A 7 THETA p 0 t VENUS W h F A d 6 W 5 SS YCROSS A 8', 'image: f e r, nulls h F, then l a e r a, p e l o: "a Fer[r]ara pe[r] lo presente" (the Council at Ferrara, Jan. 1438); the -la- stays open', 'I'),
 (26, "se n'à a {a}fa[r]lo", 'senza {a}fal{a}[l]o', 'c^ S u b 0 t d A b B THETA', 'So-compound = z: "e che senza fallo il marchese di Mantova è acordato col Duca di Milano"', 'Z'),
]

def apply(t, edits, log=True):
    for ln, old, new, toks, ev, st in edits:
        if t.count(old) != 1:
            print('NOT UNIQUE/NOT FOUND:', old, t.count(old)); continue
        t = t.replace(old, new)
    return t

if __name__ == '__main__':
    orig = (D / 'reading_no24.txt').read_text(encoding='utf8')
    t = apply(orig, E)
    hdr = ('# REVISED reading (14 Oct 2026, this project): George Lasry\'s reading with the runs resolved from our transcription,\n'
           '# the key sheet R4755 and the DECODE image of R4812; the table of changes is in NOTES.md ("No. 24 revised").\n')
    out = D / 'reading_no24_rev.txt'
    out.write_text(t.replace('# Concistoro 2308 no. 24', hdr + '# Concistoro 2308 no. 24', 1), encoding='utf8')
    for f in ('reading_no24.txt', 'reading_no24_rev.txt'):
        tot, ins = understood(D / f); print(f, tot, ins, f'{1 - ins / tot:.1%}')
    st = {}
    for e in E: st[e[5]] = st.get(e[5], 0) + 1
    print('edits', len(E), st)
