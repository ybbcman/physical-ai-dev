from fastapi import APIRouter, Depends
from sqlmodel import Session

from backend.src.db.models.auth.service import AuthService
from backend.src.db.session import get_session
from backend.src.common.response import ApiResponse
from backend.src.db.models.auth.schemas import LoginRequest, RegisterRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["auth"])

def get_auth_service(session: Session = Depends(get_session)) -> AuthService:
    return AuthService(session)

@router.post("/register", response_model=ApiResponse[TokenResponse], summary="Register a new user")
def register(request: RegisterRequest, service: AuthService = Depends(get_auth_service)):
    token = service.register(request)
    return ApiResponse(data=token)

@router.post("/login", response_model=ApiResponse[TokenResponse], summary="Login a user")
def login(request: LoginRequest, service: AuthService = Depends(get_auth_service)):
    token = service.login(request)
    return ApiResponse(data=token)