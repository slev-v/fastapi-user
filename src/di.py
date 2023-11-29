from functools import partial

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.config import WebConfig
from src.stub import get_session_stub


def create_session_maker(config: WebConfig):
    db_uri = config.async_db_uri
    if not db_uri:
        raise ValueError("db_uri is not set")

    engine = create_async_engine(db_uri, echo=True, pool_size=15, max_overflow=15)
    return async_sessionmaker(engine, autoflush=False, expire_on_commit=False)


async def new_session(session_maker):
    async with session_maker() as session:
        yield session


def init_dependencies(app: FastAPI, config: WebConfig):
    session_maker = create_session_maker(config)
    app.dependency_overrides[get_session_stub] = partial(new_session, session_maker)
