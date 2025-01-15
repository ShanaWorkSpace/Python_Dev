from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, StudentProfile
from schemas import StudentProfileCreate, StudentProfileResponse
import crud

# Create the tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/profiles/", response_model=StudentProfileResponse)
def create_profile(profile: StudentProfileCreate, db: Session = Depends(get_db)):
    # Check if the email already exists
    existing_profile = db.query(StudentProfile).filter(StudentProfile.email == profile.email).first()
    if existing_profile:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Validate the password
    if not crud.validate_password(profile.password):
        raise HTTPException(status_code=400, detail="Password does not meet the requirements")

    # Create the profile in the database
    return crud.create_student_profile(db=db, profile=profile)


@app.get("/profiles/{profile_id}", response_model=StudentProfileResponse)
def read_profile(profile_id: int, db: Session = Depends(get_db)):
    db_profile = db.query(StudentProfile).filter(StudentProfile.id == profile_id).first()
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile
