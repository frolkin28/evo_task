import os
import pathlib


BASE_DIR = pathlib.Path(__file__).paren


class Config:
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
