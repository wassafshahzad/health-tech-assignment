from fastapi import FastAPI
from app.routers import interaction, doctor, patient

app = FastAPI()
app.include_router(interaction.router, tags=["Interactions"])
app.include_router(doctor.router, tags=["Doctors"])
app.include_router(patient.router, tags=["Patients"])


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

