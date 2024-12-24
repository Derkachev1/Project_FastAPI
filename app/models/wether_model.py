from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    temperature = Column(Float)
    description = Column(String)
    humidity = Column(Integer)
    pressure = Column(Integer)
    wind_speed = Column(Float)
