from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastapi_sandbox.dependencies import get_db
from fastapi_sandbox.settings import settings

router = APIRouter(prefix="/q")


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/settings")
def get_settings():
    return settings


@router.get("/some_table")
def get_some_table(db: Session = Depends(get_db)):
    return {"q": "w"}
