from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import crud, schemas, models
from ..auth import get_current_user

router = APIRouter(
    prefix="/complaints",
    tags=["Complaints"]
)


# =====================================================
# Create Complaint
# =====================================================

@router.post("/", response_model=schemas.ComplaintResponse)
def create_complaint(
    complaint: schemas.ComplaintCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    return crud.create_complaint(
        db=db,
        complaint=complaint,
        user_id=current_user.id
    )


# =====================================================
# Get All Complaints
# =====================================================

@router.get("/", response_model=list[schemas.ComplaintResponse])
def get_all_complaints(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    return crud.get_complaints(db)


# =====================================================
# Get Complaint By ID
# =====================================================

@router.get("/{complaint_id}", response_model=schemas.ComplaintResponse)
def get_single_complaint(
    complaint_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    complaint = crud.get_complaint(
        db,
        complaint_id
    )

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    return complaint


# =====================================================
# Update Complaint
# =====================================================

@router.put("/{complaint_id}", response_model=schemas.ComplaintResponse)
def update_complaint(
    complaint_id: int,
    complaint: schemas.ComplaintUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    updated = crud.update_complaint(
        db,
        complaint_id,
        complaint
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    return updated


# =====================================================
# Delete Complaint
# =====================================================

@router.delete("/{complaint_id}")
def delete_complaint(
    complaint_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    deleted = crud.delete_complaint(
        db,
        complaint_id
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    return {
        "message": "Complaint deleted successfully"
    }


# =====================================================
# Logged-in User Complaints
# =====================================================

@router.get("/my/list", response_model=list[schemas.ComplaintResponse])
def my_complaints(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    return crud.get_user_complaints(
        db,
        current_user.id
    )


# =====================================================
# Update Complaint Status (Admin)
# =====================================================

@router.put("/{complaint_id}/status")
def update_status(
    complaint_id: int,
    status: schemas.StatusUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    complaint = crud.update_complaint_status(
        db,
        complaint_id,
        status.status
    )

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    return {
        "message": "Status updated successfully",
        "status": complaint.status
    }