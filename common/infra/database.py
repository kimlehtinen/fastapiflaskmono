import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

env = os.getenv('ENV', 'production')

if env == 'local':
    DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/publicapi'
else:
    DATABASE_URL = 'postgresql://postgres:postgres@db:5432/publicapi'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

db = SQLAlchemy()

def get_db():
    db_session = SessionLocal()

    try:
        yield db_session
    finally:
        db_session.close()
