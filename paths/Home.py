#Python
import json
from typing import List

#Pydantic

#FastApi
from fastapi import status
from fastapi import APIRouter

#Native Modules


router = APIRouter()


## Home
@router.get(path="/", 
         status_code=status.HTTP_200_OK , 
         summary="Home",
         tags=["Five Stars Car Service"])
def home():
    """
    # Five Stars CAR SERVICE.
    ## Web EndPoints:
        -Users: 
            Login.
            Register an user.
            Update an User.
            Delete an User.
            Show an User.
            Show all Users.
        -Travels: 
            Show travel.
            Show travels by date.
            Show all travels.
            Show travel by CLient.
        Bookings:
            Show a booking.
            Show all bookings.
            Show all booking By client.
            Post a Booking.
            Delete a Booking.
        -Contact: 
            Post a Form.
        -Qualifications: 
            Show all qualifications
            Show a qualification
            Post a qualification
        -Reports:
            By date.
            By User.
            By destiny.
            By rate.
        -Rewards:
            Discounts.
            Referrals.
            
    """
    return "Welcome to Five Stars CAR SERVICE"