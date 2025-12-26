from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_env: str = "dev"
    app_name: str = "AI Agent Service"

    mongodb_url:str
    redis_url: str

    jwt_secret:str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    model_config=SettingsConfigDict(env_file=".env", extra="ignore")