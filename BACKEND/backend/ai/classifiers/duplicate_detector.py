import re

# Sample complaints
EXISTING_COMPLAINTS = [
    {
        "id": 1,
        "description": "Large pothole near VIT Bhopal Gate 1"
    },
    {
        "id": 2,
        "description": "Garbage overflowing near hospital"
    },
    {
        "id": 3,
        "description": "Street light not working on Main Road"
    }
]


def clean_text(text):
    words = re.findall(r"\w+", text.lower())
    return set(words)


def detect_duplicate(new_description):

    new_words = clean_text(new_description)

    best_score = 0
    best_match = None

    for complaint in EXISTING_COMPLAINTS:

        old_words = clean_text(complaint["description"])

        common = len(new_words & old_words)
        total = len(new_words | old_words)

        score = round((common / total) * 100)

        if score > best_score:
            best_score = score
            best_match = complaint

    if best_score >= 50:
        return (
            True,
            best_score,
            best_match["id"],
            best_match["description"]
        )

    return (
        False,
        best_score,
        None,
        None
    )