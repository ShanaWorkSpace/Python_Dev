import pytest
from fastapi.testclient import TestClient
from utils import log_test_result

from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


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
    return TestClient(app)


def test_create_student_profile(client):

    # Valid profile creation
    new_profile = {
        "name": "Jain",
        "email": "johdoe@gmail.com",
        "phone": "1234567890",  # Optional field
        "password": "Password@123"
    }
    response = client.post("/profiles", json=new_profile)
    assert response.status_code == 200
    assert response.json()["name"] == "Jain"
    assert response.json()["email"] == "johdoe@gmail.com"


def test_create_student_profile_missing_name(client):
    # Missing 'name' field
    new_profile = {
        "email": "johndoe@example.com",
        "phone": "1234567890",
        "password": "Password123"
    }
    response = client.post("/profiles", json=new_profile)
    assert response.status_code == 422


def test_create_student_profile_invalid_email(client):
    # Invalid email format
    new_profile = {
        "name": "Jane Doe",
        "email": "invalid-email",
        "phone": "0987654321",
        "password": "Password123"
    }
    response = client.post("/profiles", json=new_profile)
    assert response.status_code == 422


def test_create_student_profile_missing_password(client):
    # Missing 'password' field
    new_profile = {
        "name": "Alice",
        "email": "alice@example.com",
        "phone": "1122334455"
    }
    response = client.post("/profiles", json=new_profile)
    assert response.status_code == 422


def test_create_student_profile_invalid_password(client):
    # Invalid password (too short)
    new_profile = {
        "name": "Bob",
        "email": "bob@example.com",
        "phone": "5566778899",
        "password": "short"
    }
    response = client.post("/profiles", json=new_profile)
    assert response.status_code == 400


