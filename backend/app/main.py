from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.ai import router as ai_router
from app.api.auth import router as auth_router
from app.api.auth_login import router as login_router
from app.api.auth_register import router as register_router
from app.api.plans import router as plans_router
from app.config import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "Silwan backend API for authentication, AI services, "
        "and subscription plans."
    ),
    docs_url="/docs",
    redoc_url="/redoc",
)


# CORS for Silwan mobile/web clients.
# Restrict origins before production deployment.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Authentication
app.include_router(auth_router)
app.include_router(register_router)
app.include_router(login_router)

# Artificial Intelligence
app.include_router(ai_router)

# Subscription plans
app.include_router(plans_router)


@app.get("/", tags=["System"])
async def root() -> dict[str, str]:
    return {
        "name": settings.app_name,
        "status": "online",
        "version": settings.app_version,
        "language": settings.language,
        "direction": settings.direction,
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health", tags=["System"])
async def health() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "silwan-api",
    }


@app.get("/ready", tags=["System"])
async def readiness() -> dict[str, str]:
    return {
        "status": "ready",
        "service": "silwan-api",
    }
