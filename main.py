from fastapi import FastAPI
from controllers.tickets import fastapi as tickets_fastapi
from controllers.flights import fastapi as flights_fastapi
from controllers.passenger import fastapi as passenger_fastapi
import uvicorn

app = FastAPI()

app.include_router(tickets_fastapi, prefix="/tickets")
app.include_router(flights_fastapi, prefix="/flights")
app.include_router(passenger_fastapi, prefix="/passengers")



uvicorn.run(app, host="0.0.0.0", port=8000)