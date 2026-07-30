from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# =====================================================
# USER SCHEMAS
# =====================================================

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    created_at: datetime

    class Config:
        from_attributes = True


# =====================================================
# COMPLAINT SCHEMAS
# =====================================================

class ComplaintCreate(BaseModel):
    title: str
    description: str
    image_path: Optional[str] = None
    latitude: float
    longitude: float


class ComplaintUpdate(BaseModel):
    title: str
    description: str
    image_path: Optional[str] = None
    latitude: float
    longitude: float


class ComplaintResponse(BaseModel):
    id: int

    user_id: int

    title: str

    description: str

    image_path: Optional[str]

    latitude: float

    longitude: float

    category: str

    department: str

    priority: str

    severity_score: float

    genuine_score: float

    image_verified: bool

    verification_score: float

    status: str

    created_at: datetime

    class Config:
        from_attributes = True


# =====================================================
# ADMIN SCHEMAS
# =====================================================

class AdminCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class AdminResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    created_at: datetime

    class Config:
        from_attributes = True


# =====================================================
# FEEDBACK SCHEMAS
# =====================================================

class FeedbackCreate(BaseModel):
    complaint_id: int
    rating: int
    feedback: str


class FeedbackResponse(BaseModel):
    id: int
    complaint_id: int
    rating: int
    feedback: str
    created_at: datetime

    class Config:
        from_attributes = True


# =====================================================
# NOTIFICATION SCHEMAS
# =====================================================

class NotificationCreate(BaseModel):
    complaint_id: int
    title: str
    message: str


class NotificationResponse(BaseModel):
    id: int
    complaint_id: int
    title: str
    message: str
    created_at: datetime

    class Config:
        from_attributes = True


# =====================================================
# STATUS UPDATE
# =====================================================

class StatusUpdate(BaseModel):
    status: str


# =====================================================
# DASHBOARD
# =====================================================

class DashboardStats(BaseModel):
    total: int
    pending: int
    resolved: int
    rejected: int
    in_progress: int