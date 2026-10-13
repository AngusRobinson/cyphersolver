# Lodovico Birago to the Duke of Nevers, Saluzzo, 13 November 1571 (BnF fr. 3251 f. 119) — numeric cipher paragraph

Tomokiyo's unsolved list ("Lodovico Birago to Duke of Nevers (1571)"); his 2024 blog post calls it a candidate
variable-length figure cipher and says "once the continuous stream of figures can be broken into tokens, homophonic
solvers may readily decipher this". No comments on the post, no GitHub prior art (checked 2026-09-16).


Sibling: Birago to Nevers, 5 April 1571, BnF Français 3252 ff. 36r–37r, deciphered in part (87.2%) by George Lasry
(with ChatGPT Astra 6 and Anthropic Opus 5.5, "BnF cipher research", 10 Oct 2026) with the Ceppo–Nevers key from
fr. 4702 / Cryptiana: [targets/birago1571](../birago1571/NOTES.md). That key has not been tried on this letter here.

## Sources in hand
- Gallica `ark:/12148/btv1b9060248g`, view f120 = f.119r (letter, cipher paragraph at foot), f121 = f.119v (close,
  date "Da Saluzzo li 13 di Novembre 1571", signature; recto f.120 is a notarial act about Carmagnola). IIIF full-size
  images fetched with a browser UA (`pages/`, `dl_native.jpg`), 8521 x 5849 px for the opening.
- Sibling letters: f.27 (view 28) and f.39 (view 40), 1570, Ceppo-Nevers symbol cipher with interlinear decipherment;
  f.82 (view 83), March 1571, same symbol cipher; f.138, f.178 (views 139, 179), 1572, Nevers-Birago symbol cipher.
  None numeric, so Tomokiyo's reconstructed keys (`keys/`) do not apply; the 1572 key has two-digit code numbers
  85 Carmagnola, 86 Turino, 89 Bugonotti.

## Ciphertext (`ct.txt`), checked glyph by glyph against the page
482 digits, 15 letters (n x7, f, m, a x2, c, l), 22 marked two-digit groups. Tomokiyo's inline "+" signs are in fact
superscript crosses over the following digits, i.e. a fourth diacritic class beside the wavy "÷", the bar and the
two dots. Marked groups (mark, digits): %76 -59 -20 :05 :36 :41 %29 :41 :25 -43 %39 %39 +98 %40 +44 %15 %39 +74
+81 +21 %05 :12 %76 (% = wavy, - = bar, : = dots, + = cross). The paragraph opens and closes with %76.
Digit counts: 0 75, 1 62, 2 41, 3 37, 4 74, 5 64, 6 5, 7 7, 8 49, 9 68. Six and seven occur almost only inside
marked groups. One extra mark ("oo" over the 2 of the opening 762) has no counterpart in Tomokiyo's transcription.

## Context from the clear text
Birago (lieutenant-general beyond the mountains, at Saluzzo) writes about the King's order to send his cavalry to
Carmagnola, the governor there (Monsr di Bellagarda), the captain La Valletta, the Marmaglia relation, the syndics,
the King and Queen [mother], and his own reputation; the cipher paragraph follows "...che di perdere sono de la mia
reputatione" and precedes "La supplico a tenermi in sua buona gratia".

## Glyph-level transcription (`ct2.txt`, 2026-09-16, from the 8521-px Gallica image at 2-3x)
Corrections to Tomokiyo: (1) the wavy sign "÷" is a standalone inline character, 9 occurrences (opens and closes the
paragraph; internal 7); (2) the dots, bars and crosses sit over single digits, 16 marked digits in all
(2~ 5- 2- 0: 8- 3. 6. 4. 4. 2. 8+ 4+ 7+ 8+ 2+ 2.), not over pairs; two of them (8- in line 1, 2. in line 7) he did not
record and his "¨12" in line 7 does not exist; (3) the dotted "i" glyph is a variant of the figure 1 (five cases,
each followed by 5 or 1, forming the commonest pairs 15 and 11); one such 1 is missing from his line 3 after the dotted
2. Total 483 digits, 15 null letters (n f m a c l), 9 wavy signs.

## Structure tests (all with matched synthetic controls)
1. Prefix-code scan (two-digit tokens begin with a digit set S, optional X0 tokens, 1xx tokens; letters as nulls or as
   symbols; Italian and French 5-gram models with a unigram penalty): on three controls the true rule is the top score
   with a full reading (-1.6 to -1.8 per 5-gram window); on the target the best rule scores -2.24 to -2.35 and reads
   nothing. Suffix codes (right-to-left) likewise: control true rule -1.55 at top; target best -2.51. Excluded.
