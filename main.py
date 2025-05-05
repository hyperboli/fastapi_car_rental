from fastapi import FastAPI
import models
from database import engine
from users import router as users_router
from cars import router as cars_router
from bookings import router as bookings_router



models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Car Rental System",
    docs_url="/docs",
    redoc_url="/redoc_test",
    version="1.0.0",
    openapi_url="/openapi.json",
    )


app.include_router(users_router)

app.include_router(cars_router)

app.include_router(bookings_router)