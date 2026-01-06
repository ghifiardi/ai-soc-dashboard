"""
Application configuration settings
"""
import os
from typing import List
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """Application settings"""

    # Google Cloud Platform
    gcp_project_id: str = os.getenv("GCP_PROJECT_ID", "chronicle-dev-2be9")
    bigquery_dataset: str = os.getenv("BIGQUERY_DATASET", "gatra_database")
    google_credentials_path: str = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "")

    # API Configuration
    api_host: str = os.getenv("API_HOST", "0.0.0.0")
    api_port: int = int(os.getenv("API_PORT", "8000"))
    api_title: str = "SOC Executive Dashboard API"
    api_version: str = "1.0.0"

    # CORS
    cors_origins: List[str] = [
        "http://localhost:3001",
        "http://localhost:3000",
        "http://127.0.0.1:3001",
        "http://127.0.0.1:3000"
    ]

    # Environment
    environment: str = os.getenv("ENVIRONMENT", "development")
    debug: bool = environment == "development"

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
