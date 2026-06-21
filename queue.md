# autoscientist-challenge-research — Work Queue (research)

**This file is a queue of *concrete, executable steps*, not a state snapshot.** When an item is done, delete it from this file AND append a dated entry to `devlog.md` in the same commit, then push. Do not add checkmarks or "done" markers in place.

See `CLAUDE.md` § "Workflow Rules" and § "Research workflow".

> Running interactively with the user present; the three-cron autonomous playbook is intentionally NOT started this session.

---

## Active — Build phase (All Other Domains: Shinto shrines)

**Locked:** All Other Domains / Shinto shrines, **Wikidata-only (CC0)**. Data scoped (~25.8k EN-labelled shrines). Pipeline foundation built + tested (`src/extract_shrines.py`, `make_qa_pairs`; sample = 25 shrines → 117 QA pairs). See `strategy/decision.md`, `strategy/build-plan.md`, `data_lake/wikidata/data-assets.md`.

1. **Scale + enrich the dataset.** Run `scripts/run.py --full` to paginate all shrines; add more fact types to `make_qa_pairs` (official name P1448, kana P1814, part-of/Engishiki P361, reverse/aggregate questions e.g. "shrines that enshrine {kami}", "shrines in {prefecture}"). Add tests for the new pair types.
2. **Build the eval split.** Hold out ~15% of *shrines* (not pairs) as an unseen test set; write a small scorer (exact/contains match on facts) so we can measure base-vs-finetuned lift ourselves.
3. **Ask the gating eval questions in Discord** (#support / weekly Research Hour) — `strategy/shinto-shrines-questions.md` A.1–A.4 (how All Other Domains is judged; held-out set ownership; base models; dataset-quality scoring).
4. **Stand up publishing + platform.** Hugging Face + Kaggle accounts; connect keys in the Adaption app (`adaptionlabs.ai/app/settings?tab=api_keys`); confirm the 1,000 challenge credits landed (the 50 are free-tier).
5. **Train via AutoScientist**, measure held-out lift vs the base model, iterate on dataset quality.
6. **Release + submit.** Push dataset + weights to HF *and* Kaggle (credit Adaptive Data by Adaption); submit the Part 2 form when it opens (Jul 6); post the bonus demo.

---

## Pointers

- The plain-language answer: `FINDINGS.md`.
- The literature review (evidentiary base): `literature/REVIEW.md`.
- Long-horizon strategy backlog: `todo.md`.
- Completed work (chronological): `devlog.md`.
- Published report: https://emmaleonhart.github.io/autoscientist-challenge-research/
