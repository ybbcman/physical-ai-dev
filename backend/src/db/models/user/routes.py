from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session

from backend.src.common.response import ApiResponse
from backend.src.db.models.user.schema import UserCreate, UserRead, UserUpdate
from backend.src.db.models.user.service import UserService
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

@router.get("", response_model=ApiResponse[UserRead], summary="Get user by id")
def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    user = service.get_user(user_id)
    return ApiResponse(data=user)

@router.get("", response_model=List[ApiResponse[UserRead]], summary="List users")
def list_users(
    service: UserService = Depends(get_user_service)
):
    users = service.list_users()
    return ApiResponse(data=users)

@router.patch("/{user_id}", response_model=ApiResponse[UserRead], summary="Update user")
def update_user(
    user_id: int,
    data: UserUpdate,
    service: UserService = Depends(get_user_service)
):
    user = service.update_user(user_id, data)
    return ApiResponse(data=user)

def delete_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    service.delete_user(user_id)
    return ApiResponse(data={"id": user_id})
