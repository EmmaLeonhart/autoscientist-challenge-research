# Data assets — Shinto shrines on Wikidata (CC0)

Scoped live from the Wikidata Query Service on 2026-06-20. All Wikidata statement data
is **CC0 (public domain)** → freely releasable to Hugging Face + Kaggle (challenge rule).

## Scale
- **30,918** Shinto shrines (`?s wdt:P31/wdt:P279* wd:Q845945`).
- **25,837** of them have an **English label** (the usable base for English QA).

## Properties available (top, by count of statements on shrine items)
| Prop | Meaning | Count | QA use |
|---|---|---|---|
| P31 | instance of (shrine type) | 103,807 | "What type of religious site is X?" |
| P131 | located in admin territory | 63,720 | "Where is X located?" |
| P17 | country | 47,164 | description grounding |
| P6375 | street address | 43,722 | (optional) address QA |
| P3225 | Corporate Number (Japan) | 33,977 | id linking |
| P625 | coordinate location | 29,320 | "Coordinates of X?" |
| P281 | postal code | 28,882 | (optional) |
| P825 | dedicated to (kami) | 28,467 | **"Which kami is enshrined at X?"** |
| P1448 | official name | 27,681 | "Official name of X?" |
| P1454 | legal form | 22,528 | — |
| P361 | part of | 16,104 | Engishiki / shrine network |
| P1814 | name in kana | 15,040 | Japanese-name QA |
| P13677 | Kokugakuin museum entry id | 13,115 | id linking |
| P460 | said to be the same as | 11,618 | dedup/identity |
| P18 | image | 10,301 | (potential multimodal) |
| P11250 | (shinto wiki link) | 8,373 | cross-ref to owned wiki |

`_scope.json` holds the raw top-20 property counts.

## Implication
~25k shrines × several facts each → easily **100k+ instruction/QA pairs** of clean,
license-safe finetuning data — without touching any restricted source. The MVP build
plan in `strategy/build-plan.md` turns these properties into the dataset; the extractor
is `src/extract_shrines.py` (`make_qa_pairs` is the pure transform, unit-tested).
