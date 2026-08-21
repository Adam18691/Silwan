from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.auth_register import router as register_router
from app.api.auth_login import router as login_router
from app.api.ai import router as ai_router


app = FastAPI(
    title="Silwan API",
    version="0.1.0",
    description="Backend API for Silwan",
)


# Authentication
app.include_router(auth_router)
app.include_router(register_router)
app.include_router(login_router)

# Artificial Intelligence
app.include_router(ai_router)


@app.get("/")
async def root():
    return {
        "name": "Silwan",
        "status": "online",
        "version": "0.1.0",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }
