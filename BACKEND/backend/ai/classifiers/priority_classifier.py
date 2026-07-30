from typing import Tuple

PRIORITY_RULES = {
    "Critical": [
        "fire",
        "accident",
        "gas leak",
        "electric shock",
        "building collapse",
        "flood",
        "explosion"
    ],

    "High": [
        "pothole",
        "water leakage",
        "water leak",
        "open manhole",
        "sewage",
        "street light",
        "broken pole",
        "tree fallen"
    ],

    "Medium": [
        "garbage",
        "overflowing garbage",
        "dustbin",
        "drain",
        "traffic"
    ],

    "Low": [
        "bench",
        "park",
        "painting",
        "sign board",
        "cleaning"
    ]
}


def classify_priority(description: str) -> Tuple[str, float]:

    text = description.lower()

    for priority, keywords in PRIORITY_RULES.items():

        for keyword in keywords:

            if keyword in text:
                return priority, 95

    return "Medium", 60