from pydantic_settings import BaseSettings


class Config(BaseSettings):
    MODE: str

    DB_URL: str
    SECRET: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    REDIS_URL: str
    REDIS_URL: str
    REDIS_PORT: str
    REDIS_DB: str
    REDIS_PASSWORD: str
    REDIS_USERNAME: str

    SECRET_KEY: str
    TTL_REDIS: str

    BOOTSTRAP_SERVERS: str
    CLIENT_ID: str

    SENTRY_DSN: str

    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_NAME}"

    class Config:
        env_file = ".env"


config = Config()
