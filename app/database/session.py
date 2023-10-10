from sqlalchemy import create_engine
from app.core.config import get_settings
from sqlalchemy.orm import sessionmaker


settings = get_settings()
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{}:{}@{}:{}/{}".format(
    settings.MARIADB_USER,
    settings.MARIADB_PASSWORD,
    settings.MARIADB_HOST,
    settings.MARIADB_PORT,
    settings.MARIADB_DATABASE,
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
