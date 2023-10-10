from datetime import datetime
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.cruds.health_info import crud_health_info
from app.database.session import get_db

class RequestAddHealthInfo(BaseModel):
    heart_rate: int
    oxygen_saturation: str
    user_id: int

class ResponseHealthInfo(BaseModel):
    id: int
    heart_rate: int
    oxygen_saturation: str
    measure_at: datetime
    user_id: int 
    
router = APIRouter(
    prefix="/healthInfo",
    tags=["healthInfo"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=ResponseHealthInfo, status_code=201)
def add_health_info(body: RequestAddHealthInfo, db: Session = Depends(get_db)):
    return crud_health_info.create(db=db, heart_rate=body.heart_rate, oxygen_saturation=body.oxygen_saturation, user_id=body.user_id)

@router.get("/")
def get_health_info_of_user_in_day(user_id: int, year:int, month: int, day: int, duration: str, db: Session = Depends(get_db)):
    if(duration == "7-days"):
        return crud_health_info.get_health_info_by_user_id_in_7days(db=db, id=user_id, year=year, month=month, day=day)
    elif(duration == "31-days"):
        return crud_health_info.get_health_info_by_user_id_in_31days(db=db, id=user_id, year=year, month=month, day=day)
    elif(duration == "12-month"):
        return crud_health_info.get_health_info_by_user_id_in_12month(db=db, id=user_id, year=year, month=month, day=day)
    
@router.get("/latest/{user_id}")
def get_health_info_of_user_in_day(user_id: int, db: Session = Depends(get_db)):
    return crud_health_info.get_health_info_by_user_id_latest_one(db=db, id=user_id)
     
