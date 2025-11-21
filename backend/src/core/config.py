from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name : str = "Maintanance AI Portfolio API"

    # .env
    secret_key: str = Field(default="test-key")
    app_env: str = Field(default="dev")
    app_port: int = Field(default=8000)
    project_name: str = Field(default="physical-ai-dev")
    api_version: str = Field(default="v1")
    debug: bool = Field(default=True)
    app_version: str = "0.1.0"
    
    # Redis
    REDIS_PORT: int = Field(default=6379)
    
    # Ollama
    OLLAMA_HOST: str = Field(default="http://host.docker.internal:11434")
    
settings = Settings()
