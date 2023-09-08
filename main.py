from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.api.models import Base
from app.api.repository import UserRepository

app = FastAPI()

DATABASE_URL = "postgresql://Chat:Chat@localhost:5432/Chat"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


user_repository = UserRepository(SessionLocal())

@app.get("/users/")
def get_all_users():
    users = user_repository.get_all_users()
    return [{"id": user.id, "username": user.username, "photo_url": user.photo_url} for user in users]

@app.get("/users/{user_id}/")
def get_user_by_id(user_id: int):
    user = user_repository.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "username": user.username, "photo_url": user.photo_url}

@app.get("/users/{username}/")
def get_user_by_username(username: str):
    user = user_repository.get_user_by_username(username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "username": user.username, "photo_url": user.photo_url}

@app.get("/user_chats/")
def get_user_chats(user_id: int, status: int = None):
    chats = user_repository.get_user_chats(user_id, status)
    return [
        {"chat_id": chat.Chat.id, "chat_name": chat.Chat.name, "status": chat.Chat.status,
         "update_at": chat.Chat.update_at, "user_id": chat.User.id, "username": chat.User.username}
        for chat in chats
    ]

@app.get("/messages/")
def get_messages(sender_id: int = None, receiver_id: int = None, time_delivered: str = None):
    messages = user_repository.get_messages(sender_id, receiver_id, time_delivered)
    return [
        {"message_id": message.id, "sender_id": message.sender_id, "receiver_id": message.receiver_id,
         "text": message.text, "time_delivered": message.time_delivered, "time_seen": message.time_seen,
         "is_delivered": message.is_delivered}
        for message in messages
    ]

@app.get("/message_count/{chat_id}/")
def get_message_count_in_chat(chat_id: int):
    count = user_repository.get_message_count_in_chat(chat_id)
    return {"chat_id": chat_id, "message_count": count}

@app.get("/chat_count/{status}/")
def get_chat_count_by_status(status: int):
    count = user_repository.get_chat_count_by_status(status)
    return {"status": status, "chat_count": count}
