"""Extract Shinto-shrine facts from Wikidata (CC0) and emit instruction/QA pairs.

This is the DATASET pipeline — the part of the AutoScientist submission we build
ourselves. The model itself is trained by AutoScientist from this dataset; here we
turn Wikidata's structured shrine facts into the finetuning data.

Source: Wikidata Query Service. Data is CC0 (public domain), so the produced dataset
is freely releasable to Hugging Face + Kaggle (challenge requirement).

Usage:
  python src/extract_shrines.py --limit 200 --out data_lake/wikidata/shrine_qa.sample.jsonl
"""
from __future__ import annotations
import argparse
import json
import requests

WDQS = "https://query.wikidata.org/sparql"
UA = "AutoScientist-ShrineResearch/0.1 (immanuelleleonhart@gmail.com)"

# One row per shrine; value labels resolved in-query so no second lookup is needed.
SHRINE_QUERY = """
SELECT ?shrine ?sLabel
  (GROUP_CONCAT(DISTINCT ?deityL; separator=" | ") AS ?deities)
  (GROUP_CONCAT(DISTINCT ?adminL; separator=" | ") AS ?admins)
  (GROUP_CONCAT(DISTINCT ?countryL; separator=" | ") AS ?countries)
  (GROUP_CONCAT(DISTINCT ?typeL; separator=" | ") AS ?types)
  (SAMPLE(?coord) AS ?coordinate)
WHERE {
  ?shrine wdt:P31/wdt:P279* wd:Q845945 .
  ?shrine rdfs:label ?sLabel . FILTER(LANG(?sLabel) = 'en')
  OPTIONAL { ?shrine wdt:P825 ?deity.   ?deity   rdfs:label ?deityL.   FILTER(LANG(?deityL)='en') }
  OPTIONAL { ?shrine wdt:P131 ?admin.   ?admin   rdfs:label ?adminL.   FILTER(LANG(?adminL)='en') }
  OPTIONAL { ?shrine wdt:P17  ?country. ?country rdfs:label ?countryL. FILTER(LANG(?countryL)='en') }
  OPTIONAL { ?shrine wdt:P31  ?type.    ?type    rdfs:label ?typeL.    FILTER(LANG(?typeL)='en') }
  OPTIONAL { ?shrine wdt:P625 ?coord. }
}
GROUP BY ?shrine ?sLabel
LIMIT %d OFFSET %d
"""


def fetch(limit, offset=0, timeout=120):
    r = requests.get(
        WDQS,
        params={"query": SHRINE_QUERY % (limit, offset), "format": "json"},
        headers={"User-Agent": UA, "Accept": "application/sparql-results+json"},
        timeout=timeout,
    )
    r.raise_for_status()
    return r.json()["results"]["bindings"]


def row_to_record(b):
    g = lambda k: b.get(k, {}).get("value", "")
    split = lambda k: [x for x in g(k).split(" | ") if x]
    return {
        "qid": g("shrine").split("/")[-1],
        "name": g("sLabel"),
        "deities": split("deities"),
        "admins": split("admins"),
        "countries": split("countries"),
        "types": split("types"),
        "coord": g("coordinate"),
    }


def make_qa_pairs(rec):
    """Pure function: one shrine record -> list of {instruction, input, output} dicts.

    Pure (no I/O) so it can be unit-tested without hitting the network.
    """
    name = rec["name"]
    pairs = []

    def add(q, a):
        if a:
            pairs.append({"instruction": q, "input": "", "output": a})

    desc = f"{name} is a Shinto shrine"
    if rec["admins"]:
        desc += f" located in {rec['admins'][0]}"
    if rec["countries"]:
        desc += f", {rec['countries'][0]}"
    add(f"What is {name}?", desc + ".")

    add(f"Which kami (deity) is enshrined at {name}?", ", ".join(rec["deities"]))
    add(f"Where is {name} located?", ", ".join(rec["admins"]))

    types = [t for t in rec["types"] if t.lower() != "shinto shrine"] or rec["types"]
    add(f"What type of religious site is {name}?", ", ".join(types))

    if rec["coord"]:
        try:
            lon, lat = rec["coord"].replace("Point(", "").replace(")", "").split()
            add(f"What are the coordinates of {name}?", f"{float(lat):.4f}, {float(lon):.4f}")
        except ValueError:
            pass
    return pairs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=200)
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--out", default="data_lake/wikidata/shrine_qa.sample.jsonl")
    args = ap.parse_args()

    rows = fetch(args.limit, args.offset)
    n_shrines = n_pairs = 0
    with open(args.out, "w", encoding="utf-8") as f:
        for b in rows:
            rec = row_to_record(b)
            if not rec["name"]:
                continue
            n_shrines += 1
            for qa in make_qa_pairs(rec):
                qa["qid"] = rec["qid"]
                f.write(json.dumps(qa, ensure_ascii=False) + "\n")
                n_pairs += 1
    print(f"shrines: {n_shrines}  qa_pairs: {n_pairs}  -> {args.out}")


if __name__ == "__main__":
    main()
