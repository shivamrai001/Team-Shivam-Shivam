from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..database import get_db
from .. import schemas, crud
from ..security import hash_password
from ..auth import (
    authenticate_user,
    create_access_token,
    get_current_user
)
from ..config import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# ==========================================
# Register
# ==========================================

@router.post("/register")
def register(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    existing = crud.get_user_by_email(
        db,
        user.email
    )

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed = hash_password(
        user.password
    )

    new_user = crud.create_user(
        db=db,
        name=user.name,
        email=user.email,
        password=hashed
    )

    return {
        "message": "User registered successfully",
        "user": new_user
    }


# ==========================================
# Login
# ==========================================

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    if not user:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# ==========================================
# Current User
# ==========================================

@router.get("/me")
def get_me(
    current_user=Depends(get_current_user)
):

    return current_user