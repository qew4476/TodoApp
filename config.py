from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST:str
    DB_PORT:int
    DB_USER:str
    DB_PASSWORD:str
    DB_NAME:str


settings = Settings()

@lru_cache
def get_settings():
    return Settings()