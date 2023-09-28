from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router import health_info, protector, user
from .database.base import Base
from .database.session import engine

origins = ["*"]

def create_table():
    Base.metadata.create_all(bind=engine)
    
def get_application():
    app = FastAPI(title="Night Watch", version="0.1.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    create_table()
    return app

app = get_application()

app.include_router(user.router)
app.include_router(protector.router)
app.include_router(health_info.router)