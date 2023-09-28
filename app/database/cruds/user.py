from fastapi import HTTPException
from app.database.base import User
from sqlalchemy.orm import Session

class crud_user:
    def create(db: Session, name, blood_type, telno):
        db_user = User(blood_type=blood_type, name=name, telno=telno)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def get_user_by_id(db: Session, id):
        db_user = db.get(User, id)
        return db_user
    
    def update_user_by_id(db: Session, id, body):
        db_user = db.get(User, id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        new_data = body.dict(exclude_unset=True)
        for key, value in new_data.items():
            if value:
                setattr(db_user, key, value)  
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def delete_user_by_id(db: Session, id):
        db_user = db.get(User, id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        db.delete(db_user)
        db.commit()
        return {"deleted": True}