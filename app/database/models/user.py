from sqlalchemy import Column, Integer, String
from app.database.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=True)
    telno = Column(String(255), nullable=True)
    blood_type = Column(String(255), nullable=True)