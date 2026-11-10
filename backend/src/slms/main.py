
from fastapi import FastAPI

from slms.api.v1.routers import register_routers
from slms.core.exceptions import register_exception_handlers
from slms.core.lifespan import lifespan


def create_app() -> FastAPI:
    """
    Application factory.

    Creates and configures the FastAPI application.
    """

    app = FastAPI(
        title="SLMS Backend",
        description=(
            "Central service responsible for managing and coordinating "
            "the operations of The Smart Laundry Management System"
        ),
        version="0.1.0",
        lifespan=lifespan,
    )

    register_exception_handlers(app)
    register_routers(app)

    return app


app = create_app()