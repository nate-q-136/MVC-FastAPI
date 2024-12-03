# app/config/settings.py
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI SQLite Project"
    DATABASE_URL: str = "sqlite:///./test.db"  # Đường dẫn đến file SQLite
    API_PREFIX: str = "/api/v1"
    BACKEND_CORS_ORIGINS: list = ["http://localhost:3000", "http://example.com"]

    class Config:
        env_file = ".env"

settings = Settings()
