from fastapi import FastAPI
from pydantic import BaseModel

from classifiers.category_classifier import classify_category
from classifiers.priority_classifier import classify_priority
from classifiers.spam_detector import detect_spam
from classifiers.duplicate_detector import detect_duplicate
from classifiers.image_validator import validate_image
from classifiers.genuine_score import calculate_trust_score

app = FastAPI(
    title="UrbanSense AI",
    version="2.0"
)

class Complaint(BaseModel):
    description: str
    image_path: str


@app.get("/")
def home():
    return {
        "message": "UrbanSense AI Running 🚀"
    }


@app.post("/classify")
def classify(complaint: Complaint):

    category = classify_category(complaint.description)
    priority = classify_priority(complaint.description)
    spam = detect_spam(complaint.description)
    duplicate = detect_duplicate(complaint.description)
    image = validate_image(complaint.image_path)

    trust_score = calculate_trust_score(
        category_score=category[1],
        priority_score=priority[1],
        spam=spam[0],
        duplicate=duplicate[0],
        image_valid=image[0]
    )

    return {
        "description": complaint.description,

        "category": category[0],
        "category_score": category[1],

        "priority": priority[0],
        "priority_score": priority[1],

        "spam": spam[0],
        "spam_reason": spam[1],

        "duplicate": duplicate[0],
        "similarity_score": duplicate[1],

        "image_valid": image[0],
        "image_status": image[1],

        "trust_score": trust_score[0],
        "status": trust_score[1]
    }