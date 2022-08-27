#Python
import json
from typing import List
from http import client

#Pydantic

#FastApi
from fastapi import status
from fastapi import Body
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import APIRouter

#Native Modules
from models.Users import *


router = APIRouter()

## Users.
@router.post(
    path="/login",
    response_model=UserLogin,
    status_code=status.HTTP_200_OK,
    summary="Login User",
    tags=["Users"])
def login(user: UserLogin = Body(...)):
    """
    ## Login User

    **This path operation is for login user.**

    **- Parameters:**
    - Request body parameter
    - user: UserLogin
    
    **Returns a message confirmation.**
    """
    try:
        return JSONResponse(status_code=200, content={'message': "Login Successful, Welcome {user}"})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message': "sorry, we found an error."})

@router.post(
    path="/register", 
    response_model=User,
    status_code=status.HTTP_201_CREATED, 
    summary="Registration",
    tags=["Users"])

def post_user(user: UserRegister=Body(...)):
    """
    ## Signup

    **This path operation register a user in the app.**
    
    **- Parameters:**
    - Request body parameter
    - user: UserRegister
    
    **Returns a json with the basic user information:**
    - user_id: UUID
    - email: Emailstr
    - username: str
    - first_name: str
    - last_name: str
    - age: int
    - country: List Optional
    - language: List Optional
    - user_since: datetime Field
        
    """
    with open("data/users.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["user_since"] = str(user_dict["user_since"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user
        ##if any(users['email'] == user.email for users in results):
        ##    raise HTTPException(
        ## status_code=status.HTTP_409_CONFLICT,
        ## detail="Email already exist!")

@router.get(
    path="/users/",
    status_code=status.HTTP_200_OK,
    summary="Show All Users",
    tags=["Users"])
def show_users():
    """
    ## This path operation shows all users in the app

    **- Parameters:** 
    -

    **Returns a json list with all users in the app, with the following keys:**
    - user_id: UUID
    - email: Emailstr
    - username: str
    - first_name: str
    - last_name: str
    - age: int
    - country: List Optional
    - language: List Optional
    - user_since: datetime Field
        
    """
    with open("data/users.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
        return results
    
@router.put(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update an User",
    tags=["Users"]
)
def update_a_user(user_id, user: User = Body(...)): 
    """
    ## This path operation update an user in the app

    **- Parameters:**
    - 

    **Returns a json list with all users in the app, with the following keys:**
    - user_id: UUID
    - email: Emailstr
    - username: str
    - first_name: str
    - last_name: str
    - age: int
    - country: List Optional
    - language: List Optional
    - user_since: datetime Field
        
    """
    try:
        return JSONResponse(status_code=200, content={'message': "User Updated"})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message': "Sorry, we found an error"})


@router.delete(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete an User",
    tags=["Users"]
)
def delete_a_user(user_id): 
    """
    ## This path operation delete an user in the app

    **- Parameters:**
    - 

    **Returns a json message with a message:** 
    - message: "User Deleted"
        
    """
    try:
        return JSONResponse(status_code=200, content={'message': "User Deleted"})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message': "Sorry, we found an error"})
