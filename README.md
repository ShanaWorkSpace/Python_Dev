Project Documentation: FastAPI Student Profile Application
Project Overview
This project is a FastAPI application designed to manage student profiles. The application allows users to create student profiles, ensuring that basic validation criteria for passwords and unique email addresses are met. The project includes:

Password validation (minimum length, uppercase, lowercase, and numeric characters).
An API to create student profiles.
Unit tests to ensure proper functionality.
Table of Contents
Application Structure
Installation Instructions
Running the Application
Testing the Application
Notes
Application Structure
Main Components:
models.py: Defines the StudentProfile SQLAlchemy model that represents the student data.
schemas.py: Contains the Pydantic models for data validation and serialization.
crud.py: Handles the business logic for profile creation and password validation.
main.py: Defines the FastAPI application and the /profiles/ endpoint for creating student profiles.
database.py: Manages database connection and session handling.
test_main.py: Contains unit tests to ensure correct implementation of the password validation and the profile creation endpoint.
Installation Instructions
1. Install Dependencies
To install all the necessary dependencies for the project, run:


pip install -r requirements.txt
2. Set Up PostgreSQL Database
Ensure that PostgreSQL is installed and running on your machine.

Create a new database for the project (e.g., stud_profile_db):

psql -U postgres -c "CREATE DATABASE stud_profile_db;"
Or, for a test database:


psql -U postgres -c "CREATE DATABASE stud_profile_db_test;"
3. Configure Database Connection
In database.py, configure the PostgreSQL connection string. Example:


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:your-password@localhost:5432/stud_profile_db"
Replace your-password with the password for your PostgreSQL user.

4. Run Migrations (If Using Alembic)
If you are using Alembic for migrations, run the following command to apply migrations:


alembic upgrade head
If not using migrations, make sure that the tables are created using the following code in main.py:


from models import Base, engine
Base.metadata.create_all(bind=engine)
Running the Application
1. Start the FastAPI Server
To start the FastAPI development server, use uvicorn:


uvicorn main:app --reload
This will start the FastAPI application at http://127.0.0.1:8000.

Testing the Application
1. Install Test Dependencies
Install testing dependencies with:


pip install pytest fastapi sqlalchemy psycopg2 pytest-asyncio
2. Create the Test Database
Ensure that the test database (stud_profile_db_test) exists. If it's not available, create it:


psql -U postgres
CREATE DATABASE stud_profile_db_test;
3. Run Tests
Execute the tests with pytest to verify functionality:

pytest test_main.py
Notes
Ensure that the PostgreSQL service is running before starting the application.
If you encounter any errors, check the PostgreSQL logs, FastAPI logs, or test client outputs for detailed error messages.
This project uses basic FastAPI functionality combined with SQLAlchemy for database interactions. The implementation ensures robust password validation and supports testing for both the password function and profile creation API.

pip freeze > requirements.txt
uvicorn main:app --reload