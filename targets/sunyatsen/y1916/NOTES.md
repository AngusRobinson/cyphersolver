# Sun Yat-sen's intercepted telegrams, March–July 1916 (JACAR 特定人ノ発受郵便物取調) — read

Series: 各国内政関係雑纂／支那ノ部／革命党関係（亡命者ヲ含ム）／特定人ノ発受郵便物取調, Gaimushō 1.6.1.4-2-1-2,
vols 2–4. The Communications Bureau of the Ministry of Communications (逓信省通信局長 田中) sent the Foreign
Ministry's Political Affairs Bureau (政務局長 小池) a copy of every telegram and letter to or from Sun's circle,
each batch under a covering note headed 特定人發着郵便物等取調ノ件. The files hold no decodes. The Japanese analysts'
katakana worksheets on one kana stream (089100 frames 0079–0081) show that they tried and failed.

**Result: nearly every condenser telegram in the files read here decodes, under seven keys of the same systematic
family as the Swatow telegram (`../NOTES.md`).** In that family, 20 consonants × 5 vowels are numbered 01…99,00
vowel-major, each pair of syllables gives one four-digit standard telegraph code, and there is no additive. Each
correspondent pair had its own rotation and vowel order:

| key (`famtest.py`) | consonants from | vowel order | used on |
|---|---|---|---|
| swatow1916 | l | e a i o u | Tanaka, Swatow → Rosamonde (3 Apr 1916) |
| shanghai1916 | from b, reversed (01 = zi) | i o a e u | Sun ↔ Yamada Junzaburō, Shanghai; Shanghai (Chen Qimei, Xu Chongzhi …) → Rosamonde, Mar–Apr 1916 |
| manila1916 | g | o e u a i | Sun ↔ Konglipo, Manila; one Shanghai telegram signed by Xu Chongzhi |
| seito1916 | m | u i e o a | Qingdao (Ju Zheng; Kayano Nagatomo) ↔ Tokyo, Mar–Apr 1916 |
| sanfran1916 | x | o e u a i | Tokyo → "Youngchina", San Francisco |
| yamada1916 | q | e u i o a | Tokyo (Xie Chi, "Linwailuk") ↔ Junzaburo, Shanghai, May 1916 |
| shanghai1917 | k | a e u o i | Sun ↔ Dai Jitao, March 1917 (`../y1917/NOTES.md`) |

Two further keys are tentative, each resting on a single short telegram: Honolulu (rev10 e a o u i, cons-major,
z 4.9) and Manila in May (rot2 e u a o i, z 4.4).

Keys were found by brute force of the 57 600-key family (`../famtest.py`), which scores each key with a Chinese
character model. A key was accepted only when it reached z ≥ 6 on at least one long telegram *and* then read other
telegrams it had not been fitted to. For example, shanghai1916 was found on the Shanghai → Rosamonde telegram of
3 April and then read Sun's own outgoing telegrams to Yamada at z 7–10. Where a signature carries a rhyme-day
code (韻目代日), the code matches the date on the form every time: 有 25, 宥 26, 豔 29, 支 4, 元 13, 皓 19, 號 20,
箇 21, 漾 23.

Transcriptions, emendations and every unread group are in `transcripts_A.md` … `transcripts_D.md` (frames by
batch). The copying clerks' errors are consistent: g↔q (by far the commonest), then x↔d/s, h↔k↔n, e↔c, a↔o and
dropped pairs. Each emendation is a single letter, justified by sense and usually by a clean second occurrence of
the same group.

## Selected plaintexts

**Sun → Yamada, 26 Mar 1916** (088300 fr. 0465; z 7.4, re-verified):
> 京信□□□策：袁暫退，使黎代；俟歐戰終，乃借英力[復]出。故滬事當發於袁退之前乃可。文
"The Peking letter … plan: Yuan to step down for now with Li [Yuanhong] acting; when the European war ends, to come
back with British backing. So the Shanghai action must be launched before Yuan withdraws. — Wen"

**Shanghai → Rosamonde, 25 Mar 1916** (fr. 0468): 帝制取消，馮、朱等當漸觀望。滬異派力弱，於我略可從容佈置。海軍[?]發策較萬全…
("The monarchy is cancelled; Feng [Guozhang], Zhu [Rui] and the others will now sit on the fence …")

