import os
from dataclasses import dataclass

DB_URI_ENV = "DB_URI"
REDIS_URI_ENV = "REDIS_URI"
SESSION_EXPIRE_TIME = "SESSION_EXPIRE_TIME"


class ConfigParseError(ValueError):
    pass


@dataclass
class WebConfig:
    session_expire_time: int
    async_db_uri: str
    db_uri: str
    redis_uri: str


def get_str_env(key) -> str:
    val = os.getenv(key)
    if not val:
        raise ConfigParseError(f"{key} is not set")
    return val


def load_web_config() -> WebConfig:
    session_expire_time = int(get_str_env(SESSION_EXPIRE_TIME))
    async_db_uri = f"postgresql+asyncpg://{get_str_env(DB_URI_ENV)}"
    db_uri = f"postgresql://{get_str_env(DB_URI_ENV)}"
    redis_uri = get_str_env(REDIS_URI_ENV)
    return WebConfig(
        session_expire_time=session_expire_time,
        async_db_uri=async_db_uri,
        db_uri=db_uri,
        redis_uri=redis_uri,
    )
