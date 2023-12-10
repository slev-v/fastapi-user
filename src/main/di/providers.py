from fastapi import Cookie, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.user.exceptions.user import AuthError
from src.application.user.protocols.jwt_service import JwtService
from src.application.user.services import HasherPasswordImp
from src.application.user.services.jwt_service import JwtServiceImp
from src.infrastructure.database.repositories.user import UserRepo
from src.main.config import WebConfig
from src.main.di.stub import get_session_stub, provide_jwt_service_stub


async def provide_user_repo(
    session: AsyncSession = Depends(get_session_stub),
) -> UserRepo:
    return UserRepo(session)


def provide_hasher_password() -> HasherPasswordImp:
    return HasherPasswordImp()


def provide_jwt_service(config: WebConfig) -> JwtServiceImp:
    return JwtServiceImp(config)


async def get_username_from_cookie(
    access_token: str = Cookie(),
    jwt_service: JwtService = Depends(provide_jwt_service_stub),
) -> str:
    try:
        payload = jwt_service.decode(access_token)
    except AuthError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    return payload["sub"]
