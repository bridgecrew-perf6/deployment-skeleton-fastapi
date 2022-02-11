from typing import Any

from sqlalchemy import Integer, Column
from sqlalchemy.orm import declarative_base, Session

from fastapi_sandbox.schemas import CreateEntityPd, UpdateEntityPd

Base: Any = declarative_base()


class EntityOrm(Base):
    __tablename__ = "Entity"
    id = Column(Integer, primary_key=True, autoincrement=True)
    field = Column(Integer)

    @classmethod
    def get_list(
        cls, db: Session, field: int | None = None
    ) -> list["EntityOrm"]:
        query = db.query(cls)
        if field is not None:
            query = query.filter(cls.field == field)
        return query.all()

    @classmethod
    def get(cls, pk: int, db: Session) -> "EntityOrm":
        return db.query(cls).filter(cls.id == pk).one()

    @classmethod
    def create(cls, entity: CreateEntityPd, db: Session) -> "EntityOrm":
        obj = cls(**entity.dict())
        db.add(obj)
        db.commit()
        return obj

    @classmethod
    def update(
        cls, pk: int, entity: UpdateEntityPd, db: Session
    ) -> "EntityOrm":
        obj = db.query(cls).filter(cls.id == pk).one()
        obj.field = entity.field
        db.add(obj)
        db.commit()
        return obj

    @classmethod
    def delete(cls, pk: int, db: Session) -> int:
        count = db.query(cls).filter(cls.id == pk).delete()
        db.commit()
        return count
