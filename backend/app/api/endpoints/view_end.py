from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

from app.core import get_db
from app.api.schemas import user_sch
from app.api.crud import user_crud
from app.api.crud import schedule_crud

view_router = APIRouter()


def get_current_user(request: Request, db:Session) -> user_sch.User:
    user_id = request.cookies.get("user_id")
    if not user_id:
        return None
    user = user_crud.read_user_by_id(db=db, user_id=user_id)
    return user



# @view_router.get("/", tags=["root"])
# async def home(request: Request, db: Session = Depends(get_db)):
#     current_user = get_current_user(request, db)
#     if not current_user:
#         return RedirectResponse(url="/login", status_code=303)
#     schedules = schedule_crud.read_schedules_by_user_id(db=db, user_id=current_user.id)

#     return schedules