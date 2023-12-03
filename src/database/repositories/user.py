from collections.abc import Iterable

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import User

from .base import SQLAlchemyRepo


class UserRepo(SQLAlchemyRepo):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_by_username(self, username: str) -> User | None:
        user: User | None = await self._session.scalar(
            select(User).where(User.username == username)
        )
        return user

    async def get_by_id(self, id: int) -> User | None:
        user: User | None = await self._session.get(User, id)
        return user

    async def get_users(self) -> Iterable[User]:
        users: Iterable[User] = await self._session.scalars(select(User))
        return users

    async def create_user(self, username: str, email: str, password: str) -> User:
        user = User(username=username, email=email, password=password)
        self._session.add(user)
        await self._session.flush()
        await self._session.commit()
        return user
