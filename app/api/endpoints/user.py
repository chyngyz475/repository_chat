from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.repository import DatabaseRepository, UserCreate
from api.models import User
from main import get_db

router = APIRouter()
repo = DatabaseRepository()


@router.post("/users/", response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return repo.create_user(db, user)


@router.get("/users/", response_model=list[User])
async def get_all_users(db: Session = Depends(get_db)):
    return repo.get_all_users(db)


@router.get("/users/{user_id}", response_model=User)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = repo.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users/by_username/{username}", response_model=User)
async def get_user_by_username(username: str, db: Session = Depends(get_db)):
    user = repo.get_user_by_username(db, username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


