from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import os
import shutil
import uuid

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

UPLOAD_FOLDER = "backend/upload"

   try:
       os.makedirs(UPLOAD_FOLDER, exist_ok=True)
   except OSError:
       pass


# ==========================================
# Upload Image
# ==========================================

@router.post("/image")
async def upload_image(file: UploadFile = File(...)):

    allowed_extensions = ["jpg", "jpeg", "png"]

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file selected."
        )

    extension = file.filename.split(".")[-1].lower()

    if extension not in allowed_extensions:

        raise HTTPException(
            status_code=400,
            detail="Only JPG, JPEG and PNG images are allowed."
        )

    filename = f"{uuid.uuid4()}.{extension}"

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    with open(filepath, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": filename,
        "image_path": filepath
    }


# ==========================================
# View Image
# ==========================================

@router.get("/{filename}")
def get_image(filename: str):

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    if not os.path.exists(filepath):

        raise HTTPException(
            status_code=404,
            detail="Image not found."
        )

    return FileResponse(filepath)


# ==========================================
# Delete Image
# ==========================================

@router.delete("/{filename}")
def delete_image(filename: str):

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    if not os.path.exists(filepath):

        raise HTTPException(
            status_code=404,
            detail="Image not found."
        )

    os.remove(filepath)

    return {
        "message": "Image deleted successfully."
    }
