from typing import Any

from pydantic import BaseModel, Field


class OrmBaseModel(BaseModel):
    class Config:
        orm_mode = True

    @classmethod
    def from_orm_trusted(cls, orm_obj: Any) -> "OrmBaseModel":
        values = {field_name: getattr(orm_obj, field_name) for field_name in cls.__fields__.keys()}
        return cls.construct(**values)


class IdMixin(OrmBaseModel):
    id: int


class EntityCreatePd(OrmBaseModel):
    field: int


class EntityReadPd(IdMixin, EntityCreatePd):
    pass


class EntityUpdatePd(OrmBaseModel):
    field: int | None = Field(None)


class EntityPd(IdMixin, EntityCreatePd):
    pass
