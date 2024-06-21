from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship

from backend.app.core import Base

class ScheduleModel(Base):
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('userdata.id'), nullable=False)

    user = relationship("UserModel", back_populates="schedule")

    def __repr__(self):
        return f"<Schedule(title={self.title}, start_date={self.start_date}, end_date={self.end_date}, user_id={self.user_id})>"
