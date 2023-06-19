from fastapi import HTTPException
from typing import List
from fastapi import APIRouter
from models.flights import Flight, FlightIn
from services.flights import FlightService

fastapi = APIRouter()


@fastapi.get("/", response_model=List[Flight])
def get_flights():
    try:
        return FlightService.get_flights()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@fastapi.post("/", response_model=int)
def create_flight(flight: FlightIn):
    try:
        return FlightService.create_flight(flight)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
