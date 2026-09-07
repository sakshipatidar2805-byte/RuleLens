def parse_attendance(value: str) -> float:
    """
    Convert attendance input into a valid percentage.
    """

    try:
        attendance = float(value)
    except (TypeError, ValueError):
        raise ValueError("Attendance must be a valid number.")

    if attendance < 0 or attendance > 100:
        raise ValueError("Attendance must be between 0 and 100.")

    return attendance


def parse_boolean(value: str) -> bool:
    """
    Convert common yes/no values into True or False.
    """

    value = str(value).strip().lower()

    if value in {"yes", "y", "true", "1"}:
        return True

    if value in {"no", "n", "false", "0"}:
        return False

    raise ValueError("Please enter yes/no.")