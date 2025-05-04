from fastapi import FastAPI


app = FastAPI(
    redoc_url="/redoc_test",
    docs_url="/docs",
    openapi_url="/openapi.json",
    title="car rental",
    version="1.0.0",
    description="Application for convenient car rental.",
    contact={
        "name" : "Alexandr Akulov",
        "email": "akulov.am@phystech.edu",
    },
    )


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
