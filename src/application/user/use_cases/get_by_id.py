from src.application.common.use_cases import BaseUseCase
from src.application.user.dto import UserResponseDTO
from src.application.user.exceptions.user import UserIdNotExist


class GetUserById(BaseUseCase):
    async def __call__(self, id: int) -> UserResponseDTO | None:
        user = await self.user_repo.get_by_id(id)
        if not user:
            raise UserIdNotExist(id)
        return UserResponseDTO(id=user.id, username=user.username, email=user.email)
