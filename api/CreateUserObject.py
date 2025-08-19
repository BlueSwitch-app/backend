from pydantic import BaseModel, constr, Field, field_validator
from typing import Annotated, List
class User(BaseModel):
    nombre: Annotated[str, constr(min_length=1, strip_whitespace=True)]
    email: Annotated[str, constr(min_length=1, strip_whitespace=True)]
    password: Annotated[str, constr(min_length=1, strip_whitespace=True)]
    phone: Annotated[str, constr(min_length=1, strip_whitespace=True)]
    city: Annotated[str, constr(min_length=1, strip_whitespace=True)]
    avatar: Annotated[str, constr(min_length=1, strip_whitespace=True)]= "https://res.cloudinary.com/dkjlygxse/image/upload/v1746846631/is-there-a-sniper-default-pfp-that-someone-made-v0-78az45pd9f6c1_ymnf4h.webp"