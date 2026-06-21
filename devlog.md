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

## 2026-06-20 — FINDINGS.md: plain-language answer
- Wrote `FINDINGS.md` answering the core confusion: what the email was (HubSpot onboarding, not the rulebook), how the competition works, what a submission is, where today sits in the timeline, and the key lever (per-category prizes → category selection). Listed open rule-questions to resolve.

## 2026-06-20 — todo.md: strategy horizon
- Wrote `todo.md` laying out the understand→strategize track (A resolve rule-questions, B category selection, C tooling, D build submission, E publish report).

## 2026-06-20 — Report site + README reflect real findings
- Filled in `docs/index.html` (lede, pillars, findings table, repo link) and rewrote `README.md` About/Status with the actual challenge summary and links. Kept the cleanvibe theme chrome.

## 2026-06-20 — Published: public repo + live Pages report
- Final leak scan over all git-tracked files: clean; raw email confirmed untracked.
- Created PUBLIC repo `EmmaLeonhart/autoscientist-challenge-research` and pushed.
- First Pages run failed (GITHUB_TOKEN can't auto-create the Pages site); enabled Pages via API (`build_type=workflow`) and re-ran → success. Report live at https://emmaleonhart.github.io/autoscientist-challenge-research/ (HTTP 200).
- Bootstrap/understanding phase complete; queue drained. Next phase = todo.md item A (Discord rule-questions) → B (category selection).

## 2026-06-20 — Strategy phase kickoff
- Opened the email's Discord link in the browser (HubSpot JS-gated tracking URL → resolves to the invite in a real browser; curl can't pass the bot check). Public challenge page exposes no raw discord.gg invite, so the email link is the route.
- Wrote `strategy/playbook.md`: prioritized Discord rule-questions (4 blocking + 4 important + 1 category-specific), unblocked "do now" actions, and a category decision matrix flagging "language" as the highest-edge target with "all other domains" as a niche-dataset fallback.
- Repopulated `queue.md` Active with the strategy steps (todo A + B).

