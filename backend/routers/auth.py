from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

# Absolute imports from the root directory
from database import get_db
import crud
import schemas
from security import verify_password
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()

# Matches the prefix="/api/auth" registered in main.py
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


# ==========================================
# Authenticate User Helper
# ==========================================

def authenticate_user(db: Session, email: str, password: str):
    user = crud.get_user_by_email(db, email)
    if user is None or not verify_password(password, user.password):
        return None
    return user


# ==========================================
# Create JWT Token
# ==========================================

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    
    # Use timezone-aware UTC datetime
    expire = datetime.now(timezone.utc) + (
        expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# ==========================================
# Login Route
# ==========================================

@router.post("/login")
def login_user(data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, data.email, data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(
        data={"sub": user.email, "id": user.id, "role": user.role}
    )
    return {"access_token": access_token, "token_type": "bearer"}


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
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = crud.get_user_by_email(db, email)
    if user is None:
        raise credentials_exception

    return user
