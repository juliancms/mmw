from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta

from . import models, schemas

def get_location(db: Session, location_id: int):
    return db.query(models.Location).filter(models.Location.id == location_id).first()

def get_locations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Location).offset(skip).limit(limit).all()

def create_location(db: Session, location: schemas.LocationCreate):
    db_location = models.Location(**location.model_dump())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Category).offset(skip).limit(limit).all()

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_location_category_reviewed(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.LocationCategoryReviewed).offset(skip).limit(limit).all()

def create_location_category_reviewed(db: Session, review: schemas.LocationCategoryReviewedCreate):
    db_review = models.LocationCategoryReviewed(**review.model_dump())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_unreviewed_locations_categories(db: Session):
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    
    subquery = db.query(
        models.LocationCategoryReviewed.location_id,
        models.LocationCategoryReviewed.category_id,
        func.max(models.LocationCategoryReviewed.last_reviewed).label('last_reviewed')
    ).group_by(
        models.LocationCategoryReviewed.location_id,
        models.LocationCategoryReviewed.category_id
    ).subquery()
    
    unreviewed = db.query(
        subquery.c.location_id,
        subquery.c.category_id,
        subquery.c.last_reviewed
    ).filter(
        subquery.c.last_reviewed < thirty_days_ago
    ).order_by(
        subquery.c.last_reviewed
    ).limit(10).all()

    return unreviewed
