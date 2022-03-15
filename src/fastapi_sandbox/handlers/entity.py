from sqlalchemy.orm import Session

from fastapi_sandbox.models import EntityOrm
from fastapi_sandbox.schemas import EntityCreatePd, EntityReadPd, \
    EntityUpdatePd


def get_entity_list(
    db: Session, field: int | None = None
) -> list[EntityReadPd]:
    return [
        EntityReadPd.from_orm_trusted(entity) for entity in EntityOrm.get_list(db, field)
    ]


def get_entity(pk: int, db: Session) -> EntityReadPd:
    entity = EntityOrm.get(pk, db)
    return EntityReadPd.from_orm_trusted(entity)


def create_entity(entity: EntityCreatePd, db: Session) -> EntityReadPd:
    entity = EntityOrm.create(entity, db)
    return EntityReadPd.from_orm_trusted(entity)


def update_entity(pk: int, entity: EntityUpdatePd, db: Session) -> EntityReadPd:
    entity = EntityOrm.update(pk, entity, db)
    return EntityReadPd.from_orm_trusted(entity)


def delete_entity(pk: int, db: Session) -> int:
    return EntityOrm.delete(pk, db)
