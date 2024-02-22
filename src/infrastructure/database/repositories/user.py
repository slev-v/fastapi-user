from collections.abc import Iterable

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.application.common.dto import Pagination

from src.domain.user import entities
from src.infrastructure.database.models import User
from src.infrastructure.database.repositories.user_protocol import UserRepo


class UserRepoImp(UserRepo):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_username(self, username: str) -> entities.User | None:
        user = await self._session.scalar(
            select(entities.User).where(User.username == username)
        )
        return user

    async def get_by_id(self, id: int) -> entities.User | None:
        user = await self._session.get(entities.User, id)
        return user

    async def get_by_email(self, email: str) -> entities.User | None:
        user = await self._session.scalar(
            select(entities.User).where(User.email == email)
        )
        return user

    async def get_users(self, pagination: Pagination) -> Iterable[entities.User]:
        users = await self._session.scalars(
            select(entities.User).limit(pagination.limit).offset(pagination.offset)
        )
        return users

    async def create_user(self, user: entities.User) -> None:
        self._session.add(user)
        await self._session.commit()

    async def delete_user(self, user: entities.User) -> None:
        await self._session.delete(user)
        await self._session.commit()
