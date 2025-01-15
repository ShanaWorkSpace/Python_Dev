from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

Base = declarative_base()


class StudentProfile(Base):
    __tablename__ = "student_created_profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, nullable=True)
    password = Column(String)  # Store hashed passwords in production


class TestResult(Base):
    __tablename__ = "test_results"
    id = Column(Integer, primary_key=True, index=True)
    test_name = Column(String, index=True)
    status = Column(String, index=True)
    message = Column(String, nullable=True)
    executed_at = Column(DateTime, default=datetime.utcnow)
