from fastapi import APIRouter

router = APIRouter(prefix="/readiness")


@router.get("/")
def readiness():
    pass
