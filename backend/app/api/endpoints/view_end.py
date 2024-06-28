from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

from app.core import get_db
from app.api.schemas import user_sch

view_router = APIRouter()


def get_current_user(request: Request) -> user_sch.User:
    user_id = request.cookies.get("user_id")
    if not user_id:
        return None
    user = user_crud.read_user_by_id(db=db, user_id=user_id)
    return user

@view_router.get("/", tags=["root"])
async def home(request: Request, db: Session = Depends(get_db)):
    current_user = get_current_user(request)
    if current_user is None:
        return RedirectResponse(url="/login")
    return none