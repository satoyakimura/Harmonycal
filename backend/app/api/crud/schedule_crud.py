from sqlalchemy.orm import Session

from app.api.models import User, Schedule
from app.api.schemas import schedule_sch

def create_schedule(db:Session, schedule:schedule_sch.ScheduleCreate, owner_id:int):
    db_schedule = Schedule(**schedule.dict(), owner_id=owner_id)
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

# def delete_schedule_by_id(db:Session, id: int):
#     title = db.query(Schedule).filter(Schedule.owner_id == user_id).first.title
#     db.query(Schedule).filter(Schedule.owner_id == user_id).delete()
#     db.commit()
#     return title