from src.extract_shinto import make_qa_pairs


def test_shrine_record_generates_expected_pairs():
    rec = {
        "kind": "shrine",
        "name": "Test Shrine",
        "deities": ["Amaterasu"],
        "admins": ["Kyoto"],
        "countries": ["Japan"],
        "types": ["Shinto shrine", "grand shrine"],
        "coord": "Point(135.5 35.0)",
    }
    by_q = {p["instruction"]: p["output"] for p in make_qa_pairs(rec)}
    assert by_q["Which kami (deity) is enshrined at Test Shrine?"] == "Amaterasu"
    assert by_q["Where is Test Shrine located?"] == "Kyoto"
    assert by_q["What are the coordinates of Test Shrine?"] == "35.0000, 135.5000"
    assert "grand shrine" in by_q["What type of religious site is Test Shrine?"]
    assert by_q["What is Test Shrine?"] == "Test Shrine is a Shinto shrine located in Kyoto, Japan."


def test_kami_record_generates_genealogy_pairs():
    rec = {
        "kind": "kami",
        "name": "Amaterasu",
        "native": "天照大神",
        "parents": ["Izanagi"],
        "children": ["Ame-no-Oshihomimi"],
    }
    by_q = {p["instruction"]: p["output"] for p in make_qa_pairs(rec)}
    assert by_q["What is Amaterasu?"] == "Amaterasu is a kami (deity) in Shinto."
    assert by_q["Who are the parents of Amaterasu in Japanese mythology?"] == "Izanagi"
    assert by_q["Who are the children of Amaterasu in Japanese mythology?"] == "Ame-no-Oshihomimi"
    assert by_q["What is the Japanese name of Amaterasu?"] == "天照大神"


def test_seed_record_uses_description():
    rec = {"kind": "seed", "name": "Kojiki", "description": "oldest extant chronicle in Japan", "authors": ["Ō no Yasumaro"]}
    by_q = {p["instruction"]: p["output"] for p in make_qa_pairs(rec)}
    assert by_q["What is Kojiki?"] == "oldest extant chronicle in Japan"
    assert by_q["Who wrote Kojiki?"] == "Ō no Yasumaro"


def test_bare_record_still_has_description_and_skips_missing_facts():
    rec = {"kind": "shrine", "name": "Bare Shrine", "deities": [], "admins": [], "countries": [], "types": [], "coord": ""}
    qs = {p["instruction"] for p in make_qa_pairs(rec)}
    assert "What is Bare Shrine?" in qs
    assert "Where is Bare Shrine located?" not in qs
    assert not any("coordinates" in q for q in qs)


def test_bad_coordinate_is_skipped_gracefully():
    rec = {"kind": "shrine", "name": "X", "deities": [], "admins": [], "countries": [], "types": [], "coord": "garbage"}
    assert not any("coordinates" in p["instruction"] for p in make_qa_pairs(rec))
