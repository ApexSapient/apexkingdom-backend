from fastapi import APIRouter, HTTPException
from app.models.user import User, UserInDB
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Temporary User Storage (we'll replace this with DB later)
users_db = {}

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@router.post("/register")
async def register(user: User):
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    users_db[user.email] = UserInDB(email=user.email, hashed_password=hashed_password)
    return {"message": "User registered successfully"}

@router.post("/login")
async def login(user: User):
    db_user = users_db.get(user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"message": "Login successful"}