**Sun → Yamada, 31 Mar 1916** (fr. 0485): 北方來電，帝制取消，軍心益振。而[滬]反[?]觀望。恐前聯絡之人皆多不實，故托此爲辭，[?]得款耳。望兄詳察，勿受其欺。孫文
("I fear the people we contacted earlier are mostly not genuine and use this as an excuse to get money. Look into
it carefully and don't be taken in.")

**Sun → Yamada, 4 Apr 1916** (fr. 0494; z 9.8, no emendation, re-verified):
> 由臺灣電六百金，請交寶昌路寶康里一八三號張宗海，往甘費。聞西林赴南寧組政府，定設法破之。文
"600 gold wired via Taiwan; give it to Zhang Zonghai, 183 Baokang-li, Baochang Road, for the journey to Gansu. I hear
Xilin [Cen Chunxuan] is going to Nanning to form a government: I will find a way to break it."

**Aoyama → Kayano, Qingdao, 4 Apr 1916** (fr. 0492): 卽由正金電萱野轉五萬金，收覆。荷物由[?]以寄青島軍政官名義… (50 000 via the
Yokohama Specie Bank; arms shipped to Qingdao consigned in the name of the Qingdao military administration.)

**Hankow → Sun, 13 Apr 1916** (088400 fr. 0517; `hankow.py`). This is a digit telegram in the +111 code that Consul
Segawa described, and it reads with no emendation:
> 武漢發動事，日人謂非念五萬不辦。迭電陸參兩部，桐以軍械運輸困難且爲時久。刻人心已熟，海陸均有七分以上把握，三萬可行。機不可[失]，望速決電示。元
"On the Wuhan rising: the Japanese say it cannot be done for under 250 000. [We] have repeatedly wired the Army
Ministry and General Staff; 桐 says the arms and transport are difficult and would take a long time. Opinion here is
ripe; army and navy are both more than 70 % sure; 30 000 would do it. Don't miss the moment. Decide quickly and
wire. — 13th"

**Shanghai → Linwailuk (Tokyo), 19 May 1916** (089100 fr. 0066; z 6.0, re-verified):
> 英士昨下午在山田家被兇轟斃，捕兇[一]人，關係者數人。
"Yingshi [Chen Qimei] was shot dead by assassins yesterday afternoon in the Yamada house; one assassin and several
accomplices arrested."
Tokyo's replies the same day are 英士捐軀，極堪慟悼。主使爲誰？ ("Who was behind it?") and 先生…務處處戒備 ("the
Master must take every precaution"). Shanghai answered on 22 May that the instigator was the government, 遣之暗殺主謀爲[政]府.

**Tokyo → Yamada, 26 May 1916** (fr. 0092–93; z 9.6, re-verified):
> 克強言外務省意先生宜緩赴青島。又軍械事能得青木一電參謀本部較更有力云云…
"Keqiang [Huang Xing] says the Foreign Ministry's view is that the Master should put off going to Qingdao. On the arms,
a telegram from Aoki [Nobuzumi] to the General Staff would carry more weight."
This is Tokyo reporting the Foreign Ministry's own advice back to Sun, and the Foreign Ministry was reading the copy.

**Tokyo → Yamada, 29 May 1916** (fr. 0113–14): 據譚根云，岑有軍火船四艘由神戶回粵… (Tan Gen says Cen Chunxuan has four
munitions ships going from Kobe to Guangdong.)

**Luzhou → "Ilchang Tokio", 10 Jul 1916** (090000 fr. 0417). Plain code:
> 宥電敬悉。承念甚感。久罹喉病，軍中失調，醫治漸痊，幸釋綺注。鍔叩。蒸
This is Cai E (蔡鍔) thanking Tokyo for its concern about the throat illness he had caught with the army, which was
getting better. He died of it in Fukuoka four months later, eight days after Huang Xing.

**Tokyo (中田) → Huang Xing, Shanghai, 13 Sept 1916** (090100 fr. 0471), plain code: 閱報憂悚。接[?]電，母[恙?]稍安。請靜養。現如何？
("Alarmed to read the papers. Your mother is a little better. Please rest. How are you now?") Huang Xing was already
ill; he died on 31 October. The Japanese clerk's own kanji glosses on the form differ at 4443 and 3225.

## Not read / open

* **The July–November 1916 systems** were decoded by Brice Dudout in October 2026. See "Outside decipherment" below.
  This file earlier called them one "文密 code (six vowels)". That was wrong: there are two systems, and the 文密
  prefix belongs to the five-vowel one.
* Five Tokyo → Junzaburo telegrams of late May with no "Thirtyseventh" prefix. Three are 8 words long, and one
  exists as a typed copy, so misreading is ruled out. The Ylchang telegrams of 29–30 May use *w* as a consonant.
  Dudout reports that they do not decode in his two grids either.
* A few groups in most long telegrams, flagged [?] in the transcripts.
* **The Swatow telegram's operator original is not in B03050088300 or B03050088400.** Every Latin-letter form in
  both files was read, and the kana forms (088300 fr. 0441–0458) are domestic. None comes from Swatow. The copy filed
  in B03050738800 remains the only one found, and its three garbled tail groups stay unresolved.

## Outside decipherment: Brice Dudout, July–November 1916 (received 11 Oct 2026)

Brice Dudout emailed on 11 Oct 2026 with readings of the July–November 1916 traffic. His readings, transcriptions
and solver are at https://bdudout.github.io/wenmi/ and https://github.com/bdudout/wenmi (CC BY 4.0). The traffic is
in two systems, and he calls the two grids G0 and Y0. Both number the syllables consonant by consonant, with the vowel
order reversed on every second consonant. A pair of syllables gives one standard telegraph code, with no additive.

* **G0**, five vowels. This is Tokyo → 軍務院 (Zhaoqing, then Canton), June–September 1916, frames 0348, 0386, 0406,
  0415, 0416b, 0455b and 0462. The 20 consonants run h g f d c b z y x w v t s r q p n m l k (with w and y, without j).
  The value is 5·i plus the rank of the vowel in a e i o u, counted backwards on odd i (ha 00 … hu 04, gu 05 … ga 09).
  Dudout held 0406 out of the fitting.
* **Y0**, six vowels (y is a vowel). This is Tokyo → Yunnan (Tang Jiyao, the provincial assembly, the finance office)
  and Shanghai (中華新報), July–November 1916, frames 0413, 0416a, 0449, 0455a, 0467, 0473, 0489a, 0494, 0496 and 0498.
  The consonants are b d f g h k l m n p r s t v w x z, in alphabetical order. The value is 6 × rank plus the rank of
  the vowel in y u o i e a, counted backwards on odd ranks. The cells ze and za, 100 and 101, are unused. Dudout
  anchored the grid on the clear twin 0489b and held out 0496a, which reports Cai E's death.

**Checked here, 11 Oct 2026.** Both checks used our own JACAR PDFs and transcriptions made blind from the forms,
not from his files. The frame offsets are 089900 → 0329, 090000 → 0388, 090100 → 0447 and 090200 → 0503.

* **0489a**, 5 Nov 1916, to 0781 4206 6511 唐督軍 yunnanfu, 9 words. The text reads
  `Cg gyrotatapo fobawahavo rodunifubu kyhary`. Y0 gives 擬[7777]號南歸謹聞伸歌, and 8 of the 9 codes are exact.
  十 (0577) needs ta → ba. The clear twin 0489b goes to 4164 ···· ·585 yunnanfu (省議會 according to Dudout; only 4164 省 is
  clean on the form) and reads
  0577 5714 6386 4453 2588 2608 2107 3329 0135 2960 = 十號起程月末抵滇伸歌. The sender's address field on both forms
  reads **青山南町四ノ二一 関方 趙伸**, which identifies 伸 as Zhao Shen, care of Seki, directly on the form. Frame 0388
  has a kana delivery form to アヲヤマミナミマチ セキマサヲ.
* **0416b**, 19 Jul 1916, Tokyo → 6511 0523 7108 5128 1989 (軍務院肇慶) Canton, 16 words. It begins with the clear
  2429 1378 文密, followed by `fazihipego wezelucuna hamodarodo vorokesiya rodugoluro xoxotuhica hematemiba
  giheyuxifa`. G0 gives 報傳取消日人態度遽變[確]否速示俾便行檄 伸 [皓], with two one-letter emendations: x→r
  (4315 確) and i→e (4110 皓). 皓 is the rhyme-day code for the 19th, which matches the form's date.
* **The correction.** The six-vowel telegram on the same frame, 0416a to 0022 5478 2450 1032 中華新報 Shanghai, opens
  with the clear 6567 2429 5028 6567 3329 4206 = 轉文羣轉滇督, then `Cg`. So 文密 is the prefix of the G0 channel. We had
  attached it to the six-vowel system and lumped the two together. `../y1917/fam6.py` could not have found either grid,
  because it was run only on 0509/0511 and never reversed the vowel order on alternate consonants.
* **Not checked here:** his other ~15 readings, including 0496a (Cai E) and 0406.
* **Possible slip in his 0406:** 誕意 is probably 誠意. In G0, 6130 and 6134 differ by za/zu.

We adopt none of his readings as our own. The site page (`docs/sunintercepts.html`, section 07) credits him and shows
only the two telegrams checked here. If his readings are used beyond that, `outcome.method` for that part is "read
from existing decipherment", found 11 Oct 2026.

## Files

* `transcripts_A.md`–`transcripts_D.md`: per-telegram transcriptions, headers, keys, z-scores and decodes.
* `hankow.py`: the Hankow +111 digit telegram.
* `../famtest.py`: runs the whole family plus the known keys on any telegram (`python famtest.py "w1 w2 …"`).
* `../jacar_fetch.py`: JACAR metadata and raw-PDF fetcher (the PDFs themselves are git-ignored).
