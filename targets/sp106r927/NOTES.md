# TNA SP 106/10 ff. 241-243 — undeciphered letter in the "masonic alphabet" (DECODE R927)

Lasry review (25 Sept 2026): the letter was decoded by Sheila Richards in *Secret Writings* (1973). The book was not seen here and a web search found no record of it; it was not used. This reading is an independent re-solution (outcome.first_break = false), left out of the ciphertext-only list for Klaus Schmeh.

Outcome: read (key recovered from ciphertext-only; 2026-09-19; all pages transcribed 2026-10-02; pass 2 2026-10-03; reclassed
read at the write-up update of 2026-10-03: the letter, f. 243 + f. 241, is 95.6% and every open piece is blocked from outside:
blots and a stain on f. 241 with no second copy and no better image, name signs with no key).
French, homophonic pigpen. The letter runs f. 243 -> f. 241. Correction 12 Oct 2026: f. 242 is not a second copy: images P2 and P3 show the same leaf, f. 243, with the pasted flap folded down (P2) and lifted (P3) (WAINUT, PR #30, confirmed on the images 12 Oct 2026). The letter has
two pages, and the agreement of `hand_p2.txt` with `hand_p3.txt` checked only the transcription, not the text.
Measured (pass 2, `measure.py`): **95.6%** of the letter's signs read as sense (843/882; 97.1% leaving out 14 code and name
signs); f. 243 98.3%, f. 241 92.5%. Before pass 2: 84.0%. Written at Nancy, in December, signed "Nicle"(?).

## Source

- DECODE record 927, `TNA_SP106/10_UND_(0241-0243)`, 3 images (auth-only; fetched with the bordeaux cookie):
  `IMG_R927_I4921_P1.png`, `I4922_P2.png`, `I4923_P3.png` (kept in `img/`, git-ignored).
- DECODE: "Undeciphered letter in the masonic alphabet, say 800 codegroups in sum total." No sender, recipient, date.
- Web search (Sept 2026): no published decipherment found.

## What the pages show

- Pigpen-type glyphs (the nine tic-tac-toe cell shapes), each followed by 1-3 dots (occasionally 0 or 4).
  Some glyphs carry an inner stroke or inner dot; a few are stacked composites (e.g. ⊔ over ⌟); two special
  "9/6"-like signs; "=" marks at line ends (word carried over).
- Writer's frame: turn the images 90° counter-clockwise (the "67" on p.1 is then upright). Text then runs in
  horizontal rows, dots above the glyphs. In the archive's image orientation the rows appear as vertical columns.
