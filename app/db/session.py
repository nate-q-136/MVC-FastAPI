# app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.configs.settings import settings

# Tạo engine cho SQLite
DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # Dành cho SQLite

# SessionLocal để quản lý session trong các request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# app/db/base.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()