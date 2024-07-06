from fastapi import FastAPI
from app.routers import interaction

app = FastAPI()
app.include_router(interaction.router, tags=["Interactions"])

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

