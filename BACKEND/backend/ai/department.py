def assign_department(category):
    #assigning different works to different govt. organizations
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
