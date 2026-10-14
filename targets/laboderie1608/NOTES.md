# La Boderie → Pierre Jeannin, 7 June1608, BnF Français 3516 — La Boderie, f59r–60v

Status: no write-up of our own (result by George Lasry, presented on docs/laboderie1608.html and summarised on docs/lasry-bnf.html)

Hub page: [George Lasry's BnF cipher research](https://dbourdeau.github.io/cyphersolver/lasry-bnf.html).

## Source

This result is George Lasry's, obtained with ChatGPT Astra 6 and Anthropic Opus 5.5 and reported in "BnF cipher research" (10 October 2026), which he sent to Daniel Bourdeau on 13 October 2026 for publication here. The transcription, the key and the reading are his. This repository only spot-checked one sample against the Gallica image (below); it did not re-solve the cipher.

## His metadata

- Report status: 4/4 pages transcribed; 3/4 cipher pages deciphered; 1 more in part
- Ciphertext-only: No
- Sender: La Boderie
- Recipient: Pierre Jeannin
- Date: 7 June1608
- Key: 112 symbols:57 letter signs,53 word or syllable codes,2 controls.
- Ciphertext: 1023 elements,923 identified (90.2%).
- Contents: A report from England on negotiations in the Low Countries, expressing concern about placing too much hope in one course of action.
- Method category (our classification): key recovered based on adjacent plaintext; extent: partial

## His entry, as sent (excerpts and translations)

Quoted from the report; line breaks as extracted from the PDF.

```text
Français 3516 — La Boderie, f59r–60v
Contents: A report from England on negotiations in the Low Countries, expressing concern about placing too
much hope in one course of action.
4/4 pages transcribed; 3/4 cipher pages deciphered; 1 more in part
Ciphertext-only: No
Sender: La Boderie
Recipient: Pierre Jeannin
Year: 7 June1608
Key: 112 symbols:57 letter signs,53 word or syllable codes,2 controls.
Ciphertext: 1023 elements,923 identified (90.2%).
Interlinear plaintext: Historical interlinear plaintext on ff59r–60v.
Plaintext elsewhere: Corresponding published letter in Jeannin (1875), pp.383–384. · Jeannin (1875)

Excerpt and Translation
Excerpt
f59v, four full cipher lines
assez mal fondees, de sorte que tant s’en faut que je me promette rien de bien de ce commerage.
J’ai peur qu’il ne produise que du mespris de part et d’autre, et de part et d’autre il semble que
on y chemine que par maniere d’acquit.
Translation
Quite ill-founded, so that I am far from expecting any good from this godparent relationship. I fear that it will
produce only contempt on both sides, and on both sides it seems that people are merely going through the
motions.
```

## Links

- <https://archive.org/details/negociationsdiplomatiquesetpoli/page/383/mode/1up>
- <https://gallica.bnf.fr/ark:/12148/btv1b9059630p/f103.item> — Fr. 3516 f59v, image 103 (the report links the printed edition on archive.org)
- <https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9059630p/f103/pct:20,3,80,40/1800,/0/default.jpg> — image checked in the spot-check

## Images

- `lasry_p108_1.png`: George Lasry's image from the report (credit: George Lasry, BnF cipher research; manuscript © BnF via Gallica).
- Further images in the report, not copied here: p109_2.png.

## Spot-check (13 Oct 2026)

- Batch B. Image checked: https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9059630p/f103/pct:20,3,80,40/1800,/0/default.jpg
- Folio matches the report: yes; cipher present: yes
- What we checked: f59v (canvas 103 of fr. 3516, same volume as jeannin1607; his link was archive.org): interlinear "assez mal fondees de sorte que tant sen fault que je me promette rien de bien de ce commerage. Jay peur quil ne produise que du mespris de part et dautre, comme de part et dautre il semble quon y chemine que par maniere dacquit" = his excerpt
- Verdict: **confirmed** (method key recovered based on adjacent plaintext, extent partial). The check is a sample, not a re-solution.
- Notes: Letter printed in Jeannin, Negociations (1875) pp. 383-384, so text already published; 90.2% of elements identified. His excerpt omits "comme".

## Notes and corrections

Fr. 3516, image 103. The letter is printed in Jeannin, Négociations (1875), pp. 383–384. Lasry's excerpt leaves out one word ("comme").
