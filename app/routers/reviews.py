from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.LocationCategoryReviewed)
def create_review(review: schemas.LocationCategoryReviewedCreate, db: Session = Depends(get_db)):
    return crud.create_location_category_reviewed(db=db, review=review)

@router.get("/", response_model=list[schemas.LocationCategoryReviewed])
def read_reviews(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reviews = crud.get_location_category_reviewed(db, skip=skip, limit=limit)
    return reviews
