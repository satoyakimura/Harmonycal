from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core import Base

class Record(Base):
    __tablename__ = "record"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    owner_id = Column(Integer, ForeignKey("userdata.id"))
    
    owner = relationship("User", back_populates="records")
