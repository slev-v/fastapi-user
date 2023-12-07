from src.application.common.use_cases import BaseUseCase
from src.application.user.dto import UserResponseDTO


class GetUserById(BaseUseCase):
    async def __call__(self, id: int) -> UserResponseDTO | None:
        user = await self.user_repo.get_by_id(id)
        if not user:
            return None
        return UserResponseDTO(id=user.id, username=user.username, email=user.email)
