from typing import List, Optional
from sqlmodel import Session, select

from backend.src.db.models.users import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def get(self, user_id: int) -> Optional[User]:
        return self.session.get(User, user_id)
    
    def get_by_email(self, email: str) -> Optional[User]:
        statement = select(User).where(User.email == email)
        return self.session.exec(statement).first()
    
    def list(self) -> List[User]:
        statement = select(User)
        return list(self.session.exec(statement).all())
    
    def create(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        
        return user
    
    def delete(self, user: User) -> None:
        self.session.delete(user)
        self.session.commit()
        
    def update(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        
        return user