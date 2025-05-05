from pydantic import BaseModel
from datetime import datetime


class UserCreate(BaseModel):
    name: str



class CarCreate(BaseModel):
    brand: str
    price_per_hour: int



class BookingCreate(BaseModel):
    user_id: int
    car_id: int
    start_time: datetime
    end_time: datetime