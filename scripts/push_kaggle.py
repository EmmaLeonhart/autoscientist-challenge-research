"""Mirror the Shinto QA dataset to Kaggle (the challenge requires HF *and* Kaggle).

  python scripts/push_kaggle.py

Requires Kaggle API credentials in ~/.kaggle/kaggle.json (never committed). Releases CC0;
the dataset card credits Adaptive Data by Adaption.
"""
import argparse
import json
import os
import shutil

from kaggle.api.kaggle_api_extended import KaggleApi

FILES = [
    ("results/train.jsonl", "train.jsonl"),
    ("results/test.jsonl", "test.jsonl"),
    ("data_lake/wikidata/shinto_qa.sample.jsonl", "sample.jsonl"),
    ("data_lake/wikidata/dataset_stats.json", "dataset_stats.json"),
    ("data_lake/wikidata/HF_DATASET_CARD.md", "README.md"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--owner", default="emmaleonhart")
    ap.add_argument("--slug", default="shinto-wikidata-qa")
    ap.add_argument("--updir", default="results/kaggle_upload")
    args = ap.parse_args()

    os.makedirs(args.updir, exist_ok=True)
    for src, dst in FILES:
        if os.path.exists(src):
            shutil.copy(src, os.path.join(args.updir, dst))

    meta = {
        "title": "Shinto Wikidata QA",
        "id": f"{args.owner}/{args.slug}",
        "licenses": [{"name": "CC0-1.0"}],
        "subtitle": "Shinto (shrines, kami, texts) QA from Wikidata — AutoScientist Challenge",
    }
    json.dump(meta, open(os.path.join(args.updir, "dataset-metadata.json"), "w"), indent=2)

    api = KaggleApi()
    api.authenticate()
    api.dataset_create_new(folder=args.updir, public=True, dir_mode="skip")
    print("created:", f"https://www.kaggle.com/datasets/{args.owner}/{args.slug}")


if __name__ == "__main__":
    main()
