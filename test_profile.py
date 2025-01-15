import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is in 'main.py'


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


def test_create_student_profile(client):
    # Valid profile creation
    new_profile = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "1234567890",  # Optional field
        "password": "Password123"
    }
    response = client.post("/profiles", json=new_profile)
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "johndoe@example.com"


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
    assert response.status_code == 422


