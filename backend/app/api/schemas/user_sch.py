from datetime import datetime
from pydantic import BaseModel, Field

class UserBase(BaseModel):
    name: str = Field(..., title="User Name")

class UserCreate(UserBase):
    password: str = Field(..., title="Password")

class User(UserBase):
    id: int = Field(0, title="User ID")
    created_at: datetime = Field(datetime.now(), title="Creation Date")

    class Config:
        orm_mode = True