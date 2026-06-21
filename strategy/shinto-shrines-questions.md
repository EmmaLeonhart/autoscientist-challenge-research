# Open questions — "All Other Domains: Shinto shrines" submission

Questions we will have / need answered to actually build and submit a Shinto-shrines
model in the All Other Domains track. Split into: **(A) must-ask Adaption** (only they
can answer — Discord #support / weekly Research Hour), **(B) decisions we make
ourselves** (task framing + data), and **(C) risks to watch**.

Context for every answer: rules in `strategy/answers.md`; locked choice in `decision.md`.

---

## A. Must-ask Adaption (Discord #support / Research Hour)

**Evaluation — the biggest unknown for a custom niche domain:**
1. For an **All Other Domains** entry with a self-chosen topic (Shinto shrines), **how is it evaluated?** Is there a held-out test set, and **who builds it** — Adaption, or do we supply our own held-out split?
2. The FAQ says "other tracks follow the same principle" as Language (LLM-as-judge win rates vs a base model). **For an arbitrary domain, is it also LLM-as-judge on general competence, or task-specific metrics?** What exactly is the judge comparing?
3. "Improvement over **the base model you train on**" — concretely, do we (a) pick a base model, (b) train an adapted version, and (c) they compare adapted-vs-base on their/our held-out set? Confirm the loop.
4. How is **dataset quality** scored (it "factors in")? Is there a rubric, or is it judged qualitatively?
5. Any minimum bar — e.g. a required margin of improvement, or a minimum dataset size?

**Platform / models:**
6. Which **base models** are available/allowed in AutoScientist, and are there size limits? Any recommended default for a knowledge-heavy text domain?
7. Does the AutoScientist UI support **bring-your-own dataset**, or must data be generated through Adaptive Data's adaptation loop? If BYO, what **format** (instruction/response pairs? raw text? QA?) and how is it ingested?
8. Is **multimodal** (shrine images) usable/scored here, or stick to text? (Images modality was recently added.)
9. Practical export: confirm the **HF + Kaggle export** flow for dataset *and* weights (settings → api_keys → connect → approve). Any gotchas reported for Kaggle export?

**Submission / logistics:**
10. When does the **Part 2 submission form** open (Part 2 starts Jul 6), and is it the same multiple-submissions-allowed flow?
11. For All Other Domains specifically, do we need to **declare/scope the domain** anywhere so the judges know what they're evaluating?
12. Confirm the **1,000 credits** are on the account (not the 50 free-tier) and whether they're enough for a full train + iterations.

---

## B. Decisions we make ourselves (resolve before building)

**Task framing — what does the model actually *do*?** Pick the capability we adapt for; this determines the dataset shape and what "improvement" means:
- (a) **Factual QA** about shrines (kami enshrined, rank, location, founding, festivals).
- (b) **Structured extraction / classification** (shrine → type, deity, Engishiki status, prefecture, rank).
- (c) **Description generation** (generate accurate shrine descriptions from structured facts).
- (d) **Multilingual** shrine knowledge (Japanese ⇄ English ⇄ others), leaning on our multilingual Wikidata labels.
- *Working lean:* instruction-tuned **factual QA + description** on shrines, because it's the most LLM-judge-friendly framing of "general competence in this domain." Reconsider after A.1–A.4.

**Data selection (what we own → what we can release):**
- Inventory the usable sources: **Wikidata shrine entities (CC0 ✅)**, shrine wiki text (license? CC-BY-SA — attribution needed), Engishiki / Shikinai-ronsha records, Kokugakuin shrine DB references (**licensing? may be restricted — verify before any release**), shrine genealogies.
- **Only include data we can publicly re-release** (open license + attribution). Flag and exclude anything from a restricted source; Wikidata (CC0) is the safe backbone.
- Decide dataset size + train/holdout split (in case we must supply our own eval).
- How to convert structured Wikidata/shrine records into the training format the platform wants (see A.7).

**Scope of "Shinto shrines":** keep it tight ("Shinto shrines") or broaden to "Japanese religious sites / cultural heritage" so the eval has more surface area and the model looks more generally competent? Decide once A.1–A.2 clarify how niche topics are judged.

---

## C. Risks to watch
- **Eval mismatch:** if Adaption builds a generic held-out set and our model overfits to shrine trivia, "general competence" may not move. Mitigate by training for broad, well-grounded shrine knowledge, not memorized edge cases.
- **License contamination:** a single restricted source (e.g. a scraped DB) in the released dataset could disqualify it. Keep provenance per record; default to CC0/CC-BY data.
- **Deadline:** Part 2 closes Aug 3; the form opens Jul 6. Plenty of runway, but the eval questions (A) gate the dataset design — ask them in the first Research Hour.
- **Platform constraints:** AutoScientist training is UI-only right now; budget time for manual runs and the 1,000-credit cap.
