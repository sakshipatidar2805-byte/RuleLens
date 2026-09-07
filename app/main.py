from .decision import evaluate_attendance
from .ingestion import load_rules
from .retrieval import retrieve_rules
from .utils import parse_attendance, parse_boolean


def run_rulelens(
    attendance: str,
    medical: str = "no",
    medical_approved: str = "no",
):
    attendance_value = parse_attendance(attendance)
    medical_value = parse_boolean(medical)
    medical_approved_value = parse_boolean(medical_approved)

    rules = load_rules()

    query = (
        f"attendance {attendance_value} percent "
        f"medical {medical_value} approved {medical_approved_value}"
    )

    relevant_rules = retrieve_rules(
        query=query,
        rules=rules,
        top_k=5,
    )

    decision = evaluate_attendance(
        attendance=attendance_value,
        medical=medical_value,
        medical_approved=medical_approved_value,
        supporting_rules=relevant_rules,
    )

    return decision


def print_decision(decision):
    print("\n" + "=" * 60)
    print("RULELENS ATTENDANCE DECISION")
    print("=" * 60)

    print(f"\nStatus: {decision.status}")
    print(f"Eligible: {'YES' if decision.eligible else 'NO'}")

    print("\nExplanation:")
    print(decision.explanation)

    if decision.warnings:
        print("\nWarnings:")
        for warning in decision.warnings:
            print(f"- {warning}")

    print("\nSupporting Rules:")

    if not decision.supporting_rules:
        print("- No matching rules found.")
    else:
        for item in decision.supporting_rules:
            print(
                f"- {item.rule.section}: "
                f"{item.rule.title} "
                f"(score: {item.score:.2f})"
            )

    print("=" * 60)


if __name__ == "__main__":
    print("Welcome to RuleLens")
    print("University Attendance Rule Decision System")

    attendance = input("\nEnter attendance percentage: ")
    medical = input("Do you have a medical circumstance? (yes/no): ")
    medical_approved = input(
        "Is the medical circumstance documented and approved? (yes/no): "
    )

    try:
        result = run_rulelens(
            attendance=attendance,
            medical=medical,
            medical_approved=medical_approved,
        )

        print_decision(result)

    except ValueError as error:
        print(f"\nInput Error: {error}")

    except FileNotFoundError as error:
        print(f"\nFile Error: {error}")