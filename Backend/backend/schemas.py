from pydantic import BaseModel, EmailStr


# ==================================================
# USER SCHEMAS
# ==================================================

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
    email: str

    class Config:
        from_attributes = True


# ==================================================
# COMPLAINT SCHEMAS
# ==================================================
class ComplaintCreate(BaseModel):
    user_id: int
    title: str
    description: str
    image_path: str
    latitude: float
    longitude: float


class ComplaintUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    image_path: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    status: str | None = None

class ComplaintResponse(BaseModel):
    image_path: str

    image_verified: bool

    verification_score: float
    id: int

    user_id: int

    title: str

    description: str

    image: str

    latitude: float

    longitude: float

    category: str

    department: str

    priority: str

    severity_score: int

    genuine_score: float

    status: str

    created_at: str

    class Config:
        from_attributes = True


# ==================================================
# ADMIN SCHEMAS
# ==================================================

class AdminCreate(BaseModel):

    name: str

    email: EmailStr

    password: str

    role: str


class AdminResponse(BaseModel):

    id: int

    name: str

    email: str

    role: str

    class Config:
        from_attributes = True


# ==================================================
# FEEDBACK SCHEMAS
# ==================================================

class FeedbackCreate(BaseModel):

    complaint_id: int

    rating: int

    feedback: str


class FeedbackResponse(BaseModel):

    id: int

    complaint_id: int

    rating: int

    feedback: str

    class Config:
        from_attributes = True


# ==================================================
# NOTIFICATION SCHEMAS
# ==================================================

class NotificationCreate(BaseModel):

    title: str

    message: str

    complaint_id: int

    created_at: str


class NotificationResponse(BaseModel):

    id: int

    title: str

    message: str

    complaint_id: int

    created_at: str

    class Config:
        from_attributes = True