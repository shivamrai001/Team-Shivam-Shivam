#importing all libarires
from datetime import datetime
from sqlalchemy.orm import Session
from . import models
from .security import hash_password
# AI Modules
from .ai.classifier import classify
from .ai.severity import calculate_severity
from .ai.priority import get_priority
from .ai.duplicate import genuine_score
from .ai.department import assign_department
# ******************************************************
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
# ******************************************************
# CREATE COMPLAINT
# ======================================================
def create_complaint(db: Session, complaint):
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
    #new complaints
    new_complaint = models.Complaint(
        title=complaint.title,
        description=complaint.description,
        image=complaint.image,
        latitude=complaint.latitude,
        longitude=complaint.longitude,
        category=category,
        severity_score=severity,
        priority=priority,
        genuine_score=score,
        department=department,
        status="Pending",
        created_at=str(datetime.now())
    )
    db.add(new_complaint)
    db.commit()
    db.refresh(new_complaint)
    return new_complaint
# ======================================================
# GET ALL COMPLAINTS
# ******************************************************
def get_all_complaints(db: Session):
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
# ******************************************************
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
    complaint.title = complaint_data.title
    complaint.description = complaint_data.description
    complaint.image = complaint_data.image
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
    db.commit()
    db.refresh(complaint)
    return complaint
# ======================================================
# UPDATE STATUS
# ******************************************************
def update_complaint_status(
        db: Session,
        complaint_id: int,
        status: str
):
    complaint = get_complaint(
        db,
        complaint_id
    )
    if complaint is None:
        return None
    complaint.status = status
    db.commit()
    db.refresh(complaint)
    return complaint
# ======================================================
# DELETE COMPLAINT
# ******************************************************
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
# ******************************************************
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
# ******************************************************
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
from sqlalchemy import func
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
