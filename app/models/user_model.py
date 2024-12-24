from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    user_surname = Column(String)
    user_last_name = Column(String)
    password = Column(String)
    login = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
