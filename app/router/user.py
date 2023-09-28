from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.cruds.user import crud_user
from app.database.session import get_db

class RequestAddUser(BaseModel):
    name: str
    blood_type: str = None
    telno: str
    
class RequestUpdateUser(BaseModel):
    blood_type: str = None
    telno: str = None

class ResponseUser(BaseModel):
    id: int
    name: str
    blood_type: str
    telno: str
    
router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=ResponseUser, status_code=201)
def add_user(body: RequestAddUser, db: Session = Depends(get_db)):
    return crud_user.create(db=db, name=body.name, blood_type=body.blood_type, telno=body.telno)

@router.get("/{user_id}", response_model=ResponseUser)
def get_one_user(user_id: int, db: Session = Depends(get_db)):
    return crud_user.get_user_by_id(db=db, id=user_id)

@router.patch("/{user_id}", response_model=ResponseUser)
def update_one_user(user_id: int, body: RequestUpdateUser, db: Session = Depends(get_db)):
    return crud_user.update_user_by_id(db=db, id=user_id, body=body)

@router.delete("/{user_id}")
def delete_one_user(user_id: int, db: Session = Depends(get_db)):
    return crud_user.delete_user_by_id(db=db, id=user_id)