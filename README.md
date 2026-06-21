# autoscientist-challenge-research

> A **research project** scaffolded with
> [cleanvibe](https://github.com/Immanuelle/cleanvibe) `research`.

**Research question:** How does the Adaption Labs AutoScientist Challenge work, and what is a concrete strategy to place in it?

## About

This project started from one confusing email: a *"You're In. Now share with the
world."* onboarding mail from **Adaption Labs**. It works out what the
**AutoScientist Challenge** actually is and how to place in it.

**What it is (short version):** a four-week, **$50,000**, **per-category** open
competition. You finetune a model in one of ten categories, show a measurable
improvement over a baseline on Adaption's **held-out test set**, and open-source
**both the adapted dataset and the trained weights to Hugging Face *and* Kaggle**.
Prizes: 10× $4k firsts (one per category), 10× $1k runners-up, 30 honorary mentions.
Because prizes are per category, the decisive lever is **category selection**.

- The plain-language answer: **`FINDINGS.md`**.
- The evidence base: **`literature/REVIEW.md`** (+ `sources.md`).
- The source email (redacted): **`data_lake/email/`**.
- The strategy track: **`todo.md`**.

## Status

Understanding pass **complete** (what the challenge is, how submissions/judging
work, the timeline). Next phase is strategy: resolve open rule-questions in Discord,
pick a target category, and build a submission. Part 1 closes **Jul 5, 2026**;
Part 2 runs **Jul 6 – Aug 3**.

## How it's organized

- `literature/` — the literature review (sources + `REVIEW.md`), built first.
- `data_lake/` — datasets and supplied material.
- `src/` — the research code; `scripts/run.py` — the run entry point.
- `results/` — run outputs (gitignored). `FINDINGS.md` — the write-up.
- `docs/` — the published GitHub Pages report site (themed) + built PDF.
- `queue.md` / `todo.md` / `devlog.md` — the cleanvibe work loop.

## Getting started

```
cd autoscientist-challenge-research
claude
```

Then work `queue.md` top to bottom. The bootstrap sequence pins down the
research question with you, runs the literature review, plans the experiments,
takes the repo public, and keeps the report current as results land.

## Published report

Once the repo is public with Pages set to **Source: GitHub Actions**,
`.github/workflows/pages.yml` deploys `docs/` (the report site) and builds
`docs/report.pdf`. Site-shape inspiration: http://latent-space.emmaleonhart.com/
