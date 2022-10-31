from typing import Optional
from enum import Enum
from datetime import date
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import EmailStr

class Referrals(BaseModel):
    
    referral_id: Optional[int] = Field(gt=0)
    referral_code: str = Field(
        min_length=0,
        max_length=20,
        example="MCLKD123"
        )
    email: EmailStr = Field(
        ...,
        example="joseotero@gmail.com")
    telephone: int = Field(
        ...,
        example=1123322345
        )
    first_name: str = Field(
        ...,
        min_length=0,
        max_length=20,
        example="Jose"
        )
    last_name: str = Field(
        ...,
        min_length=0,
        max_length=20,
        example="Otero"
        )
    user_since: datetime = Field(default=datetime.now())
    status: int = Field(default=1)
    

    class Config:
        orm_mode =True