# autoscientist-challenge-research — Work Queue (research)

**This file is a queue of *concrete, executable steps*, not a state snapshot.** When an item is done, delete it from this file AND append a dated entry to `devlog.md` in the same commit, then push. Do not add checkmarks or "done" markers in place.

See `CLAUDE.md` § "Workflow Rules" and § "Research workflow".

> Running interactively with the user present; the three-cron autonomous playbook is intentionally NOT started this session.

---

## Active — Build phase (All Other Domains: Shinto shrines)

**Locked:** All Other Domains / **broad Shinto** (shrines + kami + texts/concepts), **Wikidata-only (CC0)**, self-contained. **Full dataset gathered: 26,193 entities → 104,087 QA pairs** (`results/shinto_qa.full.jsonl`; sample + `dataset_stats.json` committed). See `strategy/decision.md`, `data_lake/wikidata/data-assets.md`.

Dataset **published to Hugging Face**: https://huggingface.co/datasets/EmmaLeonhart/shinto-wikidata-qa (CC0, train/test, card credits Adaptive Data). Eval split done (`src/dataset.py`, by-entity, 0 leakage; scorer + tests).

1. **Mirror the dataset to Kaggle.** The challenge requires the dataset on **both** HF *and* Kaggle. Push the same train/test + card to a Kaggle dataset (need Kaggle API creds).
2. **Ask the gating eval questions in Discord** (#support / weekly Research Hour) — `strategy/shinto-shrines-questions.md` A.1–A.4 (how All Other Domains is judged; held-out set; base models; dataset-quality scoring).
3. **Platform + credits.** Connect HF/Kaggle keys in the Adaption app (`adaptionlabs.ai/app/settings?tab=api_keys`); confirm the 1,000 challenge credits landed (the 50 are free-tier).
4. **Train via AutoScientist** on the dataset; measure held-out lift vs the base model with `src/dataset.py`'s scorer; iterate.
5. **Release weights + submit.** Push trained weights to HF *and* Kaggle (credit Adaptive Data); submit the Part 2 form when it opens (Jul 6); post the bonus demo.
6. **Enrich the dataset (optional breadth).** More fact types/kinds: official name P1448, kana P1814, Engishiki P361; kami reverse enshrinement; festivals/sects buckets. Verify each new class QID against a sample (Q175331→Q524158 lesson) + add tests.

---

## Pointers

- The plain-language answer: `FINDINGS.md`.
- The literature review (evidentiary base): `literature/REVIEW.md`.
- Long-horizon strategy backlog: `todo.md`.
- Completed work (chronological): `devlog.md`.
- Published report: https://emmaleonhart.github.io/autoscientist-challenge-research/
