from functools import partial

from fastapi import FastAPI

from src.infrastructure.database import create_session_maker, new_session
from src.infrastructure.redis import create_redis_pool, new_redis_connection
from src.presentation.api.config import WebConfig
from src.presentation.api.di.providers import (
    provide_delete_user,
    provide_get_user_by_id,
    provide_get_user_by_session_id,
    provide_get_user_by_username,
    provide_get_users,
    provide_hasher_password,
    provide_login,
    provide_logout,
    provide_new_user,
    provide_redis_repo,
    provide_session_service,
    provide_user_repo,
)
from src.presentation.api.di.stub import (
    get_redis_stub,
    get_session_stub,
    provide_delete_user_stub,
    provide_get_user_by_id_stub,
    provide_get_user_by_session_id_stub,
    provide_get_user_by_username_stub,
    provide_get_users_stub,
    provide_hasher_password_stub,
    provide_login_stub,
    provide_logout_stub,
    provide_new_user_stub,
    provide_redis_repo_stub,
    provide_session_service_stub,
    provide_user_repo_stub,
)


def init_dependencies(app: FastAPI, config: WebConfig) -> None:
    session_maker = create_session_maker(config)
    redis_pool = create_redis_pool(config)
    app.dependency_overrides[get_session_stub] = partial(new_session, session_maker)
    app.dependency_overrides[get_redis_stub] = partial(new_redis_connection, redis_pool)
    app.dependency_overrides[provide_user_repo_stub] = provide_user_repo
    app.dependency_overrides[provide_redis_repo_stub] = provide_redis_repo
    app.dependency_overrides[provide_hasher_password_stub] = provide_hasher_password
    app.dependency_overrides[provide_session_service_stub] = partial(
        provide_session_service, config
    )
    app.dependency_overrides[provide_get_users_stub] = provide_get_users
    app.dependency_overrides[provide_delete_user_stub] = provide_delete_user
    app.dependency_overrides[provide_new_user_stub] = provide_new_user
    app.dependency_overrides[provide_login_stub] = provide_login
    app.dependency_overrides[provide_logout_stub] = provide_logout
    app.dependency_overrides[
        provide_get_user_by_session_id_stub
    ] = provide_get_user_by_session_id
    app.dependency_overrides[provide_get_user_by_id_stub] = provide_get_user_by_id
    app.dependency_overrides[
        provide_get_user_by_username_stub
    ] = provide_get_user_by_username
