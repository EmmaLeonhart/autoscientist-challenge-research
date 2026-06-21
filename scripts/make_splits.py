"""Read the full QA jsonl and write entity-level train/test splits to results/.

  python scripts/make_splits.py --in results/shinto_qa.full.jsonl --outdir results --test-frac 0.15
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.dataset import split_by_entity  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="infile", default="results/shinto_qa.full.jsonl")
    ap.add_argument("--outdir", default="results")
    ap.add_argument("--test-frac", type=float, default=0.15)
    args = ap.parse_args()

    rows = [json.loads(l) for l in open(args.infile, encoding="utf-8")]
    train, test = split_by_entity(rows, test_frac=args.test_frac)

    os.makedirs(args.outdir, exist_ok=True)
    for name, part in (("train", train), ("test", test)):
        with open(os.path.join(args.outdir, f"{name}.jsonl"), "w", encoding="utf-8") as f:
            for r in part:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

    train_q = {r["qid"] for r in train}
    test_q = {r["qid"] for r in test}
    assert train_q.isdisjoint(test_q), "entity leakage between splits!"
    print(f"train: {len(train)} pairs / {len(train_q)} entities")
    print(f"test:  {len(test)} pairs / {len(test_q)} entities")
    print(f"entity leakage: {len(train_q & test_q)} (must be 0)")


if __name__ == "__main__":
    main()
