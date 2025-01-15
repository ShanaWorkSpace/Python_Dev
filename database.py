from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine("postgresql://postgres:12345@localhost:5432/stud_profile_db")
print("Connection successful!")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


