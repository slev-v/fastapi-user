from src.application.common.use_cases.base_user import BaseUseCase
from src.application.user.dto.user_dto import UserResponseDTO, UsersResponseDTO


class GetUsers(BaseUseCase):
    async def __call__(self) -> UsersResponseDTO:
        users = await self.user_repo.get_users()
        users_response: list[UserResponseDTO] = []
        for user in users:
            users_response.append(
                UserResponseDTO(
                    id=user.id,
                    username=user.username,
                    email=user.email,
                )
            )
        return UsersResponseDTO(users=users_response)
