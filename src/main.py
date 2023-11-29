from fastapi import FastAPI

from src.api import setup_routers
from src.config import load_web_config
from src.di import init_dependencies


def init_api() -> FastAPI:
    app = FastAPI(title="Second Life")
    config = load_web_config()
    load_web_config()
    init_dependencies(app, config)
    setup_routers(app)
    return app
