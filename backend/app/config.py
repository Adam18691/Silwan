class Settings(jwt_secret_key: str = "CHANGE_THIS_IN_ENV"):
    app_name: str = "Silwan API"
    app_version: str = "0.1.0"
    debug: bool = False

    database_url: str = "postgresql+psycopg://silwan:silwan@localhost:5432/silwan"

    jwt_secret_key: str = "CHANGE_THIS_IN_ENV"

    model_provider: str = "local"
    qwen_model_path: str = ""
    deepseek_api_key: str = ""
    dashscope_api_key: str = ""
