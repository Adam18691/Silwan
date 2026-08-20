from fastapi import FastAPI

from app.api.auth import router as auth_router


app = FastAPI(
    title="Silwan API",
    version="0.1.0",
    description="Backend API for Silwan",
)


app.include_router(auth_router)


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
