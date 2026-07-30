from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas

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

    complaint = db.query(models.Complaint).filter(
        models.Complaint.id == feedback.complaint_id
    ).first()

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    new_feedback = models.Feedback(
        complaint_id=feedback.complaint_id,
        rating=feedback.rating,
        feedback=feedback.feedback
    )

    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)

    return {
        "message": "Feedback submitted successfully",
        "data": new_feedback
    }


# ------------------------------------
# Get All Feedback
# ------------------------------------
@router.get("/")
def get_all_feedback(
    db: Session = Depends(get_db)
):
    return db.query(models.Feedback).all()


# ------------------------------------
# Get Feedback by ID
# ------------------------------------
@router.get("/{feedback_id}")
def get_feedback(
    feedback_id: int,
    db: Session = Depends(get_db)
):

    feedback = db.query(models.Feedback).filter(
        models.Feedback.id == feedback_id
    ).first()

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

    feedback = db.query(models.Feedback).filter(
        models.Feedback.id == feedback_id
    ).first()

    if feedback is None:
        raise HTTPException(
            status_code=404,
            detail="Feedback not found"
        )

    db.delete(feedback)
    db.commit()

    return {
        "message": "Feedback deleted successfully"
    }