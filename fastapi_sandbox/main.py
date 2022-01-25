from fastapi import FastAPI, APIRouter

from fastapi_sandbox.settings import settings
from fastapi_sandbox.views.readiness import router as readiness_router
from fastapi_sandbox.views.entity import router as entity_router

app = FastAPI(debug=settings.DEBAG)

root_router = APIRouter(prefix="/api")

public_router = APIRouter(prefix="/public")
private_router = APIRouter(prefix="/private")

private_router.include_router(readiness_router)

public_router.include_router(entity_router)

root_router.include_router(public_router)
root_router.include_router(private_router)

app.include_router(root_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True, debug=True)
