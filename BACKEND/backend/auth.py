#importing required libaries
from sqlalchemy.orm import Session
from . import crud
from .security import (
    verify_password,
    create_access_token
)
#authentication using eamil,password
def authenticate_user(
        db: Session,
        email: str,
        password: str
):
    user = crud.get_user_by_email(
        db,
        email
    )
    if not user:
        return None
    if not verify_password(
            password,
            user.password
    ):
        return None
    return user
def login_user(
        db: Session,
        email: str,
        password: str
):
    user = authenticate_user(
        db,
        email,
        password
    )
    if not user:
        return None
    token = create_access_token(
        {
            "sub": user.email
        }
    )
    return {
        "access_token": token,
        "token_type": "bearer"
    }
