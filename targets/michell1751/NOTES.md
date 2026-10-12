# Frederick II to Louis Michell, Berlin, 28 December 1751 (KHA, Prins Willem V inv. 198; DECODE R1957)

Catalogue item 215 (class C, scored by rule). Worked 19 Sept 2026.

**Outcome: found in print.** The text this cipher hides is printed in the *Politische Correspondenz Friedrichs des Grossen*,
vol. 8 (Berlin 1882), no. 5263, pp. 576–577, "Au secrétaire Michell à Londres, Berlin, 28 décembre 1751", edited from the
minute ("Nach dem Concept"). The copy at The Hague is the Dutch interceptors' copy of the letter as sent, in the Prussian
numerical nomenclator; nobody had matched the two until now. The code itself is not rebuilt here beyond the anchors below.

## The document

Two pages (DECODE images P2 = first page, P1 = second page; the DECODE order is reversed). A clear heading and opening, 550
code groups, a clear date line and a copied signature:

- *Au S<sup>r</sup> Michel à Londres.* / *J'ai reçu votre dépêche du 14<sup>e</sup> de ce mois,* 1555 1550 15 144 66 6203 …
- … 6472 403 2179 4004 1437. *A Berlin ce 28 décembre 1751.* *(signé) Féderic.*

Groups run from 2 to 6472, written with a point between them. A few groups are underlined (single, double or triple
strokes: 533, 2102, 206, 211, 362, 4013 …); two corrections are written above the line (759 over a struck group, 5760 over
a struck 5760-like group). Full transcription in `transcription.txt` (ciphertext only in `ct.txt`; `ct.txt` corrected 12 Oct 2026 for 27 groups
where 0 was read for the theta-shaped 8, list in `ct_corrections.tsv`, old file `ct_2026-09-19.txt`).

## Why it is PC 5263

1. The clear opening "J'ai reçu votre dépêche du 14 de ce mois" is word for word the opening of no. 5263. The other letter
   to Michell of the same date at The Hague (DECODE R1955, "(1)") opens "Toutes vos dépêches m'ont été bien rendues et la
   dernière est du 14e de ce mois" and uses a different code (fractional groups like 1½, 150½, 660½); it is the letter
   DECODE's note calls "a letter of the same date with different length". R1955 is not this target and is not read here.
2. Length: 550 groups against 438 words of print after the opening, a ratio of 1.26, usual for a nomenclator that spells
   rarer words in syllables.
