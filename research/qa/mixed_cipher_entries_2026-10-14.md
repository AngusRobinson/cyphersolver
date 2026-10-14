# QA: entries that combine different ciphers (14 Oct 2026)

Rule (George Lasry, 14 Oct 2026; now in `.claude/skills/writeup/SKILL.md`, "One key, one entry"): a write-up
presents one key or cipher system. Letters in different ciphers are not combined because they share a volume,
sender, recipient or feature.

Fixed in the same session: `superscript` → `ghinucci1527` + `gilino1527`; `vasto1527` → `vasto1527` (no. 6) +
`ranzo1528` (no. 20 and the Ranzo letters; no. 10, Cipher 1, kept as a cross-reference).

Read-only audit of every page in `PAGES` with its profile and NOTES (sub-agent, 14 Oct 2026). Line numbers are
in `docs/_build_site.py` (the PAGES entry) unless another file is named. Not yet verified by hand.

## High confidence: two or more keys presented with results

| Slug | Distinct keys / systems | Evidence | Suggested split |
|---|---|---|---|
| `r1854` | Four letters to Gonzaga, each in a different homophonic cipher; three keys recovered, Malatesta's runs open | :491 ("four different homophonic ciphers"); `targets/r1854/NOTES.md:15` | one slug per letter, plus `malatesta1428` |
| `gramont1529` | Four letters, four Lasry keys (Gramont, Mâcon, Langeac, …) | :586; `targets/gramont1529/NOTES.md:5,7`; profile "Four separate keys" | one slug per key |
| `soria1523` | Key A (R9488–90, R9492–93) and key B (R9491, R9494–98) | :641; README already "Split entry 1/2, 2/2"; profile `outcome.parts` | `soria1523a`, `soria1523b` |
| `conti1649` | Nos. 41–42 Lasry's polyphonic key; no. 43 a syllabic number code | :711; `targets/conti1649/NOTES.md:17,54` | `conti1649`, `conti1649code` |
| `windischgraetz1720` | R5017 Chancellery nomenclator (no. 1); R5018 private key (nos. 2, 3, 6) | :898; NOTES:6,12; profile "Two keys" | two slugs |
| `kaa4591` | At least six systems (Fulda key, Łaski glossed key, R9416 ciphertext-only, A′/B …) | :209; profile parts with two methods | one slug per system |
| `kaa4591b` | Łaski key plus two new homophonic alphabets (King John 1533, Wardein 1537) | :204 | Łaski letter to its key family; `zapolya1533`, `wardein1537` |
| `maisse1592` | Cipher 1 (ff. 370/373) and Cipher 2 (ff. 404/406/410), both with Tomokiyo keys | :1068; README "Two ciphers, not one" | `maisse1592a`, `maisse1592b` |
| `champagne1590` | Name key (no. 23); two-digit alphabet (nos. 24/25/60); Laurière's Nevers key no. 57 | :1104 | `champagne1590`, `lauriere1593` (and possibly no. 23) |
| `esp318` | No. 5 (Parisi), no. 92 (Cifra general), no. 95 (Lasry alphabet), nos. 93–94 (another family) | :526; profile "a different key per letter" | per letter |
| `legation` | Erving 1807 code and JQA 1812 own code, both decrypted | :1351; `docs/_methods.py:162` | `erving1807`, `jqa1812` |
| `sieniawski1708` | Vienna agent → Schenck 1706 (R7486–R7500) and Sieniawski letters (R7468–R7485, key A) | :863; README rows 103 and 368 already separate | `schenck1706`, `sieniawski1708` |

## Medium confidence

- `ferdinand3`: R1889/R1890 one alphabet + syllabary; R1887 (1634) "the different 1634 cipher", 88.4%. :295; NOTES:40. Split `ferdinand1634`.
- `rupert`: f. 107 graphic signs read (key f. 106) with unsolved numeric ciphers (Maurice 1645; R8623/R8624; f. 104; Trevor). :372. Split `woman1645`.
- `malsburg1637`: numeric homophonic table and a separate five-shift alphabetic block. :355; NOTES:3,6.
- `riksarkivet1628`: "four unrelated groups"; Bremen read. :276. Split `bremen1631`.
- `sessa1593`: nos. 45/79/47 one syllabic cipher; no. 68 (Feria–Mansfeld) a second. :1217. Split `feria1593`.
- `mondoucet`: a 1572 key and a 1573 key, each recovered (key change within one correspondence, like Soria). `docs/mondoucet.html:59`.
- `wod1568`: Throckmorton Cipher 1 read; margin word-sign code and Wood's 1568 line closed. :179.
- `geertruidenberg`: Torcy's two-part code and Villars's other code, both attempted. :1307.
- `sp106box10`: Systems A (R725), B, C and the three-figure code; one codebreaker's file, defensible as an archival unit. :246.

## Low confidence: a second system shown but barely worked

`morosini1588` (R53/R54 second key, partly read), `dandini1580` (key variant), `rome1536` (R4248 second cipher, from
its contemporary decipherment), `nevers1593` (Revol letters in key no. 60, not deciphered), `r4349`, `potocka1714`,
`vanreede1787`, `affry1757` (R1071 counted in the stats), `vich1511`, `adfgvx` (fifteen daily keys of one system).

## Judged fine

`sp106r597` (keys A/B alternate inside one designed system), `estrada1503` (code/letter mixture of one Cifra
general), `sanchez1522`, `cobham1588`, `harley287`, `segur`, `raince`, `ottobon`, `armstrong`, `vatican`, `joyeuse`
(other cipher only as a ruled-out sibling or cross-reference), `heidelberg597` (one notebook, one writer),
`hm1645`, `ronquillo1676`, `sauli1579`, `selve1535`, `smith1562`, `lebel1593`, `benedict1399` (several letters, same
key). To check: `castelcicala1816` (page says one code; profile notes R9586/R9588 use a second).

Not on the site yet, apply the rule when written up: `thurloe` (four unrelated ciphers), `louis1615` (Brulart and
Sabran keys), `matignon1586` (Cipher-1 and Cipher-3).
