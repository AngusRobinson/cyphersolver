# DECODE 4282: Chifferklaver låda II 113

Status: read with scattered gaps; key recovered from ciphertext-only; contributed solution.
Key state: partial; three word signs remain unidentified.
Solved by George Lasry, using CTTS transcription and CTTS's built-in homophonic solver. GPT-6 Astra assisted with refinement of the key, transcription and reading.
Contribution prepared: 14 October 2026.

This target records Lasry's solution and the subsequent assisted review. It is not a claim that an LLM independently broke the cipher. The requested work here is a contribution package, not a fresh attack or an exhaustive historical investigation.

## Source and scope

The source is DECODE record 4282, Chifferklaver_låda_II_113, held by Riksarkivet, The National Archives of Sweden, Stockholm. The live catalogue was checked on 14 October 2026. It gives the broad date range 1600-1699 and does not identify the sender or recipient. The document's exact date, author and addressee remain unknown; the catalogue range is not a newly established date.

The record has three attachments: wrapper I25745, first text page I25746 and second text page I25747. The contribution covers the selected two text-page views in full: 25 manuscript lines on the first and seven on the second. It does not claim to transcribe the partially visible right-hand/facing page in the raw attachment. That area is outside these views and outside the token counts.

The source record still labelled the item "Non-decrypted" and "Inline Cleartext: No" when consulted. Those catalogue labels do not establish the absence of an earlier solution. Four cleartext passages are visible in the text, and the first page also has the pencil heading "Chiffer-skrift." ("Cipher writing."). Public metadata and source hashes are recorded in [source.json](source.json). Native source-page images are not included in the contribution.

## Method, credit and conditions

Lasry explicitly confirmed the sequence: he transcribed the manuscript in CTTS, recovered the initial solution with CTTS's built-in homophonic solver, and then used GPT-6 Astra to improve and finalize the key and reading. The initial solver recovery was ciphertext-only. The original cleartext passages were brought into the subsequent review and helped refine and complete the continuous reading.

The primary method is therefore **key recovered from ciphertext-only**, followed by contextual and visual refinement using the manuscript, including its cleartext. It is neither a solution obtained by applying a previously known key nor an independent LLM-only break. Credit for the solution belongs to George Lasry.

The current CTTS key bears the origin line "Cryptanalysis by CTTS". The local working material also contains AI detection, line and embedding files and visual-recognition model metadata. These are transcription aids, not logs of the homophonic solver. A model catalogue is not evidence that every listed model was tried.

Detailed solver configuration, search budget, restart count, random seeds, scoring model, run times and intermediate solver traces are not attested in the supplied records and are unknown. The precise initial prompt and other experimental conditions are likewise unknown unless explicitly described above. Do not reconstruct them from the final result.

## Earlier repository attempt and prior-reading evidence

The existing [Riksarkivet group notes](../riksarkivet1628/NOTES.md), dated 21 September 2026, record an earlier, unsuccessful attempt on R4282. Those notes report substitution and homophonic annealing both with and without the written word divisions, producing no acceptable Latin, and suggest that the transcription may have merged signs. They also identify clear words as possible next cribs. This is **prior repository work**, not an attempt carried out as part of the present Lasry/CTTS and GPT-6 Astra contribution.

The September notes' broad group heading must not be used to date this letter or identify its correspondents. The group included unrelated records. Nor should their negative search be represented as a new controlled result: the contribution did not rerun it or establish a matched control. The earlier notes remain unchanged.

No known earlier decipherment was supplied or identified in the materials reviewed for this contribution. No exhaustive literature, archive-key or novelty search was performed here. Thus the notes do not claim that this is the first decipherment ever made, and a catalogue's "Non-decrypted" label is not used as proof of novelty.

## Documented refinement sequence

