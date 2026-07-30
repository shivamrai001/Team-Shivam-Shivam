import os


def verify_image(image_path: str) -> dict:

    if not image_path:
        return {
            "verified": False,
            "score": 0.0
        }

    if os.path.exists(image_path):
        return {
            "verified": True,
            "score": 95.0
        }

    return {
        "verified": False,
        "score": 0.0
    }