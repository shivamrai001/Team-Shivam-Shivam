import shutil

from fastapi import UploadFile

from .file_helper import (
    generate_filename,
    get_file_path
)


def save_image(image: UploadFile):

    filename = generate_filename(
        image.filename
    )

    path = get_file_path(
        filename
    )

    with open(path, "wb") as buffer:

        shutil.copyfileobj(
            image.file,
            buffer
        )

    return filename


def delete_image(path: str):

    import os

    if os.path.exists(path):

        os.remove(path)