from enum import Enum
from typing import Any

from app.config import settings


class ModelType(str, Enum):
    DEEPSEEK = "deepseek"
    QWEN_ONLINE = "qwen_online"
    QWEN_OFFLINE = "qwen_offline"


class ModelManager:
    """
    Central manager for Silwan AI models.

    The manager selects a provider but does not expose
    API keys to the mobile application.
    """

    def __init__(self) -> None:
        self.default_model = ModelType.QWEN_OFFLINE

    def available_models(self) -> list[dict[str, Any]]:
        return [
            {
                "id": ModelType.DEEPSEEK,
                "name": "DeepSeek",
                "mode": "online",
                "enabled": bool(settings.deepseek_api_key),
            },
            {
                "id": ModelType.QWEN_ONLINE,
                "name": "Qwen",
                "mode": "online",
                "enabled": bool(
                    settings.qwen_api_key or settings.dashscope_api_key
                ),
            },
            {
                "id": ModelType.QWEN_OFFLINE,
                "name": "Qwen Offline",
                "mode": "local",
                "enabled": bool(settings.qwen_model_path),
            },
        ]

    def select_model(self, model: ModelType | None = None) -> ModelType:
        return model or self.default_model

    async def generate(
        self,
        prompt: str,
        model: ModelType | None = None,
    ) -> dict[str, Any]:
        selected_model = self.select_model(model)

        return {
            "model": selected_model,
            "status": "adapter_not_connected",
            "message": (
                "Model adapter is ready for integration."
            ),
            "prompt_length": len(prompt),
        }


model_manager = ModelManager()
