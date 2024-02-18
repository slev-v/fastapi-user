import pytest

from src.application.user.dto import UserRequestDTO
from src.application.user.exceptions.user import (
    EmailAlreadyExists,
    UsernameAlreadyExists,
)
from src.application.user.use_cases.new_user import NewUser
from src.domain.user.entities.value_objects.email import WrongEmailValue
from src.domain.user.entities.value_objects.raw_password import WrongPasswordValue
from src.domain.user.entities.value_objects.username import WrongUsernameValue
from tests.mocks import HasherPasswordMock, UserRepoMock


@pytest.mark.asyncio
async def test_new_user_creation(
    user_repo: UserRepoMock, hasher_password: HasherPasswordMock
) -> None:
    new_user = NewUser(user_repo, hasher_password)

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


@pytest.mark.asyncio
async def test_new_user_with_invalid_password(user_repo: UserRepoMock) -> None:
    new_user = NewUser(user_repo, HasherPasswordMock())

    user_data = UserRequestDTO(
        email="test@example.com", username="test_user", password="Testtest1"
    )

    with pytest.raises(WrongPasswordValue):
        await new_user(user_data)


@pytest.mark.asyncio
async def test_new_user_with_invalid_email(user_repo: UserRepoMock) -> None:
    new_user = NewUser(user_repo, HasherPasswordMock())

    user_data = UserRequestDTO(
        email="test", username="test_user", password="Testtest1!"
    )

    with pytest.raises(WrongEmailValue):
        await new_user(user_data)


@pytest.mark.asyncio
async def test_new_user_with_invalid_username(user_repo: UserRepoMock) -> None:
    new_user = NewUser(user_repo, HasherPasswordMock())

    user_data = UserRequestDTO(
        email="test@example.com", username="1test", password="Testtest1!"
    )

    with pytest.raises(WrongUsernameValue):
        await new_user(user_data)


@pytest.mark.asyncio
async def test_new_user_with_existing_username(user_repo: UserRepoMock) -> None:
    new_user = NewUser(user_repo, HasherPasswordMock())

    user_data = UserRequestDTO(
        email="test@example.com", username="test_user", password="Testtest1!"
    )
    await new_user(user_data)

    existing_user = UserRequestDTO(
        email="test1@example.com", username="test_user", password="Testtest1!"
    )

    with pytest.raises(UsernameAlreadyExists):
        await new_user(existing_user)


@pytest.mark.asyncio
async def test_new_user_with_existing_email(user_repo: UserRepoMock) -> None:
    new_user = NewUser(user_repo, HasherPasswordMock())

    user_data = UserRequestDTO(
        email="test@example.com", username="test_user", password="Testtest1!"
    )
    await new_user(user_data)

    existing_user = UserRequestDTO(
        email="test@example.com", username="test_user1", password="Testtest1!"
    )

    with pytest.raises(EmailAlreadyExists):
        await new_user(existing_user)
