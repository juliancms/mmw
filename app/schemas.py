from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class LocationBase(BaseModel):
    latitude: float
    longitude: float

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class LocationCategoryReviewedBase(BaseModel):
    location_id: int
    category_id: int
    last_reviewed: datetime

class LocationCategoryReviewedCreate(LocationCategoryReviewedBase):
    pass

class LocationCategoryReviewed(LocationCategoryReviewedBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class Recommendation(BaseModel):
    location_id: int
    category_id: int
    last_reviewed: datetime

    model_config = ConfigDict(from_attributes=True)