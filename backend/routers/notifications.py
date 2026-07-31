from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
import crud
import schemas

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


# ------------------------------------
# Create Notification
# ------------------------------------
@router.post("/")
def create_notification(
    notification: schemas.NotificationCreate,
    db: Session = Depends(get_db)
):
    complaint = crud.get_complaint(db, notification.complaint_id)

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    new_notification = crud.create_notification(db, notification)

    return {
        "message": "Notification created successfully",
        "data": new_notification
    }


# ------------------------------------
# Get All Notifications
# ------------------------------------
@router.get("/")
def get_all_notifications(db: Session = Depends(get_db)):
    return crud.get_all_notifications(db)


# ------------------------------------
# Get Notification by ID
# ------------------------------------
@router.get("/{notification_id}")
def get_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):
    notification = crud.get_notification(db, notification_id)

    if notification is None:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return notification


# ------------------------------------
# Delete Notification
# ------------------------------------
@router.delete("/{notification_id}")
def delete_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):
    notification = crud.delete_notification(db, notification_id)

    if notification is None:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return {
        "message": "Notification deleted successfully"
    }
