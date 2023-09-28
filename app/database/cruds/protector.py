from fastapi import HTTPException
from app.database.base import Protector
from sqlalchemy.orm import Session

from app.database.models.user import User

class crud_protector:
    def create(db: Session, name, relationship, telno, user_id):
        db_protector = Protector(relationship=relationship, name=name, telno=telno, user_id=user_id)
        db.add(db_protector)
        db.commit()
        db.refresh(db_protector)
        return db_protector
    
    def get_protector_by_id(db: Session, id):
        db_protector = db.get(Protector, id)
        return db_protector
    
    def get_protector_by_user_id(db: Session, id):
        db_protectors = (db.query(Protector)
                            .join(User, Protector.user_id == id)
                            .all())
        res = []
        for protector in db_protectors:
            res.append({
                "id": protector.id,
                "user_id": protector.user_id,
                "telno": protector.telno,
                "name": protector.name,
                "relationship": protector.relationship
            })
        return res
    
    def update_protector_by_id(db: Session, id, body):
        db_protector = db.get(Protector, id)
        if not db_protector:
            raise HTTPException(status_code=404, detail="Protector not found")
        new_data = body.dict(exclude_unset=True)
        for key, value in new_data.items():
            if value:
                setattr(db_protector, key, value)  
        db.add(db_protector)
        db.commit()
        db.refresh(db_protector)
        return db_protector
    
    def delete_protector_by_id(db: Session, id):
        db_protector = db.get(Protector, id)
        if not db_protector:
            raise HTTPException(status_code=404, detail="Protector not found")
        db.delete(db_protector)
        db.commit()
        return {"deleted": True}
        