from typing import List

from .models import Decision, RetrievedRule


def evaluate_attendance(
    attendance: float,
    medical: bool = False,
    medical_approved: bool = False,
    supporting_rules: List[RetrievedRule] | None = None,
) -> Decision:

    supporting_rules = supporting_rules or []
    warnings = []

    if attendance >= 75:
        return Decision(
            eligible=True,
            status="Eligible",
            explanation=(
                f"Attendance is {attendance:.2f}%, which meets the "
                "minimum requirement of 75% for examination eligibility."
            ),
            supporting_rules=supporting_rules,
            warnings=warnings,
        )

    if attendance >= 65 and medical and medical_approved:
        return Decision(
            eligible=True,
            status="Eligible under Medical Concession",
            explanation=(
                f"Attendance is {attendance:.2f}%. It is below the normal "
                "75% requirement, but it meets the 65% medical concession "
                "threshold because the medical circumstance is documented "
                "and approved."
            ),
            supporting_rules=supporting_rules,
            warnings=warnings,
        )

    if attendance >= 65:
        warnings.append(
            "Medical concession requires a properly documented and approved "
            "medical circumstance."
        )

    return Decision(
        eligible=False,
        status="Not Eligible",
        explanation=(
            f"Attendance is {attendance:.2f}%, which is below the applicable "
            "eligibility threshold."
        ),
        supporting_rules=supporting_rules,
        warnings=warnings,
    )