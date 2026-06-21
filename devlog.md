# autoscientist-challenge-research — Devlog

**This file is where "done" lives.** `queue.md` is delete-only: when a queue
item is finished, the item is **deleted from `queue.md`** and a dated entry
is **appended here**, in the same commit as the work, then pushed. Never
tick a box in place — a checked box left in `queue.md` is the failure mode
this file exists to prevent.

Also record releases (tag + a one-line note), notable milestones, and
anything else worth a chronological trail. Newest entries at the bottom.

This is the **same convention as the cleanvibe repo's own `devlog.md`** —
every cleanvibe-scaffolded project gets one for the same reason.

See `CLAUDE.md` § "Workflow Rules" and `queue.md`'s preamble.

---

## 2026-06-20 — Project scaffolded

Scaffolded with `cleanvibe new` (cleanvibe v1.13.1). Future entries
land here as queue items get deleted.

## 2026-06-20 — Ingested source email into data lake (redacted)
- Moved the AutoScientist Challenge welcome email (`team@adaptionlabs.ai`, 2026-06-17) into `data_lake/email/`.
- Raw original with live HubSpot tracking + unsubscribe tokens kept locally at `data_lake/email/_raw/` (gitignored, never published).
- Committed a redacted `.eml` (QP soft-breaks joined so every tracking URL/token is scrubbed → `[REDACTED-TRACKING-URL]` / `[REDACTED-TOKEN]`) and a clean `autoscientist-welcome.parsed.md` extraction. Verified 0 live tokens in committed files.

## 2026-06-20 — Literature review: how the challenge works
- Web-researched Adaption Labs + the AutoScientist Challenge from primary (challenge page, product pages) and independent (TechCrunch) sources.
- Wrote `literature/sources.md` (S1–S5) and `literature/REVIEW.md` synthesizing the mechanics: 4-week / two 2-week phases, 10 categories, submission = adapted dataset + trained weights to BOTH Hugging Face & Kaggle + measurable % gain over baseline on Adaption's held-out test sets. Noted email-vs-official domain-split discrepancy.
