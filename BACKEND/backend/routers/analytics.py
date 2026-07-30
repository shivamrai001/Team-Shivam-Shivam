#importing libaries
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import crud
#declaring router
router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)
@router.get("/category")
def category_analysis(db: Session = Depends(get_db)):
    return crud.category_statistics(db)
@router.get("/department")
def department_analysis(db: Session = Depends(get_db)):
    return crud.department_statistics(db)
@router.get("/priority")
def priority_analysis(db: Session = Depends(get_db)):
    return crud.priority_statistics(db)
@router.get("/status")
def status_analysis(db: Session = Depends(get_db)):
    return crud.status_statistics(db)
