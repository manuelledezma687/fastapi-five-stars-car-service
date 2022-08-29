#Python
import json
from typing import List,Optional
from http import client

#Pydantic

#FastApi
from fastapi import status
from fastapi import Body, Path
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import APIRouter

#Native Modules
from schemas.Bookings import *


router = APIRouter()


## Bookings.
@router.get(
    path="/bookings",
    status_code=status.HTTP_200_OK,
    summary="Show All Bookings",
    tags=["Bookings"])
def show_bookings():
    """
    ## This path operation shows all bookings in the app.

    **- Parameters:** 
    -

    **Returns a json list with all bookings in the app, with the following keys:**
    - booking_id: UUID
    - user_id: UUID
    - email: EmailStr
    - username: str
    - Destiny: str
    - Telephone: int
    - amount_of_booking: float
    - created_at: datetime Field
                
    """
    with open("data/bookings.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
        return results

@router.post(
    path="/bookings",
    response_model=Bookings,
    status_code=status.HTTP_201_CREATED,
    summary="Post a booking",
    tags=["Bookings"])
def post_booking(booking: Bookings=Body(...)):
    """
    ## This path operation post a booking in the app.

    **Parameters:**
    bookings: Bookings

    **Returns a created booking in the app, with the following keys:**
    - booking_id: UUID
    - user_id: UUID
    - email: EmailStr
    - username: str
    - Destiny: str
    - Telephone: int
    - amount_of_booking: float
    - created_at: datetime Field

    """
    with open("data/bookings.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
        bookings_dict = booking.dict()
        bookings_dict["user_id"] = str(bookings_dict["user_id"])
        bookings_dict["booking_id"] = str(bookings_dict["booking_id"])
        bookings_dict["created_at"] = str(bookings_dict["created_at"])
        results.append(bookings_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return booking
    
@router.delete(
    path="/bookings/{booking_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete a Booking",
    tags=["Bookings"])
def delete_booking(booking_id):
    """
    ## This path operation delete a booking in the app.

    **Parameters:**
    booking_id: UUID

    **Returns a json Response with the result for this operation.**

    """
    try:
        return JSONResponse(status_code=200, content={'message': "Your Booking was deleted"})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message': "Sorry, We found an error"})

