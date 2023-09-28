from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.cruds.protector import crud_protector
from app.database.session import get_db

class RequestAddProtector(BaseModel):
    telno: str
    name: str
    relationship: str
    user_id: int
    
class RequestUpdateProtector(BaseModel):
    telno: str

class ResponseProtector(BaseModel):
    id: int
    telno: str
    name: str
    relationship: str
    
    
router = APIRouter(
    prefix="/protector",
    tags=["protector"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=ResponseProtector, status_code=201)
def add_protector(body: RequestAddProtector, db: Session = Depends(get_db)):
    return crud_protector.create(db=db, name=body.name, telno=body.telno, relationship=body.relationship, user_id=body.user_id)

@router.get("/{protector_id}", response_model=ResponseProtector)
def get_one_protector(protector_id: int, db: Session = Depends(get_db)):
    return crud_protector.get_protector_by_id(db=db, id=protector_id)

@router.get("/")
def get_protectors_of_user(user_id: int, db: Session = Depends(get_db)):
    return crud_protector.get_protector_by_user_id(db=db, id=user_id)

@router.patch("/{protector_id}", response_model=ResponseProtector)
def update_one_protector(protector_id: int, body: RequestUpdateProtector, db: Session = Depends(get_db)):
    return crud_protector.update_protector_by_id(db=db, id=protector_id, body=body)

@router.delete("/{protector_id}")
def delete_one_protector(protector_id: int, db: Session = Depends(get_db)):
    return crud_protector.delete_protector_by_id(db=db, id=protector_id)