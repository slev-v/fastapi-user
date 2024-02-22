from src.application.user.dto import UserResponseDTO, UsersResponseDTO
from src.application.user.dto.user import UsersRequestDTO
from src.infrastructure.database.repositories.user import UserRepo


class GetUsers:
    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    async def __call__(self, data: UsersRequestDTO) -> UsersResponseDTO:
        users = await self.user_repo.get_users(data.pagination)
        users_response: list[UserResponseDTO] = []
        for user in users:
            users_response.append(
                UserResponseDTO(
                    user_id=user.id,
                    username=user.username,
                    email=user.email,
                )
            )
        return UsersResponseDTO(users=users_response)
