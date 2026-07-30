from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


# -----------------------------
# Get All Users
# -----------------------------
@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


# -----------------------------
# Get All Complaints
# -----------------------------
@router.get("/complaints")
def get_all_complaints(db: Session = Depends(get_db)):
    return db.query(models.Complaint).all()


# -----------------------------
# Update Complaint Status
# -----------------------------
@router.put("/complaints/{complaint_id}")
def update_status(
    complaint_id: int,
    status: str,
    db: Session = Depends(get_db)
):

    complaint = db.query(models.Complaint).filter(
        models.Complaint.id == complaint_id
    ).first()

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    complaint.status = status

    db.commit()
    db.refresh(complaint)

    return {
        "message": "Complaint status updated",
        "complaint": complaint
    }


# -----------------------------
# Delete Complaint
# -----------------------------
@router.delete("/complaints/{complaint_id}")
def delete_complaint(
    complaint_id: int,
    db: Session = Depends(get_db)
):

    complaint = db.query(models.Complaint).filter(
        models.Complaint.id == complaint_id
    ).first()

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    db.delete(complaint)
    db.commit()

    return {
        "message": "Complaint deleted successfully"
    }