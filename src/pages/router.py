from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory='src/templates')


@router.get("/repos") #Если функция, которая образается к БД должна получить какой-то аргумент, то мы его указываем в декораторе
def get_repos(request: Request):
    return templates.TemplateResponse("list.html", {"request": request})