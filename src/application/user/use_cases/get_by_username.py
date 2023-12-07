from src.application.common.use_cases.base_user import BaseUseCase
from src.application.user.dto.user_dto import UserResponseDTO


class GetUserByUsername(BaseUseCase):
    async def __call__(self, username: str) -> UserResponseDTO | None:
        user = await self.user_repo.get_by_username(username)
        if not user:
            return None
        return UserResponseDTO(id=user.id, username=user.username, email=user.email)
