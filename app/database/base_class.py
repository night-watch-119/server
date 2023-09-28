from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    id: Any
    __name__: str
    
    # 클래스 이름으로부터 테이블 이름 생성
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()