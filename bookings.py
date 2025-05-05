from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import and_
from database import SessionLocal
from datetime import datetime
import models, schemas

router = APIRouter(prefix="/bookings", tags=["Car bookings"])




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/available/")
def get_available_cars(start_time: datetime, end_time: datetime, db: Session = Depends(get_db)):
    subquery = db.query(models.Booking.car_id).filter(
        and_(
            models.Booking.start_time < end_time,
            models.Booking.end_time > start_time
        )
    )
    available_cars = db.query(models.Car).filter(~models.Car.id.in_(subquery))
    return available_cars.all()


@router.get("/price/")
def calculate_price(car_id: int, start_time: datetime, end_time: datetime, db: Session = Depends(get_db)):
    car = db.query(models.Car).get(car_id)
    if not car:
        return {"error": "Cars not found"}
    duration = (end_time-start_time).total_seconds()/3600
    return {"price": round(duration * car.price_per_hour, 2)}


@router.post("/")
def book_car(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    conflicts = db.query(models.Booking).filter(
        models.Booking.car_id == booking.car_id,
        models.Booking.start_time < booking.end_time,
        models.Booking.end_time > booking.start_time
    ).first()
    if conflicts:
        return {"error": "Car is already booked for this time"}
    db_booking = models.Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


@router.delete("/{booking_id}")
def cancel_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = db.query(models.Booking).get(booking_id)
    if db_booking:
        db.delete(db_booking)
        db.commit()
        return {"message": "Booking cancelled"}
    return {"error": "Booking not found"}