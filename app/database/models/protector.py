from sqlalchemy import Column, ForeignKey, Integer, String
from app.database.base_class import Base


class Protector(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    name = Column(String(255), nullable=True)
    telno = Column(String(255), nullable=True)
    relationship = Column(String(255), nullable=True)