# "El Gilino" to Francesco II Sforza, Paredes de Nava, 15 September 1527 (BL Cotton MS Vespasian C IV ff. 214-218, DECODE R8572)

Status: read (9 Oct 2026). Deciphered to 96.1% (2,872 of 2,989 significant tokens) with the Sforza key DECODE R5258, found by scanning the Milan key sheets on DECODE. George Lasry had reconstructed the same key from the ciphertext by 7 Oct 2026 (Codex-assisted; contributed 14 Oct 2026, `lasry/`). Written up as docs/gilino1527.html. Until 14 Oct 2026 this letter sat in `targets/superscript/` with Ghinucci R8613 (now `targets/ghinucci1527/`), a different cipher.

## The letter

- Cotton MS Vespasian C IV ff.214-218 (old f.199 ff.), DECODE R8572 ("Non-decrypted", city "Daredos" = Paredes [de Nava]).
  Italian, nine text pages and an address leaf. Bound among Wolsey's papers next to the Worcester letters, which
  is how it was first grouped with them; its cipher is unrelated (see `targets/ghinucci1527/`).
- Images: DECODE full size with the cookie, in the old folder `img/` (git-ignored), not copied here.

## 9 Oct 2026: Gilino (R8572) transcribed; key search in the Sforza key files

- Sub-agent transcription `r8572_tokens.txt` (~3,157 tokens, 198 distinct; 162 cipher lines on 9 pages) and the
  clear passages `r8572_clear.txt`. Address leaf (P10): "Illmo et Exmo Dno Dno Mediolani Duci ... Cremone": the
  letter is to **Francesco II Sforza, Duke of Milan, at Cremona**; "el Gilino" is a Sforza agent at the imperial
  court; dated Paredes [de Nava] 15 Sept 1527. The clear text names Gattinara, Bourbon, the French and English
  ambassadors, Ludovico Catti (Ferrara), the bishop of Tarbes (who gave him copies of intercepted letters),
  Caiazzo, Monteleone, Marco Pio. No decipherment on the MS.
- System: barred base glyphs (6, B, D, d, o, H, A, P, R) with two-digit numbers 20-80, plus ~40 unnumbered signs.
  A one-token-one-letter homophonic anneal (Italian 'it-cinquecento' 4-gram, frequency penalty) gave no Italian
  (-2.9/char, restarts disagree): the numbered groups are syllables/words, not single letters.
- Key search: DECODE holds ~377 Sforza key records (ASMi Carteggio Sforzesco cart. 1591/1597/1598, PDFs). R5256
  (cart. 1591 no. 22) is the same family (barred B/D with numbers for names: Papa B20, Imperatore D20, Gran
  Cancelliere D22, Antonio Leyva D26, Duca di Milano B28 ...), 1520s, but its syllable table differs. A full scan of
  the key files for Gilino's table is running.
