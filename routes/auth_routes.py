from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.auth_schema import UserRegister, UserLogin
from services.auth_services import (
    register_user, 
    login_user, 
)
from db.session import get_db 
from utils.access_token import create_access_token

router = APIRouter()

@router.post("/auth/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    try:
        return register_user(user, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/auth/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
   try:
       return login_user(user_data, db)
   except ValueError as e:
       raise HTTPException(status_code=400, detail=str(e))