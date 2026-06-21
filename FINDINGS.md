# Findings — What is the AutoScientist Challenge, and what did I sign up for?

**Question:** I got a "You're In" email from Adaption and I'm confused about how it works. What is this thing?

**Short answer:** You're registered for the **AutoScientist Challenge**, a four-week open competition run by **Adaption Labs** (the startup from ex-Cohere leaders Sara Hooker and Sudip Roy). You compete by **finetuning an AI model in one category, beating a baseline on Adaption's hidden test set, and open-sourcing both your dataset and your model weights** to Hugging Face *and* Kaggle. Prizes are **$50,000 total, awarded per category** (10× $4k, 10× $1k, 30 honorary mentions). The email you got is just the "you're in, go post about it" onboarding mail — it does **not** contain the rules, which is why it felt confusing.

---

## What the email actually was

A HubSpot-sent onboarding email from `team@adaptionlabs.ai` (2026-06-17), subject *"You're In. Now share with the world."* It does three things and nothing more: (1) confirms you're competing, (2) gives you social-media cards to share, (3) lists quick reminders (prize pool, the two parts, the open-source-to-Kaggle/HF + credit-Adaptive-Data requirement, a Discord link). It is **marketing collateral, not the rulebook.** The real mechanics live on the challenge page. (Redacted copy + parsed text in `data_lake/email/`.)

> ⚠️ One discrepancy to be aware of: the email's domain split doesn't perfectly match the official challenge page (e.g. the email puts "math and code" in Part 1; the official page puts it in Part 2). **Trust the challenge page and confirm in Discord.**

## How the competition actually works

- **Shape:** 4 weeks = two consecutive 2-week phases. **Register once**, submit to either or both.
  - **Part 1** — Jun 8 → **Jul 5**, winners Jul 13. Categories (per official page): Finance, healthcare, language, legal, marketing.
  - **Part 2** — Jul 6 → Aug 3, winners Aug 10. Categories: Science, agriculture, data visualization & chart interpretation, math & code, all other domains.
- **A valid submission = four things:**
  1. Pick **one** of the ten categories.
  2. **Open-source** the *adapted dataset* you finetuned on **and** the *trained weights* — to **both Hugging Face and Kaggle**, crediting *Adaptive Data by Adaption*.
  3. Show a **measurable % improvement over a baseline model on Adaption's held-out, in-house test set** (they grade you on data you never see).
  4. *(Bonus)* demo + social posts tagging @adaption_ai / adaption-labs.
- **Prizes ($50,000):** 10× **$4,000** firsts (one per category) · 10× **$1,000** runners-up · 30 honorary mentions (swag & credits).
- **They give you:** ~"1000 in credits for data adaptation and free compute," a Discord, and sessions with their research team.

## What you're really being asked to build

Adaption sells two products and the challenge is a showcase for them:
- **Adaptive Data** — tooling that *generates/refines the training data* on the fly.
- **AutoScientist** — tooling that *auto-runs the training loop*, co-optimizing data + recipe until the model converges ("idea to an owned model in an afternoon").

So the intended loop is: **use Adaptive Data to build a strong finetuning set → use AutoScientist to train a model that beats the baseline in your chosen category → publish dataset + weights.** The credits they hand out strongly imply they expect you to use their stack (confirm whether it's required vs. merely encouraged).

## Where today (2026-06-20) sits in the timeline

Part 1 is **live** and closes **Jul 5** (~2 weeks out). Part 2 runs Jul 6 – Aug 3. So there's a near-term window if you want to target a Part-1 category, and a second, less time-pressured shot in Part 2.

## The actual lever for placing: category selection

Because prizes are awarded **per category** (ten separate $4k firsts), you do **not** have to be the best entrant overall — only the best in **one** category. The highest-leverage decision is therefore picking a category where you have domain leverage *and* the entrant field is likely thin, rather than fighting in a crowded one. That choice, plus resolving the open rule-questions below, is the strategy work tracked in `todo.md`.

## Open questions to resolve before committing (→ `todo.md`)

1. Per category: what *is* the held-out test set, and what baseline model must you beat?
2. Is using AutoScientist / Adaptive Data **required** or just encouraged?
3. Dataset/weights licensing + eligibility fine print.
4. Confirm which phase each target category is actually in (email vs. page mismatch).
5. How to claim the credits + free compute, and any compute caps.

*Sources for every claim above: `literature/REVIEW.md` (S1–S5).*
