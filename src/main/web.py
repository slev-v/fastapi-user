from fastapi import FastAPI

from src.infrastructure.database.models.mapping import start_mappers
from src.main.config import load_web_config
from src.main.di.di import init_dependencies
from src.presentation.api.exceptions import setup_exception_handlers
from src.presentation.api.routes import setup_routers


def init_api() -> FastAPI:
    app = FastAPI(title="Second Life")
    config = load_web_config()
    start_mappers()
    setup_exception_handlers(app)
    init_dependencies(app, config)
    setup_routers(app)
    return app
