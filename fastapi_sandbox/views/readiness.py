from fastapi import APIRouter

router = APIRouter(prefix="/readiness", tags=["readiness"])


@router.get("/")
def readiness():
    pass
