from fastapi import Depends

from src.application.common.use_cases.base_user import BaseUseCase
from src.application.user.dto import UserLoginRequestDTO
from src.application.user.exceptions.user import AuthError
from src.application.user.protocols.hasher_password import HasherPassword
from src.application.user.protocols.jwt_service import JwtService
from src.database.repositories.user import UserRepo
from src.di.stub import (
    provide_hasher_password_stub,
    provide_jwt_service_stub,
    provide_user_repo_stub,
)


class UserLogin(BaseUseCase):
    def __init__(
        self,
        user_repo: UserRepo = Depends(provide_user_repo_stub),
        hasher_password: HasherPassword = Depends(provide_hasher_password_stub),
        jwt_service: JwtService = Depends(provide_jwt_service_stub),
    ):
        super().__init__(user_repo=user_repo)
        self.hasher_password = hasher_password
        self.jwt_service = jwt_service

    async def __call__(self, data: UserLoginRequestDTO) -> str:
        username = data.username
        password = data.password

        user = await self.user_repo.get_by_username(username)
        if user is None:
            raise AuthError("Invalid username")
        if not self.hasher_password.verify_password(
            plain_password=password, hashed_password=user.hashed_password
        ):
            raise AuthError("Invalid password")

        token = self.jwt_service.encode(username=user.username)
        return token
