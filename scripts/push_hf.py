"""Publish the Shinto QA dataset to the Hugging Face Hub.

  python scripts/push_hf.py --repo EmmaLeonhart/shinto-wikidata-qa

Requires a logged-in HF token (huggingface-cli login / HF_TOKEN). Releases CC0; the
challenge requires the dataset on both Hugging Face and Kaggle, crediting Adaptive Data.
"""
import argparse
import os

from huggingface_hub import HfApi, create_repo


FILES = [
    ("results/train.jsonl", "train.jsonl"),
    ("results/test.jsonl", "test.jsonl"),
    ("data_lake/wikidata/shinto_qa.sample.jsonl", "sample.jsonl"),
    ("data_lake/wikidata/dataset_stats.json", "dataset_stats.json"),
    ("data_lake/wikidata/HF_DATASET_CARD.md", "README.md"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="EmmaLeonhart/shinto-wikidata-qa")
    ap.add_argument("--private", action="store_true")
    args = ap.parse_args()

    api = HfApi()
    create_repo(args.repo, repo_type="dataset", private=args.private, exist_ok=True)
    print("repo ready:", args.repo)

    for local, remote in FILES:
        if not os.path.exists(local):
            print(f"  [skip] {local} (missing)")
            continue
        api.upload_file(path_or_fileobj=local, path_in_repo=remote,
                        repo_id=args.repo, repo_type="dataset")
        print(f"  uploaded {local} -> {remote} ({os.path.getsize(local)//1024} KB)")

    print("done:", f"https://huggingface.co/datasets/{args.repo}")


if __name__ == "__main__":
    main()
