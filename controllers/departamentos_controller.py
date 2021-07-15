import requests
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from utils import add_link

templates = Jinja2Templates(directory="templates")

router = APIRouter()
headers = {'Content-Type': 'application/json ; charset=utf-8'}


@router.get("",
            response_class=HTMLResponse)
async def get(request: Request):
    response = requests.get(
        "http://localhost:8000/departamentos", headers=headers)
    departamentos = add_link(items=response.json()['data'],
                             type='departamentos')
    return templates.TemplateResponse(
        "departamentos.html",
        {"request": request, "departamentos": departamentos}
    )


@router.post("",
             response_class=HTMLResponse)
async def post(request: Request):
    form = await request.form()
    response = requests.get(
        f"http://localhost:8000/departamentos/{form.get('search')}"
        if form.get('type') == 'id' else
        f"http://localhost:8000/departamentos/province/{form.get('search')}",
        headers=headers)
    data = response.json()
    departamentos = add_link(
        items=data['data'] if data.get('data') else [data],
        type='departamentos')
    return templates.TemplateResponse(
        "departamentos.html",
        {"request": request, "departamentos": departamentos}
    )


@router.get("/new",
            response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse(
        "edit_departamento.html",
        {"request": request}
    )


@router.post("/new",
             response_class=HTMLResponse)
async def post_departamento(request: Request):
    form = await request.form()
    json = {
        'nombre': form.get('nombre'),
        'id': form.get('id'),
        'provincia_id': form.get('provincia_id')
    }
    response = requests.post(
        f"http://localhost:8000/departamentos",
        headers=headers,
        json=json
    )
    if response.status_code == 400:
        error = response.json()['detail']
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": error}
        )
    return templates.TemplateResponse(
        "edit_departamento.html",
        {"request": request, "departamento": response.json()}
    )


@router.get("/{departamento_id}/edit",
            response_class=HTMLResponse)
async def get(request: Request, departamento_id: int):
    response = requests.get(
        f"http://localhost:8000/departamentos/{departamento_id}",
        headers=headers)
    return templates.TemplateResponse(
        "edit_departamento.html",
        {"request": request, "departamento": response.json()}
    )


@router.post("/{departamento_id}/edit",
             response_class=HTMLResponse)
async def put_departamento(request: Request,
                           departamento_id: int):
    form = await request.form()
    json = {
        'nombre': form.get('nombre'),
        'id': form.get('id'),
        'provincia_id': form.get('provincia_id')
    }
    response = requests.put(
        f"http://localhost:8000/departamentos/{departamento_id}",
        headers=headers,
        json=json
    )
    if response.status_code == 400:
        error = response.json()['detail']
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": error}
        )
    return RedirectResponse(url="departamentos")
