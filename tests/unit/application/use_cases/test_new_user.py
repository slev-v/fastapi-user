import pytest

from src.application.user.dto import UserRequestDTO
from src.application.user.use_cases.new_user import NewUser
from tests.mocks import HasherPasswordMock, UserRepoMock


@pytest.mark.asyncio
async def test_new_user_creation(
    user_repo: UserRepoMock, hasher_password: HasherPasswordMock
):
    new_user = NewUser(user_repo, hasher_password)  # type: ignore

    user_data = UserRequestDTO(
        email="test@example.com", username="test_user", password="Testtest1!"
    )

    user_id = await new_user(user_data)

    created_user = user_repo.users[user_id]

    assert user_id == created_user.id
    assert created_user.username == user_data.username
    assert created_user.email == user_data.email
    assert created_user.hashed_password.value == hasher_password.get_password_hash(
        user_data.password
    )
