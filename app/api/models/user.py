from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.models import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

    chats = relationship("UserChat", back_populates="user")
