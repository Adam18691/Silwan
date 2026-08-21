from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.auth import decode_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


security = HTTPBearer(
    auto_error=False,
)


@router.get("/status")
async def auth_status():
    return {
        "service": "authentication",
        "status": "ready",
    }


async def get_current_user_id(
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
) -> int:
    """
    Extract and validate the authenticated user ID from JWT.
    """

    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Authentication required.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if credentials.scheme.lower() != "bearer":
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication scheme.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id = decode_access_token(
        credentials.credentials,
    )

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired access token.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user_id
