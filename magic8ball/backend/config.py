"""Configuration for Magic 8 Ball Backend"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings"""
    app_name: str = "Magic 8 Ball"
    debug: bool = False
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    cors_origins: list = ["*"]
    database_url: str = "sqlite:///./magic8ball.db"
    animation_delay_ms: int = 500
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
