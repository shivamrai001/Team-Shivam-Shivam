import re

SPAM_WORDS = [
    "test",
    "asdf",
    "qwerty",
    "hello",
    "abc",
    "dummy"
]

def detect_spam(description: str):

    text = description.lower().strip()

    # Empty complaint
    if len(text) == 0:
        return True, "Empty Complaint"

    # Too short
    if len(text) < 10:
        return True, "Description Too Short"

    # Spam words
    for word in SPAM_WORDS:
        if word == text:
            return True, "Spam Keyword"

    # Repeated characters
    if re.fullmatch(r"(.)\1{4,}", text):
        return True, "Repeated Characters"

    # Only numbers
    if text.isdigit():
        return True, "Only Numbers"

    return False, "Valid Complaint"