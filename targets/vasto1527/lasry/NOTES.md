# Ranzo correspondence: George Lasry’s contributed working key

Contributed by **George Lasry**, based on **Norbert Biermann’s transcription (2021)**. The decipherment was achieved in collaboration between **Claude Opus 5.5 and GPT-6 Astra**, as attributed by Lasry. This packet preserves the Codex consolidation of 6 October 2026; it does not substitute Rosson’s or a newer Claude key.

## Scope and method

Five letters, 6,428 cipher occurrences, supplied as `Ranzo transcript.docx`. Shelfmarks and all existing clear passages are preserved in `transcription.json`. Recovery combined Italian cribs, repeated contexts, code-family structure, and testing proposed readings throughout the five letters. An early assumption of a purely alphabetically ordered vocabulary was not adequate; spelling signs, stems, syllables, words and phrases occur together. The research also checked selected entries of the historical “Aditione nel zifra” at Français 3022 f. 50. That limited historical key material is acknowledged; this is not a claim that every mapping was established without a historical aid. Original manuscript glyphs were checked selectively, not re-transcribed in full during this submission.

The documented stages included an early 62-entry table, comparison with an approximately 230-entry working key, repeated crib batches and cross-occurrence checks, a 74-query search that found no matching plaintext, and consolidation with the other model’s proposals. Proposed readings with question marks were explicitly retained at Lasry’s request. This publication performs no new cryptanalysis and claims no solver-based accuracy test.

## Other solution and chronology

Paolo Rosson independently obtained a contemporaneous solution using Claude. [Satoshi Tomokiyo’s Cryptiana account](https://cryptiana.web.fc2.com/code/ranzo.htm), dated 6 October 2026, records receiving Lasry’s report only a few hours after Rosson’s email and presents Rosson’s solution. [Rosson’s publication](https://pangoleen.github.io/cipher-readings/centurione-1528.html) used Daniel Bourdeau’s transcription. The present contribution uses Norbert Biermann’s transcription. Independence is Lasry’s account; the public chronology supports contemporaneous reports, not a claim to priority. The original project edition and Rosson-based measurements remain separate.

## Counts and limits

The 871 observed key entries assign a proposed meaning to 5,967 of 6,221 non-null occurrences (95.9% assignment coverage). This includes 381 tentative mappings, used 841 times. The assumed null rule removes 207 occurrences numbered 1–5; 254 other occurrences remain unassigned. Neither that coverage nor the absence of a question mark establishes plaintext accuracy. Some mappings do not fit every occurrence. For example t16=tal works in several contexts but needs checking in “le tale lettere”; a171=ambasciadori? does not explain the spelling contexts. These are preserved as unresolved limitations, not silently corrected during publication.

## Excerpts and visual key

`excerpts.json` contains two continuous passages, each punctuated into three sentences, with exact source-token boundaries, literal key output, joined Italian and a full English translation. They concern a compact cipher and preparation of alum water for secret writing. No unresolved cipher token is omitted within those selections; tentative values remain marked. Word division, accents and punctuation are editorial. The full visual key is linked from the write-up and preserves every source mapping and question mark.

## Verification

Run `python verify.py`. It checks source-token counts, key frequencies, every line-aligned decipherment, selected-token boundaries and all packaged hashes. It verifies reproducibility, not historical correctness. Original inputs and Claude-owned files were not modified.
