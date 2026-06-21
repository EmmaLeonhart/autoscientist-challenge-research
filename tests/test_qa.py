from src.extract_shrines import make_qa_pairs


def test_full_record_generates_expected_pairs():
    rec = {
        "name": "Test Shrine",
        "deities": ["Amaterasu"],
        "admins": ["Kyoto"],
        "countries": ["Japan"],
        "types": ["Shinto shrine", "grand shrine"],
        "coord": "Point(135.5 35.0)",
    }
    pairs = make_qa_pairs(rec)
    by_q = {p["instruction"]: p["output"] for p in pairs}

    assert by_q["Which kami (deity) is enshrined at Test Shrine?"] == "Amaterasu"
    assert by_q["Where is Test Shrine located?"] == "Kyoto"
    # coordinates parsed as "lat, lon"
    assert by_q["What are the coordinates of Test Shrine?"] == "35.0000, 135.5000"
    # the specific type is preferred over the generic "Shinto shrine"
    assert "grand shrine" in by_q["What type of religious site is Test Shrine?"]
    # descriptive pair grounds country + admin
    assert by_q["What is Test Shrine?"] == "Test Shrine is a Shinto shrine located in Kyoto, Japan."


def test_bare_record_still_has_description_and_skips_missing_facts():
    rec = {"name": "Bare Shrine", "deities": [], "admins": [], "countries": [], "types": [], "coord": ""}
    pairs = make_qa_pairs(rec)
    qs = {p["instruction"] for p in pairs}
    assert "What is Bare Shrine?" in qs
    # no fact -> no question minted for it
    assert "Where is Bare Shrine located?" not in qs
    assert not any("coordinates" in q for q in qs)


def test_bad_coordinate_is_skipped_gracefully():
    rec = {"name": "X", "deities": [], "admins": [], "countries": [], "types": [], "coord": "garbage"}
    pairs = make_qa_pairs(rec)
    assert not any("coordinates" in p["instruction"] for p in pairs)
