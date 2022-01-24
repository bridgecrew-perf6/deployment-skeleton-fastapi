from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBAG: bool = False

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: int = 5432


settings = Settings()
