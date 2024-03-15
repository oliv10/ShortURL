from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DBHOST: str = "redis"
    DBPORT: int = 6379
    DBUSER: str | None = None
    DBPASS: str | None = None
    KEYLEN: int = 8