- P.2 carries a paper flap with a **pencil key** (later hand, probably a reader's attempt):
  `akt | blu | cmw / dnx | eoy | fpz / gq | hr | is` — i.e. the 1-2-3-dot pigpen (a-i one dot, k-s two, t-z three).

## Tests so far (p.3, ~470 glyphs, automatic segmentation + hand checks of cols 0-11)

- The flap key applied literally gives nonsense ("oeaeydakdorsefekdoi..."). Under it g/q would be ~16% of text, t ~0,
  k ~9%: the key is not right as written.
- All 8 rotations/reflections of the grid × all dot-order permutations × both reading directions × dot-shift ±1,2:
  best quadgram score -6.3/char (real text ≈ -4.0). Languages: en, fr, de, nl, es, it, la.
- Cell-constrained solve (letter free within the key cell), any orientation: no language fits.
- All 9! shape→cell assignments (dots = position): no fit.
- Free homophonic hill-climb over (shape, dot-count) symbols, IoC of that stream 1.64 (×26, i.e. language-like):
  en/fr/de/nl/it/es/la/sv/da/pt/cy/pl/hu all -4.5..-5.0 with no readable text; column, row, reversed and
  boustrophedon orders tried. Synthetic English with 10% symbol noise still reaches -4.6 and reads in part,
  so either transcription error is much higher than 10% or the symbol set is wrong (inner-mark variants,
  composites and the special signs not yet separated).

## Next

Full hand transcription with inner-mark variants and composites as separate symbols (p.3 cols 0-11 partly done
in this session's notes below), then pp.1-2; rerun the free solver.

### Hand transcription p.3 (archive orientation, columns right→left, top→bottom; `*` = inner mark; `@` = 9/6 sign)

    c0: E2 E1 A1 E1 E3 D1 A1 A2 D*1 E2 H*2 I2 E*1 F1 E1 A2 D1 E*2 I1
    c1: A2 A1 E1 A1 A1 A2 G2 E*3 F3 A2 I*2 H2 E1 A1 H2 E2 H1 F2 E*1
    c2: B1 G2 B1 A1 D2 [blot] B1 E*3 E*2 I1 E2 H*2 C2 A2 E*1 I1 A2 A1 D*2 E2
    c3: B1 B*2 E1 I1 E*1 F1 E1 B2 E1 A1 D2 E2 F*3 F2 D1 G1 G1 E1
    c4: F3 E1 C2 A2 E1 F*2 H2 B1 F*3 A2 B*1 I1 E1 I2 A*1 E2 E1 I1 E1 G1 E1 A1 D2
    c5: @ A? I1 E1 F2 B1 E3 B1 I2 D2 I1 E0 @ G1 D1 A1 G1 B1 E2 D1 ?
    c6: [blot] A2 H2 B1 A2 E*2 E1 H2 F*1 I2 E1 A2 C2 A2 E*1 F3 C1 A2

### Session 1 close (2026-09-19)

- Auto labels (`v3_glyphs2.json`, from `segv.py` + `segv2.py`) checked against hand reading for cols 0-6:
  133 glyphs, 16 shape errors, 20 dot errors (~25% symbol error). Cols 7-23 eyeballed in montages: same error profile,
  plus inner-stroke variants (◻ with inner bar, ⊓ with inner stroke) that the classifier merges with plain shapes.
- The free solver fails at this noise level. Next step: finish the hand transcription (cols 7-23, then pp.1-2),
  keep inner-mark variants as separate symbols, then rerun `hc3.py` (en, la, fr first).
- Tools here: `seg2.py`/`segv.py` (glyphs), `segv2.py` (dots → nearest glyph), `hc2.py`/`hc3.py` (homophonic
  annealing with quadgrams `q_<lang>.json`, built by `mkq.py`), `cons.py`/`cellperm.py` (key-constrained tests).

## Broken (session 1, later)

Full hand transcription of p.3 in `hand_p3.txt` (450 signs). With it the free solver lands on **French**
(quadgram -4.39 vs -4.8/-5 elsewhere); anchors then fixed by hand ("monsieur", "de vostre", "vous supplie",
"croire que je vous honnor"). The system is a **homophonic pigpen**: sign = cell shape (+ optional inner stroke)
+ 1-3 dots; common letters have several signs. The pencil key on the flap is NOT the key.

Working key (`key_fr3.json`; `*` = inner stroke; some values still provisional):
a=B1  b=H1  c=F1  d=I1  e=E1,E*1,K3?  i=E2,E*2,B*1  l=F2,F3,F*3  m=G1  n=A1,D*1?,K1  o=D1  p=E3,E*3
q=C1,C2  r=I2,I3,D*2  s=H2,H*2,I*2,F*2  t=D2,B2,F*1  u/v=A2,A*1  y=G2  h=K2  nn/ss?=X2  g=B*2

Reading of p.3 (end of the letter; brackets = my regularisation, ? = unsure):
  je ne pouvois recevoir d'un ennuy plus sensible [qu'] ayant appris que du [ma]riage de cet[te] ... l'homme
  lequel ... de vie ... [&] de la part de [&] mon ... vous avez esté ... quelque ... closes, prejudice
  de l'entiere affection ... a vostre service ... je puisse prendre confiance ... nous eussions ...
  jusque je ne te dis rien tant que les occasions de ... des effets ... ce que cet entier homme ...
  et vous supplie tres humblem[ent], monsieur, [de] me continuer l'honneur de vostre bienveuillance
  et croire que je vous honnor[e] ...
Language and formulae point to a French letter of the 17th century. Sender and recipient are not yet identified.

Next: hand-transcribe pp.1-2 (the start of the letter, which should name people), finish the key, then /writeup.

## Reading of f. 243 (the first page of the letter, see Session 3; `hand_p3.txt` → `p3_plain.txt`, key `key.json`)

Raw decipherment, one line per written line:

    ieneponunisreceuoid / unennuyplussensible / ayantapidisquedunri / agedecegentillomme /
    lequessaluiderviedement / &ndelapartde&monmaio / usauiestreuquelfu / closespreiudice /
    dehentiereaffectionse / iayuoueauostreseruice / utesteiersnenei / ipeusseprendreconfia /
    nuouseussiescouguupr / luyqueienecledisrien / tantfuetesoccasionsdeutub / entesmoingnerdeseffets /
    iescrisa&cequecegentil / lommealloetfaircpardela / etuoussupplietreshunblem / monsieurmecontinuerlloseur /
    deuostrebienueuheanceet / croirefueieuoushonnor

Regularised: "... je ne pouvois recevoir d'un ennuy plus sensible, ayant appris que du mariage de ce gentilhomme,
lequel ... de la part de mon ma[istre] ... vous a esté ... prejudice de l'entiere affection [que] j'ay vouée
a vostre service ... je puisse prendre confiance ... Je ne te dis rien tant que les occasions ... en tesmoigner
des effets. J'escris a[u] ... ce que ce gentilhomme alloit faire par dela, et vous supplie tres humblement,
monsieur, me continuer l'honneur de vostre bienveuillance et croire que je vous honnor[e] ..."

Key notes: C1 serves both f (affection, effets) and q (que): either a true polyphone or an inner-mark variant
not separated in transcription. K1=c, K2=h, B2/B*2=g, G2=y. The two circle/"9" signs (@) and the stacked
composites are unresolved; they sit where names or abbreviations are expected (e.g. before "de la part de").

## f. 241 (session 1 fragments; superseded by Session 3, it is the closing page)

Auto-segmented (`v1_glyphs2.json`); the classifier often reads ⊔ as ◻ on this page. Hand-checked columns give
"... disposer ... envoier le ...", "... la santé ... la longue maladie qu'il a eue, je m'asseure ...",
"... que les personnes ...", "vous aimés, n'en seroint ...", "... mon costé ...", "... mon coeur ...",
"... faveur ...". Full hand transcription of f. 241 is still open.

Sender, recipient and date are not named in the parts read. The formulae ("monsieur", "tres humblement",
"vostre bienveuillance") and spelling point to a French letter of the 17th century, from a client or
servant to a patron.

## Session 3 (2 Oct 2026): ff. 241 and 242 transcribed

Files: `hand_p1.txt` (f. 241, 20 columns), `hand_p2.txt` (f. 242, 22 columns), `dec2.py` (decoder: key.json, polyphones
resolved per occurrence by `lang` fr-1600-letters), `reading.txt` (marked decrypt + regularised French, all pages),
`measure.py` (checks the marks against dec2.py and counts the share read). Method: columns located with the old
auto-segmentation (`v1_glyphs2.json`, offset +1150/+100 on the DECODE image), then every sign read by eye from deskewed
5x strips; the auto labels were not used.

**Page order.** f. 243 ends "et croire que je vous honnor-"; f. 241 begins "-e et cheris ce qui se peut, s'y vous
trouviés a propos de disposer ..." and ends with the subscription and dateline. So the letter is f. 243 + f. 241.
~~f. 242 is a second copy of f. 243~~ (withdrawn 12 Oct 2026: P2 and P3 are the same leaf, flap down and flap lifted;
see the WAINUT section below). Line for line the same line breaks and signs (cj, cp, cs read independently agree sign
for sign; the same '@' at the same place), because they are the same page photographed twice; the agreement checked the
transcription only. The upper part of its six rightmost columns is under the pasted flap
that carries the pencil key, and three signs of ch are under an ink blot.

**f. 241 (regularised):** "[...honnor]e et cheris ce qui se peut. S'y vous trouviés a propos de disposer [..] d'envoier
le .. [..] de Sa Majesté vers [..] pour se resjouir de sa santé apres la longue maladie qu'il a eue, je m'asseure que les
personnes que vous aimés n'en seroint marris, et [..] mon costé je [..] j'iray, mon coeur, de tout ce que je jugeray
estre du [..] [67] et du [..], vous conjurant me faire [..] faveur d'asseurer Sa Majesté du zele que j'ay a son tres
humble service, estant, mo[nsieur], [..] vostre tres humble et fidel serviteur Nicle(?). De Nancy le [n] decembre."

Key changes (key.json; the pre-session key is in git): H3 = z (zele); C*2 = q (ce qui); C1 = f/q polyphone (faveur,
confiance, affection, effets vs que, qu'il, quelque); F2 = l/h polyphone (plus sensible vs cheris, gentilhomme, choses,
homme, l'honeur); C3 = l and A*2 = q (one occurrence each on f. 242, provisional). The polyphones are resolved by the LM
in dec2.py. lm.best_language puts fr-1600-letters first on both pages (-2.1/char).

Content: a client or servant writing from Nancy (Lorraine) in December to a "Monsieur" whose favour he asks; the marriage
of "ce gentilhomme", an envoy to congratulate "Sa Majesté" on recovering from a long illness, and assurances of his zeal
for the King's service. Sender (signature read "Nicle", perhaps a contraction), recipient and year stay open.

### Neighbouring records (2 Oct 2026)

Opened on DECODE (catalogue_harvest views + RecordsView pages with the bordeaux cookie): R922 is NAH (not SP 106);
R923 (ff. 233-234), R924 (ff. 235-236), R925 (ff. 238-240), R928 (ff. 245-246), R929 (f. 247) are the digit-code
Henrietta Maria / Goffe 1645-46 group (images of R925 checked: numbers); R930 (f. 249) is a strip of alchemical-type
symbols and letters, not this pigpen; R931/R932 (ff. 251-252) numeric; R933 a key sheet with English names. R926 and
ff. 237, 244 have no record (the image id I4920 between R925 and R927 is not served). No other letter in this pigpen and
no decipherment or clear copy of R927 in the neighbouring records.

## Pass 2 (3 Oct 2026): every unread word re-read sign by sign

- Image routes: TNA Discovery has no digitised SP 106/10; DECODE serves only the 2300-px PNGs already in `img/`.
- Every glyph of the unread words cut out at 3-4x (the `v3_glyphs2.json` / `v1_glyphs2.json` boxes, offsets +80/+880
  on f. 243 and +100/+1150 on f. 241, used only as locators) and read again. Corrected: f. 243 c0, c2, c4-c6, c8, c9,
  c11, c13-c16, c21, c22; f. 241 c2, c3, c5, c9, c10, c12 (the errors were the open side of corner shapes, dot counts,
  inner strokes, and two signs the writer cancelled with an ink blot, now `[struck]` and skipped). The v3 "c7" and
  "c12" of f. 243 are a stain and the head of c11. f. 242 cq-cv re-synced to the corrected f. 243 lines.
- Key: F*1 = l (not t; "que les occasions" twice), D*1 = o (pouvois). Joint re-annealing of all sign values over the
  three pages with fr-1600-letters (`anneal.py`) raised the LM score (-2.106 -> -2.002/char) but turned B2 g->s and
  K2 h->d against gentilhomme, longue, tesmoigner, humble, honnor: over-fitting, not adopted except F*1.
- f. 243 now reads: "Je ne pouvois recevoir d'un ennuy plus sensible, ayant appris que du mariage de ce gentilhomme,
  lequel salua dernierement [name] de la part de [name] mon maistre, vous aviés creu quelques choses au prejudice de
  l'entiere affection que j'ay vouée a vostre service: s'il fut esté personne en qui je peusse prendre confiance, vous
  eussiés congnu par luy que je ne cheris rien tant que les occasions de vous en tesmoigner des effets. J'escris a
  [name] ce que ce gentilhomme alloit faire par dela, et vous supplie tres humblement, Monsieur, me continuer l'honneur
  de vostre bienveuillance et croire que je vous honnor-"
- f. 241: "-e et cheris ce qui se peut. S'y vous trouviés a propos de disposer [name] d'envoier ledit [name] de la part
  de Sa Majesté vers [name] pour se resjouir de sa santé apres la longue maladie qu'il a eue, je m'asseure que les
  personnes que vous aimés n'en seroint marris, et de mon costé je leur ouvriray mon coeur de tout ce que je jugeray
  estre du [..] [67] et du [..], vous conjurant me faire la faveur d'asseurer Sa Majesté du zele que j'ay a son tres
  humble service, estant, Mo[nsieur], [..] vostre tres humble et fidel serviteur Nicle(?). De Nancy le [..] decembre."

## Persons, date and an independent key (12 Oct 2026, contributed by WAINUT)

Contributed by WAINUT (a Dutch AI company, https://github.com/WAINUTAI); the work was done with Claude Opus 5.5 subagents. It is a separate line of
work from the sessions above and should not be counted with them in `profile.json`. The decipherment of this letter is
Bourdeau's (19 Sept 2026, above) and, per Lasry, Sheila Richards's before that. This section adds (1) a proposed
identification of the writer, the three code signs and the recipient, with a probable year, and (2) an independent
transcription and key, compared with the ones in this folder. `key.json`, `hand_p*.txt` and `reading.txt` are unchanged.
Files in `wainut/`: `transcription_R927.txt`, `key_R927.tsv` and `plaintext_R927.txt` (our transcription, key and
plaintext of ff. 243 and 241) and `compare_keys.py` (the comparison; standard library only).

### Independent transcription and key

WAINUT transcribed ff. 243 and 241 by hand from the three DECODE images and recovered the key with a French language
model, before we knew of this folder. Our notation turns the images 90° counter-clockwise (the writer's frame) and names
the nine pigpen cells by their look in that frame; the key has 20 signs (cell shape + 1-3 dots), one letter each, and
does not separate inner strokes. `python targets/sp106r927/wainut/compare_keys.py` maps the two notations (archive
sides R->T, T->L, L->B, B->R) and gives:

- **Key.** All 20 of our sign values agree with `key.json` for the same sign: 18 are identical, and in 2 `key.json` has
  a polyphone that contains our value (C1 = f/q, ours f; F2 = l/h, ours h). `key.json` also has 6 plain signs we do not
  use (C3, H3, I3, K1-K3) and 15 inner-stroke signs that our transcription does not separate. The two keys were found
  separately and do not contradict each other on any shared sign.
- **Transcriptions**, aligned line by line on cell shape (code signs and lost signs left out): 849 signs aligned over
  the two pages; 810 (95.4%) also have the same dot count, and 833 (98.1%) decode to the same letter, each with its own
  key. A polyphone counts as agreeing when one of its values is ours, so the second figure is generous.

Differences that matter for the text (signs in `hand_p*.txt` notation):

- f. 243 c2, the word before "-age de ce gentilhomme": `hand_p3.txt` has A1 D*2 E2 ("nri", regularised as "mari-age"
  with one sign marked unread); we have A2 D1 E2 ("uoi"), which gives "du voiage de ce gentilhomme" with every sign read.
  Two dot counts and an inner stroke differ, and we cannot settle them at the 2300-px DECODE resolution. "Voyage" fits
  the next clause ("lequel salua dernierement [67] de la part de [6] mon maistre").
- f. 241 c12: we read "[se]ruice du [67] et du uos[tre]", i.e. "du service du [67] et du vostre"; one dot count and one
  cell shape differ from `hand_p1.txt` ("b_ruiledu ... et du uoii"), and both ends of the line are damaged.
- f. 241 c17: we read the head as "sieur" (H2 E2 E1 A2 I2), giving "estant, Mo-sieur, vostre tres humble";
  `hand_p1.txt` has H1 E2 E1 A1 I2 ("bienr"). Two dot counts differ.
- **Code signs.** Both transcriptions have code signs in the same seven places, but the images show three different
  signs there: a "67" (f. 243 c5, first sign; f. 241 c2 and c12), a lone "6" (f. 243 c5 before "mon maistre"; f. 241 c4)
  and a circled sign (f. 243 c18; f. 241 c3). `hand_p*.txt` writes all of them as '@' except the "67" of f. 241 c12.
  Kept apart, the passages read: "lequel salua dernierement [67] de la part de [6] mon maistre"; "disposer [67]
  d'envoier ledit [@] de la part de Sa Majesté vers [6] pour se resjouir de sa santé apres la longue maladie qu'il a
  eue"; "du service du [67] et du vostre". So [67] is a king ("Sa Majesté" in the same sentence), [6] is the writer's
  master, recovering from a long illness, and [@] is a man the writer has written to and whom [67] could send to [6].
- **Signature** (f. 241 c18, last five signs). Both transcriptions have the same five cell shapes and differ in the dots
  of signs 1 and 3: `hand_p1.txt` has A1 E2? F1? F3 E1 = "nicle"; we have A2 E2 F3 F3 E1 = "uille", i.e. "Ville" (our
  transcription marks the first sign uncertain). The dots are faint at the DECODE resolution, and we cannot decide
  between the two readings from the image. **This is the weak link of the identification below**: it rests on "Ville"
  and on the content, and "Nicle" would not support it.
- **Page structure.** Images P2 (f. 242 here) and P3 (f. 243) show the same leaf, with the same holes, blots, stains, line
  breaks and sign forms, photographed with the paper flap folded down (P2) and lifted (P3). We therefore think f. 242
  is not a second copy of f. 243 but the same page. If so, the sign-for-sign agreement of `hand_p2.txt` with
  `hand_p3.txt` checks the transcription, not the text, and the text "under the flap" on f. 242 is visible on P3. How the
  folio numbers 241-243 fall on the three images needs the original.

### Who wrote it, to whom, and when (hypothesis)

This is inferred from the content and from English and Lorraine sources; no document found so far names the persons
of R927. The confidence figures are our own estimates, not measurements.

| Item | Proposed identification | Confidence |
|---|---|---|
| Writer (signature "?ille") | Henri de Livron, marquis de Ville(-sur-Illon), first gentleman of the chamber of Charles IV, Duke of Lorraine, and his envoy to Charles I | about 70% |
| [6], "mon maistre", recovering from a long illness | Charles IV, Duke of Lorraine | about 70% |
| [67], the King, "Sa Majesté" | Charles I of England | about 75% |
| "Monsieur", the recipient | Henry Rich, Earl of Holland; second choice James Hay, Earl of Carlisle (about 15%) | about 40% |
| [@] | not identified; Walter Montagu is a guess | about 25% |
| Year | December 1629 most likely; alternatives 1630, 1627, 1644/45 | 1629 about 35% |

Evidence:

- **Ville as the Duke's envoy to Charles I.** The Venetian ambassador's dispatch of 5 April 1628 reports that "M. de
  Rilegia" had "come express from Lorraine" and been received by Charles I; the editor identifies him as "Henry de
  Livron, Marquis of Villa" (CSP Venice XXI, p. 48 and note 6, in pp. 41-51). A warrant of 14 March 1628 pays the
  Earl of Carlisle £200 "for an entertainment which his Majesty is pleased to give to Charles Henry de Livron Ville"
  (CSP Domestic 1628-29, p. 16). Haussonville calls him "premier gentilhomme de sa chambre" when the Duke sent him to
  demand the release of Walter Montagu, arrested in Lorraine in 1627 (*Histoire de la
  réunion de la Lorraine à la France*, vol. I, p. 217).
- **Ville and Holland.** In May 1629 Charles I orders Captain Mennes to "waft the Marquis de Ville, employed to the King
  by his Majesty's cousin the Duke of Lorraine" to Dunkirk. The next entry, "wholly written by the King", is to Henry
  Earl of Holland: he is to tell "Mr. de Ville" that if he will not go in the King's ship, "the King will complain of him
  to Rosabella" (CSP Domestic 1628-29, p. 553). "Rosabella" is very probably the duchesse de Chevreuse, to whom Holland
  was closely attached; that would fit "les personnes que vous aimés" on f. 241. This reading of the alias is an
  inference.
- **Holland handled Lorraine business.** A Lorraine messenger, Sandrin, landed at Dover at the end of February 1629
  with letters from the Duke and said "his business was to Lord Holland from the Duke of Lorraine" (CSP Domestic 1628-29,
  pp. 481, 485).
- **The illness.** When Gaston d'Orléans came to Nancy on his flight to Lorraine (1629), he went to see the Duke "qui
  était malade" (Haussonville I, p. 234). How long that illness lasted is not established here.
- **The name.** Ville signed "Henry de Livron Ville" (treaty of Liverdun, 26 June 1632; Haussonville I, pièces
  justificatives, pp. 508-509), so "Ville" is the name he signed with.

What would settle it: TNA SP 78/86/104 (Charles IV to Charles I, April 1630) and SP 78/83/78 (Charles I to the Duke,
23 Nov 1628); autograph letters signed "Ville" in SP 78 or SP 16, to compare the hand and the signature; a life of
Charles IV giving the length of the 1629 illness; the original of SP 106/10, for the dots of the signature and any cover
or address; and Richards (next paragraph).

### Richards 1974 (not seen)

The book Lasry cites is probably Sheila R. Richards, *Secret Writing in the Public Records: Henry VIII - George II*
(HMSO, London, 1974): the TNA catalogue entry for SP 106/10 says "Some deciphered transcript are published in Secret
Writing in the Public Records: Henry VIII - George II by Sheila R Richards (HMSO, London, 1974)". We have not seen the
book. It may print the decipherment of this letter, and it may already name the writer and the recipient. Until it is
checked, the identification above is a hypothesis that may not be new; the recipient and the year are its least secure
parts, and the signature reading is its weak link.

### Review of the WAINUT section (12 Oct 2026)

Re-run: `compare_keys.py` gives the figures above (20/20 signs consistent; 849 aligned, 95.4% same dots, 98.1% same
letter); these measure agreement between two transcriptions, not a read share. The page-structure claim was checked on the
DECODE images and is right: P2 and P3 are one leaf (same circled sign, blots, hole and line breaks), flap down and lifted.
Adopted in `reading.txt` and on the page, credited to WAINUT: "du voiage" (f. 243 c2; A2 D1 E2 = u o i with `key.json`),
"Mo-sieur" (f. 241 c17; H2 E2 E1 A2 I2 = s i e u r), and the split of the code signs into [67], [6] and a circled sign
[@]. Kept open: the signature, "Nicle" or "Ville". "du service du [67] et du vostre" (f. 241 c12) is a WAINUT
conjecture over damaged line ends, not a reading. The persons are a hypothesis; the CSP Venice XXI note (Rilegia =
Henry de Livron, Marquis of Villa) was checked online, CSP Dom p. 553 and Haussonville were not. `hand_p*.txt` and
`key.json` are unchanged, so the `measure.py` figures stand.

## Remaining gaps
- f. 241 c12 and c17 ("b_ruiledu ... et du uoii", "bienr"; WAINUT reads c17 "sieur", adopted, and conjectures c12 "[se]ruice du [67] et du uos[tre]") and single signs at the ends of c13, c15 and the day in c19 - blocker: illegible; under ink blots and a stain or ambiguous at 2300 px; f. 241 has no second copy, TNA has not digitised SP 106 and DECODE has no larger image
- the '@' (circle/9) signs, the clear "67", the date numeral and the signature "Nicle"(?) - blocker: no-key-material; 14 signs in name positions, too few to value from context, and no nomenclator survives with the letter or in the neighbouring records
- two lost signs on f. 243 (c2 blot, c6 paper hole) - blocker: illegible; there is no second copy (P2 is the same leaf with the flap down), so only the original or a better image can settle them
- sender, recipient and year - blocker: no-key-material; the names sit in the '@' code signs; no docket or address leaf in the record

## Escalation
- [x] siblings: neighbouring SP 106/10 records R922-R933 opened (2 Oct 2026); none is in this pigpen; f. 242 at first taken for a second copy of f. 243; corrected 12 Oct 2026 (WAINUT, PR #30): P2 and P3 are the same leaf, flap down and lifted, so the comparison checked the transcription only
- [x] clear-pages: no clear page, docket or decipherment on ff. 241-243 or in the neighbouring records; the top half of f. 241 is show-through from another leaf, not text
- [x] known-keys: the pencil flap key tested in all orientations and rejected
- [x] print: web search (SP 106/10 pigpen, Nancy), the GL.htm copies in the repo and Tomokiyo's Cryptiana index (only the Walsingham-Wilkes pigpen): no edition; Sheila Richards, Secret Writings (1973), reported by Lasry, not seen; CSP needs a year or names
- [x] key-rebuild: homophonic key built by annealing (hc3.py) on the p. 3 hand transcription plus hand anchors (key.json); extended 2 Oct (H3, C*2, C1/F2 polyphones) and 3 Oct (F*1 = l, D*1 = o); joint re-anneal over all pages tried (anneal.py), over-fits
- [x] retry: pp. 1-2 hand-transcribed (2 Oct) and every unread word re-read sign by sign at 3-4x (3 Oct); measured 84.0% -> 95.6%
