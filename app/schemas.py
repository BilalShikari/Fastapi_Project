from pydantic import BaseModel, EmailStr
from typing import Optional, List


# User Schema
class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None  # User's name is optional


class UserCreate(UserBase):
    google_id: str  # The Google OAuth ID


class UserResponse(UserBase):
    id: int  # Unique identifier for the user

    class Config:
        orm_mode = True


# Watchlist Schema
class WatchlistBase(BaseModel):
    symbol: str  # Stock symbol (e.g., AAPL, TSLA)
    list_name: str  # Name of the watchlist


class WatchlistCreate(WatchlistBase):
    pass  # For creation, no additional fields are required


class WatchlistUpdate(BaseModel):
    symbol: Optional[str] = None  # Allow partial updates
    list_name: Optional[str] = None


class WatchlistResponse(WatchlistBase):
    id: int  # Unique identifier for the watchlist entry
    user_id: int  # Foreign key to the User table

    class Config:
        orm_mode = True


# Response Schemas
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[EmailStr] = None
