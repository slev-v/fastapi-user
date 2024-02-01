from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.main.config import WebConfig


def create_session_maker(config: WebConfig):
    db_uri = config.async_db_uri

    engine = create_async_engine(db_uri, echo=True, pool_size=15, max_overflow=15)
    return async_sessionmaker(engine, autoflush=False, expire_on_commit=False)


async def new_session(session_maker):
    async with session_maker() as session:
        yield session
