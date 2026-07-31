from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
import crud

router = APIRouter(
    prefix="/maps",
    tags=["Interactive Maps"]
)


@router.get("/markers")
def map_markers(db: Session = Depends(get_db)):
    # FIXED: Changed get_all_complaints -> get_complaints
    complaints = crud.get_complaints(db)

    data = []
    for c in complaints:
        data.append({
            "id": c.id,
            "title": c.title,
            "category": c.category,
            "priority": c.priority,
            "latitude": c.latitude,
            "longitude": c.longitude,
            "status": c.status
        })

    return data
