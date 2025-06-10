from sqlalchemy.orm import Session
from models.user import User
from schemas.user_schema import UserResponse, UserUpdate

def get_users(db: Session): 
    users = db.query(User).all()
    return users


def get_user_by_id(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError("User not found")
    return UserResponse.from_orm(user)


def remove_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError("User not found")
    db.delete(user)
    db.commit()
    return {"msg": "User deleted successfully"}


def update_user(user_id: int, user_data: UserUpdate, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError("User not found")

    user.first_name = user_data.first_name
    user.last_name = user_data.last_name
    user.email = user_data.email
    user.birthday = user_data.birthday

    db.commit()
    db.refresh(user)
    return UserUpdate.from_orm(user)