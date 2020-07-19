import os
import pathlib


BASE_DIR = pathlib.Path(__file__).parent
UPLOADS_DIR = BASE_DIR / 'uploads'
DOMAIN = '127.0.0.1:5000'


class Config:
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
