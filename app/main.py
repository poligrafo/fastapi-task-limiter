import logging
from fastapi import FastAPI

from app.api.routes import router
from app.core.logging_config import setup_logging

def create_app() -> FastAPI:
    setup_logging()

    application = FastAPI(
        title="FastAPI Task Limiter",
        description="A service to manage task execution with time limits.",
        version="1.0.0",
    )

    application.include_router(router)

    logger = logging.getLogger("app")
    logger.info("Application startup complete")

    return application

app = create_app()
