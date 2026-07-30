from fastapi import HTTPException


ALLOWED_EXTENSIONS = [
    "jpg",
    "jpeg",
    "png"
]


MAX_SIZE = 5 * 1024 * 1024


def validate_extension(filename: str):

    extension = filename.split(".")[-1].lower()

    if extension not in ALLOWED_EXTENSIONS:

        raise HTTPException(
            status_code=400,
            detail="Only JPG, JPEG and PNG are allowed."
        )


def validate_size(size: int):

    if size > MAX_SIZE:

        raise HTTPException(
            status_code=400,
            detail="Image size should be less than 5MB."
        )