import pytest
from src.application.user.dto.user import UserLoginRequestDTO, UserRequestDTO
from src.application.user.use_cases.get_by_session_id import GetUserBySessionId
from src.application.user.use_cases.login import UserLogin
from src.application.user.use_cases.new_user import NewUser

from tests.mocks import UserRepoMock, SessionServiceMock, HasherPasswordMock


@pytest.mark.asyncio
async def test_get_by_session_id(
    user_repo: UserRepoMock,
    session_service: SessionServiceMock,
    hasher_password: HasherPasswordMock,
) -> None:
    new_user = NewUser(user_repo, hasher_password)
    user_data = UserRequestDTO(
        email="test@example.com", username="test_user", password="Testtest1!"
    )
    user_id = await new_user(user_data)

    user_login = UserLogin(user_repo, hasher_password, session_service)
    login_data = UserLoginRequestDTO(user_id, password="Testtest1!")

    session_id = await user_login(login_data)

    get_by_session_id = GetUserBySessionId(user_repo, session_service)
    user = await get_by_session_id(session_id)

    assert user.user_id == user_id
    assert user.username == "test_user"
    assert user.email == "test@example.com"
