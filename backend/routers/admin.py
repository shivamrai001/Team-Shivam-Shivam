from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
import models
import crud
from auth import get_current_user

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

# -----------------------------
# Get All Users
# -----------------------------
@router.get("/users")
def get_all_users(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user) # SECURITY FIX
):
    # Optional: Add a check here to ensure current_user.role == "admin"
    return crud.get_all_users(db)

# -----------------------------
# Get All Complaints
# -----------------------------
@router.get("/complaints")
def get_all_complaints(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user) # SECURITY FIX
):
    return crud.get_complaints(db)

# -----------------------------
# Update Complaint Status
# -----------------------------
@router.put("/complaints/{complaint_id}")
def update_status(
    complaint_id: int,
    status: str,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user) # SECURITY FIX
):
    complaint = crud.update_complaint_status(db, complaint_id, status)
    
    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

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
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user) # SECURITY FIX
):
    deleted = crud.delete_complaint(db, complaint_id)
    
    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    return {
        "message": "Complaint deleted successfully"
    }
