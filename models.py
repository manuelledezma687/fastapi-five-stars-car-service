from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from connections import Base

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer,primary_key=True,index=True)
    email = Column(String(30))
    telephone = Column(Integer)
    username = Column(String(20))
    first_name = Column(String(20))
    last_name = Column(String(20))
    age = Column(Integer)
    country = Column(String(20))
    language = Column(String(20))
    user_since = Column(String(50))
    status = Column(Integer)
    
class Bookings(Base):
    __tablename__ = 'bookings'
    booking_id = Column(Integer,primary_key=True,index=True)
    type_of_travel = Column(String(20))
    pick_up_location = Column(String(150))
    drop_off_location = Column(String(150))
    flight_id = Column(String(20))
    passengers = Column(Integer)
    full_name = Column(String(30))
    email = Column(String(20))
    observations = Column(String(200))
    payment_method = Column(String(20))
    date = Column(String(20))
    hour = Column(String(20))
    created_at = Column(String(50))
    
class Ratings(Base):
    __tablename__ = 'ratings'
    rating_id = Column(Integer,primary_key=True,index=True)
    booking_id = Column(Integer, ForeignKey("bookings.booking_id"))
    stars = Column(Integer)
    first_name = Column(String(20))
    last_name = Column(String(20))
    comments = Column(String(50))
    created_at = Column(String(50))
