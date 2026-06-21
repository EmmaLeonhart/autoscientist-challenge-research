"""Train/test split (by entity) and a fact-matching scorer for the Shinto QA set.

Two jobs:
  * `split_by_entity` — hold out a fraction of *entities* (not pairs), so every QA pair
    of a held-out entity lands wholly in the test set. This prevents leakage: the model
    must answer about shrines/kami it never saw in training, which is what "measurable
    improvement over the base model on a held-out set" actually requires.
  * `score_pair` / `evaluate` — a simple, transparent fact-match score so we can measure
    base-vs-finetuned lift ourselves before the platform's internal eval.
"""
from __future__ import annotations
import hashlib
import re


def _bucket(qid, mod=1000):
    return int(hashlib.sha1(qid.encode()).hexdigest()[:8], 16) % mod


def split_by_entity(rows, test_frac=0.15, mod=1000):
    """Deterministically split rows so an entity's pairs never straddle train/test.

    Bucketing on a hash of qid means the split is stable across runs and independent
    of row order. Returns (train, test).
    """
    cut = int(test_frac * mod)
    train, test = [], []
    for r in rows:
        (test if _bucket(r["qid"], mod) < cut else train).append(r)
    return train, test


_WS = re.compile(r"\s+")


def normalize(s):
    return _WS.sub(" ", (s or "").replace("　", " ").strip().lower())


def score_pair(prediction, gold):
    """1.0 if the gold answer is matched, else 0.0.

    Credit an exact normalized match, gold contained in the prediction (the model may
    add words), or — for multi-answer gold like "A, B" — all parts present.
    """
    p, g = normalize(prediction), normalize(gold)
    if not g:
        return 0.0
    if p == g or g in p:
        return 1.0
    parts = [normalize(x) for x in gold.split(",") if x.strip()]
    if len(parts) > 1 and all(part in p for part in parts):
        return 1.0
    return 0.0


def evaluate(items):
    """items: iterable of dicts with 'output' (gold) and 'prediction'. Returns accuracy."""
    items = list(items)
    if not items:
        return 0.0
    return sum(score_pair(i.get("prediction", ""), i["output"]) for i in items) / len(items)
