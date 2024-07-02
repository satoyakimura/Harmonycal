from datetime import datetime
from pydantic import BaseModel, Field

class ScheduleBase(BaseModel):
    title: str = Field(..., title="Schedule Name")
    description: str = Field(..., title="Description")
    start_date: datetime = Field(..., title="Start Date/Time")
    end_date: datetime = Field(..., title="End Date/Time")

class ScheduleCreate(ScheduleBase):
    pass

class Schedule(ScheduleBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True