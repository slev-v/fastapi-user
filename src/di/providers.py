from fastapi import Cookie, Depends, Header, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.user.entities.user import User
from src.application.user.exceptions.user import AuthError
from src.application.user.services import HasherPasswordImp
from src.application.user.services.jwt_service import JwtServiceImp
from src.database.repositories.user import UserRepo
from src.di.stub import get_session_stub


async def provide_user_repo(
    session: AsyncSession = Depends(get_session_stub),
) -> UserRepo:
    return UserRepo(session)


def provide_hasher_password() -> HasherPasswordImp:
    return HasherPasswordImp()


def provide_jwt_service() -> JwtServiceImp:
    return JwtServiceImp()


async def get_user_by_cookie(
    access_token: str = Cookie(),
    user_repo: UserRepo = Depends(provide_user_repo),
    jwt_service: JwtServiceImp = Depends(provide_jwt_service),
) -> User:
    try:
        payload = jwt_service.decode(access_token)
    except AuthError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    user = await user_repo.get_by_username(payload["sub"])
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user
