from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import crud
from .. import schemas

router = APIRouter(
    prefix="/complaints",
    tags=["Complaints"]
)


@router.post("/", response_model=schemas.ComplaintResponse)
def create(
        complaint: schemas.ComplaintCreate,
        db: Session = Depends(get_db)
):
    return crud.create_complaint(db, complaint)


@router.get("/", response_model=list[schemas.ComplaintResponse])
def all_complaints(
        db: Session = Depends(get_db)
):
    return crud.get_all_complaints(db)


@router.get("/{complaint_id}",
            response_model=schemas.ComplaintResponse)
def one_complaint(
        complaint_id: int,
        db: Session = Depends(get_db)
):

    complaint = crud.get_complaint(
        db,
        complaint_id
    )

    if complaint is None:

        raise HTTPException(
            status_code=404,
            detail="Complaint Not Found"
        )

    return complaint


@router.put("/{complaint_id}")
def update_status(
        complaint_id: int,
        update: schemas.ComplaintUpdate,
        db: Session = Depends(get_db)
):

    complaint = crud.update_status(
        db,
        complaint_id,
        update.status
    )

    if complaint is None:

        raise HTTPException(
            status_code=404,
            detail="Complaint Not Found"
        )

    return complaint


@router.delete("/{complaint_id}")
def delete(
        complaint_id: int,
        db: Session = Depends(get_db)
):

    complaint = crud.delete_complaint(
        db,
        complaint_id
    )

    if complaint is None:

        raise HTTPException(
            status_code=404,
            detail="Complaint Not Found"
        )

    return {
        "message": "Complaint Deleted"
    }