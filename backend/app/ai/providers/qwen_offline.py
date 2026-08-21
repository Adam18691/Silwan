from typing import Any

from app.config import settings


class QwenOfflineProvider:
    name = "qwen_offline"

    async def generate(self, prompt: str) -> dict[str, Any]:
        if not settings.qwen_model_path:
            return {
                "provider": self.name,
                "status": "not_configured",
            }

        return {
            "provider": self.name,
            "status": "adapter_ready",
            "model_path": settings.qwen_model_path,
            "message": "Local GGUF adapter is ready for llama.cpp.",
            "prompt_length": len(prompt),
        }
