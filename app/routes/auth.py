from fastapi import APIRouter

router = APIRouter()

@router.get("/auth/google/login")
async def login():
    return {"message": "Login route"}
