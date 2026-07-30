def genuine_score(description):
    text = description.lower()
    fake = [
        "test",
        "hello",
        "abc",
        "checking",
        "dummy"
    ]
    for word in fake:
        if word in text:
            return 15.0
    return 95.0
