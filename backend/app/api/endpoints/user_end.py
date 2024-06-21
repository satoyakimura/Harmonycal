from fastapi import Depends, APIRouter, HTTPException, Request, status
from sqlalchemy.orm import Session

from backend.db import crud
from backend.db import schemas
from backend.db.database import get_db

user_router = APIRouter()

@user_router.get("/user", response_model=list[schemas.User], tags=["user"])
async def read_user(offset: int = 0,
                limit: int = 100,
                db: Session = Depends(get_db)):
    users = crud.read_user(db=db, offset=offset, limit=limit)
    return users


@user_router.get("/user/{user_id}", response_model=schemas.User, tags=['user'])
async def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = crud.read_user_by_id(db=db, user_id=user_id)
    return user

@user_router.post("/signup", response_model=schemas.User, tags=['user'])
async def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.read_user_by_name(db=db, user_name=user.name)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username already registered")

    new_user = crud.create_user(db=db, user=user)
    return new_user

@user_router.post("/login", response_model=schemas.User, tags=['user'])
async def login(user: schemas.UserCreate, db: Session = Depends(get_db)):

    db_user = crud.read_user_by_name(db=db, user_name=user.name)
    if user.password != db_user.password:
        raise HTTPException(
            status_code=401, detail="Password is incorrect")
    return db_user