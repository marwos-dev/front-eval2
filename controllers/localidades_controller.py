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
        "http://localhost:8000/localidades", headers=headers)
    localidades = add_link(items=response.json()['data'],
                           type='localidades')
    return templates.TemplateResponse(
        "localidades.html",
        {"request": request, "localidades": localidades}
    )


@router.post("",
             response_class=HTMLResponse)
async def post(request: Request):
    form = await request.form()
    response = requests.get(
        f"http://localhost:8000/localidades/{form.get('search')}"
        if form.get('type') == 'id' else
        f"http://localhost:8000/localidades/departamento/{form.get('search')}",
        headers=headers)
    data = response.json()
    localidades = add_link(
        items=data['data'] if data.get('data') else [data],
        type='localidades')
    return templates.TemplateResponse(
        "localidades.html",
        {"request": request, "localidades": localidades}
    )


@router.get("/new",
            response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse(
        "edit_localidad.html",
        {"request": request}
    )


@router.post("/new",
             response_class=HTMLResponse)
async def post_localidad(request: Request):
    form = await request.form()
    json = {
        'nombre': form.get('nombre'),
        'id': form.get('id'),
        'departamento_id': form.get('departamento_id')
    }
    response = requests.post(
        f"http://localhost:8000/localidades",
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
        "edit_localidad.html",
        {"request": request, "localidad": response.json()}
    )


@router.get("/{departamento_id}/edit",
            response_class=HTMLResponse)
async def get(request: Request, localidad_id: int):
    response = requests.get(
        f"http://localhost:8000/localidades/{localidad_id}",
        headers=headers)
    return templates.TemplateResponse(
        "edit_localidad.html",
        {"request": request, "localidad": response.json()}
    )


@router.post("/{localidad_id}/edit",
             response_class=HTMLResponse)
async def put_departamento(request: Request,
                           localidad_id: int):
    form = await request.form()
    json = {
        'nombre': form.get('nombre'),
        'id': form.get('id'),
        'departamento_id': form.get('departamento_id')
    }
    response = requests.put(
        f"http://localhost:8000/localidades/{localidad_id}",
        headers=headers,
        json=json
    )
    if response.status_code == 400:
        error = response.json()['detail']
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": error}
        )
    return RedirectResponse(url="localidades")
