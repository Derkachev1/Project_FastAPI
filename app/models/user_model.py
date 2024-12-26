from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.mutable import MutableString
from sqlalchemy.orm import validates
from app.database import Base
import hashlib
import re

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    user_surname = Column(String)
    user_last_name = Column(String, nullable=True)
    password_hash = Column(MutableString.as_mutable(String))
    email = Column(String, unique=True, index=True)

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('Email cannot be empty')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Invalid email format')
        return email

    def __repr__(self):
        return f"<User(id={self.id}, name={self.user_name} {self.user_surname} {self.user_last_name}, password={self.password_hash}, email={self.email})>"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password_hash = None

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, value):
        self.password_hash = hashlib.md5(value.encode()).hexdigest()

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        if 'password' in kwargs:
            instance.password = kwargs['password']
        return instance

    def verify_password(self, password):
        return self.password_hash == hashlib.md5(password.encode()).hexdigest()