from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
#from .models.user import Person

class Base(DeclarativeBase): pass

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
   SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