- **Key found: DECODE R5258** (ASMi Carteggio Sforzesco cart. 1591 no. 24, docket "Cum equite Bilie / extracta ex
  cifris"), by a sub-agent scanning the contact sheets of cart. 1591 (R5235-R5300) and R5301-R5309 (cart. 1597/1598
  R5310-R5611 not examined after the match). Its barred "G" = Gilino's "6"; rows B.31-50 ba..gu, B.51-55 fa..fu,
  D.51-65 la..nu, 6.56-80 pa..tu, o.33-47 va..zu; words H.26 cosa, H.27 che, H.28 come, R.23 con, R.28 ancora,
  D.40 sara; letters and nulls (a++ etc.) also on the sheet. First application gives Italian throughout ("firmato
  da molti", "le galere di Napoli", "cento milla ducati del cambio", "la morte di Borbone", "dalli oratori
  confederati", "nuncio in credenza", "camerero di Sua Santita"). Notes: `key_R5258.md`, first decoder
  `dec.py`, `final.py`, output `r8572_test_decrypt.txt`. Key renders in `img/` (git-ignored).
- Name question: the key is "with the Cavaliere Bilia", the letter is signed "Servo el Gilino" (checked on the
  image); R5287 (cart. 1591 no. 53, 7 Nov 1525) lists "Cavallero billia" and "Ghilino" as two people. Open.
- Other Sforza keys for the same men: R5237 (Bilia, plain numeric alphabet), R5248 ("Cum Camillo Gilino in
  Fiandra", digraph-to-digit key), R5236 and R5287 (nomenclators naming Gilino).

## 9 Oct 2026: Gilino R8572 deciphered with R5258

- Sub-agent reading `reading_r8572.txt` (decoder `decode_r8572.py`, `build_reading.py`; key
  `key_r8572.tsv`, 183 rows with source sheet/context; 24 transcription corrections in
  `transcription_corrections.txt`; English summary `summary_r8572.txt`). Measure: 3,111 cipher tokens,
  122 nulls, 2,989 significant, 9 unread, ~108 in doubtful words -> 2,872 read as sense = 96.1%; it-cinquecento
  LM -1.52/char on the word-divided text.
- Folio order differs from DECODE image order: P1 > P2 > P7 > P3 > P5 > P4 > P6 > P8 > P9 (ff.214r-218r).
- Content: Gattinara out of favour over two intercepted letters to the Viceroy of Naples about relieving Genoa (the
  confessor and secretary Lalemand his enemies); the Duke should have "the Bilia" keep in with Gattinara now that
  Bourbon is dead; the new Portuguese ambassador and a letter in the Pope's own hand; two papal briefs; the
  Abbatino's mission and Gregorio Casale; Paolo Luzzasco to go over to the Emperor with 300 light horse; the French
  ambassadors insist the Duke keep Milan; the Emperor said to revoke the Pope's liberation after the Lombard news;
  Andrea da Burgo "pro opprimenda Italia"; investiture of Milan sent to the Infante with 100,000 ducats.
- Bilia vs Gilino: the cipher names Bilia in the third person, and R5287's codes for Bilia (A28) and Ghilino (A29)
  do not occur; R5258 is a key drawn from the Bilia correspondence that Gilino also used.
- Prior solution: none found (no decipherment on the MS, not in L&P); the key was in the Milan archive, filed under
  another correspondent, not previously tied to this letter.

## Remaining gaps

- Gilino R8572: 9 unread tokens (Bp, "q o", a small o, "b o" in a struck group, o.29 xp b+) and ~108 tokens in 45 doubtful words, listed in reading_r8572.txt - blocker: illegible; the writer's own a/o and i/e confusions and glyphs that the image does not separate (struck groups, cramped superscripts); no second copy of the letter exists.

## Escalation

- [x] siblings: the DECODE neighbours of R8572 opened by API (R8566-R8579): all are Lee/Poyntz/Worcester despatches in the English letter cipher, none in this key.
- [x] clear-pages: R8572's only extra page is the address leaf (P10), which named the recipient.
- [x] known-keys: DECODE Sforza key files (ASMi cart. 1591 R5235-R5309) scanned, R5258 fits; R5256, R5237, R5248, R5287 checked and do not. George Lasry's independently recovered key (lasry/key.json) agrees with R5258 on 101 of 106 shared numbered signs.
- [x] print: not in L&P iv; no decipherment on the MS.
- [x] key-rebuild: R5258 extended from context (key_r8572.tsv).
- [x] retry: unread tokens re-checked on crops by the transcribing sub-agent (24 corrections).

## DECODE queue

- R8572: author "Gilino" (sign. "Servo el Gilino"), recipient Francesco II Sforza, Duke of Milan, at Cremona (address
  leaf P10); origin Paredes [de Nava] (not "Daredos"); language Italian; key = DECODE R5258 (ASMi Carteggio
  Sforzesco cart. 1591 no. 24); image order vs folio order as above; reading in `reading_r8572.txt`.
- R5258: link to R8572 as the key that reads it (docket "Cum equite Bilie / extracta ex cifris").

## 14 October 2026: George Lasry’s Gilino edition contributed

Contributed by George Lasry. The separate edition in `lasry/` preserves his reconstructed key, nine-page transcription, literal alignment and Italian reading with original cleartext inserted. Its dated research record (7 October 2026) describes Italian crib testing, repeated patterns and syllabary structure with Codex assistance, without an archival key. Do not attribute a CTTS homophonic-solver run to this contribution: none is documented in its records. The existing project work with R5258 and the Ghinucci material remain unchanged.

The contribution adds 161 cipher lines, 3,105 cipher occurrences and two original cleartext abbreviations, with 136 cipher labels. These are an alternative transcription of the same nine text pages, not additional pages or tokens to add to the earlier totals. Every aligned assignment reproduces from its key; this does not make tentative values or anomalous words secure. The supplied PDF is an older presentation of this edition; subsequent corrections in the accompanying files are retained.

The headline 96.1% and existing statistical test continue to describe the earlier project transcription. No combined or replacement accuracy is claimed. The current page now includes the full contributed Italian reading and its key, with technical evidence and disagreements retained in the contribution directory.

Two explanatory examples on the page were corrected to its already-existing working key: B.51–54 = fa…fo, with B.55/B.56 title codes; D.40 = i in this letter. They do not alter either key table.

## 14 Oct 2026: split from the combined 'superscript' target

George Lasry asked whether the Ghinucci material and his Gilino work were "about the same key". They are not:
the old page put the two letters together only because both use superscript numbers. The Gilino files moved
here from `targets/superscript/gilino/` (`gilino/lasry/` became `lasry/`, untouched, so its hashes still verify),
with `r8572_tokens.txt` and `r8572_clear.txt`; script paths updated (decode_r8572.py output unchanged).
`mk_validation.py`/`validation.tsv` rebuilt for R8572 alone (it-cinquecento).

Same key, two routes: on the numbered signs both editions label (B., D., d., G/6., o., A., H., R., P., x.),
George Lasry's recovered values agree with R5258 on 101 of 106 (nulls and tentative marks normalised). The
five others: H.28 (R5258 *come*, his *et*), R.22 (*e*; his null), R.28 (*ancora*; his null), x.22 (*pero*; his
null), 6.65 (a null here; his tentative *qu?*).
