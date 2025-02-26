from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.api.models import Schedule
from app.core import Base

class User(Base):
    __tablename__ = "userdata"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    schedules = relationship("Schedule", back_populates="owner")
    records = relationship("Record", back_populates="owner")