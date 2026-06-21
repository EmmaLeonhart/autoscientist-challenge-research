"""Entry point: build the broad **Shinto** QA dataset from Wikidata.

Default builds a small SAMPLE across all entity kinds (cheap, CI-safe). Use --full to
paginate the large kinds (shrines ~25k, kami ~1.8k).

  python scripts/run.py                       # sample -> data_lake/wikidata/shinto_qa.sample.jsonl
  python scripts/run.py --full --out results/shinto_qa.full.jsonl
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.extract_shinto import fetch, make_qa_pairs  # noqa: E402

# (kind, paginate?) — 'seed' is a fixed small set, the rest paginate under --full.
KINDS = [("shrine", True), ("kami", True), ("seed", False)]


def build(out, full, page=500, cap=None):
    n_ent = n_pairs = 0
    with open(out, "w", encoding="utf-8") as f:
        for kind, paginate in KINDS:
            offset = 0
            while True:
                recs = fetch(kind, page if (full and paginate) else 100, offset)
                if not recs:
                    break
                for rec in recs:
                    if not rec["name"]:
                        continue
                    n_ent += 1
                    for qa in make_qa_pairs(rec):
                        qa["qid"] = rec["qid"]
                        qa["kind"] = rec["kind"]
                        f.write(json.dumps(qa, ensure_ascii=False) + "\n")
                        n_pairs += 1
                if not (full and paginate):
                    break
                offset += page
                if cap and offset >= cap:
                    break
    print(f"entities: {n_ent}  qa_pairs: {n_pairs}  -> {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--full", action="store_true", help="paginate the large kinds (network-heavy)")
    ap.add_argument("--cap", type=int, default=None, help="stop each paginated kind after N offset")
    ap.add_argument("--out", default="data_lake/wikidata/shinto_qa.sample.jsonl")
    args = ap.parse_args()
    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    build(args.out, args.full, cap=args.cap)


if __name__ == "__main__":
    main()
