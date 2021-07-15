import requests
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get("",
            response_class=HTMLResponse)
async def get(request: Request):
    headers = {'Content-Type': 'application/json ; charset=utf-8'}
    response = requests.get(
        "http://localhost:8000/provincias", headers=headers)

    return templates.TemplateResponse(
        "provincias.html",
        {"request": request, "provincias": response.json()['data']}
    )
