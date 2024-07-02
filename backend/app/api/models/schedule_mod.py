from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core import Base

class Schedule(Base):
    __tablename__ = "schedule"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    start_date = Column(DateTime, default=datetime.now(), nullable=False)
    end_date = Column(DateTime, default=datetime.now(), nullable=False)
    owner_id = Column(Integer, ForeignKey('userdata.id'), nullable=False)

    owner = relationship("User", back_populates="schedules")
