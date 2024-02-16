import pytest

from src.application.user.dto.user import UserLoginRequestDTO, UserRequestDTO
from src.application.user.use_cases.delete_user import DeleteUser
from src.application.user.use_cases.login import UserLogin
from src.application.user.use_cases.new_user import NewUser
from tests.mocks import HasherPasswordMock, SessionServiceMock, UserRepoMock


@pytest.mark.asyncio
async def test_delete_user(
    user_repo: UserRepoMock,
    hasher_password: HasherPasswordMock,
    session_service: SessionServiceMock,
):
    new_user = NewUser(user_repo, hasher_password)  # type: ignore
    user_data = UserRequestDTO(
        email="test@example.com", username="test_user", password="Testtest1!"
    )
    user_id = await new_user(user_data)

    user_login = UserLogin(user_repo, hasher_password, session_service)  # type: ignore
    login_data = UserLoginRequestDTO(user_id, password="Testtest1!")
    session_id = await user_login(login_data)

    user_delete = DeleteUser(user_repo, session_service)  # type: ignore
    await user_delete(session_id)

    assert not user_repo.users
