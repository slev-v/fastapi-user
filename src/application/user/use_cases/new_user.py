from fastapi import Depends

from src.application.common.use_cases import BaseUseCase
from src.application.user import entities
from src.application.user.dto import UserRequestDTO
from src.application.user.entities import value_objects as vo
from src.application.user.exceptions import AuthError
from src.application.user.protocols import HasherPassword
from src.infrastructure.database.repositories.user import UserRepo
from src.main.di.stub import provide_hasher_password_stub, provide_user_repo_stub


class NewUser(BaseUseCase):
    def __init__(
        self,
        user_repo: UserRepo = Depends(provide_user_repo_stub),
        hasher_password: HasherPassword = Depends(provide_hasher_password_stub),
    ):
        super().__init__(user_repo=user_repo)
        self.hasher_password = hasher_password

    async def __call__(
        self,
        data: UserRequestDTO,
    ) -> None:
        email = data.email
        username = data.username
        password = data.password
        try:
            raw_password = vo.RawPassword(password)
            hashed_password = self.hasher_password.get_password_hash(raw_password.value)

            user = entities.User(
                username=vo.UserName(username),
                email=vo.Email(email),
                hashed_password=vo.HashedPassword(hashed_password),
            )
        except ValueError as e:
            raise AuthError(e)
        except TypeError as e:
            raise AuthError(e)
        await self.user_repo.create_user(user)
