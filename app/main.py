from fastapi import Depends, FastAPI, Query
from typing import Optional
from datetime import date

from pydantic import BaseModel


app = FastAPI()


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date

class SHotel(BaseModel):
    address: str
    name: str
    stars: int

class HotelSearchArgs:
    def __init__(
            self,
            location: str,
            date_from: date, 
            date_to: date,
            stars: Optional[int] = None,
            has_spa: Optional[bool] = Query(default=None, ge=1, le=5)
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa

@app.get("/hotels/{hotel_id}")
def get_all_hotels(hotel_id: int, date_from, date_to): 
    return hotel_id, date_from, date_to

@app.get("/hotels", response_model=list[SHotel])
def get_hotels(search_args: HotelSearchArgs = Depends()): 
    hotels = [
        {
            "address": "Paper street",
            "name": "Super Hotel",
            "stars": 5
        }
    ]

    return hotels

@app.post("/bookings")
def add_booking(booking: SBooking): 
    return booking

