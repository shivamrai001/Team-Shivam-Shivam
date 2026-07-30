def get_priority(severity: float) -> str:

    if severity >= 90:
        return "Emergency"

    elif severity >= 75:
        return "Critical"

    elif severity >= 60:
        return "High"

    elif severity >= 40:
        return "Medium"

    return "Low"