from db import flights


class FlightService:
    @staticmethod
    def get_flights():
        return flights

    @staticmethod
    def create_flight(flight):
        if not flights:
            current_index = 1
        else:
            current_index = flights[-1]["id"] + 1
        current_flight = {
            "id": current_index,
            "number": flight.number,
            "departure": flight.departure,
            "arrival": flight.arrival,
            "departure_time": flight.departure_time,
            "arrival_time": flight.arrival_time
        }
        flights.append(current_flight)
        return current_index
