from db import tickets, flights, passengers
from models.tickets import TicketIn


class TicketService:
    @staticmethod
    def create_ticket(ticket: TicketIn):
        if not tickets:
            current_index = 1
        else:
            current_index = tickets[-1]["id"] + 1
        flight_exists = False
        passenger_exists = False
        for flight in flights:
            if flight["id"] == ticket.id_flight:
                flight_exists = True
                break
        if not flight_exists:
            raise Exception("Flight not found")
        for passenger in passengers:
            if passenger["id"] == ticket.id_passenger:
                passenger_exists = True
                break
        if not passenger_exists:
            raise Exception("Passenger not found")

        current_ticket = {
            "id": current_index,
            "id_flight": ticket.id_flight,
            "id_passenger": ticket.id_passenger
        }
        tickets.append(current_ticket)

        return current_index

    @staticmethod
    def get_tickets(passenger_id: int):
        result = []
        # проверка на существование пассажира
        passenger_exists = False
        for passenger in passengers:
            if passenger["id"] == passenger_id:
                passenger_exists = True
                break
        if not passenger_exists:
            raise Exception("Passenger not found")

        for ticket in tickets:
            if ticket["id_passenger"] == passenger_id:
                result.append(ticket)
        return result

    @staticmethod
    def delete_ticket(ticket_id: int):
        for ticket in tickets:
            if ticket["id"] == ticket_id:
                tickets.remove(ticket)
                for flight in flights:
                    if flight["id"] == ticket["id_flight"]:
                        break
                return "Ticket deleted"
        raise Exception("Ticket not found")
