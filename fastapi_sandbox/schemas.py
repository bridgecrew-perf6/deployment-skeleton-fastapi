from pydantic import BaseModel


class SomeModel(BaseModel):
    id: int
    a: int

    class Config:
        orm_mode = True
