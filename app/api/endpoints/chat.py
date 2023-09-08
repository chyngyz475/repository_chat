from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.repository import DatabaseRepository, ChatCreate
from api.models import Chat
from main import get_db

router = APIRouter()
repo = DatabaseRepository()


@router.post("/chats/", response_model=Chat)
async def create_chat(chat: ChatCreate, db: Session = Depends(get_db)):
    return repo.create_chat(db, chat)


@router.get("/chats/{user_id}", response_model=list[Chat])
async def get_user_chats(user_id: int, db: Session = Depends(get_db)):
    return repo.get_user_chats(db, user_id)


@router.get("/chats/{chat_id}", response_model=Chat)
async def get_chat_by_id(chat_id: int, db: Session = Depends(get_db)):
    chat = repo.get_chat_by_id(db, chat_id)
    if chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat


