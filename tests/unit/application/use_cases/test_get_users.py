from typing import List
import pytest

from src.application.user.dto import UserRequestDTO
from src.application.user.use_cases.get_users import GetUsers
from src.application.user.use_cases.new_user import NewUser
from tests.mocks import HasherPasswordMock, UserRepoMock


@pytest.fixture
def users() -> List[UserRequestDTO]:
    users: List[UserRequestDTO] = [
        UserRequestDTO("test1", "test1@example.com", "Testtest1!"),
        UserRequestDTO("test2", "test2@example.com", "Testtest2!"),
        UserRequestDTO("test3", "test3@example.com", "Testtest3!"),
    ]
    return users


@pytest.mark.asyncio
async def test_get_users(
    users: List[UserRequestDTO],
    user_repo: UserRepoMock,
    hasher_password: HasherPasswordMock,
) -> None:
    new_user = NewUser(user_repo, hasher_password)
    for user in users:
        await new_user(user)

    get_users = GetUsers(user_repo)
    result = await get_users()

    result_list = [
        {"user_id": user.user_id, "username": user.username, "email": user.email}
        for user in result.users
    ]
    expected = [
        {"user_id": id + 1, "username": user.username, "email": user.email}
        for id, user in enumerate(users)
    ]

    assert result_list == expected
