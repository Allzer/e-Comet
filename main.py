from fastapi import FastAPI

from src.GetRepos.parser import parser
from src.GetRepos.update import update
from src.config import URL
from src.pages.router import router as router_pages

app = FastAPI(
    title='GetRepos'
)

app.include_router(router_pages)

@app.on_event("startup")
def on_startup():
    print("Началась загрузка данных")
    pars = parser(URL)
    update(pars)




