from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

from app.api.endpoints.view_end import get_current_user
from app.core import get_db
from app.api.schemas import schedule_sch
from app.api.crud import schedule_crud

schedule_router = APIRouter()

@schedule_router.post("/createschedule", response_model=schedule_sch.ScheduleCreate, tags=['schedule'])
async def createschedule(schedule: schedule_sch.ScheduleCreate, request: Request, db:Session = Depends(get_db)):
    current_user = get_current_user(request, db)
    if not current_user:
        return RedirectResponse(url="/login", status_code=303)
    new_schedule = schedule_crud.create_schedule(db=db, schedule=schedule, owner_id=current_user.id)
    return schedule