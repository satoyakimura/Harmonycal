from pydantic import BaseModel, Field

class ScheduleBase(BaseModel):
    title: str = Field("", title="Schedule Title")
    description: str | None = Field(None, title="Schedule Description")

class ScheduleCreate(ScheduleBase):
    pass

class Schedule(ScheduleBase):
    id: int = Field(0, title="Schedule ID")
    created_at: datetime = Field(datetime.now(), title="Creation Date")
    owner_id