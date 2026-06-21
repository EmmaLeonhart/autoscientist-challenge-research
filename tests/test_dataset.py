from src.dataset import split_by_entity, score_pair, evaluate, normalize


def _rows():
    rows = []
    for i in range(200):
        qid = f"Q{i}"
        for j in range(3):
            rows.append({"qid": qid, "kind": "shrine", "instruction": f"q{i}-{j}", "output": "a"})
    return rows


def test_split_has_no_entity_leakage():
    train, test = split_by_entity(_rows(), test_frac=0.2)
    train_q = {r["qid"] for r in train}
    test_q = {r["qid"] for r in test}
    assert train_q and test_q
    assert train_q.isdisjoint(test_q)  # an entity is never in both splits


def test_split_is_deterministic_and_roughly_sized():
    rows = _rows()
    a = split_by_entity(rows, test_frac=0.2)
    b = split_by_entity(rows, test_frac=0.2)
    assert [r["qid"] for r in a[1]] == [r["qid"] for r in b[1]]  # stable
    frac = len(a[1]) / len(rows)
    assert 0.1 < frac < 0.3  # ~0.2


def test_score_exact_contains_and_multipart():
    assert score_pair("Amaterasu", "Amaterasu") == 1.0
    assert score_pair("It is Amaterasu.", "Amaterasu") == 1.0          # contained
    assert score_pair("Izanagi and Izanami", "Izanagi, Izanami") == 1.0  # all parts
    assert score_pair("Susanoo", "Amaterasu") == 0.0                    # wrong
    assert score_pair("", "Amaterasu") == 0.0


def test_evaluate_accuracy():
    items = [
        {"output": "Kyoto", "prediction": "Kyoto"},
        {"output": "Kyoto", "prediction": "Tokyo"},
    ]
    assert evaluate(items) == 0.5
    assert evaluate([]) == 0.0


def test_normalize_handles_fullwidth_space_and_case():
    assert normalize("  Amaterasu　Ōmikami ") == "amaterasu ōmikami"
