
def assign_department(category):

    mapping = {

        "Garbage": "Municipal Corporation",

        "Road": "PWD Department",

        "Water": "Water Supply Department",

        "Electricity": "Electricity Board",

        "Environment": "Forest Department"

    }

    return mapping.get(
        category,
        "General Administration"
    )