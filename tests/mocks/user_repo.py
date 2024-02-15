from typing import Dict, List

from src.domain.user import entities


class UserRepoMock:
    def __init__(self):
        self.users: Dict[int, entities.User] = {}
        self.next_user_id = 1

    async def get_by_username(self, username: str) -> entities.User | None:
        for user in self.users.values():
            if user.username == username:
                return user
        return None

    async def get_by_id(self, user_id: int) -> entities.User | None:
        return self.users.get(user_id, None)

    async def get_by_email(self, email: str) -> entities.User | None:
        for user in self.users.values():
            if user.email == email:
                return user
        return None

    async def get_users(self) -> List[entities.User]:
        return list(self.users.values())

    async def create_user(self, user: entities.User) -> entities.User:
        user.id = self.next_user_id
        self.users[user.id] = user
        self.next_user_id += 1
        return user

    async def delete_user(self, user: entities.User) -> None:
        if user.id in self.users:
            del self.users[user.id]
