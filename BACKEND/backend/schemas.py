from pydantic import BaseModel
from pydantic import EmailStr
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
class UserLogin(BaseModel):
    email: EmailStr
    password: str
class ComplaintCreate(BaseModel):
    title: str
    description: str
    image: str
    latitude: float
    longitude: float
class ComplaintResponse(BaseModel):
    id: int
    title: str
    description: str
    image: str
    latitude: float
    longitude: float
    category: str
    severity_score: int
    priority: str
    genuine_score: float
    department: str
    status: str
    created_at: str
    class Config:
        from_attributes = True
class Token(BaseModel):
    access_token: str
    token_type: str
from typing import Optional
class ComplaintUpdate(BaseModel):
    status: Optional[str] = None
class ComplaintResponse(BaseModel):
    id: int
    title: str
    description: str
    image: str
    latitude: float
    longitude: float
    category: str
    severity_score: int
    priority: str
    genuine_score: float
    department: str
    status: str
    created_at: str
    class Config:
        from_attributes = True
