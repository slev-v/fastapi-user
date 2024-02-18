from collections.abc import Iterable
from typing import Protocol
from src.domain.user import entities
from src.domain.user.entities import User


class UserRepo(Protocol):
    async def get_by_username(self, username: str) -> User | None:
        raise NotImplementedError

    async def get_by_id(self, id: int) -> User | None:
        raise NotImplementedError

    async def get_by_email(self, email: str) -> User | None:
        raise NotImplementedError

    async def get_users(self) -> Iterable[entities.User]:
        raise NotImplementedError

    async def create_user(self, user: User) -> None:
        raise NotImplementedError

    async def delete_user(self, user: User) -> None:
        raise NotImplementedError
