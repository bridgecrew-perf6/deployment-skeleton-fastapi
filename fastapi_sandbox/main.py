from fastapi import FastAPI, APIRouter

from fastapi_sandbox.views.readiness import router as readiness_router
from fastapi_sandbox.views.views import router as views_router

app = FastAPI()

root_router = APIRouter(prefix="/api")

root_router.include_router(readiness_router)
root_router.include_router(views_router)

app.include_router(root_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True, debug=True)
