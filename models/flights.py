from pydantic import BaseModel, validator
from datetime import datetime


class Flight(BaseModel):
    id: int
    number: str
    departure: str
    arrival: str
    departure_time: datetime
    arrival_time: datetime

    @validator('id')
    def id_must_be_positive(cls, flight_id: int):
        if flight_id < 0:
            raise ValueError("ID рейса может быть только положительным числом")
        return flight_id

    @validator('number')
    def validate_flight_number(cls, flight_number):
        if not flight_number.isalnum():
            raise ValueError("Номер рейса может быть только из букв и цифр")
        return flight_number

    @validator('departure')
    def validate_departure(cls, departure):
        if not departure.isalpha():
            raise ValueError("Пункт отправления может быть только из букв")
        return departure

    @validator('arrival')
    def validate_arrival(cls, arrival):
        if not arrival.isalpha():
            raise ValueError("Пункт прибытия может быть только из букв")
        return arrival



class FlightIn(BaseModel):
    number: str
    departure: str
    arrival: str
    departure_time: datetime
    arrival_time: datetime

    @validator('number')
    def validate_flight_number(cls, flight_number):
        if not flight_number.isalnum():
            raise ValueError("Номер рейса может быть только из букв и цифр")
        return flight_number

    @validator('departure')
    def validate_departure(cls, departure):
        if not departure.isalpha():
            raise ValueError("Пункт отправления может быть только из букв")
        return departure

    @validator('arrival')
    def validate_arrival(cls, arrival):
        if not arrival.isalpha():
            raise ValueError("Пункт прибытия может быть только из букв")
        return arrival



