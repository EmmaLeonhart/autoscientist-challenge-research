"""Entry point: build the Shinto-shrine QA dataset from Wikidata.

Default builds a small SAMPLE (one network page) so it is cheap and CI-safe.
Use --full to paginate the full ~25k English-labelled shrines.

  python scripts/run.py                 # sample -> data_lake/wikidata/shrine_qa.sample.jsonl
  python scripts/run.py --full --out results/shrine_qa.full.jsonl
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.extract_shrines import fetch, row_to_record, make_qa_pairs  # noqa: E402


def build(out, full, page=500, cap=None):
    n_shrines = n_pairs = 0
    offset = 0
    with open(out, "w", encoding="utf-8") as f:
        while True:
            rows = fetch(page if full else 200, offset)
            if not rows:
                break
            for b in rows:
                rec = row_to_record(b)
                if not rec["name"]:
                    continue
                n_shrines += 1
                for qa in make_qa_pairs(rec):
                    qa["qid"] = rec["qid"]
                    f.write(json.dumps(qa, ensure_ascii=False) + "\n")
                    n_pairs += 1
            if not full:
                break
            offset += page
            if cap and n_shrines >= cap:
                break
    print(f"shrines: {n_shrines}  qa_pairs: {n_pairs}  -> {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--full", action="store_true", help="paginate all shrines (network-heavy)")
    ap.add_argument("--cap", type=int, default=None, help="stop after N shrines (for --full)")
    ap.add_argument("--out", default="data_lake/wikidata/shrine_qa.sample.jsonl")
    args = ap.parse_args()
    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    build(args.out, args.full, cap=args.cap)


if __name__ == "__main__":
    main()
