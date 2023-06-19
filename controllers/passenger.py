from fastapi import HTTPException
from fastapi import APIRouter

from models.passengers import PassengerIn
from services.passengers import PassengerService

fastapi = APIRouter()


@fastapi.post("/", response_model=int)
def create_passenger(passenger: PassengerIn):
    try:
        return PassengerService.create_passenger(passenger)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))