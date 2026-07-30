from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    Text,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base


# =====================================================
# USER MODEL
# =====================================================

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(150), unique=True, nullable=False, index=True)

    password = Column(String(255), nullable=False)

    role = Column(String(20), default="citizen")

    created_at = Column(DateTime, default=datetime.utcnow)

    complaints = relationship(
        "Complaint",
        back_populates="owner",
        cascade="all, delete-orphan"
    )


# =====================================================
# COMPLAINT MODEL
# =====================================================

class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    title = Column(String(200), nullable=False)

    description = Column(Text, nullable=False)

    image_path = Column(String(300), nullable=True)

    latitude = Column(Float, nullable=False)

    longitude = Column(Float, nullable=False)

    category = Column(String(100), default="Unknown")

    department = Column(String(100), default="General")

    priority = Column(String(50), default="Low")

    severity_score = Column(Float, default=0)

    genuine_score = Column(Float, default=0)

    image_verified = Column(Boolean, default=False)

    verification_score = Column(Float, default=0)

    status = Column(String(50), default="Pending")

    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship(
        "User",
        back_populates="complaints"
    )

    feedbacks = relationship(
        "Feedback",
        back_populates="complaint",
        cascade="all, delete-orphan"
    )

    notifications = relationship(
        "Notification",
        back_populates="complaint",
        cascade="all, delete-orphan"
    )


# =====================================================
# ADMIN MODEL
# =====================================================

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(150), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    role = Column(String(20), default="admin")

    created_at = Column(DateTime, default=datetime.utcnow)


# =====================================================
# FEEDBACK MODEL
# =====================================================

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)

    complaint_id = Column(
        Integer,
        ForeignKey("complaints.id")
    )

    rating = Column(Integer, nullable=False)

    feedback = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)

    complaint = relationship(
        "Complaint",
        back_populates="feedbacks"
    )


# =====================================================
# NOTIFICATION MODEL
# =====================================================

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)

    complaint_id = Column(
        Integer,
        ForeignKey("complaints.id")
    )

    title = Column(String(200), nullable=False)

    message = Column(Text, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    complaint = relationship(
        "Complaint",
        back_populates="notifications"
    )