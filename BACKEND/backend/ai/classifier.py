def classify(description: str):
    text = description.lower()
    if any(word in text for word in [
        "garbage",
        "waste",
        "dustbin",
        "trash"
    ]):
        return "Garbage"
    elif any(word in text for word in [
        "road",
        "pothole",
        "street",
        "highway"
    ]):
        return "Road"
    elif any(word in text for word in [
        "water",
        "pipe",
        "leak",
        "drain"
    ]):
        return "Water"
    elif any(word in text for word in [
        "light",
        "electric",
        "pole"
    ]):
        return "Electricity"
    elif any(word in text for word in [
        "tree",
        "park",
        "forest"
    ]):
        return "Environment"
    return "Other"
