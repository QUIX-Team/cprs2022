from ..db_setup import Base
from sqlalchemy import Column, Integer, Boolean, Text, String


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(25))
    last_name = Column(String(25))
    email = Column(String(80), unique=True)
    username = Column(String(25), unique=True)
    password = Column(Text, nullable=True)
    faculty = Column(String(25))
    city = Column(String(25))
    graduated = Column(Boolean, default=True)


class TokenBlackList(Base):
    __tablename__ = 'token_blacklist'
    id = Column(Integer, primary_key=True)
    jti = Column(String(30))
