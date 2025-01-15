from pydantic import BaseModel, EmailStr


class StudentProfileCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str


class StudentProfileResponse(BaseModel):
    id: int
    name: str
    phone: str
    email: EmailStr

    class Config:
        orm_mode = True
