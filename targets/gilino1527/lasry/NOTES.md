# Gilino: working key, transcription and reading

Contribution by **George Lasry**, prepared with **Codex assistance**. This packet preserves the latest local edition, dated 7 October 2026, of the Italian diplomatic letter subscribed "Servo el Gilino", dated 15 September 1527 at Paredes. Gilino’s exact forename remains unestablished. The address leaf documented by the existing repository edition identifies the recipient as Francesco II Sforza, Duke of Milan, at Cremona.

The [British Library catalogue](https://searcharchives.bl.uk/catalog/040-001103269) identifies Cotton MS Vespasian C IV, ff. 214r–218v. The [DECODE record R8572](https://de-crypt.org/decrypt-web/RecordsView/8572) identifies the nine supplied photographs. The working reading is Italian with occasional Latin; inherited "Latin", "English?", and "Serno" labels are not adopted as established manuscript readings.

## Files and scope

- `key.json` and `key.txt`: recovered working assignments, counts, uncertainty and evidence notes; these are hypotheses, not a surviving archival key.
- `transcription.txt`: assembled cipher-token transcription in manuscript order.
- `alignment.tsv`: every token and its literal value, retaining presumed nulls and doubtful glyphs.
- `literal_decode.txt`: group-by-group reading with presumed nulls omitted.
- `plaintext_reading.txt`: punctuated Italian reader edition, with clear manuscript passages distinguished and conjectures retained.
- `source.json`: public source links, original and bundled artifact SHA-256 hashes, and hashes recorded for the unbundled photographs and input transcriptions.
- `counts.json` and `verify.py`: reproducible counts and consistency checks.

The nine photographed faces are ordered **P1/214r, P2/214v, P7/215r, P3/215v, P5/216r, P4/216v, P6/217r, P8/217v, P9/218r**. No photograph of 218v is supplied. Scans, glyph atlas, large HTML/ZIP deliverables and image-audit working files are not bundled.

## Recovery and attribution

The documented method used repeated Italian phrases, group frequencies, positional patterns, and cross-occurrence checking. Stable cribs exposed ordered consonant–vowel rows; single letters, homophones, presumed nulls and a small nomenclator completed the working key. Source-image checks corrected the transcription, including overlapping annotations. The supplied older transcription covered P1–P5; Codex transcribed P6–P9 and assisted the subsequent audit of all nine images.

The source account explicitly describes crib and structural recovery rather than simulated annealing. This contribution does not claim that cyphersolver or CrypTool recovered the key, and does not attribute the work to a specific Codex model. No independent historical key or complete plaintext was found in the prior bounded research. This submission adds no new cryptanalysis.

## Counts and remaining limits

There are **161 cipher lines and 3,107 transcribed tokens**: **3,105 cipher tokens plus two inline cleartext abbreviations**, `vva` and `xha`. The **138 canonical transcription labels comprise 136 cipher labels and two cleartext labels**. There are 20 doubtful-glyph occurrences, 12 presumed-null groups, five tentative-value groups and one possible-separator group. Uncertainty categories can overlap. Full assignment coverage measures neither decipherment accuracy nor the completeness of the edited plaintext.

The tentative mappings are `b50=gu?`, `g65=qu?`, `b55=imperatore?`, `b56=sua maesta?` and `h26=cosa?`; `ooo=[separator?]` remains qualified. Q+ and H+ have residual glyph/allography problems. The P3 terminal sequence, anomalous words and connectives, P9's `abbassi`, and an overwritten final sign remain unresolved. Editorial interpretations and already-clear passages must not be counted as independently recovered cipher wording.

## Relationship to the supplied PDF

The supplied `gilino.pdf` is a presentation reference: manuscript beside the reading, bold decipherment and regular cleartext. Its content reflects an earlier state. This packet retains later source-image corrections: `g5000` is a presumed null, replacing the obsolete `g2000=A?`; `g70=ru` is independently supported by RUINA; `x26=quanto` has multiple supporting contexts. The final reading also retains corrected `intercette`, `sicure`, `se conservi a`, removal of a spurious I/descender token, and `No[n]`. The PDF's obsolete unknown `b72?` label is not reintroduced; the final-sign uncertainty remains explicit. Some wording in the earlier method narrative was likewise superseded by the final key and completion audit.

## Verification

Run `python verify.py` from this directory with Python 3. The standard-library script verifies transcription/alignment identity, sequential line IDs and photo order, every token's fixed-key value, key frequencies, doubtful-glyph counts, `counts.json`, and the six bundled core-file hashes. It does not evaluate historical correctness or verify unbundled image hashes. All source originals were preserved; only portable copies were normalized for this packet.
