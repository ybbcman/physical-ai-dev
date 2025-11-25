from typing import List
from sqlmodel import Session

from backend.src.common.exceptions import BeException
from backend.src.db.models.user.repository import UserRepository
from backend.src.db.models.user.schema import UserCreate, UserRead, UserUpdate
from backend.src.db.models.users import User


class UserService:
    def __init__(self, session: Session):
        self.repo = UserRepository(session)
        
    def create_user(self, data: UserCreate) -> UserRead:
        # email 중복 체크
        existing = self.repo.get_by_email(data.email)
        if existing:
            raise BeException("Email already exists", status_code=400)

        user = User(email=data.email, name=data.name)
        created = self.repo.create(user)
        return UserRead.model_validate(created)
    
    def get_user(self, user_id: int) -> UserRead:
        user = self.repo.get(user_id)
        if not user:
            raise BeException("User not found", status_code=404)

        return UserRead.model_validate(user)
    
    def list_users(self) -> List[UserRead]:
        users = self.repo.list()
        return [UserRead.model_validate(user) for user in users]
    
    def delete_user(self, user_id: int) -> None:
        user = self.repo.get(user_id)
        if not user:
            raise BeException("User not found", status_code=404)
        
        self.repo.delete(user)
    
    def update_user(self, user_id: int, data: UserUpdate) -> UserRead:
        user = self.repo.get(user_id)
        if not user:
            raise BeException("User not found", status_code=404)
        
        if data.email:
            existing = self.repo.get_by_email(data.email)
            if existing and existing.id != user.id:
                raise BeException("Email already exists", status_code=400)
            user.email = data.email
            
        if data.name:
            user.name = data.name
        
        updated = self.repo.update(user)
        return UserRead.model_validate(updated)
            
                