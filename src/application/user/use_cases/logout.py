from src.application.user.protocols import SessionService
from src.infrastructure.database.repositories.user import UserRepo


class UserLogout:
    def __init__(self, user_repo: UserRepo, session_service: SessionService):
        self.user_repo = user_repo
        self.session_service = session_service

    async def __call__(self, session_id: str) -> None:
        await self.session_service.delete_session(session_id)
