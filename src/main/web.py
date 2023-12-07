from fastapi import FastAPI

from src.database.models.mapping import start_mappers
from src.di.di import init_dependencies
from src.main.config import load_web_config
from src.presentation.api.routes import setup_routers


def init_api() -> FastAPI:
    app = FastAPI(title="Second Life")
    config = load_web_config()
    start_mappers()
    load_web_config()
    init_dependencies(app, config)
    setup_routers(app)
    return app
