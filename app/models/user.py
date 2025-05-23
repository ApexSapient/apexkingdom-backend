from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr
    password: str

class UserInDB(BaseModel):
    email: EmailStr
    hashed_password: str