import pytest

from tests.mocks import HasherPasswordMock, UserRepoMock
from tests.mocks.session_service import SessionServiceMock


@pytest.fixture
def user_repo() -> UserRepoMock:
    return UserRepoMock()


@pytest.fixture
def hasher_password() -> HasherPasswordMock:
    return HasherPasswordMock()


@pytest.fixture
def session_service() -> SessionServiceMock:
    return SessionServiceMock()
