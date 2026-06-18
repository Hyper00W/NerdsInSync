from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.models.user import User
from app.database import get_db

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    return{
        "message": "User Recieved",
        "data" : user
    }