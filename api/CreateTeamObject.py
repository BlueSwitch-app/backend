from typing import Annotated
from pydantic import BaseModel, constr, Field
import secrets

class TeamMember(BaseModel):
    email: str
    role: str

class Team(BaseModel):
    Name: Annotated[str, constr(min_length=1, strip_whitespace=True)]
    StringId: str = Field(default_factory=lambda: secrets.token_hex(6))
    Members: list[TeamMember] = []