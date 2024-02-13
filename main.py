from fastapi import FastAPI

from src.pages.router import router as router_pages

app = FastAPI(
    title='GetRepos'
)

app.include_router(router_pages)





