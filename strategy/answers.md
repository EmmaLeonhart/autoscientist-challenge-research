# Answers — rule-questions resolved from the Discord export + FAQ

Source material: the #autoscientist-challenge Discord channel export (2026-06-20, in
`data_lake/discord_export/`, raw gitignored) and the official FAQ doc "AutoScientist
Challenge Rules and Context" (`data_lake/discord_export/faq.txt`). Attributions are to
Adaption staff (Ross, Isabelle, Sudip, Vie, Wilson @ Adaption) and the FAQ.

## Blocking questions

**1. Held-out test set & baseline — how is "% improvement" measured?**
- **Baseline = the base model you train on, NOT a fixed external model** (FAQ Q4): *"Your model is evaluated relative to the baseline you train on… Dataset quality and held-out test set performance both factor into scoring."*
- **You do NOT see the held-out test sets — they're internal** (FAQ Q5).
- **Language track specifically: LLM-as-judge win rates against a base model on unseen tasks, scored on language competence** (FAQ Q5). Optimize *broadly for language quality*, not a single benchmark (FAQ Q6). Other tracks follow the same principle.
- Detailed evaluation guidance will be covered in the **first office hours / Research Hour** (weekly Google Meet) — Ross said the team will "go over all the rules and the guidance on the evaluations."

**2. Is AutoScientist / Adaptive Data required?**
- In practice **yes, you use their platform.** Ross (6-18): *"We do run the actual GPU training loop using the auto scientist selected parameters. However it is only available through the UI"* (API support is "coming soon"). The FAQ goal is to "use autoscientist," and the 1,000 credits are for "data adaptation + free compute" on their platform. So the intended/expected path is: adapt data → AutoScientist selects params + runs training → export.

**3. Allowed base models / constraints?**
- Not enumerated in the FAQ; you train relative to a base model on the platform. Image modality was recently added (Sudip linked `docs.adaptionlabs.ai/guides/multimodal-context/`). Confirm specific allowed base models in office hours / #support.

**4. How do you actually submit?**
- **Submit via a HubSpot form, one per part.** Part 1 form: `https://share.hsforms.com/2r5RTDl9lSrqTQmqhRhEsQwuc9yb` (Part 2 form shared when it opens).
- **You can submit multiple times** — just submit the form again (Ross, 6-19).
- Export your dataset + weights to Hugging Face and Kaggle from the app: `adaptionlabs.ai/app/settings?tab=api_keys` → connect Kaggle/HF → Update → Approve, then export (Ross).

## Important questions

**5. License requirements?** **CC-BY-NC is acceptable; any open license that permits public release + attribution works** (FAQ Q8).

**6. Eligibility / teams / data reuse?**
- **No limit on collaborators per team**, but you must designate a **team captain** who receives + distributes the prize (FAQ).
- **Can enter Part 1 and Part 2** and win in both; **can submit to multiple tracks** — prizes are per track, evaluated independently (FAQ Q1, Q2).

**7. Phase ↔ category mapping (email vs page discrepancy) — RESOLVED.**
- **Part 1 (live, closes JULY 5, winners July 13): Finance, Healthcare, *Language*, Legal, Marketing.**
- **Part 2 (Jul 6 – Aug 3, winners Aug 10): Science, Agriculture, Data Visualization, Math & Code, HR, All Other Domains.**
- So **"language" is a Part 1 category and closes July 5** — the welcome email was wrong to imply otherwise, and "math & code" is Part 2. (Note: FAQ also lists **HR**, a category not in the email.) The terms page also wrongly said June 22 — **July 5 is correct; blog + Discord take precedence** (FAQ Q9).

**8. Credits / compute?** Challenge credits = **1,000** for data adaptation + free compute. The **50 credits already in an account are the free tier, not the challenge** (FAQ Q3). If the 1,000 haven't landed, DM sign-up email to @ross.adaption or post in #support.

**9. "Language" category — which languages / what tasks?**
- Tasks: **optimize broadly for overall language competence**, judged by LLM-as-judge win rates vs a base model on unseen tasks (FAQ Q5/Q6) — not a single benchmark.
- Sudip flagged a **known issue with "mixed languages"** ("does look like an issue, we will investigate") — relevant if pursuing multilingual adaptation; confirm current state before relying on it.

## Net effect on strategy

- **Language is viable AND urgent: Part 1, deadline July 5 2026 (~2 weeks).** If targeting language, the timeline is tight and the build should start now.
- The language objective ("broad language competence, LLM-judged") rewards a **high-quality, broad finetuning dataset** over a narrow task hack — which suits owned multilingual/lexical corpora, *if* they raise general competence in the judged setting.
- Healthcare explicitly rewards **extra clinical metrics** (FAQ Q7) — a different, metrics-friendly angle if language proves a poor fit.
- Open the **#support** channel + attend the weekly **Research Hour** for the evaluation deep-dive before locking the dataset design.
