from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator, EmailStr

class ProvinciaSchema(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True


class ProvinciasSchemaSimple(BaseModel):
    nombre: str
   
    class Config:
        orm_mode = True