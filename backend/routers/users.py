from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
import crud
import schemas
from auth import authenticate_user, create_access_token

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/register")
def register(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    existing = crud.get_user_by_email(db, user.email)

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return crud.create_user(
        db,
        user.name,
        user.email,
        user.password
    )


@router.post("/login")
def login(
    user: schemas.UserLogin,
    db: Session = Depends(get_db)
):
    # FIXED: Called authenticate_user and created access token directly
    db_user = authenticate_user(db, user.email, user.password)

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    access_token = create_access_token(
        data={"sub": db_user.email, "id": db_user.id, "role": db_user.role}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/")
def all_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db)
