from sqlalchemy import Column, Integer, String
from database import Base

class Person_model(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    user_surname = Column(String)
    user_last_name = Column(String)
    password = Column(String)
    login = Column(String, unique=True, index=True)
    Email = Column(String, unique=True, index=True)

