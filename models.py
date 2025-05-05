from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)



class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True)
    brand = Column(String, nullable=False)
    price_per_hour = Column(Integer, nullable=False)



class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    car_id = Column(Integer, ForeignKey("cars.id"))
    city_id = Column(Integer, ForeignKey("city.id"))
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

    user = relationship("User")
    car = relationship("Car")