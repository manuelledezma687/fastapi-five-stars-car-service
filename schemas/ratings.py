from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Ratings(BaseModel):
    rating_id: Optional[int] = Field(gt=0)
    booking_id: int =Field(...,gt=0)
    stars: int = Field(..., gt=0, le=5)
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
    comments: str = Field(
        ...,
        min_length=0,
        max_length=50,
        example="Hi it is a excelent service."
        )
    created_at: datetime = Field(default=datetime.now())

    class Config:
        orm_mode =True
