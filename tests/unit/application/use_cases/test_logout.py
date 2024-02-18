import pytest

from src.application.user.dto import UserLoginRequestDTO, UserRequestDTO
from src.application.user.use_cases.login import UserLogin
from src.application.user.use_cases.new_user import NewUser
from src.application.user.use_cases.logout import UserLogout
from tests.mocks import HasherPasswordMock, SessionServiceMock, UserRepoMock


@pytest.mark.asyncio
async def test_logout(
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

    user_logout = UserLogout(user_repo, session_service)
    await user_logout(session_id)

    assert session_id not in session_service.storage
