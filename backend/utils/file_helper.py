import os
import uuid


UPLOAD_FOLDER = "backend/upload"


def generate_filename(filename: str):

    extension = filename.split(".")[-1]

    unique_name = f"{uuid.uuid4()}.{extension}"

    return unique_name


def get_file_path(filename: str):

    return os.path.join(
        UPLOAD_FOLDER,
        filename
    )