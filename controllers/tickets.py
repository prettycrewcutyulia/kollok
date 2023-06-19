from fastapi import HTTPException
from typing import List
from fastapi import APIRouter
from models.tickets import TicketIn, TicketOut
from services.tickets import TicketService

fastapi = APIRouter()


@fastapi.post("/")
def create_ticket(ticket: TicketIn):
    try:
        return TicketService.create_ticket(ticket)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@fastapi.get("/{passengerId}", response_model=List[TicketOut])
def get_tickets(passenger_id: int):
    try:
        return TicketService.get_tickets(passenger_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@fastapi.delete("/{ticketId}")
def delete_ticket(ticket_id: int):
    try:
        return TicketService.delete_ticket(ticket_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))