from typing import List

from pydantic import BaseModel


class DepartamentosSchemaSimple(BaseModel):  # noqa
    nombre: str
    provincia_id: int

    class Config:
        orm_mode = True


class DepartamentoSchema(DepartamentosSchemaSimple):  # noqa
    id: int

    class Config:
        orm_mode = True


class ResponseGetAllSchemas(BaseModel):
    data: List[DepartamentoSchema]