2. Uniform two-digit tokens: with letters as separators between tokens, 20 of 33 digit runs are odd; excluded. With
   letters dropped (nulls inserted anywhere), the wavy sign inline, and each marked digit heading a code group of one
   or two digits, a dynamic program finds exactly 75 pairings in which every letter run is even; they differ only in
   the spans of the 16 code groups. With the wavy sign as a grid boundary, or with three-digit groups, none or
   millions. Pair IC of the resulting 228 tokens over 62 symbols is 0.020-0.023 against a shuffled null of
   0.018-0.020: weakly consistent with a heavily homophonic two-digit alphabet of the kind in Nevers keys no. 19-20
   (1588-89: two-digit letters with vowel homophones, figures for words).
3. Joint segmentation+key annealer: fails its own control (-1.88 vs true -1.55); discarded.
4. Readability at this size: profile-matched controls (228 tokens, 54-62 symbols, 16 code groups, 9 inline signs)
   have true-key scores of -1.67/-1.75, but 6 restarts x 200k iterations find only false optima at -1.84/-1.88
   (7-11% letters right). The target's best pairings score -1.84 to -1.97: the same false-optimum band. So far the
   solver, not the text, is the limit.

## Solve attempts on the two-digit design (`pairings.json`, `par.py`, `refine_words.py`)
Annealer: Italian 5-gram (fixed-weight interpolation of add-k tables, orders 5 to 1, Roman numerals and k/w/x/y/j
words stripped from the Nuntiaturberichte corpus), unigram chi-square penalty 0.3, moves: single reassignment,
symbol swap, letter-level swap, and a Gibbs resample of one symbol; windows never span a code group or the wavy sign.
Validated: it reads the prefix-rule controls at 20-37 symbols every time (99-100%), and 1 of 3 two-digit controls at
40 symbols / 215 tokens (98%).

| run | restarts x iters | matched control (true score) | control found | target best |
|---|---|---|---|---|
| 6 x 200k | | -1.67 / -1.75 | -1.84 / -1.88 (7-11% right) | -1.84 to -1.97 over 16 pairings |
| 20 x 400k | | -1.67 / -1.75 | -1.79 / -1.86 (14-16%) | -1.85 / -1.88 (pairings 0, 4) |
| 120 x 400k, 14 cores | | -1.67 | -1.80 (14%) | -1.84 (pairing 0) |
| + word-segmentation hill-climb (30,000-word list) | | | -1.83, fluent-looking junk, 10-14% | not run: no better on the control |
| symbol-cap penalty (vowels <= 8 symbols, consonants <= 3) | 12 x 300k | -1.67 / -1.75 | 11-15% | |
| 18 hapax symbols treated as code groups (44 letter symbols) | 120 x 400k | -1.70 / -1.74 | -1.83 (12%); **-1.70 (7%) on control 1, i.e. a wrong key outscores the true key** | -1.81 |

The target's best scores fall exactly in the band of the controls' false optima, and no restart's decrypt reads as
Italian; the recurrent fragments in the top target decrypts (sua santi-, -esiastate-, -ionessoreett-) are the language
model's own attractors and appear in the control junk too. Sukhotin vowel separation is at chance (27-67% token-weighted)
on the matched controls under this much homophony, so it cannot constrain the search.

## Verdict (2026-09-16): structure narrowed, not read
- Not a variable-length prefix or suffix figure code with null letters between tokens (control-validated scans, Italian
  and French). Not readable as one symbol per glyph (IC 0.127 for 483 digits).
- Consistent with the design of Birago's own circle: two-digit figures for letters with heavy vowel homophony, marked
  figures (bar, dots, cross) of one or two digits for names or words, the wavy sign as an inline word-sign, and the six
  letters as nulls placed anywhere. Exactly 75 pairings satisfy the even-run constraint; they share the same 228 letter
  tokens over 62 symbols (18 hapax) and differ only in the 16 code-group spans.
- At 228 tokens over 62 symbols the ciphertext-only annealer fails its own matched controls (best-of-120 restarts 0.13
  per window short of the true key, 14% letters right), and on one hapax-reduced control a wrong key outscores the true
  key (-1.70 vs -1.74, 7% right): the text is below the unicity distance of a 5-gram model at this homophony, so the
  target's negative says nothing about its content. Same regime as Moray (134 tokens / 32 symbols) and SP 53.
- What would read it: a second Birago letter in the same figure cipher (the other Saluzzo letters of late 1571 in
  fr. 3251 and the Nevers papers in fr. 3252-3253, 3974-3994 are the place to look), or the key itself in the Nevers
  cipher collections (BnF fr. 3995 has none this early), or a crib: the paragraph follows a passage about the King,
  Bellegarde and the Carmagnola cavalry, so the code groups likely include il Re, la Regina, Bellagarda, Carmagnola,
  Savoia; a crib-constrained anneal is the next cheap step once any code group is fixed.

## Last attempts (2026-09-16, later session)
- **Word-level objective.** A 30,000-word Italian list with Viterbi segmentation (`wordscore.py`) separates the true key
  from the annealer's false optima on every matched control (-2.6/-2.9 vs -3.0/-3.6 per letter), including the one where
  the 5-gram preferred a wrong key. But annealing under the combined score (`anneal2.py`, weights 1.0 and 0.3, seeded
  from the 20 best char-LM keys) still reaches only 3-30% letters right; at weight 1 the word score rewards runs of
  one-letter words. The objective ranks the truth first; the search does not find it.
