from typing import List, Optional

from fastapi import APIRouter, Depends, Query, HTTPException
from pydantic.types import PositiveInt
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from fastapi_sandbox.dependencies import get_db
from fastapi_sandbox.handlers import entity as handlers
from fastapi_sandbox.schemas import EntityPd, CreateEntityPd, UpdateEntityPd

router = APIRouter(prefix="/entity", tags=["entity"])


@router.get("/list", response_model=List[EntityPd])
def get_entity_list(
    field: Optional[int] = Query(None), db: Session = Depends(get_db)
) -> List[EntityPd]:
    return handlers.get_entity_list(db, field)


@router.get("/{pk}")
def get_entity(entity_id: PositiveInt, db: Session = Depends(get_db)) -> EntityPd:
    try:
        entity = handlers.get_entity(entity_id, db)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="not found")
    return entity


@router.post("/", response_model=EntityPd, status_code=201)
def create_entity(
    entity: CreateEntityPd, db: Session = Depends(get_db)
) -> EntityPd:
    return handlers.create_entity(entity, db)


@router.patch("/{pk}")
def update_entity(
    entity_id: PositiveInt, entity: UpdateEntityPd, db: Session = Depends(get_db)
) -> EntityPd:
    try:
        entity = handlers.update_entity(entity_id, entity, db)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="not found")
    return entity


@router.delete("/{pk}")
def delete_entity(entity_id: PositiveInt, db: Session = Depends(get_db)) -> None:
    count = handlers.delete_entity(entity_id, db)
    if count == 0:
        raise HTTPException(status_code=404, detail="not found")
