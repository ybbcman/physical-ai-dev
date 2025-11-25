from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    name: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    

class UserRead(UserBase):
    id: int
    
    class Config:
        from_attributes = True