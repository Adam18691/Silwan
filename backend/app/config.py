from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Silwan API"
    app_version: str = "0.1.0"
    debug: bool = False

    database_url: str = "postgresql+psycopg://silwan:silwan@localhost:5432/silwan"

    model_provider: str = "local"
    qwen_model_path: str = ""
    deepseek_api_key: str = ""
    dashscope_api_key: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
