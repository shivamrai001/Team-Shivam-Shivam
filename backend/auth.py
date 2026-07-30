from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from .database import get_db
from . import crud
from .security import verify_password
from .config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")


# ==========================================
# Authenticate User
# ==========================================

def authenticate_user(db: Session, email: str, password: str):

    user = crud.get_user_by_email(db, email)

    print("=================================")
    print("Email entered:", email)
    print("Password entered:", password)
    print("User found:", user)

    if user:
        print("Stored password:", user.password)
        print("Verify:", verify_password(password, user.password))

    if user is None:
        return None

    if not verify_password(password, user.password):
        return None

    return user


# ==========================================
# Create JWT Token
# ==========================================

def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None
):

    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


# ==========================================
# Login User
# ==========================================

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

    if user is None:
        return None

    access_token = create_access_token(
        data={
            "sub": user.email,
            "id": user.id,
            "role": user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# ==========================================
# Get Current Logged-in User
# ==========================================

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = crud.get_user_by_email(
        db,
        email
    )

    if user is None:
        raise credentials_exception

    return user