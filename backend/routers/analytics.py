from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
import crud
import models
from auth import get_current_user

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/category")
def category_analysis(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.category_statistics(db)

@router.get("/department")
def department_analysis(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.department_statistics(db)

@router.get("/priority")
def priority_analysis(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.priority_statistics(db)

@router.get("/status")
def status_analysis(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.status_statistics(db)
