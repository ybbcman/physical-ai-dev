from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    APP_NAME : str = "Maintanance AI Portfolio API"

    # .env
    SECRET_KEY: str = Field(default="test-key")
    APP_ENV: str = Field(default="dev")
    APP_PORT: int = Field(default=8000)
    PROJECT_NAME: str = Field(default="physical-ai-dev")
    VERSION: str = Field(default="v1")
    DEBUG: bool = Field(default=True)
    
    # Redis
    REDIS_PORT: int = Field(default=6379)
    
    # Ollama
    OLLAMA_HOST: str = Field(default="http://host.docker.internal:11434")
    
settings = Settings()
