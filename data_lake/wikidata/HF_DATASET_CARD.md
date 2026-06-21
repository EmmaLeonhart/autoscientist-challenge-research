---
license: cc0-1.0
language:
- en
- ja
task_categories:
- question-answering
- text-generation
tags:
- shinto
- wikidata
- japan
- religion
- knowledge-graph
pretty_name: Shinto Wikidata QA
size_categories:
- 100K<n<1M
---

# Shinto Wikidata QA

Instruction/QA pairs about the **Shinto** domain — Shinto shrines, kami (deities, with
genealogy), and key texts (Engishiki, Kojiki, Nihon Shoki) — generated from **Wikidata**
structured facts.

Built for the **Adaption Labs AutoScientist Challenge** (All Other Domains track).
Credit: **Adaptive Data by Adaption**.

## Source & license
- **Source:** Wikidata Query Service (https://query.wikidata.org). All statement data is
  **CC0 / public domain**, so this derived dataset is released **CC0-1.0**.
- Generated 2026-06-20 by `src/extract_shinto.py` in
  [autoscientist-challenge-research](https://github.com/EmmaLeonhart/autoscientist-challenge-research).

## Contents
- **26,193 distinct entities** → **104,087 QA pairs**: 25,837 shrines, 350 kami, 6 seed texts.
- Splits are **by entity** (an entity's pairs never straddle train/test), so test answers
  concern entities unseen in training.
  - `train.jsonl` — 88,712 pairs / 22,319 entities
  - `test.jsonl` — 15,375 pairs / 3,872 entities

## Schema (JSON lines)
```json
{"instruction": "Which kami (deity) is enshrined at Nishinomiya Shrine?", "input": "", "output": "Ebisu", "qid": "Q705297", "kind": "shrine"}
```
`kind` ∈ {`shrine`, `kami`, `seed`}. Question types: enshrined kami, location, shrine
type, coordinates, kami genealogy (parents/children), Japanese names, text descriptions.

## Intended use
Finetuning a base model into a Shinto knowledge model; measuring lift over the base model
on the held-out `test.jsonl`.
