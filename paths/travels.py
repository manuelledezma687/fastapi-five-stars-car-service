#Python
import json
from http import client

#Pydantic

#FastApi
from fastapi import status
from fastapi import Body
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import APIRouter

#Native Modules
from schemas.Travels import *


router = APIRouter()


## Travels.
@router.get(
    path="/travels",
    status_code=status.HTTP_200_OK,
    summary="Show All travels",
    tags=["Travels"])
def show_travels():
    """
    ## This path operation shows all travels in the app.

    **- Parameters:** 
    -

    **Returns a json list with all travels in the app, with the following keys:**
    - travel_id: UUID
    - booking_id: UUID
    - user_id: UUID
    - payment_method: List
    - amount: float
    - status: bool
    - Created_at: datetime Field
                
    """
    with open("data/travels.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
        return results

@router.post(
    path="/travels",
    response_model=Travels,
    status_code=status.HTTP_201_CREATED,
    summary="Post a travel",
    tags=["Travels"])
def post_travels(travel: Travels=Body(...)):
    """
    ## This path operation post a travel in the app.

    **Parameters:**
    travel: Travels

    **Returns a json list with a created travel in the app, with the following keys:**
    - travel_id: UUID
    - booking_id: UUID
    - user_id: UUID
    - payment_method: List
    - amount: float
    - status: bool
    - Created_at: datetime Field
        
    """
    with open("data/travels.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
        travels_dict = travel.dict()
        travels_dict["travel_id"] = str(travels_dict["travel_id"])
        travels_dict["booking_id"] = str(travels_dict["booking_id"])
        travels_dict["user_id"] = str(travels_dict["user_id"])
        travels_dict["created_at"] = str(travels_dict["created_at"])
        results.append(travels_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return travel