from src.application.user.exceptions import UserIdNotExists
from src.application.user.protocols import SessionService
from src.infrastructure.database.repositories.user import UserRepo


class DeleteUser:
    def __init__(self, user_repo: UserRepo, session_service: SessionService) -> None:
        self.user_repo = user_repo
        self.session_service = session_service

    async def __call__(self, session_id: str) -> None:
        user_id = await self.session_service.get(session_id)
        user = await self.user_repo.get_by_id(user_id)
        if not user:
            raise UserIdNotExists(user_id)
        await self.user_repo.delete_user(user)
