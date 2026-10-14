# Siena, Concistoro 2308 nos. 6 and 24: Cristofano's letters to the Signori, key R4755 (c. 1431-38)

Status: read in part (outside solution, verified here). Key recovered ciphertext-only by the solver, then matched
to the filed key DECODE R4755. No. 6 93.4% of its decrypted letters understood as submitted, **95.4% after the 14 Oct key correction (below)**; no. 24 72.7%, and its dorse
(8 run-over lines) is not in the submitted reading.

Split off from `targets/siena1421/` (the whole busta, catalogue 336), where nos. 6 and 24 were listed as one open
system ("nos. 6 + 24, no-key-material"). The transcriptions used below were made there on 24 Sept 2026.

## Credit

- **Solution: George Lasry**, done with Claude and with the help of ChatGPT Astra; sent to Daniel Bourdeau on
  14 Oct 2026 as a 7-page PDF ("Siena, two ciphered letters to the Signori (Concistoro 2308, nos. 6 and 24)").
  As the PDF tells it, the key was first recovered by cryptanalysis from the ciphertext only (Claude, with the
  help of Astra), and the matching historical key table, DECODE R4755, was then found in the collection (Astra).
- contributor: George Lasry (settled 14 Oct 2026; the PDF itself names no person).
- This project: independent verification on its own transcription (below), the key table as a tsv, the dorse of
  no. 24, the signature of no. 24, the dating check, and the DECODE corrections.

Files: `reading_no06.txt`, `reading_no24.txt` (the submitted reading, verbatim, credited); `key_R4755.tsv` (the
key, read here from the DECODE photograph, with the labels of our transcription); `verify.py` (the check);
`decode_no06.txt`, `decode_no24.txt` (our transcription decoded); `dorse24.py`, `decode_no24_dorse.txt`.

## The documents

| no. | DECODE | images | content | ciphertext (ours, measured) | theirs |
|---|---|---|---|---|---|
| 6 | R4795 (`Concistoro_2308_49`) | P2 text side, 15 lines; P1 verso, show-through and docket | dated 19 February, signed "Cristofano de Mont[...]" | 1,051 signs (`siena1421/transcripts/no06.tok` lines) | 1,007 |
| 24 | R4812 (`Concistoro_2308_66`) | P2 text side, 38 lines; P1 dorse: 8 run-over cipher lines + address "Magnifici et potenti signiori e ... Capitano di popolo della citta di Siena" | not dated; signed on the dorse (found here, below) | P2 2,638 signs; P1 dorse 637 (first pass) | 2,559 (P2 only) |

Both open with a clear salutation ("Magnifici et potentes domini domini mei singularissimi ...") and run on in
cipher without word division. Key: R4755 (`Concistoro_2308_10`), fasc. 1, one sheet, heading "Cifra cum
Christofano [M?]tucci(?)"; DECODE's name is "Cifra cum Christoforo Ghinucci[?]". The surname on the sheet is hard
to read; the signature of no. 6, "Cristofano de Mont‹vccia›" in the submitted reading, points to the same name
(Montucci?), not to Ghinucci. Left as a question in the DECODE note, not asserted.

Note against ourselves: `siena1421/NOTES.md` (24 Sept) already indexed R4755 as "Cifra cum Christofano ...
(Papa, Fiorentini, Veneziani, Duca di Milano, Niccolò Piccinino, Conte Francesco, Lucca ...)", dated it c. 1440 and
never tried it on nos. 6/24: the fasc. 1 alphabets were compared with the letters "by eye", and this one was missed.

## The key (R4755), checked on the DECODE photograph

The photograph `IMG_R4755_I27827_P.jpg` was fetched with the DECODE cookie on 14 Oct 2026 (git-ignored, ASSi
image); it is the same sheet as the image in the PDF. Read here: 21 letters a-u plus x, z (y has no sign); four
homophones each for a, e, i, o, u, one sign for every other letter (k, h, x included), so 36 cipher signs (k, x,
z and the o-sign "S" do not occur in these letters). Nulls, headed "Nichil importantes": seven signs (ŋ-like, a, f,
B, E, G, h). Word signs: 18 (Papa, Fiorentini, Viniziani, Duca di Milano, Nicholo Piccinino, Conte Francesco,
Luccha, Pisa, Pistoia, Siena, Pontremoli, Parma, Pietrasanta, Genova, Bologna, Messer Thomaso, Cavagli, Fanti).
All of this matches the PDF's description (36 signs for 21 letters, 18 word signs, 7 nulls).

Word signs that occur, by our transcription: CIRC 20 (= Lucca 16 + Piccinino 4: Lucca's ⊙ and Piccinino's
circled D were merged by our transcribers), RX/RX+ (Viniziani), BIGX 1 (Fiorentini), and the Duca di Milano Φ,
which our labels merged with PHI = m. Our transcribers had flagged exactly these point-framed signs as "probable
name codes". So **5 of 18 word signs occur**, as claimed (Lucca 16, Piccinino 4, Duca di Milano 3, Viniziani 2,
Fiorentini 1 in their count; our counts agree for Lucca + Piccinino = 20).

