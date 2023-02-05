from typing import List
from fastapi import status
from fastapi import Path, Query
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
import models
from schemas.ratings import Ratings
from connections import SessionLocal,engine


models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get(path="/ratings/{rating_id}",
            response_model=Ratings,
            status_code=status.HTTP_200_OK,
            summary="Show a valid Rating",
            tags=["Ratings"])
def show_rating(rating_id:int = Path(...,gt=0),db:Session=Depends(get_db)):
    """
    ## This path operation shows a valid rating in the app
    **- Parameters:**
    - rating_id : int
    **Returns a json with a valid rating in the app, with the following keys:**
    - rating_id: int Primary Key
    - booking_id: int FR
    - stars: int
    - first_name: str
    - last_nam: str
    - comments: str
    - created_at: datetime Field
    """
    try:
        rating = db.query(models.Ratings).filter_by(rating_id=rating_id).first()
        db.commit()
        db.refresh(rating)
        return rating
    except Exception as error:
        print(error)
        return JSONResponse(status_code=404, content={'message':'Rating Not Found.'})


@router.get(path='/ratings',
            response_model=List[Ratings],
            status_code=status.HTTP_200_OK,
            summary="Show Ratings",
            tags=["Ratings"])
def show_ratings(db:Session=Depends(get_db),
                 skip: int | None= Query(default=0),
                 limit: int| None = Query(default=10)):
    """
    ## This path operation shows all ratings in the app
    **- Parameters:**
    -
    **Returns a json list with all ratings in the app, with the following keys:**
    - rating_id: int Primary Key
    - booking_id: int FR
    - stars: int
    - first_name: str
    - last_nam: str
    - comments: str
    - created_at: datetime Field
    """
    ratings = db.query(models.Ratings).all()
    return ratings[skip: skip + limit]


@router.post(
    path="/ratings",
    response_model=Ratings,
    status_code=status.HTTP_201_CREATED,
    summary="Register a rating.",
    tags=["Ratings"])
def post_rating(entry_point:Ratings,db:Session=Depends(get_db)):
    """
    ## Pos a rating
    **This path operation register a rating in the app.**
    **- Parameters:**
    - rating: Ratings
    **Returns a json body with a message:**
    - message: "rating sent Successfully"
    """
    try:
        rating = models.Ratings(booking_id = entry_point.booking_id,
                                stars = entry_point.stars,
                                first_name = entry_point.first_name,
                                last_name = entry_point.last_name,
                                comments = entry_point.comments,
                                created_at = entry_point.created_at)
        db.add(rating)
        db.commit()
        db.refresh(rating)
        return JSONResponse(status_code=201, content={'message': "rating sent Successfully"})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message': 'Sorry, there is an error'})
