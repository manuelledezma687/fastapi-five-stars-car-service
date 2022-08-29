from typing import Optional
from enum import Enum
from datetime import date
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import EmailStr


class UserRegister(BaseModel):
    user_id: Optional[int]
    email: EmailStr = Field(
        ...,
        example="testing@gmail.com")
    username: str = Field(
        ...,
        max_length=20,
        example="Manuel"
        )
    first_name: str = Field(
        ...,
        min_length=0,
        max_length=20,
        example="Manuel"
        )
    last_name: str = Field(
        ...,
        min_length=0,
        max_length=20,
        example="Ledezma"
        )
    age: int = Field(
        ...,
        gt=15,
        le=99,
        example=34
        )
    country: str = Field (min_length=4, max_length=20, example="Argentina")
    language: str = Field (min_length=4,max_length=20, example="Español")
    #user_since: Optional[datetime] = Field(default=datetime.now())
    status: int = Field(default=1)
        
    class Config:
        orm_mode =True
        
class UserUpdate(BaseModel):   
    first_name:str
   

    class Config:
        orm_mode =True
        
        
class Response(BaseModel):   
    message: str
    

    
