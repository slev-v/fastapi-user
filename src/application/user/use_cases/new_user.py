from src.application.user.dto import UserRequestDTO
from src.application.user.exceptions import EmailAlreadyExists, UsernameAlreadyExists
from src.application.user.protocols import HasherPassword
from src.domain.user import entities
from src.domain.user.entities import value_objects as vo
from src.infrastructure.database.repositories.user import UserRepo


class NewUser:
    def __init__(
        self,
        user_repo: UserRepo,
        hasher_password: HasherPassword,
    ) -> None:
        self.user_repo = user_repo
        self.hasher_password = hasher_password

    async def __call__(
        self,
        data: UserRequestDTO,
    ) -> int:
        email = data.email
        username = data.username
        password = data.password
        raw_password = vo.RawPassword(password)
        hashed_password = self.hasher_password.get_password_hash(raw_password.value)

        if await self.user_repo.get_by_email(email):
            raise EmailAlreadyExists(email)
        if await self.user_repo.get_by_username(username):
            raise UsernameAlreadyExists(username)

        user = entities.User(
            username=vo.UserName(username),
            email=vo.Email(email),
            hashed_password=vo.HashedPassword(hashed_password),
        )
        await self.user_repo.create_user(user)
        return user.id
