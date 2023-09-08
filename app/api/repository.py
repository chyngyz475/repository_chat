from sqlalchemy.orm import Session
from .models.models import User, Chat, Message, UserChat

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_users(self):
        return self.session.query(User).all()

    def get_user_by_id(self, user_id):
        return self.session.query(User).filter(User.id == user_id).first()

    def get_user_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def get_user_chats(self, user_id, status=None):
        query = self.session.query(Chat, UserChat, User).join(UserChat).join(User).filter(User.id == user_id)
        if status is not None:
            query = query.filter(Chat.status == status)
        return query.all()

    def get_messages(self, sender_id=None, receiver_id=None, time_delivered=None):
        query = self.session.query(Message)
        if sender_id:
            query = query.filter(Message.sender_id == sender_id)
        if receiver_id:
            query = query.filter(Message.receiver_id == receiver_id)
        if time_delivered:
            query = query.filter(Message.time_delivered == time_delivered)
        return query.all()

    def get_message_count_in_chat(self, chat_id):
        return self.session.query(Message).filter(Message.receiver_id == chat_id).count()

    def get_chat_count_by_status(self, status):
        return self.session.query(Chat).filter(Chat.status == status).count()
