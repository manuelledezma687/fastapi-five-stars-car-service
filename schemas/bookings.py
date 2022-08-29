from typing import Optional
from enum import Enum
from uuid import UUID
from datetime import date
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import EmailStr


class Bookings(BaseModel):
    booking_id: UUID = Field(...)
    user_id: UUID = Field(...)
    email: EmailStr = Field(
        ...,
        example="manuelledezma@gmail.com")
    username: str = Field(
        ...,
        max_length=20,
        example="manuel687"
        )
    destiny: str = Field(
        ...,
        min_length=0,
        max_length=20,
        example="Miami"
        )
    telephone: int = Field(
        ...,
        example=11343454322
        )
    amount_of_booking: float = Field (...,gt=50)
    created_at: datetime = Field(default=datetime.now())