from sqlalchemy.orm import Session
from sqlalchemy import and_
from datetime import datetime, timedelta
import pytz

from app.api.models import User, Schedule, Record
from app.api.schemas import schedule_sch

def create_schedule(db:Session, schedule:schedule_sch.ScheduleCreate, user_id:int):
    db_schedule = Schedule(**schedule.dict(), owner_id=user_id)
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

def read_schedules_by_user_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    schedules = user.schedules
    return schedules

def delete_schedule_by_id(db:Session, user_id: int, schedule_id: int):
    schedule_to_delete = db.query(Schedule).filter(
        Schedule.owner_id == user_id, Schedule.id == schedule_id
    ).first()
    if schedule_to_delete is None:
        raise ScheduleNotFoundError("Schedule not found")
    db.query(Schedule).filter(Schedule.owner_id == user_id, Schedule.id == schedule_id).delete()
    db.commit()
    return schedule_to_delete

def read_records_by_week(db: Session, user_id: int):
    tokyo_tz = pytz.timezone("Asia/Tokyo")
    now = datetime.now(tokyo_tz)
    one_week_ago = now - timedelta(weeks=1)

    records = db.query(Record).filter(
        and_(
            Record.owner_id == user_id,
            Record.start_date >= one_week_ago,  # 一週間前から
            Record.start_date <= now           # 現在まで
        )
    ).all()
    return records