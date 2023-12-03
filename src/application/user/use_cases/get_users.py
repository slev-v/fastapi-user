from collections.abc import Iterable

from src.application.common.use_cases.base_user import BaseUseCase
from src.database.models.user import User


class GetUsers(BaseUseCase):
    async def __call__(self) -> Iterable[User]:
        return await self.user_repo.get_users()
