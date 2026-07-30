#importing all the required lbarires
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import crud
from .. import schemas
from .. import auth
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)
@router.post("/register")
#registration of users
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
            detail="Email already exists"
        )
    return crud.create_user(
        db,
        user.name,
        user.email,
        user.password
    )
@router.post("/login")
#login for users
def login(
        user: schemas.UserLogin,
        db: Session = Depends(get_db)
):
    token = auth.login_user(
        db,
        user.email,
        user.password
    )
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )
    return token
@router.get("/")
def all_users(
        db: Session = Depends(get_db)
):
    return crud.get_all_users(db)
