def assign_department(category: str) -> str:

    mapping = {

        "Garbage": "Municipal Corporation",

        "Road": "PWD Department",

        "Water": "Water Supply Department",

        "Electricity": "Electricity Board",

        "Environment": "Forest Department",

        "Other": "General Administration"

    }

    return mapping.get(
        category,
        "General Administration"
    )