from fastapi import FastAPI
import models
from database import engine
from users import router as users_router


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Car Rental Service")


app.include_router(users_router)
