import json
from typing import List
from http import client

from fastapi import status
from fastapi import Path
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from connections import SessionLocal,engine
from sqlalchemy.orm import Session
from fastapi.params import Depends

import models
from schemas.users import UserRegister, UserUpdate

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get(path="/users/{user_id}",
            response_model=UserRegister,
            status_code=status.HTTP_200_OK, 
            summary="Show a valid User",
            tags=["Users"])
def show_user(user_id:int = Path(...,gt=0),db:Session=Depends(get_db)):
    """
    ## This path operation shows a valid user in the app

    **- Parameters:** 
    -

    **Returns a json list with a valid user in the app, with the following keys:**
    - user_id: int PK
    - email: Emailstr
    - telephone: int
    - username: str
    - first_name: str
    - last_name: str
    - age: int
    - country: List Optional
    - language: List Optional
    - user_since: datetime Field
    - status: int
    
    """
    try:
        user = db.query(models.Users).filter_by(user_id=user_id).first()
        db.commit()
        db.refresh(user)
        if not user:
            return JSONResponse(status_code=400, content={'message':'User Not Found.'})
        else:
            return user
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message': 'Sorry, there is an error'})


@router.get(path='/users',
            response_model=List[UserRegister],
            status_code=status.HTTP_200_OK, 
            summary="Show Users",
            tags=["Users"])
def show_users(db:Session=Depends(get_db)):
    """
    ## This path operation shows all users in the app

    **- Parameters:** 
    -

    **Returns a json list with all users in the app, with the following keys:**
    - user_id: int PK
    - email: Emailstr
    - telephone: int
    - username: str
    - first_name: str
    - last_name: str
    - age: int
    - country: List Optional
    - language: List Optional
    - user_since: datetime Field
    - status: int
    
    """
    users = db.query(models.Users).all()
    return users


@router.post(
    path="/users", 
    response_model=UserRegister,
    status_code=status.HTTP_201_CREATED, 
    summary="Register an user.",
    tags=["Users"])
def create_user(entry_point:UserRegister,db:Session=Depends(get_db)):
    """
    ## Signup

    **This path operation register a user in the app.**
    
    **- Parameters:**
    - user: UserRegister
    
    **Returns a json message with a message:** 
    - message: "User Register Successfully"
        
    """
    try:
        user = models.Users(email = entry_point.email, 
                            telephone = entry_point.telephone,
                            username = entry_point.username,
                            first_name = entry_point.first_name,
                            last_name = entry_point.last_name,
                            age = entry_point.age, 
                            country = entry_point.country,
                            language = entry_point.language,
                            status = entry_point.status)
        db.add(user)
        db.commit()
        db.refresh(user)
        return JSONResponse(status_code=201, content={'message': "User Register Successfully"})
    except:
        return JSONResponse(status_code=500, content={'message': "Sorry, there is an error"})


@router.put(
    path="/users/{user_id}",
    response_model=UserRegister,
    status_code=status.HTTP_200_OK,
    summary="Update an User",
    tags=["Users"])
def update_a_user(user_id:int,entry_point:UserUpdate,db:Session=Depends(get_db)):
    """
    ## This path operation update an user in the app

    **- Parameters:**
    - user_id: int

    **Returns a json message with a message:** 
    - message: "User Updated"
        
    """
    try:
        user = db.query(models.Users).filter_by(user_id=user_id).first()
        user.first_name = entry_point.first_name
        db.commit()
        db.refresh(user)
        if not user:
            return JSONResponse(status_code=400, content={'message':'User Not Found.'})
        else:
            return JSONResponse(status_code=200, content={'message': "User was Updated"})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message': 'Sorry, there is an error'})


@router.delete('/users/{user_id}',
               status_code=status.HTTP_200_OK, 
               summary="Delete an user",
               tags=["Users"])
def delete_users(user_id:int = Path(...,gt=0),db:Session=Depends(get_db)):
    """
    ## This path operation delete an user in the app

    **- Parameters:**
    - user_id: int

    **Returns a json message with a message:** 
    - message: "User Deleted"
        
    """
    try:
        user = db.query(models.Users).filter_by(user_id=user_id).first()
        db.delete(user)
        db.commit()
        if not user:
            return JSONResponse(status_code=400, content={'message':'User Not Found.'})
        else:
            return JSONResponse(status_code=200, content={'message': "User was deleted"})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message': 'Sorry, there is an error'})