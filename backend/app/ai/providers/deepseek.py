from typing import Any

import httpx

from app.config import settings


class DeepSeekProvider:
    name = "deepseek"

    async def generate(self, prompt: str) -> dict[str, Any]:
        if not settings.deepseek_api_key:
            return {
                "provider": self.name,
                "status": "not_configured",
            }

        headers = {
            "Authorization": f"Bearer {settings.deepseek_api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "deepseek-chat",
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        }

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
                "https://api.deepseek.com/chat/completions",
                headers=headers,
                json=payload,
            )

        response.raise_for_status()
        data = response.json()

        return {
            "provider": self.name,
            "status": "success",
            "response": data,
        }
