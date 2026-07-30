#importing
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import crud
router = APIRouter(
    prefix="/dashboard",
    tags=["Government Dashboard"]
)
@router.get("/summary")
#working on dashboard
def dashboard_summary(db: Session = Depends(get_db)):
    return {
        "total_complaints": crud.total_complaints(db),
        "pending": crud.pending_complaints(db),
        "resolved": crud.resolved_complaints(db),
        "rejected": crud.rejected_complaints(db),
        "in_progress": crud.inprogress_complaints(db)
    }
@router.get("/emergency")
def emergency_complaints(db: Session = Depends(get_db)):
    complaints = crud.complaints_by_priority(
        db,
        "Emergency"
    )
    return complaint
@router.get("/critical")
def critical_complaints(db: Session = Depends(get_db)):
    complaints = crud.complaints_by_priority(
        db,
        "Critical"
    )
    return complaints
