from functools import partial

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.application.user.use_cases import (GetUserById, GetUserByUsername,
                                            GetUsers, NewUser)
from src.config import WebConfig
from src.di.providers import provide_user_repo
from src.di.stub import (get_session_stub, get_user_by_id_stub,
                         get_user_by_username_stub, get_users_stub,
                         new_user_stub, provide_user_repo_stub)


def create_session_maker(config: WebConfig):
    db_uri = config.async_db_uri

    engine = create_async_engine(db_uri, echo=True, pool_size=15, max_overflow=15)
    return async_sessionmaker(engine, autoflush=False, expire_on_commit=False)


async def new_session(session_maker):
    async with session_maker() as session:
        yield session


def init_dependencies(app: FastAPI, config: WebConfig):
    session_maker = create_session_maker(config)
    app.dependency_overrides[get_session_stub] = partial(new_session, session_maker)
    app.dependency_overrides[provide_user_repo_stub] = provide_user_repo
    app.dependency_overrides[get_users_stub] = GetUsers
    app.dependency_overrides[get_user_by_id_stub] = GetUserById
    app.dependency_overrides[get_user_by_username_stub] = GetUserByUsername
    app.dependency_overrides[new_user_stub] = NewUser