## Verification (14 Oct 2026, `python targets/siena1431/verify.py [--seed-only]`)

Our transcription of nos. 6 and 24 (made 24 Sept by agents A, H, I, before any key; sign legend in
`siena1421/transcripts/no06.txt`) was decoded with the key and compared with the submitted reading by a DP
alignment (gap cost 6).

1. **Key read off the sheet by eye only** (31 of our labels given the key value of the sign they look like, no
   fitting; `--seed-only`): our decode equals their letter at 650/941 = **69.1%** of their decrypted letters in
   no. 6 and 1,586/2,286 = **69.4%** in no. 24. LM (it-cinquecento, order 5, no spaces, per char): our decode
   -3.53 / -3.62 against a shuffled-key control of mean -4.77 / -4.77 (best of 20: -4.22 / -4.19).
2. **Labels fitted by EM** (each of our labels takes the value it aligns with most, 6 rounds, seeded from 1):
   751/941 = **79.8%** (no. 6), 1,743/2,286 = **76.2%** (no. 24) with one value per label; **90.5%** and
   **88.2%** when a label our transcribers used for two key signs counts for both. LM -3.06 / -3.34 against a
   control mean -4.03 / -4.04 (best -3.63 / -3.56). Their own reading scores -2.42 / -2.69.
3. Where we disagree, it is our transcription, not their key: our labels merge key signs that differ on the sheet
   - `t` = three key signs: o (+), q (t), f (o+t ligature);
   - `c` = h (c) and n (e-like); `c^` and `e` are both n;
   - `0` = a (o) and, 23 times, i (+o with the cross not seen);
   - `g` = i (ʒ-like) and, 16 times, e; `THETA` = d and, 25 times, o;
   - `d` and `u` are one a-sign (a reversed c with a tail); `VENUS` and `YCROSS` are one e-sign (♀);
   - CIRC = Lucca and Piccinino; PHI = m and Duca di Milano.
   No case found where a key value has to be changed to fit our transcription. The p p pair = e, which our
   notes (24 Sept) had flagged as a unit, is a key sign ("pp" under e on the sheet).
4. No independent re-transcription of their sign inventory was possible (the PDF gives their reading, not their
   transcription); their element counts (1,007 and 2,559) are close to ours (1,051 and 2,638).

Conclusion: the solution holds. The key is the right one, and our own transcription, made blind, decodes
to their letters at 69% with the key read by eye and 88-91% once our merged labels are allowed for.

## Sense share (the read bar)

Counted on their reading (letters inside ‹...› or {...} = decrypted but not understood; word signs count as one):
- **no. 6**: 62 of 941 not understood: **93.4% understood**. Below the 95% bar, but the gaps are scattered
  (‹b·›, ‹teaite›, ‹kanaa·not›, ‹adiertenaa›, ‹nilalado›, the surname ‹vccia›).
- **no. 24 (P2)**: 623 of 2,286 not understood: **72.7% understood**. Many runs: ‹chaaeiisai›, ‹lnifesstt›,
  ‹tromel··aeraomiliaetc·oa›, ‹carpelaelotecednelgnnpei›, ‹vannoafonatificas›, ‹eqnleodiaferraerapeo› ...
- **no. 24 dorse (P1)**: not in the submitted reading at all (below).
Both letters: **read in part**.

## No. 24 dorse: decoded here (`dorse24.py`)

The letter runs over onto the back: 8 cipher lines above the address (our first-pass transcription by agent E,
637 tokens, own sign legend, `siena1421/transcripts/no24.txt`). Mapped onto the key by sign shape and decoded,
it reads in stretches (LM -3.42 against a shuffled control of -3.96, best -3.63):

- L02 "... cose sono ... segrete ..." (things that are secret)
- L05 "... umilemente mi racoma[ndo] ..." (the closing recommendation)
- L06 "... a la uostra ... Signoria ..."
- L08 "... a uostra ... Signoria. Crist[ofa]no ... si racoman[d]a"

