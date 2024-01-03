from src.application.common.use_cases.base_user import BaseUseCase
from src.application.user.exceptions.user import UsernameNotExist


class DeleteUser(BaseUseCase):
    async def __call__(self, username: str) -> None:
        user = await self.user_repo.get_by_username(username)
        if not user:
            raise UsernameNotExist(username)
        await self.user_repo.delete_user(user)