1. **CTTS transcription and initial recovery.** Lasry produced the sign transcription and used the built-in homophonic solver to obtain the initial reading. The user confirms this step; it is not inferred solely from the key header.
2. **Contextual review of the current key and exports.** Repeated Latin contexts supported the QU sign, X and other letter values, and revealed that several apparent letters were nulls. The roles of individual sign classes were checked against multiple occurrences rather than assigning plaintext to isolated words without qualification.
3. **Visual classification and transcription checks.** Manuscript crops were checked where the text exposed possible merged signs or incorrect classifications, notably D/O, ordinary I-like/null forms versus the QU sign, and individual N and I occurrences. Corrections were incorporated into CTTS by the working session and the resulting exports were reviewed again.
4. **Separators and continuous reading.** Added word separators and punctuation made some earlier apparent contradictions disappear. For example, the apparent continuous reading AMBITERAT divided as AMBIT ... . ATQUI ..., with nulls between the words.
5. **Cleartext reintegration.** The four original cleartext passages were read from the images and placed back in their manuscript positions. This completed constructions that the cipher-only export could not supply.
6. **Edition and translation.** The entire selected two-page text was checked in aligned Latin-English units. Unresolved word signs and contextual restorations were kept visible. Source metadata and the distinction between catalogue dating and an established document date were corrected in the accompanying report.
7. **Contribution preparation.** Current CTTS files, deterministic token-level decoding, measurements, the aligned reading and the editorial qualifications are packaged here. This step does not add a new solve.

An earlier saved working key provides concrete evidence of superseded values. Sign 31 had been grouped under O and is now D. Signs 15, 20, 21, 26, 33 and 34 had letter readings and are now nulls. Signs 37, 38 and 39 had L/P/C readings and are now kept as distinct unresolved word signs. These were revised working assignments, not documented separate failed cryptanalytic attacks.

Both surviving working and final keys already contain QU and X, so those two files alone cannot establish the exact time at which those values were first found. There is no complete timestamped log of every hypothesis. No additional solver runs, searches or controls should be inferred from this narrative.

## Cipher and reproducible material

The current inventory has 39 sign classes: 24 letter signs, one QU sign, 11 null signs and three unidentified word signs. Several letters have homophones. The three unresolved signs occur five times in total: 37 twice, 38 twice and 39 once. They are not interchangeable placeholders.

The package retains [key.txt](key.txt), the CTTS [transcription.txt](transcription.txt), [literal_decryption.txt](literal_decryption.txt), the position files and sign crops. [key.json](key.json), [cipher_tokens.txt](cipher_tokens.txt), [decode.py](decode.py) and [token_readings.tsv](token_readings.tsv) support reproduction and measurement. [reading.json](reading.json), [readable.txt](readable.txt), [translation.txt](translation.txt) and [editorial_notes.md](editorial_notes.md) distinguish the continuous edition from the literal export.

The sign counts were independently remeasured from the current CTTS numeric tokens, excluding punctuation, inserted word separators and original cleartext:

| View | All cipher tokens | Null tokens | Known non-null tokens | Unidentified word tokens |
|---|---:|---:|---:|---:|
| Text page 1, 25 lines | 856 | 217 | 635 | 4 |
| Text page 2, 7 lines | 228 | 62 | 165 | 1 |
| Total | 1,084 | 279 | 800 | 5 |

Assigned values account for 800 of 805 non-null tokens (99.38%), or 1,079 of 1,084 tokens when recognized nulls are included (99.54%). These are **assignment fractions, not demonstrated transcription accuracy**.

For a conservative coherent-reading floor, exclude all 27 non-null sign occurrences in the five editorially restored words, even where some letters are already correct, as well as the five open word-sign occurrences. This leaves 773 of 805 non-null tokens, **96.02%**. The excluded word spans contain 6, 4, 7, 8 and 2 non-null tokens respectively. This meets the repository's 95% read bar while retaining the scattered uncertainties explicitly. Both selected text pages are covered; the key remains partial. The floor is a conservative coverage measure, not a statistical test or proof that every retained glyph is correctly classified.

## Cleartext and editorial reading

The four cleartext insertions are original manuscript writing, **not recovered ciphertext**:

- Page 1, line 10, after "vigore": "et qualis sit eius futurus status dubitatur".
- Page 1, line 20, between "occasionem" and "maneat": "sed tamen ut res".
- Page 1, line 24, before "maximas": "facimus magnas admodum expensas". The damaged ending of "facimus" is supplied from the visible word and its construction.
- Page 2, opening, before "et grandis pecunia": "Mittatur nobis responsum".

