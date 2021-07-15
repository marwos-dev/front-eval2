from fastapi import FastAPI, APIRouter, Request
import uvicorn
from controllers.index_controller import router as index_router
from controllers.provincias_controller import router as provincia_router
from controllers.localidades_controller import router as localidades_router
from controllers.departamentos_controller import router as departamentos_router
# Aplicacion
app = FastAPI()

# Rutas API
api_router = APIRouter()

app.include_router(index_router, tags=["Index"])

app.include_router(provincia_router,
                   tags=["Provincias"],
                   prefix="/provincias")
app.include_router(localidades_router,
                   tags=["Localidades"],
                   prefix="/localidades")
app.include_router(departamentos_router,
                   tags=["Departamentos"],
                   prefix="/departamentos")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
