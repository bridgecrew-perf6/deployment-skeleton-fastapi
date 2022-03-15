from fastapi import FastAPI, APIRouter

from fastapi_sandbox.settings import settings
from fastapi_sandbox.views.health import router as health_router
from fastapi_sandbox.views.entity import router as entity_router
from fastapi_sandbox.views.hostname import router as hostname_router

app = FastAPI(debug=settings.DEBUG)

root_router = APIRouter(prefix="/api")

public_router = APIRouter(prefix="/public")
private_router = APIRouter(prefix="/private")

private_router.include_router(health_router)

public_router.include_router(entity_router)
public_router.include_router(hostname_router)

root_router.include_router(public_router)
root_router.include_router(private_router)

app.include_router(root_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True, debug=True)
