from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.user.services import HasherPasswordImp
from src.database.repositories.user import UserRepo
from src.di.stub import get_session_stub


async def provide_user_repo(
    session: AsyncSession = Depends(get_session_stub),
) -> UserRepo:
    return UserRepo(session)


def provide_hasher_password() -> HasherPasswordImp:
    return HasherPasswordImp()
