# Decision — locked category

**Category:** All Other Domains (Part 2)
**Topic:** **Shinto shrines** (Japanese shrine knowledge — drawn from owned Wikidata / wiki / Engishiki / Kokugakuin shrine corpora)
**Locked:** 2026-06-20 by the user.

## Why
- **All Other Domains** is the Part 2 catch-all, so a niche owned dataset is allowed and is evaluated in its own track (prizes per track).
- **Shinto shrines** is where we have an unusually deep, largely unique owned dataset: multilingual Wikidata shrine entities, Engishiki / Shikinai-ronsha records, Kokugakuin shrine database references, shrine genealogies, and shrine wiki text. A thin-to-empty competitive field plus a proprietary-grade data edge.
- **Deadline:** Part 2 closes **Aug 3, 2026** (form opens Jul 6) — more runway than the Language track's Jul 5.

## Key constraints carried from the rules (`strategy/answers.md`)
- Release the **adapted dataset + model weights to BOTH Hugging Face and Kaggle**, crediting *Adaptive Data by Adaption*.
- Must show **measurable improvement over the base model you train on** on Adaption's internal held-out test set; **dataset quality also factors in**.
- Data must be under an **open license permitting public release + attribution** (CC-BY-NC acceptable).
- Training runs via **AutoScientist (UI)**; 1,000 challenge credits.

## Next
The open questions that must be resolved before/while building are in **`strategy/shinto-shrines-questions.md`**. The build is decomposed in `queue.md`.
