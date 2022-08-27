from typing import Optional
from enum import Enum
from uuid import UUID
from datetime import date
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import EmailStr


class Travels(BaseModel):
    travel_id: UUID = Field(...)
    booking_id: UUID = Field(...)
    user_id: UUID = Field(...)
    payment_method: str = Field(..., example="cash")  ## crear una lista
    amount: float = Field (...,gt=50, example=255.02)
    status: bool = Field(default=True)
    created_at: datetime = Field(default=datetime.now())
    
