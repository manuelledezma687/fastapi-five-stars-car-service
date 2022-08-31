from fastapi import status
from fastapi import APIRouter


router = APIRouter()


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
            Show all travels.
            Post a travel.
        Bookings:
            Show a booking. 
            Show all bookings.
            Post a Booking.
            Delete a Booking.
        -Contact: 
            Post a Form.
        -ratings: 
            Show all ratings
            Show all ratings per stars
            Show all ratings per users
            Show a rating per id
            Post a rating
        -Rewards: In Definition
            Discounts.
            Referrals.
            
    """
    return "Welcome to Five Stars CAR SERVICE"