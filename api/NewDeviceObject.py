from typing import Annotated, List
from pydantic import BaseModel, constr, Field, field_validator
from datetime import datetime

class Producto(BaseModel):
    nombre: Annotated[str, constr(min_length=1, strip_whitespace=True)]
    categoria: Annotated[str, constr(min_length=1, strip_whitespace=True)]
    watts: int
    color: Annotated[str, constr(min_length=1, strip_whitespace=True)]
    state: bool = True
    created_at: List[datetime] = Field(default_factory=lambda: [datetime.utcnow().isoformat()])
    email: Annotated[str, constr(min_length=1, strip_whitespace=True)]
    favorite: bool = False
    team: Annotated[str, constr(min_length=1, strip_whitespace=True)]

    @field_validator('watts')
    @classmethod
    def validar_watts_positivo(cls, valor):
        if valor <= 0:
            raise ValueError('El valor de los watts debe ser positivo')
        return valor