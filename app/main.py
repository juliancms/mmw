from fastapi import FastAPI
from .routers import locations, categories, reviews, recommendations
from .database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(locations.router)
app.include_router(categories.router)
app.include_router(reviews.router)
app.include_router(recommendations.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Map My World API"}
