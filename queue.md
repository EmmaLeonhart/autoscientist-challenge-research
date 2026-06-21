# autoscientist-challenge-research — Work Queue (research)

**This file is a queue of *concrete, executable steps*, not a state snapshot.** When an item is done, delete it from this file AND append a dated entry to `devlog.md` in the same commit, then push. Do not add checkmarks or "done" markers in place.

See `CLAUDE.md` § "Workflow Rules" and § "Research workflow".

> Running interactively with the user present; the three-cron autonomous playbook is intentionally NOT started this session.

---

## Active — Strategy phase (todo A + B)

1. **Resolve blocking rule-questions in Discord.** Post `strategy/playbook.md` §1 blocking questions (held-out test set + baseline; required tooling; base-model constraints; submission mechanism). Record answers → `strategy/answers.md`; update `FINDINGS.md` where they change the picture. *(User action in Discord; agent drafts/records.)*
2. **Stand up publishing accounts.** Confirm/create Hugging Face org + Kaggle account (both mandatory release destinations). Note handles in `strategy/playbook.md` §2.
3. **Draft the data-asset inventory** to firm up the §3 category matrix (what datasets/corpora we already own that map to a category).
4. **Lock the target category** once Q1/Q2/Q9 are answered (working rec: "language", fallback "all other domains").
5. **Decompose the build** for the chosen category into a fresh queue (dataset → finetune/beat baseline → dual HF+Kaggle release → demo/social).

---

## Pointers

- The plain-language answer: `FINDINGS.md`.
- The literature review (evidentiary base): `literature/REVIEW.md`.
- Long-horizon strategy backlog: `todo.md`.
- Completed work (chronological): `devlog.md`.
- Published report: https://emmaleonhart.github.io/autoscientist-challenge-research/
