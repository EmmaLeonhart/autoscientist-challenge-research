# Build plan — Wikidata **Shinto** knowledge model (MVP)

Category: **All Other Domains** (Part 2, closes Aug 3). Data: **Wikidata only (CC0)** — clean license, fully releasable. Scope: broad Shinto — shrines (~25.8k EN), kami/deities (~352, Q524158), and curated texts/concepts. See `data_lake/wikidata/data-assets.md`.

## The idea (one sentence)
Finetune a small base model into a **Shinto knowledge model** using instruction/QA pairs generated from Wikidata structured facts (shrines, kami genealogy, texts), and show measurable improvement over the base model on a held-out split of unseen entities.

## Why it fits the rules
- **Open dataset + weights, dual HF+Kaggle release:** Wikidata is CC0, so the dataset is trivially releasable; the finetuned weights are ours to release. Credit *Adaptive Data by Adaption*.
- **Measurable improvement over the base model you train on:** we hold out unseen shrines; the base model has no special shrine knowledge, the finetuned one should answer shrine facts correctly → clear lift. Dataset quality also scores (it's clean, structured, broad).
- **Self-contained eval:** we can supply our own held-out QA set if All Other Domains needs one (open question A.1).

## Data → QA generation (from the scoped properties)
For each shrine, mint instruction/QA pairs from its facts:
| Fact (property) | Example question | Answer source |
|---|---|---|
| Enshrined kami (P825) | "Which kami is enshrined at {shrine}?" | deity label(s) |
| Admin location (P131) | "Where is {shrine} located?" | city/prefecture label |
| Country (P17) | "In which country is {shrine}?" | country label |
| Shrine type (P31) | "What type of religious site is {shrine}?" | type label |
| Coordinates (P625) | "What are the coordinates of {shrine}?" | lat/long |
| Official name (P1448/P1814) | "What is the official Japanese name of {shrine}?" | name/kana |
| Part of / Engishiki (P361) | "What is {shrine} part of?" | parent label |
| Aggregate (reverse) | "List shrines that enshrine {kami}." / "...in {prefecture}." | grouped |

Plus a descriptive pair per shrine ("What is {shrine}?" → grounded one-liner).

## Steps (mirrored in queue.md)
1. **Extract + generate** — `src/extract_shrines.py` queries Wikidata and emits QA JSONL. (Foundation written; sample runs now.)
2. **Scale + split** — paginate to the full ~25k shrines; hold out ~15% of *shrines* (not pairs) as the test set so eval is on unseen shrines.
3. **Format for the platform** — convert to whatever AutoScientist ingests (open question A.7); pick a base model (A.6).
4. **Train via AutoScientist**, measure held-out QA accuracy vs base.
5. **Release** dataset + weights to HF + Kaggle (credit Adaptive Data), then submit the Part 2 form.

## Open questions that gate the eval design: `strategy/shinto-shrines-questions.md` (esp. A.1–A.4).
