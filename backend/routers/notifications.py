from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas

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

    complaint = db.query(models.Complaint).filter(
        models.Complaint.id == notification.complaint_id
    ).first()

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    new_notification = models.Notification(
        title=notification.title,
        message=notification.message,
        complaint_id=notification.complaint_id,
        created_at=notification.created_at
    )

    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)

    return {
        "message": "Notification created successfully",
        "data": new_notification
    }


# ------------------------------------
# Get All Notifications
# ------------------------------------
@router.get("/")
def get_all_notifications(
    db: Session = Depends(get_db)
):
    return db.query(models.Notification).all()


# ------------------------------------
# Get Notification by ID
# ------------------------------------
@router.get("/{notification_id}")
def get_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):

    notification = db.query(models.Notification).filter(
        models.Notification.id == notification_id
    ).first()

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

    notification = db.query(models.Notification).filter(
        models.Notification.id == notification_id
    ).first()

    if notification is None:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    db.delete(notification)
    db.commit()

    return {
        "message": "Notification deleted successfully"
    }