from fastapi import FastAPI

from .user.router import router as user_router


def setup_routers(app: FastAPI) -> None:
    app.include_router(user_router)
