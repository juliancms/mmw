from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/recommendations",
    tags=["recommendations"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[schemas.Recommendation])
def read_recommendations(db: Session = Depends(get_db)):
    recommendations = crud.get_unreviewed_locations_categories(db)
    return recommendations
