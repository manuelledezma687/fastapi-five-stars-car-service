#Python
import json
from http import client

#Pydantic
from pydantic import EmailStr

#FastApi
from fastapi import status
from fastapi import Form
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import APIRouter

#Native Modules
from schemas.Contact import Contact


router = APIRouter()


## Contact.
@router.post(
    path="/contact", 
    status_code=status.HTTP_201_CREATED, 
    summary="Contact Form",
    tags=["Contact Us"])
def contact(
    name: str=Form(
        ...,
        min_length=5,
        max_length=20),
    email: EmailStr = Form(...), 
    comments: str =Form(
        ...,
        min_length=5,
        max_length=250)):
    """
    ## This path operation is for direct contact with fivestarscarservice.com

    **- Request body parameter:**
    - **Form**:
        mane: str
        email: EmailStr
        comments: str

    **Returns a message confirmation:**
    - "Thank you very much for sending your message, we will contact you shortly."
        
    """
    return JSONResponse(status_code=201, content={'message': "Thank you very much for sending your message, we will contact you shortly."})