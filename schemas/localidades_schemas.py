from typing import List

from pydantic import BaseModel


class LocalidadesSchemaSimple(BaseModel):  # noqa
    nombre: str
    departamento_id: int

    class Config:
        orm_mode = True


class LocalidadesSchema(LocalidadesSchemaSimple):  # noqa
    id: int

    class Config:
        orm_mode = True


class ResponseGetAllSchemas(BaseModel):
    data: List[LocalidadesSchema]
