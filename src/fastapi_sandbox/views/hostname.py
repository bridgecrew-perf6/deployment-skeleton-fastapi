import os

from fastapi import APIRouter

router = APIRouter(prefix="/hostname", tags=["hostname"])


@router.get("/")
def get_hostname():
    return os.uname()[1]
