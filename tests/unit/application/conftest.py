import pytest

from tests.mocks import HasherPasswordMock, UserRepoMock


@pytest.fixture
def user_repo() -> UserRepoMock:
    return UserRepoMock()


@pytest.fixture
def hasher_password() -> HasherPasswordMock:
    return HasherPasswordMock()
