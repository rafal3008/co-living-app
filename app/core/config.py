
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_VERSION: str
    API_V1_STR: str = "/api/v1s"
    SECRET_KEY: str
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file = ".env",
        env_ignore_empty = True,
        extra = "ignore",
    )

settings = Settings()