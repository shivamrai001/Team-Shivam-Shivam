from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
import crud
import schemas

router = APIRouter(
    prefix="/feedback",
    tags=["Feedback"]
)


# ------------------------------------
# Submit Feedback
# ------------------------------------
@router.post("/")
def create_feedback(
    feedback: schemas.FeedbackCreate,
    db: Session = Depends(get_db)
):
    complaint = crud.get_complaint(db, feedback.complaint_id)

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    new_feedback = crud.create_feedback(db, feedback)

    return {
        "message": "Feedback submitted successfully",
        "data": new_feedback
    }


# ------------------------------------
# Get All Feedback
# ------------------------------------
@router.get("/")
def get_all_feedback(db: Session = Depends(get_db)):
    return crud.get_all_feedback(db)


# ------------------------------------
# Get Feedback by ID
# ------------------------------------
@router.get("/{feedback_id}")
def get_feedback(
    feedback_id: int,
    db: Session = Depends(get_db)
):
    feedback = crud.get_feedback(db, feedback_id)

    if feedback is None:
        raise HTTPException(
            status_code=404,
            detail="Feedback not found"
        )

    return feedback


# ------------------------------------
# Delete Feedback
# ------------------------------------
@router.delete("/{feedback_id}")
def delete_feedback(
    feedback_id: int,
    db: Session = Depends(get_db)
):
    feedback = crud.delete_feedback(db, feedback_id)

    if feedback is None:
        raise HTTPException(
            status_code=404,
            detail="Feedback not found"
        )

    return {
        "message": "Feedback deleted successfully"
    }
