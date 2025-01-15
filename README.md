Python FastAPI Student Profile System
This project implements a system for creating and managing student profiles using Python's FastAPI framework and PostgreSQL for the database. It includes validation for password policies, user-friendly error messages, unit tests, and proper documentation.

Functional Requirements
Profile Creation
The system supports creating a student profile with the following fields:

Name (Required, String)
Email (Required, Valid Email Address)
Phone (Optional, Numeric)
Password (Required, String, Must meet password policy)
Password Policy Validation
Passwords must adhere to the following rules:

At least 8 characters long.
Include at least one uppercase letter (A-Z).
Include at least one lowercase letter (a-z).
Include at least one numeric digit (0-9).
Include at least one special character (e.g., @, #, $, %).
System Behavior
If the password does not meet policy requirements, an error message is displayed.
Upon successful profile creation, a confirmation message is shown.

Installation
Prerequisites
Python 3.8 or higher
PostgreSQL
Git
Virtual Environment (recommended)

Clone the repository:
git clone https://github.com/ShanaWorkSpace/Python_Dev.git
cd Python_Dev

Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Update the database connection

API Endpoints
POST /profiles
Creates a new student profile.

Request Body
{
  "name": "Jia",
  "email": "jiya@erediff.com",
  "phone": "1234567890",
  "password": "Password@1234"
}

Responses
201 Created: Profile successfully created.
400 Bad Request: Validation errors.

Unit Testing
Unit tests are written using pytest.

Running the Application
Start the FastAPI application:
uvicorn app.main:app --reload

Access the API documentation at:
Swagger UI: http://127.0.0.1:8000/docs


Main Components:
models.py: Defines the StudentProfile SQLAlchemy model that represents the student data.
schemas.py: Contains the Pydantic models for data validation and serialization.
crud.py: Handles the business logic for profile creation and password validation.
main.py: Defines the FastAPI application and the /profiles/ endpoint for creating student profiles.
database.py: Manages database connection and session handling.
test_profile.py: Contains unit tests to ensure correct implementation of the password validation and the profile creation endpoint.

Set Up PostgreSQL Database
Ensure that PostgreSQL is installed and running on your machine.

Create a new database for the project (e.g., stud_profile_db):
psql -U postgres -c "CREATE DATABASE stud_profile_db;"

Or, for a test database:
psql -U postgres -c "CREATE DATABASE stud_profile_db_test;"

 Configure Database Connection
In database.py, configure the PostgreSQL connection string. Example:
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:your-password@localhost:5432/stud_profile_db"

Replace your-password with the password for your PostgreSQL user.

Running the Application
1. Start the FastAPI Server
To start the FastAPI development server, use uvicorn:
uvicorn main:app --reload
This will start the FastAPI application at http://127.0.0.1:8000.

Testing the Application
Install Test Dependencies
  Install testing dependencies with:
    pip install pytest fastapi sqlalchemy psycopg2 pytest-asyncio

Create the Test Database
  Ensure that the test database (stud_profile_db_test) exists. If it's not available, create it:
    psql -U postgres
    CREATE DATABASE stud_profile_db_test;

Run Tests
Execute the tests with pytest to verify functionality:
pytest test_main.py

Notes
Ensure that the PostgreSQL service is running before starting the application.
If you encounter any errors, check the PostgreSQL logs, FastAPI logs, or test client outputs for detailed error messages.
This project uses basic FastAPI functionality combined with SQLAlchemy for database interactions. The implementation ensures robust password validation and supports testing for both the password function and profile creation API.

