import logging
from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session

from backend.src.common.authz import require_self
from backend.src.common.response import ApiResponse
from backend.src.db.models.auth.dependencies import get_current_user
from backend.src.db.models.user.schema import UserCreate, UserRead, UserUpdate
from backend.src.db.models.user.service import UserService
from backend.src.db.models.users import User
from backend.src.db.session import get_session


router = APIRouter(prefix="/users", tags=["users"])

def get_user_service(session: Session = Depends(get_session)) -> UserService:
    return UserService(session)

@router.post("", response_model=ApiResponse[UserRead], summary="Create user")
def create_user(
    data: UserCreate,
    service: UserService = Depends(get_user_service)
):
    user = service.create_user(data)
    return ApiResponse(data=user)

@router.get("/me", response_model=ApiResponse[UserRead], summary="Get my profile")
def show_me(current_user: User = Depends(get_current_user)):
    return ApiResponse(data=UserRead.model_validate(current_user))

@router.get("/{user_id}", response_model=ApiResponse[UserRead], summary="Get user by id")
def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service),
    current_user: User = Depends(get_current_user)
):
    require_self(user_id, current_user)
    user = service.get_user(user_id)
    return ApiResponse(data=user)

@router.get("", response_model=ApiResponse[list[UserRead]], summary="List users")
def list_users(
    service: UserService = Depends(get_user_service),
    current_user: User = Depends(get_current_user)
):
    users = service.list_users()
    return ApiResponse(data=users)

@router.patch("/{user_id}", response_model=ApiResponse[UserRead], summary="Update user")
def update_user(
    user_id: int,
    data: UserUpdate,
    service: UserService = Depends(get_user_service),
    current_user: User = Depends(get_current_user)
):
    require_self(user_id, current_user)
    user = service.update_user(user_id, data)
    return ApiResponse(data=user)

@router.delete("/{user_id}", response_model=ApiResponse[dict], summary="Delete user")
def delete_user(
    user_id: int,
    service: UserService = Depends(get_user_service),
    current_user: User = Depends(get_current_user)
):
    require_self(user_id, current_user)
    service.delete_user(user_id)
    return ApiResponse(data={"id": user_id})

