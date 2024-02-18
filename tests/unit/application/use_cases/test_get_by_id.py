import pytest

from src.application.user.dto.user import UserRequestDTO
from src.application.user.exceptions.user import UserIdNotExists
from src.application.user.use_cases.get_by_id import GetUserById
from src.application.user.use_cases.new_user import NewUser
from tests.mocks import HasherPasswordMock, UserRepoMock


@pytest.mark.asyncio
async def test_get_by_id(
    user_repo: UserRepoMock,
    hasher_password: HasherPasswordMock,
) -> None:
    new_user = NewUser(user_repo, hasher_password)
    user_data = UserRequestDTO(
        email="test@example.com", username="test_user", password="Testtest1!"
    )
    user_id = await new_user(user_data)

    get_by_id = GetUserById(user_repo)
    user = await get_by_id(user_id)

    assert user.user_id == user_id
    assert user.username == "test_user"
    assert user.email == "test@example.com"


@pytest.mark.asyncio
async def test_get_by_id_user_id_not_exists(
    user_repo: UserRepoMock,
) -> None:
    get_by_id = GetUserById(user_repo)
    with pytest.raises(UserIdNotExists):
        await get_by_id(1)
