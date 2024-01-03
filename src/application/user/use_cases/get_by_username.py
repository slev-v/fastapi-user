from src.application.common.use_cases import BaseUseCase
from src.application.user.dto import UserResponseDTO
from src.application.user.exceptions.user import UsernameNotExist


class GetUserByUsername(BaseUseCase):
    async def __call__(self, username: str) -> UserResponseDTO | None:
        user = await self.user_repo.get_by_username(username)
        if not user:
            raise UsernameNotExist(username)
        return UserResponseDTO(id=user.id, username=user.username, email=user.email)
