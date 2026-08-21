from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.ai.model_manager import ModelManager, ModelType


router = APIRouter(
    prefix="/api/v1/ai",
    tags=["AI"],
)

manager = ModelManager()


class GenerateRequest(BaseModel):
    prompt: str = Field(
        min_length=1,
        max_length=12000,
    )

    model: ModelType | None = None


@router.get("/models")
async def get_models():
    return {
        "app": "Silwan",
        "language": "ar",
        "direction": "rtl",
        "models": manager.available_models(),
    }


@router.post("/generate")
async def generate(request: GenerateRequest):
    result = await manager.generate(
        prompt=request.prompt,
        model=request.model,
    )

    return result
