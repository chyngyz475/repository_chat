from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.models import Base

class Chat(Base):
    __tablename__ = "chats"
    
    id = Column(Integer, primary_key=True, index=True)

    users = relationship("UserChat", back_populates="chat")
