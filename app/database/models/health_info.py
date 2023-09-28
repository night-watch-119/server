from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from app.database.base_class import Base


class Health_info(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    heart_rate = Column(Integer, nullable=True)
    oxygen_saturation = Column(String(255), nullable=True)
    measure_at = Column(DateTime, default=datetime.now)