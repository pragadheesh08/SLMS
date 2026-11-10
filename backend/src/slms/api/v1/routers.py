
from fastapi import APIRouter, FastAPI

from slms.api.v1.health import router as healthRouter


def register_routers(app: FastAPI):
    router = APIRouter(prefix="/api/v1")

    router.include_router(healthRouter)

    app.include_router(router)