These joins matter. "Sed tamen ut res" continues into "maneat in vestro arbitrio"; "expensas" supplies the noun understood with "maximas in coronatione facturi"; and "Mittatur nobis responsum" governs the ensuing request for money. Original cleartext must not be counted as solver output.

Five current export readings remain editorially restored:

| Literal export | Contextual reading | Qualification |
|---|---|---|
| SIMPIR | [semper] | Two vowel readings differ. |
| A_GLO | [Anglo] | N is supplied where the current class is null. |
| PRSRSVS | [prorsus] | The first S after PR is read as O. |
| PRSMITAT | [promittat] | S is read as O and a second T is supplied in the normalized spelling. |
| IT | [et] | I is read as E. |

These are contextual readings, not additional verified key values. Ordinary u/v, orthographic, punctuation and word-division normalization is also distinguished from literal decoding. No complete per-token H/C/M/I grading ledger is attested; the five bracketed restorations are inferred readings, not values read from a surviving primary key.

The names behind 37, 38 and 39 have not been guessed. The repeated sign 38 occupies the position of the person urged to marry an Englishman, but grammar does not identify that person. Pronouns and implicit subjects remain correspondingly cautious in translation. In the final clause, the singular person who doubts and acts is left unidentified; the plural "their" refers to the two dukes.

## Remaining gaps

- Sign 37, two occurrences on text page 1 - blocker: open-codes; the source forms and both contexts were examined, but no lexical or personal value is established.
- Sign 38, two occurrences on text page 1 - blocker: open-codes; its marriage-related contexts were examined, but a personal name or title has not been recovered.
- Sign 39, one occurrence on text page 2 after "pro" - blocker: open-codes; its distinct source form and context were examined, but its value remains unknown.
- The five word readings listed above remain contextual restorations. Their literal forms are preserved, their sign spans are excluded from the conservative coherence floor, and they are not promoted to verified key readings.
- Exact date, sender, recipient and the implicit personal referents remain unidentified. The broad catalogue date is retained without a historical identification inferred from the contents.
- The partially visible facing-page area in the raw attachment is outside the defined two-view contribution, not an unreported completed decipherment.

The three open signs were considered during the review; they are not unexamined omissions. Further source or key work may resolve them, but this contribution does not claim that such work has been exhausted or that the gaps are intrinsically insoluble.

## Escalation

- [ ] siblings: no fresh neighbouring-record or volume-wide sweep was performed for this contribution. The same-record wrapper and two text-page views were inspected. The earlier September group survey is separately attributed above.
- [x] clear-pages: the visible cleartext within the selected text views was examined and integrated, and the wrapper/text-page scope was checked. No separate complete clear decipherment was identified in these materials; this is not a claim about every neighbouring record.
- [ ] known-keys: no external historical-key sweep or application of the R4284 key-test leaf was performed in this contribution. Do not import the September group's tests as new tests of this solution.
- [ ] print: no exhaustive search of printed editions, calendars or prior decipherments was performed. No priority claim rests on such a search.
- [x] key-rebuild: Lasry's reported CTTS ciphertext-only recovery was followed by contextual and visual refinement of sign values and classifications, including nulls and the D/O distinction. The unresolved word signs remain open.
- [x] retry: revised CTTS exports were checked repeatedly against contexts and selected manuscript crops. The complete two-view reading and translation were reviewed; the five remaining editorial restorations are explicitly retained. No new independent LLM solver run is claimed.
- [x] statistical validation (14 October 2026): `python docs/_validate.py decode4282 --write` returned **pass** on the literal aligned values. Latin score −2.170 per letter; 200 random keys mean −4.847 (z=9.5); six shuffled-ciphertext refits best −3.479 (mean −3.506). The random-start real-text annealer reached −2.170. The test fixes null positions and does not validate the unknown codes or contextual restorations. See profile.json validation and validation.tsv.

The unchecked items record work not performed; they are not disguised as completed or inapplicable. The present task is to submit the contributed solution with its limitations, not to undertake a new archival solving campaign or overwrite the prior group history. The required site build and submission checks are recorded with the pull request.
