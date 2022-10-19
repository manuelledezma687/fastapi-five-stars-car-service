from typing import Optional
from enum import Enum
from datetime import date
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import EmailStr

class Bookings(BaseModel):
    booking_id: Optional[int] = Field(gt=0)
    type_of_travel: str = Field(
        ...,
        min_length=0,
        max_length=20,
        example="hourly"
        )
    pick_up_location: str = Field(
        ...,
        min_length=0,
        max_length=150,
        example="Atlanta Airport"
        )
    drop_off_location: str = Field(
        ...,
        min_length=0,
        max_length=150,
        example="Miami"
        )
    flight_id: str = Field(
        ...,
        min_length=0,
        max_length=20,
        example="MSE2123"
        )
    passengers: int = Field (...,gt=0, example=3)
    full_name: str = Field(
        ...,
        min_length=0,
        max_length=30,
        example="Mike Adams"
        )
    email: EmailStr = Field(
        ...,
        example="joseotero@gmail.com")
    observations: str = Field(
        ...,
        min_length=10,
        max_length=200,
        example="Hi, this is a comment."
        )
    payment_method: str = Field(
        ...,
        min_length=0,
        max_length=20,
        example="Cash"
        )
    date: str = Field(
        ...,
        min_length=0,
        max_length=20,
        example="05/05/2022"
        )
    hour: str = Field(
        ...,
        min_length=0,
        max_length=20,
        example="01:00"
        )
    created_at: datetime = Field(default=datetime.now())
    status: int = Field(default=1)
    
    class Config:
        orm_mode =True