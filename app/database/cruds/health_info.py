import calendar
from datetime import datetime, timedelta
from app.database.base import Health_info
from sqlalchemy.orm import Session

from app.database.models.user import User

class crud_health_info:
    def create(db: Session, heart_rate, oxygen_saturation, user_id):
        db_protector = Health_info(heart_rate=heart_rate, oxygen_saturation=oxygen_saturation, user_id=user_id)
        db.add(db_protector)
        db.commit()
        db.refresh(db_protector)
        return db_protector
    
    def get_health_info_by_user_id(db: Session, id, year, month, day):
        start_date = datetime(year=year, month=month, day=day)
        end_date = datetime(year=year, month=month, day=day+1)
        db_health_info = (db.query(Health_info)
                            .join(User, Health_info.user_id == id)
                            .filter(Health_info.measure_at >= start_date, Health_info.measure_at < end_date)
                            .all())
        res = []
        for health_info in db_health_info:
            res.append({
                "id": health_info.id,
                "user_id": health_info.user_id,
                "heart_rate": health_info.heart_rate,
                "oxygen_saturation": health_info.oxygen_saturation,
                "measure_at": health_info.measure_at
            })
        return res
    
    def get_health_info_by_user_id_in_month(db: Session, id, year, month):
        start_date = datetime(year=year, month=month, day=1)
        end_date = datetime(year=year, month=month+1, day=1)
        db_health_info = (db.query(Health_info)
                            .join(User, Health_info.user_id == id)
                            .filter(Health_info.measure_at >= start_date, Health_info.measure_at < end_date)
                            .all())
        res = []
        for health_info in db_health_info:
            res.append({
                "id": health_info.id,
                "user_id": health_info.user_id,
                "heart_rate": health_info.heart_rate,
                "oxygen_saturation": health_info.oxygen_saturation,
                "measure_at": health_info.measure_at
            })
        return res
        