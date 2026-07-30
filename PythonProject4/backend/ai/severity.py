def calculate_severity(category, description):

    score = 20

    text = description.lower()

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

    emergency = [
        "accident",
        "danger",
        "hospital",
        "fire",
        "school",
        "children"
    ]

    for word in emergency:
        if word in text:
            score += 10

    return min(score, 100)