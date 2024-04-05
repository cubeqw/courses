# build a schema using pydantic
from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str


    class Config:
        orm_mode = True