3. Repeated groups fall in the same order and at the same relative places as repeated words of the print (`anchors.py`,
   the largest positional gap across all occurrences shown):

   | group | word | occurrences | max gap |
   |---|---|---|---|
   | 1064 | Vienne | 4 | 0.022 |
   | 545 | avec | 3 | 0.024 |
   | 4364 | faire | 6 | 0.039 |
   | 4310 | Sardaigne | 3 | 0.039 |
   | 3042 | dessein (corrected 12 Oct: *sur*; *dessein* = 700, the group before it) | 3 | 0.043 |
   | 87 | encore | 3 | 0.017 |

   Other probable equivalents from local context (corrected 12 Oct 2026, see the review section at the end: 169 = *que*,
   47 probably *affaire*, *et suis* = 15 144, 1555 1550 the opening pair): 169 = *de* (11×), 47 = *roi* (in *le roi de Sardaigne* = 16 140 47 169
   4310, and 3279 47 twice for *le roi* before *d'Angleterre*), 1555 1550 = *et suis*. 1900 fits *Pologne* by position
   (3×, gap 0.046) but 4366 (4×) also sits near *Pologne*; not settled.

## What the letter says (from the print)

Frederick agrees with Michell that the King of Sardinia will join the Austro-Spanish treaty being negotiated at Madrid.
He has learned in secret that Vienna and St Petersburg plan to make Prince Charles of Lorraine the next King of Poland,
and reads Austria's Italian neutrality treaty as freeing its hands for that. Michell is to find out whether London knows
of the plan, or whether Vienna settled it with Russia alone; Frederick suspects the Empress-Queen's new cessions to
Sardinia were made on George II's advice, with Poland as her compensation. Michell is to say how long the present
pacific system of the English ministry will last if George II lives some years more, to report to the King alone,
without copies to the foreign department, and to say whether George II grieved for the Queen of Denmark (d. 19 Dec)
and for the Duke of Cumberland's dangerous illness.

The instruction "report to me alone, without doubles to the department" is why two letters went to Michell that day: the
ministerial one (R1955) and this immediate one, both intercepted and copied in The Hague.

## Open

- (Superseded 12 Oct 2026: WAINUT rebuilt the code, 179 values, see below.) The code is not reconstructed; a full alignment of the 550 groups to the print would give most of a Prussian 1751
  nomenclator (numbers up to ~6500, homophones for common words). Worth doing if other Prussian ciphers of 1750–52
  come up.
- R1955 (the ministerial letter) is in a different code; the ministerial rescripts are not in the *Politische
  Correspondenz*, so its plaintext is not in print. Not a catalogue target of its own.

## Sources

- DECODE R1957 (images `IMG_R1957_I13456_P1.png`, `IMG_R1957_I13457_P2.png`) and R1955, fetched with the DECODE cookie;
  images git-ignored.
- *Politische Correspondenz Friedrich's des Grossen*, Bd. 8 (1882), no. 5263, pp. 576–577:
  https://archive.org/details/politischecorres08freduoft

## R1955, the other letter of 28 December 1751: attempted, open

Worked 19 Sept 2026 (catalogue entry for DECODE R1955). Transcribed in full in `transcription_r1955.txt`.

- The Dutch copy is headed *Lettre du Roi de Prusse au Secrétaire Michell du 28 Decemb. 1751* and signed *Féderic*, but
  the *Politische Correspondenz* prints only one letter to Michell of that date (no. 5263 = R1957). This one is the
  ministerial rescript, issued in the King's name and not printed.
- The clear opening is *Toutes vos dépêches m'ont été bien rendues et la dernière est du 14e de ce mois*. Then come 362
  code groups (2 to 5346, most under 3600, with half-groups 1½, 10½, 40½, 150½, 180½, 660½) and the date.
- It shares no code with R1957: only 19 of their distinct groups coincide, and those are chance collisions.
- 295 of the 362 groups are distinct, and the commonest (2, 230) occurs 5 times. That is a large two-part code with
  homophones even for *de* and *que*, so ciphertext-only analysis has nothing to work with. The pair 1487 50 recurs 3×.
- No printed or online decipherment was found. What could open it: the Prussian ministerial code of 1751 (GStA PK, I. HA
  Rep. 96 / Rep. 9 Chiffres), Pierre Lyonet's decipherments for the States General (see K. de Leeuw, *Diplomacy &
  Statecraft* 10, 1999), British decyphers of Michell's correspondence (BL Add MS Newcastle papers; TNA SP 107), or
  other rescripts to Michell in the same code with known content. DECODE R1953 (von der Hellen to the King, 4 Jan 1752,
  KHA inv. 196) was checked the same day and is in a different, smaller code (groups under ~1650, frequent repeats), so it is no sibling of R1955.

## Contributed by WAINUT, 11-12 Oct 2026: the cabinet code rebuilt; R1955 partly decoded in Michell's envoy code

This section is a contribution by WAINUT (a Dutch AI company, https://github.com/WAINUTAI); the work was done with Claude Opus 5.5 subagents on
11 Oct 2026, three weeks after the work above and before we knew of it (we found this folder on 12 Oct). Our match of
R1957 with PC 8 no. 5263 is therefore an independent confirmation of Bourdeau's identification and adds nothing to it.
What the section adds: (1) a reconstruction of the cabinet code, tested blind on R1957; (2) the finding that R1955 is
in the code of Michell's own reports, with 26% of its groups decoded from contemporary Dutch decipherments of two of
those reports, and a negative test for a printed parallel text. Files are in `key1751/`. Every number below was
checked again on 12 Oct 2026 by re-running the scripts there (Python 3, standard library plus numpy; run from
`key1751/`) or counting in the files there; the hand check in `blind_test_summary.txt` is quoted as recorded.

### 1. The cabinet code (R1957 and six letters in Fagel 5177)

**Sources.** Nationaal Archief, 1.10.29 (Fagel) inv. 5177, scans 95-101, holds Dutch copies of six letters of
Frederick II to Michell in the same numerical code, 2 Nov - 25 Dec 1751, without decipherment. Two carry the note
"Nonsense ou autre Clef", and a slip pasted on scan 95R says "Ayant examiné ces Lettres, je trouve qu'elles n'ont
point de Sens, ou qu'elles sont d'une clef que nous n'avons pas". Their concepts are printed in PC 8 nos. 5169 (2
Nov), 5197 (16 Nov), 5208 (23 Nov), 5227 (3 Dec), 5231 (7 Dec) and 5253 (25 Dec). Our transcriptions:
`key1751/fagel5177/` (1,813 groups).

