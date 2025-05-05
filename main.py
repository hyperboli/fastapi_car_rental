from fastapi import FastAPI
import models
from database import engine
from users import router as users_router
from cars import router as cars_router



models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Car Rental Service")


app.include_router(users_router)

app.include_router(cars_router)
