"""
This file can initialize to connect the database when you run the server.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Items.Items_models import Base

DATABASE_URL = "postgresql://postgres:12345@localhost/prac"

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(engine) # This code will create columns automatically when run server

def get_session():
    session = sessionLocal()
    try:
        yield session
    finally:
        session.close()