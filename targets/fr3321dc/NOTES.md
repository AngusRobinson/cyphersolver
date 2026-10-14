# Signed DC → Not established, 20 May; year not established, BnF Français 3321

Status: no write-up of our own (result by George Lasry, presented on docs/fr3321dc.html and summarised on docs/lasry-bnf.html)

Hub page: [George Lasry's BnF cipher research](https://dbourdeau.github.io/cyphersolver/lasry-bnf.html).

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: Transcribed; Deciphered
- Ciphertext-only: No
- Sender: Signed DC
- Recipient: Not established
- Date: 20 May; year not established
- Key: 32 symbols, 25 letter signs, 5 in nomenclature, 1 null ?, 1 unidentified
- Ciphertext: 49 elements, 46 identified (93.9%); 2 ?, 1 unidentified
- Contents: A political letter says the union can impose its terms and describes an escape from execution, drowning and plunder; several named opponents remain uncertain.
- Method category (our classification): key recovered based on adjacent plaintext; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 3321
Contents: A political letter says the union can impose its terms and describes an escape from execution,
drowning and plunder; several named opponents remain uncertain.
Transcribed; Deciphered
Ciphertext-only: No
Sender: Signed DC
Recipient: Not established
Year: 20 May; year not established
Key: 32 symbols, 25 letter signs, 5 in nomenclature, 1 null ?, 1 unidentified
Ciphertext: 49 elements, 46 identified (93.9%); 2 ?, 1 unidentified
Interlinear plaintext: Interlinear plaintext on the same page, f103r. ·
Gallica f103r

Excerpt and Translation
Excerpt
f103r, first four lines
Les affaires sont en tel termes qu'infalliblement la Ruyne de Espernon s'en ensuivra, ou de cest estat.
Car l'union est si forte qu'elle peult mieux donner la loy que la recepvoir. Demain la req[ueste] s'en
doibt partir, vous en aurez Incontinent la coppie Comme on vous envoye du reste.
Translation
Affairs have reached such a point that Épernon’s ruin, or the ruin of this state, will inevitably follow. The union
is so strong that it can dictate the law rather than receive it. The petition is to be sent tomorrow; you will
immediately receive a copy, as the other material is being sent to you.
```

## Links

- <https://gallica.bnf.fr/ark:/12148/btv1b9060212v/f105.item>
- <https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060212v/f105/full/1600,/0/default.jpg> — image checked in the spot-check

## Images

- `lasry_p080_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p081_2.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060212v/f105/full/1600,/0/default.jpg
- Folio matches the report: yes; cipher present: yes
- What we checked: f103r l.2 after "Car": l u n i o n [est] s i f o r t (14 signs incl. est code) = "lunion est si fort"; also Espernon code after "Ruyne de"; matches excerpt and interlinear
- Verdict: **confirmed** (method key recovered based on adjacent plaintext, extent partial). The check is a sample, not a re-solution.
- Notes: Only 49 cipher elements; 93.9% identified (<95%). Signed with monogram, "xxme may". Ligue context (union vs Epernon) suggests 1588.
