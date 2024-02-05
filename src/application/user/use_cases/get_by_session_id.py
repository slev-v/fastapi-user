from src.application.user.dto import UserResponseDTO
from src.application.user.exceptions import UserIdNotExist
from src.application.user.protocols import SessionService
from src.infrastructure.database.repositories.user import UserRepo


class GetUserBySessionId:
    def __init__(
        self,
        user_repo: UserRepo,
        session_service: SessionService,
    ):
        self.user_repo = user_repo
        self.session_service = session_service

    async def __call__(self, session_id: str) -> UserResponseDTO:
        user_id = await self.session_service.get(session_id)
        user = await self.user_repo.get_by_id(user_id)
        if user is None:
            raise UserIdNotExist(user_id)
        return UserResponseDTO(
            user_id=user.id, username=user.username, email=user.email
        )
