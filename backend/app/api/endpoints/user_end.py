from fastapi import Depends, APIRouter, HTTPException, Request, status, Cookie, Response
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime, timedelta


from app.api.crud import user_crud
from app.core import get_db
from app.api.schemas import user_sch

user_router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@user_router.get("/user", response_model=list[user_sch.User], tags=["user"])
async def read_user(offset: int = 0,
                limit: int = 100,
                db: Session = Depends(get_db)):
    users = user_crud.read_user(db=db, offset=offset, limit=limit)
    return users


@user_router.get("/user/{user_id}", response_model=user_sch.User, tags=['user'])
async def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.read_user_by_id(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.post("/signup", response_model=user_sch.User, tags=['user'])
async def signup(user: user_sch.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.read_user_by_name(db=db, user_name=user.username)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username already registered")
    hashed_pass = hash_password(user.password)
    user_data = user.copy(update={"password": hashed_pass})
    new_user = user_crud.create_user(db=db, user=user_data)
    return new_user

@user_router.post("/login", response_model=user_sch.User, tags=['user'])
async def login(user: user_sch.UserCreate, response: Response, db: Session = Depends(get_db)):
    db_user = user_crud.read_user_by_name(db=db, user_name=user.username)
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    response.set_cookie(key="user_id", value=str(db_user.id))
    return db_user

@user_router.get("/set-cookie")
async def set_cookie(response: Response):
    response.set_cookie(key="my_cookie", value="cookie_value", expires=datetime.utcnow() + timedelta(days=7))
    return {"message": "Cookie set successfully"}

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_pass: str) -> bool:
    return pwd_context.verify(plain_password, hashed_pass)