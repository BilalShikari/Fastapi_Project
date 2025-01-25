from fastapi import FastAPI
from app.routes import auth, watchlist

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(watchlist.router, prefix="/watchlist", tags=["Watchlist"])

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Project"}
