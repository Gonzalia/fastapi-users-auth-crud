from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from services.user_service import (
    get_users, 
    remove_user, 
    get_user_by_id,
    update_user
)
from db.session import get_db 
from schemas.user_schema import UserResponse, UserUpdate

router = APIRouter()

@router.get("/users", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return get_users(db)


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    try:
        return get_user_by_id(user_id, db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        return remove_user(user_id, db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@router.put("/users/{user_id}")
def put_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    try:
        return update_user(user_id, user_data, db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))    
