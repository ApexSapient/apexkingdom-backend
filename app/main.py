from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth

app = FastAPI()

# Enable frontend communication clearly
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your authentication routes clearly
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Connected to Apex Kingdom Backend!"}