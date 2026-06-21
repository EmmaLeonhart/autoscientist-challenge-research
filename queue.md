# autoscientist-challenge-research — Work Queue (research)

**This file is a queue of *concrete, executable steps*, not a state snapshot.** When an item is done, delete it from this file AND append a dated entry to `devlog.md` in the same commit, then push. Do not add checkmarks or "done" markers in place.

See `CLAUDE.md` § "Workflow Rules" and § "Research workflow" for how this file, planning mode, and the task tool stay in sync.

> **Note:** Running interactively with the user present, so the three-cron autonomous playbook is intentionally NOT started this session. Add it later if autonomous operation is wanted.

---

## Active

1. **Ingest the source email into `data_lake/` (redacted for public release).** Move the user's `.eml` welcome email into `data_lake/email/`. Keep the original raw file (with live HubSpot/unsubscribe tokens) under `data_lake/email/_raw/`, which is gitignored so it is never published. Commit a redacted `.eml` and a clean `parsed.md` extraction with all tracking links / unsubscribe tokens replaced by `[REDACTED]`.

2. **Literature review / web research — how the AutoScientist Challenge actually works.** Use web search + `WebFetch` to investigate: Adaption Labs (adaptionlabs.ai), the AutoScientist Challenge rules, what "Adaptive Data by Adaption" is, what a submission actually consists of, how judging/winners work, the Kaggle/Hugging Face open-source requirement, the two parts and their domains. Write one note per source into `literature/sources.md` (claim, what it contributes, citation) and synthesize `literature/REVIEW.md`.

3. **Write the analysis: what the email is + how the challenge works.** Create `FINDINGS.md` answering the user's actual confusion: what they signed up for, the mechanics, deadlines (Part 1 ends Jul 5, Part 2 Jul 6–Aug 3), and the open-source requirement. Plain-language, cited from the literature review.

4. **Create `todo.md` — the long-horizon strategy ("understand → strategize").** Now that the mechanics are understood, lay out the strategy track: candidate domains/tracks to target, what a competitive submission looks like, timeline against the deadlines.

5. **Update `docs/index.html` + `README.md`** to reflect the real question, the one-line findings, and project state.

6. **Go live: create a PUBLIC GitHub repo under `EmmaLeonhart` and push.** `gh repo create --public --source=. --push`. Confirm Pages/CI wire up. Verify no live tokens are in the committed tree.

---

## Pointers

- The literature review (evidentiary base): `literature/REVIEW.md`.
- Completed work (chronological): `devlog.md`.
- Long-horizon strategy backlog: `todo.md`.
