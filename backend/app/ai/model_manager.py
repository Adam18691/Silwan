from enum import Enum
from typing import Any

from app.config import settings
from app.ai.providers.deepseek import DeepSeekProvider
from app.ai.providers.qwen_online import QwenOnlineProvider
from app.ai.providers.qwen_offline import QwenOfflineProvider


class ModelType(str, Enum):
    DEEPSEEK = "deepseek"
    QWEN_ONLINE = "qwen_online"
    QWEN_OFFLINE = "qwen_offline"


class ModelManager:
    """
    Central manager for Silwan AI models.

    API keys remain on the backend and are never exposed
    to the mobile application.
    """

    def __init__(self) -> None:
        self.providers = {
            ModelType.DEEPSEEK: DeepSeekProvider(),
            ModelType.QWEN_ONLINE: QwenOnlineProvider(),
            ModelType.QWEN_OFFLINE: QwenOfflineProvider(),
        }

        self.default_model = ModelType.QWEN_OFFLINE

    def available_models(self) -> list[dict[str, Any]]:
        return [
            {
                "id": ModelType.DEEPSEEK.value,
                "name": "DeepSeek",
                "mode": "online",
                "enabled": bool(settings.deepseek_api_key),
            },
            {
                "id": ModelType.QWEN_ONLINE.value,
                "name": "Qwen Online",
                "mode": "online",
                "enabled": bool(
                    settings.qwen_api_key
                    or settings.dashscope_api_key
                ),
            },
            {
                "id": ModelType.QWEN_OFFLINE.value,
                "name": "Qwen Offline",
                "mode": "local",
                "enabled": bool(settings.qwen_model_path),
            },
        ]

    def select_model(
        self,
        model: ModelType | None = None,
    ) -> ModelType:
        return model or self.default_model

    async def generate(
        self,
        prompt: str,
        model: ModelType | None = None,
    ) -> dict[str, Any]:

        selected_model = self.select_model(model)

        provider = self.providers.get(selected_model)

        if provider is None:
            return {
                "status": "error",
                "message": "Unknown model provider",
            }

        result = await provider.generate(prompt)

        return {
            "model": selected_model.value,
            **result,
        }


model_manager = ModelManager()
