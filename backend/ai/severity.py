def calculate_severity(category: str, description: str) -> float:

    score = 20

    text = description.lower().strip()

    # Base score by category
    if category == "Road":
        score += 40

    elif category == "Garbage":
        score += 30

    elif category == "Water":
        score += 35

    elif category == "Electricity":
        score += 45

    elif category == "Environment":
        score += 25

    # Emergency keywords
    emergency = [
        "accident",
        "danger",
        "hospital",
        "fire",
        "school",
        "children",
        "urgent",
        "emergency",
        "collapse",
        "injury"
    ]

    for word in emergency:
        if word in text:
            score += 10

    return float(min(score, 100))