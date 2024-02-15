from fastapi import FastAPI

from src.database import SessionLocal
from src.pages.router import router as router_pages

app = FastAPI(
    title='GetRepos'
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(router_pages)





