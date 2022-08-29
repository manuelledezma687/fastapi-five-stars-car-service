from sqlalchemy import Column, Integer, String
from connections import Base

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer,primary_key=True,index=True)
    email = Column(String(30))
    username = Column(String(20))
    first_name = Column(String(20))
    last_name = Column(String(20))
    age = Column(Integer)
    country = Column(String(20))
    language = Column(String(20))
    #user_since = Column(String(50))
    status = Column(Integer)
