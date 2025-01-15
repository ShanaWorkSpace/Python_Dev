from schemas import StudentProfileCreate

import re
from models import StudentProfile
from sqlalchemy.orm import Session


# Password validation function
def validate_password(password: str) -> bool:
    # Check password length
    if len(password) < 8:
        return False
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    # Check for at least one numeric digit
    if not re.search(r'[0-9]', password):
        return False
    # Check for at least one special character
    if not re.search(r'[@#$%^&+=!]', password):
        return False
    return True


def create_student_profile(db: Session, profile: StudentProfileCreate):
    # No hash the password, just stored it as it is
    db_profile = StudentProfile(
        name=profile.name,
        email=profile.email,
        phone=profile.phone,
        password=profile.password  # Store as plaintext
    )
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile
