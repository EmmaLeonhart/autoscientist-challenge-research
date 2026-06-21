"""Extract broad **Shinto** facts from Wikidata (CC0) and emit instruction/QA pairs.

This is the DATASET pipeline — the part of the AutoScientist submission we build
ourselves; AutoScientist trains the model from the dataset we produce here.

Scope is the Shinto domain, not just shrines: **shrines** (Q845945), **kami / deities**
(Q524158), and a curated set of **texts & concepts** (Kojiki, Nihon Shoki, Engishiki,
Shinto itself, ...). The extraction borrows the seed-and-traverse pattern from
latent-space-cartography's `random_walk.py` but stays self-contained here.

All Wikidata statement data is CC0 → the dataset is freely releasable to HF + Kaggle.

Usage:
  python src/extract_shinto.py --kind shrine --limit 200 --out data_lake/wikidata/shinto_qa.sample.jsonl
"""
from __future__ import annotations
import argparse
import json
import time
import requests

WDQS = "https://query.wikidata.org/sparql"
UA = "AutoScientist-ShintoResearch/0.2 (immanuelleleonhart@gmail.com)"

# Curated Shinto texts & concepts (seed list — extend freely).
SEED_ENTITIES = [
    "Q1342448",  # Engishiki
    "Q533996",   # Kojiki
    "Q695225",   # Nihon Shoki
    "Q1011402",  # Shinto
    "Q524158",   # kami
    "Q845945",   # Shinto shrine
]

SHRINE_QUERY = """
SELECT ?e ?eLabel
  (GROUP_CONCAT(DISTINCT ?deityL; separator=" | ") AS ?deities)
  (GROUP_CONCAT(DISTINCT ?adminL; separator=" | ") AS ?admins)
  (GROUP_CONCAT(DISTINCT ?countryL; separator=" | ") AS ?countries)
  (GROUP_CONCAT(DISTINCT ?typeL; separator=" | ") AS ?types)
  (SAMPLE(?coord) AS ?coordinate)
WHERE {
  ?e wdt:P31/wdt:P279* wd:Q845945 .
  ?e rdfs:label ?eLabel . FILTER(LANG(?eLabel) = 'en')
  OPTIONAL { ?e wdt:P825 ?deity.   ?deity   rdfs:label ?deityL.   FILTER(LANG(?deityL)='en') }
  OPTIONAL { ?e wdt:P131 ?admin.   ?admin   rdfs:label ?adminL.   FILTER(LANG(?adminL)='en') }
  OPTIONAL { ?e wdt:P17  ?country. ?country rdfs:label ?countryL. FILTER(LANG(?countryL)='en') }
  OPTIONAL { ?e wdt:P31  ?type.    ?type    rdfs:label ?typeL.    FILTER(LANG(?typeL)='en') }
  OPTIONAL { ?e wdt:P625 ?coord. }
}
GROUP BY ?e ?eLabel
ORDER BY ?e
LIMIT %d OFFSET %d
"""

KAMI_QUERY = """
SELECT ?e ?eLabel ?native
  (GROUP_CONCAT(DISTINCT ?parentL; separator=" | ") AS ?parents)
  (GROUP_CONCAT(DISTINCT ?childL;  separator=" | ") AS ?children)
WHERE {
  ?e wdt:P31/wdt:P279* wd:Q524158 .
  ?e rdfs:label ?eLabel . FILTER(LANG(?eLabel) = 'en')
  OPTIONAL { ?e wdt:P1559 ?native. }
  OPTIONAL { ?e (wdt:P22|wdt:P25) ?parent. ?parent rdfs:label ?parentL. FILTER(LANG(?parentL)='en') }
  OPTIONAL { ?e wdt:P40 ?child.            ?child  rdfs:label ?childL.  FILTER(LANG(?childL)='en') }
}
GROUP BY ?e ?eLabel ?native
ORDER BY ?e
LIMIT %d OFFSET %d
"""

SEED_QUERY = """
SELECT ?e ?eLabel ?eDescription
  (GROUP_CONCAT(DISTINCT ?authorL; separator=" | ") AS ?authors)
  (SAMPLE(?inception) AS ?date)
WHERE {
  VALUES ?e { %s }
  ?e rdfs:label ?eLabel . FILTER(LANG(?eLabel) = 'en')
  OPTIONAL { ?e schema:description ?eDescription . FILTER(LANG(?eDescription)='en') }
  OPTIONAL { ?e wdt:P50 ?author. ?author rdfs:label ?authorL. FILTER(LANG(?authorL)='en') }
  OPTIONAL { ?e wdt:P571 ?inception. }
}
GROUP BY ?e ?eLabel ?eDescription
"""


def _get(b, k):
    return b.get(k, {}).get("value", "")


def _split(b, k):
    return [x for x in _get(b, k).split(" | ") if x]


