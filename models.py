from sqlalchemy import Column, Integer, String
from database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column (String, unique=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
'''id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))'''
