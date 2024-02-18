import pytest

from src.application.user.dto.user import UserLoginRequestDTO, UserRequestDTO
from src.application.user.exceptions.user import (
    InvalidPassword,
    UserIdNotExists,
)
from src.application.user.use_cases.login import UserLogin
from src.application.user.use_cases.new_user import NewUser
from tests.mocks import HasherPasswordMock, SessionServiceMock, UserRepoMock


@pytest.mark.asyncio
async def test_login(
    user_repo: UserRepoMock,
    hasher_password: HasherPasswordMock,
    session_service: SessionServiceMock,
) -> None:
    new_user = NewUser(user_repo, hasher_password)
    user_data = UserRequestDTO(
        email="test@example.com", username="test_user", password="Testtest1!"
    )
    user_id = await new_user(user_data)

    user_login = UserLogin(user_repo, hasher_password, session_service)
    login_data = UserLoginRequestDTO(user_id, password="Testtest1!")

    session_id = await user_login(login_data)
    session_data = session_service.storage[session_id]

    assert session_id
    assert session_data[0] == user_id
    assert session_data[1] == 30 * 60


@pytest.mark.asyncio
async def test_login_invalid_password(
    user_repo: UserRepoMock,
    hasher_password: HasherPasswordMock,
    session_service: SessionServiceMock,
) -> None:
    new_user = NewUser(user_repo, hasher_password)
    user_data = UserRequestDTO(
        email="test@example.com", username="test_user", password="Testtest1!"
    )
    user_id = await new_user(user_data)

    user_login = UserLogin(user_repo, hasher_password, session_service)
    login_data = UserLoginRequestDTO(user_id, password="Testtest2!")

    with pytest.raises(InvalidPassword):
        await user_login(login_data)


@pytest.mark.asyncio
async def test_login_user_id_not_exists(
    user_repo: UserRepoMock,
    hasher_password: HasherPasswordMock,
    session_service: SessionServiceMock,
) -> None:
    user_login = UserLogin(user_repo, hasher_password, session_service)
    login_data = UserLoginRequestDTO(user_id=1, password="Testtest1!")

    with pytest.raises(UserIdNotExists):
        await user_login(login_data)
