from fastapi import FastAPI
from app.database import engine, Base
from app.models.user import User

app = FastAPI()

Base.metadata.create_all(bind=engine) #jo bhi columns user me defined honge usse according table bnayega DB me 

@app.get("/")
def home():
    return {"message": "Nerds are in sync"}