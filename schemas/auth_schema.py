from pydantic import BaseModel, EmailStr
from datetime import date


class UserRegister(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    birthday: date
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True