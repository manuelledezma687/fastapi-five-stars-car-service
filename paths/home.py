from fastapi import status
from fastapi import APIRouter


router = APIRouter()


@router.get(path="/",
         status_code=status.HTTP_200_OK ,
         summary="Home",
         tags=["Five Stars Car Service"])
def home():
    """
    # FIVE STARS CAR SERVICE.
    ## Web EndPoints:
        -Users:
            Login.
            Register an user.
            Update an User.
            Delete an User.
            Show an User.
            Show all Users.
        Bookings:
            Show a booking.
            Show all bookings.
            Post a Booking.
            Delete a Booking.
        -Contact:
            Post a Form.
        -ratings:
            Show all ratings
            Show a rating per id
            Post a rating
    """
    return "Welcome to Five Stars CAR SERVICE"
