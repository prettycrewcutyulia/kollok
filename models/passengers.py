from pydantic import BaseModel, validator

class Passenger(BaseModel):
    id: int
    name: str
    surname: str

    @validator('id')
    def id_must_be_positive(cls, passenger_id: int):
        if passenger_id < 0:
            raise ValueError("ID пассажира может быть только положительным числом")
        return passenger_id

    @validator('name')
    def name_must_be_str(cls, name: str):
        if not isinstance(name, str):
            raise ValueError("Имя пассажира должно быть строкой")
        return name

    @validator('surname')
    def surname_must_be_str(cls, surname: str):
        if not isinstance(surname, str):
            raise ValueError("Фамилия пассажира должна быть строкой")
        return surname


class PassengerIn(BaseModel):
    name: str
    surname: str

    @validator('name')
    def name_must_be_str(cls, name: str):
        if not isinstance(name, str):
            raise ValueError("Имя пассажира должно быть строкой")
        return name

    @validator('surname')
    def surname_must_be_str(cls, surname: str):
        if not isinstance(surname, str):
            raise ValueError("Фамилия пассажира должна быть строкой")
        return surname