So **no. 24 is signed on its dorse by "Cristofano"**, the same writer as no. 6 ("Cristofano de Mont[...] si
racomanda"); the PDF calls no. 24 unsigned because it did not reach the dorse. The surname letters after
"Crist..." do not come out of the first-pass transcription. Graded C (probable): the forename and the formula are
clear; the rest of the dorse is not yet sense.

## Dating

The PDF dates both letters "about 1431-1432" from the war of Florence against Lucca (1429-33): Piccinino on the
road to Lucca; the King of Hungary (Sigismund in Italy 1431-33); the Council of Basel (1431); the "marquis of
Mantua" (a title "Sigismund created in 1432-1433").

Checked: the marquisate of Mantua was conferred by Sigismund on Gianfrancesco Gonzaga in September 1433, after the
peace of Ferrara (April 1433) that closed that war. No. 24 also says the marquis "è acordato col Duca di Milano"
and names "il ducha Alberto ... re d'Ongnaria". Gonzaga left Venetian service and went over to Filippo Maria
Visconti in 1438; Albert of Austria (Duke Albert V) became King of Hungary in December 1437 and King of the
Romans in 1438; Sigismund died in December 1437 ("lo 'mperadore non verrà" fits either a living emperor who stays
away or the vacancy). Florence attacked Lucca again in 1437-38, with Piccinino on the Milanese side. So **no. 24
fits 1437-38 at least as well as 1431-32**, and the Mantua title argues against a date before September 1433.
No. 6 (19 February; Piccinino's men opening the road to Lucca; Antonio Petrucci's chancellor back from Milan) fits
February 1431 or February 1437/38 (Sienese style 1430 or 1436/37). Recorded as c. 1431-38; the PDF's 1431-32 is
not adopted. This is reasoning from the decrypted content, graded M; the archive does not date either letter.

## No. 6 pushed past 95% (14 Oct 2026)

Two key values were misapplied in both the submitted reading and our check, and are settled on the key sheet R4755:
- **z is the compound "So"** (an S with a small o attached), drawn so in the z column; plain S is o. Our transcription had split it into S + u/0. Seen on the DECODE image of no. 6 in all three places: line 7 "c So d" (aduert-en-z-a), line 11 "s e n So 5 o H pp" (senz-a auere), line 13 "c So 7" (Vincen-z-o). At "bi-S-gnio" (line 7) the S stands alone and is o: *bisognio*.
- **4 = u** (the u column reads 9, H, 4, ϵ); our check had mapped 4 to i.

Readings changed (reading_no06_rev.txt; the submitted reading is kept unchanged in reading_no06.txt):
- "buona ‹adiertenaa›" → "buona **aduertenza**" (*avvertenza*)
- "tornò da Milano [a] Sena ‹aaa›vere" → "tornò da Milano **senza avere** fact[o] **nula** ‹lado›": the chancellor came back from Milan *without having done anything*, not "to Siena"; no editorial insertion needed
- "facti di Vincena{ao} da Camerino" → "facti di **Vincenzo** da Camerino"

Measured with the same rule (verify.py `understood`): 896 of 939 decrypted letters understood = **95.4%** (was 879/941 = 93.4%). Without the *nula* change: 95.0% (the margin is thin). The signature "Montuccia" would add five letters but is not legible enough on the image and is not counted.
No. 6 now meets the read bar; no. 24 stays read in part, so the target as a whole stays read in part.

## Remaining gaps

- no. 24 P2, the ‹...› runs (623 of 2,286 decrypted letters) - blocker: illegible; the runs decode but do not make sense, which points to sign misreadings at this photograph's resolution (20-25 px per sign, half of no. 6's) or to errors of the encipherer; a sign-level re-check needs a better image than DECODE's (ASSi reading room).
- no. 6, 43 letters in ‹...› (4.6%) after the 14 Oct correction - blocker: illegible; scattered single words (‹teaite›, ‹kanaa·not›, ‹rver›mo, the surname Mont‹vccia›), not legible enough at the DECODE resolution
- no. 24 dorse P1 (637 tokens), beyond the closing formula and signature - blocker: illegible; the dorse is cramped and partly lost at the fold (first-pass transcription marked "draft"); needs a better image.
- the writer's surname (Mont‹vccia›; key heading "[M?]tucci") - blocker: illegible; the signature and the key heading are both damaged or cursive.

## Escalation

- [x] siblings: every record of the busta opened in siena1421 (keys R4746-R4789, letters R4790-R4814, R1858); nos. 6 and 24 confirmed as one system; no other letter of the busta is in this key (nos. 14, 18, 25 have their own keys).
- [x] clear-pages: no. 6 P1 (verso, docket only) and no. 24 P1 (dorse, run-over cipher + address) checked; no decipherment on either.
- [x] known-keys: R4755 applied (the solver's match, confirmed here on the DECODE photograph); the other fasc. 1 keys were tried on these letters in siena1421 and do not fit.
- [x] print: Meister 1902 (pp. 50-53, three Sienese keys of the 1430s, other values), the 1952 inventory, Treccani DBI (Petrucci); no printed decipherment of either letter found.
- [x] key-rebuild: the key is complete for every letter sign that occurs (36 signs, 7 nulls); the gaps are not key gaps.
- [x] retry: both letters decoded again from our own blind transcription (verify.py), and the dorse of no. 24 decoded for the first time (dorse24.py); the ‹...› runs stay unread under both transcriptions.
