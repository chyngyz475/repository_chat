from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.repository import DatabaseRepository, MessageCreate, MessageFilter
from api.models import Message
from main import get_db

router = APIRouter()
repo = DatabaseRepository()


@router.post("/messages/", response_model=Message)
async def send_message(message: MessageCreate, db: Session = Depends(get_db)):
    return repo.send_message(db, message)


@router.get("/messages/", response_model=list[Message])
async def get_messages(filters: MessageFilter, db: Session = Depends(get_db)):
    return repo.get_messages(db, filters)


