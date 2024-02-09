import redis.asyncio as redis
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.user.protocols import SessionService
from src.application.user.services import HasherPasswordImp, SessionServiceImp
from src.application.user.use_cases import (
    DeleteUser,
    GetUserById,
    GetUserBySessionId,
    GetUserByUsername,
    GetUsers,
    NewUser,
    UserLogin,
    UserLogout,
)
from src.infrastructure.database.repositories.user import UserRepo
from src.infrastructure.redis.repositories import RedisRepository
from src.main.config import WebConfig
from src.main.di.stub import (
    get_redis_stub,
    get_session_stub,
    provide_hasher_password_stub,
    provide_session_service_stub,
    provide_user_repo_stub,
)


async def provide_user_repo(
    session: AsyncSession = Depends(get_session_stub),
) -> UserRepo:
    return UserRepo(session)


async def provide_redis_repo(
    connection: redis.Redis = Depends(get_redis_stub),
) -> RedisRepository:
    return RedisRepository(connection)


def provide_session_service(
    config: WebConfig, redis_repo: RedisRepository = Depends(provide_redis_repo)
) -> SessionService:
    return SessionServiceImp(config, redis_repo)


def provide_hasher_password() -> HasherPasswordImp:
    return HasherPasswordImp()


async def provide_get_users(
    user_repo: UserRepo = Depends(provide_user_repo_stub),
) -> GetUsers:
    return GetUsers(user_repo)


async def provide_delete_user(
    user_repo: UserRepo = Depends(provide_user_repo_stub),
    session_service: SessionService = Depends(provide_session_service_stub),
) -> DeleteUser:
    return DeleteUser(user_repo, session_service)


async def provide_new_user(
    user_repo: UserRepo = Depends(provide_user_repo_stub),
    hasher_password: HasherPasswordImp = Depends(provide_hasher_password_stub),
) -> NewUser:
    return NewUser(user_repo, hasher_password)


async def provide_login(
    user_repo: UserRepo = Depends(provide_user_repo_stub),
    hasher_password: HasherPasswordImp = Depends(provide_hasher_password_stub),
    session_service: SessionService = Depends(provide_session_service_stub),
) -> UserLogin:
    return UserLogin(user_repo, hasher_password, session_service)


async def provide_logout(
    user_repo: UserRepo = Depends(provide_user_repo_stub),
    session_service: SessionService = Depends(provide_session_service_stub),
) -> UserLogout:
    return UserLogout(user_repo, session_service)


async def provide_get_user_by_session_id(
    user_repo: UserRepo = Depends(provide_user_repo_stub),
    session_service: SessionService = Depends(provide_session_service_stub),
) -> GetUserBySessionId:
    return GetUserBySessionId(user_repo, session_service)


async def provide_get_user_by_id(
    user_repo: UserRepo = Depends(provide_user_repo_stub),
) -> GetUserById:
    return GetUserById(user_repo)


async def provide_get_user_by_username(
    user_repo: UserRepo = Depends(provide_user_repo_stub),
) -> GetUserByUsername:
    return GetUserByUsername(user_repo)
