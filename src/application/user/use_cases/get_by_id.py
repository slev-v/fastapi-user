from src.application.common.use_cases.base_user import BaseUseCase
from src.database.models.user import User


class GetUserById(BaseUseCase):
    async def __call__(self, id: int) -> User | None:
        return await self.user_repo.get_by_id(id)
