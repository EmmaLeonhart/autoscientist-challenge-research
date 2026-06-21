# Decision — locked category

**Category:** All Other Domains (Part 2)
**Topic:** **Shinto** (broad) — kami/deities, shrines, texts (Kojiki, Nihon Shoki, Engishiki), festivals, sects, concepts. Not limited to shrines.
**Data:** **Wikidata-only (CC0)**, built **self-contained** here (reusing latent-space-cartography's seed-and-traverse pattern; not depending on Loka / latent-space-cartography).
**Locked:** 2026-06-20 by the user.

## Why
- **All Other Domains** is the Part 2 catch-all, so a niche domain is allowed and is evaluated in its own track (prizes per track).
- **Shinto** is where we have an unusually deep data edge: the maintainer's whole ecosystem (the Claw4S "Wikidata for Shinto Studies" work, latent-space-cartography, Loka) already orbits this domain. Broadening past shrines to kami + texts gives the model more "general competence" surface for the judge.
- **Deadline:** Part 2 closes **Aug 3, 2026** (form opens Jul 6) — more runway than the Language track's Jul 5.

## Key constraints carried from the rules (`strategy/answers.md`)
- Release the **adapted dataset + model weights to BOTH Hugging Face and Kaggle**, crediting *Adaptive Data by Adaption*.
- Must show **measurable improvement over the base model you train on** on Adaption's internal held-out test set; **dataset quality also factors in**.
- Data must be under an **open license permitting public release + attribution** (CC-BY-NC acceptable).
- Training runs via **AutoScientist (UI)**; 1,000 challenge credits.

## Next
The open questions that must be resolved before/while building are in **`strategy/shinto-shrines-questions.md`**. The build is decomposed in `queue.md`.
