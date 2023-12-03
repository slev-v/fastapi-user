from dataclasses import dataclass

from src.application.common.use_cases.base_user import BaseUseCase


@dataclass
class NewUserDTO:
    username: str
    email: str
    password: str


class NewUser(BaseUseCase):
    async def __call__(self, data: NewUserDTO):
        return await self.user_repo.create_user(
            data.username, data.email, data.password
        )
