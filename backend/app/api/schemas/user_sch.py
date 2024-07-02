from datetime import datetime
from pydantic import BaseModel, Field

from app.api.models import User

class UserBase(BaseModel):
    username: str = Field(..., title="User Name")

class UserCreate(UserBase):
    password: str = Field(..., title="Password")

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True