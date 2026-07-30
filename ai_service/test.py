from classifiers.category_classifier import classify_category
from classifiers.priority_classifier import classify_priority
from classifiers.spam_detector import detect_spam
from classifiers.duplicate_detector import detect_duplicate
from classifiers.image_validator import validate_image
from classifiers.genuine_score import calculate_trust_score


# -----------------------------
# Get Complaint from User
# -----------------------------
text = input("Enter Complaint: ")

# -----------------------------
# Image Path
# -----------------------------
image_path = "uploads/road.jpg"

# -----------------------------
# AI Modules
# -----------------------------
category = classify_category(text)

priority = classify_priority(text)

spam = detect_spam(text)

duplicate = detect_duplicate(text)

image = validate_image(image_path)

# -----------------------------
# Trust Score
# -----------------------------
image_valid = image[0]

trust_score = calculate_trust_score(
    category_score=category[1],
    priority_score=priority[1],
    spam=spam[0],
    duplicate=duplicate[0],
    image_valid=image_valid
)

# -----------------------------
# Final Result
# -----------------------------
print("\n" + "=" * 45)
print("        SMART CITY AI RESULT")
print("=" * 45)

print(f"Complaint          : {text}")

print(f"\nCategory           : {category[0]}")
print(f"Category Score     : {category[1]}")

print(f"\nPriority           : {priority[0]}")
print(f"Priority Score     : {priority[1]}")

print(f"\nSpam               : {spam[0]}")
print(f"Spam Reason        : {spam[1]}")

print(f"\nDuplicate          : {duplicate[0]}")
print(f"Similarity Score   : {duplicate[1]}")

if duplicate[0]:
    print(f"Matched Complaint  : {duplicate[3]}")

print(f"\nImage Valid        : {image[0]}")
print(f"Image Status       : {image[1]}")

print("\n" + "-" * 45)
print(f"Trust Score        : {trust_score[0]}/100")
print(f"Status             : {trust_score[1]}")
print("=" * 45)