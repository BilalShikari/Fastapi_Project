from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.middleware.sessions import SessionMiddleware
from starlette.config import Config
from routes import router as api_router
from dependencies import get_db
from models import Base
from database import engine

# Load environment variables
config = Config(".env")
SECRET_KEY = config("SECRET_KEY", cast=str, default="supersecretkey")
GOOGLE_CLIENT_ID = config("GOOGLE_CLIENT_ID", cast=str, default="")
GOOGLE_CLIENT_SECRET = config("GOOGLE_CLIENT_SECRET", cast=str, default="")
REDIRECT_URI = config("REDIRECT_URI", cast=str, default="http://localhost:8000/auth/google/callback")

# Create database tables
Base.metadata.create_all(bind=engine)

# FastAPI instance
app = FastAPI(title="Stock Watchlist API", version="1.0")

# CORS middleware setup
origins = ["http://localhost:3000", "http://localhost:8000"]  # Frontend URLs
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Session middleware (for Google OAuth)
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

# API routes
app.include_router(api_router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Project"}
