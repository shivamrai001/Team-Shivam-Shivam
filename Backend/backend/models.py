from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship

from .database import Base


# ==========================================
# USER TABLE
# ==========================================

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    password = Column(String, nullable=False)

    role = Column(String, default="citizen")
    complaints = relationship(
        "Complaint",
        back_populates="user",
        cascade="all, delete"
    )


# ==========================================
# COMPLAINT TABLE
# ==========================================

class Complaint(Base):

    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    title = Column(String, nullable=False)

    description = Column(String)

    image_path = Column(String)

    image_verified = Column(Boolean, default=False)

    verification_score = Column(Float, default=0.0)

    latitude = Column(Float)

    longitude = Column(Float)

    category = Column(String)

    department = Column(String)

    priority = Column(String)

    severity_score = Column(Integer)

    genuine_score = Column(Float)

    status = Column(
        String,
        default="Pending"
    )

    from sqlalchemy import DateTime
    from datetime import datetime

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship(
        "User",
        back_populates="complaints"
    )

# ==========================================
# ADMIN TABLE
# ==========================================

class Admin(Base):

    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    email = Column(
        String,
        unique=True
    )

    password = Column(String)

    role = Column(String)


# ==========================================
# FEEDBACK TABLE
# ==========================================

class Feedback(Base):

    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)

    complaint_id = Column(
        Integer,
        ForeignKey("complaints.id")
    )

    rating = Column(Integer)

    feedback = Column(String)


# ==========================================
# NOTIFICATION TABLE
# ==========================================

class Notification(Base):

    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    message = Column(String)

    complaint_id = Column(
        Integer,
        ForeignKey("complaints.id")
    )

    created_at = Column(String)