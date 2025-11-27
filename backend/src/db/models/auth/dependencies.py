import logging
from typing import Annotated
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlmodel import Session
from jose import JWTError, jwt

from backend.src.core.config import settings
from backend.src.db.models.users import User
from backend.src.db.session import get_session
from backend.src.common.exceptions import BeException
from backend.src.db.models.user.repository import UserRepository


logger = logging.getLogger(__name__)

bearer_scheme = HTTPBearer(auto_error=False)

def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(bearer_scheme)],
    session: Session = Depends(get_session)
) -> User:
    credentials_exception = BeException(
        "Could not validate credential", status_code=401
    )
    
    token = credentials.credentials if credentials else None
    
    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm]
        )
        sub: str = payload.get("sub")
        if sub is None:
            raise credentials_exception
        
        user_id = int(sub)
    except JWTError as exc:
        logger.exception("JWT decode failed: %s", exc)
        raise credentials_exception
    
    repo = UserRepository(session)
    user = repo.get(user_id)
    if user is None:
        raise credentials_exception
    
    return user
    