def _query(q, timeout=180, retries=5):
    """Query WDQS with backoff. WDQS throttles heavy queries with 429/502/503/504;
    retry those with exponential backoff instead of crashing the whole run.
    """
    last = None
    for attempt in range(retries):
        try:
            r = requests.get(
                WDQS, params={"query": q, "format": "json"},
                headers={"User-Agent": UA, "Accept": "application/sparql-results+json"},
                timeout=timeout,
            )
            if r.status_code in (429, 502, 503, 504):
                raise requests.HTTPError(f"{r.status_code} {r.reason}")
            r.raise_for_status()
            return r.json()["results"]["bindings"]
        except (requests.RequestException, ValueError) as e:
            last = e
            if attempt < retries - 1:
                time.sleep(3 * (2 ** attempt))  # 3, 6, 12, 24s
    raise last


def fetch(kind, limit=200, offset=0):
    if kind == "shrine":
        rows = _query(SHRINE_QUERY % (limit, offset))
        return [{
            "kind": "shrine", "qid": _get(b, "e").split("/")[-1], "name": _get(b, "eLabel"),
            "deities": _split(b, "deities"), "admins": _split(b, "admins"),
            "countries": _split(b, "countries"), "types": _split(b, "types"),
            "coord": _get(b, "coordinate"),
        } for b in rows]
    if kind == "kami":
        rows = _query(KAMI_QUERY % (limit, offset))
        return [{
            "kind": "kami", "qid": _get(b, "e").split("/")[-1], "name": _get(b, "eLabel"),
            "native": _get(b, "native"), "parents": _split(b, "parents"), "children": _split(b, "children"),
        } for b in rows]
    if kind == "seed":
        values = " ".join(f"wd:{q}" for q in SEED_ENTITIES)
        rows = _query(SEED_QUERY % values)
        return [{
            "kind": "seed", "qid": _get(b, "e").split("/")[-1], "name": _get(b, "eLabel"),
            "description": _get(b, "eDescription"), "authors": _split(b, "authors"),
            "date": _get(b, "date"),
        } for b in rows]
    raise ValueError(f"unknown kind: {kind}")


def make_qa_pairs(rec):
    """Pure function: one Shinto entity record -> list of {instruction, input, output}.

    Dispatches on rec['kind'] (shrine | kami | seed). Pure (no I/O) for unit tests.
    """
    kind = rec.get("kind", "shrine")
    name = rec["name"]
    pairs = []

    def add(q, a):
        if a:
            pairs.append({"instruction": q, "input": "", "output": a})

    if kind == "shrine":
        desc = f"{name} is a Shinto shrine"
        if rec.get("admins"):
            desc += f" located in {rec['admins'][0]}"
        if rec.get("countries"):
            desc += f", {rec['countries'][0]}"
        add(f"What is {name}?", desc + ".")
        add(f"Which kami (deity) is enshrined at {name}?", ", ".join(rec.get("deities", [])))
        add(f"Where is {name} located?", ", ".join(rec.get("admins", [])))
        types = [t for t in rec.get("types", []) if t.lower() != "shinto shrine"] or rec.get("types", [])
        add(f"What type of religious site is {name}?", ", ".join(types))
        if rec.get("coord"):
            try:
                lon, lat = rec["coord"].replace("Point(", "").replace(")", "").split()
                add(f"What are the coordinates of {name}?", f"{float(lat):.4f}, {float(lon):.4f}")
            except ValueError:
                pass

    elif kind == "kami":
        add(f"What is {name}?", f"{name} is a kami (deity) in Shinto.")
        add(f"Who are the parents of {name} in Japanese mythology?", ", ".join(rec.get("parents", [])))
        add(f"Who are the children of {name} in Japanese mythology?", ", ".join(rec.get("children", [])))
        if rec.get("native"):
            add(f"What is the Japanese name of {name}?", rec["native"])

    elif kind == "seed":
        add(f"What is {name}?", rec.get("description") or f"{name} is associated with Shinto.")
        add(f"Who wrote {name}?", ", ".join(rec.get("authors", [])))

    return pairs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kind", choices=["shrine", "kami", "seed"], default="shrine")
    ap.add_argument("--limit", type=int, default=200)
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--out", default="data_lake/wikidata/shinto_qa.sample.jsonl")
    args = ap.parse_args()

    recs = fetch(args.kind, args.limit, args.offset)
    n_ent = n_pairs = 0
    with open(args.out, "w", encoding="utf-8") as f:
        for rec in recs:
            if not rec["name"]:
                continue
            n_ent += 1
            for qa in make_qa_pairs(rec):
                qa["qid"] = rec["qid"]
                qa["kind"] = rec["kind"]
                f.write(json.dumps(qa, ensure_ascii=False) + "\n")
                n_pairs += 1
    print(f"kind={args.kind}  entities: {n_ent}  qa_pairs: {n_pairs}  -> {args.out}")


if __name__ == "__main__":
    main()
