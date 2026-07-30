from typing import Tuple

CATEGORY_KEYWORDS = {
    "Road": [
        "pothole",
        "road",
        "crack",
        "street",
        "highway",
        "bridge",
        "footpath"
    ],

    "Garbage": [
        "garbage",
        "trash",
        "waste",
        "dustbin",
        "overflow",
        "dump"
    ],

    "Water": [
        "water",
        "leak",
        "pipe",
        "drain",
        "sewage",
        "flood"
    ],

    "Electricity": [
        "street light",
        "light",
        "electric",
        "wire",
        "pole",
        "transformer"
    ],

    "Public Safety": [
        "accident",
        "fire",
        "crime",
        "danger",
        "tree fallen"
    ]
}


def classify_category(description: str) -> Tuple[str, float]:
    """
    Returns:
        category
        confidence
    """

    text = description.lower()

    for category, keywords in CATEGORY_KEYWORDS.items():

        for keyword in keywords:

            if keyword in text:
                return category, 95
    return "Other", 60