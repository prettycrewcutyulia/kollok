from pydantic import BaseModel, validator


class Ticket(BaseModel):
    id: int
    id_flight: int
    id_passenger: int

    @validator('id_flight')
    def id_flight_must_be_positive(cls, flight_id: int):
        if flight_id < 0:
            raise ValueError("ID рейса может быть только положительным числом")
        return flight_id

    @validator('id_passenger')
    def id_passenger_must_be_positive(cls, passenger_id: int):
        if passenger_id < 0:
            raise ValueError("ID пассажира может быть только положительным числом")
        return passenger_id


class TicketIn(BaseModel):
    id_flight: int
    id_passenger: int

    @validator('id_flight')
    def id_flight_must_be_positive(cls, flight_id: int):
        if flight_id < 0:
            raise ValueError("ID рейса может быть только положительным числом")
        return flight_id

    @validator('id_passenger')
    def id_passenger_must_be_positive(cls, passenger_id: int):
        if passenger_id < 0:
            raise ValueError("ID пассажира может быть только положительным числом")
        return passenger_id


class TicketOut(BaseModel):
    id: int
    id_flight: int

    @validator('id')
    def id_must_be_positive(cls, ticket_id: int):
        if ticket_id <= 0:
            raise ValueError("ID билета может быть только положительным числом")
        return ticket_id

    @validator('id_flight')
    def id_flight_must_be_positive(cls, flight_id: int):
        if flight_id <= 0:
            raise ValueError("ID рейса может быть только положительным числом")
        return flight_id



