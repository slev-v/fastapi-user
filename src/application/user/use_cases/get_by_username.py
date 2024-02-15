from src.application.user.dto import UserResponseDTO
from src.application.user.exceptions import UsernameNotExists
from src.infrastructure.database.repositories.user import UserRepo


class GetUserByUsername:
    def __init__(self, user_repo: UserRepo) -> None:
        self.user_repo = user_repo

    async def __call__(self, username: str) -> UserResponseDTO:
        user = await self.user_repo.get_by_username(username)
        if not user:
            raise UsernameNotExists(username)
        return UserResponseDTO(
            user_id=user.id, username=user.username, email=user.email
        )