- **Consensus.** Across the 120 restarts on a matched control not one symbol has a majority letter, so the optima share
  no partial truth to build on (`consensus.py`).
- **Sibling sweep of BnF fr. 3251.** All 118 remaining openings (views 88-207) fetched at 2400 px and screened with a
  line detector calibrated on the target page (`find_digits.py`; catches 4 of its 7 cipher lines). Every candidate with
  two or more flagged lines (views 99, 100, 107, 109, 156) is plain text on inspection: the letters of 22 September 1571,
  the Frascheta relation of 30 August 1571, a letter of 30 August 1571, and one of 15 June 1572. No second letter in the
  figure cipher exists in this volume; the 1572 letters are in the symbol cipher Tomokiyo reconstructed. The opening
  after the target (f. 120-121) is the notarial attestation of Marco Balbo's mission to Carmagnola, not a decipherment.
- The letters of 22 September (f. 98) and 30 August 1571 (f. 108) are in clear and give the vocabulary of the affair
  (Bellagarda, Carmagnola, Centurione's company, the frascheta, Valletta, Perosa, Melchion da Gattico): crib material if a
  code group is ever fixed.

**Final state: not solved.** Design identified and transcription corrected; the ciphertext-only attack is below the
unicity distance of the available models at this homophony, and no key, sibling or decipherment is online.
- **Structured homophony** (`structured.py`): if the key were a table in which a letter's homophones differ by a fixed
  offset (pair mod M, M = 19-33) or share a digit (units or tens digit with the other digit's half or parity, digit sum,
  digit difference), the 62 symbols collapse to about 20 and the problem is monoalphabetic. Every such collapse scores
  -2.29 to -2.63 per window against -2.00 unconstrained and -1.6 for readable Italian, and none reads. The 1571 key is
  not built on any of these simple patterns; its homophones are arbitrary, as in Nevers no. 19-20.
- **Slow annealing** (`slow.py`): 4,000,000 steps per restart, T 8 to 0.05, three seeds each on the 54-symbol control and on
  the target's best pairing. Control: -1.85 to -1.91 per window, 6-25% letters right (true key -1.67). Target: -1.91 to
  -1.97. Cooling rate is not the limit either.
- **Polyphonic single figures** (`poly.py`, `poly_control.py`): the alternative that the single-digit IC (0.127) allows,
  each figure standing for two or three letters as in Lucca 1644, with a marked figure as a doubled letter (16 marks
  against about 17 expected geminates in 480 letters of Italian), the wavy sign as a break and the six letters as nulls.
  Letter-to-figure assignment annealed under a trigram Viterbi decode, then 5-gram rescoring. Matched control (496
  letters, 10 figures, target's digit profile): three of three seeds return the same key, 9 of 10 figures right, -1.84
  trigram / -1.91 5-gram per letter, decode readable. Target: -2.07 to -2.28 per letter under every convention
  (letters as nulls or as clear letters; marks as doubling, as separate symbols or as plain figures; wavy sign as break
  or as symbol), keys differing between seeds, nothing readable. Excluded.
- **Syllabic two-digit alphabet** (`syll.py`): tokens as letters or CV syllables, as in Nevers no. 5 (1585). A matched
  control segments naturally into about 60 units for 228 tokens, the target's profile, so the design is plausible on
  its face. But the token-to-unit annealer (5-gram over the expanded string, 7 seeds x 400k) reads 0-5% of the control's
  units and falls into degenerate optima; the tool is not validated and its target output (-2.3 to -3.6) says nothing.
  A unit-level attack that passes its control is the open research problem that also stopped Vatican 5.
- **Nevers cipher of 1574** (BnF fr. 3315 f. 12-13, Gallica btv1b90600800 views 13-14, fetched): a symbol alphabet with
  symbol nulls and symbol doubles, plus a figure nomenclature 8-62 (Le Roy 8, La Royne 9, Le Roy de Pollongne 10, Le
  Roy Philippe 11, L'Empereur 12, Le Pape 13, Le Turc 14, Le Duc de Savoie 15, Madame de Savoie 16, ... Italie 37,
  Angleterre 38, Escosse 39, Flandres 40, Ambassadeur 41, Monsieur 42, Madame 43, Chancellier 44, Infanterie 45,
  France 46, Italiens 47, Espagnols 48, Allemans 49, Suisses 50, Lombardie 51, Gennes 52, Argent 59, Armee de mer 60,
  Huguenots 61, Piedmont 62). Not a figure cipher for letters, so it does not apply; its number list is at most a gloss to
  test on the target's marked code groups (15, 41, 43, 44, 12, 59 among them) once any reading fixes one.
