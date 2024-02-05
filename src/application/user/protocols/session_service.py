from typing import Protocol


class SessionService(Protocol):
    async def create_session(self, user_id: int) -> str:
        raise NotImplementedError

    async def delete_session(self, session_id: str) -> None:
        raise NotImplementedError

    async def get(self, session_id: str) -> int:
        raise NotImplementedError
