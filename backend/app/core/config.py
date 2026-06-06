from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FinanceFlow"
    debug: bool = True
    mongodb_uri: str = "mongodb://localhost:27017"
    jwt_secret: str = "your-secret-key-change-in-production"

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
