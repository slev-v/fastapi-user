from fastapi import FastAPI

from src.api import setup_routers


def init_api() -> FastAPI:
    app = FastAPI(title="Second Life")
    setup_routers(app)
    return app
