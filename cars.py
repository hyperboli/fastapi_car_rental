from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter(prefix="/cars", tags=["Cars"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    db_car = models.Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


@router.delete("/{car_id}")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    db_car = db.query(models.Car).get(car_id)
    if db_car:
        db.delete(db_car)
        db.commit()
        return {"message": "car deleted"}
    return {"error": "car not found"}