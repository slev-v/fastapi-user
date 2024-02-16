import pytest

from src.application.user.dto import UserRequestDTO
from src.application.user.exceptions.user import UsernameNotExists
from src.application.user.use_cases.new_user import NewUser
from src.application.user.use_cases.get_by_username import GetUserByUsername
from tests.mocks import UserRepoMock, HasherPasswordMock


@pytest.mark.asyncio
async def test_get_by_username(
    user_repo: UserRepoMock,
    hasher_password: HasherPasswordMock,
):
    new_user = NewUser(user_repo, hasher_password)  # type: ignore
    user_data = UserRequestDTO(
        email="test@example.com", username="test_user", password="Testtest1!"
    )
    user_id = await new_user(user_data)

    get_by_username = GetUserByUsername(user_repo)  # type: ignore
    user = await get_by_username("test_user")

    assert user.username == "test_user"
    assert user.email == "test@example.com"
    assert user.user_id == user_id


@pytest.mark.asyncio
async def test_get_by_username_not_exists(
    user_repo: UserRepoMock,
):
    get_by_username = GetUserByUsername(user_repo)  # type: ignore
    with pytest.raises(UsernameNotExists):
        await get_by_username("test_user")
