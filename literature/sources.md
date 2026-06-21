# Sources — AutoScientist Challenge research

One entry per source: the claim/what it contributes, plus the citation. Used to build `REVIEW.md`.

---

### S1 — AutoScientist Challenge (official challenge page)
- **What it contributes:** The authoritative mechanics. Register once; submit to either or both two-week phases inside the four-week window. **Submission = (a) an *adapted dataset* used for finetuning + (b) the *trained model weights*, both released to BOTH Hugging Face and Kaggle, (c) a *measurable % improvement vs a baseline model on Adaption's held-out in-house test sets*, plus (d) optional bonus demo/social engagement.** Ten categories, one prize each.
- **Prize:** $50,000 total — 10× $4,000 first prizes (one per category), 10× $1,000 runners-up, 30 honorary mentions (swag & credits).
- **Parts:** Part 1 Jun 8–Jul 5 (Finance, healthcare, language, legal, marketing; winners Jul 13). Part 2 Jul 6–Aug 3 (Science, agriculture, data viz/chart interpretation, math & code, all other domains; winners Aug 10).
- **Resources:** "1000 in credits for data adaptation and free compute," Discord, sessions with the research team.
- **Citation:** Adaption Labs, "AutoScientist Challenge: Bring Frontier AI to the World." https://adaptionlabs.ai/blog/autoscientist-challenge

### S2 — AutoScientist (product page)
- **What it contributes:** What the tool you compete *with* actually is. AutoScientist "self-improves and automates the full research loop behind model training and alignment," co-optimizing data and training configs in lockstep until the model converges — "from idea to an owned, adapted model in an afternoon, not weeks." Claims it outperforms expert human-configured training by ~35% on average (win rates 48% → 64%).
- **Relationship to Adaptive Data:** Adaptive Data shapes the *inputs* (training data); AutoScientist shapes the *model*. Sequential: Adaptive Data refines data → AutoScientist trains. "From Adaptive Data to Adaptive Systems."
- **Citation:** Adaption Labs, "AutoScientist: Automating the Science of Model Training." https://adaptionlabs.ai/blog/autoscientist

### S3 — TechCrunch (independent reporting)
- **What it contributes:** Outside validation + a skeptical note. AutoScientist automates finetuning by co-optimizing data and model; built on the existing Adaptive Data offering; free for 30 days post-release. Co-founder/CEO **Sara Hooker** (ex-VP AI research at Cohere). Hooker claims it "more than doubled win rates," but TechCrunch notes the figure is "difficult to put into context" since it targets specific tasks, not standard benchmarks (SWE-Bench, ARC-AGI).
- **Citation:** TechCrunch, "Adaption aims big with AutoScientist, an AI tool that helps models train themselves," 2026-05-13. https://techcrunch.com/2026/05/13/adaption-aims-big-with-autoscientist-an-ai-tool-that-helps-models-train-themselves/

### S4 — Adaptive Data (beta launch)
- **What it contributes:** Defines "Adaptive Data by Adaption" (the thing submissions must credit). AI systems treat the data space as dynamic/malleable, generating/refining the data they need rather than relying on static pretraining corpora; claimed avg 82% increase in data quality across early deployments.
- **Citation:** Adaption Labs, "Adaptive Data: Designed for Change." https://www.adaptionlabs.ai/blog/adaption-launches-adaptive-data-beta

### S5 — Company background
- **What it contributes:** Who is running this. Adaption Labs founded 2025 by **Sara Hooker** and **Sudip Roy** (both ex-Cohere); mission "thinking machines that adapt and continuously learn"; reported $50M seed. Three pillars including adaptive data; gradient-free, inference-time adaptation that sits above base models.
- **Citation:** creati.ai, "Adaption Labs Secures $50M Seed Funding…," 2026-02-04. https://creati.ai/ai-news/2026-02-04/adaption-labs-50m-seed-funding-adaptive-ai-models/ ; The Data Exchange interview with Sudip Roy, https://thedataexchange.media/sudip-roy-adaptation/
