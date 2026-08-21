from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration for the Silwan backend."""

    app_name: str = "Silwan API"
    app_version: str = "0.2.0"
    debug: bool = False
    api_prefix: str = "/api/v1"
    language: str = "ar"
    direction: str = "rtl"

    database_url: str = (
        "postgresql+psycopg://silwan:silwan@localhost:5432/silwan"
    )
    jwt_secret_key: str = "CHANGE_THIS_IN_ENV"

    model_provider: str = "qwen_offline"
    qwen_api_key: str = ""
    qwen_model_path: str = ""
    deepseek_api_key: str = ""
    dashscope_api_key: str = ""

    instapay_handle: str = "waeldeban@instapay"
    payment_currency: str = "EGP"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
