from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserLogin
from app.models.user import User
from app.database import get_db

from app.core.security import hash_password, verify_password


router = APIRouter()

@router.post("/register")
def register(user:UserCreate, db:Session = Depends(get_db)):
    new_user = User(
        username = user.username,
        email = user.email,
        password = hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return{
        "message" : "User Created",
        "id" : new_user.id
    }

@router.post("/login")
def login(user: UserLogin, db:Session = Depends(get_db)):
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user is None:
        return {
            "message" : "User not Found, Login Failed!"
        }

    if not verify_password( user.password, existing_user.password):
        return {
            "message" : "Incorrect Password"
        }
    return {
        "message" : "Login Successful"
    }