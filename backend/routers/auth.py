from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Absolute imports from the root directory
from database import get_db
import schemas
import crud

# Assuming auth.py is at your root level
from auth import (
    authenticate_user,
    create_access_token,
    get_current_user
)
from config import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# ==========================================
# Register
# ==========================================
@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # BUG FIX: Removed hash_password() here because crud.create_user already hashes it.
    new_user = crud.create_user(
        db=db,
        name=user.name,
        email=user.email,
        password=user.password 
    )

    return {
        "message": "User registered successfully",
        "user": new_user
    }

# ==========================================
# Login
# ==========================================
@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={"sub": db_user.email},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": db_user.role
    }

# ==========================================
# Current User
# ==========================================
@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return current_user
