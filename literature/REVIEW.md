# Literature Review — How the AutoScientist Challenge works

**Research question:** How does the Adaption Labs AutoScientist Challenge work, and what is a concrete strategy to place in it?

This review synthesizes the sources in `sources.md` (S1–S5). Its job is to answer the "what's going on with it" confusion before any strategy work.

## 1. Who is running it

**Adaption Labs** is an AI research startup founded in 2025 by **Sara Hooker** (co-founder/CEO, ex-VP AI Research at Cohere) and **Sudip Roy** (both ex-Cohere), reportedly with a $50M seed [S5]. Its thesis is *adaptation*: gradient-free, inference-time techniques that sit above base models so a small/cheap model "grows into" a specialized role without expensive retraining [S5]. The challenge is a marketing + ecosystem-seeding event for two of their products.

## 2. The two products you need to understand

- **Adaptive Data** — shapes the *inputs*. AI systems treat the dataset as dynamic and malleable, generating/refining the data they need instead of relying on a fixed corpus; claimed avg +82% data quality in early deployments [S4]. This is the "Adaptive Data by Adaption" that submissions must credit.
- **AutoScientist** — shapes the *model*. It automates the full research loop behind training/alignment, co-optimizing the dataset and the training recipe in lockstep until the model converges — "idea to an owned, adapted model in an afternoon" [S2]. Adaption claims ~35% over expert-tuned training (win rates 48%→64%) [S2]; TechCrunch quotes a "more than doubled win rates" claim but flags it's hard to contextualize because it targets bespoke tasks, not public benchmarks like SWE-Bench/ARC-AGI [S3].

The pipeline is **Adaptive Data → AutoScientist**: refine the data, then auto-train the model [S2].

## 3. The challenge mechanics (the part the email didn't explain)

The welcome email in `data_lake/` only says "you're in, go share it." The actual rules live on the challenge page [S1]:

- **Format:** A four-week competition split into two consecutive two-week phases. **Register once**; submit to either or both phases.
- **Ten categories**, with prizes awarded **per category**:
  - *Part 1 (Jun 8 – Jul 5, winners Jul 13):* Finance, healthcare, language, legal, marketing.
  - *Part 2 (Jul 6 – Aug 3, winners Aug 10):* Science, agriculture, data visualization & chart interpretation, math & code, all other domains.
  - (Note: the welcome email's domain split differs slightly from the official page — e.g. the email lists "math and code" under Part 1; the official page lists it under Part 2. **Treat the challenge page [S1] as authoritative** and confirm in Discord.)
- **A submission has four parts** [S1]:
  1. **Pick one category.**
  2. **Open-source release:** publish *both* the **adapted dataset** used for finetuning *and* the **trained model weights** to **both Hugging Face and Kaggle**.
  3. **Measurable win:** the final model must show a **measurable % improvement over a baseline model on Adaption's held-out, in-house test sets** — i.e. *they* score you on data you don't see.
  4. **Bonus:** demos + social posts tagging @adaption_ai / adaption-labs.
- **Prizes ($50,000):** 10× **$4,000** first prizes (one per category) · 10× **$1,000** runners-up · 30 honorary mentions (swag & credits) [S1].
- **Provided:** "1000 in credits for data adaptation and free compute," a Discord, and sessions with Adaption's research team [S1].

## 4. What this means in practice (the gap → strategy)

The competition is essentially: **use Adaption's Adaptive Data + AutoScientist tooling to finetune a model in one category, beat a baseline on their hidden test set, and open-source the dataset + weights.** Because prizes are *per category* (10 firsts), the realistic path to placing is **category selection** — pick a category where (a) you have domain leverage and (b) the field of entrants is thin — rather than competing head-to-head in a crowded one.

**Key unknowns to resolve before committing (Discord / rules):**
- What exactly are the held-out test sets per category, and what's the baseline model you must beat?
- Are you required to use AutoScientist/Adaptive Data, or just allowed to? (The credits strongly imply intended use.)
- Licensing/eligibility constraints on the dataset and weights you publish.
- Which phase a given category actually falls in (email vs. page discrepancy above).

These unknowns become the first items of `todo.md` (the strategy horizon).
