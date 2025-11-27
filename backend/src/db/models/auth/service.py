from datetime import timedelta
from sqlmodel import Session

from backend.src.common.security import create_access_token, get_password_hash, verify_password
from backend.src.core.config import settings
from backend.src.db.models.auth.schemas import LoginRequest, RegisterRequest, TokenResponse
from backend.src.db.models.user.repository import UserRepository
from backend.src.common.exceptions import BeException
from backend.src.db.models.users import User


class AuthService:
    def __init__(self, session: Session):
        self.session = session
        self.user_repo = UserRepository(session)
        
    def register(self, request: RegisterRequest) -> TokenResponse:
        # email 중복 체크
        existing = self.user_repo.get_by_email(request.email)
        if existing:
            raise BeException("Email already exists", status_code=400)
        
        hashed_password = get_password_hash(request.password)
        user = User(
            email=request.email,
            name=request.name,
            hashed_password=hashed_password,
        )
        self.user_repo.create(user)
        
        # 회원가입후 token 발급
        access_token_expires = timedelta(
            minutes=settings.jwt_access_token_expire_minutes
        )
        access_token = create_access_token(
            data={"sub": str(user.id)},
            expires_delta=access_token_expires
        )
        return TokenResponse(access_token=access_token)
    
    def login(self, request: LoginRequest) -> TokenResponse:
        user = self.user_repo.get_by_email(request.email)
        if not user:
            raise BeException("Invalid email or password", status_code=401)
        
        if not verify_password(request.password, user.hashed_password):
            raise BeException("Invalid email or password", status_code=401)
        
        access_token_expires = timedelta(
            minutes=settings.jwt_access_token_expire_minutes
        )
        access_token = create_access_token(
            data={"sub": str(user.id)},
            expires_delta=access_token_expires
        )
        return TokenResponse(access_token=access_token)
    
    def login_with_email_password(self, email: str, password: str) -> TokenResponse:
        return self.login(LoginRequest(email=email, password=password))