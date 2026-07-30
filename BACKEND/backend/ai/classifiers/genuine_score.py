def calculate_trust_score(
    category_score,
    priority_score,
    spam,
    duplicate,
    image_valid
):
    score = 0

    # Category Score (20%)
    score += category_score * 0.20

    # Priority Score (20%)
    score += priority_score * 0.20

    # Spam Check (25%)
    score += 25 if not spam else 0

    # Duplicate Check (15%)
    score += 15 if not duplicate else 5

    # Image Validation (20%)
    score += 20 if image_valid else 15

    score = round(score)

    if score >= 90:
        status = "Verified"
    elif score >= 70:
        status = "Needs Review"
    else:
        status = "Rejected"

    return score, status