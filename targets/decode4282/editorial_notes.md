# Reading conventions

Solved by George Lasry. CTTS (CrypTool Transcriber and Solver) was used for
transcription and its built-in homophonic solver recovered the key. GPT-6 Astra
assisted in improving and finalizing the key and decryption.

The original CTTS key and literal decryption are preserved verbatim. The numbered
labels are transcription identifiers, not numbers written on the manuscript.
Three different word signs, (37), (38), and (39), remain unresolved at five positions.
They must not be merged just because the original CTTS export used one placeholder.

The readable edition regularizes punctuation, spacing and u/v. It also regularizes
SUPLICAT to supplicat, NUNQUAM to numquam, PRE to prae, PRETERMISSURI to
praetermissuri, and CAUSE to causae. These changes are not additional cipher mappings.

Five contextual restorations are bracketed in the Latin reading:

| Location | Literal cipher output | Editorial reading | Grade |
|---|---|---|---|
| p1 line12 | SIMPIR | semper | I |
| p1 line12 | AGLO (with an intervening null) | Anglo | I |
| p1 line13 | PRSRSVS | prorsus | I |
| p1 line16 | PRSMITAT | promittat | I |
| p2 line4 | IT | et | I |

No new letter value is claimed from these contextual corrections. In the last
sentence, the subject of diffidit/conficiat is an unidentified singular person;
eorum refers to the two dukes. The translation preserves this distinction.

Four original cleartext spans remain in their manuscript positions in reading.json,
in regular type between bold deciphered spans. They are original prose, not a
historical decipherment of the cipher. They are omitted from cipher token counts.

Assignment coverage is not plaintext accuracy. Of805 non-null tokens,800 have a
key value. A conservative coherence floor excludes all27 tokens within the five
editorially restored words as well as the five open codes:773/805 (96.02%). It is
a coverage lower bound, not a probabilistic accuracy estimate.
