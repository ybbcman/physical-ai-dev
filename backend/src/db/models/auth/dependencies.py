from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session
from jose import JWTError, jwt

from backend.src.core.config import settings
from backend.src.db.models.users import User
from backend.src.db.session import get_session
from backend.src.common.exceptions import BeException
from backend.src.db.models.user.repository import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Session = Depends(get_session)
) -> User:
    credentials_exception = BeException(
        "Could not validate credential", status_code=401
    )
    
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
    except (JWTError, ValueError):
        raise credentials_exception
    
    repo = UserRepository(session)
    user = repo.get(user_id)
    if user is None:
        raise credentials_exception
    
    return user
    