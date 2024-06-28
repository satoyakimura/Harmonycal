from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core import Base

class UserModel(Base):
    __tablename__ = "userdata"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    