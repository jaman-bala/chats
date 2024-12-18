from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_VERSION: str
    MODE: Literal["PROD", "test"]

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DB_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int
    REGEX: str

    LINK_IMAGES: str
    LINK_UPLOAD_FILES: str

    model_config = SettingsConfigDict(env_file=".env")  # extra="ignore"


settings = Settings()
