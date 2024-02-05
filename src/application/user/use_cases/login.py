from src.application.user.dto import UserLoginRequestDTO
from src.application.user.exceptions import InvalidPassword, UserIdNotExist
from src.application.user.protocols import HasherPassword, SessionService
from src.infrastructure.database.repositories.user import UserRepo


class UserLogin:
    def __init__(
        self,
        user_repo: UserRepo,
        hasher_password: HasherPassword,
        session_service: SessionService,
    ):
        self.user_repo = user_repo
        self.hasher_password = hasher_password
        self.session_service = session_service

    async def __call__(self, data: UserLoginRequestDTO) -> str:
        user_id = data.user_id
        password = data.password

        user = await self.user_repo.get_by_id(user_id)
        if user is None:
            raise UserIdNotExist(user_id)
        if not self.hasher_password.verify_password(
            plain_password=password, hashed_password=user.hashed_password
        ):
            raise InvalidPassword()
        session_id = await self.session_service.create_session(user_id=user.id)
        return session_id
