from sqlalchemy.orm import Session

from app.api.models import models
from app.api.schemas import user_sch

def create_user(db:Session, user: user_sch.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def read_user(db: Session, offset: int = 0, limit: int = 100):
    users = db.query(models.User).offset(offset).limit(limit).all()
    return users

def read_user_by_id(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user

def read_user_by_name(db: Session, user_name: str):
    user = db.query(models.User).filter(models.User.username == user_name).first()
    return user