**Key v1 and the blind test.** Aligning the six letters with their printed concepts gave a partial table of 72 entries
(`key_cabinet_v1_frozen.tsv`). Its content was committed in our research repository at 16:07 on 11 Oct 2026, before
R1957 was transcribed; the hashes are in `frozen_keys.sha256`. R1957 was then transcribed (`R1957_tx.txt`, 548
groups) and decoded with v1 before PC 5263 was consulted (`blind_R1957_key_cabinet_v1_frozen_20261011T210822.txt`):
181 groups (33.0%) receive a value.
- Alignment-free test (`scripts/lcs_test.py`): the 168 decoded whole words have a longest common subsequence of 123
  with the 460 words of PC 5263. 500 shuffles of the same words give a mean of 58.9 and a maximum of 65. Against 12
  other letters to Michell in PC 8 (not used for the key) the decode scores at shuffle level (e.g. no. 4605: 28 against
  26.5).
- Per group (`scripts/eval_blind.py`, against the alignment with PC 5263 made after the blind run, `align_R1957.txt`):
  142 confirmed, 9 partly right ('le roi' where the group means 'le roi de Sardaigne', '-s' for s'), 6 contradicted,
  24 not checkable. A check by hand of the unclear cases (`blind_test_summary.txt`) gives 150 confirmed and 6
  contradicted, all six from two wrong v1 entries: 156 is *entre*, not *de*, and 4366_ is *le*, not *Prince* (the
  script's six are a different six: four of these cases plus one 104 *d'*, partly right in the hand check, and one 795
  *-ere*). These per-group figures are partly circular, because the alignment was made after seeing the decode; the
  LCS test is the unbiased one.

**Key v2.** R1957 was then aligned with PC 5263 (297 positions fixed by hand, the rest filled by dynamic programming)
and all seven letters were re-aligned with the growing key: `key_cabinet_v2_final.tsv`, 179 entries. Our grades
measure evidence: A = two or more agreeing occurrences in two or more letters (122 entries), B (20), C = agreements
from the automatic alignment only (37, weak). They are not the README H/C/M/I scale; in those terms every entry comes
from a known-plaintext letter. `key_cabinet_v2_curated.tsv` gives the evidence for 43 syllable, ending and phrase
entries. v2 gives a value to 381 of R1957's 548 groups (69.5%); most of the rest are one-off syllables of spelled-out
words and names. v2 has not been tested on a held-out letter: we know of no further letter in this code.

**R1957 group by group.** `R1957_decipherment.tsv` gives for every group the v2 value and grade, the word of PC 5263 it
aligns with, and a status: K, key value agrees with the aligned word (315); M, position fixed by hand, no key value
(44); A, automatic alignment only, unverified (107); k?, key value differs from the automatic alignment (51); N/kN,
aligned with nothing (31). This is the printed concept carried through the cipher, so it is no independent
decipherment of R1957; where the sent text departs from the concept the alignment marks it with '!'.

**Code conventions seen.** Values do not follow the alphabet (*de* = 7, 258, 2179); legible, separated groups run from
7 to 6492 in our seven cabinet-code transcriptions; homophones for function words (*de* = 7, 2179, 258; *que* = 16,
169); plural and final s as separate groups (5814, 82); endings as separate groups (66 -e/-é, 1730 -er, 3243 -ment);
names spelled by syllables; phrase groups (4310 *le roi de Sardaigne*, 190 *le roi d'Angleterre*); a double underline
can change the value (190= *roi d'Angleterre* after du/au).

**Against the values given above.** Agreed: 1064 *Vienne*, 545 *avec*, 4364 *faire*, 87 *encore*; 4310 is the
phrase group *le roi de Sardaigne* (5 agreeing occurrences in 3 letters). Different:
- 3042 is *sur* (8 occurrences in 5 letters). *Dessein* is 700, the group before 3042 in each "dessein sur la
  Pologne"; the two sit side by side, which explains the positional match of 3042 with *dessein*.
- 169 is *que* (22 occurrences in 5 letters). The opening "16 140 47 169 4310" gives *que l'affaire que le roi de
  Sardaigne* (print: "du sentiment que l'affaire que le roi de Sardaigne entre ..."). 47 is then probably *affaire*: it
  also stands in "3279 47" = *des affaire(s)* before *d'Angleterre* and before *étrangères*. This value is inferred
  from R1957 alone and is not in v2.
- 1555 1550 is an opening pair that matches no word of the print; *et suis* is 15 144.
- 1900 is *Pologne* (three positions fixed by hand); 4366 is *le*.

**Transcription of R1957 against `ct.txt`** (`scripts/compare_tx.py R1957_tx.txt ../ct.txt`): 513 of our 548 groups
agree in sequence. `ct.txt` counts the two groups written above struck ones (759, 5760), which our file keeps as
notes: hence 550 against 548. 35 groups differ, 28 of them only by 8 against 0, and in 27 of these we read 8: the
first hand writes 8 as a narrow oval with an inner stroke (858, 894, 5814 in our reading; 050, 094, 5014 in `ct.txt`).
None of the 2,721 groups in our eight transcriptions (six Fagel 5177 letters, R1957, R1955) begins with 0. Where the
independent v1 table decides, it favours our reading in 5 places (538 *a*, 894 *les*, 5814 *-s* twice, 82 *-s*) and
the reading of `ct.txt` in 2: 2439 *savoir* ("votre savoir faire", where we read 2139) and 586 *vous* (where we read
506). In two more places `ct.txt` has 104 (*d'* in v1) where we read 184; *d'* fits neither place in the alignment.

### 2. R1955: Michell's envoy code

**Key material.** DECODE R1050 (Michell to Frederick II, London 5 Sep 1752) and R1051 (London 12 Nov 1751) are Hague
copies of Michell's own reports with the contemporary Dutch decipherment written over the numbers (attributed in our
notes to Pieter Lyonet; we have not compared the hand; on Lyonet's work for the States General see De Leeuw 1999,
cited above). DECODE's transcriptions of them (March 2020) give each line of the decipherment above its cipher line.
Pairing them token by token gives 512 code-word pairs for 271 codes; 5 lines with unequal counts are skipped. The code
held over the ten months between the two reports: 40 codes occur in both, 32 with the same commonest value; 4 more
differ only by inflection or by a tie between variants (*continuer*/*continue*, *dernier*/*dernière*, *on*/*l'on*,
*d'*/*d*), and 4 disagree (800, 1005, 1805, 2341).
The table derives from DECODE's transcriptions, so neither it nor they are committed here. `scripts/envoy_key.py
<folder>` rebuilds it from DOC_R1050_*.txt and DOC_R1051_*.txt (DECODE login needed); `frozen_keys.sha256` holds the
hash of the table used on 11 Oct.

**R1955 is in that code.** The envoy table gives a value to 95 of R1955's 360 groups (26.4%), against 10 (2.8%) for
cabinet v1 and 20 (5.6%) for v2; on R1957 it gives 30 of 548 (5.5%). Adjacent decoded words in R1955 form attested
French word pairs more often than chance (`scripts/coherence.py`): 19 of 30 adjacent pairs, against a mean of 11.1 for
2000 permutations of the same values (p = 0.001), with word pairs taken from our corpus of 18th-c. diplomatic French
(French paragraphs of the Politische Correspondenz; the first 6 M characters used come from vols 8-13 only; spelling
partly archaised, e.g. -ait to -oit, at random; not included). With PC vols 8-9 alone as corpus the result is weaker:
14 of 30 against 9.5 (p = 0.046). The test has little power when the decoded values are mostly function words: the v1
decode of R1957, which the LCS test shows to be right, scores 26 of 44 against 23.7 (p = 0.28).

**Reading.** `R1955_reading_line.txt`, '·' for a group without a value. Legible fragments include "... avis ... sur
... negociation avec ... de Vienne ... les difficulte(s) ... article ... du ... Prince Stadhouder ... maison ... cet
avis et ... états ... depuis avis est ... ce projet ... nouvelle ... doit être ... des esperance(s) de ...". These are
fragments of a trial decoding with a table from two other letters; the subject cannot be stated with confidence beyond
Dutch affairs (the Prince Stadholder, a house, the States) and a negotiation that involves Vienna.

**Circular-letter test (negative).** Hypothesis: R1955 repeats the wording of a royal letter of the same days printed
in PC 8-9, which would then give its plaintext. The scoring rule was fixed before the results were seen
(`scripts/circular.py`): longest common subsequence of R1955's 77 decoded words with each French PC letter of vols
8-9, z against 100 shuffles; candidates are the letters of 22 Dec 1751 - 10 Jan 1752 (21), controls the other 1,329;
a candidate counts only with z >= 4 and above every control. Best candidate PC 5268 (to Michell, 4 Jan 1752), z =
2.69; highest control PC 5117, z = 4.85; no candidate qualifies. Our first run also scored five Dutch decipherments of
royal letters to von der Hellen of 3-24 Dec 1751 (Fagel 5177, our transcriptions, not included here): z from -2.01 to
0.57. Positive control (`--power`): a random 17% of the words of PC 5263 or 5262 scores z = 27.6 to 31.3 against its
source and 5.8 to 10.9 against a 50% paraphrase of it, with control maxima of 2.7 to 5.3. A shared wording would have
shown.

**Transcription of R1955 against `transcription_r1955.txt`** (`scripts/compare_tx.py R1955_tx.txt
../transcription_r1955.txt`): 352 of our 360 groups agree in sequence. Differences: the underlined run of nine digits
without separators on l. 16 is one unsplit group in our file (best split 2 2407 2398) and "2240? 7? 2398" there, hence
362 against 360; and 3356/3336, 194?/1949 (1949 is also our preferred reading), 247/227, 2?07/2407, 1401/1403,
1517/1857 (p. 2 l. 1), 1321/1821 (p. 2 l. 3), ours first. The envoy table has values for 247 (*me*) and 1401
(*depuis*) and none for 227, 1403, 1857 or 1821; that is weak support only.

**Against the notes above.** We agree that R1955 is in another code than R1957, and we have nothing against its
identification as the ministerial rescript of that day. Its code is the one Michell used for his own reports to the
King (R1050, R1051); the King's immediate letters (R1957 and the six in Fagel 5177) use the cabinet code. Of the leads
listed above, the contemporary Dutch decipherments (the Lyonet lead) are the one that worked.

### Established and inferred
- Established: v1, built without R1957, predicts R1957's wording in order (LCS 123 against at most 65 for shuffles);
  grade-A v2 values recur in two or more letters; R1955 is not in the cabinet code; the envoy table fits R1955 far
  better than the cabinet tables and gives coherent neighbours more often than chance.
- Inferred: grade-C v2 values; 47 = *affaire*; the sense of the R1955 fragments; the attribution of the R1050/R1051
  decipherments to Lyonet.

### Residual risks
- The time order of the blind test rests on our own records (file times, hashes and a commit in our private research
  repository); there is no third-party timestamp.
- The per-group blind figures are partly circular (see above), and v2 has had no held-out test.
- The R1955 values come from two letters ten months apart; changed or homophone values could mislead, and 26% gives
  fragments only. The envoy table depends on DECODE's transcription of the decipherments, which we did not check
  against the images line by line.
- A contemporary Dutch decipherment of R1955 may survive in Nationaal Archief 1.01.50 inv. 159 (not digitised); more
  decipherments of Michell's reports are probably in KHA A31-1181 (not online). Neither was consulted.
- Uncertain digits are marked '?' in our transcriptions; the readings above use them as written.

### Next steps
- Decipherments of further Michell reports (KHA A31-1181) to extend the envoy table and decode the rest of R1955.
- Nationaal Archief 1.01.50 inv. 159, for a contemporary decipherment of R1955.
- Any further letter in the cabinet code, for a held-out test of v2.

### Files (`key1751/`)
- `fagel5177/*.txt`, `R1957_tx.txt`, `R1955_tx.txt`: WAINUT transcriptions (notation in each header).
- `key_cabinet_v1_frozen.tsv`, `key_cabinet_v2_final.tsv`, `key_cabinet_v2_curated.tsv`, `frozen_keys.sha256`.
- `blind_R1957_key_cabinet_v1_frozen_20261011T210822.txt` (the blind output as written), `blind_test_summary.txt`,
  `align_R1957.txt`, `R1957_decipherment.tsv`, `R1955_reading_line.txt`, `circular_scores.tsv` (first run, which
  also scored our transcriptions of Fagel 5177 decipherments to von der Hellen).
- `pc_michell.json`: PC 8-9 texts of the letters to Michell used here. Not included: build it locally from the UB Trier
  digital edition with `pc_html2txt.py` and `build_pc_michell.py` (git-ignored).
- `scripts/`: `decode.py`, `common.py`, `lcs_test.py`, `eval_blind.py`, `envoy_key.py`, `coherence.py`, `circular.py`,
  `pc_html2txt.py`, `build_pc_michell.py`, `compare_tx.py`. Files derived from DECODE transcriptions and the full PC volumes are git-ignored.

## Review of PR #29 and corrections (Bourdeau, 12 Oct 2026)

Reviewed and merged with Claude Opus 5.5. Checks re-run here:

- Blind test re-run with `lcs_test.py` on a `pc_michell.json` built from our own archive.org OCR of PC 8-9 (not the
  Trier text WAINUT used): 168 decoded words, LCS 121 against 477 print words; shuffles mean 58.9, max 65; the 12
  control letters at shuffle level. `eval_blind.py`: 142 confirmed, 9 partial, 6 contradicted, 24 not checkable.
- v2 gives a value to 381 of 548 groups of `R1957_tx.txt` (69.5%), confirmed.
- The LF hash of `key_cabinet_v1_frozen.tsv` matches `frozen_keys.sha256`. That v1 was fixed before R1957 was
  transcribed rests on WAINUT's frozen hash and their private commit history (16:07 and 21:29, 11 Oct), which is not
  public; the PR arrived as one commit.
- Spot checks: Fagel 100R (3 Dec) decoded with v2 follows PC 5227 in order ("savoir exactement si le roi de Sardaigne
  entre ... entre les cours de Vienne et de Madrid ... afin d'en être bien ..."); 099R (7 Dec) follows PC 5231 ("ainsi
  que vous marquez que la ... à Londres que le roi de Sardaigne entre comme ... dans la négociation qui se traite").
  These letters trained v2, so this shows consistency, not independence.

Corrections to our 19 Sept anchors, accepted from WAINUT's key: 3042 = *sur*, not *dessein* (700 3042 la 1900 =
*dessein sur la Pologne*, twice; the two groups sit side by side, hence the positional match); 169 = *que*, not *de*
(22 occurrences in 5 letters); 47 probably *affaire*; 1555 1550 is the opening pair and *et suis* is 15 144; 1900 =
Pologne and 4366 = *le*, which settles the Pologne question above. 1064, 545, 4364, 87 confirmed; 4310 is the phrase
group *le roi de Sardaigne*.

`ct.txt`: 27 groups corrected from 0 to 8 (`ct_corrections.tsv`); with them, v2 gives a value to 373 of its 550 groups
(357 before). The other eight differences with `R1957_tx.txt` are left as they were.

Outcome: R1957 stays read from existing decipherment (the print), complete; the cabinet key is a partial key recovered
from external plaintext (WAINUT); R1955 is read in part, 95 of 360 groups (26.4%), fragments only, with outside
blockers (no further decipherments of Michell's reports online; NA 1.01.50 inv. 159 not digitised).
