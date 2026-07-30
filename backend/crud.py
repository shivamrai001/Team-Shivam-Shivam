from datetime import datetime
from sqlalchemy.orm import Session
from .ai.verifier import verify_image
from . import models
from sqlalchemy import func
from .security import hash_password
# AI Modules
from .ai.classifier import classify
from .ai.severity import calculate_severity
from .ai.priority import get_priority
from .ai.duplicate import genuine_score
from .ai.department import assign_department


# ======================================================
# USER CRUD
# ======================================================

def create_user(db: Session, name: str, email: str, password: str):

    user = models.User(
        name=name,
        email=email,
        password=hash_password(password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_user_by_email(db: Session, email: str):

    return db.query(models.User).filter(
        models.User.email == email
    ).first()


def get_user_by_id(db: Session, user_id: int):

    return db.query(models.User).filter(
        models.User.id == user_id
    ).first()


def get_all_users(db: Session):

    return db.query(models.User).all()

# ======================================================
# CREATE COMPLAINT
# ======================================================

def create_complaint(
    db: Session,
    complaint,
    user_id: int
):

    # AI Processing
    category = classify(
        complaint.description
    )

    severity = calculate_severity(
        category,
        complaint.description
    )

    priority = get_priority(
        severity
    )

    score = genuine_score(
        complaint.description
    )

    department = assign_department(
        category
    )

    verification = verify_image(
        complaint.image_path
    )

    new_complaint = models.Complaint(

        user_id=user_id,

        title=complaint.title,

        description=complaint.description,

        image_path=complaint.image_path,

        latitude=complaint.latitude,

        longitude=complaint.longitude,

        category=category,

        department=department,

        priority=priority,

        severity_score=severity,

        genuine_score=score,

        image_verified=verification["verified"],

        verification_score=verification["score"],

        status="Pending",

        created_at=datetime.utcnow()

    )

    db.add(new_complaint)

    db.commit()

    db.refresh(new_complaint)

    return new_complaint

# ======================================================
# GET ALL COMPLAINTS
# ======================================================

def get_complaints(db: Session):

    return db.query(models.Complaint).all()


# ======================================================
# GET COMPLAINT BY ID
# ======================================================

def get_complaint(db: Session, complaint_id: int):

    return db.query(models.Complaint).filter(
        models.Complaint.id == complaint_id
    ).first()


# ======================================================
# UPDATE COMPLAINT
# ======================================================

def update_complaint(
        db: Session,
        complaint_id: int,
        complaint_data
):

    complaint = get_complaint(
        db,
        complaint_id
    )

    if complaint is None:
        return None

    # Update complaint fields
    complaint.title = complaint_data.title
    complaint.description = complaint_data.description
    complaint.image_path = complaint_data.image_path
    complaint.latitude = complaint_data.latitude
    complaint.longitude = complaint_data.longitude

    # Run AI Again
    complaint.category = classify(
        complaint.description
    )

    complaint.severity_score = calculate_severity(
        complaint.category,
        complaint.description
    )

    complaint.priority = get_priority(
        complaint.severity_score
    )

    complaint.genuine_score = genuine_score(
        complaint.description
    )

    complaint.department = assign_department(
        complaint.category
    )

    # Verify updated image
    verification = verify_image(
        complaint.image_path
    )

    complaint.image_verified = verification["verified"]

    complaint.verification_score = verification["score"]

    db.commit()
    db.refresh(complaint)

    return complaint

# ======================================================
# UPDATE STATUS
# ======================================================


# ======================================================
# DELETE COMPLAINT
# ======================================================

def delete_complaint(
        db: Session,
        complaint_id: int
):

    complaint = get_complaint(
        db,
        complaint_id
    )

    if complaint is None:
        return None

    db.delete(complaint)
    db.commit()

    return complaint


# ======================================================
# DASHBOARD COUNTS
# ======================================================

def total_complaints(db: Session):

    return db.query(
        models.Complaint
    ).count()


def pending_complaints(db: Session):

    return db.query(
        models.Complaint
    ).filter(
        models.Complaint.status == "Pending"
    ).count()


def resolved_complaints(db: Session):

    return db.query(
        models.Complaint
    ).filter(
        models.Complaint.status == "Resolved"
    ).count()
def recent_complaints(db: Session):

    return db.query(
        models.Complaint
    ).order_by(
        models.Complaint.id.desc()
    ).limit(10).all()

def rejected_complaints(db: Session):

    return db.query(
        models.Complaint
    ).filter(
        models.Complaint.status == "Rejected"
    ).count()


def inprogress_complaints(db: Session):

    return db.query(
        models.Complaint
    ).filter(
        models.Complaint.status == "In Progress"
    ).count()


# ======================================================
# FILTERS
# ======================================================

def complaints_by_category(
        db: Session,
        category: str
):

    return db.query(
        models.Complaint
    ).filter(
        models.Complaint.category == category
    ).all()


def complaints_by_priority(
        db: Session,
        priority: str
):

    return db.query(
        models.Complaint
    ).filter(
        models.Complaint.priority == priority
    ).all()


def complaints_by_department(
        db: Session,
        department: str
):

    return db.query(
        models.Complaint
    ).filter(
        models.Complaint.department == department
    ).all()


def complaints_by_status(
        db: Session,
        status: str
):

    return db.query(
        models.Complaint
    ).filter(
        models.Complaint.status == status
    ).all()



def category_statistics(db):

    data = db.query(

        models.Complaint.category,

        func.count(models.Complaint.id)

    ).group_by(

        models.Complaint.category

    ).all()

    return [
        {
            "category": c,
            "count": count
        }

        for c, count in data
    ]


def department_statistics(db):

    data = db.query(

        models.Complaint.department,

        func.count(models.Complaint.id)

    ).group_by(

        models.Complaint.department

    ).all()

    return [

        {
            "department": d,
            "count": c
        }

        for d, c in data

    ]


def priority_statistics(db):

    data = db.query(

        models.Complaint.priority,

        func.count(models.Complaint.id)

    ).group_by(

        models.Complaint.priority

    ).all()

    return [

        {
            "priority": p,
            "count": c
        }

        for p, c in data

    ]


def status_statistics(db):

    data = db.query(

        models.Complaint.status,

        func.count(models.Complaint.id)

    ).group_by(

        models.Complaint.status

    ).all()

    return [

        {
            "status": s,
            "count": c
        }

        for s, c in data

    ]
def highest_severity(db: Session):

    return db.query(
        models.Complaint
    ).order_by(
        models.Complaint.severity_score.desc()
    ).all()
#****************************************
#ADMIN
#****************************************
def create_admin(db: Session, admin):

    new_admin = models.Admin(
        name=admin.name,
        email=admin.email,
        password=admin.password,
        role="admin"
    )

    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)

    return new_admin
def get_all_admins(db: Session):

    return db.query(models.Admin).all()
def get_admin(db: Session, admin_id: int):

    return db.query(models.Admin).filter(
        models.Admin.id == admin_id
    ).first()
def get_admin_by_email(db: Session, email: str):

    return db.query(models.Admin).filter(
        models.Admin.email == email
    ).first()


def delete_admin(db: Session, admin_id: int):

    admin = get_admin(db, admin_id)

    if admin:

        db.delete(admin)

        db.commit()

    return admin
#*******************************************
#FEEDBACK
#*******************************************
# ======================================================
# FEEDBACK CRUD
# ======================================================

def create_feedback(db: Session, feedback):

    new_feedback = models.Feedback(

        complaint_id=feedback.complaint_id,

        rating=feedback.rating,

        feedback=feedback.feedback

    )

    db.add(new_feedback)

    db.commit()

    db.refresh(new_feedback)

    return new_feedback


def get_all_feedback(db: Session):

    return db.query(models.Feedback).all()


def get_feedback(db: Session, feedback_id: int):

    return db.query(models.Feedback).filter(
        models.Feedback.id == feedback_id
    ).first()


# NEW
def delete_feedback(db: Session, feedback_id: int):

    feedback = get_feedback(db, feedback_id)

    if feedback:

        db.delete(feedback)

        db.commit()

    return feedback
def create_notification(db: Session, notification):

    new_notification = models.Notification(

        title=notification.title,

        message=notification.message,

        complaint_id=notification.complaint_id,

        created_at=datetime.utcnow()

    )

    db.add(new_notification)

    db.commit()

    db.refresh(new_notification)

    return new_notification
def get_all_notifications(db: Session):

    return db.query(
        models.Notification
    ).all()
def get_notification(db: Session, notification_id: int):

    return db.query(
        models.Notification
    ).filter(
        models.Notification.id == notification_id
    ).first()
def delete_notification(db: Session, notification_id: int):

    notification = get_notification(
        db,
        notification_id
    )

    if notification:

        db.delete(notification)

        db.commit()

    return notification
def get_user_complaints(db: Session, user_id: int):

    return db.query(
        models.Complaint
    ).filter(
        models.Complaint.user_id == user_id
    ).all()
def update_complaint_status(
        db: Session,
        complaint_id: int,
        status: str
):

    complaint = db.query(
        models.Complaint
    ).filter(
        models.Complaint.id == complaint_id
    ).first()

    if complaint:

        complaint.status = status

        db.commit()

        db.refresh(complaint)

    return complaint
