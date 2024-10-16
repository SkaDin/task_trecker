from pydantic_settings import BaseSettings


class Config(BaseSettings):
    MODE: str

    DB_URL: str
    REDIS_URL: str
    SECRET: str
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    # REDIS_URL: str
    # REDIS_PORT: str
    # REDIS_DB: str
    # REDIS_PASSWORD: str
    # REDIS_USERNAME: str

    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_NAME}"

    class Config:
        env_file = ".env"


config = Config()
