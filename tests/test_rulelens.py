from app.decision import evaluate_attendance
from app.ingestion import load_rules
from app.retrieval import retrieve_rules


def test_rules_loaded():
    rules = load_rules()

    assert len(rules) == 10


def test_normal_eligibility():
    decision = evaluate_attendance(80)

    assert decision.eligible is True
    assert decision.status == "Eligible"


def test_medical_concession():
    decision = evaluate_attendance(
        attendance=70,
        medical=True,
        medical_approved=True,
    )

    assert decision.eligible is True
    assert decision.status == "Eligible under Medical Concession"


def test_medical_not_approved():
    decision = evaluate_attendance(
        attendance=70,
        medical=True,
        medical_approved=False,
    )

    assert decision.eligible is False
    assert decision.status == "Not Eligible"


def test_low_attendance():
    decision = evaluate_attendance(60)

    assert decision.eligible is False
    assert decision.status == "Not Eligible"


def test_rule_retrieval():
    rules = load_rules()

    results = retrieve_rules(
        "minimum attendance requirement examination eligibility",
        rules,
    )

    assert len(results) > 0