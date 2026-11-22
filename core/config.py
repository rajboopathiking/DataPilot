from pydantic_settings import BaseSettings,SettingsConfigDict
import os

from dotenv import load_dotenv
from functools import lru_cache

load_dotenv(".env")


class Config(BaseSettings):
    app_name : str = os.getenv("APP_NAME")
    app_env : str = os.getenv("APP_ENV","production")
    database_url : str = os.getenv("Database_URL")
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False
    )
    debug : bool = False
    jwt_secret_key : str = os.getenv("JWT_SECRET_KEY")
    jwt_algorithm : str = "HS256"
    access_token_expiry_minutes : int = 30
    jwt_issuer : str = "data-pilot"
    jwt_author : str ="data-pilot"

    log_level : str = "INFO"

@lru_cache
def get_config():
    return Config()