## 2026-06-20 — Ingested Discord export; rules resolved
- User's channel export (adaption.zip) arrived early; ingested it now instead of waiting for the 5:51/6:08 crons (both cancelled as redundant).
- Raw export (other participants' messages + avatars) extracted to gitignored `data_lake/discord_export/_raw/`. Committed only PII-free official content: `faq.txt` (official FAQ doc) + `official-rules.md` (pinned rules).
- Wrote `strategy/answers.md` resolving all open rule-questions. Corrected `FINDINGS.md`: **Language is Part 1 (closes Jul 5)**, not Part 2; FAQ adds an HR category; baseline = the base model you train on; Language judged by LLM-as-judge on broad competence; AutoScientist (UI) runs training; CC-BY-NC data OK; unlimited team w/ captain; submit via per-part HubSpot form.

## 2026-06-20 — Locked category + built the dataset pipeline (executing)
- **Locked:** All Other Domains / **Shinto shrines**, **Wikidata-only (CC0)** (user decision). Clean license = no ownership/release risk; skip restricted sources.
- Scoped Wikidata: **30,918 Shinto shrines (25,837 with EN labels)**, rich properties (enshrined kami P825, location P131, coords, type, official names, Engishiki P361). → `data_lake/wikidata/data-assets.md`.
- Wrote `strategy/decision.md`, `strategy/shinto-shrines-questions.md` (questions for Discord/#support), `strategy/build-plan.md` (the MVP: Wikidata facts → QA pairs → AutoScientist finetune → beat base → dual HF+Kaggle release).
- Built + tested the dataset pipeline: `src/extract_shrines.py` (`make_qa_pairs` pure transform), `scripts/run.py` entry (sample/--full), `tests/test_qa.py` (3 passing), CI (`.github/workflows/ci.yml`), `requirements.txt`. Live sample: 25 shrines → 117 QA pairs.
- Clarified the workflow shape for the user: we build the DATASET (Wikidata pipeline, the scored edge); AutoScientist trains the MODEL; Hugging Face + Kaggle are the release destinations.

## 2026-06-20 — Broadened scope: shrines → full Shinto (kami + texts)
- User direction: don't limit to shrines, stay within **Shinto** (broad); build self-contained, reusing latent-space-cartography's seed-and-traverse pattern (no hard dep on Loka / latent-space-cartography).
- Generalized the pipeline: `src/extract_shrines.py` → `src/extract_shinto.py` with type-aware `make_qa_pairs` over 3 kinds — **shrine**, **kami** (genealogy: parents/children/native name), **seed** (curated texts/concepts: Engishiki, Kojiki, Nihon Shoki, Shinto). Updated `scripts/run.py`, tests (5 passing), and docs.
- **Fixed a data-quality bug:** the kami class was mis-set to Q175331 ("demonstration/protest" — pulled in "1989 Tiananmen Square protests"); corrected to **Q524158** ("kami"). Sample now clean: Amaterasu, Susanoo (parents Izanami/Izanagi), Hachiman, Ōkuninushi. Sample: 206 entities → 684 QA pairs.

## 2026-06-20 — Live data gather + WDQS robustness fix
- Switched from scheduled crons to gathering the full dataset live (cancelled the 7:31/8:10 jobs).
- First full run hit a WDQS **502** at shrine offset 3500 and crashed (no retry) — captured ~3.5k shrines / 16.3k pairs before dying.
- Hardened the extractor: `_query` now retries 429/502/503/504 with exponential backoff; `scripts/run.py` lightens page size to 250, throttles 1s between pages, flushes incrementally, and continues to the next kind if a page fails after retries (partial data is kept, not lost). Re-running the full gather.

## 2026-06-20 — Fix unstable pagination (duplicates + gaps)
- The resilient full run completed but the output had only 17,081 distinct shrines of 25,837 processed — OFFSET pagination without ORDER BY overlaps and skips on WDQS, producing duplicate pairs and missing entities.
- Fix: added `ORDER BY ?e` to the shrine + kami queries (deterministic OFFSET) and a `(kind, qid)` dedup guard in `scripts/run.py` that skips/reports any overlap. Re-running the full gather.

## 2026-06-20 — Honor WDQS Retry-After (finish full coverage)
- Previous gather stopped at 15,500/25,837 shrines: WDQS returned a sustained 429 at offset 15500 that outlasted the short backoff, so continue-on-failure moved on. Data captured was clean (deduped, stable), just incomplete.
- Fix: `_query` now honors the `Retry-After` header on 429 (waits the instructed time, up to 75s), 8 retries; `scripts/run.py` pause raised to 2.5s/page to stay under the rate limit. Re-running for full coverage.

## 2026-06-20 — Full Shinto dataset gathered (clean, complete)
- Re-gather succeeded with full coverage: **26,193 distinct entities (25,837 shrines + 350 kami + 6 texts) → 104,087 QA pairs**, deduped, CC0. No rate-limit drop (Retry-After handling held).
- Committed a 187-line representative sample + `dataset_stats.json`; full 104k-pair file stays in gitignored `results/`. Updated `data_lake/wikidata/data-assets.md` and `queue.md`.

## 2026-06-21 — Eval split + scorer; dataset published to Hugging Face
- `src/dataset.py`: by-entity train/test split (no leakage) + transparent fact-match scorer (`score_pair`/`evaluate`); `scripts/make_splits.py`; tests (10 passing total).
- Splits: train 88,712 pairs / 22,319 entities; test 15,375 pairs / 3,872 entities; entity leakage 0.
- **Published to Hugging Face (public, CC0):** https://huggingface.co/datasets/EmmaLeonhart/shinto-wikidata-qa — train/test/sample/stats + dataset card crediting Adaptive Data by Adaption. `scripts/push_hf.py` for reproducibility.

## 2026-06-21 — Kaggle mirror blocked on token scope
- HF dataset is live; attempted the Kaggle mirror via `scripts/push_kaggle.py`.
- The provided Kaggle token authenticates and can READ (datasets/list -> 200) but is rejected for WRITE (datasets/create/new -> 401 "Unauthorized access"). It is a read-only token; uploading needs a full-access API token.
- `scripts/push_kaggle.py` is ready to run as-is once a write-capable token is in ~/.kaggle/kaggle.json. (Credentials live only in ~/.kaggle, never committed.)
