from typing import Optional
from enum import Enum
from uuid import UUID
from datetime import date
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import EmailStr


class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(
        ...,
        example="manuelledezma@gmail.com")
    
class UserLoginOk(BaseModel):
    
    message: str=Field(default="Login exitoso")

class User(UserBase):
    username: str = Field(
        ...,
        max_length=20,
        example="Manuel"
        )
    first_name: str = Field(
        ...,
        min_length=0,
        max_length=50,
        example="Manuel"
        )
    last_name: str = Field(
        ...,
        min_length=0,
        max_length=50,
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
    user_since: datetime = Field(default=datetime.now())
    
class UserRegister(User):
    password: str = Field(
    ..., 
    min_length=8,
    max_length=64,
    example="Mamamia20202"
)

class UserLogin(UserBase):
    password: str = Field(
    ..., 
    min_length=8,
    max_length=64,
    example="Mamamia20202"
)
    
