from fastapi import APIRouter

router = APIRouter()

@router.get("/auth/google/login")
async def google_login():
    return {"message": "Redirecting to Google Login"}

@router.get("/auth/google/callback")
async def google_callback():
    return {"message": "Google Authentication Successful"}
