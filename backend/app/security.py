from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.config import settings


# ============================================================
# Password Security
# ============================================================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


# ============================================================
# JWT Configuration
# ============================================================

SECRET_KEY = settings.jwt_secret_key
ALGORITHM = getattr(settings, "jwt_algorithm", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = getattr(
    settings,
    "access_token_expire_minutes",
    60,
)


# ============================================================
# Password Hashing
# ============================================================

def hash_password(password: str) -> str:
    """
    Hash a user's password using bcrypt.
    """

    if not password:
        raise ValueError("Password cannot be empty.")

    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    password_hash: str,
) -> bool:
    """
    Verify a plain-text password against its stored hash.
    """

    if not plain_password or not password_hash:
        return False

    try:
        return pwd_context.verify(
            plain_password,
            password_hash,
        )
    except (ValueError, TypeError):
        return False


# ============================================================
# JWT Creation
# ============================================================

def create_access_token(user_id: int) -> str:
    """
    Create an access token for a user.
    """

    if user_id <= 0:
        raise ValueError("Invalid user ID.")

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES,
    )

    payload = {
        "sub": str(user_id),
        "exp": expire,
        "iat": datetime.now(timezone.utc),
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


# ============================================================
# JWT Decoding
# ============================================================

def decode_access_token(
    token: str,
) -> int | None:
    """
    Decode an access token and return the user ID.

    Returns None when the token is invalid or expired.
    """

    if not token:
        return None

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        user_id = payload.get("sub")

        if user_id is None:
            return None

        return int(user_id)

    except (
        JWTError,
        ValueError,
        TypeError,
    ):
        return None
