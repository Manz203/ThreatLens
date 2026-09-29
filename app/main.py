from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine

app = FastAPI(title="PS25 Security Alert Backend")


@app.get("/")
def root():
    return {"message": "PS25 backend is running"}


@app.get("/health/db")
def database_health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {"database": "connected"}

    except Exception as e:
        print("DATABASE ERROR:", repr(e))
        return {"database": "error"}       