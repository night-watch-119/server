from functools import lru_cache
import os
from dotenv import load_dotenv

from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    MARIADB_HOST: str
    MARIADB_PORT: int
    MARIADB_DATABASE: str
    MARIADB_USER: str
    MARIADB_PASSWORD: str
    MARIADB_ROOT_PASSWORD: str
     
    class Config:
        env_file = '.env'
        orm_mode = True
    
@lru_cache()
def get_settings():
    return Settings()