from fastapi import FastAPI
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base

app = FastAPI()

@app.get("/product/list", response_model=list[schemas.ProductOut])