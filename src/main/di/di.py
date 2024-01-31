from functools import partial

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.application.user.use_cases import (DeleteUser, GetUserById,
                                            GetUserByUsername, GetUsers,
                                            NewUser, UserLogin)
from src.infrastructure.redis import create_redis_pool, new_redis_connection
from src.main.config import WebConfig
from src.main.di.providers import (get_username_from_cookie,
                                   provide_hasher_password,
                                   provide_jwt_service, provide_user_repo)
from src.main.di.stub import (delete_user_stub, get_redis_stub,
                              get_session_stub, get_user_by_id_stub,
                              get_user_by_username_stub,
                              get_username_from_cookie_stub, get_users_stub,
                              new_user_stub, provide_hasher_password_stub,
                              provide_jwt_service_stub, provide_user_repo_stub,
                              user_login_stub)


def create_session_maker(config: WebConfig):
    db_uri = config.async_db_uri

    engine = create_async_engine(db_uri, echo=True, pool_size=15, max_overflow=15)
    return async_sessionmaker(engine, autoflush=False, expire_on_commit=False)


async def new_session(session_maker):
    async with session_maker() as session:
        yield session


def init_dependencies(app: FastAPI, config: WebConfig):
    session_maker = create_session_maker(config)
    redis_pool = create_redis_pool(config)
    app.dependency_overrides[get_session_stub] = partial(new_session, session_maker)
    app.dependency_overrides[get_redis_stub] = partial(new_redis_connection, redis_pool)
    app.dependency_overrides[provide_user_repo_stub] = provide_user_repo
    app.dependency_overrides[provide_hasher_password_stub] = provide_hasher_password
    app.dependency_overrides[provide_jwt_service_stub] = partial(
        provide_jwt_service, config
    )
    app.dependency_overrides[get_username_from_cookie_stub] = get_username_from_cookie
    app.dependency_overrides[delete_user_stub] = DeleteUser
    app.dependency_overrides[user_login_stub] = UserLogin
    app.dependency_overrides[get_users_stub] = GetUsers
    app.dependency_overrides[get_user_by_id_stub] = GetUserById
    app.dependency_overrides[get_user_by_username_stub] = GetUserByUsername
    app.dependency_overrides[new_user_stub] = NewUser
