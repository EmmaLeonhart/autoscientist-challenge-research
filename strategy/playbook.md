# Strategy Playbook — placing in the AutoScientist Challenge

Moving from "understand" to "do." This decomposes `todo.md` items **A** (resolve rule-questions) and **B** (category selection) into something actionable. Grounded in `FINDINGS.md` / `literature/REVIEW.md`.

---

## 1. Open rule-questions to ask in Discord (prioritized)

These are the things that genuinely block committing to a build. Ask the top ones first — the answers change *what* and *whether* we build.

**Blocking (ask first):**
1. **Held-out test set & baseline.** Per category, what *is* the held-out test set, what **baseline model** must we beat, and how is the "measurable % improvement" measured and reported? Is scoring automated or judged?
2. **Required tooling.** Is using **AutoScientist / Adaptive Data required**, or just encouraged (the credits imply intended use)? Can we bring our own finetuning pipeline / dataset?
3. **Base-model constraints.** Which base models are allowed? Any size, family, or license restrictions on the model we adapt?
4. **Submission mechanism.** *How* do we actually submit? Is posting the dataset + weights to HF/Kaggle enough, or is there a submission form/deadline/registration-of-entry step? Where does the entry get linked?

**Important (ask next):**
5. **Open-source license requirements** for the released dataset + weights (must they be a specific permissive license? any commercial-use clause?).
6. **Eligibility / reuse.** Team size limits? Can we **adapt an existing public dataset** we already maintain, or must data be net-new? Any prior-work restriction?
7. **Phase/category mapping.** Confirm which phase each target category is in — the welcome email and the official page disagree (e.g. "math and code" appears in Part 1 in the email, Part 2 on the page).
8. **Credits & compute.** How do we claim the "~1000 in credits for data adaptation and free compute," and what are the compute caps / time limits?

**Category-specific (only for the one we pick):**
9. **"language"** category — which **languages are "supported by Adaption"**, and does multilingual / low-resource adaptation qualify?

> These map 1:1 onto messages to post in Discord. Paste answers back into `strategy/answers.md` (create when we have them) and update `FINDINGS.md` where they change the picture.

---

## 2. What we can do NOW (not blocked on Discord answers)

- **Confirm registration state.** We received "You're In," so the entry exists. Double-check whether the `share.hsforms.com/22aXHNrCbQ8qEI_UOJgFVrwuc9yb` form needs anything else (team name, category pre-declaration).
- **Stand up the publishing accounts** required for any submission: a **Hugging Face** account/org and a **Kaggle** account, since *both* are mandatory destinations for the dataset + weights. Zero downside, needed regardless of category.
- **Inventory our data assets** (see §3) — the single biggest determinant of which category is winnable.
- **Smoke-test a finetuning loop** on a throwaway task so we know our pipeline end-to-end before the real run (can start even before confirming whether AutoScientist is mandatory).
- **Join + lurk the Discord** to see what categories other entrants are crowding into (thin field = easier per-category prize).

---

## 3. Category decision matrix (the main lever)

Prizes are **per category** (10 separate $4k firsts), so we only need to be best in **one**. Pick on: *(domain/data edge) × (estimated competition) × (data availability) × (deadline fit)*.

The decisive input is **our own assets**. Based on the existing body of work (multilingual Wikidata/knowledge-graph tooling, lexeme/lexicography work on Wikibase, constructed-language data, Japanese-religion text corpora, genealogy datasets), the categories where we plausibly have an unusual edge:

| Category | Phase* | Our edge | Competition (guess) | Notes |
|---|---|---|---|---|
| **language** | TBD (confirm) | **High** — lexeme data, multilingual Wikidata, conlang corpora, Japanese text | Medium–High | Strong fit *if* low-resource / multilingual adaptation qualifies. Q9. |
| **data visualization / chart interpretation** | Part 2 | Medium | Medium | Have structured-data pipelines; chart-interp is a model task, less of a data edge |
| **all other domains** | Part 2 | **High (flexibility)** | Unknown | Catch-all — lets us bring a niche dataset we already own (genealogy, religious-text classification) where there may be *no* competition |
| math & code | TBD (confirm) | Low | High | Crowded; no special edge |
| science / agriculture / finance / healthcare / legal / marketing | mixed | Low | Varies | No standout asset |

\*Confirm phase via Q7 — email vs. page disagree.

**Working recommendation (pre-Discord):** target **"language"** (highest genuine edge) as the primary, with **"all other domains"** as a fallback to weaponize a niche dataset we already own against a likely-thin field. Lock the choice only after Q1/Q2/Q9 are answered.

---

## 4. Immediate next actions

1. Get into Discord (tab opened) and post questions §1 (blocking four first).
2. Create/confirm Hugging Face + Kaggle accounts.
3. Draft the data-asset inventory to firm up the §3 matrix.
4. Record answers → `strategy/answers.md`; then lock category and decompose the build into `queue.md`.
