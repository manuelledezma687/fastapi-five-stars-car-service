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
            Show an User. --> filtrado mail, filtrado datos personales
            Show all Users.
        -Travels: 
            Show travel. ---> afinar filtros
            Show all travels.
            Post a travel.
        Bookings:
            Show a booking. --> filter by client by destiny
            Show all bookings.
            Post a Booking.
            Delete a Booking. ---> lograr borrar delete
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