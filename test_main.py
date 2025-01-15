import pytest
from fastapi.testclient import TestClient


from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, StudentProfile
from schemas import StudentProfileCreate
import crud

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:12345@localhost:5432/stud_profile_db_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Override the dependency to use the test database
@pytest.fixture(scope="module")
def db():
    # Create the tables in the test database
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def client():
    client = TestClient(app)  # 'app' should be the FastAPI instance
    return client


# Test validate_password function
def test_validate_password():
    assert crud.validate_password("Password123") is True  # Valid password
    assert crud.validate_password("password123") is False  # No uppercase letter
    assert crud.validate_password("PASSWORD123") is False  # No lowercase letter
    assert crud.validate_password("Password") is False  # No number
    assert crud.validate_password("Pass123") is False  # Less than 8 characters


# Test create student profile endpoint
def test_create_student_profile(client, db):
    # Valid profile creation
    new_profile = StudentProfileCreate(name="John Doe", email="johndoe@example.com", password="Password123")
    response = client.post("/profiles/", json=new_profile.dict())
    assert response.status_code == 200
    assert response.json()["name"] == "Sia Glenn"
    assert response.json()["email"] == "siaglen@example.com"

    # Ensure the profile is saved in the database
    student = db.query(StudentProfile).filter(StudentProfile.email == "johndoe@example.com").first()
    assert student is not None

    # Test duplicate email
    response = client.post("/profiles/", json=new_profile.dict())
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"

    # Test password validation error
    new_profile_invalid = StudentProfileCreate(name="Jane Doe", email="janedoe@example.com", password="password")
    response = client.post("/profiles/", json=new_profile_invalid.dict())
    assert response.status_code == 400
    assert response.json()["detail"] == "Password does not meet the requirements"



