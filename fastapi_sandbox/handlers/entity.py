from typing import List, Optional

from sqlalchemy.orm import Session

from fastapi_sandbox.models import EntityOrm
from fastapi_sandbox.schemas import EntityPd, CreateEntityPd, UpdateEntityPd


def get_entity_list(
    db: Session, field: Optional[int] = None
) -> List[EntityPd]:
    return [
        EntityPd.from_orm(entity) for entity in EntityOrm.get_list(db, field)
    ]


def get_entity(pk: int, db: Session) -> EntityPd:
    return EntityPd.from_orm(EntityOrm.get(pk, db))


def create_entity(entity: CreateEntityPd, db: Session) -> EntityPd:
    return EntityPd.from_orm(EntityOrm.create(entity, db))


def update_entity(pk: int, entity: UpdateEntityPd, db: Session) -> EntityPd:
    return EntityPd.from_orm(EntityOrm.update(pk, entity, db))


def delete_entity(pk: int, db: Session) -> int:
    return EntityOrm.delete(pk, db)
