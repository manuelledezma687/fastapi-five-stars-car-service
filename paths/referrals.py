from typing import List
from typing import Union
from fastapi import status
from fastapi import Path, Query
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from connections import SessionLocal,engine
from sqlalchemy.orm import Session
from fastapi.params import Depends

import models
from schemas.referrals import Referrals

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get(path="/referrals/{referral_id}",
            response_model=Referrals,
            status_code=status.HTTP_200_OK, 
            summary="Show a valid referral",
            tags=["Referrals"])
def show_referral(referral_id:int = Path(...,gt=0),db:Session=Depends(get_db)):
    """
    ## This path operation shows a valid referral in the app.

    **- Parameters:** 
    - referral_id: int

    **Returns a json with a valid referral in the app, with the following keys:**
    - referral_code: str
    - email : EmailStr
    - telephone : int
    - first_name : str
    - last_name : str
    - user_since: datetime Field
    - status : int
           
    """
    try:
        referral = db.query(models.Referrals).filter_by(referral_id=referral_id).first()
        db.commit()
        db.refresh(referral)
        return referral_id
    except Exception as error:
        print(error)
        return JSONResponse(status_code=404, content={'message':'Referral Not Found.'})
    
    
@router.get(
    path="/referrals",
    response_model=List[Referrals],
    status_code=status.HTTP_200_OK,
    summary="Show All Referrals",
    tags=["Referrals"])
def show_referrals(db:Session=Depends(get_db), 
                  skip: int = Query(default=0) , limit: Union[int, None] = None):
    """
    ## This path operation shows all valid referrals in the app.

    **- Parameters:** 

    **Returns a json with all valid referrals in the app, with the following keys:**
    - referral_code: str
    - email : EmailStr
    - telephone : int
    - first_name : str
    - last_name : str
    - user_since: datetime Field
    - status : int
           
    """
    referrals = db.query(models.Referrals).all()
    return referrals

@router.post(
    path="/referrals",
    response_model=Referrals,
    status_code=status.HTTP_201_CREATED,
    summary="Post a Referrals",
    tags=["Referrals"])
def post_referral(entry_point:Referrals,db:Session=Depends(get_db)):
    """
    ## This path operation post a referrals in the app.

    **- Parameters:**
    - referrals: Referrals

    **Returns a json body with a message:** 
    - message: "Referrals Saved successfully"

    """
    try:
        referral = models.Referrals(referral_code = entry_point.referral_code,
                                    email = entry_point.email,
                                    observations = entry_point.observations,
                                    telephone = entry_point.telephone,
                                    first_name = entry_point.first_name,
                                    last_name = entry_point.last_name,
                                    user_since =entry_point.user_since
                                    status = entry_point.status)
        db.add(referral)
        db.commit()
        db.refresh(referral)
        return JSONResponse(status_code=201, content={'message': "Referrals Saved successfully"})
    except:
        return JSONResponse(status_code=500, content={'message': "Sorry, there is an error"})