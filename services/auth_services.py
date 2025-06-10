from sqlalchemy.orm import Session
from models.user import User
from schemas.user_schema import UserResponse
from schemas.auth_schema import UserRegister, UserLogin
from passlib.context import CryptContext
from utils.access_token import create_access_token

bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user(user_data: UserRegister, db: Session):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise ValueError("Email ya registrado")
    access_token = create_access_token(data={"sub": user_data.email})
    hashed_pw = bcrypt.hash(user_data.password)
    user = User(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
        password=hashed_pw,
        birthday=user_data.birthday,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {
        "user": UserResponse.from_orm(user),
        "access_token": access_token,
        "token_type": "bearer"
    }


def login_user(user_data: UserLogin, db: Session):
    user = db.query(User).filter(User.email == user_data.email).first()
    access_token = create_access_token(data={"sub": user_data.email})

    if not user or not bcrypt.verify(user_data.password, user.password):
        raise ValueError("Invalid credentials")
    user_response = UserResponse.from_orm(user)
    return {"msg": "Login successful", "user": user_response, "access_token": access_token, "token_type": "bearer"}