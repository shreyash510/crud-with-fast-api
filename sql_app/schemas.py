from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    lastname: str

class UserUpdate(BaseModel):
    email: Optional[str]
    lastname: Optional[str]


class User(UserBase):
    id: int
    # firstname: str
    lastname: str
    is_active: Optional[bool] = True  # Optional field with default value

    class Config:
        from_attributes = True  # This enables compatibility with SQLAlchemy models
