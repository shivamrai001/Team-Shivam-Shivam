def genuine_score(description: str) -> float:

    text = description.lower().strip()

    fake_words = [
        "test",
        "hello",
        "abc",
        "checking",
        "dummy",
        "sample",
        "random"
    ]

    # Fake complaint detected
    if any(word in text for word in fake_words):
        return 15.0

    score = 50.0

    # Longer descriptions are generally more genuine
    if len(text) > 30:
        score += 15

    if len(text) > 80:
        score += 15

    if len(text) > 150:
        score += 10

    # More detailed complaints
    detail_words = [
        "road",
        "garbage",
        "water",
        "electric",
        "location",
        "urgent",
        "danger",
        "broken"
    ]

    for word in detail_words:
        if word in text:
            score += 2

    return min(score, 100.0)