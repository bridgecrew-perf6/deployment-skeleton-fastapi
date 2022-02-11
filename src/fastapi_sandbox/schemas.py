from pydantic import BaseModel, Field


class OrmBaseModel(BaseModel):
    class Config:
        orm_mode = True


class IdMixin(OrmBaseModel):
    id: int


class CreateEntityPd(OrmBaseModel):
    field: int


class UpdateEntityPd(OrmBaseModel):
    field: int | None = Field(None)


class EntityPd(IdMixin, CreateEntityPd):
    pass
