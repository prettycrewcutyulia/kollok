from db import passengers
from models.passengers import PassengerIn, Passenger

class PassengerService:
    @staticmethod
    def create_passenger(passenger: PassengerIn):
        if not passengers:
            current_index = 1
        else:
            current_index = passengers[-1]["id"] + 1
        current_passenger = {
            "id": current_index,
            "name": passenger.name,
            "surname": passenger.surname,
        }
        passengers.append(current_passenger)
        return current_index
