from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import WebConfig
from src.stub import get_config_stub, get_session_stub

router = APIRouter()


@router.get("/")
async def test(config: WebConfig = Depends(get_config_stub)):
    print(config.db_uri)
    return {"hello": "world"}


@router.get("/test")
async def test_2(session: AsyncSession = Depends(get_session_stub)):
    res = await session.execute(text("SELECT * FROM users"))
    data = res.fetchall()
    print(data)


@router.get("/test2")
async def test_3(session: AsyncSession = Depends(get_session_stub)):
    await session.execute(
        text("INSERT INTO users (email, username, password) VALUES ('bb', 'bb', 'bb')")
    )
    await session.commit()
