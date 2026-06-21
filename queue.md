# autoscientist-challenge-research — Work Queue (research)

**This file is a queue of *concrete, executable steps*, not a state snapshot.** When an item is done, delete it from this file AND append a dated entry to `devlog.md` in the same commit, then push. Do not add checkmarks or "done" markers in place.

See `CLAUDE.md` § "Workflow Rules" and § "Research workflow".

> Running interactively with the user present; the three-cron autonomous playbook is intentionally NOT started this session.

---

## Active — Strategy phase (todo A + B)

Rule-questions are **resolved** from the Discord export + FAQ — see `strategy/answers.md`. Key: **Language is Part 1, closes Jul 5**; baseline = the base model you train on; Language judged by LLM-as-judge on broad language competence; AutoScientist (UI) runs the training; submit via per-part HubSpot form; CC-BY-NC data OK; unlimited team w/ a captain.

1. **Lock the target category.** Working rec: **Language** (Part 1, highest owned-data edge, but tight Jul 5 deadline); fallbacks: "all other domains" (Part 2, niche owned dataset) or Healthcare (rewards extra metrics). *A 6:10pm cron asks the user to pick if not already locked.*
2. **Stand up publishing accounts + platform.** Hugging Face + Kaggle (both mandatory release destinations) and the Adaption app (connect HF/Kaggle keys at `adaptionlabs.ai/app/settings?tab=api_keys`); confirm the 1,000 challenge credits landed.
3. **Draft the data-asset inventory** mapping owned corpora (lexemes, multilingual Wikidata, Aelaki, Japanese text, genealogy) to the chosen category's objective.
4. **Decompose the build** for the locked category into a fresh queue (adapt dataset → AutoScientist train to beat baseline → dual HF+Kaggle release crediting Adaptive Data → submit form → demo/social).

---

## Pointers

- The plain-language answer: `FINDINGS.md`.
- The literature review (evidentiary base): `literature/REVIEW.md`.
- Long-horizon strategy backlog: `todo.md`.
- Completed work (chronological): `devlog.md`.
- Published report: https://emmaleonhart.github.io/autoscientist-challenge-research/
