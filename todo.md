# todo.md — long-horizon plan (abstract destinations)

The understanding pass is done (`FINDINGS.md`, `literature/REVIEW.md`). This file is the **strategy horizon**: abstract goals, decomposed into concrete `queue.md` steps when worked. Items only flow forward (here → `queue.md` → `devlog.md`).

## A. Resolve the open rule-questions (blocks any real commitment)
- Join the challenge Discord; confirm: per-category held-out test set + baseline model; whether AutoScientist/Adaptive Data is required vs. encouraged; dataset/weights licensing + eligibility; which phase each target category is in (email-vs-page mismatch); how to claim credits/compute and any caps.
- Capture answers into `literature/` and update `FINDINGS.md` where they change the picture.

## B. Choose a category to target (the main lever)
- Prizes are per-category → pick where (a) domain leverage is highest and (b) the entrant field is likely thinnest.
- Build a short decision matrix over the 10 categories: personal/domain edge × estimated competition × data availability × phase deadline. Recommend one Part-1 and one Part-2 candidate.

## C. Stand up the tooling
- Get an Adaption account + the credits; set up Hugging Face and Kaggle accounts/orgs for the dual open-source release.
- Smoke-test the Adaptive Data → AutoScientist loop on a throwaay task end-to-end so the mechanics are known before the real run.

## D. Build the submission for the chosen category
- Assemble/adapt the finetuning dataset; run AutoScientist to beat the baseline on the held-out set; iterate until there's a measurable, defensible % gain.
- Release dataset + weights to BOTH Hugging Face and Kaggle, crediting Adaptive Data by Adaption; write the demo + social posts (the bonus).

## E. Publish the research report
- Keep `FINDINGS.md` + the themed `docs/` GitHub Pages site current: what the challenge is, the strategy chosen and why, the submission, and the measured result.

---
*Pull the top unblocked item into `queue.md`, decompose into concrete steps, mirror into the task tool, execute. Item **A** is the natural next concrete queue once the user wants to proceed past "understand."*
