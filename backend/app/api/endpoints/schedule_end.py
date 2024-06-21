from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from backend.app import crud
from backend.app import schemas
from backend.app.core.database import get_db

schedule_router = APIRouter()

@schedule_router.post("/schedule/{user_id}", response_model=schemas.Schedule, tags=['schedule'])
def create_schedule(schedule: schemas.ScheduleCreate,
                    user_id: int,
                    db: Session = Depends(get_db)):
    new_schedule = crud.create_user_schedule(db=db, schedule=schedule, user_id=user_id)
    return new_schedule

@schedule_router.get("/schedules/{user_id}", response_model=list[schemas.Schedule])
def read_schedules(user_id: int,
                    offset: int = 0,
                    limit: int = 100,
                    db: Session = Depends(get_db)):
    schedules = crud.read_user_schedule(
        db=db, user_id=user_id, offset=offset, limit=limit)
    return schedules

@schedule_router.put("/schedule/update", response_model=schemas.Schedule, tags=['schedule'])
def update_schedule(schedule: schemas.Schedule, db: Session = Depends(get_db)):
    db_schedule = crud.read_schedule_by_id(db=db, schedule_id=schedule.id)
    if not db_schedule:
        raise HTTPException(status_code=400, detail="Schedule does not exist")
    new_schedule = crud.update_schedule(db=db, schedule=schedule)
    return new_schedule

@schedule_router.delete("/schedule/{schedule_id}",response_model=schemas.Schedule, tags=['schedule'])
def delete_schedule(schedule_id: int, db: Session = Depends(get_db)):
    db_schedule = crud.read_schedule_by_id(db=db, schedule_id=schedule_id)
    if not db_schedule:
        raise HTTPException(status_code=400, detail="Schedule does not exist")

    delete_schedule = crud.delete_schedule_by_id(db=db, schedule_id=schedule_id)
    return db_schedule