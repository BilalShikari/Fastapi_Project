from fastapi import APIRouter

router = APIRouter()

@router.post("/watchlist/")
async def create_watchlist():
    return {"message": "Watchlist created"}
