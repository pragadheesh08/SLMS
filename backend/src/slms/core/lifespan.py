
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from slms.core.config import get_settings
from slms.core.logging import setup_logging

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown lifecycle.
    """
    settings = get_settings()
    setup_logging(settings.LOG_DIR)
    logger.info("Application startup initiated")

    try:
        logger.info("Application startup completed")
        yield
    finally:
        logger.info("Application shut down completed")
        pass

