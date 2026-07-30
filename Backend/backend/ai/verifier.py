import random


def verify_image(image_path: str):

    score = random.uniform(70, 100)

    verified = score >= 80

    return {
        "verified": verified,
        "score": round(score, 2)
    }