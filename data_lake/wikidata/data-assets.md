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
license-safe finetuning data — without touching any restricted source.

## Broadened to the full Shinto domain (kind buckets)
The extractor (`src/extract_shinto.py`, `make_qa_pairs` pure transform, unit-tested)
covers three entity kinds with type-aware questions:
- **shrine** — Q845945 (~25.8k EN): enshrined kami, location, type, coords, official name.
- **kami / deity** — **Q524158** (~352): description, **genealogy** (parents P22/P25, children P40 — e.g. Susanoo → Izanami/Izanagi), Japanese name.
- **seed (texts & concepts)** — curated QIDs (Engishiki Q1342448, Kojiki Q533996, Nihon Shoki Q695225, Shinto Q1011402, ...): description, author.

> **Data-quality note:** the kami class was initially mis-set to **Q175331, which is actually
> "demonstration/protest"** (it pulled in "1989 Tiananmen Square protests"). Corrected to
> **Q524158 ("kami — divine being in Shinto")**. Lesson: verify class QIDs against a sample,
> since the dataset's quality is itself scored by the challenge.

## Full dataset built (2026-06-20)
A complete extraction now exists (`results/shinto_qa.full.jsonl`, gitignored — large):
- **26,193 distinct entities** — 25,837 shrines (the full EN-labelled set), 350 kami, 6 seed texts.
- **104,087 instruction/QA pairs**, deduped (`(kind,qid)` guard), CC0.
- A 187-line representative `shinto_qa.sample.jsonl` and `dataset_stats.json` are committed.

Two robustness lessons baked into `src/extract_shinto.py` / `scripts/run.py`:
1. **Stable pagination** — `OFFSET` without `ORDER BY` overlaps/skips on WDQS; add `ORDER BY ?e`.
2. **Rate limits** — WDQS 429s on heavy queries; honor the `Retry-After` header + throttle paging.
