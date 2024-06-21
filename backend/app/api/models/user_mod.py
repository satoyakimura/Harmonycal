from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.app.core import Base

class UserModel(Base):
    __tablename__ = "userdata"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    schedules = relationship("ScheduleModel", back_populates="user")

    def __repr__(self):
        return f"<UserData(username={self.username}, email={self.email}, created_at={self.created_at})>"
