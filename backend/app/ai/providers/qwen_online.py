from typing import Any

import httpx

from app.config import settings


class QwenOnlineProvider:
    name = "qwen_online"

    async def generate(self, prompt: str) -> dict[str, Any]:
        api_key = settings.qwen_api_key or settings.dashscope_api_key

        if not api_key:
            return {
                "provider": self.name,
                "status": "not_configured",
            }

        return {
            "provider": self.name,
            "status": "adapter_ready",
            "message": "Qwen online adapter is ready for API integration.",
            "prompt_length": len(prompt),
        }
